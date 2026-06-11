<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet 
    version="3.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
    xmlns:sitemap="http://www.sitemaps.org/schemas/sitemap/0.9"
    >
    <xsl:output method="html" indent="yes" encoding="UTF-8"/>
    <xsl:template match="/">
<xsl:message>Powered by <a href="https://www.sitemap.style/">Sitemap Style</a></xsl:message>

<!-- get the hostname from the first url/loc -->
<xsl:variable name="hostname" select="substring-before(substring-after(/sitemap:urlset/sitemap:url[1]/sitemap:loc, '://'), '/')" />

        <html>
            <head>
                <meta name="viewport" content="width=device-width, initial-scale=1" />
                <meta name="referrer" content="unsafe-url" />
                <title>Sitemap for <xsl:value-of select="$hostname"/></title>
                <link rel="stylesheet" href="https://www.sitemap.style/css/pico.classless.min.css" />
                <script>
                    window.addEventListener('load', function() {                        
                        var viewPara = document.getElementById("viewpara");
                        viewPara.style.display = "block";
                        var viewLink = document.getElementById("viewlink");
                        viewLink.href = `https://sitemap-viewer.fileformat.info/view.html?url=${encodeURIComponent(window.location.href)}`;
                    });
                </script>
            </head>
            <body>
                <main>
                    <h1>Pages on <xsl:value-of select="$hostname" /></h1>

                    <p id="viewpara" style="display:none;">
                        <a id="viewlink" href="" role="button">View as a tree</a>
                    </p>

                    <ul>
                        <xsl:for-each select="sitemap:urlset/sitemap:url">
                        <xsl:variable name="sitemap_loc"><xsl:value-of select="sitemap:loc" /></xsl:variable>
                        <xsl:variable name="sitemap_lastmod"><xsl:value-of select="sitemap:lastmod" /></xsl:variable>
                        <li>
                            <a href="{$sitemap_loc}">
                                    <xsl:value-of select="sitemap:loc" /></a>
                            <xsl:if test="$sitemap_lastmod!=''">
                                (<xsl:value-of select="sitemap:lastmod" />)
                            </xsl:if>
                        </li>
                        </xsl:for-each>
                    </ul>
                    <p><xsl:value-of select="count(sitemap:urlset/sitemap:url)" /> pages</p>
                    <p><small>Powered by <a href="https://www.sitemap.style/"><img referrerpolicy="origin" src="https://www.sitemap.style/favicon.svg" style="height:1em;padding-right:0.25em;vertical-align:middle;" />Sitemap.Style</a></small></p>
                </main>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
