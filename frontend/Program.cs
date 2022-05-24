using Microsoft.AspNetCore.Components.Web;
using Microsoft.AspNetCore.Components.WebAssembly.Hosting;
using MudBlazor.Services;
using frontend;

var builder = WebAssemblyHostBuilder.CreateDefault(args);
builder.RootComponents.Add<App>("#app");
builder.RootComponents.Add<HeadOutlet>("head::after");

Uri baseaddress;
if (builder.HostEnvironment.IsDevelopment())
    baseaddress = new Uri(builder.Configuration["ApiBaseAddress"]);
else
    baseaddress = new Uri(builder.HostEnvironment.BaseAddress);
builder.Services.AddScoped(sp => new HttpClient { BaseAddress = baseaddress });
builder.Services.AddSingleton<ConfigReader>();
builder.Services.AddMudServices();

await builder.Build().RunAsync();
