import dns.resolver
import logging

logging.basicConfig(filename="dns_log.txt", level=logging.INFO)

domain = "example.com"
records = ['A', 'MX', 'CNAME']

for r in records:
    try:
        result = dns.resolver.resolve(domain, r)
        for val in result:
            print(f"{r} Record: {val.to_text()}")
            logging.info(f"{r} Record: {val.to_text()}")
            
    except dns.resolver.NoAnswer:
        print(f"No {r} record found for {domain}")
        logging.info(f"No {r} record found for {domain}")
    except dns.resolver.NXDOMAIN:
        print(f"Domain {domain} does not exist")
        logging.info(f"Domain {domain} does not exist")
    except Exception as e:
        print(f"Error resolving {r} record for {domain}: {e}")
        logging.error(f"Error resolving {r} record for {domain}: {e}")

