/**
 * Created by ylfa on 13/03/2017.
 */
var app = angular.module("app", []);

app.controller("AppCtrl", function ($http) {
    var app = this;

    app.message = "Am I working?";

    $http.get("/api/farm_names").success(function (data) {
        app.farm_names = data.objects;
    });

    app.addNew = function() {
        $http.post("api/farm_names",{"id":app.farm_names.length+1,"area_name":"NewArea"})
            .success(function (data) {
            app.farm_names.push(data);
        })
    }
});