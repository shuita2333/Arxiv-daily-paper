# 📦 其他研究 | 2026年05月23日

> 本类共 **347** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-347](./part-07.md)

---

### 101. [From TF-IDF to Transformers: A Comparative and Ensemble Approach to Sentiment Classification](https://arxiv.org/abs/2605.22003)

**<font color=#1a73e8>作者：</font>** Dip Biswas Shanto, Mitali Yadav, Prajwal Panth 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sentiment analysis, also referred to as opinion mining, primarily tries to extract opinion from any text-based data. In the context of movie reviews and critics, sentimental analysis can be a helpful tool to predict whether a movie review is generally positive or negative. It can be difficult for the ML models to understand the context or metaphysical sentiment accurately, as ML models rely largely on statistical word representations. The objective of this paper is to examine and categorise movie reviews into positive and negative sentiments. Diverse machine learning models are considered in doing so, and Natural Language Processing (NLP) methodologies are employed for data preprocessing and model assessment. The IMDb dataset is used. Specifically, Naive Bayes, Logistic Regression, Support Vector Machines (SVM), LightGBM, LSTM, and transformer-based models such as RoBERTa and DistilBERT were evaluated. After a lot of testing with accuracy, precision, recall, F1-score, and ROC-AUC, RoBERTa performed better than all the other models, with an accuracy of 93.02%. A soft voting ensemble that combined all the models also improved classification performance, showing that model ensembling works well for sentiment analysis.

---


### 102. [Rethinking Token Reduction for Diffusion Models via Output-Similarity-Awareness](https://arxiv.org/abs/2605.22011)

**<font color=#1a73e8>作者：</font>** Hangyeol Lee, Hyojeong Lee, Joo-Young Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformers (DiTs) achieve superior image generation quality but suffer from quadratic computational complexity relative to token count. While various token reduction (TR) methods have been proposed to mitigate this cost, they overlook the primary objective of generative models: minimizing recovery error, which requires reflecting output token similarity. They rely solely on input token similarity inherited from reduction-only ViT paradigms, leading to a fundamental misalignment with this objective.
To bridge this gap, we propose DiTo, a novel TR paradigm that shifts the focus toward output-centric token reduction. Based on the observation that output token similarity is consistently preserved across adjacent timesteps, DiTo utilizes prior-step similarities as an effective proxy to establish token correspondences at a Matching timestep, which are then reused across multiple subsequent Reduction timesteps. To optimize this interleaved scheduling, we propose Pair Match Ratio (PMR)-guided Interval Scheduling to determine the optimal matching frequency. Furthermore, to mitigate localized approximation errors and resulting blocking artifacts caused by repeated reuse, we propose Frequency-aware Token Matching by incorporating a selection-frequency penalty. Extensive experiments demonstrate that DiTo consistently outperforms existing TR methods with 1.6-3.9 dB higher PSNR at comparable speedups, achieving a superior Pareto frontier.

---


### 103. [ORBIS: Output-Guided Token Reduction with Distribution-Aware Matching for Video Diffusion Acceleration](https://arxiv.org/abs/2605.22015)

**<font color=#1a73e8>作者：</font>** Hangyeol Lee, Joo-Young Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformer (DiT) has emerged as a powerful model architecture for generating high-quality images and videos. In the case of video DiT, 3D Spatio-Temporal Attention increases token length in proportion to the number of frames, sharply increasing computational cost. Token reduction methods mitigate this cost by exploiting spatial redundancy, but existing approaches rely on inaccurate similarity estimates and lightweight matching algorithms, resulting in poor matching quality and only marginal acceleration.
To overcome these limitations, we propose ORBIS, an SW-HW co-designed accelerator for video DiT. ORBIS leverages the output activation from the previous timestep to obtain more accurate inter-token similarity, substantially improving matching quality and enabling a higher token reduction ratio. We further introduce a Distribution-Aware Token Matching (DATM) algorithm that captures global token distribution and explicitly minimizes token-pair loss for additional gains. To fully hide DATM latency, we design specialized, deeply pipelined hardware and minimize its hardware cost through quantization, occupying only 2.4% of total area with negligible accuracy loss. Extensive experiments show that ORBIS achieves about 2x higher token reduction ratio than the state-of-the-art approach, AsymRnR, while delivering up to 4.5x speedup and 79.3% energy reduction compared to an NVIDIA A100 GPU.

---


### 104. [Diverse Yet Consistent: Context-Guided Diffusion with Energy-Based Joint Refinement for Multi-Agent Motion Prediction](https://arxiv.org/abs/2605.22017)

**<font color=#1a73e8>作者：</font>** Lei Chu, Yuhuan Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deepgenerative models havebecomeapromisingapproach for human motion prediction due to their ability to capture multimodal distributions and represent diverse human be haviors. However, generating predictions that are both di verse and jointly consistent among interacting agents re mains challenging. In addition, most existing approaches are primarily evaluated using single-agent (marginal) met rics, which fail to fully reflect the joint dynamics of multi agent interactions. We propose a diffusion-based frame work that improves multi-agent motion prediction by lever aging rich contextual information from historical trajecto ries. This information is incorporated through a guidance mechanism to enhance the diversity and expressiveness of predicted motions. To further enforce interaction consis tency, we introduce an energy-based formulation that re fines the joint trajectory distribution while preserving the plausibility of individual trajectories. Extensive experi ments on four benchmark datasets demonstrate that our approach consistently outperforms existing methods. No tably, our approach substantially improves both marginal (ADE/FDE) and joint (JADE/JFDE) metrics on ETH/UCY over strong marginal baselines. Compared with prior joint prediction methods, it delivers significant gains in marginal metrics while maintaining competitive joint performance.

---


### 105. [FRED: A Multi-Modal Autonomous Driving Dataset for Flooded Road Environments](https://arxiv.org/abs/2605.22018)

**<font color=#1a73e8>作者：</font>** Connor Malone, Sebastien Demmel, Sebastien Glaser  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The Flooded Road Environments Dataset (FRED) is, to our knowledge, the first multi-modal autonomous driving dataset specifically targeting the collection of data from scenarios involving water hazards on the road. The dataset contains images from a 2.3 MP FLIR Blackfly USB3 camera, 64-beam 360$^\circ$ point clouds from an Ouster OS1-64 LiDAR, and data from an iXblue ATLANS-C IMU corrected by a Geoflex RTK GNSS, from five separate locations captured both during and after flooding events. The data has been released in two formats: a KITTI-style format for easy integration with existing data tools, and the RTMaps format for direct replay of the vehicle's data capture. We provide semantic labels to enable the training and evaluation of both single-sensor and sensor-fusion methods for water hazard detection. Position and velocity, as well as data captured under dry conditions, are provided to enable the development of location-based detection methods that may incorporate maps, and to evaluate other tasks such as localisation and SLAM.

---


### 106. [ForeSplat: Optimization-Aware Foresight for Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2605.22020)

**<font color=#1a73e8>作者：</font>** Yuke Li, Weihang Liu, Cheng Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D Gaussian Splatting (3DGS) models offer fast single-pass reconstruction,but scaling them to match per-scene optimization quality is fundamentally hindered by the scarcity of large-scale 3D annotations.A practical compromise is predict-then-refine,where post-prediction optimization compensates for the limited capacity of the feed-forward this http URL,standard feed-forward 3DGS is trained solely for zero-step rendering error,ignoring whether its output constitutes a good initialization for the downstream this http URL present ForeSplat,an optimization-aware training framework that equips feed-forward 3DGS models to produce initializations explicitly designed for rapid,effective this http URL offloading part of the scene-modeling burden to the optimizer,ForeSplat substantially reduces the capacity pressure on the feed-forward model,making high-quality reconstruction feasible even with compact this http URL its core is MetaGrad,a lightweight multi-anchor meta-gradient training rule that bypasses costly higher-order differentiation through the 3DGS this http URL unrolls a short inner-loop refinement trajectory,samples anchor states,and back-propagates aggregated first-order gradients to the prediction head as a surrogate optimization-aware this http URL fine-tuning adds no inference cost and enables high-quality reconstruction within seconds after a few refinement this http URL instantiate ForeSplat on diverse backbones,including AnySplat,Pi3X,and a distilled variant tailored for edge this http URL all tested architectures,a ForeSplat-trained initialization converges in fewer refinement steps and reaches a higher peak reconstruction quality than its vanilla counterpart,even fully this http URL framework consistently bridges the gap between amortized prediction and per-scene optimization,establishing a practical path toward lightweight,high-fidelity 3D reconstruction.

---


### 107. [Parser-Free Querying of Security Logs](https://arxiv.org/abs/2605.22027)

**<font color=#1a73e8>作者：</font>** Evan Luo, Julien Piet, David Wagner  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security analysts routinely query system logs to detect threats and investigate incidents, but each log source uses its own semi-structured format: logs are cheap to produce, but expensive to use. The standard approach, building per-source parsers to normalize logs into structured schemas, is powerful but requires continuous engineering effort for each new format. Querying raw logs directly with tools like grep avoids this cost, but requires analysts to know each source's message variants and cannot express the multi-line temporal queries that security investigations demand. We present Sieve, a system that generates executable query code from natural-language security questions by grounding a large language model with lightweight, automatically extracted log-format context, requiring only one LLM call per query followed by deterministic execution. Evaluating 133 security queries across 5 log types, we find that Sieve achieves over a 3x reduction in error rate on complex temporal and cross-event queries compared to manual analyst scripting, with the largest gains on the multi-line correlation tasks most critical to active investigations. Our results and benchmark provide evidence that LLM-generated code can bridge the gap between the expressiveness of structured log querying and the immediacy of working directly with raw files.

---


### 108. [SO-Mamba: State-Ownership Mamba for Unrolled MRI Reconstruction](https://arxiv.org/abs/2605.22031)

**<font color=#1a73e8>作者：</font>** Pengcheng Fang, Hongli Chen, Fangfang Tang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accelerated MRI reconstruction requires recovering missing details while preserving anatomically coherent structures across large spatial regions. State-space models such as Mamba provide efficient long-range modeling, making them attractive learned regularizers for unrolled reconstruction. However, in a data-consistency-coupled unrolled solver, different stages operate on different reconstruction iterates, where the resident carrier should preserve coherent reconstruction content across stages while stage-dependent non-resident evidence is tied to the current update. Treating these roles uniformly can place persistent resident-carrier evidence and update-dependent non-resident evidence into the same recurrent content route. We therefore propose SO-Mamba, a state-ownership Mamba regularizer that assigns reconstruction evidence within each Mamba stage to recurrent residency, state-interface access, and non-state output correction. SO-Mamba implements this ownership rule with a State-Ownership Router (SOR), which constructs a resident carrier for recurrent content and routes non-resident evidence to affine modulation of the B/C state interfaces and an output correction outlet. The resident carrier supplies the Mamba content route, while the non-resident evidence stream adapts the state interfaces and contributes through the output outlet without entering the recurrent content route. We further introduce a two-level outer-band leakage diagnostic that separates hidden-state storage from readout expression by measuring outer-band energy in the selective-scan state trajectory and the post-scan Mamba readout. Experiments on five public MRI reconstruction benchmarks spanning diverse anatomies, sampling patterns, and coil configurations show that SO-Mamba consistently improves over CNN-, Transformer-, and Mamba-based baselines with competitive computational efficiency.

---


### 109. [AgroVG: A Large-Scale Multi-Source Benchmark for Agricultural Visual Grounding](https://arxiv.org/abs/2605.22034)

**<font color=#1a73e8>作者：</font>** Haocheng Li, Juepeng Zheng, Zenghao Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual grounding, the task of localizing objects described by natural-language expressions, is a foundational capability for agricultural AI systems, enabling applications such as selective weeding, disease monitoring, and targeted harvesting. Reliable evaluation of agricultural visual grounding remains challenging because agricultural targets are often small, repetitive, occluded, or irregularly shaped, and instructions may refer to one, many, or no objects in an image. Evaluating this capability therefore requires jointly testing localization accuracy, target-set completeness, and existence-aware abstention. To address these challenges, we introduce \textbf{AgroVG}, a multi-source benchmark that formulates agricultural grounding as generalized set prediction: given an image and a referring expression, a model must return all matching target instances or abstain when no target is present. AgroVG contains 10{,}071 annotation-grounded image-query pairs from ten source datasets across six target families: crop/weed, fruit, wheat head, pest, plant disease, and tree canopy. It supports bounding-box grounding (T1) across all six families and instance-mask grounding (T2) on sources with reliable instance-level pixel annotations, with queries covering single-target, multi-target, and target-absent regimes. AgroVG further provides task-specific protocols for box-set matching and query-level mask coverage. Zero-shot evaluation of 26 model configurations spanning closed-source MLLMs, open-source VLMs, and specialized grounding systems reveals persistent gaps: the best multi-target Set-$F_1$ reaches only 0.35, and the best positive-query mask success rate at IoU@0.75 remains below 0.17. Data and code are available at this https URL .

---


### 110. [HyLoVQA: Dynamic Hypernetwork-Generated Low-Rank Adaptation for Continual Visual Question Answering](https://arxiv.org/abs/2605.22035)

**<font color=#1a73e8>作者：</font>** Yiran Wang, Chenyi Xiong, Ziyue Qin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continual Visual Question Answering (VQA) requires learning from non-stationary streams of visual inputs and questions while preserving past knowledge. Most prior methods adapt by updating a largely shared parameter set. This often leads to cross-level task interference, hindering accurate adaptation to the current task and object. To address this limitation, we propose HyLoVQA. It maintains a drift-resilient memory bank of anchors. The bank stores the content of visual objects and textual tasks, and they are updated using current input features. Conditioned on retrieved anchors, a hypernetwork generates lightweight Low-Rank Adaptation (LoRA) adapters. This ensures parameter efficiency, allowing the model to adapt to each task and object dynamically. Additionally, we formulate an alignment loss that aligns semantic discrepancies in the feature space with functional changes in the parameter space, thereby constraining LoRA adapters to remain focused on the current task and object. Extensive experiments on VQA v2 and NExT-QA under both standard and compositional settings demonstrate the superiority of HyLoVQA over prior state-of-the-art methods.

---


### 111. [CASE-NET: Deep Spatio-Temporal Representation Learning via Causal Attention and Channel Recalibration for Multivariate Time Series Classification](https://arxiv.org/abs/2605.22043)

**<font color=#1a73e8>作者：</font>** Fan Zhang, Yating Cui, Hua Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multivariate time series (MTS) classification is foundational to pervasive computing and financial analysis, yet existing multi-scale paradigms are often constrained by suboptimal representation fidelity. We identify two critical bottlenecks: temporal non-causality in standard encoders that induces temporal confounding in non-stationary dynamics, and the absence of explicit channel saliency mechanisms that allows noise to contaminate the latent space. To address these challenges, we propose the Causal Attention and Spatio-temporal Encoder Network (CASE-NET), an architecture designed for structural manifold pre-conditioning. CASE-NET synergizes a Causal Temporal Encoder, which enforces physical arrow-of-time constraints via masked self-attention and causal convolutions, with an Adaptive Channel Recalibration module functioning as an information bottleneck to suppress detrimental noise. Comprehensive evaluations across six heterogeneous domains demonstrate that CASE-NET establishes new state-of-the-art benchmarks on four tasks, achieving a peak accuracy of 98.6% on the AWR dataset and superior robustness in non-stationary regimes.

---


### 112. [Physiology and Anatomy Aware Inverse Inference of Myocardial Infarction for Cardiac Digital Twin](https://arxiv.org/abs/2605.22044)

**<font color=#1a73e8>作者：</font>** Mengxiao Wang, Yilin Lyu, Julia Camps 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate localization of myocardial infarction is essential for risk stratification. While LGE-MRI remains the gold standard, it is resource-intensive. Integrating cine MRI with ECG enables a more detailed representation of infarct properties. Existing inverse MI inference methods overlook realistic scar morphology and cardiac repolarization, reducing sensitivity to subtle ECG variations and interpretability of infarct-induced electrophysiological changes. In this paper, we propose a novel framework for noninvasive MI localization using cardiac digital twins. To bridge the domain gap between simulation and reality, we introduce an anatomy-aware stochastic infarct synthesis strategy to synthesize realistic, irregular scars with border zones, mimicking ischemic transmural progression. We then construct a virtual cohort to simulate QRS-T waveforms, capturing both depolarization and repolarization dynamics. Furthermore, we design a Physiology and Anatomy Aware Network (PAA-Net) that jointly encodes 3D myocardial geometry and multi-lead ECGs to infer infarct areas with varying localizations, sizes, spatial extents, and transmuralities. Experimental results demonstrate that our framework significantly outperforms existing methods in inverse inference, achieving Dice scores of 0.7391 and 0.5503 for scar and border zone segmentation, respectively, while further enhancing the interpretability of the ECG-infarct relationship. Our code will be released upon acceptance.

---


### 113. [Broken Memories: Detecting and Mitigating Memorization in Diffusion Models with Degraded Generations](https://arxiv.org/abs/2605.22050)

**<font color=#1a73e8>作者：</font>** Yuanmin Huang, Mi Zhang, Chen Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While diffusion models excel at generating high-quality images, their tendency to memorize training data poses significant privacy and copyright risks. In this work, we for the first time identify that memorization induces internal numerical instability, often manifesting as visually ``broken'' artifacts. Inspired by stability analysis in numerical methods, we introduce empirical stability regions based on latent update norms to quantitatively characterize stable behavior during generation. Leveraging this, we propose a principled, on-the-fly framework for step-wise detection and adaptive mitigation. Our approach suppresses memorization without altering prompts or guidance, thereby preserving semantic fidelity and image quality. Extensive experiments on Stable Diffusion 1.4 demonstrate that our method achieves an AUC $>0.999$ detection performance and a $0.0\%$ memorization rate after mitigation with negligible overhead ($\approx0.01$s per image).

---


### 114. [EasyVFX: Frequency-Driven Decoupling for Resource-Efficient VFX Generation](https://arxiv.org/abs/2605.22051)

**<font color=#1a73e8>作者：</font>** Yue Ma, Xu Ye, Qinghe Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating high-fidelity visual effects (VFX) typically demands massive datasets and prohibitive computational power due to the intricate coupling of spatial textures and temporal dynamics. In this paper, we introduce EasyVFX, a resource-efficient framework that achieves realistic VFX synthesis under stringent constraints. Our core philosophy lies in frequency-domain decomposition: we observe that the complexity of VFX can be significantly mitigated by decoupling high-frequency components, which represent intricate spatial appearances, from low-frequency components that encapsulate global motion dynamics. This spectral disentanglement transforms a high-dimensional learning problem into manageable sub-tasks, thereby lowering the optimization barrier and reducing data dependency. Building upon this insight, we propose a two-stage training paradigm. First, we design a Frequency-aware Mixture-of-Experts (Freq-MoE) architecture. By utilizing a soft routing mechanism, our model assigns specialized experts to distinct spectral bands, enabling them to cultivate robust priors for appearance and motion dynamics. This specialization allows the model to acquire foundational VFX knowledge with fewer GPU resources. Second, we introduce a Test-Time Training strategy powered by a novel Frequency-constraint Loss. This allows the pre-trained model to swiftly adapt to specific, unseen effects through localized optimizations, requiring only about 100 steps on a single GPU. Experimental results demonstrate that EasyVFX produces structurally consistent and visually stunning effects, proving that frequency-aware learning is a key catalyst for democratizing professional-grade VFX.

---


### 115. [Prototype-Guided Classification Sub-Task Decoupling Framework: Enhancing Generalization and Interpretability for Multivariate Time Series](https://arxiv.org/abs/2605.22055)

**<font color=#1a73e8>作者：</font>** Xianhao Song, Yuang Zhang, Yuqi She 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time Series Classification (TSC) is a long-standing research problem that has gained increasing attention in recent years with the rapid growth of large-scale temporal data. Despite substantial progress enabled by deep learning, designing TSC models that are both accurate and interpretable remains a challenging task. Many existing approaches adopt a direct feature-to-label classification paradigm, by collapsing high-dimensional temporal embeddings into class logits via a single linear projection (often after global pooling), the paradigm conflates feature extraction and decision logic into an inseparable mapping.
To address these limitations, we propose PDFTime, a prototype-guided framework that reformulates time series classification as a multi-stage decision process. Instead of direct feature-to-label mapping, PDFTime leverages learned prototypes to approximate class-conditional feature distributions in the latent space, enabling progressive discrimination through classification sub-tasks of varying granularity. To our knowledge, PDFTime is the first framework to reformulate time series classification as a decoupled, multi-stage similarity-based reasoning process, breaking the long-standing paradigm of direct, black-box feature-to-label mapping. Extensive evaluations demonstrate that PDFTime achieves state-of-the-art (SOTA) performance across UEA and UCR benchmarks. Notably, it secures the top-$1$ accuracy on 80 out of 128 datasets in the UCR archive, significantly outperforming recent strong baselines in both consistency and generalization.

---


### 116. [FlyRoute: Self-Evolving Agent Profiling via Data Flywheel for Adaptive Task Routing](https://arxiv.org/abs/2605.22057)

**<font color=#1a73e8>作者：</font>** Rongjun Li, Ziyu Zhou, Yihang Wu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Enterprise routers assign queries to expert agents, yet deployed profiles stay static while agents evolve (prompts, tools, models), and developers rarely keep descriptions or exemplars current. We present FlyRoute, a self-evolving profiling framework that grows capability evidence from real traffic: dispatch candidates, quality-gate successful pairs into each agent's success store, periodically distill evidence into learned capability descriptions, and inject those descriptions together with BM25-retrieved successes into an LLM router. To make this flywheel data-efficient, FlyRoute introduces a targeted exploration policy that combines profile uncertainty, BM25 relevance, and lexical novelty, prioritizing under-profiled agents only for plausible queries and avoiding redundant evidence collection. In experiments on our proprietary enterprise developer-support dataset of real routed queries, FlyRoute improves a same-backbone zero-shot LLM router from 72.57% to 78.04% with only five seed queries per agent, showing that profile retrieval already strengthens cold-start routing. After streaming 7,211 labeled training queries through the flywheel, accuracy rises to 89.83% (+17.26pp over zero-shot; +11.79pp over cold start), with consistent gains across four expert domains under standard routing accuracy on single-gold test queries.

---


### 117. [Safeguarding Text-to-Image Generative Models Against Unauthorized Knowledge Distillation](https://arxiv.org/abs/2605.22060)

**<font color=#1a73e8>作者：</font>** Yilan Gao, Sida Huang, Hongyuan Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Closed-weight generative services are increasingly deployed through query-based APIs, where users can obtain generated outputs while model parameters remain inaccessible. However, such deployment does not prevent model stealing: an attacker can repeatedly query the service, collect large volumes of released synthetic images, and use them as training data for a private substitute model. This query-output-driven process enables unauthorized knowledge distillation and capability replication without direct access to the original weights. To mitigate this threat, a practical defense should preserve the visual fidelity of released images, provide explicit control over perturbation magnitude, and scale efficiently to large-volume output release. We present WaveGuard, a single-pass, generator-based protection framework that safeguards released synthetic images under a user-specified perturbation budget. WaveGuard employs a frequency-aware perturbation generator to inject structured, imperceptible perturbations that maintain perceptual utility for benign viewers while reducing the usefulness of protected images as training data for unauthorized student models. Extensive experiments under WikiArt-related synthetic-output distillation settings show that WaveGuard achieves a favorable efficacy--fidelity--efficiency trade-off, with explicit imperceptibility control and substantial gains in protection efficiency.

---


### 118. [Hy-MT2: A Family of Fast, Efficient and Powerful Multilingual Translation Models in the Wild](https://arxiv.org/abs/2605.22064)

**<font color=#1a73e8>作者：</font>** Mao Zheng, Zheng Li, Tao Chen 等 53 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hy-MT2 is a family of fast-thinking multilingual translation models designed for complex real-world scenarios. It includes three model sizes: 1.8B, 7B, and 30B-A3B (MoE), all of which support translation among 33 languages and effectively follow translation instructions in multiple languages. For on-device deployment, with AngelSlim 1.25-bit extreme quantization, the 1.8B model requires only 440 MB of storage and improves inference speed by 1.5x. Multi-dimensional evaluations show that Hy-MT2 delivers outstanding performance across general, real-world business, domain-specific, and instruction-following translation tasks. The 7B and 30B models outperform open-source models such as DeepSeek-V4-Pro and Kimi K2.6 in fast-thinking mode, while the lightweight 1.8B model also surpasses mainstream commercial APIs from providers such as Microsoft and Doubao overall.

---


### 119. [Echo4DIR: 4D Implicit Heart Reconstruction from 2D Echocardiography Videos](https://arxiv.org/abs/2605.22066)

**<font color=#1a73e8>作者：</font>** Yanan Liu, Qinya Li, Hao Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing 4D (3D+t) cardiac geometry from sparse 2D echocardiography is highly desirable yet fundamentally challenged by geometric ambiguity and temporal discontinuity. To tackle these issues, we propose Echo4DIR, a novel test-time 4D implicit reconstruction framework. Specifically, we learn robust 3D shape priors from statistical shape models (SSMs) via a cardiac conditional SDF, constructing an Epipolar Mask Encoder module with epipolar cross attention to effectively fuse multi-view features. To bridge the synthetic-to-real domain gap, we introduce a self-supervised SDF-tailored differentiable rendering strategy for patient-specific 3D shape adaptation using uncalibrated clinical masks without requiring 3D ground truth. Crucially, the inherent continuity of implicit representation overcomes sparse observations, enabling anatomically reliable geometry at arbitrary resolutions. Furthermore, to empower our framework with physically continuous 4D extension, we introduce a Radial SDF Alignment strategy that strictly locks shape evolution to the predicted velocity field, fundamentally eliminating mesh drift. Extensive experiments on synthetic benchmarks and real clinical datasets demonstrate that Echo4DIR achieves state-of-the-art 4D cardiac mesh reconstruction, notably yielding an impressive clinical overlap of up to 98.35% Dice and 96.75% IoU.

---


### 120. [TWINGS: Thin Plate Splines Warp-aligned Initialization for Sparse-View Gaussian Splatting](https://arxiv.org/abs/2605.22069)

**<font color=#1a73e8>作者：</font>** Hyeseong Kim, Geonhui Son, Deukhee Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Novel view synthesis from sparse-view inputs poses a significant challenge in 3D computer vision, particularly for achieving high-quality scene reconstructions with limited viewpoints. We introduce TWINGS, a framework that enhances 3D Gaussian Splatting (3DGS) by directly addressing point sparsity. We employ Thin Plate Splines (TPS), a smooth non-rigid deformation model that minimizes bending energy to estimate a globally coherent warp from control-point correspondences, to align backprojected points from estimated depth with triangulated 3D control points, yielding calibrated backprojected points. By sampling these calibrated points near the control points, TWINGS provides a fast and geometrically accurate initialization for 3DGS, ultimately improving structural detail preservation and color fidelity in reconstructed scenes. Extensive experiments on DTU, LLFF, and Mip-NeRF360 demonstrate that TWINGS consistently outperforms existing methods, delivering detailed and accurate reconstructions under sparse-view scenarios.

---


### 121. [Can Breath Biomarkers Causally Influence Blood Glucose? Investigating VOC-Mediated Modulation in Diabetes](https://arxiv.org/abs/2605.22075)

**<font color=#1a73e8>作者：</font>** Varsha Sharma, Prasanta K. Guha, Avik Ghose  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diabetes is a global health burden, and early detection is critical for timely intervention. This study explores a non-invasive, data-driven framework to identify individuals at risk of diabetes using Volatile Organic Compounds (VOCs) and lifestyle variables. We use causal inference techniques to estimate the impact of VOCs such as acetone, isopropanol, isoprene, and ethanol on blood glucose levels. Additionally, we designed a classifier to distinguish diabetics from non-diabetics using non-invasive markers. We created a risk-based ranking system for individuals in the "gray zone," and identified natural clusters in the population using Gaussian Mixture Model. Our results suggest that specific VOCs exhibit a strong causal influence on glucose levels and that machine learning models can reliably classify and stratify individuals at high risk. This integrated causal-explainable analysis can support the development of tool for non-invasive early screening of diabetes.

---


### 122. [Ishigaki-IDS-Bench: A Benchmark for Generating Information Delivery Specification from BIM Information Requirements](https://arxiv.org/abs/2605.22079)

**<font color=#1a73e8>作者：</font>** Ryo Kanazawa, Koyo Hidaka, Teppei Miyamoto 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are widely used to generate structured outputs such as JSON, SQL, and code, yet public resources remain limited for evaluating generation that must simultaneously satisfy industry-standard XML and domain vocabulary constraints. This paper presents Ishigaki-IDS-Bench, a benchmark for evaluating the ability to generate Information Delivery Specification (IDS) XML from Building Information Modeling (BIM) information requirements. The benchmark contains 166 BIM/IDS expert-authored and verified examples created by expanding 83 practical scenarios into Japanese and English, corresponding gold IDS files, and metadata for input format, language, turn setting, IFC version, and construction domain. Its evaluation combines IDSAuditTool-based Processability, Structure, and Content audits with content-agreement evaluation against gold IDS files. In zero-shot evaluation over 10 LLMs, the best model reaches 65.6% macro F1 for content agreement, while only 27.7% of outputs pass the Content audit. These results show that current LLMs can express part of the information requirements as IDS, but still struggle to stably generate XML that satisfies the IDS standard and IFC vocabulary constraints. Ishigaki-IDS-Bench supports comparative evaluation, failure analysis, and the development of constrained structured generation methods that conform to domain standards. We release the evaluation scripts and benchmark data under the CC BY 4.0 license on GitHub and Hugging Face.

---


### 123. [ArabDiscrim: A Decade-Long Arabic Facebook Corpus on Racism and Discrimination](https://arxiv.org/abs/2605.22081)

**<font color=#1a73e8>作者：</font>** Wajdi Zaghouani, Shimaa Amer Ibrahim, Mabrouka Bessghaier 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present ArabDiscrim, a decade-long lexical resource and corpus of 293K public Arabic Facebook posts (2014--2024) discussing racism and discrimination. Unlike existing Twitter-centric datasets, ArabDiscrim integrates platform-native engagement signals, including reactions, shares, comments, and page metadata, enabling joint analysis of language and audience response. The resource includes 200 curated terms (100 racism-related and 100 discrimination-related) with morphological regex families (13+ inflections per lemma), and 20 discrimination axes capturing identity-based grounds for unequal treatment. It also provides explicit attribution patterns. Released under a restricted research-use license for ethical compliance with platform terms, ArabDiscrim supports weak supervision, axis-aware sampling, and platform ecology research. By bridging lexical depth and ecological validity, it establishes a foundation for fairness-oriented, platform-aware Arabic NLP.

---


### 124. [GenHAR: Generalizing Cross-domain Human Activity Recognition for Last-mile Delivery](https://arxiv.org/abs/2605.22086)

**<font color=#1a73e8>作者：</font>** Zhiqing Hong, Zelong Li, Xiubin Fan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human Activity Recognition (HAR) has shown remarkable effectiveness in various applications, such as smart healthcare and intelligent manufacturing. However, a major challenge faced by HAR is the distribution shift across different sensor data domains, which often leads to decreased performance when deployed for real-world applications. To address this issue, this paper introduces GenHAR, a novel framework designed to mitigate the domain gap by learning domain-invariant sensor representations. GenHAR aims to enhance the generalization capabilities of HAR on target domains purely with data from the source domain. The key novelty of GenHAR lies in two aspects. Firstly, GenHAR tokenizes sensor data and learns correlations among frequency sensor channel dimensions to improve the robustness of HAR models. Secondly, GenHAR improves the efficiency via selective masking and an efficient attention mechanism. We conduct a systematic analysis of GenHAR by comparing it with state-of-the-art HAR methods on real-world human activity datasets. Results show that GenHAR outperforms state-of-the-art methods by 9.97% in accuracy, and reduces Floating Point Operations by 6.4 times. Moreover, we deploy GenHAR at a leading logistics company in 4 cities, and have detected 2.15 billion real-time activities. We release our code at: this https URL.

---


### 125. [LVDrive: Latent Visual Representation Enhanced Vision-Language-Action Autonomous Driving Model](https://arxiv.org/abs/2605.22089)

**<font color=#1a73e8>作者：</font>** Xiaodong Mei, Diankun Zhang, Hongwei Xie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models have emerged as a promising framework for end-to-end autonomous driving. However, existing VLAs typically rely on sparse action supervision, which underutilizes their powerful scene understanding and reasoning capabilities. Recent attempts to incorporate dense visual supervision via world modeling often overemphasize pixel-level image reconstruction, neglecting semantically meaningful scene representation learning. In this work, we propose LVDrive, a Latent Visual representation enhanced VLA framework for autonomous driving. LVDrive introduces a future scene prediction task into the VLA paradigm, where future representations are learned entirely in a high-level latent space under auxiliary supervision from a pretrained vision backbone. Departing from inefficient autoregressive generation, we jointly model future scene and motion prediction within a unified embedding space, processed in a single forward pass to conduct the future-aware reasoning. We further design a two-stage trajectory decoding strategy that explicitly leverages the learned latent future representations to refine trajectory generation. Extensive experiments on the challenging Bench2Drive benchmark demonstrate that LVDrive achieves significant improvements in closed-loop driving performance, outperforming both action supervised methods and image-reconstruction-based world model approaches.

---


### 126. [Knowledge Graph Re-engineering Along the Ontological Continuum (extended version)](https://arxiv.org/abs/2605.22093)

**<font color=#1a73e8>作者：</font>** Enrico Daga, Valentina Tamma, Terry Payne  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge graphs have become the primary vehicle for data integration and are critical to the success of modern AI, but the diversity of KG modelling practices, from lightweight vocabularies to richly axiomatised ontologies, makes integration and reuse expensive and brittle. This challenge is particularly acute in neuro-symbolic AI, where bridging neural and symbolic components depends on the ability to reengineer KGs to fit new requirements; GenAI now offers unprecedented automation capability, but without a principled understanding of the KG space, such automation remains conceptually ungrounded. We introduce the ontological continuum as that missing conceptualisation, a theoretical construct a theoretical construct whose characterisation framework is defined by two orthogonal distinctions: semantics vs pragmatics, and properties vs affordances; together these define a vocabulary to describe, compare, navigate, and transform KGs across the full range of modelling practices. The methodological stance is empirical: rather than prescribing how KGs should be modelled, the continuum aims to define a theory of the existent, derived from observation of real-world KG engineering practices and whose structure can be made formally explicit, for example, through Formal Concept Analysis (FCA). We ground the vision through a case study on provenance knowledge, showing how a single concern manifests differently across the continuum. We articulate five open research challenges and invite the community to develop the ontological continuum as a shared research agenda.

---


### 127. [TextTeacher: What Can Language Teach About Images?](https://arxiv.org/abs/2605.22098)

**<font color=#1a73e8>作者：</font>** Tobias Christian Nauen, Stanislav Frolov, Brian Bernhard Moser 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The platonic representation hypothesis suggests that sufficiently large models converge to a shared representation geometry, even across modalities. Motivated by this, we ask: Can the semantic knowledge of a language model efficiently improve a vision model? As an answer, we introduce TextTeacher, a simple auxiliary objective that injects text embeddings as additional information into image classification training. TextTeacher uses readily available image captions, a pre-trained and frozen text encoder, and a lightweight projection to produce semantic anchors that efficiently guide representations during training while leaving the inference-time model unchanged. On ImageNet with standard ViT backbones, TextTeacher improves accuracy by up to +2.7 percentage points (p.p.) and yields consistent transfer gains (on average +1.0 p.p.) under the same recipe and compute. It outperforms vision knowledge distillation, yielding more accuracy at a constant compute budget or similar accuracy, but 33% faster. Our analysis indicates that TextTeacher acts as a feature-space preconditioner, shaping deeper layers in the first stages of training, and aiding generalization by supplying complementary semantic cues. TextTeacher adds negligible overhead, requires no costly multimodal training of the target model and preserves the simplicity and latency of pure vision models.
Project page with code and captions: this https URL

---


### 128. [MPDocBench-Parse: Benchmarking Practical Multi-page Document Parsing](https://arxiv.org/abs/2605.22100)

**<font color=#1a73e8>作者：</font>** Bangbang Zhou, Hangdi Xing, Yifan Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Document parsing converts visually rich documents into machine-readable structured representations, forming a crucial foundation for information systems. Although many benchmarks have been proposed for document parsing, they remain inadequate for realistic scenarios. Existing benchmarks either focus on specific tasks or assess only single-page, text-centric settings, making them insufficient for practical multi-page parsing. Moreover, they lack fine-grained evaluation of semantic continuity, hierarchical structure recovery, and visual content preservation. To address these gaps, we propose MPDocBench-Parse, a benchmark for multi-page document parsing in real-world applications. It contains 433 manually annotated documents with 3,246 pages, covering 15 document types in English and Chinese, with diverse layout styles, and supports document-level end-to-end evaluation. We further design a comprehensive protocol for content fidelity and logical structure, covering text, table, and formula recognition, truncated text and table merging, figure extraction, reading order, and heading hierarchy recovery. Experiments show that, while existing models perform well on basic text extraction, they still suffer clear limitations in semantic continuity integration, visual content parsing, and hierarchical structure recovery. MPDocBench-Parse provides a unified foundation for advancing document parsing toward more realistic scenarios.

---


### 129. [OPERA: An Agent for Image Restoration with End-to-End Joint Planning-Execution Optimization](https://arxiv.org/abs/2605.22104)

**<font color=#1a73e8>作者：</font>** Feng Zhu, Shuyang Xie, Yihan Zeng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world image restoration is challenging due to complex and interacting mixed degradations. Recent agent-based approaches address this problem by composing multiple task-specific restoration tools. However, empirical analysis reveals that their performance is fundamentally limited by implicitly constrained planning spaces and the lack of coordination among independently pretrained tools. To address these issues, we propose OPERA (Optimized Planning-Execution Restoration Agent), a framework that jointly optimizes restoration planning and tool execution in an end-to-end manner. On the planning side, OPERA uses reinforcement learning to directly optimize tool composition over a combinatorial plan space, with the final restoration quality as the reward. On the execution side, OPERA introduces agent-guided co-training of restoration tools, enabling them to learn cooperative behaviors under sequential composition. Extensive experiments on multi-degradation benchmarks and real-world datasets demonstrate that OPERA consistently outperforms both all-in-one restoration models and existing agent-based methods across diverse and complex degradation scenarios.

---


### 130. [Aerodynamic force reconstruction using physics-informed Gaussian processes](https://arxiv.org/abs/2605.22111)

**<font color=#1a73e8>作者：</font>** Gledson Rodrigo Tondo, Igor Kavrakov, Guido Morgenthal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate modeling of aerodynamic loads is essential for understanding and predicting the responses of complex structural systems. However, these models often rely on simplifications of the true physical forces, introducing assumptions that can limit their accuracy. Validating such models becomes particularly challenging in the presence of noisy or incomplete data. To address this, we introduce a probabilistic physics-informed machine learning approach designed to reconstruct the underlying aerodynamic loads from noisy measurements of structural dynamic responses. The model avoids overfitting, eliminates the need for regularization schemes, and allows for the use of heterogeneous and multi-fidelity data during the training process. The efficacy of the approach is demonstrated through the reconstruction of aerodynamic loads on the Great Belt East Bridge, simulated under a linear unsteady assumption. Results show a strong agreement between true and predicted loads, particularly related to root mean squared errors, magnitude, phase angle and peak values of the signals. The method for load reconstructing holds broad applicability, such as modeling validation, future load estimation, and structural damage prognosis.

---


### 131. [QT-PUF: Quantum Tunneling Leakage Based PUF for Implantable IoMT Devices](https://arxiv.org/abs/2605.22113)

**<font color=#1a73e8>作者：</font>** Yueqi Ma, Vivek Mohan, Chip-Hong Chang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Internet of Medical Things (IoMT) marks a shift toward decentralized healthcare, enabling continuous monitoring and personalized care through connected wearable and implantable devices. However, ensuring the trust and integrity of these devices themselves remains a major challenge, as physical compromise or counterfeiting can directly endanger patient safety, privacy, and data integrity. This work presents QT-PUF, a gate-tunneling-leakage-based physical unclonable function (PUF) that leverages quantum-mechanical gate leakage resulting from process-induced variations in standard CMOS devices. A differential readout circuit with a pseudo-resistor I-to-V frontend is proposed to convert the picoampere-level leakage variations into digital responses. Unlike existing PUFs such as those based on memory, ring oscillators, or arbiters, which are less suitable for ultralow-power IoMT devices (due to additional circuitry, power overhead, or poor stability), QT-PUF requires no external excitation or stabilization and operates under static bias. Simulation-based measurements for a $\mathbf{65}$~nm CMOS process demonstrate an entropy of $\mathbf{0.9999998}$, an FHD of $\mathbf{0.5001}$, and an average power (energy) consumption of $\mathbf{96.04}$~nW/bit ($\mathbf{19.21}$~fJ/bit, respectively) at $\mathbf{1.2\,V}$ and $\mathbf{35\,^{\circ}C}$ for the proposed PUF. It operates reliably across $\mathbf{0.9}\text{--}\mathbf{1.3}$~V and $\mathbf{0}\text{--}\mathbf{100\,^{\circ}C}$ with an average BER below $\mathbf{0.000163}$ across $\mathbf{1.0}\text{--}\mathbf{1.3}$~V and $\mathbf{10}\text{--}\mathbf{70\,^{\circ}C}$ within the operating conditions of typical implantable devices.

---


### 132. [Human Vulnerability Assessment in Cybersecurity: A Systematic Literature Review of Methods, Models, and Instruments](https://arxiv.org/abs/2605.22119)

**<font color=#1a73e8>作者：</font>** Dimitra Papatsaroucha, Stavroula Psaroudaki, Eleftheria Vassilaki 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In cybersecurity, vulnerability assessment has typically focused on identifying and measuring vulnerabilities within digital assets and technical infrastructures. However, there is growing recognition that this approach alone is inadequate without a structured examination of the human factor, which is becoming more frequently targeted and manipulated by cyber adversaries. Human vulnerabilities extend beyond individual susceptibility to cyber threats, encompassing a wide array of psychological, cognitive, behavioral, social, and contextual factors that can, whether unintentionally or intentionally, jeopardize the security and integrity of systems and data. Despite this recognition, human vulnerability assessment remains fragmented, often addressed from a static rather than a dynamic perspective, and with limited focus on the ways it propagates across individuals and systems; a growing body of literature has explored specific facets of the issue, including one-time assessments of security behavior, user awareness, and, to a degree, intentional insider threats and their detection. This research offers a systematic literature review (SLR) of Human Vulnerability Assessment (HVA) in cybersecurity, including methods, models, and instruments proposed for the conceptual or practical assessment of human vulnerabilities across various dimensions. Following the PRISMA framework, this review gathers relevant studies published from 2017 to 2025, aiming to investigate whether any assessment methods, models, or instruments exist that address the entire spectrum of human vulnerabilities dynamically. The findings highlight gaps and limitations in current proposed solutions and identify areas for further investigation regarding holistic assessment that simultaneously and dynamically considers the entire spectrum of both the unintentional and intentional dimensions of human vulnerability.

---


### 133. [MotionDPS: Motion-Compensated 3D Brain MRI Reconstruction](https://arxiv.org/abs/2605.22121)

**<font color=#1a73e8>作者：</font>** Antonio Ortiz-Gonzalez, Erich Kobler, Lukas Schletter 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Magnetic resonance imaging (MRI) is highly susceptible to patient motion due to its relatively long acquisition times and the fact that data are acquired sequentially in k-space. Even small patient movements introduce phase inconsistencies across measurements, leading to severe artifacts such as blurring, ghosting, and geometric distortions that can compromise diagnostic quality. Retrospective motion compensation remains challenging, particularly in accelerated acquisitions, due to the ill-posed nature of the joint reconstruction and motion estimation problem. In this work, we propose a unified Bayesian framework for motion-compensated 3D MRI that jointly estimates the anatomical image, rigid-body motion parameters, and coil sensitivity maps directly from motion-corrupted k-space data. Our approach integrates pretrained 3D complex-valued score-based diffusion models as expressive anatomical image priors within a physics-based forward model. Inference is performed by alternating diffusion posterior image updates with efficient proximal optimization steps for motion and coil sensitivity estimation, enabling fully unsupervised reconstruction without the need for paired motion-free training data. Experiments on simulated and real-motion brain MRI datasets demonstrate that the proposed method achieves improved image quality and motion robustness compared to state-of-the-art classical and learning-based motion correction techniques, particularly in the presence of severe motion and high acceleration.

---


### 134. [Adversarial Trust Poisoning in Vehicular Collaborative Perception](https://arxiv.org/abs/2605.22122)

**<font color=#1a73e8>作者：</font>** Yutong Liu, Chenyi Wang, Ming F. Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Collaborative perception (CP) enables connected and autonomous vehicles to share sensor data and jointly reason about their environment. To defend against adversaries that fabricate or manipulate shared data, existing systems employ cross-vehicle inconsistency detection and trust estimation, penalizing vehicles whose observations conflict with the majority. In this work, we show that these defenses themselves introduce a new attack surface. We present TrustFlip, a novel attack that weaponizes consistency-based defenses to poison the trust assigned to benign vehicles. Instead of injecting false data into the collaboration pipeline, it deploys physical adversarial objects that are genuine but induce inconsistent observations among benign vehicles. The resulting inconsistencies are misattributed by the defense to the targeted vehicle, causing its trust score to degrade and eventually leading to its downweighting or exclusion from collaboration. Consequently, the system loses reliable sensing contributors, degrading perception capability and potentially inducing safety-critical failures. We evaluate TrustFlip across multiple collaborative perception architectures and defense mechanisms. Our results show that state-of-the-art defenses can be significantly affected: the attack removes the targeted benign vehicle from collaboration in up to 87.7% of scenarios and drops Average Precision (AP) by up to 13%. As an initial mitigation, we introduce TrustReflect, a lightweight self-reflection mechanism that marks disputed regions as uncertain and excludes them from trust evaluation, reducing the attack success rate by 35-100%.

---


### 135. [AesFormer: Transform Everyday Photos into Beautiful Memories](https://arxiv.org/abs/2605.22126)

**<font color=#1a73e8>作者：</font>** Tianxiang Du, Hulingxiao He, Yuxin Peng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In everyday photography, aesthetically appealing moments are often captured with structural flaws (e.g., composition, camera viewpoint, or pose) that existing retouching and portrait enhancement methods cannot fix. We formulate Aesthetic Photo Reconstruction (APR) as improving a photo's aesthetic quality via structural reconstruction while preserving subject identity and scene semantics. Although recent advances in image editing models make APR feasible, they often lack aesthetic understanding, yielding edits that are semantically plausible yet aesthetically weak. To address this, we propose AesFormer, a two-stage framework that decouples aesthetic planning from image editing. In Stage 1, an aesthetic action model (AesThinker) analyzes the input along seven progressive photographic dimensions and outputs executable editing actions; we further apply GRPO-A to encourage broad exploration over diverse action plans beyond SFT. In Stage 2, an action-conditioned editor (AesEditor) performs structural edits guided by these actions. To support APR, we build a video-based corpus-mining pipeline (VCMP) and construct AesRecon, a benchmark of 9,071 strictly aligned (poor, good) image pairs. Experiments show that AesFormer substantially improves APR performance and is competitive with Nano Banana Pro. Code is available at this https URL.

---


### 136. [EventGait: Towards Robust Gait Recognition with Event Streams](https://arxiv.org/abs/2605.22139)

**<font color=#1a73e8>作者：</font>** Senyan Xu, Shuai Chen, Chuanfu Shen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gait recognition enables non-intrusive, privacy-preserving identification but suffers in uncontrolled environments due to illumination and motion sensitivity of conventional cameras. In this work, we explore gait recognition using event cameras, which offer microsecond temporal resolution and high dynamic range, naturally capturing robust dynamic cues and suppressing static noise. Existing event-based approaches typically aggregate event streams into event images over long time windows, thereby discarding fine-grained motion dynamics critical for gait recognition. Therefore, we propose \textbf{EventGait}, an end-to-end dual-stream framework that separately models motion and shape while preserving the advantages of events. Our dynamic stream leverages a Mixture of Spiking Experts (MoSE) with diverse neuron constants for robust dynamic perception across complex motion and illumination scenes, while the static stream learns dense shape representations via Cross-modal Structure Alignment (CroSA) with large vision foundation models. To address the absence of large-scale event-based gait datasets, we introduce a synthesis pipeline and release two new benchmarks: SUSTech1K-E and CCGR-Mini-E. Extensive experiments have shown that event-based gait recognition not only achieves results comparable to camera-based gait recognition under normal conditions but also significantly outperforms it in low-light scenarios. Our approach sets a new state of the art on both synthesized and real-world event-based gait benchmarks, highlighting the robustness and potential of event-driven gait analysis. The code and datasets are released at this https URL.

---


### 137. [Psy-Chronicle:A Structured Pipeline for Synthesizing Long-Horizon Campus Psychological Counseling Dialogues](https://arxiv.org/abs/2605.22140)

**<font color=#1a73e8>作者：</font>** Chaogui Gou, Jiarui Liang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In recent years, large language models have shown substantial potential in psychological support tasks. However, existing psychological counseling data mostly rely on single-turn question answering or short multi-turn dialogues, making it difficult to characterize how college students' psychological distress accumulates, interacts, and gradually evolves over long periods within campus life events. To address this issue, this paper proposes Psy-Chronicle, a structured data-generation framework for synthesizing long-horizon campus psychological counseling dialogues. We generate a semester-spanning temporal stress event graph to model the chronological order and evolutionary dependencies among campus stress events. Through interactive simulation between a student agent and a counselor agent, together with a structured memory integration mechanism, Psy-Chronicle generates long-horizon dialogues with continuity across counseling sessions. Based on Psy-Chronicle, we construct and open-source CPCD, a Chinese long-horizon dialogue dataset for college psychological counseling, containing 100 student profiles, 90,000 counseling dialogues. We further build CPCD-Bench to evaluate models' long-horizon campus counseling capabilities from three dimensions: session-level response, long-horizon memory recall, and temporal-causal reasoning. Experimental results show that CPCD effectively improves session-level response generation and long-horizon memory recall for models with the same base architecture. Meanwhile, improvements in temporal-causal reasoning remain limited, indicating that event-chain organization and causal explanation are key challenges in long-horizon psychological counseling modeling. The related code and data are available at: this https URL

---


### 138. [Short-Term-to-Long-Term Memory Transfer for Knowledge Graphs under Partial Observability](https://arxiv.org/abs/2605.22142)

**<font color=#1a73e8>作者：</font>** Taewoon Kim, Vincent François-Lavet, Michael Cochez  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning under partial observability requires deciding what information to retain, yet most memory-based approaches do not explicitly model short-term-to-long-term transfer of symbolic observations. We study this transfer process in a temporal knowledge-graph memory setting and cast it as a neuro-symbolic value-based decision problem: for each observed triple, the agent chooses whether to keep or drop it before long-term insertion. To handle variable-sized short-term buffers, we use a per-item Q-learning design with shared parameters and a practical temporal-difference update over matched items across consecutive steps. On the RoomKG benchmark at long-term memory capacity 128, learned transfer decisions outperform symbolic and neural baselines, including symbolic baselines with temporal annotations and history-based LSTM/Transformer baselines. Across transfer-policy ablations, a lightweight local short-term-only variant performs best, and step-level behavior shows that the policy keeps navigation- and query-relevant facts while discarding lower-value candidate facts, supporting explicit and interpretable memory decisions under memory constraints.

---


### 139. [One Sentence, One Drama: Personalized Short-Form Drama Generation via Multi-Agent Systems](https://arxiv.org/abs/2605.22144)

**<font color=#1a73e8>作者：</font>** Yufei Shi, Weilong Yan, Naixuan Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing approaches for digital short-drama production typically rely on one-shot LLM generated scripts and loosely coupled pipelines, which fail to satisfy three key requirements of short-drama generation: (1) narrative pacing, resulting in weak hooks, insufficient escalation, and unattractive endings; (2) spatial consistency, leading to drifting scene layouts and inconsistent character positions across clips; and (3) production-level quality control, requiring extensive manual review and correction across script and visual stages. We present One Sentence, One Drama, a hierarchical multi-agent framework that transforms a user's single-sentence idea into a fully produced short drama through structured intermediate modules and iterative refinement. Our approach is built upon three key components: (1) a multi-agent debate-based story generation module that enforces short-drama pacing and narrative coherence; (2) a 3D-grounded first-frame generation mechanism that establishes a shared spatial reference for consistent character positioning and scene layout across clips; and (3) multi-stage reviewer loops that perform comprehensive error detection and targeted revision across script, visual, and video generation stages. We also introduce scene-level BGM matching and scene transition planning to improve the audience's immersive experience. To systematically evaluate this task, we introduce Short-Drama-Bench, a benchmark that extends standard video quality metrics with short-drama-specific criteria. Experimental results demonstrate that our method significantly outperforms existing pipelines in narrative quality, cross-clip consistency, and overall viewing experience.

---


### 140. [Flow-based Gaussian Splatting for Continuous-Scale Remote Sensing Image Super-Resolution](https://arxiv.org/abs/2605.22147)

**<font color=#1a73e8>作者：</font>** Jiangwei Mo, Xi Lu, Hanlin Wu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution remote sensing images (RSIs) are crucial for Earth observation applications, yet acquiring them is often limited by sensor constraints and costs. In recent years, generative super-resolution (SR) methods, particularly diffusion models, have made significant progress. However, they typically require slow iterative inference with 40--1000 steps and exhibit limited flexibility in continuous-scale SR settings. To address these issues, we propose FlowGS, a generative reconstruction framework for arbitrary-scale SR of RSIs. FlowGS models the high-frequency detail representations between high- and low-resolution images and learns a continuous probability flow from noise to detail priors via flow matching (FM) constrained by shortcut consistency, thereby reducing generative complexity and improving inference efficiency. Additionally, we employ 2D Gaussian splatting to construct a continuous feature field, thereby enabling flexible reconstruction at arbitrary query locations. Experimental results show that FlowGS delivers competitive perceptual quality compared with existing methods in both continuous-scale and fixed-scale SR settings, with substantially improved inference efficiency.

---


### 141. [Market-Analysis-Driven Methodology for Assessing Charging Station Cybersecurity](https://arxiv.org/abs/2605.22151)

**<font color=#1a73e8>作者：</font>** Jakob Löw, Lukas Eder, Alexander Müller 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern charging communication standards for electric vehicles include optional security controls such as TLS-based authentication and encryption. However, with tens of thousands of fast charging points deployed in any given country, individually testing each one for security control support is infeasible. This paper proposes a scalable, extrapolation-based methodology for assessing charging station cybersecurity at a national level. A market analysis identifies operator-manufacturer pairs, enabling the targeted selection of charging stations for field testing, whose results can then be extrapolated to all stations sharing the same combination. We demonstrate this methodology for Germany, covering over 40000 CCS charging points as of December 2025. With a manageable number of field tests, our extrapolated data examines 51.9\% of german CCS charging stations. It shows that only 27.4\% of charging stations in our scope provide TLS-protected communication, despite widespread theoretical support.

---


### 142. [Algebraic Machine Learning for Small-to-Medium Datasets Is Competitive against Strong Standard Baselines](https://arxiv.org/abs/2605.22155)

**<font color=#1a73e8>作者：</font>** David Mendez, Fernando Martin-Maroto, Gonzalo G. de Polavieja  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Symbolic methods are generally not considered competitive with strong modern learners on realistic supervised tasks. We evaluate Algebraic Machine Learning (AML), a framework that learns through subdirect decomposition of algebraic structure rather than numerical optimization, against standard baselines on image and tabular classification across varying training-set sizes. We find that AML trained only on training data without using validation or cross-validation outperforms a family of cross-validated baseline methods including CNNs on small to medium image datasets (50--2000 training examples). On tabular datasets in the same size range, XGBoost is overall the best performing method, but AML is nonetheless comparable to methods incorporating task-specific biases such as LightGBM and random forests. AML achieves this competitive performance across two very different types of datasets using a generic algebraic inductive bias, rather than the modality-specific biases built into standard baselines like CNNs for images or XGBoost for tabular data, and requires no cross validation because it has no task-dependent hyperparameters to tune.

---


### 143. [Measuring Cross-Modal Synergy: A Benchmark for VLM Explainability](https://arxiv.org/abs/2605.22168)

**<font color=#1a73e8>作者：</font>** Joël Roman Ky, Salah Ghamizi, Maxime Cordy  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) map complex visual inputs to semantic spaces, but interpreting the cross-modal reasoning of VLMs currently relies on post-hoc explainers evaluated via unimodal perturbation metrics. We expose a limitation in this paradigm: because multimodal datasets contain language priors and modality biases, VLMs frequently exhibit cross-modal redundancy, allowing them to answer visual queries using text alone. Consequently, unimodal metrics penalize faithful explainers, triggering an evaluation collapse where visual and textual rankings fundamentally contradict each other. %(Kendall's $\tau = -0.06$). To resolve this, we introduce Synergistic Faithfulness ($\mathcal{F}_{syn}$), a scalable metric rooted in the Shapley Interaction Index that strictly isolates the joint Harsanyi dividend between modalities, serving as a highly accurate surrogate ($\rho = 0.92$) while achieving a $24\times$ computational speedup. Evaluating 8 distinct XAI methods across 3 VLM architectures and 3 benchmark datasets, reveals that explainers proposed for VLMs heavily over-index on visual salience and significantly underperform adapted attention-based methods in capturing true cross-modal synergy. By decoupling visual plausibility from cross-modal faithfulness, this work provides a rigorous evaluation framework required to safely audit VLM reasoning in high-stakes deployments.

---


### 144. [IKNO: Infinite-order Kernel Neural Operators](https://arxiv.org/abs/2605.22182)

**<font color=#1a73e8>作者：</font>** Pengyuan Zhu, Ivor W. Tsang, Yueming Lyu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators have achieved significant success in modern scientific computing due to their flexibility and strong generalization capabilities. Existing models, however, primarily rely on first-order kernel integral approximations, which severely limit their expressivity. To address this, we propose the Infinite-order Kernel Neural Operator (IKNO), which constructs neural operators via infinite-order kernel integrals and admits an elegant closed-form finite approximation. We develop two complementary infinite-order neural operator constructions: IKNO-Vanilla, which applies the full-kernel resolvent on the product grid via Kronecker eigendecomposition, and IKNO-TP, an alternative tensor-product operator that composes per-axis resolvents. Furthermore, we develop fast computation schemes for both variants of IKNO, which achieve outstanding global information aggregation while maintaining high computational efficiency. Empirically, we evaluate our IKNO on both time-dependent and time-independent benchmarks with arbitrary input shapes, including large-scale industrial datasets. Extensive experiments demonstrate that the IKNO method consistently achieves the SOTA accuracy with significant improvements on nearly all benchmark datasets while maintaining scalability to very large point clouds.

---


### 145. [Event-Illumination Collaborative Low-light Image Enhancement with a High-resolution Real-world Dataset](https://arxiv.org/abs/2605.22186)

**<font color=#1a73e8>作者：</font>** Senyan Xu, Zhijing Sun, Kean Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event-based low-light image enhancement (LIE) methods mainly focus on incorporating high dynamic range (HDR) information from events while overlooking the essential global illumination in images and the inherent noise sensitivity of event signals in real-world scenarios. To address these issues, we propose EIC-LIE, an event-illumination collaborative LIE framework. Concretely, we first design an Event-Illumination Collaborative Interaction (EICI) module, which contains two key processes: forward gathering, which gathers HDR features across varying lighting conditions, and backward injection, which provides complementary content for illumination and event representations. Next, we introduce an Illumination-aware Event Filter (IAEF) that dynamically reduces event noise based on brightness statistics derived from images. Additionally, we build a beam-splitter-based hybrid imaging system to collect high-quality event-image pairs with temporal synchronization from dynamic scenes, providing the first high-resolution, real-world event-based LIE dataset. Extensive experiments show that our EIC-LIE outperforms state-of-the-art methods on five real-world and synthetic datasets, significantly surpassing previous methods with improvements of up to 1.24dB in PSNR and 0.069 in SSIM. The code and dataset are released at this https URL.

---


### 146. [From Sequential Nodes to GPU Batches: Parallel Branch and Bound for Optimal $k$-Sparse GLMs](https://arxiv.org/abs/2605.22188)

**<font color=#1a73e8>作者：</font>** Jiachang Liu, Andrea Lodi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> GPUs have significantly accelerated first-order methods for large-scale optimization, especially in continuous optimization. However, this success has not transferred cleanly to problems with discrete variables, combinatorial structure, and nonlinear objectives, such as certifying optimal solutions for cardinality-constrained generalized linear models. Major challenges include the sequential processing of heterogeneous nodes in branch and bound (BnB) and frequent data movement between the CPU and GPU. We propose a simple, generic, and modular CPU--GPU framework that processes multiple BnB nodes in batches on GPUs. The framework is built around a small set of GPU-efficient routines and uses padding together with lightweight custom kernels to handle irregular node data structures. Experiments show one to two orders of magnitude speedups and zero optimality gap on challenging instances. The framework can also be extended to collect the entire Rashomon set, enabling downstream statistical analysis such as variable-importance analysis and model selection under secondary user-specific measures (e.g., AUC in classification).

---


### 147. [No Pose, No Problem in 4D: Feed-Forward Dynamic Gaussians from Unposed Multi-View Videos](https://arxiv.org/abs/2605.22190)

**<font color=#1a73e8>作者：</font>** Matteo Balice, Yanik Kunzi, Chenyangguang Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent feed-forward 3D gaussian splatting methods have made dramatic progress on individual aspects of 3D scene reconstruction, but no existing method jointly addresses dynamic content, multi-view input, and unknown camera poses in a single feed-forward pass. Methods that handle dynamics either require accurate camera poses or accept only monocular input; pose-free multi-view methods address only static scenes; and per-scene optimization methods bridge some of these gaps but at minutes-to-hours cost per scene. We introduce NoPo4D, the first feed-forward system that addresses this empty quadrant. Building on a pretrained geometry backbone and recent 4D Gaussian frameworks, NoPo4D introduces a velocity decomposition that splits Gaussian motion into per-pixel image-plane shifts and depth changes, allowing direct supervision from pseudo ground-truth optical flow on the 2D component. This sidesteps both the differentiable rendering that couples prior posed methods to pose accuracy and the 3D motion ground truth that prior pose-free methods require. The system is rounded out by a bidirectional motion encoder for cross-view and cross-frame feature aggregation, and view-dependent opacity that mitigates cross-view and cross-timestep Gaussian misalignments. On four multi-view dynamic benchmarks, NoPo4D consistently outperforms prior feed-forward baselines, and with an optional post-optimization stage surpasses per-scene optimization methods, while running orders of magnitude faster.

---


### 148. [Bandit Convex Optimization with Gradient Prediction Adaptivity](https://arxiv.org/abs/2605.22191)

**<font color=#1a73e8>作者：</font>** Shuche Wang, Adarsh Barik, Vincent Y. F. Tan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bandit convex optimization (BCO) is a fundamental online learning framework with partial feedback, where the learner observes only the loss incurred at the chosen decision point in each round. In this work, we investigate whether optimistic gradient predictions can improve worst-case regret guarantees in a prediction-adaptive manner. Specifically, given gradient predictions $m_t$, we seek regret bounds that scale with the cumulative prediction error $S_T=\sum_{t=1}^T \|\nabla f_t(x_t)-m_t\|^2.$ We first establish a negative result: under the single-point feedback protocol, an unavoidable $\Omega(\sqrt{T})$ regret lower bound persists even when $S_T=o(T)$, showing that the variance of gradient estimation fundamentally obscures the benefit of accurate predictions. To overcome this barrier, we propose \emph{Two-Point Variance-Reduced Optimistic Gradient Descent} (TP-VR-OPT) for the two-point feedback setting. The key idea is a novel variance-reduced gradient estimator whose variance scales with the prediction error rather than the gradient norm. This yields a regret bound of $O\big(\sqrt{d\,\mathbb{E}[S_T]}\big),$ where $d$ is the decision dimension. Complementing this result, we establish an information-theoretic lower bound that scales as $\Omega(\sqrt{\mathbb{E}[S_T]})$, providing a fundamental characterization of the best achievable prediction-adaptive regret and showing that TP-VR-OPT is optimal up to a factor of $\sqrt d$. We further develop adaptive variants that eliminate the need for prior knowledge of $\mathbb{E}[S_T]$ or the horizon $T$, and extend our framework to non-stationary environments, establishing dynamic regret guarantees that adapt simultaneously to the cumulative prediction error and the comparator path length.

---


### 149. [Ultra-High-Definition Image Quality Assessment via Graph Representation Learning](https://arxiv.org/abs/2605.22192)

**<font color=#1a73e8>作者：</font>** Shaode Yu, Enqi Chen, Ming Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Blind image quality assessment (BIQA) for ultrahighdefinition (UHD) images remains challenging because native-resolution inference is computationally expensive, whereas aggressive resizing or isolated cropping may suppress scale-sensitive distortions and weaken the relationship between local artifacts and global scene context. This paper aims to improve UHD-BIQA by explicitly modeling the structural dependencies among sampled image regions rather than treating them as independent views, and a graph representation learning framework UHD-GCN-BIQA is proposed. The framework samples aspect-ratio-aligned patches from each UHD image, encodes them as graph nodes, and constructs a hybrid k-nearest-neighbor graph using spatial proximity and feature similarity. Residual graph convolution is used to propagate contextual information across regions, and gated attention pooling aggregates patchlevel evidence into an imagelevel quality prediction. An exponential moving average normalized multiobjective loss function is adopted to stabilize the joint optimization of regression, correlation, and ranking objectives. Experiments on the UHD-IQA benchmark show that UHD-GCN-BIQA achieves PLCC = 0.7784, SRCC = 0.8019, and RMSE = 0.0519, obtaining competitive correlation performance and the lowest RMSE among the compared methods. These results indicate that graph-based region relation modeling is effective for UHD image quality assessment, particularly for improving absolute quality score estimation under high-resolution visual content.

---


### 150. [OSS: Open Suturing Skills Vision-Based Assessment Challenge 2024-2025](https://arxiv.org/abs/2605.22200)

**<font color=#1a73e8>作者：</font>** Hanna Hoffmann, Setareh Bady, Claas de Boer 等 57 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Achieving high levels of surgical skill through effective training is essential for optimal patient outcomes. Automated, data-driven skill assessment holds significant potential to improve surgical training. While machine learning-based methods are increasingly popular for assessing skills in minimally invasive surgery, their application to open surgery remains limited. We present the results of a dedicated MICCAI challenge designed to benchmark and advance vision-based skill assessment in open surgery.
The challenge dataset comprises videos of an open suturing training task recorded with a static GoPro camera in a dry-lab setting, with instrument trajectories available in addition to the primary video modality. The OSS Challenge was hosted over two consecutive years, comprising two and three independent tasks, respectively: (1) classifying skill level into four classes, (2) predicting the full Objective Structured Assessment of Technical Skills across eight categories, and (3) tracking hands and surgical tools. Participants submitted diverse solutions including deep learning-based video models, tracking-driven methods, and hybrid approaches.
General-purpose spatiotemporal video models consistently achieved the strongest performance, though conceptually diverse approaches reached competitive levels when well-executed. Predicting fine-grained OSATS scores remains challenging but benefits substantially from increased training data. Keypoint tracking proves difficult given frequent occlusions and out-of-frame instances, limiting current applicability for motion-based skill analysis. This work benchmarks innovative and diverse solutions for surgical skill assessment, highlighting both the promise and current limitations of video-based evaluation in open surgery and identifying critical directions for advancing automated skill assessment toward clinical impact.

---


> [!TIP]
> 当前位于：**101-150**（第 3/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-347](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
