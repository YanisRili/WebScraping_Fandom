import scrapy


class ChampionsSpider(scrapy.Spider):
    name = 'champions'
    start_urls = ['https://leagueoflegends.fandom.com/wiki/List_of_champions']

    def parse(self, response):

        champion_elements = response.css('span.inline-image.label-only.champion-icon')
        for champ in champion_elements:
            raw_text = champ.css('a::text').getall()
            if raw_text:
                name = raw_text[0].strip()
                title = raw_text[1].strip() if len(raw_text) > 1 else None
            else:
                name, title = None, None

            link = champ.css('a::attr(href)').get()
            full_link = response.urljoin(link)

            yield response.follow(full_link, callback=self.parse_champion, meta={'champion_name': name, 'champion_title': title})

    def parse_champion(self, response):
        # Logique pour extraire les données spécifiques d'un champion
        name = response.meta['champion_name']
        title = response.meta['champion_title']

        base_health = response.css('span#Health_' + name + '_lvl::text').get()
        base_mana = response.css('span#ResourceBar_' + name + '_lvl::text').get()
        attack_damage = response.css('span#AttackDamage_' + name + '_lvl::text').get()

        # Gestion du cas manaless et energy
        if base_mana is None:
            base_mana = 'Manaless'
        if base_mana == '+0':
            base_mana = 'Energy'

        # Récupérer l'URL de l'image
        image_url = response.css('.pi-image-thumbnail::attr(src)').get()
        
        # Récupération des rôles (Top, Middle, etc.)
        roles = response.xpath('//div[@class="pi-data-value pi-font"]//span[contains(@class, "glossary")]//a/text()').getall()

        # Liste des rôles à conserver
        valid_roles = ["Marksman", "Support", "Top", "Middle", "Jungle"]

        # Filtrer les rôles pour ne garder que ceux qui sont valides
        roles = [role.strip() for role in roles if role.strip() in valid_roles]
        
        # Supprimer les doublons de roles en utilisant un set
        roles = list(set(roles))

        # Si aucun rôle valide n'est trouvé, on peut mettre "No Valid Role"
        if not roles:
            roles = ["No Valid Role"]

        # Renvoyer les données
        yield {
            'name': name,
            'title': title,
            'base_health': base_health.strip() if base_health else None,
            'base_mana': base_mana.strip() if base_mana else None,
            'attack_damage': attack_damage.strip() if attack_damage else None,
            'roles': roles if roles else ['No Role'],  # Si aucun rôle, mettre "No Role"
            'image_url': image_url,
        }
