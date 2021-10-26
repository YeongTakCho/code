import cfscrape

scraper = cfscrape.create_scraper()
r = scraper.get("https://bbaggome.com/yajjal_board?page=1")
r.status_code  # 200

print(r.content.decode('utf-8'))