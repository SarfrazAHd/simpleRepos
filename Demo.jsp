<%@ page contentType="text/html; charset=utf-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="u" tagdir="/WEB-INF/tags" %>
<!DOCTYPE html>
<html>
<head>
<title>??? ??? ??</title>
</head>
<body>
<%-- 
<c:if test="${! empty authUser}">
	${authUser.name}?, ?????.
	<a href="logout.do">[??????]</a>
	<a href="changePwd.do">[??????]</a>
</c:if>
<c:if test="${empty authUser}">
	<a href="join.do">[??????]</a>
	<a href="login.do">[?????]</a>
</c:if>
--%>
<u:isLogin>
	CT: ${authUser.name}?, ?????.
	<a href="logout.do">[??????]</a>
	<a href="changePwd.do">[??????]</a>
</u:isLogin>
<u:notLogin>
	CT: <a href="join.do">[??????]</a>
	<a href="login.do">[?????]</a>
</u:notLogin>
<br/>
</body>
</html>