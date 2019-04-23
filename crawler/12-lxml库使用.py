from lxml import etree

text = """

<!DOCTYPE html>
<html>
<head>
    <!-- meta -->
    <meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
<meta name="renderer" content="webkit">
<meta property="qc:admins" content="23635710066417756375" />
<meta name="baidu-site-verification" content="QIQ6KC1oZ6" />

<meta content="找工作,招聘网,招聘信息,互联网招聘" name="keywords">

<meta content="找工作,招聘网,求职网,互联网招聘,拉勾网是互联网领域垂直招聘网站,互联网职业机会尽在拉勾网" name="description">

<title>找工作-互联网招聘求职网-拉勾网</title>

<link rel="Shortcut Icon" href="//www.lgstatic.com/www/static/common/static/favicon_faed927.ico">



    <!-- header/global_domain FE_base.. -->
    
<script type="text/javascript">

(function() {
    var protocol = window.location.protocol;
    var host = window.location.host;
    var baseUrl = protocol + '//' + host;

    window.GLOBAL_DOMAIN = window.GLOBAL_DOMAIN || {
        ctx: 'https://www.lagou.com',
        rctx: 'https://hr.lagou.com',
        crctx: 'https://hr.lagou.com/company',
        pctx: 'https://passport.lagou.com',
        actx: 'https://account.lagou.com',
        cpctx: 'https://xiaoyuan.lagou.com',
        acctx: 'https://activity.lagou.com',
        paictx: 'https://pai.lagou.com',
        sctx: 'https://suggest.lagou.com',
        zctx: 'https://yanzhi.lagou.com',
        ectx: 'https://easy.lagou.com',
        proctx: 'https://pro.lagou.com',
        lgsctx: protocol + '//www.lgstatic.com',
        FE_frontLogin: baseUrl + '/frontLogin.do',
        FE_frontLogout: baseUrl + '/frontLogout.do',
        FE_frontRegister: baseUrl + '/frontRegister.do'
    };

    window.GLOBAL_CDN_DOMAIN = 'www.lgstatic.com';

    var CONST_VARS = window.CONST_VARS = (function() {
        var varsCache = {};
        var user;
                    varsCache.user = user = {};
        
    var _hasOwnProperty = Object.prototype.hasOwnProperty;
    var _toString = Object.prototype.toString;

    return function (key) {
        var ret = {};
        var src = varsCache[key];
        if (_toString.call(src) === '[object Object]') {
            for (var prop in src) {
                if (_hasOwnProperty.call(src, prop)) {
                    ret[prop] = src[prop];
                }
            }
        } else {
            ret = src;
        }

        return ret;
    }

    })();
})();
</script>



    
    
    <!-- 公共样式 -->    <!-- header样式 -->    <!-- footer样式 -->
    <!-- 页面样式 -->    
    <!-- 动态token，防御伪造请求，重复提交 -->
    <script type="text/javascript">
    window.X_Anti_Forge_Token = '';
    window.X_Anti_Forge_Code = '';
</script>


    <link rel="stylesheet" type="text/css" href="//www.lgstatic.com/www/static/dep/mCustomScrollbar/css/mCustomScrollbar_ac2fb8b.css" />
    <link rel="stylesheet" type="text/css" href="//www.lgstatic.com/www/static/pkg/layout_cb75ea0.css" />
    <link rel="stylesheet" type="text/css" href="//www.lgstatic.com/www/static/pkg/search-result/page/index/main.html_aio_57e8c9c.css" />
    <link rel="stylesheet" type="text/css" href="//www.lgstatic.com/www/static/pkg/widgets_1a33497.css" />
    <link rel="stylesheet" type="text/css" href="//www.lgstatic.com/www/static/pkg/search-result/page/index/main.html_aio_2_fe924e1.css" />
</head>
<body>
    
    <!-- header -->
    	<!--C端头部通栏广告位-->
	

	<!--验证注册邮箱-->
	<!--
    @require "common/widgets/header_c/modules/emailvalid/main.less"
-->


	<div id="lg_header">

		<!--C端头部黑色导航-->
			<div id="lg_tbar">

		<div class="inner">

			<div class="lg_tbar_l">
				<a rel="nofollow" href="https://www.lagou.com/app/download.html" class="lg_app" data-lg-tj-id="5500" data-lg-tj-no="idnull" data-lg-tj-cid="idnull" target="_blank">拉勾APP</a>
				<a rel="nofollow" href="https://easy.lagou.com/dashboard/index.htm?from=c_index" class="lg_os" data-lg-tj-id="5600" data-lg-tj-no="idnull" data-lg-tj-cid="idnull" data-lg-tj-track-code="index_qiyeban">进入企业版</a>
			</div>

			
			<ul class="lg_tbar_r">
				<li>
					<a href="/frontLogin.do" data-lg-tj-id="5f00" data-lg-tj-no="idnull" data-lg-tj-cid="idnull" rel="nofollow">登录</a>
				</li>
				<li>
					<a href="/frontRegister.do" class="bl" data-lg-tj-id="5g00" data-lg-tj-no="idnull" data-lg-tj-cid="idnull" rel="nofollow">注册</a>
				</li>
			</ul>

			
		</div>

	</div><!--end #lg_tbar-->


		<!--C端头部白色导航-->
			<div id="lg_tnav">

		<div class="inner">
			<div class="lg_tnav_l">
				<a href="https://www.lagou.com/" class="lg_logo" data-lg-tj-id="5h00" data-lg-tj-no="idnull" data-lg-tj-cid="idnull">
					<h1>拉勾网</h1>
				</a>

				
							</div>
			<ul class="lg_tnav_wrap">
				<li>
					<a href="https://www.lagou.com/"  data-lg-tj-id="5i00" data-lg-tj-no="idnull" data-lg-tj-cid="idnull">首页</a>
				</li>
				<li>
					<a href="https://www.lagou.com/gongsi/"  data-lg-tj-id="5j00" data-lg-tj-no="idnull" data-lg-tj-cid="idnull" data-lg-tj-track-code="index_company">公司</a>
				</li>
				<li>
					<a rel="nofollow" href="https://xiaoyuan.lagou.com/" data-lg-tj-id="19xc" data-lg-tj-no="idnull" data-lg-tj-cid="idnull" target="_blank" data-lg-tj-track-code="index_campus">校园</a>
				</li>
				<li>
					<a rel="nofollow" href="https://yanzhi.lagou.com/"  data-lg-tj-id="ic00" data-lg-tj-no="idnull" data-lg-tj-cid="idnull" data-lg-tj-track-code="index_yanzhi">言职</a>
				</li>
			</ul>

		</div>

	</div><!--end #lg_tnav-->


	</div><!--end #header-->

	<input type="hidden" id="serverTime" value="1541504079601" />

    <!-- 页面主体START -->
    <div id="content-container">

        <div class="search-wrapper  ">
    <div id="searchBar" class="search-bar">
        <div class="tab-wrapper">
                        <a id="tab_pos" class="active" rel="nofollow" href="javascript:;">职位 ( <span>500+</span> ) </a>
            <a id="tab_comp" class="disabled" rel="nofollow" href="javascript:;">公司 ( <span>0</span> ) </a>
                    </div>
        <div class="input-wrapper" data-lg-tj-track-code="search_search" data-lg-tj-track-type="1">
            <div class="keyword-wrapper">
                                <input type="text" id="keyword" autocomplete="off" maxlength="64" placeholder="搜索职位、公司或地点" value="python"/>
                            </div>
            <input type="button" id="submit" value="搜索"/>
        </div>
                <div class="r_search_tit" data-lg-tj-track-code="search_relevant" data-lg-tj-track-type="1">
            <span>相关搜索：</span>
            <ul class="r_search_con">
                                                                                                            <li class="r_search"><a class="r_search_a" href="https://www.lagou.com/zhaopin/shujuwajue/">数据挖掘</a></li>
                                                                                <li class="r_search"><a rel="nofollow" class="r_search_a" href="https://www.lagou.com/jobs/list_爬虫?oquery=python&fromSearch=true&labelWords=relative">爬虫</a></li>
                                                                                <li class="r_search"><a rel="nofollow" class="r_search_a" href="https://www.lagou.com/jobs/list_python爬虫?oquery=python&fromSearch=true&labelWords=relative">python爬虫</a></li>
                                                                                <li class="r_search"><a rel="nofollow" class="r_search_a" href="https://www.lagou.com/jobs/list_python后端?oquery=python&fromSearch=true&labelWords=relative">python后端</a></li>
                                                                                <li class="r_search"><a rel="nofollow" class="r_search_a" href="https://www.lagou.com/jobs/list_python实习?oquery=python&fromSearch=true&labelWords=relative">python实习</a></li>
                                                                                <li class="r_search"><a rel="nofollow" class="r_search_a" href="https://www.lagou.com/jobs/list_django?oquery=python&fromSearch=true&labelWords=relative">django</a></li>
                                                                                <li class="r_search"><a rel="nofollow" class="r_search_a" href="https://www.lagou.com/jobs/list_python web?oquery=python&fromSearch=true&labelWords=relative">python web</a></li>
                                                                                <li class="r_search"><a rel="nofollow" class="r_search_a" href="https://www.lagou.com/jobs/list_python数据分析?oquery=python&fromSearch=true&labelWords=relative">python数据分析</a></li>
                                                                                <li class="r_search"><a rel="nofollow" class="r_search_a" href="https://www.lagou.com/jobs/list_c?oquery=python&fromSearch=true&labelWords=relative">c</a></li>
                                                </ul>
        </div>
            </div>
</div>

        <!-- 搜索输入框模块 -->
        <div id="main_container">
        <!-- 左侧 -->
            <div class="content_left">

                <!-- 依次填入左侧各个模块 -->

                <!--当前为公司标签时，隐藏筛选条件栏-->
                <div id="positionHead" class="">

                    <!-- 公司卡片 -->

                    

                    <!-- 筛选 -->

                    <ul id="filterBox" class="filter-wrapper">
    <input id="filterOption" type="hidden" value="1">

        <li class="li-taller brief dn" id="filterBrief">
        <span class="title">工作地点：</span>
                    <a rel="nofollow" href="javascript:;" class="active">全国</a>
        
        
        <span class="title">工作经验：</span>
                <a rel="nofollow" href="javascript:;" class="active">不限</a>
        
        <span class="title">学历要求：</span>
                <a rel="nofollow" href="javascript:;" class="active">不限</a>
        
        <span class="title">融资阶段：</span>
                <a rel="nofollow" href="javascript:;" class="active">不限</a>
        
        <span class="title">公司规模：</span>
                <a rel="nofollow" href="javascript:;" class="active">不限</a>
        
        <span class="title">行业领域：</span>
                <a rel="nofollow" href="javascript:;" class="active">不限</a>
            </li>
    
        <div class="details" id="filterCollapse">
        <div class="has-more">
            <div class="more more-positions workPosition">
                <li class="hot">
                    <span class="title">工作地点：</span>
                                                            <a rel="nofollow" href="javascript:;" class="active" data-lg-tj-id="8p00" data-lg-tj-no="
                                                            0001
                                                    " data-lg-tj-cid="idnull" data-id="">全国</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8p00" data-lg-tj-no="
                                                            0002
                                                    " data-lg-tj-cid="idnull" data-id="5" class="more-city-name">北京</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8p00" data-lg-tj-no="
                                                            0003
                                                    " data-lg-tj-cid="idnull" data-id="6" class="more-city-name">上海</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8p00" data-lg-tj-no="
                                                            0004
                                                    " data-lg-tj-cid="idnull" data-id="765" class="more-city-name">深圳</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8p00" data-lg-tj-no="
                                                            0005
                                                    " data-lg-tj-cid="idnull" data-id="763" class="more-city-name">广州</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8p00" data-lg-tj-no="
                                                            0006
                                                    " data-lg-tj-cid="idnull" data-id="653" class="more-city-name">杭州</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8p00" data-lg-tj-no="
                                                            0007
                                                    " data-lg-tj-cid="idnull" data-id="801" class="more-city-name">成都</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8p00" data-lg-tj-no="
                                                            0008
                                                    " data-lg-tj-cid="idnull" data-id="635" class="more-city-name">南京</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8p00" data-lg-tj-no="
                                                            0009
                                                    " data-lg-tj-cid="idnull" data-id="736" class="more-city-name">武汉</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8p00" data-lg-tj-no="
                                                            0010
                                                    " data-lg-tj-cid="idnull" data-id="854" class="more-city-name">西安</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8p00" data-lg-tj-no="
                                                            0011
                                                    " data-lg-tj-cid="idnull" data-id="682" class="more-city-name">厦门</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8p00" data-lg-tj-no="
                                                            0012
                                                    " data-lg-tj-cid="idnull" data-id="749" class="more-city-name">长沙</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8p00" data-lg-tj-no="
                                                            0013
                                                    " data-lg-tj-cid="idnull" data-id="639" class="more-city-name">苏州</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8p00" data-lg-tj-no="
                                                            0014
                                                    " data-lg-tj-cid="idnull" data-id="7" class="more-city-name">天津</a>
                                                        </li>
                <li class="other">
                                                            <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0001
                                                    " data-lg-tj-cid="idnull" data-id="8" class="more-city-name">重庆</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0002
                                                    " data-lg-tj-cid="idnull" data-id="719" class="more-city-name">郑州</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0003
                                                    " data-lg-tj-cid="idnull" data-id="703" class="more-city-name">青岛</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0004
                                                    " data-lg-tj-cid="idnull" data-id="664" class="more-city-name">合肥</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0005
                                                    " data-lg-tj-cid="idnull" data-id="681" class="more-city-name">福州</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0006
                                                    " data-lg-tj-cid="idnull" data-id="702" class="more-city-name">济南</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0007
                                                    " data-lg-tj-cid="idnull" data-id="600" class="more-city-name">大连</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0008
                                                    " data-lg-tj-cid="idnull" data-id="766" class="more-city-name">珠海</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0009
                                                    " data-lg-tj-cid="idnull" data-id="636" class="more-city-name">无锡</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0010
                                                    " data-lg-tj-cid="idnull" data-id="768" class="more-city-name">佛山</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0011
                                                    " data-lg-tj-cid="idnull" data-id="779" class="more-city-name">东莞</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0012
                                                    " data-lg-tj-cid="idnull" data-id="654" class="more-city-name">宁波</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0013
                                                    " data-lg-tj-cid="idnull" data-id="638" class="more-city-name">常州</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0014
                                                    " data-lg-tj-cid="idnull" data-id="599" class="more-city-name">沈阳</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0015
                                                    " data-lg-tj-cid="idnull" data-id="565" class="more-city-name">石家庄</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0016
                                                    " data-lg-tj-cid="idnull" data-id="831" class="more-city-name">昆明</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0017
                                                    " data-lg-tj-cid="idnull" data-id="691" class="more-city-name">南昌</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0018
                                                    " data-lg-tj-cid="idnull" data-id="785" class="more-city-name">南宁</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0019
                                                    " data-lg-tj-cid="idnull" data-id="622" class="more-city-name">哈尔滨</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0020
                                                    " data-lg-tj-cid="idnull" data-id="799" class="more-city-name">海口</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0021
                                                    " data-lg-tj-cid="idnull" data-id="780" class="more-city-name">中山</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0022
                                                    " data-lg-tj-cid="idnull" data-id="773" class="more-city-name">惠州</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0023
                                                    " data-lg-tj-cid="idnull" data-id="822" class="more-city-name">贵阳</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0024
                                                    " data-lg-tj-cid="idnull" data-id="613" class="more-city-name">长春</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0025
                                                    " data-lg-tj-cid="idnull" data-id="576" class="more-city-name">太原</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0026
                                                    " data-lg-tj-cid="idnull" data-id="656" class="more-city-name">嘉兴</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0027
                                                    " data-lg-tj-cid="idnull" data-id="710" class="more-city-name">泰安</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0028
                                                    " data-lg-tj-cid="idnull" data-id="" class="more-city-name">昆山</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0029
                                                    " data-lg-tj-cid="idnull" data-id="707" class="more-city-name">烟台</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0030
                                                    " data-lg-tj-cid="idnull" data-id="864" class="more-city-name">兰州</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0031
                                                    " data-lg-tj-cid="idnull" data-id="685" class="more-city-name">泉州</a>
                                                            <a rel="nofollow" href="javascript:;" id="all_city">全部城市 > </a>
                </li>
            </div>

            <!-- 处理工作地点深层选择 -->
            <div class="choose-detail">
                <li class="position-head">

                    <div class="current-handle-position">
                        <span class="title">工作地点：</span>
                                                    <a class="current_city current">全国</a>
                        
                                                

                                                                                
                                                
                    </div>

                    <div class="other-hot-city">
                        <div class="city-wrapper dn">
                                                                                                                                                                                                                                                                    <a data-id="5" class="hot-city-name">北京</a>
                                                                                                                                                                                                        <a data-id="6" class="hot-city-name">上海</a>
                                                                                                                                                                                                        <a data-id="765" class="hot-city-name">深圳</a>
                                                                                                                                                                                                        <a data-id="763" class="hot-city-name">广州</a>
                                                                                                                                                                                                        <a data-id="653" class="hot-city-name">杭州</a>
                                                                                                                                                                                                        <a data-id="801" class="hot-city-name">成都</a>
                                                                                                                                                                                                        <a data-id="635" class="hot-city-name">南京</a>
                                                                                                                                                                                                        <a data-id="736" class="hot-city-name">武汉</a>
                                                                                                                                                                                                        <a data-id="854" class="hot-city-name">西安</a>
                                                                                                                                                                                                        <a data-id="682" class="hot-city-name">厦门</a>
                                                                                                                                                                                                        <a data-id="749" class="hot-city-name">长沙</a>
                                                                                                                                                                                                        <a data-id="639" class="hot-city-name">苏州</a>
                                                                                                                                                                                                        <a data-id="7" class="hot-city-name">天津</a>
                                                                                                                        </div>
                        <a rel="nofollow" class="btn-more" href="javascript:;">更多&ensp;<i></i></a>
                    </div>

                </li>

                
                
                
                
                                

                
                

            </div>
        </div>
                <li class="multi-chosen"><span class="title">工作经验：</span>
                                                    <a rel="nofollow" href="javascript:;" class="active" data-lg-tj-id=8r00 data-lg-tj-no="
                                                            0001
                                                    " data-lg-tj-cid="idnull">不限
            </a>
                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id=8r00 data-lg-tj-no="
                                                                    0002
                                                            " data-lg-tj-cid="idnull">应届毕业生                            <i class="delete"></i>

                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id=8r00 data-lg-tj-no="
                                                                    0003
                                                            " data-lg-tj-cid="idnull">3年及以下                            <i class="delete"></i>

                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id=8r00 data-lg-tj-no="
                                                                    0004
                                                            " data-lg-tj-cid="idnull">3-5年                            <i class="delete"></i>

                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id=8r00 data-lg-tj-no="
                                                                    0005
                                                            " data-lg-tj-cid="idnull">5-10年                            <i class="delete"></i>

                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id=8r00 data-lg-tj-no="
                                                                    0006
                                                            " data-lg-tj-cid="idnull">10年以上                            <i class="delete"></i>

                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id=8r00 data-lg-tj-no="
                                                                    0007
                                                            " data-lg-tj-cid="idnull">不要求                            <i class="delete"></i>

                </a>
                                                </li>

        <li class="multi-chosen"><span class="title">学历要求：</span>

                                    <a rel="nofollow" href="javascript:;" class="active" data-lg-tj-id="8s00" data-lg-tj-no="
                                                            0001
                                                    " data-lg-tj-cid="idnull">不限
            </a>
                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8s00" data-lg-tj-no="
                                                                    0002
                                                            " data-lg-tj-cid="idnull">大专
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8s00" data-lg-tj-no="
                                                                    0003
                                                            " data-lg-tj-cid="idnull">本科
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8s00" data-lg-tj-no="
                                                                    0004
                                                            " data-lg-tj-cid="idnull">硕士
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8s00" data-lg-tj-no="
                                                                    0005
                                                            " data-lg-tj-cid="idnull">博士
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8s00" data-lg-tj-no="
                                                                    0006
                                                            " data-lg-tj-cid="idnull">不要求
                            <i class="delete"></i>
                </a>
                                        
        </li>
        <li class="multi-chosen"><span class="title">融资阶段：</span>
                                    <a rel="nofollow" href="javascript:;" class="active" data-lg-tj-id="8t00" data-lg-tj-no="
                                                            0001
                                                    " data-lg-tj-cid="idnull">不限
            </a>
                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8t00" data-lg-tj-no="
                                                                    0002
                                                            " data-lg-tj-cid="idnull">未融资
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8t00" data-lg-tj-no="
                                                                    0003
                                                            " data-lg-tj-cid="idnull">天使轮
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8t00" data-lg-tj-no="
                                                                    0004
                                                            " data-lg-tj-cid="idnull">A轮
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8t00" data-lg-tj-no="
                                                                    0005
                                                            " data-lg-tj-cid="idnull">B轮
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8t00" data-lg-tj-no="
                                                                    0006
                                                            " data-lg-tj-cid="idnull">C轮
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8t00" data-lg-tj-no="
                                                                    0007
                                                            " data-lg-tj-cid="idnull">D轮及以上
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8t00" data-lg-tj-no="
                                                                    0008
                                                            " data-lg-tj-cid="idnull">上市公司
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8t00" data-lg-tj-no="
                                                                    0009
                                                            " data-lg-tj-cid="idnull">不需要融资
                            <i class="delete"></i>
                </a>
                                                </li>
        <li class="multi-chosen"><span class="title">公司规模：</span>

                                    <a rel="nofollow" href="javascript:;" class="active" data-lg-tj-id="1c49" data-lg-tj-no="
                                                            0001
                                                    " data-lg-tj-cid="idnull">不限
            </a>
                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="1c49" data-lg-tj-no="
                                                                    0002
                                                            " data-lg-tj-cid="idnull">少于15人
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="1c49" data-lg-tj-no="
                                                                    0003
                                                            " data-lg-tj-cid="idnull">15-50人
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="1c49" data-lg-tj-no="
                                                                    0004
                                                            " data-lg-tj-cid="idnull">50-150人
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="1c49" data-lg-tj-no="
                                                                    0005
                                                            " data-lg-tj-cid="idnull">150-500人
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="1c49" data-lg-tj-no="
                                                                    0006
                                                            " data-lg-tj-cid="idnull">500-2000人
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="1c49" data-lg-tj-no="
                                                                    0007
                                                            " data-lg-tj-cid="idnull">2000人以上
                            <i class="delete"></i>
                </a>
                                        
        </li>
        <div class="has-more hy-area">
            <li class="multi-chosen">
                <span class="title">行业领域：</span>
                                                <a rel="nofollow" href="javascript:;" class="active" data-lg-tj-id="8u00" data-lg-tj-no="
                                                            0001
                                                    " data-lg-tj-cid="idnull">不限
                </a>
                                                                                        <a rel="nofollow" href="javascript:;" data-lg-tj-id="8u00" data-lg-tj-no="
                                                                    0002
                                                            " data-lg-tj-cid="idnull">移动互联网
                            <i class="delete"></i>
                    </a>
                                                                                                            <a rel="nofollow" href="javascript:;" data-lg-tj-id="8u00" data-lg-tj-no="
                                                                    0003
                                                            " data-lg-tj-cid="idnull">电子商务
                            <i class="delete"></i>
                    </a>
                                                                                                            <a rel="nofollow" href="javascript:;" data-lg-tj-id="8u00" data-lg-tj-no="
                                                                    0004
                                                            " data-lg-tj-cid="idnull">金融
                            <i class="delete"></i>
                    </a>
                                                                                                            <a rel="nofollow" href="javascript:;" data-lg-tj-id="8u00" data-lg-tj-no="
                                                                    0005
                                                            " data-lg-tj-cid="idnull">企业服务
                            <i class="delete"></i>
                    </a>
                                                                                                            <a rel="nofollow" href="javascript:;" data-lg-tj-id="8u00" data-lg-tj-no="
                                                                    0006
                                                            " data-lg-tj-cid="idnull">教育
                            <i class="delete"></i>
                    </a>
                                                                                                            <a rel="nofollow" href="javascript:;" data-lg-tj-id="8u00" data-lg-tj-no="
                                                                    0007
                                                            " data-lg-tj-cid="idnull">文化娱乐
                            <i class="delete"></i>
                    </a>
                                                                                                            <a rel="nofollow" href="javascript:;" data-lg-tj-id="8u00" data-lg-tj-no="
                                                                    0008
                                                            " data-lg-tj-cid="idnull">游戏
                            <i class="delete"></i>
                    </a>
                                                                                                            <a rel="nofollow" href="javascript:;" data-lg-tj-id="8u00" data-lg-tj-no="
                                                                    0009
                                                            " data-lg-tj-cid="idnull">O2O
                            <i class="delete"></i>
                    </a>
                                                                                                            <a rel="nofollow" href="javascript:;" data-lg-tj-id="8u00" data-lg-tj-no="
                                                                    0010
                                                            " data-lg-tj-cid="idnull">硬件
                            <i class="delete"></i>
                    </a>
                                                                    <span class="btn-more-hy" href="javascript:;">更多&ensp;<i></i></span>
            </li>
            <div class="more-hy more-fields">
                <li class="hot multi-chosen">
                    <span class="title">行业领域：</span>
                                                            <a rel="nofollow" href="javascript:;" class="active" data-lg-tj-id="8u00" data-lg-tj-no="
                                                                    0001
                                                            " data-lg-tj-cid="idnull">不限
                    </a>
                                                                                                            <a rel="nofollow" href="javascript:;" data-lg-tj-id="8v00" data-lg-tj-no="
                                                                    0002
                                                            " data-lg-tj-cid="idnull">移动互联网
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8v00" data-lg-tj-no="
                                                                    0003
                                                            " data-lg-tj-cid="idnull">电子商务
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8v00" data-lg-tj-no="
                                                                    0004
                                                            " data-lg-tj-cid="idnull">金融
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8v00" data-lg-tj-no="
                                                                    0005
                                                            " data-lg-tj-cid="idnull">企业服务
                            <i class="delete"></i>
                         </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8v00" data-lg-tj-no="
                                                                    0006
                                                            " data-lg-tj-cid="idnull">教育
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8v00" data-lg-tj-no="
                                                                    0007
                                                            " data-lg-tj-cid="idnull">文化娱乐
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8v00" data-lg-tj-no="
                                                                    0008
                                                            " data-lg-tj-cid="idnull">游戏
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8v00" data-lg-tj-no="
                                                                    0009
                                                            " data-lg-tj-cid="idnull">O2O
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8v00" data-lg-tj-no="
                                                                    0010
                                                            " data-lg-tj-cid="idnull">硬件
                            <i class="delete"></i>
                        </a>
                                                                                </li>
                <li class="other multi-chosen other-hy">
                                                                                        <a rel="nofollow" href="javascript:;" data-lg-tj-id="8w00" data-lg-tj-no="
                                                                    0001
                                                            " data-lg-tj-cid="idnull">社交网络
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8w00" data-lg-tj-no="
                                                                    0002
                                                            " data-lg-tj-cid="idnull">旅游
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8w00" data-lg-tj-no="
                                                                    0003
                                                            " data-lg-tj-cid="idnull">医疗健康
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8w00" data-lg-tj-no="
                                                                    0004
                                                            " data-lg-tj-cid="idnull">生活服务
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8w00" data-lg-tj-no="
                                                                    0005
                                                            " data-lg-tj-cid="idnull">信息安全
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8w00" data-lg-tj-no="
                                                                    0006
                                                            " data-lg-tj-cid="idnull">数据服务
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8w00" data-lg-tj-no="
                                                                    0007
                                                            " data-lg-tj-cid="idnull">广告营销
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8w00" data-lg-tj-no="
                                                                    0008
                                                            " data-lg-tj-cid="idnull">分类信息
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8w00" data-lg-tj-no="
                                                                    0009
                                                            " data-lg-tj-cid="idnull">招聘
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8w00" data-lg-tj-no="
                                                                    0010
                                                            " data-lg-tj-cid="idnull">其他
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8w00" data-lg-tj-no="
                                                                    0011
                                                            " data-lg-tj-cid="idnull">区块链
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8w00" data-lg-tj-no="
                                                                    0012
                                                            " data-lg-tj-cid="idnull">人工智能
                            <i class="delete"></i>
                        </a>
                                                                                </li>
            </div>
        </div>
    </div>
</ul>
<div class="btn-collapse-wrapper">
    <a rel="nofollow" class="btn-collapse " title="点击收起筛选项" href="javascript:"></a>
</div>




                    <!-- 排序 -->

                    <ul class="order" id="order">
    <li class="wrapper">
        <div class="item order">
            <span class="title">排序方式：</span>
                                    <a rel="nofollow" href="javascript:;" class="active" data-lg-tj-id="8x00" data-lg-tj-no="
                                                            0001
                                                    " data-lg-tj-cid="idnull">默认</a>
                                                <a rel="nofollow" href="https://www.lagou.com/jobs/list_python?px=new&city=全国#order" data-lg-tj-id="8x00" data-lg-tj-no="
                                                            0002
                                                    " data-lg-tj-cid="idnull">最新</a>
                                </div>
        <div class="item salary selectUI">
            <span class="title">月薪：</span>
                                                                                                                                                                                                                                                                                    <div class="selectUI-text text"><span>不限</span><i></i>
                            <ul>
                                        <li><a rel="nofollow" href="https://www.lagou.com/jobs/list_python?px=default&city=全国#order" data-lg-tj-id="8y00" data-lg-tj-no="
                                                            0001
                                                    " data-lg-tj-cid="idnull">不限</a></li>
                                        <li><a rel="nofollow" href="https://www.lagou.com/jobs/list_python?px=default&yx=2k以下&city=全国#order" data-lg-tj-id="8y00" data-lg-tj-no="
                                                            0002
                                                    " data-lg-tj-cid="idnull">2k以下</a></li>
                                        <li><a rel="nofollow" href="https://www.lagou.com/jobs/list_python?px=default&yx=2k-5k&city=全国#order" data-lg-tj-id="8y00" data-lg-tj-no="
                                                            0003
                                                    " data-lg-tj-cid="idnull">2k-5k</a></li>
                                        <li><a rel="nofollow" href="https://www.lagou.com/jobs/list_python?px=default&yx=5k-10k&city=全国#order" data-lg-tj-id="8y00" data-lg-tj-no="
                                                            0004
                                                    " data-lg-tj-cid="idnull">5k-10k</a></li>
                                        <li><a rel="nofollow" href="https://www.lagou.com/jobs/list_python?px=default&yx=10k-15k&city=全国#order" data-lg-tj-id="8y00" data-lg-tj-no="
                                                            0005
                                                    " data-lg-tj-cid="idnull">10k-15k</a></li>
                                        <li><a rel="nofollow" href="https://www.lagou.com/jobs/list_python?px=default&yx=15k-25k&city=全国#order" data-lg-tj-id="8y00" data-lg-tj-no="
                                                            0006
                                                    " data-lg-tj-cid="idnull">15k-25k</a></li>
                                        <li><a rel="nofollow" href="https://www.lagou.com/jobs/list_python?px=default&yx=25k-50k&city=全国#order" data-lg-tj-id="8y00" data-lg-tj-no="
                                                            0007
                                                    " data-lg-tj-cid="idnull">25k-50k</a></li>
                                        <li><a rel="nofollow" href="https://www.lagou.com/jobs/list_python?px=default&yx=50k以上&city=全国#order" data-lg-tj-id="8y00" data-lg-tj-no="
                                                            0008
                                                    " data-lg-tj-cid="idnull">50k以上</a></li>
                                    </ul>
            </div>
        </div>
                <div class="item type selectUI">
            <span class="title">工作性质：</span>
                                                                                                                                                                    <div class="selectUI-text value text"><span>不限</span><i></i>
                            <ul>
                                        <li><a rel="nofollow" href="https://www.lagou.com/jobs/list_python?px=default&city=全国#order" data-lg-tj-id="8z00" data-lg-tj-no="
                                                            0001
                                                    " data-lg-tj-cid="idnull">不限</a></li>
                                        <li><a rel="nofollow" href="https://www.lagou.com/jobs/list_python?px=default&gx=全职&city=全国#order" data-lg-tj-id="8z00" data-lg-tj-no="
                                                            0002
                                                    " data-lg-tj-cid="idnull">全职</a></li>
                                        <li><a rel="nofollow" href="https://www.lagou.com/jobs/list_python?px=default&gx=兼职&city=全国#order" data-lg-tj-id="8z00" data-lg-tj-no="
                                                            0003
                                                    " data-lg-tj-cid="idnull">兼职</a></li>
                                        <li><a rel="nofollow" href="https://www.lagou.com/jobs/list_python?px=default&gx=实习&city=全国&isSchoolJob=1#order" data-lg-tj-id="8z00" data-lg-tj-no="
                                                            0004
                                                    " data-lg-tj-cid="idnull">实习</a></li>
                                    </ul>
            </div>
        </div>
                <div class="item page">
                            <div class="prev ban">
                    &lt;
                </div>
                                        <div class="next_disabled next ">
                    &gt;
                </div>
                        <div class="page-number">
                <span class="curNum">1</span>
                /
                <span class="span totalNum">30</span>
            </div>
        </div>
    </li>
</ul>


                    <!--活动位-->

                </div>

                

                <!-- 公司列表 -->

                <div class="company_list dn" id="company_list">

	<ul class="item_con_list">
	</ul>

	<!-- 推荐公司、城市 -->
    <!-- <div class="recommend-comp-city dn">
    <div class="r_search_tit">相关搜索：</div>
    <ul class="r_search_con">

    </ul>
</div> -->


<div class="recommend-comp-city hide-recom dn" style="display: block;">
	<a rel="nofollow" href="javascript:;" class="expansion">展开<i></i></a>
    <div class="r_company_tit">推荐公司：</div>
    <ul class="r_company_con">
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/9251.html">美柚</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/1373.html">喜马拉雅fm</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/14229.html">微盟</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/49369.html">淘粉吧</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/107435.html">熊猫TV</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/2768.html">易到用车</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/40738.html">小红唇</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/97631.html">汽车超人</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/109.html">蚂蜂窝</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/36996.html">三好网</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/4760.html">唯品会</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/1686.html">爱奇艺</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/23014.html">快法务</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/1575.html">百度招聘</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/81491.html">蚂蚁金服</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/62.html">今日头条</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/2474.html">滴滴</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/20909.html">AcFun</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/23489.html">点点客</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/59251.html">映客</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/3712.html">京东</a></li>
    	    </ul>
    <div class="r_city_tit">推荐城市：</div>
    <ul class="r_city_con">
    	    		<li class="r_search_item"><a href="https://www.lagou.com/beijing/">北京找工作</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/beijing/">北京招聘</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/shanghai/">上海找工作</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/shanghai/">上海招聘</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/hangzhou/">杭州找工作</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/hangzhou/">杭州招聘</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/guangzhou/">广州找工作</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/guangzhou/">广州招聘</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/shenzhen/">深圳找工作</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/shenzhen/">深圳招聘</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/chengdu/">成都找工作</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/chengdu/">成都招聘</a></li>
    	    </ul>
</div>

	<!-- 分页 -->
	<div class="item_con_pager"></div>
    <input type="hidden" name="abtCode" value="dm-csearch-useUserAllInterest|0" />
</div>

<script id="tpl-comp-list" type="text/html">
	{{each data as item i}}
	<li class="c_list_item" data-index="{{i + indexOffset}}" data-companyid="{{item.companyId}}">

		<div class="cl_left">
			<a href="https://www.lagou.com/gongsi/{{item.companyId}}.html" target="_blank" data-lg-tj-id="8B00" data-lg-tj-no="
             	{{if i<9}}
             		{{if item.curpage<10}}
                	0{{item.curpage}}0{{i+1}}
                	{{else}}
                	{{item.curpage}}0{{i+1}}
                	{{/if}}
                {{else}}
                	{{if item.curpage<10}}
                    0{{item.curpage}}{{i+1}}
                    {{else}}
                    {{item.curpage}}{{i+1}}
                    {{/if}}
               {{/if}}
                " data-lg-tj-cid="{{item.companyId}}" {{if extra.abt}}data-lg-tj-abt="{{extra.abt}}"{{/if}}><img src="//www.lgstatic.com/thumbnail_160x160/{{item.companyLogo}}" alt="{{item.companyFullName}}" width="80" height="80"></a>
		</div>

		<div class="cl_r">

			<div class="cl_r_top">
				<h3><a class="company_link" href="https://www.lagou.com/gongsi/{{item.companyId}}.html" target="_blank" data-lg-tj-id="8C00" data-lg-tj-no="
             	{{if i<9}}
             		{{if item.curpage<10}}
                	0{{item.curpage}}0{{i+1}}
                	{{else}}
                	{{item.curpage}}0{{i+1}}
                	{{/if}}
                {{else}}
                	{{if item.curpage<10}}
                    0{{item.curpage}}{{i+1}}
                    {{else}}
                    {{item.curpage}}{{i+1}}
                    {{/if}}
               {{/if}}
                " data-lg-tj-cid="{{item.companyId}}" {{if extra.abt}}data-lg-tj-abt="{{extra.abt}}"{{/if}}>{{item.companyShortName}}</a></h3>
				<div>“{{item.companyFeatures}}”</div>
			</div>

			<div class="cl_r_bot">
				<ul class="list_c">
					<li class="address"><span></span>{{item.city}}{{if item.district}},{{item.district}}{{/if}}</li>
					<li class="indu"><span></span>{{item.industryField}}</li>
					<li class="posi"><a href="https://www.lagou.com/gongsi/j{{item.companyId}}.html" target="_blank" data-lg-tj-id="8H00" data-lg-tj-no="
                {{if i<9}}
                    {{if item.curpage<10}}
                    0{{item.curpage}}0{{i+1}}
                    {{else}}
                    {{item.curpage}}0{{i+1}}
                    {{/if}}
                {{else}}
                    {{if item.curpage<10}}
                    0{{item.curpage}}{{i+1}}
                    {{else}}
                    {{item.curpage}}{{i+1}}
                    {{/if}}
               {{/if}}
                " data-lg-tj-cid="{{item.companyId}}" {{if extra.abt}}data-lg-tj-abt="{{extra.abt}}"{{/if}}><span></span>{{item.positionNum}}个在招职位</a></li>
					<li class="inter"><a href="https://www.lagou.com/gongsi/interviewExperiences.html?companyId={{item.companyId}}" target="_blank" data-lg-tj-id="8I00" data-lg-tj-no="
                {{if i<9}}
                    {{if item.curpage<10}}
                    0{{item.curpage}}0{{i+1}}
                    {{else}}
                    {{item.curpage}}0{{i+1}}
                    {{/if}}
                {{else}}
                    {{if item.curpage<10}}
                    0{{item.curpage}}{{i+1}}
                    {{else}}
                    {{item.curpage}}{{i+1}}
                    {{/if}}
               {{/if}}
                " data-lg-tj-cid="{{item.companyId}}" {{if extra.abt}}data-lg-tj-abt="{{extra.abt}}"{{/if}}><span></span>{{item.interviewRemarkNum}}个面试评价</a></li>
					<li class="c_btn"><a href="https://www.lagou.com/gongsi/{{item.companyId}}.html" target="_blank" data-lg-tj-id="8D00" data-lg-tj-no="
             	{{if i<9}}
             		{{if item.curpage<9}}
                	0{{item.curpage}}0{{i+1}}
                	{{else}}
                	{{item.curpage}}0{{i+1}}
                	{{/if}}
                {{else}}
                	{{if item.curpage<10}}
                    0{{item.curpage}}{{i+1}}
                    {{else}}
                    {{item.curpage}}{{i+1}}
                    {{/if}}
               {{/if}}
                " data-lg-tj-cid="{{item.companyId}}" {{if extra.abt}}data-lg-tj-abt="{{extra.abt}}"{{/if}}>公司主页&nbsp;<i></i></a></li>
				</ul>
			</div>
		</div>

	</li>
	{{/each}}
</script>

<script id="empty-comp" type="text/html">
    <div class="empty_position">
        <div class="pic"></div>
        <div class="txt">
            <div>暂时没有符合该搜索条件的公司</div>
            <span>请重新修改搜索条件后再进行搜索</span>
        </div>
    </div>
</script>


                <!-- 职位列表 -->

                <div class="s_position_list " id="s_position_list">
        
    <!-- 切换分站 -->
        
    
            <ul class="item_con_list"></ul>
    
    <!-- 推荐公司、城市 -->
    <!-- <div class="recommend-comp-city dn">
    <div class="r_search_tit">相关搜索：</div>
    <ul class="r_search_con">

    </ul>
</div> -->


<div class="recommend-comp-city hide-recom dn" style="display: block;">
	<a rel="nofollow" href="javascript:;" class="expansion">展开<i></i></a>
    <div class="r_company_tit">推荐公司：</div>
    <ul class="r_company_con">
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/9251.html">美柚</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/1373.html">喜马拉雅fm</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/14229.html">微盟</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/49369.html">淘粉吧</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/107435.html">熊猫TV</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/2768.html">易到用车</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/40738.html">小红唇</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/97631.html">汽车超人</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/109.html">蚂蜂窝</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/36996.html">三好网</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/4760.html">唯品会</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/1686.html">爱奇艺</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/23014.html">快法务</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/1575.html">百度招聘</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/81491.html">蚂蚁金服</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/62.html">今日头条</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/2474.html">滴滴</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/20909.html">AcFun</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/23489.html">点点客</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/59251.html">映客</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/3712.html">京东</a></li>
    	    </ul>
    <div class="r_city_tit">推荐城市：</div>
    <ul class="r_city_con">
    	    		<li class="r_search_item"><a href="https://www.lagou.com/beijing/">北京找工作</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/beijing/">北京招聘</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/shanghai/">上海找工作</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/shanghai/">上海招聘</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/hangzhou/">杭州找工作</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/hangzhou/">杭州招聘</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/guangzhou/">广州找工作</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/guangzhou/">广州招聘</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/shenzhen/">深圳找工作</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/shenzhen/">深圳招聘</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/chengdu/">成都找工作</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/chengdu/">成都招聘</a></li>
    	    </ul>
</div>


    <!-- 分页 -->
            <div class="item_con_pager"></div>
        <input id="isSEO" type="hidden" value="false">
    <input id="pageNoSEO" type="hidden" value="">
    <input id="pageSizeSEO" type="hidden" value="">
    <input id="totalPageCountSEO" type="hidden" value=""
    >
    <input id="resultLengthSEO" type="hidden" value="">
    <input type="hidden" name="abtCode" value="dm-csearch-useUserAllInterest|0" />
</div>

<!-- template -->
<script id="tpl-position-list" type="text/html">
    {{each data as item i}}
    {{if i <= 14 }}
    <li class="con_list_item{{if i==0}} first_row{{/if}} default_list" data-index="{{i + indexOffset}}" data-positionid="{{item.positionId}}" data-salary="{{item.salary}}" data-company="{{item.companyShortName}}" data-positionname="{{item.positionName}}" data-companyid="{{item.companyId}}" data-hrid="{{item.publisherId}}" data-tpladword="{{item.adWord}}">
        {{if item.adWord == 9 }}
            <span class="hurry_up"></span>
        {{/if}}
        <div class="list_item_top">
            <div class="position">
                <div class="p_top">
                    <a class="position_link" href="https://www.lagou.com/jobs/{{item.positionId}}.html" target="_blank" data-index="{{i}}" data-lg-tj-id="8E00" data-lg-tj-no="
                {{if i<9}}
                    {{if item.curpage<10}}
                    0{{item.curpage}}0{{i+1}}
                    {{else}}
                    {{item.curpage}}0{{i+1}}
                    {{/if}}
                {{else}}
                    {{if item.curpage<10}}
                    0{{item.curpage}}{{i+1}}
                    {{else}}
                    {{item.curpage}}{{i+1}}
                    {{/if}}
               {{/if}}
                " data-lg-tj-cid="{{item.positionId}}" {{if extra.abt}}data-lg-tj-abt="{{extra.abt}}"{{/if}}>
                        <h3>{{item.positionName}}</h3>
                        {{if "" == item.city }}
                            {{if !item.city}}
                                <span class="add">[<em>{{item.province}}</em>]</span>
                            {{else}}
                                {{if item.businessZones && item.businessZones.length>0 && item.businessZones[0] != ''}}
                                    <span class="add">[<em>{{item.businessZones[0]}}</em>]</span>
                                {{else}}
                                    {{if item.district}}
                                        <span class="add">[<em>{{item.district}}</em>]</span>
                                    {{else}}
                                        <span class="add">[<em>{{item.city}}</em>]</span>
                                    {{/if}}
                                {{/if}}
                            {{/if}}
                        {{else}}
                            {{if !item.city}}
                                <span class="add">[<em>{{item.province}}</em>]</span>
                            {{else}}
                                {{if item.businessZones && item.businessZones.length>0 && item.businessZones[0] != ''}}
                                    <span class="add">[<em>{{item.city}}·{{item.businessZones[0]}}</em>]</span>
                                {{else}}
                                    {{if item.district}}
                                        <span class="add">[<em>{{item.city}}·{{item.district}}</em>]</span>
                                    {{else}}
                                        <span class="add">[<em>{{item.city}}</em>]</span>
                                    {{/if}}
                                {{/if}}
                            {{/if}}
                        {{/if}}

                    </a>
                    <span class="format-time">{{item.formatCreateTime}}</span>
                    {{each data.hrInfoMap as one}}
                        {{if one.key == item.positionId}}
                            <input type="hidden" class='hr_portrait' value='{{one.portrait}}'>
                            <input type="hidden" class='hr_name' value='{{one.realName}}'>
                            <input type="hidden" class='hr_position' value='{{one.positionName}}'>
                            <input type="hidden" class='target_hr' value='{{one.userId}}'>
                            <input type="hidden" class='target_position' value='{{item.positionId}}'>
                            {{if one.canTalk == true}}
                            <div class="chat_me" data-lg-tj-id="1WI0" data-lg-tj-no="{{if item.curpage < 10}}0{{item.curpage}}{{else}}{{item.curpage}}{{/if}}{{if i < 9}}0{{i + 1}}{{else}}{{i + 1}}{{/if}}" data-lg-tj-cid="{{item.companyId}}" data-lg-tj-track-code="search_code" data-lg-tj-track-type="1"></div>
                            {{/if}}
                        {{/if}}
                    {{/each}}
                </div>
                <div class="p_bot">
                    <div class="li_b_l">
                        <span class="money">{{item.salary}}</span>
                        <!--<i></i>-->经验{{item.workYear}} / {{item.education}}
                    </div>
                </div>
            </div>
            <div class="company">
                <div class="company_name">
                    <a href="https://www.lagou.com/gongsi/{{item.companyId}}.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                {{if i<9}}
                    {{if item.curpage<10}}
                    0{{item.curpage}}0{{i+1}}
                    {{else}}
                    {{item.curpage}}0{{i+1}}
                    {{/if}}
                {{else}}
                    {{if item.curpage<10}}
                    0{{item.curpage}}{{i+1}}
                    {{else}}
                    {{item.curpage}}{{i+1}}
                    {{/if}}
               {{/if}}
                " data-lg-tj-cid="{{item.companyId}}" {{if extra.abt}}data-lg-tj-abt="{{extra.abt}}"{{/if}}>{{item.companyShortName}}</a>
                </div>
                <div class="industry">
                    {{item.industryField}} / {{item.financeStage}} / {{item.companySize}}
                </div>
            </div>
            <div class="com_logo">
                <a href="https://www.lagou.com/gongsi/{{item.companyId}}.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                {{if i<9}}
                    {{if item.curpage<10}}
                    0{{item.curpage}}0{{i+1}}
                    {{else}}
                    {{item.curpage}}0{{i+1}}
                    {{/if}}
                {{else}}
                    {{if item.curpage<10}}
                    0{{item.curpage}}{{i+1}}
                    {{else}}
                    {{item.curpage}}{{i+1}}
                    {{/if}}
               {{/if}}
                " data-lg-tj-cid="{{item.companyId}}" {{if extra.abt}}data-lg-tj-abt="{{extra.abt}}"{{/if}}><img src="//www.lgstatic.com/thumbnail_120x120/{{item.companyLogo}}" alt="{{item.companyShortName}}" width="60" height="60"></a>
            </div>
        </div>
        <div class="list_item_bot">
            {{if item.positionLables && item.positionLables.length > 0}}
                <div class="li_b_l">
                    {{each item.positionLables as datas i}}
                        <span>{{datas}}</span>
                    {{/each}}
                </div>
            {{else}}
                <div class="li_b_l">
                    {{each item.companyLabelList as datas i }}
                        {{if i<4}}
                            <span>{{datas}}</span>
                        {{/if}}
                    {{/each}}
                </div>
            {{/if}}
            <div class="li_b_r">“{{item.positionAdvantage}}”</div>
        </div>
    </li>
    {{/if}}
    {{/each}}
</script>

<!-- 数据为空 template -->
<script id="empty-position" type="text/html">
    <div class="empty_position">
        <div class="pic"></div>
        <div class="txt">
            <div>暂时没有符合该搜索条件的职位</div>
            <span>请重新修改搜索条件后再进行搜索</span>
        </div>
    </div>
</script>


            </div>

            <!-- 右侧 -->
            <!-- 依次填入右侧各个模块 -->
            <div class="content_right">

                <!-- 最近浏览 -->

                <div class="history dn" data-lg-tj-track-code="search_history">
	<div class="title">最近浏览过</div>
	<ul class="history_position_list" id="history_position_list">	
	</ul>
</div>


                <!-- 广告位  -->

                <div class="lgad_container" data-lg-tj-track-code="search_banner" data-lg-tj-track-type="1">
	<!--qq群广告位-->
	<div key="SPACE_KEY_ZHIWEISOUSUOYE_QQQUN" keywordSelector="#keyword" style="margin-bottom: 15px;"></div>
	<!--广告位-->
	<div key="ZHIWEISOUSUOYE_GUANGGAOWEI1" class="lgad_jsonp ad_exposure" style="margin-bottom: 15px;"></div>
	<div key="ZHIWEISOUSUOYE_GUANGGAOWEI2" class="lgad_jsonp ad_exposure" style="margin-bottom: 15px;"></div>
	<div key="ZHIWEISOUSUOYE_GUANGGAOWEI3" class="lgad_jsonp ad_exposure" style="margin-bottom: 15px;"></div>
	<div key="ZHIWEISOUSUOYE_GUANGGAOWEI4" class="lgad_jsonp ad_exposure" style="margin-bottom: 15px;"></div>
	<div key="ZHIWEISOUSUOYE_GUANGGAOWEI5" class="lgad_jsonp ad_exposure" style="margin-bottom: 15px;"></div>
	<div key="ZHIWEISOUSUOYE_GUANGGAOWEI6" class="lgad_jsonp ad_exposure" style="margin-bottom: 15px;"></div>
	<div key="ZHIWEISOUSUOYE_GUANGGAOWEI7" class="lgad_jsonp ad_exposure" style="margin-bottom: 15px;"></div>
	<div key="ZHIWEISOUSUOYE_GUANGGAOWEI8" class="lgad_jsonp ad_exposure" style="margin-bottom: 15px;"></div>
	<div key="ZHIWEISOUSUOYE_GUANGGAOWEI9" class="lgad_jsonp ad_exposure" style="margin-bottom: 15px;"></div>
	<div key="ZHIWEISOUSUOYE_GUANGGAOWEI10" class="lgad_jsonp ad_exposure" style="margin-bottom: 15px;"></div>
	<div key="ZHIWEISOUSUOYE_GUANGGAOWEI11" class="lgad_jsonp ad_exposure" style="margin-bottom: 15px;"></div></div>


                <!-- 待验证 广告位 -->

            </div>
        </div>        
    </div>
    <!-- 页面主体END -->
    <!-- footer -->
    <a id="backtop" title="回到顶部" rel="nofollow"></a>

<div id="footer">
    <div class="wrapper">
        <div class="inner_wrapper">
            <div class="footer_module_column">
                <a class="footer_app" href="https://www.lagou.com/app/download.html" rel="nofollow"> <i class="footer_app_icon"></i>下载拉勾APP <img data-delay-src="https://www.lgstatic.com/i/image/M00/35/06/CgpFT1lDioCAFqS2AAEeWsD3HHo535.PNG" width="160" height="160"></a>
                <a class="footer_mina" href="javascript:;" rel="nofollow"><i class="footer_mina_icon"></i> 微信小程序<img src="//www.lgstatic.com/www/static/common/widgets/footer_c/layout/img/lagou-mina-code_d70848a.png"></a>
                <div class="footer_module_item">
                    <!-- <a class="footer_wechat" href="javascript:;" rel="nofollow"><i class="footer_wechat_icon"></i> 拉勾微信 </a> -->
                    <a class="footer_wechat" href="javascript:;" rel="nofollow"><i class="footer_wechat_icon"></i> 拉勾微信 <img src="//www.lgstatic.com/www/static/common/widgets/footer_c/layout/img/lg_pic_weixin@2x_c372698.png" width="160" height="160"></a>
                    <a class="footer_webo" href="http://e.weibo.com/lagou720" target="_blank" rel="nofollow"><i class="footer_webo_icon"></i>拉勾微博</a>                            
                </div>
            </div>
            <div class="footer_module_right">
                <div class="footer_module_business">
                    <p class="footer_module_title">企业服务</p>
                    <a href="https://activity.lagou.com/activity/dist/business/index.html " target="_blank" rel="nofollow">招聘解决方案</a>
                    <a href="https://www.lagou.com/gongsi/ " target="_blank" rel="nofollow">公司搜索</a>
                    <a href="https://www.lagou.com/app/download.html " target="_blank" rel="nofollow">拉勾APP</a>
                </div>
                <div class="footer_module_business">
                    <p class="footer_module_title">用户帮助</p>
                    <a href="https://www.lagou.com/qa.html?t=1" target="_blank" rel="nofollow">帮助中心</a>
                    <a href="https://www.lagou.com/privacy.html " target="_blank" rel="nofollow">用户服务协议</a>
                    <a href="https://yanzhi.lagou.com/topic/419.html " target="_blank" rel="nofollow">在线提问</a>
                </div>
                <div class="footer_module_business">
                    <p class="footer_module_title">联系方式</p>
                    <span class="tel">服务热线：<em>4006 2828 35 (9:00 -18:00)</em></span> 
                    <a class="tel" href="mailto:cc@lagou.com">企业服务邮箱：<em>cc@lagou.com</em></span> 
                    <a href="https://www.lagou.com/about.html" target="_blank" rel="nofollow">联系我们</a>
                </div> 
            </div>
        </div>
        <div class="copyright">
            <div class="copyright_main">
                <div class="copyright_main_left">
                    <span class="copyright_title"><em>&copy;</em>2018 拉勾网</span>
                    <a target="_blank" href="http://www.miitbeian.gov.cn/state/outPortal/loginPortal.action" rel="nofollow">京ICP备14023790号-2</a>
                    <a target="_blank" class="footer_gongan" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010802024043" rel="nofollow"><i class="footer_lagou_gongan"></i>京公网安备 11010802024043号</a>
                    <div class="footer_lagou_jubao">
                        <i class="lagou_jubao"></i>
                        <p>
                        <span>违法和不良信息举报</span>
                        <span>电话: 4006 2828 35</span>
                        <span>邮箱: cc@lagou.com</span>
                        </p>
                    </div>
                </div>
                <i class="footer_lagou_icon"></i>
            </div>
        </div>
    </div>
</div>

    <!-- jquery lib --><!-- ignore -->    
    <!-- analytics js file -->    <!-- plat analytics js file -->
<script type="text/javascript" src="//www.lgstatic.com/www/static/pkg/vendor_019c1fd.js"></script>
<script type="text/javascript">/*resourcemap*/
require.config({paths:{
  "common/components/artTemplate/template-helper": "//www.lgstatic.com/www/static/common/components/artTemplate/template-helper_69eaf51",
  "common/widgets/common/msgPopup": "//www.lgstatic.com/www/static/common/widgets/common/msgPopup_4efa90e"
}});</script>
<script type="text/javascript" src="//www.lgstatic.com/www/static/pkg/search-result/page/index/main.html_aio_c025e33.js"></script>
<script type="text/javascript" src="//www.lgstatic.com/www/static/pkg/widgets_bf7295d.js"></script>
<script type="text/javascript" src="//www.lgstatic.com/www/static/pkg/layout_5709967.js"></script>
<script type="text/javascript" src="//www.lgstatic.com/www/static/pkg/search-result/page/index/main.html_aio_2_6c829ba.js"></script>
<script type="text/javascript">
    require(['common/widgets/header_c/modules/emailvalid/main']);


    require(['common/widgets/passport/passport'], function() {

    
        /* 设置自动登录监听器 */
        PASSPORT.on('autologin:succ', function() {
            PASSPORT.util.tinfo('autologin:succ');
            window.location.reload();
        });
        PASSPORT.on('autologin:fail', function() {
            PASSPORT.util.tinfo('autologin:fail');
        });
        // 触发自动登录
        PASSPORT.auto();

        /* 设置弹窗登录监听器 */
        PASSPORT.on('popuplogin:succ', function() {
            PASSPORT.util.tinfo('popuplogin:succ');
            window.location.reload();
        });
        PASSPORT.on('popuplogin:fail', function() {
            PASSPORT.util.tinfo('popuplogin:fail');
        });
        // 触发弹窗登录
        //PASSPORT.popup();
        jQuery('.passport_login_pop').each(function() {
            jQuery(this).click(function() {
                PASSPORT.popup();
            });
        });

    
    });


	    require(['common/widgets/header_c/layout/main']);
	
require(['common/widgets/plat/poster'])

    require(['common/widgets/footer_c/layout/main']);


        window.global = window.global || {};
        global.ctx = GLOBAL_DOMAIN.ctx;

        global.isLogin = "false" == "true";
        //分站城市
        global.current_city="";
                global.subSite="全国";
                global.isCloseNotice = "";
        global.keyword = "python";
        global.positionNum = "500+";
        global.companyNum = "0";
        global.isCompanySelected = "false" == 'true';
        global.queryParam = {
            city: "",
            district: "",
            bizArea: "",
            fromSearch: "false"
        };
        global.queryParamStr = "px=default&needAddtionalResult=false";
        global.isShowMoreIndustryField = "false";
        //当前搜索是否匹配到了精确的公司
        global.exactlyCompanyName = "";
        global.needAddtionalResult = "false";
        //页面筛选条件
        global.searchCondition={
            city:"",
            gj:"",
            xl:"",
            jd:"",
            hy:"",
            px:"default"
        }
        //页面统计参数(待整理)
        global.searchTj={
            cl: "false",
            fromSearch:true,
            labelWords:"",
            suginput:""
        }
        // 服务器系统时间(毫秒)
        global.serverTime = 1541504079603;
        global.isSchoolJob = "";
    

        require(['search-result/page/index/main']);
    </script>
<script type="text/javascript" src="//www.lgstatic.com/www/static/pkg/lg-analytics_ea85146.js"></script>
<script type="text/javascript" src="https://www.lagou.com/upload/oss.js"></script></body>
</html>

"""

def parse_text():
    htmlElement = etree.HTML(text)
    print(etree.tostring(htmlElement,encoding='utf-8').decode('utf-8'))

# def parse_file():
#     htmlElement = etree.parse("")
#     print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))

def parse_lagou_file():
    parser = etree.HTMLParser(encoding='utf-8')
    htmlElement = etree.parse('lagou.html',parser=parser)
    print(etree.tostring(htmlElement,encoding='utf-8').decode('utf-8'))

if __name__ == '__main__':
    parse_lagou_file()