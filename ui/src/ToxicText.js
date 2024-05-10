import React, {useState} from "react";
import './ToxicText.css'
import { TSuccess, TError, BACKEND_URL} from "./service";
import axios from 'axios';
import {InfinitySpin} from 'react-loader-spinner'

export function ToxicText(){

	const [TextData, setTextData] = useState('');
	const [PredictB, setPredictB] = useState(false);

	const setTextOnChange = (e) => {
		setTextData(e.target.value);
	}

	const Predict = () => {
		
		var Axios = axios.create({
			baseURL: BACKEND_URL
		})

		if(TextData === ""){
			TError("Please Enter some text")
			return
		}
		setPredictB(true)

		Axios.post('/toxic_sensify', {
			"text_data": TextData
		}).then((data) => {
			if(data.data.value === "1"){
				TError("Sentence is Toxic.")
			}else{
				TSuccess("Sentence is Normal")
			}
			setPredictB(false)
		}).catch((err) => {
			TError(err.message)
			setPredictB(false)
		})
	}
	return (
		<div className="toxic_main">
			<textarea className="toxic_text_area" onChange={(e) => setTextOnChange(e)}/>
			<div>
				{
					!PredictB ? (<div className="toxic_predict" onClick={Predict}>Predict</div>) : (<InfinitySpin color="blue" />)
				}
			</div>
			
		</div>
	);
}