# 📦 其他研究 | 2026年06月25日

> 本类共 **219** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-219](./part-05.md)

---

### 51. [Towards Version-aware Operations and Transaction Memories for Multi-layer MeMo](https://arxiv.org/abs/2606.24040)

**<font color=#1a73e8>作者：</font>** Peiran Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> MeMo proposes language models with explicit multi-layer correlation matrix memories (CMMs), where memorization, retrieval, and forgetting are architectural operations. This paper asks how such memories can reduce the need for retraining when knowledge changes. For changes expressible as MeMo memory associations, the model's accessible knowledge can be updated by editing explicit memories rather than retraining the whole model. We propose a version-aware operation layer in which high-level operations such as replace, obsolete, keep-history, rollback, and trace are compiled into MeMo-native primitive calls over sequences and tokens. The key observation is that a version-aware operation is rarely a single MeMo association. It is an ordered transaction of primitive edits, for example forgetting one sequence-token chain, memorizing another, preserving a historical chain, and recording an inverse program. The framework introduces two auxiliary CMMs: a Version CMM (V-CMM) for mapping version transitions to transaction handles, and a Transaction CMM (T-CMM) for storing reusable change contents and inverse programs. It supports both direct sequence-level edits and structured diff-level inputs, and outlines an evaluation route for update success, rollback, traceability, locality, and transaction reuse.

---


### 52. [Breaking the Filter Bubble: A Semantic Pareto-DQN Framework for Multi-Objective Recommendation](https://arxiv.org/abs/2606.24042)

**<font color=#1a73e8>作者：</font>** Cláudio Lúcio Do Val Lopes, Lucca Machado da Silva, André de Oliveira Brandão  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recommender systems often induce filter bubbles and semantic homogenization by monolithically optimizing for immediate user engagement. Standard single-objective models, including traditional Deep Q-Networks, are ill-equipped to navigate the trade-offs between platform retention and critical societal values like information diversity and provider fairness. To address these limitations, we introduce a multi-objective reinforcement learning framework that formalizes recommendation as a semantic multi-objective Markov decision process. By integrating high-fidelity semantic embeddings with a Pareto-DQN agent, our architecture treats engagement, diversity, and fairness as distinct, non-aggregable reward signals, avoiding the pitfalls of static reward scalarization. Empirical evaluations on the MovieLens small dataset shows that our hypervolume based action selection disrupts the feedback loops responsible for semantic collapse. By sustaining high state-trajectory variance, the Pareto-DQN effectively maps the Pareto frontier, achieving gains in auxiliary societal objectives with only marginal impacts on engagement. This work provides a path toward intrinsically aligned, responsible recommender systems.

---


### 53. [Rapid FinFET Modelling Using an Autoencoder](https://arxiv.org/abs/2606.24046)

**<font color=#1a73e8>作者：</font>** Amit Sarkar Suman Sau, Swagata Mandal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work presents a machine learning framework that leverages an autoencoder (AE) for the efficient modeling of FinFET. We first calibrated a BSIM-CMG model to generate a dataset of current-voltage (ID-VG) characteristics. This data was used to train an autoencoder that compresses full I-V curves into a low-dimensional latent space, which intrinsically encodes key device physics. A key innovation is the explicit incorporation of parameter such as drain to source voltage (VDS) as an input feature, enhancing the model ability to capture bias dependent variation. The trained model successfully reconstructs full I-V curves and directly extracts critical device metrics including threshold voltage (VTH), subthreshold slope (SS), and peak transconductance (gm). This approach demonstrates that data driven compact models, built from actual characterization data, can achieve high accuracy with minimal training data, providing a powerful tool for rapid device characterization, modelling and circuit level simulation.

---


### 54. [Ensemble Feature Selection and Harris Hawks Optimization for Explainable Mental Health Risk Prediction in Female Sex Workers](https://arxiv.org/abs/2606.24047)

**<font color=#1a73e8>作者：</font>** Ahnaf Atef Choudhury, Md. Parvej Hoque Palash, Shahriar Siddique Ayon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> One of the significant mental health issues affecting female sex workers (FSWs) is mental disorders, especially depression. Exposure to violence, stigma, and economic hardship further increases their psychological risk. Current machine learning (ML) models are typically ineffective at capturing the high-dimensional and complex risk patterns that exist in this marginalized group. This paper suggests a hybrid predictive model that merges an ensemble feature selection strategy using ANOVA and mutual information and Harris Hawks optimization-tuned logistic regression and represents a new application of swarm intelligence to predict mental health in vulnerable groups. The explainable AI (XAI) methods can be used to understand the factors of trauma associated with model predictions. When applied to a group of 3,005 FSWs, it can be seen that the proposed model is more effective than traditional classifiers, with an accuracy of 95.78%, an F1 score of 95.77%, and an AUC of 0.96, and identifying post-traumatic stress, client-related violence, and occupational factors as major contributors to depression. This work bridges the gaps between conventional and ML approaches to develop an XAI tool that enables vulnerable groups to receive early assistance, evidence-based targeted psychosocial care, and health planning.

---


### 55. [Best Preprocessing Techniques for Sentiment Analysis](https://arxiv.org/abs/2606.24055)

**<font color=#1a73e8>作者：</font>** Saranzaya Magsarjav, Melissa Humphries, Jonathan Tuke 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sentiment analysis in Twitter datasets is important because it enables monitoring public opinion on products and analysis of political and social movements. One critical step is preprocessing: the automated processing of text for machine learning algorithms. Preprocessing plays a critical role in reducing noise and improving efficiency. However, little research has systematically examined the order in which preprocessing techniques are implemented. We find that, when accounting for order, spelling correction is the least impactful preprocessing technique, whereas tokenisation is the most impactful. Stemming and stop-word removal are interchangeable, and it is better to remove stop words without removing negation. The best order for applying the preprocessing techniques was tokenisation, text cleaning, stemming, and then stopword removal. Our results provide a systematic approach for practitioners to deploy preprocessing to improve model output without the costly preprocessing exploratory phase.

---


### 56. [EPEdit: Redefining Image Editing with Generative AI and User-Centric Design](https://arxiv.org/abs/2606.24057)

**<font color=#1a73e8>作者：</font>** Hoang-Phuc Nguyen, Dinh-Khoi Vo, Trong-Le Do 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The demand for image manipulation has seen a significant increase recently. Traditional tools like Photoshop and Capture One, while powerful, require considerable expertise to use effectively. Generative AI has introduced alternative platforms, such as Luminar Neo, Pixlr X, and Canva. However, many of these solutions, including resource-heavy models like Stable Diffusion, often require substantial retraining and fine-tuning, leading to high costs for users. To address these challenges, we introduce Efficient Photo Editor (EPEdit), an application that integrates a robust backend framework with a user-friendly front-end interface. EPEdit supports a wide range of creative image editing tasks, including image generation, object replacement, object removal, background modification, changes in object pose or perspective, region-specific editing, and thematic collection design, all guided by masks and prompts. Users can interact with the system through simple text commands or by marking areas for precise adjustments, making it accessible even to those without technical expertise. At its core, EPEdit leverages zero-shot image editing algorithms based on Stable Diffusion model, removing the need for additional fine-tuning. This approach enables efficient image manipulation and thematic collection creation. User evaluations for tasks of image editing, thematic design, and overall system performance demonstrate that EPEdit outperforms existing solutions, offering a user-friendly, cost-effective solution for comprehensive image editing.

---


### 57. [VisChronos: Revolutionizing Image Captioning Through Real-Life Events](https://arxiv.org/abs/2606.24058)

**<font color=#1a73e8>作者：</font>** Phuc-Tan Nguyen, Hieu Nguyen, Minh-Triet Tran 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper aims to bridge the semantic gap between visual content and natural language understanding by leveraging historical events in the real world as a source of knowledge for caption generation. We propose VisChronos, a novel framework that utilizes large language models and dense captioning models to identify and describe real-life events from a single input image. Our framework can automatically generate detailed and context-aware event descriptions, enhancing the descriptive quality and contextual relevance of generated captions to address the limitations of traditional methods in capturing contextual narratives. Furthermore, we introduce a new dataset, EventCap (this https URL), specifically constructed using the proposed framework, designed to enhance the model's ability to identify and understand complex events. The user study demonstrates the efficacy of our solution in generating accurate, coherent, and event-focused descriptions, paving the way for future research in event-centric image understanding.

---


### 58. [Ingredient-Level Food Image Segmentation for Nutrition Awareness](https://arxiv.org/abs/2606.24059)

**<font color=#1a73e8>作者：</font>** Jonesh Shrestha  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Food images often contain several visible ingredients, so assigning one dish label to an entire image hides important visual structure. This work studies ingredient-level semantic segmentation on FoodSeg103, where the model predicts an ingredient class for each pixel. Two SegFormer variants were fine-tuned and evaluated under a controlled setup: SegFormer-B0 as the smaller baseline model and SegFormer-B1 as the larger final model. Both models use ImageNet-pretrained MiT backbones with newly initialized 104-class output layers. On the held-out FoodSeg103 test split of 2,135 images, B0 achieved 0.7709 pixel accuracy and 0.2521 mean IoU, while B1 achieved 0.7929 pixel accuracy and 0.3204 mean IoU. B1 improved every saved test metric, including a +0.0683 absolute gain in mean IoU. The system also converts predicted masks into visible ingredient-area percentages, giving a simple visual composition summary of the predicted meal. This summary can serve as a first-pass nutrition-awareness cue by providing a visual alternative to detailed food tracking similar to plate-based meal guidance, but it is not a direct estimate of calories, macronutrients, food mass, volume, density, or true portion size.

---


### 59. [RAVEN: A Regime-Aware Variable-context Expert Network for Financial Time Series Forecasting](https://arxiv.org/abs/2606.24062)

**<font color=#1a73e8>作者：</font>** Cheng He, Zhenyu Guan, Xijie Liang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Financial time series forecasting presents structural challenges absent from standard benchmarks. Log-returns are non-stationary, exhibit exceptionally low signal-to-noise (SNR) ratios, and are governed by regime-dependent temporal dependencies. We identify a key limitation of state-of-the-art (SOTA) time series models in financial settings. A fixed context window is mismatched to the time-varying optimal look-back of non-stationary price processes. We propose the Regime-Aware Variable-context Expert Network (RAVEN), a Mixture-of-Experts framework designed to adaptively determine the temporal context for each input sample. Instead of relying on a fixed look-back horizon, RAVEN constructs a hierarchy of nested contiguous windows whose lengths are determined by the data itself. Specifically, RAVEN scores patches by learned importance in reverse chronological order and applies the Cumulative Importance Thresholding (CIT) mechanism to derive nested prefix windows, each routed to a scale-specialized expert. A Global Compressed Representation (GCR) branch runs in parallel over the full context, preserving global temporal coherence that local experts cannot guarantee. Because the nested routing induces structured overlap among expert inputs, we introduce a Correlation-Aware Weighting (CAW) to align variable-length expert outputs and penalize pairwise cosine similarity prior to aggregation. Experiments on cumulative log-return prediction (HS300, S&P500) and fund sales forecasting demonstrate that RAVEN achieves SOTA performances, improves Pearson correlation by 9.2% on HS300 and 20.2% on S&P500, and reduces MSE by 18.2% on fund sales forecasting, while achieving the best results in 14 of 16 metrics on four PEMS traffic benchmarks.

---


### 60. [Selective Capability Unlearning in End-to-End Spoken Language Understanding](https://arxiv.org/abs/2606.24063)

**<font color=#1a73e8>作者：</font>** Akanksha Singh, Vinod Kumar Kurmi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern spoken language understanding (SLU) systems are increasingly deployed in real-world settings, where specific functionalities may need to be removed due to policy or safety constraints. In SLU, a functionality corresponds to an intent and its associated slot-generation behavior. However, in autoregressive models, suppressing a target intent does not eliminate the conditional mapping that generates slots conditioned on that intent. When the intent prefix is externally supplied, the model can reconstruct the original intent-slot structure. We identify this structural failure as \textbf{\emph{capability persistence}}. We propose \textit{\underline{B}inding \underline{S}ubspace (BSU)}, a representation-level framework that isolates and attenuates intent-conditioned directions underlying this mapping. Across SLU benchmarks, BSU substantially reduces forced-prefix recoverability while preserving retained performance.

---


### 61. [ObsGraph: Hierarchical Observation Representation for Embodied Reasoning and Exploration](https://arxiv.org/abs/2606.24068)

**<font color=#1a73e8>作者：</font>** Taekbeom Lee, Youngseok Jang, Jeonghwa Heo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Embodied reasoning and exploration are increasingly considered crucial abilities for robots operating in complex and unfamiliar environments. To accomplish tasks in such settings, an agent must identify and acquire the information necessary for the task through exploration. We propose ObsGraph, an observation-centric hierarchical scene graph that unifies scene representation, retrieval, and exploration. It retains visual evidence and organizes it into room-view-object layers: rooms provide coarse semantic anchors, views preserve contextual object covisibility, and objects store fine-grained details. On top of this representation, we perform coarse-to-fine hierarchical retrieval under a bounded budget, and crucially use retrieval outcomes to structure the exploration candidate space--activating room-level exploration, view refinement, or frontier exploration--thereby tightly coupling representation, retrieval, and adaptive multi-scale exploration. Experiments across embodied reasoning and exploration benchmarks demonstrate improved success and efficiency, highlighting the benefits of structured scene representation and more targeted information gathering driven by identified evidence gaps.

---


### 62. [Fabric Image Demoiréing Benchmark from Synthesis to Restoration](https://arxiv.org/abs/2606.24072)

**<font color=#1a73e8>作者：</font>** Pengchao Wei, Xiaojie Guo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fabric moiré is a sampling-induced aliasing artifact caused by the interaction between fine textile patterns and camera sensor grids, producing structured interference that severely degrades image quality. Unlike screen-induced moiré, which stems from strictly periodic display lattices, fabric moiré is intrinsically more challenging due to the broadband and semi-periodic nature of textile weaves. The heavy spectral overlap between intrinsic texture and aliasing components renders fabric demoiréing substantially more ill-posed. Consequently, existing models trained on screen moiré datasets generalize poorly to these complex textile patterns. Despite its practical importance, fabric image demoiréing remains underexplored and lacks standardized benchmarks. We present the first comprehensive benchmark for fabric image demoiréing. To address the difficulty of acquiring pixel-aligned real-world pairs, we develop a physically motivated synthesis framework and construct a large-scale dataset comprising 16,050 paired multi-resolution fabric images with controllable aliasing severity. Furthermore, we customize a baseline model, which establishes promising performance on the proposed benchmark dataset with strong generalization ability. Our benchmark provides a standardized platform for advancing research in fabric image demoiréing.

---


### 63. [End-to-End Radar and Communication Modulation Recognition with Neuromorphic Computing](https://arxiv.org/abs/2606.24075)

**<font color=#1a73e8>作者：</font>** Xiaohu Li, Chongxiao Qu, Caiyong Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although deep learning-based methods can achieve high accuracy in automatic modulation recognition (AMR) tasks, their high computational cost makes it difficult to strike a balance between accuracy and power consumption, thereby limiting their application on resource-constrained platforms. Neuromorphic architectures that perform spike-driven inference with modest energy budgets have recently been explored for vision and timeseries tasks. Motivated by these works, we propose EMRFormer, a novel end-to-end spiking nerural network (SNN) architecture that applies spike-driven transformer to the constraints of neuromorphic hardware for AMR. The model incorporates an adaptive spike encoder and Integer Leaky Integrate-and-Fire neurons to mitigate the degradation of effective information and enhance SNN representational capacity. By integrating spike-separable Convolution Neural Networks (SSCNN) into Spike-Driven Transformers (SpikeFormer), EMRFormer effectively extracts multi-scale temporal features from the raw IQ waveforms. We validate our approach across various mainstream datasets, the experimental results show that EMRFormer achieves state-of-the-art interms of accuracy, outperforming all the baselines. Furthermore, the model maintains strong performance in low signal-to-noise(SNR) environments and reduces theoretical energy consumption by over 90%. Finally, we evaluate our model on a KA200 neuromorphic chip. The results show that our model achieves up to 5 times reduction in power compared to running on a 3090 GPU or an Orin NX. This work demonstrates a promising pathway for AMR on resource-constrained devices.

---


### 64. [PixJail: Self-Evolving Paper-to-Pipeline Reproduction for Text-to-Image Jailbreak Evaluation](https://arxiv.org/abs/2606.24081)

**<font color=#1a73e8>作者：</font>** Leyi Sheng, Han Sun, Zhen Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As Text-to-Image (T2I) jailbreak techniques evolve rapidly, existing benchmarks and reproduction workflows often struggle to keep pace. More importantly, T2I jailbreak evaluation is not a single prompt-level test, but a pipeline-level problem shaped by multiple stages, including prompt transformation, image generation, safety filtering, and multimodal judging. This makes results across papers difficult to reliably reproduce and fairly compare. To bridge this gap, we propose PixJail, a self-evolving paper-to-pipeline agent framework for reproducible T2I jailbreak evaluation. Given a T2I jailbreak paper and optional reference code, PixJail rapidly constructs a paper-specific attack module and a runnable evaluation pipeline under a unified contract, while faithfully reproducing the original experimental results. PixJail further maintains a memory bank that stores paper digests, attack evolution patterns, reusable templates, failure cases, and versioned artifacts, enabling future reproduction efforts to reuse prior experience. We reproduce eleven representative T2I jailbreak methods, including both code-available and code-unavailable papers. Under their original settings, our framework accurately recovers prior results with minimal error (2.1\% average, 0\% median). We hope that PixJail can serve as a unified foundation for future T2I jailbreak reproduction and evaluation, significantly reducing manual effort.

---


### 65. [Blockwise Policy-Drift Gating for On-Policy Distillation](https://arxiv.org/abs/2606.24084)

**<font color=#1a73e8>作者：</font>** Liwen Zheng, Haiyun Jiang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains a student policy using teacher signals computed on trajectories sampled by the student itself. Recent work shows that sampled-token OPD can be fragile on long-horizon reasoning tasks and that local teacher-support matching is a simple and effective repair. This paper introduces blockwise policy-drift gating, a lightweight student-only old-current drift controller for OPD under rollout reuse. The method computes log-probability shifts between the behavior student and the current student on the sampled token path, aggregates these shifts over fixed blocks or spans, and uses the resulting detached, mean-normalized gates to reweight OPD position losses. It does not change teacher targets, teacher top-K supports, or the rollout policy. In a six-variant Qwen3 math reasoning benchmark with a uniform 200-step training budget for all trained variants, we use pass@8 as the primary problem-level solve-rate metric. Fixed 64-token block gating improves sampled-token OPD mean pass@8 from 0.4978 to 0.5160 across AIME24, AIME25, MATH500, and AMC23. On Teacher-TopK/LSM, Block64 gives the best four-benchmark mean pass@8 among trained students. The results identify local old-current policy drift as a practical control signal for reused OPD rollouts and motivate block-level gating as a simple default for improving solve-rate robustness.

---


### 66. [NeuroSonic: Conditional Flow Matching for EEG-to-Speech Reconstruction](https://arxiv.org/abs/2606.24087)

**<font color=#1a73e8>作者：</font>** Wenhao Gao, Yifan Wang, Yijia Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reconstructing continuous speech from scalp electroencephalography (EEG) remains fundamentally challenging. EEG provides a weak, spatially diffuse, and highly variable measurement of distributed cortical activity, whereas speech is organized as a coherent acoustic trajectory with strong harmonic and temporal structure. The resulting mismatch makes waveform regression unstable and causes stochastic multi-step generation to be sensitive to artifact-dependent conditioning and subject variability. We introduce NeuroSonic, a conditional flow-matching framework for EEG-to-speech reconstruction. Instead of predicting waveforms directly or refining them through stochastic denoising, NeuroSonic learns a deterministic probability-flow velocity field that transports a noise-corrupted acoustic state toward clean speech under EEG conditioning. EEG and audio are embedded into a shared token space and processed by a time-conditioned gated Transformer that parameterizes the transport ordinary differential equation. This formulation models trajectory evolution explicitly while avoiding iterative stochastic sampling. We evaluate NeuroSonic on the CineBrain and EAV benchmarks under cross-subject evaluation. Across both datasets, the proposed method improves distributional realism, spectral fidelity, and perceptual quality over representative GAN-, diffusion-, and mean-flow baselines, with up to a 26.3\% gain in overall perceptual quality. The performance gap is most evident in artifact-heavy segments, where conditioning variability is strongest. These findings indicate that deterministic conditional transport provides a stable and effective formulation for EEG-driven speech reconstruction. Code is available at this https URL .

---


### 67. [Progressive Pixel-Neighborhood Deformable Cross-Attention for Multispectral Object Detection](https://arxiv.org/abs/2606.24092)

**<font color=#1a73e8>作者：</font>** Tian Qiu, Jifeng Shen, Xin Zuo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Effective cross-modal feature alignment and interaction are central challenges in multispectral object detection. Although global cross-attention provides strong long-range modeling ability, its quadratic complexity with respect to feature size limits deployment on resource-constrained platforms. We therefore propose Progressive Pixel-Neighborhood Deformable Cross-Attention for multispectral feature fusion, termed PNAFusion. The proposed framework is motivated by two observations: weak misalignment between visible and thermal images is usually concentrated around local neighborhoods, and semantic correspondence across modalities often follows non-linear spatial mappings that fixed receptive fields cannot model well. To address these issues, PNAFusion incorporates local spatial priors into its architectural design to concentrate feature interaction and alignment on the most relevant neighborhoods. Specifically, a Pixel-Neighborhood Cross-Attention (PNCA) module is introduced to avoid redundant global feature matching and suppress background noise. Meanwhile, an Adaptive Deformable Alignment (ADA) module captures non-linear spatial correspondences through learned pixel-wise offsets. These components are further integrated through an iterative feedback mechanism to progressively refine cross-modal feature alignment. Experiments on FLIR, M3FD, and DroneVehicle show that PNAFusion achieves 84.2, 90.5, and 85.5 mAP@0.5, respectively, under the YOLOv5 detector, and further reaches 86.8 mAP@0.5 on FLIR and 90.8 mAP@0.5 on M3FD when transferred to Co-DETR. Efficiency analysis indicates that PNAFusion reduces allocated GPU memory by 33.0\% compared with ICAFusion and reduces theoretical FLOPs from 194.8 G to 156.4 G, although the deformable sampling and iterative refinement introduce additional latency. Our code will be available at this https URL.

---


### 68. [Predicting Poets' Origins from Verse: A Computational Analysis of Regional Linguistic Fingerprints in the Complete Tang Poems](https://arxiv.org/abs/2606.24093)

**<font color=#1a73e8>作者：</font>** Chi-Sheng Chen, Hung-Yun Liu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We ask whether the geographic origin of Tang-dynasty poets leaves a detectable linguistic trace in their work. Aggregating every poem attributed to each author in the Complete Tang Poems (Quan Tang Shi) and linking poets to their administrative circuit of origin via the China Biographical Database (CBDB), we build a poet-level corpus of 357 poets across the ten Tang circuits and frame origin prediction as multi-class classification. Using character $n$-gram TF-IDF together with interpretable domain features (imagery, season, and allusion), classical and neural models predict a poet's broad region (South vs.\ North) at $0.69$ accuracy, well above the $0.53$ majority baseline, and finer circuit-level origin above chance. Beyond classification, three findings emerge. (i) Linguistic distance between circuits grows with geographic distance (Mantel $r=0.40$, $p\approx0.09$ over nine circuits), evidence of a distance-decay effect in poetic language. (ii) The signal interacts with time: South/North separability is at chance in the High Tang and strongest in the Late Tang, consistent with court-driven homogenization at the empire's height followed by regional divergence. (iii) The model's confident errors are historically meaningful -- in the Early Tang, every misclassification is a southern poet read as northern, reflecting the prestige of the northern court idiom. We further show that, when given the whole corpus through a hierarchical frozen-encoder representation, a classical-Chinese transformer (GuwenBERT) only matches -- not beats -- simple TF-IDF, and that combining them adds nothing, indicating that character $n$-grams already capture the regional signal. Our results position interpretable machine learning as a hypothesis generator for literary history.

---


### 69. [Beyond Bayer: Task-Optimal Sensor Co-Design for Robust Autonomous-Driving Segmentation](https://arxiv.org/abs/2606.24096)

**<font color=#1a73e8>作者：</font>** Reeshad Khan, John Gauch  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robust perception underpins autonomous driving, and most recent progress comes from scaling the model-larger backbones, foundation models, and cooperative multi-agent fusion. We pursue a complementary, upstream question: what should the camera itself measure? Using a differentiable RAW-to-task pipeline, we decompose which sensor degrees of freedom benefit dense prediction. Learning the spectral colour-filter-array (CFA) weights is the dominant lever, improving mIoU by +0.017 (KITTI-360) and +0.023 (ACDC) over a fixed camera. In contrast, point-spread-function (optics) co-design is net-negative (-0.020 mIoU on KITTI-360) - a consequence of the data-processing inequality, which also bounds the task information that any downstream model, however large or cooperative, can recover. Noise co-optimisation is marginal, and counter to intuition enlarging the CFA tile beyond 2x2 consistently hurts, as the filters are confined to the rank three sRGB input. Because the intervention is at the sensor, the gains are model-agnostic; we validate robustness on ACDC's fog, night, rain, and snow, and conclude with a simple recipe: learn the 2x2 CFA weights and keep an identity PSF.

---


### 70. [Exploring Academic Influence of Algorithms by Co-occurrence Network Based on Full-text of Academic Papers](https://arxiv.org/abs/2606.24099)

**<font color=#1a73e8>作者：</font>** Yuzhuo Wang, Chengzhi Zhang, Min Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Algorithms have become central to scientific research in the era of artificial intelligence (AI). Although algorithm mentions in papers are often used to indicate popularity and influence, existing studies usually evaluate individual algorithms in isolation and pay limited attention to the collective influence formed through their interconnections. This study constructs large-scale algorithm co-occurrence networks in natural language processing (NLP) based on the full text of academic papers and investigates algorithm influence from a network perspective. Using deep learning models, we extract algorithm entities and build overall, cumulative, and annual co-occurrence networks. We analyze their structural characteristics and apply multiple centrality measures to assess the group influence of algorithms across the whole field and over time. The results show that algorithm networks display typical features of complex networks, with increasingly dense connections developing over approximately two decades. Classic, high-performing algorithms and those located at the intersections of different research periods tend to have high popularity, control, centrality, and balanced influence. When the influence of an algorithm declines, it usually loses its core network position first, followed by weaker associations with other algorithms. This study is the first large-scale analysis of algorithm co-occurrence networks. Covering more than four decades of academic publications, it provides a temporal and structural view of algorithm influence and offers a foundation for future research on networks linking algorithms, scholars, and tasks.

---


### 71. [The impact of generative artificial intelligence on academic development of Chinese students in humanities and social sciences](https://arxiv.org/abs/2606.24104)

**<font color=#1a73e8>作者：</font>** Lei Fan, Fangxue Liu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative artificial intelligence(GenAI) is reshaping learning in higher education, with particularly pronounced implications for the humanities and social sciences(HSS), where learning outcomes are commonly expressed through written and interpretive forms that align closely with GenAI's capabilities. Yet, systematic evidence on the educational impacts of GenAI on HSS students remains limited. Addressing this gap, this study draws on a large-scale survey of HSS students in China to examine its role in academic development. Guided by relevant learning theories, this study focuses on four dimensions: patterns of use, effects on learning processes and academic performance, challenges associated with GenAI use, and preferred approaches to curricular integration. We found that more than half perceived enhanced learning motivation, independent thinking and creativity, although a substantial minority reported little change or even decline. Comparatively, a notably larger majority reported academic performance gains, although these gains may partly reflect limitations in conventional assessment practices. The study identifies variations in perceived learning and performance improvements among students with differing durations of GenAI experience, along with observable disciplinary differences and modest gender differences. While an overwhelming majority valued the importance of ethical considerations, only slightly more than half were satisfied with privacy protection. Limited accuracy and overreliance emerged as the most pressing concerns reported by students. Students favored partial or optional curricular integration supported by practice-oriented training, and widely recognized GenAI's significance for their future professional development. Grounded in student perspectives, this study offers evidence-based recommendations for the responsible and pedagogically meaningful integration of GenAI

---


### 72. [DoHFuse: A Dual-Branch Architecture with DMAGLSTM for Website Fingerprinting over DNS over HTTPS/3](https://arxiv.org/abs/2606.24105)

**<font color=#1a73e8>作者：</font>** ZunDong Zhang, Yanan Cheng, Zhaoxin Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As personal data privacy becomes increasingly critical in Internet of Things (IoT) environments, secure DNS protocols such as DNS over HTTPS (DoH) and DNS over TLS (DoT) have been widely adopted to protect device communications. However, without effective obfuscation, these protocols remain vulnerable to Website Fingerprinting (WF) attacks that can reveal user activity. With the ongoing deployment of DNS over HTTP/3 (DoH/3) in modern networked systems, padding strategies have been increasingly applied in practice. It is therefore essential to investigate whether DoH/3 can effectively mitigate WF attacks in realistic IoT and edge-network scenarios. To address this, we first collect and publicly release the first real-world benchmark dataset of DoH/3 traffic, generated from domain resolution processes in practical network environments. We further propose DoHFuse, a dual-branch learning framework that integrates inter-arrival time sequences and refined statistical features through an improved DMAG-LSTM, specifically designed to capture burst-aligned temporal patterns. Experimental results show that DoHFuse achieves an accuracy of 88.05% (precision 88.56, recall 87.96, F1 87.83) in a closed-world setting of 449 classes, and an AUPRC of 0.975 with an F1 score of 0.951 (precision 0.906, recall 1.0) in open-world detection. These findings demonstrate that DoH/3 traffic remains susceptible to WF attacks, suggesting that commonly deployed padding mechanisms alone are insufficient to ensure privacy protection in IoT-scale encrypted DNS communications.

---


### 73. [DramaDirector: Geometry-Guided Short Drama Generation](https://arxiv.org/abs/2606.24107)

**<font color=#1a73e8>作者：</font>** Hengji Zhou, Sijie Liu, Jianrun Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Short dramas, with their rapid shot rhythms, dialogue-driven focus shifts, and demanding cinematographic grounding, pose challenges that prompt-level or text-only video generation pipelines struggle to meet. We study plot-to-short-drama generation, where a global plot and local context are transformed into visually grounded multi-shot videos. We propose DramaDirector, a geometry-grounded framework that lets the planner borrow cinematographic geometry from a gallery of real short-drama shots indexed by depth and pose. DramaDirector decouples each shot into static visual and dynamic narrative conditions, trains the planner with schema-constrained SFT and GRPO under a learned text-visual alignment reward, and retrieves depth-pose references to guide first-frame generation and image-to-video synthesis. We also introduce DramaBoard, a benchmark built from 35 live-action dramas, 2.8K episodes, and 81K shots, with structured storyboards and multi-dimensional evaluation protocols. Experiments show that DramaDirector improves over representative multi-agent and video generation baselines on faithfulness, consistency, and controllability. Our code is released at: this https URL

---


### 74. [FedUP: One-Shot Federated Unlearning via Centroid-Guided Plug-in Filters](https://arxiv.org/abs/2606.24113)

**<font color=#1a73e8>作者：</font>** Feihong Nan, Zhengyi Zhong, Pan Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated unlearning (FU) is critical for complying with legal mandates like the right to be forgotten in decentralized systems, yet current methods face a persistent dilemma between non-target knowledge loss and high request latency. To resolve these issues, we propose FedUP, a one-shot federated unlearning framework utilizing lightweight pluggable filters that act as a "knowledge funnel" to screen out target data while preserving original model performance. By freezing original model parameters and training filters at the server side using differentially private (DP)-protected class centroid samples, FedUP bypasses the need for multi-round client-server communication and complex retraining, reducing unlearning latency from minutes to mere seconds. Additionally, the framework's pluggable architecture ensures inherent reversibility, enabling the seamless restoration of forgotten knowledge by simply removing the filters. Extensive experiments on diverse image and text tasks demonstrate that FedUP effectively reduces non-target knowledge loss and achieves superior unlearning precision and efficiency across various scenarios. Code is available at: this https URL.

---


### 75. [An LMM for Precisely Grounding Elements in Documents](https://arxiv.org/abs/2606.24118)

**<font color=#1a73e8>作者：</font>** Yijian Lu, Chuangxin Zhao, Kai Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual grounding in documents is a crucial ability for Large Multimodal Models (LMMs) in areas such as document understanding, deep research and document error detection. However, existing approaches exhibit poor grounding precision in text-rich document images, often failing to accurately locate the critical document elements needed for reliable reasoning. To address this gap, we introduce PreciseDoc, an LMM specifically designed for precise element grounding and can be further optimized for Document VQA tasks. Specifically, to enhance the basic localization capability, we construct challenging training data by two pipelines capable of mass-producing high-quality documents with paired metadata of fine-grained coordinates, including synthetic hand-filled documents with camera effects. The model develops more real-world functions beyond straightforward localization of single text, such as locating personal information from CVs. Furthermore, we introduce a training paradigm for visual grounded reasoning where the grounding and reasoning are supervised jointly with reinforcement learning to improve the contribution of the grounded evidence. A comprehensive evaluation on various benchmarks demonstrates the advantage of the proposed data and methods in document spatial grounding and document understanding.

---


### 76. [When Top-1 Fails: Calibrating LoRA Monitors for Masked Diffusion LMs](https://arxiv.org/abs/2606.24119)

**<font color=#1a73e8>作者：</font>** Lucky Verma, Pratik Yadav  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrete diffusion language model (DLM) fine-tuning inherits inexpensive diagnostics from denoising-time confidence monitors, but their PEFT-training meaning is untested. We test top-1 argmax concentration as a collapse warning. Across 816 LoRA/PEFT configurations from three DLM families, the warning fires for every configuration while logs record 0/816 actual collapses at the 200 step horizon, giving zero precision. The cause is pre-equilibrium saturation: top-1 concentration is already high before optimization and quickly becomes insensitive to final training stability. We then evaluate max LoRA gradient norm, a parameter-side signal that samples gradient routing rather than token concentration. On a pooled held-out LLaDA-family split, a train-optimized threshold identifies top-decile final-loss configurations with precision 0.68 and F1=0.79, above the all-positive top-1 baseline even at the lower split-bootstrap confidence bound. Autoregressive controls and cross-family threshold failures bound the result to short-horizon DLM-LoRA inspection rather than a universal collapse detector. Workflow: drop top-1 as a PEFT alarm, log max-gradient early in training, and calibrate thresholds per DLM family before routing runs for inspection.

---


### 77. [Bengal-HP_RU: A Dataset of Bengal People For Head Pose Estimation](https://arxiv.org/abs/2606.24122)

**<font color=#1a73e8>作者：</font>** Md. Ahanaf Arif Khan, Md. Tawhidur Rahman, Sangeeta Biswas 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing head pose datasets predominantly feature subjects of Western or East Asian origin, leaving South Asian populations, particularly Bengali individuals, largely underrepresented. We introduce Bengal-HP_RU, the first publicly available head pose dataset centred on Bengali subjects, comprising 12,894 labelled head images annotated with continuous yaw, pitch, and roll values. Images were collected from Wikimedia Commons under free licences and processed through an automated pipeline followed by manual label correction. The dataset is partitioned by Wikimedia uploader identity to prevent data contamination, yielding 10,494 training and 2,400 test images across 296 unique uploaders. Bengal-HP_RU exhibits substantial diversity in subject age, gender, occlusion, illumination, and background, reflecting realistic in-the-wild conditions. The dataset is publicly available at this https URL.

---


### 78. [VeryTrace: Verifying Reasoning Traces through Compilable Formalism and Structured Verification](https://arxiv.org/abs/2606.24124)

**<font color=#1a73e8>作者：</font>** Ninghan Zhong, Ahmet Ege Tanriverdi, Kaan Kale 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-step reasoning with Chain-of-Thought (CoT) prompting remains fragile: logical errors or hallucinations in early steps silently propagate, producing confident but incorrect conclusions. This paper presents VeryTrace, a zero-shot verification-and-repair framework that formalizes natural-language reasoning traces into a structured, compilable representation. VeryTrace introduces a Domain-Specific Language (DSL) that (i) makes step dependencies explicit, (ii) mechanizes quantitative content as executable expressions, and (iii) structures semantic inferences via deduction schemas. Our hybrid verifier combines deterministic checks for computational correctness, dependency resolution, and constraint satisfaction with targeted LLM audits for non-mechanizable semantic judgments, enabling step-level error localization and repair.
Across three diverse domains-competition mathematics (AIME 2025), robotics planning (LLM-BabyBench), and kinship reasoning (CLUTRR), VeryTrace improves accuracy over zero-shot baselines on state-of-the-art LLMs without requiring domain-specific training or in-context examples, demonstrating that formalized trace verification achieves both precision and generalization.

---


### 79. [Human-Centered Design: The Disclosure of Generative Artificial Intelligence for Emerging Professionals](https://arxiv.org/abs/2606.24136)

**<font color=#1a73e8>作者：</font>** Sydney Lee  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As the Human centered design continues to grow, generative AI has the potential to streamline the research process by iterating tasks within established workflows to increase efficiency. However, integrating AI raises concerns surrounding ethical bias, complexity, and the lack of prioritization of humanistic values. Emerging professionals represent a cohort with the opportunity to learn Human Centered Design principles, yet without this foundation AI becomes more of a crutch than a tool, leading to reduced experience with deep work, decreased autonomy, and deskilling of key foundations. Disclosures are a common method to self report AI usage, but they provide little clarification on appropriate implementation and may encourage omission to avoid consequences. This paper reflects on experiences in the Human Centered Design course ITIS8300, which emphasized optimizing user experience, enhancing innovation and collaboration, and improving efficiency through iterative user feedback. A semester long project, structured through milestones and team roles including a generative AI advocate, resulted in a high level disclosure report detailing design processes, methodology, findings, and rationale for AI usage. The course offered freedom in execution while setting clear boundaries for incorporating human feedback, reinforcing justification for HCI workflows and encouraging transparent AI use. This approach mirrors an industry with minimal regulation, demonstrating that when AI usage is safe, justified, and transparent, it can significantly advance the field through AI augmented workflows and support co creation an increase productivity.

---


### 80. [Sat2City v2: Native 3D City Asset Generation from a Single Satellite Image](https://arxiv.org/abs/2606.24138)

**<font color=#1a73e8>作者：</font>** Tongyan Hua, Dongli Wu, Jinjing Zhu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating explicit 3D city assets from a single satellite image is important for digital twins, urban simulation, and geospatial intelligence. Unlike satellite-to-street-view synthesis, the task requires a reusable textured mesh with plausible geometry and controllable appearance rather than a 3D proxy optimized only for rendering a small set of images or videos. The ICCV Sat2City framework made a first step by conditioning cascaded sparse-voxel latent diffusion on satellite-derived height maps, but its appearance was random, its training data were synthetic, and its task-specific VAE did not scale well to noisy real-world reconstructions. We present Sat2City v2, a journal extension that adapts a pretrained native structured-latent 3D foundation model to weakly aligned satellite images and textured meshes. We build a real-world dataset with 16,241 satellite-mesh pairs across 24 regions in 9 cities. Instead of learning a 3D representation from noisy city meshes, Sat2City v2 encodes each mesh into a pretrained native 3D latent space, fine-tunes a satellite-conditioned geometry flow, and uses the decoded shape to anchor satellite-conditioned texturing. This retains Sat2City's geometry-to-appearance cascade while enabling appearance-controllable generation from the satellite input. Experiments on metric-scale DSM reconstruction and generative city-asset benchmarks for geometry and appearance show that Sat2City v2 achieves the best overall performance among evaluated baselines. Overall, Sat2City v2 advances satellite-to-city generation from rendering-oriented 3D proxies to explicit textured mesh assets, supported by, to the best of our knowledge, the first documented satellite-mesh paired dataset collected from matched geographic crops for this asset-level task. Project page: this https URL

---


### 81. [A Time-Reparameterized Cumulative Intensity Extrapolation Sampler for Discrete Flow Matching](https://arxiv.org/abs/2606.24140)

**<font color=#1a73e8>作者：</font>** Feiyang Fu, Hehe Fan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrete flow matching (DFM) provides a principled framework for generative modeling on discrete state spaces via continuous-time Markov chain dynamics. In practice, sampling for DFM commonly employs discretizations such as $\tau$-leaping, yet efficient sampling methods under a limited number of function evaluations (NFE) remain less studied. To address this gap, we propose the Time-Reparameterized Cumulative Intensity Extrapolation (TR-CIE) sampler, which aims to improve sampling quality when function evaluations are restricted. TR-CIE consists of two components. First, a schedule-based time reparameterization rescales the time grid according to the noise schedule. Under standard factorized DFM rate parameterizations, this transformation of variables absorbs the schedule-dependent growth term and mitigates stiffness near the terminal sampling stage. Second, we introduce a cumulative-intensity extrapolation updating rule. By reusing cached model outputs from the previous step as a history term, this improves the approximation of stepwise cumulative intensities on the resulting non-uniform time grid. We provide a theoretical analysis that bounds the local approximation error of cumulative intensities and establishes convergence results. The resulting sampler requires one NFE per step and introduces no additional model evaluations compared to the standard $\tau$-leaping sampler. Extensive experiments on synthetic tasks, text generation, and text-to-image benchmarks demonstrate that our method improves sampling quality under limited NFE.

---


### 82. [Geometry-Aware Style Transfer in 3D Gaussian Splatting](https://arxiv.org/abs/2606.24144)

**<font color=#1a73e8>作者：</font>** Min Hyeok Bang, Jun Hyeong Kim, Seung-Wook Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we present a novel geometry-aware style transfer framework for 3D Gaussian splatting (3DGS) that simultaneously transfers appearance attributes and geometric structures. Unlike prior works that primarily focus on color-based stylization and often overlook structural adaptation, our method explicitly incorporates geometry adaptation through a decoupled optimization scheme that alternately updates color and geometry parameters. This strategy alleviates potential interference between color and geometry updates, leading to stable and consistent scene-level geometry transformation. The decoupled optimization is enabled by the proposed geometry-aware contrastive feature matching (GCFM). GCFM integrates RGB, depth, and edge cues into a contrastive objective and is employed in both optimization phases to effectively transfer structural characteristics from style images to Gaussian primitives. Extensive experiments show that our approach achieves superior performance in both qualitative fidelity and quantitative metrics, significantly outperforming existing 3DGS-based stylization methods. Our code is available at \href{this https URL}{this https URL}.

---


### 83. [Metis: Bridging Text and Code Memory for Self-Evolving Agents](https://arxiv.org/abs/2606.24151)

**<font color=#1a73e8>作者：</font>** Zijie Dai, Siuhin He, Hui Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-evolving agents improve over time by distilling experience from past executions and reusing it in future tasks. Existing systems represent such experience either as natural-language text injected into the agent context or as code exposed as callable tools. However, the choice between these representations is typically made at design time rather than derived from the characteristics of the experience itself, leaving the trade-offs between them poorly understood. We present the first controlled study that isolates text memory and code memory over an identical set of experiences. Our results show that the two forms exhibit complementary trade-offs in construction cost, execution efficiency, and transferability, such that neither representation alone is sufficient. Guided by these findings, we propose Metis, a self-evolving agent system built on a hierarchical dual-representation memory. Metis organizes textual experience into execution plans, environment facts, and common pitfalls, and selectively crystallizes recurring plans into validated callable tools. This design combines the broad applicability of text memory with the execution efficiency of code memory while incurring tool-generation cost only when justified by repeated reuse. We evaluate Metis on AppWorld, a challenging benchmark for interactive agents. The results show that Metis improves task accuracy by up to 20.6% over ReAct while reducing execution cost by up to 22.8%. Compared with representative self-evolving agent systems, Metis consistently achieves a better balance between accuracy, execution efficiency, and memory-construction cost.

---


### 84. [Differential Unfolding: Efficient Unfolding Reconstruction for Video Snapshot Compressive Imaging](https://arxiv.org/abs/2606.24153)

**<font color=#1a73e8>作者：</font>** Muyuan Zhang, Jiancheng Zhang, Haijin Zeng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Deep Unfolding Networks (DUNs) dominate video Snapshot Compressive Imaging (SCI), they remain constrained by a uniform design philosophy. Existing methods repeatedly stack high-complexity priors with identical structures, ignoring the fact that optimization trajectories converge toward static states. This results in representation stagnation, where high-cost computations are wasted on minimal feature updates. To address this inefficiency, we present Differential Unfolding (DU), a heterogeneous framework that replaces uniform repetition with dynamic evolution. Central to DU is the Differential Evolutionary Framework (DEF), which partitions the unfolding process into two complementary roles: structural anchoring and differential evolution. In this scheme, high-parameter general stages are sparsely deployed to generate high-fidelity feature foundations. Complementing these, lightweight differential stages employ a Differential Representation Prior (DRP) to propagate and refine these foundational features through a differential mechanism. By integrating Differential Representation Attention (DRA) for evolving attention maps and a Differential Modulated FFN (DM-FFN) for feature rectification, DRP effectively models cross-stage variations with minimal overhead. By focusing computational resources on dynamic evolution rather than static redundancy, DU achieves a superior trade-off between accuracy and efficiency. Extensive experiments verify that our method establishes new state-of-the-art results while significantly slashing computational overhead. this https URL

---


### 85. [The Geometry Behind Diffusion and Flow Matching: Gradient Flows and Geodesics in Wasserstein Space](https://arxiv.org/abs/2606.24157)

**<font color=#1a73e8>作者：</font>** Yian Yao, Weiwei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The space $\mathcal{P}_2(\mathbb{R}^d$) of probability measures with finite second moment carries a natural geometry: the quadratic Wasserstein distance W_2 makes it a complete metric space and, following Otto, a (formal) Riemannian manifold whose geodesics are the optimal-transport interpolations. On this manifold, the gradient flow of the free energy F(rho) = KL(rho || \pi) is exactly the Fokker-Planck equation, and its implicit-Euler discretization is the JKO scheme. This is the geometry underlying diffusion models: the forward process descends the free energy, and each denoising step realizes one JKO step, which recovers DDPM, DDIM, NCSN/SMLD, and Energy Matching; this is one scheme, not separate theories. The same manifold supports a second variational principle. Its geodesics - the minimum-action curves of the Benamou-Brenier formula - are precisely the optimal-transport paths that Flow Matching learns. Fixing both endpoints and following the geodesic, generation becomes a deterministic ODE along a straight line, hence far fewer sampling steps. Placing both families of models on one manifold makes their relationship exact: diffusion follows a free-energy gradient flow, an initial-value problem; optimal-transport Flow Matching follows a Wasserstein geodesic, a boundary-value problem. The two reach the same endpoints along different paths.

---


### 86. [An Introduction to Causal Reinforcement Learning](https://arxiv.org/abs/2606.24160)

**<font color=#1a73e8>作者：</font>** Elias Bareinboim, Junzhe Zhang, Sanghack Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Causal inference provides a set of principles and tools that allow one to combine data and knowledge about an environment to reason with questions of counterfactual nature, i.e., what would have happened had reality been different, even when no data of this unrealized reality is currently available. Reinforcement learning provides methods to learn a policy that optimizes a specific measure (e.g., reward, regret) when the agent is deployed in an environment and pursues an exploratory, trial-and-error approach. These two disciplines have evolved independently and with virtually no interaction between them. We note that they operate over different aspects of the same building block, counterfactual relations, which makes them umbilically connected. Based on these observations, novel learning opportunities arise when this connection is explicitly acknowledged and mathematized. To realize this potential, we note that any environment where the RL agent is deployed can be decomposed as a collection of autonomous mechanisms with different causal invariances, parsimoniously modeled as a structural causal model; any standard RL setting implicitly encodes such a model. This formalization allows us to put under a unifying treatment different modes of learning, including online, off-policy, and causal calculus learning, which appear unrelated in the literature. However, these modalities are not exhaustive: we introduce several natural and pervasive classes of learning settings that entail novel dimensions of analysis. Specifically, we introduce and discuss through causal lenses generalized policy learning, where to intervene, imitation learning, and counterfactual learning. These tasks lead to a broader view of counterfactual learning and suggest great potential for studying causal inference and reinforcement learning side by side, which we call causal reinforcement learning (CRL).

---


### 87. [Dual-Branch Cross-Projection Debiasing through Diffusion-based Disentanglement](https://arxiv.org/abs/2606.24161)

**<font color=#1a73e8>作者：</font>** Xiangqian Zhao, Xinyang Jiang, Zhipeng Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation models trained on biased datasets often rely on spurious correlations between target labels and non-causal attributes, resulting in poor generalization on minority groups. Bias mitigation remains challenging due to two fundamental issues. First, when group labels are unavailable, existing group-unsupervised methods typically infer spurious attributes implicitly from model behavior, making it difficult to identify spurious factors that are semantically aligned with real-world biases. Second, even with pseudo spurious supervision, most existing debiasing methods follow a single-branch design that operates within a single shared feature space, where target and spurious attributes are intrinsically entangled. To address the first challenge, we introduce Confidence-guided Bias Concept Mining (CBCM), which leverages diffusion-disentangled, semantically grounded concept representations to identify reliable spurious attributes without attribute annotations. To address the second challenge, we propose Dual-branch Cross-projection Debiasing (DCD), a prompt-tuning framework that separates target and spurious representations into two branches and explicitly removes spurious information through cross null-space projection while preserving target-relevant semantics. Extensive experiments on four benchmark datasets show that our method achieves state-of-the-art worst group accuracy among group-unsupervised approaches, while tuning at most 0.22% of the model parameters. The source code is available in the supplementary materials.

---


### 88. [Data Scale, Not Latency, Shapes Cross-Lingual Encoder Transfer in Streaming ASR](https://arxiv.org/abs/2606.24169)

**<font color=#1a73e8>作者：</font>** Nenad Banfic  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Adapting a streaming speech recognition model to a new language requires choosing between two plausible warm starts: a multilingual (ML) encoder or an English-only (EN) encoder. The common intuition is that the multilingual encoder should help most at low data, but it is unclear how long that advantage persists, whether tight streaming latency amplifies it, and whether it survives deployment quantization. We answer these questions with a controlled sweep of a 0.6 B-parameter cache-aware FastConformer transducer across eight European languages, up to five target-language data scales (100 h to 2500 h), three streaming tiers plus offline decoding, and up to four public test sets. The main result is that multilingual initialization is a data-limited advantage, not a latency-limited one. On FLEURS at 160 ms, the mean EN-ML word error rate (WER) gap falls from +4.21 percentage points (pp) at 100 h to +0.20 pp at 2500 h; a power-law fit summarizes this decay, with each doubling of target-language data roughly halving the remaining advantage. Across the three streaming tiers, the across-language mean EN-ML gap is approximately stable at each scale from 100 to 1000 h, and is near zero by 2500 h. Finally, 4-bit weight-only encoder quantization at the matched 560 ms streaming tier reduces the encoder footprint by about 3x, with an average FLEURS WER increase of about 0.5 pp. The resulting guideline is simple: use multilingual initialization in low-data regimes, treat the choice as effectively irrelevant at large data, and make latency and quantization decisions independently.

---


### 89. [A Pāninian Foundation for Indic Language Processing](https://arxiv.org/abs/2606.24172)

**<font color=#1a73e8>作者：</font>** Ritwik Banerjee, Lav R. Varshney  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> More than a billion people communicate in Indic languages, yet the natural language processing infrastructure serving them remains fragmented and underdeveloped. The cause is structural: the field organizes its tools and benchmarks around individual languages or small subsets of genealogical language families, building separate analyzers, parsers, and datasets for each language and starting over for the next. This overlooks a deep regularity. Through more than two millennia of convergence around Sanskrit, Indic languages came to share a morphosyntactic architecture formalized in Pānini's grammar, the Astādhyāyī. This cuts across genealogical lines, uniting languages through a common framework. We argue that this Pāninian framework supplies a unifying computational architecture the field has lacked, and that benchmarks grounded explicitly in it would make Indic language systems more accurate, more data-efficient, and more transferable, effectively merging many apparently disparate and sparse Indic language resources into a single high-resource metalanguage bedrock. We propose a four-part benchmark suite to render this shared architecture explicit, measurable, and ready to be leveraged for practical applications. Moreover, we underscore the question it raises for interpretability research: whether neural models trained on these languages come to represent Pānini's categories on their own.

---


### 90. [Lightweight Transformer Models for On-Device Fault Detection: A Benchmark Study on Resource-Constrained Deployment](https://arxiv.org/abs/2606.24173)

**<font color=#1a73e8>作者：</font>** Disha Patel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-device fault detection enables real-time diagnostics without cloud dependency, but deploying machine learning models on resource-constrained hardware demands careful tradeoffs between accuracy, latency, and model size. We present a benchmark comparing traditional ML methods (Random Forest, XGBoost, SVM, Logistic Regression) against lightweight transformer architectures (DistilBERT, TinyBERT-6L, TinyBERT-4L, MobileBERT) for binary fault detection across three public datasets: NASA C-MAPSS turbofan degradation, SECOM semiconductor manufacturing, and UCI AI4I 2020 predictive maintenance. We evaluate classification performance (F1-score, AUC), model size, and CPU inference latency, and further assess INT8 dynamic quantization and a two-stage adaptive inference pipeline. Our results reveal that on well-separated sensor data (C-MAPSS), lightweight transformers match traditional ML at 87.8% F1 but at 100x the model size and 9000x the latency. TinyBERT-4L emerges as the most deployment-friendly transformer at 55 MB and 18 ms CPU latency. INT8 quantization reduces size by 25% while preserving 86.9% F1. Our adaptive pipeline, routing 97.9% of predictions through a quantized triage model and only 2.1% to a larger expert, achieves 87.6% F1 at 19.5 ms average latency. On severely imbalanced datasets (SECOM, UCI-PM), both traditional and transformer methods struggle significantly, highlighting fundamental limitations of current approaches for extreme class imbalance in fault detection. All code is publicly available.

---


### 91. [A Synthetic Reliability-Aware PINN Benchmark for Offshore Wind Turbine Support-Structure Monitoring with Bayesian Inverse Identification](https://arxiv.org/abs/2606.24176)

**<font color=#1a73e8>作者：</font>** Puneet Kant, Monika Tanwar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reliable structural health monitoring (SHM) of offshore wind turbine (OWT) support structures requires fast state estimation from sparse measurements. Repeated high fidelity finite element or aeroelastic analyses are difficult to use directly in online monitoring loops, while purely data-driven surrogates can require large training sets. This paper presents Digi Turbine, a synthetic reliability-aware Physics Informed Neural Network (PINN) benchmark for OWT monopile support structure monitoring. The workflow embeds a simplified Euler Bernoulli beam equation with Winkler soil foundation in the training objective, couples it with Bayesian-prior-informed inverse identification, and adds First Order Reliability Method (FORM) screening. All validation uses synthetic configurations with analytical or finite-difference ground truth motivated by the NREL 5MW reference turbine context.

---


### 92. [Zero-Shot Test-Time Canonicalization using Out-of-Distribution Scoring](https://arxiv.org/abs/2606.24178)

**<font color=#1a73e8>作者：</font>** Dominik Lindner, Johann Schmidt, Tom Siegl 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained vision models often misclassify inputs that are rotated, scaled, or sheared, even though these affine transformations leave the object class unchanged. Robustness is usually restored either by building equivariance into the architecture or by retraining with augmentation, both of which require changing or retraining the model. Test-time canonicalization instead leaves the classifier untouched. It undoes the transformation of each input, mapping it to a canonical form near the training distribution before classification. Existing canonicalizers, however, rely on a narrow set of logit-based energy scores and bespoke search procedures, leaving the design space of scoring functions and optimizers unexplored. We reframe canonicalization as out-of-distribution (OOD) detection, which lets any OOD score serve as the energy minimized over transformations. Across benchmarks ranging from handwritten characters and sketches to natural images and 3D point clouds, we systematically evaluate around twenty OOD scores and nine search algorithms, finding that distance-based scores paired with random search and local refinement perform best overall. Because canonicalizing an already-aligned input can hurt accuracy, we add a gated mechanism that transforms an input only when its OOD score indicates this is needed, preserving most in-distribution accuracy while retaining the robustness gains on transformed inputs. Code is available at this http URL.

---


### 93. [Deep Learning Approaches for 3D Medical Scene Completion: From Geometric Modeling to Generative Paradigms](https://arxiv.org/abs/2606.24180)

**<font color=#1a73e8>作者：</font>** Afifa Khaled, Said Jadid Abdulkadir, Majdy Mohamed Eltayeb Eltahir  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Three-dimensional scene completion has evolved as a major problem in computer vision and robotics, and its applications are diverse, including autonomous navigation and augmented reality. In this study, a systematic review has been conducted to compile the research contributions made in the last ten years, i.e., 2016 to 2026, which has revolutionized the field from the voxel semantic completion paradigm represented by SSCNet to the latest paradigm that combines generative diffusion priors with real-time rendering using a Gaussian splatting technique. The evolution in representation paradigms, such as voxel grids, point learning, implicit neural fields, transformer networks, diffusion networks, and the latest paradigm based on rendering-aware 3D Gaussian primitives, has been discussed in this study. A comprehensive analysis has been carried out on the contributions made in the last ten years, and a taxonomy has been developed to provide a clear idea about the contributions made in the field. The study has also discussed the research contributions made in the field, along with the challenges that still need to be addressed. Finally, the study has presented a research agenda that will provide a clear idea about the directions that can be followed in the development of the next-generation system

---


### 94. [Project Ariadne: Prompt-Conditioned Route Generation for Synthesis Planning](https://arxiv.org/abs/2606.24184)

**<font color=#1a73e8>作者：</font>** Anton Morgunov, Victor S. Batista  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Retrosynthetic planning seeks to connect a target molecule to commercially available starting materials through a multistep route. Classical planners construct such routes by iteratively applying single-step reaction models within a search procedure; constrained variants often require specialized algorithms or architectural changes. Direct route generation reframes retrosynthesis as sequence generation, but existing direct-generation methods still train separate models for different planning specifications. We introduce Ariadne, a decoder-only route generator that represents the target, optional constraints, and route in one prompt-completion sequence. On the RetroCast/PaRoutes mkt-cnv-160 benchmark family, one 24-layer checkpoint follows route-depth and required-starting-material prompts: adding the corresponding prompt fields raises Solv-0 by 13.7 points for depth constraints and 31.2 points for required-leaf constraints. Ariadne also improves over DESP, a bidirectional search planner, on required-leaf Top-10 and Solv-0 in 24 GPU-minutes versus 6.8 GPU-hours. On standard reconstruction, Ariadne is comparable to DMS Explorer XL at about half the reported inference time. Across additional target-only benchmarks, Ariadne's clearest gains are on route-holdout reconstruction, whereas AiZynthFinder MCTS remains stronger on several Solv-0 comparisons. These results extend sequence generation from specialist retrosynthesis models to prompt-conditioned structural route generation. We release the codebase and training scripts to support further work, but do not introduce Tier-1--3 route checkers; those remain the main bottleneck before models of this kind can become useful to experimental chemists.

---


### 95. [Aspect-Based Sentiment Evolution and its Correlation with Review Rounds in Multi-Round Peer Reviews: A Deep Learning Approach](https://arxiv.org/abs/2606.24188)

**<font color=#1a73e8>作者：</font>** Ruxue Hana, Haomin Zhoua, Jiangtao Zhong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mining sentiment information from the textual content of peer review comments offers valuable insights into the scientific evaluation process. However, previous studies are often constrained by coarse-grained analysis and the lack of differentiation across review rounds. Notably, the dynamic shifts in reviewers' focus and sentiment tendencies throughout multiple review stages remain underexplored. To address this gap, the present study investigates the distribution and evolution of aspect-level sentiments and examines their correlation with the number of review rounds. We begin by segmenting the multi-round review comments of 11,063 accepted papers from Nature Communications and identifying fine-grained review aspect clusters. A manually annotated corpus of approximately 5,000 review sentences is then constructed. Using this dataset, we train a series of deep learning-based aspect sentiment classification models. Among them, the LCF-BERT-CDM model achieves the best performance, with a Macro-F1 score of 82.65%. Subsequent statistical analysis reveals a consistent trend: as the number of review rounds increases, the proportion of positive sentiments rises, while negative sentiments decline. Correlation analysis further indicates that aspect sentiment scores are negatively associated with the total number of review rounds. Key aspects exhibiting stronger correlations include "experiments", "research significance" and "result analysis".

---


### 96. [Co-occurring associated retained concepts in Diffusion Unlearning](https://arxiv.org/abs/2606.24192)

**<font color=#1a73e8>作者：</font>** Miso Kim, Georu Lee, Yunji Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unlearning has emerged as a key technique to mitigate harmful content generation in diffusion models. However, existing methods often remove not only the target concept, but also benign co-occurring concepts. As illustrated in Fig.1, unlearning nudity can unintentionally suppress the concept of person, preventing a model from generating images with person. We define these undesirably suppressed co-occurring concepts that must be preserved CARE (Co-occurring Associated REtained concepts). Then, we introduce the CARE score, a general metric that directly quantifies their preservation across unlearning tasks. With this foundation, we propose ReCARE (Robust erasure for CARE), a framework that explicitly safeguards CARE while erasing only the target concept. ReCARE automatically constructs the CARE-set, a curated vocabulary of benign co-occurring tokens extracted from target images, and leverages this vocabulary during training for stable unlearning. Extensive experiments across various target concepts (Nudity, Van Gogh style, and Tench object) demonstrate that ReCARE achieves overall state-of-the-art performance in balancing robust concept erasure, overall utility, and CARE preservation.

---


### 97. [A Dynamic Coupling Theory of Expertise Through Thinking Flow and Workflow Evolution](https://arxiv.org/abs/2606.24197)

**<font color=#1a73e8>作者：</font>** Annie Yuan  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Expertise has long been explained through tacit knowledge, deliberate practice, skill acquisition, and expert performance. While these perspectives have advanced understanding of expertise, they often describe its conditions or outcomes rather than the cognitive architecture through which expertise continuously emerges and evolves. This paper proposes Workflow Cognition as a theoretical framework for explaining expertise as a dynamic cognitive phenomenon. Workflow Cognition is defined as the cognitive architecture emerging from the recursive coupling of Thinking Flow and Workflow Evolution. Thinking Flow refers to ongoing processes of perception, interpretation, judgement, decision-making, and reflection; Workflow Evolution refers to the continuous adaptation of actions, task structures, and operational strategies within situated practice. Through their coupling, expertise is not treated as a static accumulation of knowledge or skill, but as an evolving process generated through cognition-in-practice.
Building on this framework, the paper advances a new ontological definition of expertise: expertise is an emergent manifestation of Workflow Cognition operating across longitudinal professional experience. Knowledge, skills, decisions, aesthetic preferences, and behavioural patterns are therefore interpreted as observable expressions of expertise rather than expertise itself. Drawing on illustrative comparisons across craft, creative production, education, and leadership, the paper introduces a Dynamic Coupling Model of Expertise and establishes a foundation for future work on Longitudinal Tacit Cognition, Longitudinal Aesthetic Cognition, and Expertise Workflow Grammar. The framework contributes a cognitive ontology of expertise and supports future computational representations of human expertise within AI+Expert systems.

---


### 98. [MMed-Bench-IR: A Heterogeneous Benchmark for Multilingual Medical Information Retrieval](https://arxiv.org/abs/2606.24200)

**<font color=#1a73e8>作者：</font>** Junhyeok Lee, Han Jang, Hyeonjin Goh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) in clinical settings increasingly requires multilingual retrieval against predominantly English evidence corpora. Multilingual medical retrieval demands three capabilities: cross-lingual alignment, concept discrimination, and evidence retrieval. However, existing benchmarks evaluate these only in isolation, leaving the interaction between biomedical expertise and multilingual coverage unmeasured. We introduce MMed-Bench-IR, a benchmark designed to disentangle these axes across 6 languages and three structurally heterogeneous tasks: (1) cross-lingual medical QA retrieval with 6,127 queries grounded in the Unified Medical Language System (UMLS), (2) concept discrimination over 4,975 confusion sets at three difficulty tiers, and (3) multilingual evidence retrieval for RAG with 2,040 quality-assured queries. The three tasks share zero concept and query overlap by design, ensuring that aggregate scores reflect genuine capability breadth. Evaluation of ten systems across six paradigm families reveals severe cross-lingual failure: biomedical encoders that score 0.818 nDCG@10 in English drop to 0.056 in Japanese, a gap that English-only benchmarks cannot detect.

---


### 99. [Inclusive Interactive Collisions for Multi-View Consistent Compositional 3D Generation](https://arxiv.org/abs/2606.24206)

**<font color=#1a73e8>作者：</font>** Chang Liu, Mingwen Shao, Xiang Lv 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent breakthroughs in 3D generation have advanced notably with the development of text-to-image diffusion model. However, existing methods remain two practical challenges: (1) They primarily generate single 3D object, but struggle to generate multi-object compositional 3D assets due to the lack of the modeling for Gaussian primitives in reasonable interactions. (2) They often suffer from cross-view inconsistency during 3D optimization, as Score Distillation Sampling inherently performs on each single view, inevitably resulting in cross-view hallucinations. To solve above issues, we propose I2C-3D, a novel optimization-based method to generate multi-view consistent compositional 3D assets with reasonable interactions. Specifically, we propose an Inclusive Interactive Collisions strategy to guide Gaussian primitives appearing in reasonable interaction regions naturally, thereby ensuring objects in the compositional scene interact in a physically plausible and visually coherent way. Additionally, to enhance multi-view consistency, Multi-View Adaptive Score Distillation Sampling is devised to distill multi-view consistency prior and layout prior from pre-trained diffusion model by modulating attention map of instance token and spatial token across viewpoints. Benefiting from above elaborate designs, I2C-3D not only generates high-fidelity multi-view consistent compositional 3D assets but also supports 3D editing flexibly, facilitating complex scene generation. Extensive experiments demonstrate our I2C-3D outperforms existing methods in generation quality and multi-view consistency.

---


### 100. [MorVess: Morphology-Aware Pulmonary Vessel Segmentation Network](https://arxiv.org/abs/2606.24214)

**<font color=#1a73e8>作者：</font>** Fuyou Mao, Yifei Chen, Beining Wu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate pulmonary vessel segmentation remains challenging due to the sparse, tortuous, and multi-scale nature of vascular structures, where small branches are easily lost and topology integrity is difficult to preserve under voxel-wise supervision. Existing deep segmentation models primarily optimize binary masks, lacking explicit geometric constraints, thus struggling to recover continuous tubular morphology and fine vascular connectivity. In this study, we introduce MorVess, a morphology-aware segmentation framework that integrates differentiable geometric priors with large-scale foundation model adaptation to achieve fine-grained vascular parsing. MorVess jointly predicts vessel masks, distance maps, and thickness maps, providing explicit supervision for vascular boundaries, centerline consistency, and smooth diameter transitions. A lightweight 2.5D adapter bridges 3D spatial context and 2D SAM representations, while a global-local fusion block aggregates multi-level semantics and geometric cues for high-fidelity topology reconstruction. Across two challenging pulmonary CT benchmarks, MorVess delivers superior Dice, clDice, and HD95 scores, substantially improving small-vessel recovery and global connectivity. These results demonstrate that embedding geometric intelligence into pretrained vision models offers a principled and scalable pathway toward precise vessel analysis and clinically reliable structural quantification. Our source code is available at this https URL.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-219](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
