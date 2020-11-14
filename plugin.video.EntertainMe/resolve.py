# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'aW1wb3J0IHJlLCByZXF1ZXN0cywganNvbiwgb3MNaW1wb3J0IHhibWNndWkNaW1wb3J0IHhibWMNaW1wb3J0IHJhbmRvbQ1kaWFsb2cgPSB4Ym1jZ3VpLkRpYWxvZygpDWltcG9ydCB4Ym1jYWRkb24NaW1wb3J0IHJlc29sdmV1cmwNZnJvbSBiczQgaW1wb3J0IEJlYXV0aWZ1bFNvdXANX2FkZG9uX2lkXyA9ICdwbHVnaW4udmlkZW8uRW50ZXJ0YWluTWUnDUFkZG9uVGl0bGUgPSAnW0JdW0NPTE9SIHJlZF1FW0NPTE9SIHllbGxvd11udGVydGFpbiBNZVsvQl1bL0NPTE9SXScNQWRkb25pY29uICA9IHhibWMudHJhbnNsYXRlUGF0aChvcy5wYXRoLmpvaW4oJ3NwZWNpYWw6Ly9ob21lL2FkZG9ucy8nICsgX2FkZG9uX2lkXywgJ2ljb24ucG5nJykpDWNsYXNzIEpzVW5wYWNrZXJWMjoNCWRlZiB1bnBhY2tBbGwoc2VsZiwgZGF0YSk6DQkJdHJ5Og0JCQlpbl9kYXRhPWRhdGENCQkJc1BhdHRlcm4gPSAnKGV2YWxcXChmdW5jdGlvblxcKHAsYSxjLGssZSwuKiknDQkJCWVuY19kYXRhPXJlLmNvbXBpbGUoc1BhdHRlcm4pLmZpbmRhbGwoaW5fZGF0YSkNCQkJZm9yIGVuY192YWwgaW4gZW5jX2RhdGE6DQkJCQl0cnk6DQkJCQkJdW5wYWNrX3ZhbD1zZWxmLnVucGFjayhlbmNfdmFsKQ0JCQkJCWluX2RhdGE9aW5fZGF0YS5yZXBsYWNlKGVuY192YWwsdW5wYWNrX3ZhbCkNCQkJCWV4Y2VwdDoNCQkJCQlwYXNzDQkJCXJldHVybiBpbl9kYXRhDQkJZXhjZXB0OiANCQkJdHJhY2ViYWNrLnByaW50X2V4YyhmaWxlPXN5cy5zdGRvdXQpDQkJCXJldHVybiBkYXRhDQlkZWYgY29udGFpbnNQYWNrZWQoc2VsZiwgZGF0YSk6DQkJcmV0dXJuICgnU3RyaW5nLmZyb21DaGFyQ29kZShjKzI5KScgaW4gZGF0YSBhbmQgJ3AsYSxjLGsnIGluIGRhdGEpDQlkZWYgdW5wYWNrKHNlbGYsIHNKYXZhc2NyaXB0LGl0ZXJhdGlvbj0xLCB0b3RhbGl0ZXJhdGlvbnM9MSk6DQkJYVNwbGl0ID0gc0phdmFzY3JpcHQuc3BsaXQoInJuIHB9KCciKQ0JCXAxLGExLGMxLGsxPSgnJywnMCcsJzAnLCcnKQ0JCXNzPSJwMSxhMSxjMSxrMT0oXCciK2FTcGxpdFsxXS5zcGxpdCgiLnNwbGkiKVswXSsnKScgDQkJZXhlYyhzcykNCQlrMT1rMS5zcGxpdCgnfCcpDQkJYVNwbGl0ID0gYVNwbGl0WzFdLnNwbGl0KCIpKSciKQ0JCWUgPSAnJw0JCWQgPSAnJyMzMjgyMw0JCXNVbnBhY2tlZDEgPSBzdHIoc2VsZi5fX3VucGFjayhwMSwgYTEsIGMxLCBrMSwgZSwgZCxpdGVyYXRpb24pKQ0JCWlmIGl0ZXJhdGlvbj49dG90YWxpdGVyYXRpb25zOg0JCQlyZXR1cm4gc1VucGFja2VkMQ0JCWVsc2U6DQkJCXJldHVybiBzZWxmLnVucGFjayhzVW5wYWNrZWQxLGl0ZXJhdGlvbisxKQ0JZGVmIF9fdW5wYWNrKHNlbGYscCwgYSwgYywgaywgZSwgZCwgaX'
love = 'EypzS0nJ9hYUL9ZFx6QDxWq2ucoTHtXTZtCw0tZFx6QDxWPJZtCFOwVP0kQDxWPJyzVPueJ2AqXGbAPDxWPJSuCKA0pvumMJkzYy9snKEiLH5yqluwYPOuXFxAPDxWPKN9pzHhp3IvXPqpKTVaVPftLJRtXlqpKTVaYPOeJ2AqYPOjXFZtIRuWHlOWHlOPoT9iMUxtp2kiqlRAPDylMKE1pz4tpN0WMTIzVS9snKEiLFumMJkzYT51oFjtpzSxnKtcBt0WPKWyp3IfqPN9VPVvQDxWnJLtoaIgCG0jBvOlMKE1pz4tWmNaQDxWq2ucoTHtoaIgVQ4tZQbAPDxWpzImqJk0VQ0tVwNkZwZ0AGL3BQyuLzAxMJManTydn2kgoz9jpKWmqUI2q3u5rvWooaIgVPHtpzSxnKuqVPftpzImqJk0QDxWPJ51oFNiCFOlLJEcrN0WPKWyqUIlovOlMKA1oUDAPJEyMvOsK2y0o2SBMKpbp2IfMvkwLljtLFx6QDxWLJR9VvVtnJLtL2ZtCPOuVTIfp2Htp2IfMv5sK2y0o2SBMKpbnJ50XTAwVP8tLFxfLFxtQDxWL2ZtCFNbL2ZtWFOuXD0WPJWvCJAbpvuwLlNeVQV5XFOcMvOwLm4tZmHtMJkmMFOmqUVbp2IfMv5sK2y0o2RbL2ZfZmLcXD0WPKWyqUIlovOuLFgvLt1xMJLtFJ5xMKtbMaWuoJHfnJAiozygLJqyXGbAPDyxnJSfo2phoz90nJMcL2S0nJ9hXRSxMT9hITy0oTHfVPqoD09ZG1VtrJIfoT93KHqyqUEcozptGTyhn3ZtDzHtHTS0nJIhqSfiD09ZG1WqWljtDJExo25cL29hYPNkZQNjZPjtEzSfp2HcQDxWnTIuMTIlplN9VUfaIKAypv1OM2IhqPp6VPqAo3ccoTkuYmHhZPNbI2yhMT93plOBIPNkZP4jBlOKnJ42AQftrQL0XFOOpUOfMIqyLxgcqP81ZmphZmLtXRgVIR1ZYPOfnJgyVRqyL2giXFOQnUWioJHiAwNhZP4mZGRlYwRkZlOGLJMupzxiAGZ3YwZ2W30APDyfnJ5eVQ0tpzIkqJImqUZhM2I0XTMlLJ1yYTSfoT93K3WyMTylMJA0pm1TLJkmMFjtnTIuMTIlpm1bMJSxMKWmXD0WPJMlLJ1yVQ0toTyhnl5bMJSxMKWmJlqZo2AuqTyiovqqQDxWqUW5Bt0WPDymqUWyLJ11pzjtCFOoKFN7VUA0pzIuoJ5uoJHtCFOoKD0WPDyfnJ5eplN9VQNAPDxWnaAIZvN9VRcmIJ5jLJAeMKWJZvtcQDxWPJuyLJEypaZtCFO7W1ImMKVgDJqyoaDaBvNaGJ96nJkfLF81YwNtXSqcozEiq3ZtGyDtZGNhZQftI2yhAwD7VUt2APxtDKOjoTIKMJWYnKDiAGZ3YwZ2VPuYFSEAGPjtoTyeMFOUMJAeolxtD2ulo21yYmLjYwNhZmRkZv4kZGZtH2SzLKWcYmHmAl4mAvpfQDxWPDxWPFqFMJMypzIlWlN6VTMlLJ1ysD0WPDyxLKEuVQ0trlqlMJMypzIlWlN6VPqmMJIbMP5hoPpfQDxWPDxWW3OfLKxaVQbtWmVmZGDmZGZ1AQDlAQZ1ZwZ1AGZ0ZwVmAQDkW30APDxWDzSmMFN9VPqbqUEjpmbiY3OfLKxhZGVmMzyfMKZhL2k1LvpAPDxWL29hqTIhqPN9VUWypKIyp3EmYaOip3DbMaWuoJHfMTS0LG1xLKEuYTuyLJEypaZ9nTIuMTIlplxhqTI4qN0WPDymo3IjVQ0t'
god = 'QmVhdXRpZnVsU291cChjb250ZW50LCdodG1sLnBhcnNlcicpDQkJCXIgPSBzb3VwLmZpbmRfYWxsKCdkaXYnLCBjbGFzc189eydzb3VyY2UnfSkNCQkJZm9yIGkgaW4gcjoNCQkJCXRpdGxlID0gaS50ZXh0DQkJCQlzb3VyY2UgPSBpWydkYXRhLWlkJ10NCQkJCSN4Ym1jLmxvZygnU09VUkNFIDo6Oicrc3RyKHNvdXJjZSkseGJtYy5MT0dOT1RJQ0UpDQkJCQlpZiBzb3VyY2Uuc3RhcnRzd2l0aCgnLy9wbGF5LjEyM2ZpbGVzLmNsdWIvJyk6IHNvdXJjZSA9ICdodHRwczonICsgc291cmNlDQkJCQllbGlmIHNvdXJjZS5zdGFydHN3aXRoKCcvPycpOiBzb3VyY2U9QmFzZStzb3VyY2UNCQkJCXhibWMubG9nKCdMSU5LIDo6Oicrc3RyKHNvdXJjZSkseGJtYy5MT0dOT1RJQ0UpDQkJCQkjaWYgbm90IEJhc2UgaW4gc291cmNlOiBzb3VyY2U9QmFzZStzb3VyY2UNCQkJCWhlYWRlcnMgPSB7J1VzZXItQWdlbnQnOiAnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzYwLjAuMzExMi4xMTMgU2FmYXJpLzUzNy4zNicsDQkJCQkJCSdSZWZlcmVyJyA6IHNvdXJjZX0NCQkJCWRhdGEgPSByZXF1ZXN0cy5nZXQoc291cmNlLGhlYWRlcnM9aGVhZGVycykudGV4dA0JCQkJI3hibWMubG9nKCdMSU5LIDo6Oicrc3RyKHNvdXJjZSkseGJtYy5MT0dOT1RJQ0UpDQkJCQkjeGJtYy5sb2coJ0RBVEEgOjo6JytzdHIoZGF0YSkseGJtYy5MT0dOT1RJQ0UpDQkJCQlpID0gMA0JCQkJdHJ5Og0JCQkJCXdoaWxlIGpzVTIuY29udGFpbnNQYWNrZWQoZGF0YSk6DQkJCQkJCWRhdGEgPSBqc1UyLnVucGFja0FsbChkYXRhKQ0JCQkJCQlpICs9IDENCQkJCQkJaWYgaSA9PSAzOiByYWlzZSBFeGNlcHRpb24oKSANCQkJCWV4Y2VwdDogcGFzcw0JCQkJdHJ5Og0JCQkJCXNvdXJjZSA9IHJlLmZpbmRhbGwocicnJ2ZpbGU6WyciXShodHRwLio/KVsnIl0nJycsZGF0YSxmbGFncz1yZS5ET1RBTEwpWzBdLnJlcGxhY2UoJ1xcJywnJykNCQkJCQkjZGlhbG9nLm9rKCJTb3VyY2UiLHN0cihzb3VyY2UpKQ0JCQkJCWxpbmtzICs9IDENCQkJCQlzb3VyY2UgPSAoJyVzfFVzZXItQWdlbnQ9TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzcyLjAuMzYyNi4xMjEgU2FmYXJpLzUzNy4zNicgJSBzb3VyY2UpDQkJCQkJdGl0bGUgPSAoJ0xpbmsgJXMgfCBGSEQgfCBESVJFQ1QnICUgbGlua3MpDQkJCQkJc3RyZWFtdXJsLmFwcGVuZChzb3VyY2UpDQkJCQkJc3RyZWFtbmFtZS5hcHBlbmQodGl0bGUpDQkJCQlleGNlcHQ6DQkJCQ'
destiny = 'xWqUW5Bt0WPDxWPDyWMaWuoJIVqJ50VQ0tpzHhMzyhMTSfoPulWlpaCTyzpzSgMF4dC3AlLm1oWlWqXP4dClyoWlWqWlpaYTEuqTRfMzkuM3Z9pzHhER9HDHkZXIfjKD0WPDxWPDxwMTyuoT9aYz9eXPWGo3IlL2HvYUA0pvuWMaWuoJIVqJ50XFxAPDxWPDxWnJLtFJMlLJ1yFUIhqP5mqTSlqUA3nKEbXPpiY2Eio2DaXFN6VTAioaEcoaIyQDxWPDxWPJIfnJLtFJMlLJ1yFUIhqP5mqTSlqUA3nKEbXPpipTkurFpcVQbtL29hqTyhqJHAPDxWPDxWnT1zVQ0tpzImo2k2MKIloP5Vo3A0MJEAMJEcLHMcoTHbFJMlLJ1yFUIhqPxAPDxWPDxWnJLtnT1zYaMuoTyxK3IloPtcBt0WPDxWPDxWoTyhn3ZtXm0tZD0WPDxWPDxWqTy0oTHtCFNbW0kcozftWKZtXPOFMKAioUMyVSIloPNcVUjtExuRWlNyVTkcozgmXD0WPDxWPDxWp3ElMJSgqKWfYzSjpTIhMPuWMaWuoJIVqJ50XD0WPDxWPDxWp3ElMJSgozSgMF5upUOyozDbqTy0oTHcQDxWPDxWMKuwMKO0BvOjLKAmQDxWPKAyoTIwqPN9VTEcLJkiMl5mMJkyL3DbW0Abo3AyVRRtGTyhnlpfp3ElMJSgozSgMFxAPDxWnJLtp2IfMJA0VQjtZQbtpKIcqPtcQDxWPKIloPN9VUA0pzIuoKIloSgmMJkyL3EqQDxWPJ5uoJHtCFOmqUWyLJ1hLJ1yJ3AyoTIwqS0APDxWnJLtpzImo2k2MKIloP5Vo3A0MJEAMJEcLHMcoTHbqKWfXF52LJkcMS91pzjbXGbAPDxWPJEcLJkiMl5ho3EcMzywLKEco24bDJExo25HnKEfMFjtW1gQG0kCHvO5MJkfo3qqH291pzAcozptJJ91pvOAMJEcLIfiD09ZG1WqWljtDJExo25cL29hYPNlAGNjXD0WPDxWp3ElMJSgK3IloPN9VUWyp29fqzI1pzjhFT9mqTIxGJIxnJSTnJkyXUIloPxhpzImo2k2MFtcQDxWPDyfnKbtCFO4Lz1wM3IcYxkcp3EWqTIgXT5uoJHfnJAioxygLJqyCJywo25coJSaMFjtqTu1oJWhLJyfFJ1uM2H9nJAiozygLJqyXD0WPDxWoTy6YaAyqSOuqTtbp3ElMJSgK3IloPxAPDxWPKuvoJZhHTkurJIlVPtcYaOfLKxbp3ElMJSgK3IloPjtoTy6YPOTLJkmMFxAPDxWMJkmMGbAPDxWPJEcLJkiMl5ho3EcMzywLKEco24bDJExo25HnKEfMFjtW1gQG0kCHvO5MJkfo3qqH291pzAcozptJJ91pvOAMJEcLIfiD09ZG1WqWljtDJExo25cL29hYPNlAGNjXD0WPDxWp3ElMJSgK3IloQ11pzjAPDxWPJkcrvN9VUuvoJAaqJxhGTymqRy0MJ0bozSgMFkcL29hFJ1uM2H9nJAiozygLJqyYPO0nUIgLz5unJkWoJSaMG1cL29hnJ1uM2HcQDxWPDyfnKbhp2I0HTS0nPumqUWyLJ1sqKWfXD0WPDxWrTWgLl5DoTS5MKVtXPxhpTkurFumqUWyLJ1sqKWfYPOfnKbfVRMuoUAyXD0WPJI4L2IjqPOSrTAypUEco24tLKZtLmbAPDxWrTWgLl5fo2pbVyAQHxSDEIVtEIWFG1VtHzImo2k2MKVtVQb6BvNyplVtWJZtYPOfMKMyoQ14Lz1wYxkCE05CIRyQEFx='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))