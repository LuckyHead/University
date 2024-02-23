from django.db.models import *
from university.models import University
from faculty_fields.models import(
    Tuition_language,
    Education_form,
    Subject
)

class Faculty(Model):
    university=ForeignKey(
        University,
        verbose_name='University',
        on_delete=CASCADE
    )

    name=CharField(
        'Faculty',
        max_length=256
    )

    tuition_language=ManyToManyField(
        Tuition_language,
        verbose_name='Tuition language'
    )

    education_form=ManyToManyField(
        Education_form,
        verbose_name='Education form'
    )

    acceptance=PositiveSmallIntegerField(
        'Acceptance number'
    )

    grand=DecimalField(
        'Grand score',
        decimal_places=1,
        blank=True,
        null=True,
        max_digits=4
    )

    contract=DecimalField(
        'Contract score',
        decimal_places=1,
        blank=True,
        null=True,
        max_digits=4
    )

    first_subject=ForeignKey(
        Subject,
        verbose_name='First subject',
        on_delete=CASCADE,
        related_name='faculty_first_subject'
    )

    second_subject=ForeignKey(
        Subject,
        verbose_name='Second subject',
        on_delete=CASCADE,
        related_name='faculty_second_subject'
    )


    class Meta:
        verbose_name='Faculty'
        verbose_name_plural='Faculties'