from django.db import models


class DiagnosticCategory(models.Model):
    """Represents a diagnostic category."""

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class DiagnosticTest(models.Model):
    """Represents a diagnostic test within a category."""

    category = models.ForeignKey(DiagnosticCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    duration = models.CharField(max_length=50)
    cost = models.CharField(max_length=50)

    def __str__(self):
        return self.name
