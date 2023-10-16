class Guest:
    def __init__(self, passport, name, country):
        self._passport = passport
        self._name = name
        self._country = country
        self._blacklistedReason = []

    @property
    def passport(self):
        return self._passport

    @property
    def name(self):
        return self._name

    @property
    def country(self):
        return self._country

    def isBlacklisted(self):
        return bool(self._blacklistedReason)

    def blacklist(self, dateReported, reason):
        self._blacklistedReason.append([dateReported, reason])

    def __str__(self):
        blacklisting = ""
        if self.isBlacklisted():
            for date, reason in self._blacklistedReason:
                blacklisting += f"\n{date}: {reason}"
        return f"Passport Number: {self.passport}\nName: {self.name}\nCountry: {self._country}{blacklisting}"
