import { createRouter, createWebHistory } from "vue-router";
import Home from "../components/home/home.vue";

const regFactura = () =>
  import("../components/factura/register/register.vue");

const verFactura = () =>
  import("../components/factura/ver/verfactura.vue");

const updateFactura = () => 
  import('../components/factura/edit/editfactura.vue');

const routes = [
  { path: "/facturas/all/", component: Home },
  { path: "/facturas/register/", component: regFactura },
  { path: "/facturas/mine/", component: verFactura },
  { path: "/facturas/update/:id", component: updateFactura, name: "updateFac",},
];

const history = createWebHistory();
const router = createRouter({
  history,
  routes,
});

export default router;