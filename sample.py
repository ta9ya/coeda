import coeda
import settings


nlp = coeda.auth(settings.cotoha_client_id, settings.cotoha_client_secret,
                 settings.cotoha_access_token_publish_url)
tokenizer = nlp('今日のライブは楽しみだ')
print(tokenizer.chunks)
print(tokenizer.tokens)
