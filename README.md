## 2020-2 데이터 분석 및 활용 캡스톤 프로젝트
### 반려묘 사료 영양 성분 분석

#### 1. 분석 주제 선정 배경<br/>
최근 ‘펫팸족’의 증가로 펫코노미가 블루오션으로 떠올랐다. 펫팸족이란 ‘애완동물(pet)’과 ‘가족(family)’의 합성어로 반려동물을 가족처럼 생각하는 사람들을 의미한다. 2020년 반려동물 시장 규모는 5조8000억원으로 전망된다. 특히 글로벌 시장 조사 회사 ‘유로모니터’에 따르면, 2020년 기준 국내 펫푸드 시장 규모(소비자가 기준,개&고양이)는 약 1조 2650억원에 이른다. 반려동물 사료 선택 시 여러 요소를 고려하는데, 왼쪽 표를 보면 반려견/반려묘가 잘 먹는지, 영양성분이 충분히 들어있는지, 좋은 재료를 사용했는지, 가격 대비 품질이 좋은지, 믿을만한 브랜드인지를 고려한다는 것을 알 수 있다. 하지만 현재 제공되고 있는 사료 추천 시스템은 단순히 사용자들의 구매정보에 기반한 추천이 이루어지는 경우가 많다. 또 반려동물에게 적합한 원료인지 판단하기가 어려워 고양이 사료 등급 정도로 파악하지만, 이것 마저도 충분하지 않다고 생각하는 소비자들이 81%였다. 하지만 반려묘의 품종, 연령, 크기, 신체 상태, 질병 등에 따라 섭취해야 할 영양성분이 달라지기 때문에 필요한 영양성분을 포함한 사료인지 판단하는 것이 중요하다.

<table width="100%">
  <tr>
    <td>
      <img src="https://user-images.githubusercontent.com/53163222/103062413-7c503c00-45f1-11eb-99ae-b4b17c0221c0.jpg"/>
    </td>
    <td>
      <img src="https://user-images.githubusercontent.com/53163222/103062417-8114f000-45f1-11eb-92d5-fe19597f243a.jpg"/>
    </td>
    <td>
      <img src="https://user-images.githubusercontent.com/53163222/103062422-82461d00-45f1-11eb-88fa-ea4444b0a54d.jpg"/>      
    </td>
  </tr>
  <tr>
    <td>
      <img src="https://user-images.githubusercontent.com/53163222/103062423-82deb380-45f1-11eb-887d-d5beb031ea82.jpg"/>
    </td>
    <td>
      <img src="https://user-images.githubusercontent.com/53163222/103062427-82deb380-45f1-11eb-8d98-42f03650ceee.jpg"/>
    </td>
    <td>
      <img src="https://user-images.githubusercontent.com/53163222/103062428-83774a00-45f1-11eb-96ce-9e4b17bb63cc.jpg"/>
    </td>
  </tr>  
  <tr>
    <td>
      <img src="https://user-images.githubusercontent.com/53163222/103062429-840fe080-45f1-11eb-862f-eb8b361c7fb7.jpg"/>
    </td>
    <td>
      <img src="https://user-images.githubusercontent.com/53163222/103062430-840fe080-45f1-11eb-8e32-bab0c2ca2e3d.jpg"/>
    </td>
    <td>
      <img src="https://user-images.githubusercontent.com/53163222/103062432-84a87700-45f1-11eb-9c1d-e2396660d2d1.jpg"/>
    </td>
  </tr> 
    <tr>
    <td>
      <img src="https://user-images.githubusercontent.com/53163222/103062433-84a87700-45f1-11eb-8d3d-bb8eaec4d98b.jpg"/>
    </td>
    <td>
      <img src="https://user-images.githubusercontent.com/53163222/103062434-85410d80-45f1-11eb-84e9-f33f46a57735.jpg"/>
    </td>
    <td>
      <img src="https://user-images.githubusercontent.com/53163222/103062436-85d9a400-45f1-11eb-8c57-fdeb3bcd5031.jpg"/>
    </td>
  </tr> 
    <tr>
    <td>
      <img src="https://user-images.githubusercontent.com/53163222/103062438-85d9a400-45f1-11eb-957a-79b34cc41d7b.jpg"/>
    </td>
    <td>
      <img src="https://user-images.githubusercontent.com/53163222/103062439-86723a80-45f1-11eb-8518-f348d214a635.jpg"/>
    </td>
     <td>
      <img src="https://user-images.githubusercontent.com/53163222/103062440-870ad100-45f1-11eb-983b-31aff161ec13.jpg"/>
    </td>  
  </tr> 
    <tr>
    <td>
      <img src="https://user-images.githubusercontent.com/53163222/103062443-870ad100-45f1-11eb-8829-f3f946faf6c6.jpg"/>
    </td>
    <td>
      <img src="https://user-images.githubusercontent.com/53163222/103062444-87a36780-45f1-11eb-9f22-459564071780.jpg"/>
    </td>
    <td>
      <img src="https://user-images.githubusercontent.com/53163222/103062445-883bfe00-45f1-11eb-8ab4-ab47a1a490be.jpg"/>
    </td>
  </tr> 
    <tr>
    <td>
      <img src="https://user-images.githubusercontent.com/53163222/103062446-883bfe00-45f1-11eb-8714-ca72b2b956a8.jpg"/>
    </td>
    <td>
      <img src="https://user-images.githubusercontent.com/53163222/103062447-88d49480-45f1-11eb-80e5-e66ce3f50625.jpg"/>
    </td>
    <td>
      <img src="https://user-images.githubusercontent.com/53163222/103062448-896d2b00-45f1-11eb-9ef7-42d166fd1d2b.jpg"/>
    </td>      
  </tr> 
</table>

<!--
![반려묘 사료 영양 성분 분석 PPT-김주은, 박영미-22](https://user-images.githubusercontent.com/53163222/103062450-896d2b00-45f1-11eb-943f-ba4c50222b46.jpg)
-->
