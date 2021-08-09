import React, { useEffect, useState } from "react";
import {
  Seoul,
  Gyeonggi,
  Incheon,
  Gangwon,
  Chungnam,
  Chungbuk,
  Sejong,
  Daejeon,
  Gyeongnam,
  Gyeongbuk,
  Jeonbuk,
  Jeonnam,
  Ulsan,
  Busan,
  Daegu,
  Gwangju,
  Jeju,
} from "./area/all_area";

import axios from "axios";

const fillColor = ["#4088da", "#ffb911", "#fc7001", "#e60000"];

function CovidInfo({area,num,level,updated_data}) {
  return (
    <div>
      <h1>대한민국 코로나 현황</h1>
      <h2>{area}</h2>
      <p>확진자 수 : {num}</p>
      <p>거리두기 단계 : {level}</p>
      <p>{updated_data} (기준)</p>
    </div>
  );
}

function CovidSvg({covidData , onClick}) {
  return (
    <svg width="700px" height="1000px" viewBox="0 0 800 1200">
        <Seoul
          fill={fillColor[covidData["서울"].level - 1]}
          onClick={onClick}
        />
        <Gyeonggi
          fill={fillColor[covidData["경기"].level - 1]}
          onClick={onClick}
        />
        <Gangwon
          fill={fillColor[covidData["강원"].level - 1]}
          onClick={onClick}
        />
        <Incheon
          fill={fillColor[covidData["인천"].level - 1]}
          onClick={onClick}
        />
        <Chungnam
          fill={fillColor[covidData["충남"].level - 1]}
          onClick={onClick}
        />
        <Chungbuk
          fill={fillColor[covidData["충북"].level - 1]}
          onClick={onClick}
        />
        <Sejong
          fill={fillColor[covidData["세종"].level - 1]}
          onClick={onClick}
        />
        <Daejeon
          fill={fillColor[covidData["대전"].level - 1]}
          onClick={onClick}
        />
        <Gyeongnam
          fill={fillColor[covidData["경남"].level - 1]}
          onClick={onClick}
        />
        <Gyeongbuk
          fill={fillColor[covidData["경북"].level - 1]}
          onClick={onClick}
        />
        <Jeonbuk
          fill={fillColor[covidData["전북"].level - 1]}
          onClick={onClick}
        />
        <Jeonnam
          fill={fillColor[covidData["전남"].level - 1]}
          onClick={onClick}
        />
        <Ulsan
          fill={fillColor[covidData["울산"].level - 1]}
          onClick={onClick}
        />
        <Busan
          fill={fillColor[covidData["부산"].level - 1]}
          onClick={onClick}
        />
        <Daegu
          fill={fillColor[covidData["대구"].level - 1]}
          onClick={onClick}
        />
        <Gwangju
          fill={fillColor[covidData["광주"].level - 1]}
          onClick={onClick}
        />
        <Jeju
          fill={fillColor[covidData["제주"].level - 1]}
          onClick={onClick}
        />
      </svg>
  )
}


function CovidMap() {
  const [covidData, setCovidData] = useState(null);
  const [selectData, setSelectData] = useState(null);

  useEffect(() => {
    console.log("업데이트 된 항목", covidData);
  }, [covidData]);

  function fetch() {
    axios.post("http://localhost:5000/covidData").then((response) => {
      // 요청 성공 시 실행되는 코드
      setCovidData(response.data);
    });
  }

  useEffect(() => {
    const timer = setInterval(() => {
      fetch();
    }, 1000);

    return () => {
      clearInterval(timer);
    }
  }, []);

  useEffect(() => {
    fetch();
  }, []);

  function handleClick(e) {
    const area = e.target.id;
    setSelectData({
      area,
      num: covidData.data[area].num,
      level: covidData.data[area].level,
    });
  }

  return covidData === null ? (
    <div>Loading</div>
  ) : (
    <div>
      {selectData && <CovidInfo area={selectData.area} num={selectData.num} level={selectData.level} updated_data={covidData.updated_data} />}
      <CovidSvg covidData={covidData.data} onClick={handleClick} />
    </div>
  );
}
export default CovidMap;