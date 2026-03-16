from django.conf import settings
from django.db import models
from django.urls import reverse


class PropertyType(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        verbose_name = "tipo de imóvel"
        verbose_name_plural = "tipos de imóvel"

    def __str__(self):
        return self.nome


class Property(models.Model):
    TIPO_ANUNCIO = (
        ("venda", "Venda"),
        ("aluguel", "Aluguel"),
    )
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    descricao = models.TextField(blank=True)
    tipo_anuncio = models.CharField(max_length=10, choices=TIPO_ANUNCIO, default="venda")
    tipo_imovel = models.ForeignKey(
        PropertyType, on_delete=models.SET_NULL, null=True, related_name="imoveis"
    )
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=10, blank=True)
    area_m2 = models.PositiveIntegerField(null=True, blank=True, verbose_name="Área (m²)")
    quartos = models.PositiveSmallIntegerField(default=0)
    banheiros = models.PositiveSmallIntegerField(default=0)
    vagas = models.PositiveSmallIntegerField(default=0, verbose_name="Vagas garagem")
    valor = models.DecimalField(max_digits=14, decimal_places=2)
    ativo = models.BooleanField(default=True)
    destaque = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    anunciante = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="imoveis_anunciados",
    )

    class Meta:
        verbose_name = "imóvel"
        verbose_name_plural = "imóveis"
        ordering = ["-criado_em"]

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("properties:detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            base = slugify(self.titulo)[:200]
            slug = base
            n = 0
            while Property.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                n += 1
                slug = f"{base}-{n}"[:220]
            self.slug = slug
        super().save(*args, **kwargs)


class PropertyImage(models.Model):
    imovel = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name="imagens"
    )
    imagem = models.ImageField(upload_to="imoveis/%Y/%m/")
    ordem = models.PositiveSmallIntegerField(default=0)
    legenda = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = "imagem"
        verbose_name_plural = "imagens"
        ordering = ["ordem", "id"]

    def __str__(self):
        return f"{self.imovel.titulo} – #{self.ordem}"
