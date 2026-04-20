# 📦 其他研究 | 2026年04月21日

> 本类共 **203** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-203](./part-05.md)

---

### 151. [MMGait: Towards Multi-Modal Gait Recognition](https://arxiv.org/abs/2604.15979)

**<font color=#1a73e8>作者：</font>** Chenye Wang, Qingyuan Cai, Saihui Hou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gait recognition has emerged as a powerful biometric technique for identifying individuals at a distance without requiring user cooperation. Most existing methods focus primarily on RGB-derived modalities, which fall short in real-world scenarios requiring multi-modal collaboration and cross-modal retrieval. To overcome these challenges, we present MMGait, a comprehensive multi-modal gait benchmark integrating data from five heterogeneous sensors, including an RGB camera, a depth camera, an infrared camera, a LiDAR scanner, and a 4D Radar system. MMGait contains twelve modalities and 334,060 sequences from 725 subjects, enabling systematic exploration across geometric, photometric, and motion domains. Based on MMGait, we conduct extensive evaluations on single-modal, cross-modal, and multi-modal paradigms to analyze modality robustness and complementarity. Furthermore, we introduce a new task, Omni Multi-Modal Gait Recognition, which aims to unify the above three gait recognition paradigms within a single model. We also propose a simple yet powerful baseline, OmniGait, which learns a shared embedding space across diverse modalities and achieves promising recognition performance. The MMGait benchmark, codebase, and pretrained checkpoints are publicly available at this https URL.

---


### 152. [SCHK-HTC: Sibling Contrastive Learning with Hierarchical Knowledge-Aware Prompt Tuning for Hierarchical Text Classification](https://arxiv.org/abs/2604.15998)

**<font color=#1a73e8>作者：</font>** Ke Xiong, Qian Wu, Wangjie Gan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Few-shot Hierarchical Text Classification (few-shot HTC) is a challenging task that involves mapping texts to a predefined tree-structured label hierarchy under data-scarce conditions. While current approaches utilize structural constraints from the label hierarchy to maintain parent-child prediction consistency, they face a critical bottleneck, the difficulty in distinguishing semantically similar sibling classes due to insufficient domain knowledge. We introduce an innovative method named Sibling Contrastive Learning with Hierarchical Knowledge-aware Prompt Tuning for few-shot HTC tasks (SCHK-HTC). Our work enhances the model's perception of subtle differences between sibling classes at deeper levels, rather than just enforcing hierarchical rules. Specifically, we propose a novel framework featuring two core components: a hierarchical knowledge extraction module and a sibling contrastive learning mechanism. This design guides model to encode discriminative features at each hierarchy level, thus improving the separability of confusable classes. Our approach achieves superior performance across three benchmark datasets, surpassing existing state-of-the-art methods in most cases. Our code is available at this https URL.

---


### 153. ["When I see Jodie, I feel relaxed": Examining the Impact of a Virtual Supporter in Remote Psychotherapy](https://arxiv.org/abs/2604.16003)

**<font color=#1a73e8>作者：</font>** Jiashuo Cao, Chen Li, Wujie Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Virtual agents have shown promising potential in mental health applications, but current research has predominantly focused on contexts outside of traditional therapy sessions. This paper examines the impact of a virtual supporter in remote psychotherapy sessions conducted via Zoom. We used a two-phase research approach. First we conducted a formative study to understand the roles and functions of human supporters in psychotherapy contexts. Based on these findings, we developed a virtual supporter operating in two modes: Daily Mode (for mood journaling outside therapy) and Therapy Mode (as an additional participant in Zoom therapy sessions). Finally we ran a user study with 14 participants who engaged with the virtual supporter for a week and then joined a remote psychotherapy session together. Our findings revealed that the virtual supporter had positive effects on creating psychological safety, reducing anxiety, and enhancing emotional articulation without disrupting the therapeutic process. We then discussed both the benefits and potential disadvantages of virtual supporters in therapeutic contexts, including concerns about over-reliance and the need for appropriate boundaries. This research contributes to understanding how AI-driven virtual agents could contribute to human-led remote psychotherapy.

---


### 154. [Corner Reflector Array Jamming Discrimination Using Multi-Dimensional Micro-Motion Features with Frequency Agile Radar](https://arxiv.org/abs/2604.16008)

**<font color=#1a73e8>作者：</font>** Jie Yuan, Lei Wang, Yanhao Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper introduces a robust discrimination method for distinguishing real ship targets from corner-reflector-array jamming with frequency-agile radar. The key idea is to exploit the multidimensional micro-motion signatures that separate rigid ships from non-rigid decoys. From Range-Velocity maps we derive two new hand-crafted descriptors-mean weighted residual (MWR) and complementary contrast factor (CCF) and fuse them with deep features learned by a lightweight CNN. An XGBoost classifier then gives the final decision. Extensive simulations show that the hybrid feature set consistently outperforms state-of-the-art alternatives, confirming the superiority of the proposed approach.

---


### 155. [MEDLEY-BENCH: Scale Buys Evaluation but Not Control in AI Metacognition](https://arxiv.org/abs/2604.16009)

**<font color=#1a73e8>作者：</font>** Farhad Abtahi, Abdolamir Karbalaie, Eduardo Illueca-Fernandez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Metacognition, the ability to monitor and regulate one's own reasoning, remains under-evaluated in AI benchmarking. We introduce MEDLEY-BENCH, a benchmark of behavioural metacognition that separates independent reasoning, private self-revision, and socially influenced revision under genuine inter-model disagreement. The benchmark evaluates 35 models from 12 families on 130 ambiguous instances across five domains and reports two complementary scores: the Medley Metacognition Score (MMS), a tier-based aggregate of reflective updating, social robustness, and epistemic articulation, and the Medley Ability Score (MAS), derived from four metacognitive sub-abilities. Results show a robust evaluation/control dissociation: evaluation ability increases with model size within families, whereas control does not. In a follow-up progressive adversarial analysis of 11 models, we observed two behavioural profiles, i.e., models that revise primarily in response to argument quality and models that track consensus statistics. Under within-model relative profiling (ipsative scoring), evaluation was the weakest relative ability in all 35 models, indicating a systematic knowing/doing gap. Smaller and cheaper models often matched or outperformed larger counterparts, suggesting that metacognitive competence is not simply a function of scale. These findings position MEDLEY-BENCH as a tool for measuring belief revision under social pressure and suggest that future training should reward calibrated, proportional updating rather than output quality alone.

---


### 156. [IA-CLAHE: Image-Adaptive Clip Limit Estimation for CLAHE](https://arxiv.org/abs/2604.16010)

**<font color=#1a73e8>作者：</font>** Rikuto Otsuka, Yuho Shoji, Yuka Ogino 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper proposes image-adaptive contrast limited adaptive histogram equalization (IA-CLAHE). Conventional CLAHE is widely used to boost the performance of various computer vision tasks and to improve visual quality for human perception in practical industrial applications. CLAHE applies contrast limited histogram equalization to each local region to enhance local contrast. However, CLAHE often leads to over-enhancement, because the contrast-limiting parameter clip limit is fixed regardless of the histogram distribution of each local region. Our IA-CLAHE addresses this limitation by adaptively estimating tile-wise clip limits from the input image. To achieve this, we train a lightweight clip limits estimator with a differentiable extension of CLAHE, enabling end-to-end optimization. Unlike prior learning-based CLAHE methods, IA-CLAHE does not require pre-searched ground-truth clip limits or task-specific datasets, because it learns to map input image histograms toward a domain-invariant uniform distribution, enabling zero-shot generalization across diverse conditions. Experimental results show that IA-CLAHE consistently improves recognition performance, while simultaneously enhancing visual quality for human perception, without requiring any task-specific training data.

---


### 157. [Breakout-picker: Reducing false positives in deep learning-based borehole breakout characterization from acoustic image logs](https://arxiv.org/abs/2604.16011)

**<font color=#1a73e8>作者：</font>** Guangyu Wang, Xiaodong Ma, Xinming Wu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Borehole breakouts are stress-induced spalling on the borehole wall, which are identifiable in acoustic image logs as paired zones with near-symmetry azimuths, low acoustic amplitudes, and increased borehole radius. Accurate breakout characterization is crucial for in-situ stress analysis. In recent years, deep learning has been introduced to automate the time-consuming and labor-intensive breakout picking process. However, existing approaches often suffer from misclassification of non-breakout features, leading to high false positive rates. To address this limitation, this study develops a deep learning framework, termed Breakout-picker, with a specific focus on reducing false positives in automatic breakout characterization. Breakout-picker reduces false positives through two strategies. First, the training of Breakout-picker incorporates negative samples of non-breakout features, including natural fractures, keyseats, and logging artifacts. They share similar characteristics with breakouts, such as low acoustic amplitude or locally enlarged borehole radius. These negative training samples enables Breakout-picker to better discriminate true breakouts and similar non-breakout features. Second, candidate breakouts identified by Breakout-picker are further validated by azimuthal symmetry criteria, whereby detections that do not exhibit the near-symmetry characteristics of breakout azimuth are excluded. The performance of Breakout-picker is evaluated using three acoustic image log datasets from different regions. The results demonstrate that Breakout-picker outperforms other automatic methods with higher accuracy and substantially lower false positive rates. By reducing false positives, Breakout-picker enhances the reliability of automatic breakout characterization from acoustic image logs, which in turn benefits in-situ stress analysis based on borehole breakouts.

---


### 158. [AstroVLM: Expert Multi-agent Collaborative Reasoning for Astronomical Imaging Quality Diagnosis](https://arxiv.org/abs/2604.16024)

**<font color=#1a73e8>作者：</font>** Yaohui Han, Tianshuo Wang, Zixi Zhao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Vision Language Models (VLMs) have been applied to several specific domains and have shown strong problem-solving capabilities. However, astronomical imaging, a quite complex problem involving multidisciplinary knowledge and several subtasks, has not been adequately studied. Due to the complexity of the astronomical imaging process, both world-class astronomical organizations, such as NASA, and expert enthusiasts devote a great deal of time and effort. This is because the processes in astronomical imaging have complex underlying correlations that significantly influence one another, making the quality diagnosis and error localization of astronomical images challenging. To address this problem, we propose AstroVLM, a collaborative multi-agent system for diagnosing the quality of astronomical images. Experiment results show that AstroVLM outperforms all baselines on real-world astronomical imaging quality diagnosis tasks, providing a reference for language models to handle complicated multi-process tasks.

---


### 159. [Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning](https://arxiv.org/abs/2604.16029)

**<font color=#1a73e8>作者：</font>** Jiaxi Bi, Tongxu Luo, Wenyu Du 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Parallel reasoning enhances Large Reasoning Models (LRMs) but incurs prohibitive costs due to futile paths caused by early errors. To mitigate this, path pruning at the prefix level is essential, yet existing research remains fragmented without a standardized framework. In this work, we propose the first systematic taxonomy of path pruning, categorizing methods by their signal source (internal vs. external) and learnability (learnable vs. non-learnable). This classification reveals the unexplored potential of learnable internal methods, motivating our proposal of STOP (Super TOken for Pruning). Extensive evaluations across LRMs ranging from 1.5B to 20B parameters demonstrate that STOP achieves superior effectiveness and efficiency compared to existing baselines. Furthermore, we rigorously validate the scalability of STOP under varying compute budgets - for instance, boosting GPT-OSS-20B accuracy on AIME25 from 84% to nearly 90% under fixed compute budgets. Finally, we distill our findings into formalized empirical guidelines to facilitate optimal real-world deployment. Code, data and models are available at this https URL

---


### 160. [Ranking XAI Methods for Head and Neck Cancer Outcome Prediction](https://arxiv.org/abs/2604.16034)

**<font color=#1a73e8>作者：</font>** Baoqiang Ma, Djennifer K. Madzia-Madzou, Rosa C.J. Kraaijveld 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> For head and neck cancer (HNC) patients, prognostic outcome prediction can support personalized treatment strategy selection. Improving prediction performance of HNC outcomes has been extensively explored by using advanced artificial intelligence (AI) techniques on PET/CT data. However, the interpretability of AI remains a critical obstacle for its clinical adoption. Unlike previous HNC studies that empirically selected explainable AI (XAI) techniques, we are the first to comprehensively evaluate and rank 13 XAI methods across 24 metrics, covering faithfulness, robustness, complexity and plausibility. Experimental results on the multi-center HECKTOR challenge dataset show large variations across evaluation aspects among different XAI methods, with Integrated Gradients (IG) and DeepLIFT (DL) consistently obtained high rankings for faithfulness, complexity and plausibility. This work highlights the importance of comprehensive XAI method evaluation and can be extended to other medical imaging tasks.

---


### 161. [Modeling Sparse and Bursty Vulnerability Sightings: Forecasting Under Data Constraints](https://arxiv.org/abs/2604.16038)

**<font color=#1a73e8>作者：</font>** Cedric Bonhomme, Alexandre Dulaunoy  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Understanding and anticipating vulnerability-related activity is a major challenge in cyber threat intelligence. This work investigates whether vulnerability sightings, such as proof-of-concept releases, detection templates, or online discussions, can be forecast over time. Building on our earlier work on VLAI, a transformer-based model that predicts vulnerability severity from textual descriptions, we examine whether severity scores can improve time-series forecasting as exogenous variables. We evaluate several approaches for short-term forecasting of sightings per vulnerability. First, we test SARIMAX models with and without log(x+1) transformations and VLAI-derived severity inputs. Although these adjustments provide limited improvements, SARIMAX remains poorly suited to sparse, short, and bursty vulnerability data. In practice, forecasts often produce overly wide confidence intervals and sometimes unrealistic negative values. To better capture the discrete and event-driven nature of sightings, we then explore count-based methods such as Poisson regression. Early results show that these models produce more stable and interpretable forecasts, especially when sightings are aggregated weekly. We also discuss simpler operational alternatives, including exponential decay functions for short forecasting horizons, to estimate future activity without requiring long historical series. Overall, this study highlights both the potential and the limitations of forecasting rare and bursty cyber events, and provides practical guidance for integrating predictive analytics into vulnerability intelligence workflows.

---


### 162. [Elucidating the SNR-t Bias of Diffusion Probabilistic Models](https://arxiv.org/abs/2604.16044)

**<font color=#1a73e8>作者：</font>** Meng Yu, Lei Sun, Jianhao Zeng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Probabilistic Models have demonstrated remarkable performance across a wide range of generative tasks. However, we have observed that these models often suffer from a Signal-to-Noise Ratio-timestep (SNR-t) bias. This bias refers to the misalignment between the SNR of the denoising sample and its corresponding timestep during the inference phase. Specifically, during training, the SNR of a sample is strictly coupled with its timestep. However, this correspondence is disrupted during inference, leading to error accumulation and impairing the generation quality. We provide comprehensive empirical evidence and theoretical analysis to substantiate this phenomenon and propose a simple yet effective differential correction method to mitigate the SNR-t bias. Recognizing that diffusion models typically reconstruct low-frequency components before focusing on high-frequency details during the reverse denoising process, we decompose samples into various frequency components and apply differential correction to each component individually. Extensive experiments show that our approach significantly improves the generation quality of various diffusion models (IDDPM, ADM, DDIM, A-DPM, EA-DPM, EDM, PFGM++, and FLUX) on datasets of various resolutions with negligible computational overhead. The code is at this https URL.

---


### 163. [Driving Assistance System for Ambulances to Minimise the Vibrations in Patient Cabin](https://arxiv.org/abs/2604.16047)

**<font color=#1a73e8>作者：</font>** Abdulaziz Aldegheishem, Nabil Alrajeh, Lorena Parra 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The ambulance service is the main transport for diseased or injured people which suffers the same acceleration forces as regular vehicles. These accelerations, caused by the movement of the vehicle, impact the performance of tasks executed by sanitary personnel, which can affect patient survival or recovery time. In this paper, we have trained, validated, and tested a system to assess driving in ambulance services. The proposed system is composed of a sensor node which measures the vehicle vibrations using an accelerometer. It also includes a GPS sensor, a battery, a display, and a speaker. When two possible routes reach the same destination point, the system compares the two routes based on previously classified data and calculates an index and a score. Thus, the index balances the possible routes in terms of time to reach the destination and the vibrations suffered in the patient cabin to recommend the route that minimises those vibrations. Three datasets are used to train, validate, and test the system. Based on an Artificial Neural network (ANN), the classification model is trained with tagged data classified as low, medium, and high vibrations, and 97% accuracy is achieved. Then, the obtained model is validated using data from three routes of another region. Finally, the system is tested in two new scenarios with two possible routes to reach the destination. The results indicate that the route with less vibration is preferred when there are low time differences (less than 6%) between the two possible routes. Nonetheless, with the current weighting factors, the shortest route is preferred when time differences between routes are higher than 20%, regardless of the higher vibrations in the shortest route.

---


### 164. [TableSeq: Unified Generation of Structure, Content, and Layout](https://arxiv.org/abs/2604.16070)

**<font color=#1a73e8>作者：</font>** Laziz Hamdi, Amine Tamasna, Pascal Boisson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present TableSeq, an image-only, end-to-end framework for joint table structure recognition, content recognition, and cell localization. The model formulates these tasks as a single sequence-generation problem: one decoder produces an interleaved stream of \texttt{HTML} tags, cell text, and discretized coordinate tokens, thereby aligning logical structure, textual content, and cell geometry within a unified autoregressive sequence. This design avoids external OCR, auxiliary decoders, and complex multi-stage post-processing. TableSeq combines a lightweight high-resolution FCN-H16 encoder with a minimal structure-prior head and a single-layer transformer encoder, yielding a compact architecture that remains effective on challenging layouts. Across standard benchmarks, TableSeq achieves competitive or state-of-the-art results while preserving architectural simplicity. It reaches 95.23 TEDS / 96.83 S-TEDS on PubTabNet, 97.45 TEDS / 98.69 S-TEDS on FinTabNet, and 99.79 / 99.54 / 99.66 precision / recall / F1 on SciTSR under the CAR protocol, while remaining competitive on PubTables-1M under GriTS. Beyond TSR/TCR, the same sequence interface generalizes to index-based table querying without task-specific heads, achieving the best IRDR score and competitive ICDR/ICR performance. We also study multi-token prediction for faster blockwise decoding and show that it reduces inference latency with only limited accuracy degradation. Overall, TableSeq provides a practical and reproducible single-stream baseline for unified table recognition, and the source code will be made publicly available at this https URL.

---


### 165. [The Amazing Stability of Flow Matching](https://arxiv.org/abs/2604.16079)

**<font color=#1a73e8>作者：</font>** Rania Briq, Michael Kamp, Ohad Fried 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The success of deep generative models in generating high-quality and diverse samples is often attributed to particular architectures and large training datasets. In this paper, we investigate the impact of these factors on the quality and diversity of samples generated by \emph{flow-matching} models. Surprisingly, in our experiments on CelebA-HQ dataset, flow matching remains stable even when pruning 50\% of the dataset. That is, the quality and diversity of generated samples are preserved. Moreover, pruning impacts the latent representation only slightly, that is, samples generated by models trained on the full and pruned dataset map to visually similar outputs for a given seed. We observe similar stability when changing the architecture or training configuration, such that the latent representation is maintained under these changes as well.
Our results quantify just how strong this stability can be in practice, and help explain the reliability of flow-matching models under various perturbations.

---


### 166. [ProcRoute: Process-Scoped Authorization of Split-Tunnel Routes](https://arxiv.org/abs/2604.16080)

**<font color=#1a73e8>作者：</font>** Arul Thileeban Sagayam  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In most split-tunnel VPN/ZTNA deployments, installing an internal route authorizes the entire device, not a specific application, to use it. An unprivileged malicious process can therefore reach internal services by reusing routes intended for corporate applications. We present ProcRoute, a system that restricts internal-route access to explicitly authorized applications. ProcRoute models route access as an access-control problem: application identities are principals, destination prefixes with port and protocol constraints are resources, and a total, default-deny decision function mediates every connect() and UDP sendmsg() to an internal destination. Processes without a grant retain external access but are denied internal routes under our threat model. We describe ProcRoute's formal model, a Linux prototype built on cgroup v2 and eBPF socket-address hooks, and two complementary evaluations. In a two-machine WireGuard deployment, ProcRoute matches the WireGuard baseline and 13% faster than an nftables cgroup-matching configuration, with a p50 connect latency of 93 $\mu$s (+3.6 $\mu$s over baseline), flat policy scaling to 5,000 prefixes, and sub-millisecond revocation. Single-machine loopback microbenchmarks confirm low hook overhead: 2.7 $\mu$s on the internal-allow path, 82/82 unauthorized pivot attempts blocked, and zero transient allows across 1.2 million connection attempts during policy reload.

---


### 167. [Veritas-RPM: Provenance-Guided Multi-Agent False Positive Suppression for Remote Patient Monitoring](https://arxiv.org/abs/2604.16081)

**<font color=#1a73e8>作者：</font>** Aswini Misro, Vikash Sharma, Shreyank N Gowda  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We present Veritas-RPM, a provenance-guided multi-agent architecture comprising five processing layers: VeritasAgent (ground-truth assembly), SentinelLayer (anomaly detection), DirectorAgent (specialist routing), six domain Specialist Agents, and MetaSentinelAgent (conflict resolution and final decision). We construct a 98-case synthetic taxonomy of false-positive scenarios derived from documented RPM patterns. Synthetic patient epochs (n = 530) were generated directly from taxonomy parameters and processed through the pipeline. Ground-truth labels are known for all cases. Performance is reported as True Suppression Rate (TSR), False Escalation Rate (FER), and Indeterminate Rate (INDR).

---


### 168. [Early Detection of Acute Myeloid Leukemia (AML) Using YOLOv12 Deep Learning Model](https://arxiv.org/abs/2604.16082)

**<font color=#1a73e8>作者：</font>** Enas E. Ahmed, Salah A. Aly, Mayar Moner  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Acute Myeloid Leukemia (AML) is one of the most life-threatening type of blood cancers, and its accurate classification is considered and remains a challenging task due to the visual similarity between various cell types. This study addresses the classification of the multiclasses of AML cells Utilizing YOLOv12 deep learning model. We applied two segmentation approaches based on cell and nucleus features, using Hue channel and Otsu thresholding techniques to preprocess the images prior to classification. Our experiments demonstrate that YOLOv12 with Otsu thresholding on cell-based segmentation achieved the highest level of validation and test accuracy, both reaching 99.3%.

---


### 169. [Unveiling Stochasticity: Universal Multi-modal Probabilistic Modeling for Traffic Forecasting](https://arxiv.org/abs/2604.16084)

**<font color=#1a73e8>作者：</font>** Weijiang Xiong, Robert Fonod, Nikolas Geroliminis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traffic forecasting is a challenging spatio-temporal modeling task and a critical component of urban transportation management. Current studies mainly focus on deterministic predictions, with limited considerations on the uncertainty and stochasticity in traffic dynamics. Therefore, this paper proposes an elegant yet universal approach that transforms existing models into probabilistic predictors by replacing only the final output layer with a novel Gaussian Mixture Model (GMM) layer. The modified model requires no changes to the training pipeline and can be trained using only the Negative Log-Likelihood (NLL) loss, without any auxiliary or regularization terms. Experiments on multiple traffic datasets show that our approach generalizes from classic to modern model architectures while preserving deterministic performance. Furthermore, we propose a systematic evaluation procedure based on cumulative distributions and confidence intervals, and demonstrate that our approach is considerably more accurate and informative than unimodal or deterministic baselines. Finally, a more detailed study on a real-world dense urban traffic network is presented to examine the impact of data quality on uncertainty quantification and to show the robustness of our approach under imperfect data conditions. Code available at this https URL

---


### 170. [Stylistic-STORM (ST-STORM) : Perceiving the Semantic Nature of Appearance](https://arxiv.org/abs/2604.16086)

**<font color=#1a73e8>作者：</font>** Hamed Ouattara, Pierre Duthon, Pascal Houssam Salmane 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> One of the dominant paradigms in self-supervised learning (SSL), illustrated by MoCo or DINO, aims to produce robust representations by capturing features that are insensitive to certain image transformations such as illumination, or geometric changes. This strategy is appropriate when the objective is to recognize objects independently of their appearance. However, it becomes counterproductive as soon as appearance itself constitutes the discriminative signal. In weather analysis, for example, rain streaks, snow granularity, atmospheric scattering, as well as reflections and halos, are not noise: they carry the essential information. In critical applications such as autonomous driving, ignoring these cues is risky, since grip and visibility depend directly on ground conditions and atmospheric conditions. We introduce ST-STORM, a hybrid SSL framework that treats appearance (style) as a semantic modality to be disentangled from content. Our architecture explicitly separates two latent streams, regulated by gating mechanisms. The Content branch aims at a stable semantic representation through a JEPA scheme coupled with a contrastive objective, promoting invariance to appearance variations. In parallel, the Style branch is constrained to capture appearance signatures (textures, contrasts, scattering) through feature prediction and reconstruction under an adversarial constraint. We evaluate ST-STORM on several tasks, including object classification (ImageNet-1K), fine-grained weather characterization, and melanoma detection (ISIC 2024 Challenge). The results show that the Style branch effectively isolates complex appearance phenomena (F1=97% on Multi-Weather and F1=94% on ISIC 2024 with 10% labeled data), without degrading the semantic performance (F1=80% on ImageNet-1K) of the Content branch, and improves the preservation of critical appearance

---


### 171. [The Harder Path: Last Iterate Convergence for Uncoupled Learning in Zero-Sum Games with Bandit Feedback](https://arxiv.org/abs/2604.16087)

**<font color=#1a73e8>作者：</font>** Côme Fiegel, Pierre Ménard, Tadashi Kozuno 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the problem of learning in zero-sum matrix games with repeated play and bandit feedback. Specifically, we focus on developing uncoupled algorithms that guarantee, without communication between players, the convergence of the last-iterate to a Nash equilibrium. Although the non-bandit case has been studied extensively, this setting has only been explored recently, with a bound of $\mathcal{O}(T^{-1/8})$ on the exploitability gap. We show that, for uncoupled algorithms, guaranteeing convergence of the policy profiles to a Nash equilibrium is detrimental to the performance, with the best attainable rate being $\Omega(T^{-1/4})$ in contrast to the usual $\Omega(T^{-1/2})$ rate for convergence of the average iterates. We then propose two algorithms that achieve this optimal rate up to constant and logarithmic factors. The first algorithm leverages a straightforward trade-off between exploration and exploitation, while the second employs a regularization technique based on a two-step mirror descent approach.

---


### 172. [GroupEnvoy: A Conversational Agent Speaking for the Outgroup to Foster Intergroup Relations](https://arxiv.org/abs/2604.16095)

**<font color=#1a73e8>作者：</font>** Koken Hata, Rintaro Chujo, Reina Takamatsu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Conversational agents have the potential to support intergroup relations when psychological or linguistic barriers prevent direct interaction. Based on intergroup contact theory, we propose GroupEnvoy, a conversational agent that represents outgroup perspectives during ingroup discussions, grounded in transcripts from outgroup-only sessions. To evaluate this approach and derive design principles, we conducted a mixed-methods, between-subjects study with university students, where host-country students formed the ingroup and international students formed the outgroup. Ingroup students performed a collaborative task, receiving outgroup perspectives via GroupEnvoy (experimental) or reading written transcripts (control). Compared to the control group, the experimental group showed greater reduction in intergroup anxiety and greater improvement in perspective-taking. Qualitatively, AI-mediated contact enhanced outcome expectancies, whereas passive exposure fostered future contact intentions. The two conditions also elicited empathy toward distinct targets: outgroup evaluations of the ingroup versus outgroup lived experiences. These findings validate AI-mediated contact as a promising paradigm for improving intergroup relations.

---


### 173. [DenTab: A Dataset for Table Recognition and Visual QA on Real-World Dental Estimates](https://arxiv.org/abs/2604.16099)

**<font color=#1a73e8>作者：</font>** Laziz Hamdi, Amine Tamasna, Thierry Paquet  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tables condense key transactional and administrative information into compact layouts, but practical extraction requires more than text recognition: systems must also recover structure (rows, columns, merged cells, headers) and interpret roles such as line items, subtotals, and totals under common capture artifacts. Many existing resources for table structure recognition and TableVQA are built from clean digital-born sources or rendered tables, and therefore only partially reflect noisy administrative conditions.
We introduce DenTab, a dataset of 2{,}000 cropped table images from dental estimates with high-quality HTML annotations, enabling evaluation of table recognition (TR) and table visual question answering (TableVQA) on the same inputs. DenTab includes 2{,}208 questions across eleven categories spanning retrieval, aggregation, and logic/consistency checks. We benchmark 16 systems, including 14 vision--language models (VLMs) and two OCR baselines. Across models, strong structure recovery does not consistently translate into reliable performance on multi-step arithmetic and consistency questions, and these reasoning failures persist even when using ground-truth HTML table inputs.
To improve arithmetic reliability without training, we propose the Table Router Pipeline, which routes arithmetic questions to deterministic execution. The pipeline combines (i) a VLM that produces a baseline answer, a structured table representation, and a constrained table program with (ii) a rule-based executor that performs exact computation over the parsed table. The source code and dataset will be made publicly available at this https URL.

---


### 174. [Polyglot: Multilingual Style Preserving Speech-Driven Facial Animation](https://arxiv.org/abs/2604.16108)

**<font color=#1a73e8>作者：</font>** Federico Nocentini, Kwanggyoon Seo, Qingju Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Speech-Driven Facial Animation (SDFA) has gained significant attention due to its applications in movies, video games, and virtual reality. However, most existing models are trained on single-language data, limiting their effectiveness in real-world multilingual scenarios. In this work, we address multilingual SDFA, which is essential for realistic generation since language influences phonetics, rhythm, intonation, and facial expressions. Speaking style is also shaped by individual differences, not only by language. Existing methods typically rely on either language-specific or speaker-specific conditioning, but not both, limiting their ability to model their interaction. We introduce Polyglot, a unified diffusion-based architecture for personalized multilingual SDFA. Our method uses transcript embeddings to encode language information and style embeddings extracted from reference facial sequences to capture individual speaking characteristics. Polyglot does not require predefined language or speaker labels, enabling generalization across languages and speakers through self-supervised learning. By jointly conditioning on language and style, it captures expressive traits such as rhythm, articulation, and habitual facial movements, producing temporally coherent and realistic animations. Experiments show improved performance in both monolingual and multilingual settings, providing a unified framework for modeling language and personal style in SDFA.

---


### 175. [Sample Complexity Bounds for Stochastic Shortest Path with a Generative Model](https://arxiv.org/abs/2604.16111)

**<font color=#1a73e8>作者：</font>** Jean Tarbouriech, Matteo Pirotta, Michal Valko 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the sample complexity of learning an $\epsilon$-optimal policy in the Stochastic Shortest Path (SSP) problem. We first derive sample complexity bounds when the learner has access to a generative model. We show that there exists a worst-case SSP instance with $S$ states, $A$ actions, minimum cost $c_{\min}$, and maximum expected cost of the optimal policy over all states $B_{\star}$, where any algorithm requires at least $\Omega(SAB_{\star}^3/(c_{\min}\epsilon^2))$ samples to return an $\epsilon$-optimal policy with high probability. Surprisingly, this implies that whenever $c_{\min} = 0$ an SSP problem may not be learnable, thus revealing that learning in SSPs is strictly harder than in the finite-horizon and discounted settings. We complement this lower bound with an algorithm that matches it, up to logarithmic factors, in the general case, and an algorithm that matches it up to logarithmic factors even when $c_{\min} = 0$, but only under the condition that the optimal policy has a bounded hitting time to the goal state.

---


### 176. [Towards In-Context Tone Style Transfer with A Large-Scale Triplet Dataset](https://arxiv.org/abs/2604.16114)

**<font color=#1a73e8>作者：</font>** Yuhai Deng, Huimin She, Wei Shen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tone style transfer for photo retouching aims to adapt the stylistic tone of the reference image to a given content image. However, the lack of high-quality large-scale triplet datasets with stylized ground truth forces existing methods to rely on self-supervised or proxy objectives, which limits model capability. To mitigate this gap, we design a data construction pipeline to build TST100K, a large-scale dataset of 100,000 content-reference-stylized triplets. At the core of this pipeline, we train a tone style scorer to ensure strict stylistic consistency for each triplet. In addition, existing methods typically extract content and reference features independently and then fuse them in a decoder, which may cause semantic loss and lead to inappropriate color transfer and degraded visual aesthetics. Instead, we propose ICTone, a diffusion-based framework that performs tone transfer in an in-context manner by jointly conditioning on both images, leveraging the semantic priors of generative models for semantic-aware transfer. Reward feedback learning using the tone style scorer is further incorporated to improve stylistic fidelity and visual quality. Experiments demonstrate the effectiveness of TST100K, and ICTone achieves state-of-the-art performance on both quantitative metrics and human evaluations.

---


### 177. [SCRIPT: Implementing an Intelligent Tutoring System for Programming in a German University Context](https://arxiv.org/abs/2604.16117)

**<font color=#1a73e8>作者：</font>** Alina Deriyeva, Jesper Dannath, Benjamin Paassen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Practice and extensive exercises are essential in programming education. Intelligent tutoring systems (ITSs) are a viable option to provide individualized hints and advice to programming students even when human tutors are not available. However, prior ITS for programming rarely support the Python programming language, mostly focus on introductory programming, and rarely take recent developments in generative models into account. We aim to establish a novel ITS for Python programming that is highly adaptable, serves both as a teaching and research platform, provides interfaces to plug in hint mechanisms (e.g.\ via large language models), and works inside the particularly challenging regulatory environment of Germany, that is, conforming to the European data protection regulation, the European AI act, and ethical framework of the German Research Foundation. In this paper, we present the description of the current state of the ITS along with future development directions, as well as discuss the challenges and opportunities for improving the system.

---


### 178. [Univariate Channel Fusion for Multivariate Time Series Classification](https://arxiv.org/abs/2604.16119)

**<font color=#1a73e8>作者：</font>** Fernando Moro, Vinicius M. A. Souza  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multivariate time series classification (MTSC) plays a crucial role in various domains, including biomedical signal analysis and motion monitoring. However, existing approaches, particularly deep learning models, often require high computational resources, making them unsuitable for real-time applications or deployment on low-cost hardware, such as IoT devices and wearable systems. In this paper, we propose the Univariate Channel Fusion (UCF) method to deal with MTSC efficiently. UCF transforms multivariate time series into a univariate representation through simple channel fusion strategies such as the mean, median, or dynamic time warping barycenter. This transformation enables the use of any classifier originally designed for univariate time series, providing a flexible and computationally lightweight alternative to complex models. We evaluate UCF in five case studies covering diverse application domains, including chemical monitoring, brain-computer interfaces, and human activity analysis. The results demonstrate that UCF often outperforms baseline methods and state-of-the-art algorithms tailored for MTSC, while achieving substantial gains in computational efficiency, being particularly effective in problems with high inter-channel correlation.

---


### 179. [Motion-Adapter: A Diffusion Model Adapter for Text-to-Motion Generation of Compound Actions](https://arxiv.org/abs/2604.16135)

**<font color=#1a73e8>作者：</font>** Yue Jiang, Mingyu Yang, Liuyuxin Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in generative motion synthesis have enabled the production of realistic human motions from diverse input modalities. However, synthesizing compound actions from texts, which integrate multiple concurrent actions into coherent full-body sequences, remains a major challenge. We identify two key limitations in current text-to-motion diffusion models: (i) catastrophic neglect, where earlier actions are overwritten by later ones due to improper handling of temporal information, and (ii) attention collapse, which arises from excessive feature fusion in cross-attention mechanisms. As a result, existing approaches often depend on overly detailed textual descriptions (e.g., raising right hand), explicit body-part specifications (e.g., editing the upper body), or the use of large language models (LLMs) for body-part interpretation. These strategies lead to deficient semantic representations of physical structures and kinematic mechanisms, limiting the ability to incorporate natural behaviors such as greeting while walking. To address these issues, we propose the Motion-Adapter, a plug-and-play module that guides text-to-motion diffusion models in generating compound actions by computing decoupled cross-attention maps, which serve as structural masks during the denoising process. Extensive experiments demonstrate that our method consistently produces more faithful and coherent compound motions across diverse textual prompts, surpassing state-of-the-art approaches.

---


### 180. [Training Time Prediction for Mixed Precision-based Distributed Training](https://arxiv.org/abs/2604.16145)

**<font color=#1a73e8>作者：</font>** Minchul Kang, Changyong Shin, Jinwoo Jeong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate prediction of training time in distributed deep learning is crucial for resource allocation, cost estimation, and job scheduling. We observe that the floating-point precision setting is a key determinant of training time, leading to training time variations of ~2.4x over its minimum. However, existing studies on distributed training time prediction rely on static model computation graphs that do not capture precision variations, including mixed precision. According to our experiments, training time prediction without considering precision results in significant prediction errors - reaching up to 147.85% in mean absolute percentage error (MAPE). To address this issue, we propose a precision-aware distributed training time predictor that achieves robust accuracy across diverse precision settings, including mixed precision, with 9.8% MAPE.

---


### 181. [SWNet: A Cross-Spectral Network for Camouflaged Weed Detection](https://arxiv.org/abs/2604.16147)

**<font color=#1a73e8>作者：</font>** Henry O. Velesaca, Luigi Miranda, Angel D. Sappa  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents SWNet, a bimodal end-to-end cross-spectral network specifically engineered for the detection of camouflaged weeds in dense agricultural environments. Plant camouflage, characterized by homochromatic blending where invasive species mimic the phenotypic traits of primary crops, poses a significant challenge for traditional computer vision systems. To overcome these limitations, SWNet utilizes a Pyramid Vision Transformer v2 backbone to capture long-range dependencies and a Bimodal Gated Fusion Module to dynamically integrate Visible and Near-Infrared information. By leveraging the physiological differences in chlorophyll reflectance captured in the NIR spectrum, the proposed architecture effectively discriminates targets that are otherwise indistinguishable in the visible range. Furthermore, an Edge-Aware Refinement module is employed to produce sharper object boundaries and reduce structural ambiguity. Experimental results on the Weeds-Banana dataset indicate that SWNet outperforms ten state-of-the-art methods. The study demonstrates that the integration of cross-spectral data and boundary-guided refinement is essential for high segmentation accuracy in complex crop canopies. The code is available on GitHub: this https URL

---


### 182. [MARCH: Multi-Agent Radiology Clinical Hierarchy for CT Report Generation](https://arxiv.org/abs/2604.16175)

**<font color=#1a73e8>作者：</font>** Yi Lin, Yihao Ding, Yonghui Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated 3D radiology report generation often suffers from clinical hallucinations and a lack of the iterative verification found in human practice. While recent Vision-Language Models (VLMs) have advanced the field, they typically operate as monolithic "black-box" systems without the collaborative oversight characteristic of clinical workflows. To address these challenges, we propose MARCH (Multi-Agent Radiology Clinical Hierarchy), a multi-agent framework that emulates the professional hierarchy of radiology departments and assigns specialized roles to distinct agents. MARCH utilizes a Resident Agent for initial drafting with multi-scale CT feature extraction, multiple Fellow Agents for retrieval-augmented revision, and an Attending Agent that orchestrates an iterative, stance-based consensus discourse to resolve diagnostic discrepancies. On the RadGenome-ChestCT dataset, MARCH significantly outperforms state-of-the-art baselines in both clinical fidelity and linguistic accuracy. Our work demonstrates that modeling human-like organizational structures enhances the reliability of AI in high-stakes medical domains.

---


### 183. [Winner of CVPR2026 NTIRE Challenge on Image Shadow Removal: Semantic and Geometric Guidance for Shadow Removal via Cascaded Refinement](https://arxiv.org/abs/2604.16177)

**<font color=#1a73e8>作者：</font>** Lorenzo Beltrame, Jules Salzinger, Filip Svoboda 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a three-stage progressive shadow-removal pipeline for the CVPR2026 NTIRE WSRD+ challenge. Built on OmniSR, our method treats deshadowing as iterative direct refinement, where later stages correct residual artefacts left by earlier predictions. The model combines RGB appearance with frozen DINOv2 semantic guidance and geometric cues from monocular depth and surface normals, reused across all stages. To stabilise multi-stage optimisation, we introduce a contraction-constrained objective that encourages non-increasing reconstruction error across the cascade. A staged training pipeline transfers from earlier WSRD pretraining to WSRD+ supervision and final WSRD+ 2026 adaptation with cosine-annealed checkpoint ensembling. On the official WSRD+ 2026 hidden test set, our final ensemble achieved 26.680 PSNR, 0.8740 SSIM, 0.0578 LPIPS, and 26.135 FID, ranked first overall, and won the NTIRE 2026 Image Shadow Removal Challenge. The strong performance of the proposed model is further validated on the ISTD+ and UAV-SC+ datasets.

---


### 184. [Synthetic data in cryptocurrencies using generative models](https://arxiv.org/abs/2604.16182)

**<font color=#1a73e8>作者：</font>** André Saimon S. Sousa, Otto Pires, Frank Acasiete 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data plays a fundamental role in consolidating markets, services, and products in the digital financial ecosystem. However, the use of real data, especially in the financial context, can lead to privacy risks and access restrictions, affecting institutions, research, and modeling processes. Although not all financial datasets present such limitations, this work proposes the use of deep learning techniques for generating synthetic data applied to cryptocurrency price time series. The approach is based on Conditional Generative Adversarial Networks (CGANs), combining an LSTM-type recurrent generator and an MLP discriminator to produce statistically consistent synthetic data. The experiments consider different crypto-assets and demonstrate that the model is capable of reproducing relevant temporal patterns, preserving market trends and dynamics. The generation of synthetic series through GANs is an efficient alternative for simulating financial data, showing potential for applications such as market behavior analysis and anomaly detection, with lower computational cost compared to more complex generative approaches.

---


### 185. [Saturation-Aware Space-Variant Blind Image Deblurring](https://arxiv.org/abs/2604.16200)

**<font color=#1a73e8>作者：</font>** Muhammad Z. Alam, Larry Stetsiuk, Arooba Zeshan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents a novel saturation aware space variant blind image deblurring framework designed to address challenges posed by saturated pixels in deblurring under high dynamic range and low light conditions. The proposed approach effectively segments the image based on blur intensity and proximity to saturation, leveraging a pre estimated Light Spread Function to mitigate stray light effects. By accurately estimating the true radiance of saturated regions using the dark channel prior, our method enhances the deblurring process without introducing artifacts like ringing. Experimental evaluations on both synthetic and real world datasets demonstrate that the framework improves deblurring outcomes across various scenarios showcasing superior performance compared to state of the art saturation-aware and general purpose methods. This adaptability highlights the framework potential integration with existing and emerging blind image deblurring techniques.

---


### 186. [Investigating Conversational Agents to Support Secondary School Students Learning CSP](https://arxiv.org/abs/2604.16213)

**<font color=#1a73e8>作者：</font>** Matthew Frazier, Kostadin Damevski, Lori Pollock  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Secondary school students enrolled in the AP Computer Science Principles (CSP) course commonly utilize web resources (e.g., tutorials, Q\&A sites) to better understand key concepts in the curriculum. The primary obstacle to using these resources is finding information appropriate for the learning task and student's background. In addition to web search, conversational agents are increasingly a viable alternative for CSP students. In this paper, we study the potential of conversational agents to aid secondary school students as they acquire knowledge on CSP concepts. We explore general purpose, generative conversational agents (e.g., ChatGPT) and custom, fixed-response conversational agents built specifically to aid CSP students. We present results from classroom use by 45 high school students in grades 9-11 (ages 14-17) across six CSP sections. Our main contributions are in better understanding how conversational agents can help CSP students and an evaluation of the effectiveness and engagement of different approaches for CSP exploratory search.

---


### 187. [OT on the Map: Quantifying Domain Shifts in Geographic Space](https://arxiv.org/abs/2604.16220)

**<font color=#1a73e8>作者：</font>** Haoran Zhang, Livia Betti, Konstantin Klemmer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In computer vision and machine learning for geographic data, out-of-domain generalization is a pervasive challenge, arising from uneven global data coverage and distribution shifts across geographic regions. Though models are frequently trained in one region and deployed in another, there is no principled method for determining when this cross-region adaptation will be successful. A well-defined notion of distance between distributions can effectively quantify how different a new target domain is compared to the domains used for model training, which in turn could support model training and deployment decisions. In this paper, we propose a strategy for computing distances between geospatial domains that leverages geographic information with Optimal Transport methods (GeoSpOT). In our experiments, GeoSpOT distances emerge as effective predictors of cross-domain transfer difficulty. We further demonstrate that embeddings from pretrained location encoders provide information comparable to image/text embeddings, despite relying solely on longitude-latitude pairs as input. This allows users to get an approximation of out-of-domain performance for geospatial models, even when the exact downstream task is unknown, or no task-specific data is available. Building on these findings, we show that GeoSpOT distances can preemptively guide data selection and enable predictive tools to analyze regions where a model is likely to underperform.

---


### 188. ["Taking Stock at FAccT": Using Participatory Design to Co-Create a Vision for the Fairness, Accountability and Transparency Community](https://arxiv.org/abs/2604.16224)

**<font color=#1a73e8>作者：</font>** Shiran Dudy, Jan Simson, Yanan Long  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As a relatively new forum, ACM FAccT has become a key space for activists and scholars to critically examine emerging AI and ML technologies. It brings together academics, civil society members, and government representatives from diverse fields to explore the broader societal impacts of both deployed and proposed technologies. We report a large-scale participatory design (PD) process for reflexive conference governance, which combined an in-person CRAFT session, an asynchronous Polis poll and the synthesis of a governance-facing report for the FAccT leadership. Participants shaped the substantive agenda by authoring seed statements, adding new statements and making patterns of agreement, disagreement and uncertainty made visible through this http URL endeavors represent one of the the first instances of applying PD to a venue that critically interrogates the societal impacts of AI, fostering a niche in which critical scholars are free to voice their concerns. Finally, this work advances large-scale PD theory by providing an effective case study of a co-design paradigm that can readily scale temporally and epistemologically.

---


### 189. [Dental Panoramic Radiograph Analysis Using YOLO26 From Tooth Detection to Disease Diagnosis](https://arxiv.org/abs/2604.16231)

**<font color=#1a73e8>作者：</font>** Khawaja Azfar Asif, Rafaqat Alam Khan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Panoramic radiography is a fundamental diagnostic tool in dentistry, offering a comprehensive view of the entire dentition with minimal radiation exposure. However, manual interpretation is time-consuming and prone to errors, especially in high-volume clinical settings. This creates a pressing need for efficient automated solutions. This study presents the first application of YOLOv26 for automated tooth detection, FDI-based numbering, and dental disease segmentation in panoramic radiographs. The DENTEX dataset was preprocessed using Roboflow for format conversion and augmentation, yielding 1,082 images for tooth enumeration and 1,040 images for disease segmentation across four pathology classes. Five YOLOv26-seg variants were trained on Google Colab using transfer learning at a resolution of 800x800. Results demonstrate that the YOLOv26m-seg model achieved the best performance for tooth enumeration, with a precision of 0.976, recall of 0.970, and box mAP50 of 0.976. It outperformed the YOLOv8x baseline by 4.9% in precision and 3.3% in mAP50, while also enabling high-quality mask-level segmentation (mask mAP50 = 0.970). For disease segmentation, the YOLOv26l-seg model attained a box mAP50 of 0.591 and a mask mAP50 of 0.547. Impacted teeth showed the highest per-class average precision (0.943), indicating that visual distinctiveness influences detection performance more than annotation quantity. Overall, these findings demonstrate that YOLOv26-based models offer a robust and accurate framework for automated dental image analysis, with strong potential to enhance diagnostic efficiency and consistency in clinical practice.

---


### 190. [Neuro-Symbolic ODE Discovery with Latent Grammar Flow](https://arxiv.org/abs/2604.16232)

**<font color=#1a73e8>作者：</font>** Karin Yu, Eleni Chatzi, Georgios Kissas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding natural and engineered systems often relies on symbolic formulations, such as differential equations, which provide interpretability and transferability beyond black-box models.
We introduce Latent Grammar Flow (LGF), a neuro-symbolic generative framework for discovering ordinary differential equations from data. LGF embeds equations as grammar-based representations into a discrete latent space and forces semantically similar equations to be positioned closer together with a behavioural loss. Then, a discrete flow model guides the sampling process to recursively generate candidate equations that best fit the observed data. Domain knowledge and constraints, such as stability, can be either embedded into the rules or used as conditional predictors.

---


### 191. [A Two-Stage, Object-Centric Deep Learning Framework for Robust Exam Cheating Detection](https://arxiv.org/abs/2604.16234)

**<font color=#1a73e8>作者：</font>** Van-Truong Le, Le-Khanh Nguyen, Trong-Doanh Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Academic integrity continues to face the persistent challenge of examination cheating. Traditional invigilation relies on human observation, which is inefficient, costly, and prone to errors at scale. Although some existing AI-powered monitoring systems have been deployed and trusted, many lack transparency or require multi-layered architectures to achieve the desired performance. To overcome these challenges, we propose an improvement over a simple two-stage framework for exam cheating detection that integrates object detection and behavioral analysis using well-known technologies. First, the state-of-the-art YOLOv8n model is used to localize students in exam-room images. Each detected region is cropped and preprocessed, then classified by a fine-tuned RexNet-150 model as either normal or cheating behavior. The system is trained on a dataset compiled from 10 independent sources with a total of 273,897 samples, achieving 0.95 accuracy, 0.94 recall, 0.96 precision, and 0.95 F1-score - a 13\% increase over a baseline accuracy of 0.82 in video-based cheating detection. In addition, with an average inference time of 13.9 ms per sample, the proposed approach demonstrates robustness and scalability for deployment in large-scale environments. Beyond the technical contribution, the AI-assisted monitoring system also addresses ethical concerns by ensuring that final outcomes are delivered privately to individual students after the examination, for example, via personal email. This prevents public exposure or shaming and offers students an opportunity to reflect on their behavior. For further improvement, it is possible to incorporate additional factors, such as audio data and consecutive frames, to achieve greater accuracy. This study provides a foundation for developing real-time, scalable, ethical, and open-source solutions.

---


### 192. [Enhancing AI and Dynamical Subseasonal Forecasts with Probabilistic Bias Correction](https://arxiv.org/abs/2604.16238)

**<font color=#1a73e8>作者：</font>** Hannah Guan, Soukayna Mouatadid, Paulo Orenstein 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decision-makers rely on weather forecasts to plant crops, manage wildfires, allocate water and energy, and prepare for weather extremes. Today, such forecasts enjoy unprecedented accuracy out to two weeks thanks to steady advances in physics-based dynamical models and data-driven artificial intelligence (AI) models. However, model skill drops precipitously at subseasonal timescales (2 - 6 weeks ahead), due to compounding errors and persistent biases. To counter this degradation, we introduce probabilistic bias correction (PBC), a machine learning framework that substantially reduces systematic error by learning to correct historical probabilistic forecasts. When applied to the leading dynamical and AI models from the European Centre for Medium-Range Weather Forecasts (ECMWF), PBC doubles the subseasonal skill of the AI Forecasting System and improves the skill of the operationally-debiased dynamical model for 91% of pressure, 92% of temperature, and 98% of precipitation targets. We designed PBC for operational deployment, and, in ECMWF's 2025 real-time forecasting competition, its global forecasts placed first for all weather variables and lead times, outperforming the dynamical models from six operational forecasting centers, an international dynamical multi-model ensemble, ECMWF's AI Forecasting System, and the forecasting systems of 34 teams worldwide. These probabilistic skill gains translate into more accurate prediction of extreme events and have the potential to improve agricultural planning, energy management, and disaster preparedness in vulnerable communities.

---


### 193. [CollideNet: Hierarchical Multi-scale Video Representation Learning with Disentanglement for Time-To-Collision Forecasting](https://arxiv.org/abs/2604.16240)

**<font color=#1a73e8>作者：</font>** Nishq Poorav Desai, Ali Etemad, Michael Greenspan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Time-to-Collision (TTC) forecasting is a critical task in collision prevention, requiring precise temporal prediction and comprehending both local and global patterns encapsulated in a video, both spatially and temporally. To address the multi-scale nature of video, we introduce a novel spatiotemporal hierarchical transformer-based architecture called CollideNet, specifically catered for effective TTC forecasting. In the spatial stream, CollideNet aggregates information for each video frame simultaneously at multiple resolutions. In the temporal stream, along with multi-scale feature encoding, CollideNet also disentangles the non-stationarity, trend, and seasonality components. Our method achieves state-of-the-art performance in comparison to prior works on three commonly used public datasets, setting a new state-of-the-art by a considerable margin. We conduct cross-dataset evaluations to analyze the generalization capabilities of our method, and visualize the effects of disentanglement of the trend and seasonality components of the video data. We release our code at this https URL.

---


### 194. [Detecting and Suppressing Reward Hacking with Gradient Fingerprints](https://arxiv.org/abs/2604.16242)

**<font color=#1a73e8>作者：</font>** Songtao Wang, Quang Hieu Pham, Fangcong Yin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) typically optimizes for outcome rewards without imposing constraints on intermediate reasoning. This leaves training susceptible to reward hacking, where models exploit loopholes (e.g., spurious patterns in training data) in the reward function to achieve high scores without solving the intended task. These reward-hacking behaviors are often implicit, as the intermediate chain-of-thought (CoT) may appear plausible on the surface, limiting the effectiveness of purely text-based monitoring. We propose Gradient Fingerprint (GRIFT), a method for detecting reward hacking using models' internal computations. Given a prompt and a model-generated CoT, GRIFT computes gradients of the CoT conditioned on the prompt and compresses them into a compact representation, which is then used to assess whether the CoT reflects reward hacking behavior. Across verifiable reasoning benchmarks spanning math, code, and logical reasoning, GRIFT substantially outperforms strong baselines, including CoT Monitor and TRACE, achieving over 25% relative improvement in detecting reward hacking behavior. Moreover, integrating GRIFT into the rejection fine-tuning pipeline for reasoning tasks reduces reward hacking and improves performance on the true task objective. Our results highlight a promising direction of leveraging gradient level representations for assessing the quality of CoT reasoning traces. Our code is available at: this https URL.

---


### 195. [Find, Fix, Reason: Context Repair for Video Reasoning](https://arxiv.org/abs/2604.16243)

**<font color=#1a73e8>作者：</font>** Haojian Huang, Chuanyu Qin, Yinchuan Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning has advanced video reasoning in large multi-modal models, yet dominant pipelines either rely on on-policy self-exploration, which plateaus at the model's knowledge boundary, or hybrid replay that mixes policies and demands careful regularization. Dynamic context methods zoom into focused evidence but often require curated pretraining and two-stage tuning, and their context remains bounded by a small model's capability. In contrast, larger models excel at instruction following and multi-modal understanding, can supply richer context to smaller models, and rapidly zoom in on target regions via simple tools. Building on this capability, we introduce an observation-level intervention: a frozen, tool-integrated teacher identifies the missing spatiotemporal dependency and provides a minimal evidence patch (e.g., timestamps, regions etc.) from the original video while the question remains unchanged. The student answers again with the added context, and training updates with a chosen-rollout scheme integrated into Group Relative Policy Optimization (GRPO). We further propose a Robust Improvement Reward (RIR) that aligns optimization with two goals: outcome validity through correct answers and dependency alignment through rationales that reflect the cited evidence. Advantages are group-normalized across the batch, preserving on-policy exploration while directing it along causally meaningful directions with minimal changes to the training stack. Experiments on various related benchmarks show consistent accuracy gains and strong generalization. Web page and source code will be available at this https URL.

---


### 196. [Beyond Distribution Sharpening: The Importance of Task Rewards](https://arxiv.org/abs/2604.16259)

**<font color=#1a73e8>作者：</font>** Sarthak Mittal, Leo Gagnon, Guillaume Lajoie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Frontier models have demonstrated exceptional capabilities following the integration of task-reward-based reinforcement learning (RL) into their training pipelines, enabling systems to evolve from pure reasoning models into sophisticated agents. However, debate persists regarding whether RL genuinely instills new skills within a base model or merely sharpens its existing distribution to elicit latent capabilities. To address this dichotomy, we present an explicit comparison between distribution sharpening and task-reward-based learning, utilizing RL as a tool to implement both paradigms. Our analysis reveals the inherent limitations of distribution sharpening, demonstrating from first principles how and why the optima can be unfavorable and the approach fundamentally unstable. Furthermore, our experiments using Llama-3.2-3B-Instruct, Qwen2.5-3B-Instruct and Qwen3-4B-Instruct-2507 on math datasets confirm that sharpening yields limited gains, whereas incorporating task-based reward signal can greatly help achieve robust performance improvements and stable learning.

---


### 197. [FL-MHSM: Spatially-adaptive Fusion and Ensemble Learning for Flood-Landslide Multi-Hazard Susceptibility Mapping at Regional Scale](https://arxiv.org/abs/2604.16265)

**<font color=#1a73e8>作者：</font>** Aswathi Mundayatt, Jaya Sreevalsan-Nair  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing multi-hazard susceptibility mapping (MHSM) studies often rely on spatially uniform models, treat hazards independently, and provide limited representation of cross-hazard dependence and uncertainty. To address these limitations, this study proposes a deep learning (DL) workflow for joint flood-landslide multi-hazard susceptibility mapping (FL-MHSM) that combines two-level spatial partitioning, probabilistic Early Fusion (EF), a tree-based Late Fusion (LF) baseline, and a soft-gating Mixture of Experts (MoE) model, with MoE serving as final predictive model. The proposed design preserves spatial heterogeneity through zonal partitions and enables data-parallel large-area prediction using overlapping lattice grids. In Kerala, EF remained competitive with LF, improving flood recall from 0.816 to 0.840 and reducing Brier score from 0.092 to 0.086, while MoE provided strongest performance for flood susceptibility, achieving an AUC-ROC of 0.905, recall of 0.930, and F1-score of 0.722. In Nepal, EF similarly improved flood recall from 0.820 to 0.858 and reduced Brier score from 0.057 to 0.049 relative to LF, while MoE outperformed both EF and LF for landslide susceptibility, achieving an AUC-ROC of 0.914, recall of 0.901, and F1-score of 0.559. GeoDetector analysis of MoE outputs further showed that dominant factors varied more across zones in Kerala, where susceptibility was shaped by different combinations of topographic, land-cover, and drainage-related controls, while Nepal showed a more consistent influence of topographic and glacier-related factors across zones. These findings show that EF and LF provide complementary predictive behavior, and that their spatially adaptive integration through MoE yields robust overall predictive performance for FL-MHSM while supporting interpretable characterization of multi-hazard susceptibility in spatially heterogeneous landscapes.

---


### 198. [Hero-Mamba: Mamba-based Dual Domain Learning for Underwater Image Enhancement](https://arxiv.org/abs/2604.16266)

**<font color=#1a73e8>作者：</font>** Tejeswar Pokuri, Shivarth Rai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Underwater images often suffer from severe degradation, such as color distortion, low contrast, and blurred details, due to light absorption and scattering in water. While learning-based methods like CNNs and Transformers have shown promise, they face critical limitations: CNNs struggle to model the long-range dependencies needed for non-uniform degradation, and Transformers incur quadratic computational complexity, making them inefficient for high-resolution images. To address these challenges, we propose Hero-Mamba, a novel Mamba-based network that achieves efficient dual-domain learning for underwater image enhancement. Our approach uniquely processes information from both the spatial domain (RGB image) and the spectral domain (FFT components) in parallel. This dual-domain input allows the network to decouple degradation factors, separating color/brightness information from texture/noise. The core of our network utilizes Mamba-based SS2D blocks to capture global receptive fields and long-range dependencies with linear complexity, overcoming the limitations of both CNNs and Transformers. Furthermore, we introduce a ColorFusion block, guided by a background light prior, to restore color information with high fidelity. Extensive experiments on the LSUI and UIEB benchmark datasets demonstrate that Hero-Mamba outperforms state-of-the-art methods. Notably, our model achieves a PSNR of 25.802 and an SSIM of 0.913 on LSUI, validating its superior performance and generalization capabilities.

---


### 199. [VEFX-Bench: A Holistic Benchmark for Generic Video Editing and Visual Effects](https://arxiv.org/abs/2604.16272)

**<font color=#1a73e8>作者：</font>** Xiangbo Gao, Sicong Jiang, Bangya Liu 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As AI-assisted video creation becomes increasingly practical, instruction-guided video editing has become essential for refining generated or captured footage to meet professional requirements. Yet the field still lacks both a large-scale human-annotated dataset with complete editing examples and a standardized evaluator for comparing editing systems. Existing resources are limited by small scale, missing edited outputs, or the absence of human quality labels, while current evaluation often relies on expensive manual inspection or generic vision-language model judges that are not specialized for editing quality. We introduce VEFX-Dataset, a human-annotated dataset containing 5,049 video editing examples across 9 major editing categories and 32 subcategories, each labeled along three decoupled dimensions: Instruction Following, Rendering Quality, and Edit Exclusivity. Building on VEFX-Dataset, we propose VEFX-Reward, a reward model designed specifically for video editing quality assessment. VEFX-Reward jointly processes the source video, the editing instruction, and the edited video, and predicts per-dimension quality scores via ordinal regression. We further release VEFX-Bench, a benchmark of 300 curated video-prompt pairs for standardized comparison of editing systems. Experiments show that VEFX-Reward aligns more strongly with human judgments than generic VLM judges and prior reward models on both standard IQA/VQA metrics and group-wise preference evaluation. Using VEFX-Reward as an evaluator, we benchmark representative commercial and open-source video editing systems, revealing a persistent gap between visual plausibility, instruction following, and edit locality in current models.

---


### 200. [Geometric regularization of autoencoders via observed stochastic dynamics](https://arxiv.org/abs/2604.16282)

**<font color=#1a73e8>作者：</font>** Sean Hill, Felix X.-F. Ye  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Stochastic dynamical systems with slow or metastable behavior evolve, on long time scales, on an unknown low-dimensional manifold in high-dimensional ambient space. Building a reduced simulator from short-burst ambient ensembles is a long-standing problem: local-chart methods like ATLAS suffer from exponential landmark scaling and per-step reprojection, while autoencoder alternatives leave tangent-bundle geometry poorly constrained, and the errors propagate into the learned drift and diffusion. We observe that the ambient covariance~$\Lambda$ already encodes coordinate-invariant tangent-space information, its range spanning the tangent bundle. Using this, we construct a tangent-bundle penalty and an inverse-consistency penalty for a three-stage pipeline (chart learning, latent drift, latent diffusion) that learns a single nonlinear chart and the latent SDE. The penalties induce a function-space metric, the $\rho$-metric, strictly weaker than the Sobolev $H^1$ norm yet achieving the same chart-quality generalization rate up to logarithmic factors. For the drift, we derive an encoder-pullback target via Itô's formula on the learned encoder and prove a bias decomposition showing the standard decoder-side formula carries systematic error for any imperfect chart. Under a $W^{2,\infty}$ chart-convergence assumption, chart-level error propagates controllably to weak convergence of the ambient dynamics and to convergence of radial mean first-passage times. Experiments on four surfaces embedded in up to $201$ ambient dimensions reduce radial MFPT error by $50$--$70\%$ under rotation dynamics and achieve the lowest inter-well MFPT error on most surface--transition pairs under metastable Müller--Brown Langevin dynamics, while reducing end-to-end ambient coefficient errors by up to an order of magnitude relative to an unregularized autoencoder.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-203](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
