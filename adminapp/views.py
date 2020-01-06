from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from adminapp.forms import ShopUserAdminCreateForm, ShopUserAdminUpdateForm, ProductCategoryAdminUpdateForm, \
    ProductAdminUpdateForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


class ShopUserListView(ListView):
    model = ShopUser
    # template_name = 'adminapp/index.html'
    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'панель администратора'
        return context


# @user_passes_test(lambda x: x.is_superuser)
# def index(request):
#     object_list = ShopUser.objects.all()
#
#     context = {
#         'page_title': 'Панель администратора',
#         'object_list': object_list,
#     }
#     return render(request, 'adminapp/index.html', context)


@user_passes_test(lambda x: x.is_superuser)
def shopuser_create(request):
    if request.method == 'POST':
        form = ShopUserAdminCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myadmin:index'))
    else:
        form = ShopUserAdminCreateForm()
    context = {
        'page_title': 'Создание пользователя',
        'form': form,
    }
    return render(request, 'adminapp/shopuser_create.html', context)


@user_passes_test(lambda x: x.is_superuser)
def shopuser_update(request, pk):
    user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        form = ShopUserAdminUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myadmin:index'))
    else:
        form = ShopUserAdminUpdateForm(instance=user)
    context = {
        'page_title': 'редактирование пользователя',
        'form': form,
    }
    return render(request, 'adminapp/shopuser_create.html', context)


@user_passes_test(lambda x: x.is_superuser)
def shopuser_delete(request, pk):
    # get_object_or_404(ShopUser, pk=pk).delete()
    # return HttpResponseRedirect(reverse('adminapp:index'))
    user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('myadmin:index'))
    elif request.method == 'GET':
        context = {
            'page_title': 'удаление пользователя',
            'object': user,
        }
        return render(request, 'adminapp/shopuser_delete.html', context)


@user_passes_test(lambda x: x.is_superuser)
def productcategory_list(request):
    object_list = ProductCategory.objects.all()

    context = {
        'page_title': 'категории товаров',
        'object_list': object_list,
    }
    return render(request, 'adminapp/productcategory_list.html', context)


class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    success_url = reverse_lazy('myadmin:productcategory_list')
    # fields ='__all__'
    form_class = ProductCategoryAdminUpdateForm
    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'создание категории'
        return context


# @user_passes_test(lambda x: x.is_superuser)
# def productcategory_create(request):
#     if request.method == 'POST':
#         form = ProductCategoryAdminUpdateForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('myadmin:productcategory_list'))
#     else:
#         form = ProductCategoryAdminUpdateForm()
#     context = {
#         'page_title': 'создание категории',
#         'form': form,
#     }
#     return render(request, 'adminapp/productcategory_create.html', context)


class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    success_url = reverse_lazy('myadmin:productcategory_list')
    form_class = ProductCategoryAdminUpdateForm
    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'изменение категории'
        return context


# @user_passes_test(lambda x: x.is_superuser)
# def productcategory_update(request, pk):
#     productcategory = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == 'POST':
#         form = ProductCategoryAdminUpdateForm(request.POST, request.FILES, instance=productcategory)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('myadmin:productcategory_list'))
#     else:
#         form = ProductCategoryAdminUpdateForm(instance=productcategory)
#     context = {
#         'page_title': 'изменение категории',
#         'form': form,
#     }
#     return render(request, 'adminapp/productcategory_create.html', context)


class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    success_url = reverse_lazy('myadmin:productcategory_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'удаление категории'
        return context


# @user_passes_test(lambda x: x.is_superuser)
# def productcategory_delete(request, pk):
#     productcategory = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == 'POST':
#         productcategory.is_active = False
#         productcategory.save()
#         return HttpResponseRedirect(reverse('myadmin:productcategory_list'))
#     elif request.method == 'GET':
#         context = {
#             'page_title': 'удаление категории',
#             'object': productcategory,
#         }
#         return render(request, 'adminapp/productcategory_delete.html', context)


@user_passes_test(lambda x: x.is_superuser)
def productcategory_products(request, pk):
    productcategory = get_object_or_404(ProductCategory, pk=pk)
    context = {
        'page_title': 'товары категории',
        'productcategory': productcategory,
        'object_list': productcategory.product_set.all(),
    }
    return render(request, 'adminapp/product_list.html', context)


@user_passes_test(lambda x: x.is_superuser)
def product_create(request, pk):
    productcategory = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        form = ProductAdminUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myadmin:productcategory_products', kwargs={'pk':pk}))
    else:
        form = ProductAdminUpdateForm(initial={'category': productcategory})
    context = {
        'page_title': 'создание товара',
        'form': form,
    }
    return render(request, 'adminapp/product_create.html', context)


@user_passes_test(lambda x: x.is_superuser)
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductAdminUpdateForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myadmin:productcategory_products',
                                                kwargs={'pk':product.category.pk}))
    else:
        form = ProductAdminUpdateForm(instance=product)
    context = {
        'page_title': 'редактирование товара',
        'form': form,
        'product': product,
    }
    return render(request, 'adminapp/product_update.html', context)


@user_passes_test(lambda x: x.is_superuser)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.is_active = False
        product.save()
        return HttpResponseRedirect(reverse('myadmin:productcategory_products',
                                            kwargs={'pk': product.category.pk}))
    elif request.method == 'GET':
        context = {
            'page_title': 'удаление товара',
            'object': product,
        }
        return render(request, 'adminapp/product_delete.html', context)


class ProductDetailView(DetailView):
    model = Product

    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'карточка товара'
        return context


# @user_passes_test(lambda x: x.is_superuser)
# def product_read(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {
#         'page_title': 'карточка товара',
#         'object': product,
#     }
#     return render(request, 'adminapp/product_read.html', context)