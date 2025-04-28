from pymisp import MISPEvent, MISPObject, PyMISP, ExpandedPyMISP
import urllib
url_blist = "https://reputation.serpro.gov.br/"
misp_key = "PUT YOUR API_KEY HERE"
misp_url = "https://SEU_MISP/"
misp_verify_cert = False
blist = urllib.request.urlopen(url_blist)
misp = ExpandedPyMISP(misp_url, misp_key, misp_verify_cert)
event = MISPEvent()
event.info = "Blocklisted IP"
event.analysis = "1"
event.threat_level_id = "1"
event.distribution = "1"
event.add_tag('tlp:green')
event.add_tag('ip_blocklist')
event.add_tag('osint:source-type="block-or-filter-list"')
for i in blist:
	ip = str(i.decode("utf-8").replace('\n',''))
	event.add_attribute('ip-dst', str(ip), comment="Blocklisted IP by Serpro", disable_correlation=False, to_ids=True)
event.published = True
event = misp.add_event(event)
