# 📦 其他研究 | 2026年08月24日

> 本类共 **155** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-155](./part-04.md)

---

### 101. [Flow Matching Meets 3D Curvilinear Structure Segmentation in Medical Imaging](https://arxiv.org/abs/2608.19965)

**<font color=#1a73e8>作者：</font>** Sidi Mohamed Sid'El Moctar, Nicolas Vitry, Hélène Bouvrais  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Segmentation of curvilinear anatomical structures in 3D medical images remains challenging due to complex topology, severe class imbalance, weak contrast, and large variations in structure morphology. While deep learning approaches for 3D curvilinear segmentation have been proposed, they are often tailored to specific anatomies or modalities, limiting generalization across clinical settings and leaving room for improvement. Recent generative models have shown the benefits of iterative prediction for structured segmentation tasks, yet diffusion-based methods suffer from computationally expensive sampling, hindering their use on high-resolution 3D volumes. We present 3D-CurvSegFlow, a flow matching-based model for 3D curvilinear structure segmentation. The model learns a continuous transformation from a simple source distribution to the target vascular representation, enabling progressive refinement of complex curvilinear geometries with efficient inference. We evaluate our method on Three public challenging datasets covering distinct anatomies and modalities: portal vein, cerebral vessel, and coronary arteries. Using a common architecture and training strategy across all tasks, our method outperforms general-purpose and vessel-specific approaches, with strong preservation of thin branches and vascular continuity. This work not only advances the state-of-the-art in 3D curvilinear segmentation but also opens new avenues for efficient, generalizable, and clinically applicable methods in medical image analysis.

---


### 102. [Rethinking Patch Based Multivariate Time Series Forecasting with Semantic Structured Partitioning](https://arxiv.org/abs/2608.19966)

**<font color=#1a73e8>作者：</font>** Jiazhe Wang, Zhiquan Huang, Linjing Xue 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multivariate time series forecasting (MTSF) is a fundamental task in many real world applications. Existing patch based forecasting methods generally fall into three categories: fixed partitioning, multi-scale partitioning, and extendable partitioning. Fixed partitioning often breaks meaningful temporal boundaries, multi-scale partitioning may introduce redundant representations across scales, and extendable partitioning improves flexibility but still lacks an explicit mechanism for organizing semantic structure and modeling interactions among heterogeneous temporal patterns. To address these limitations, we propose SCPaT, a Transformer based framework built on semantic structured partitioning. SCPaT first decomposes input sequences into semantically consistent units through adaptive semantic unit generation, then constructs a dynamic semantic graph to model directed dependencies among these units and organize them into higher order semantic blocks. Based on these structured representations, an importance aware routing mechanism adaptively dispatches different semantic blocks to different experts for customized modeling. Extensive experiments on 12 real world datasets demonstrate the effectiveness of SCPaT.

---


### 103. [Robust Incomplete Multimodal Sentiment Analysis via Iterative Proxy Correction](https://arxiv.org/abs/2608.19971)

**<font color=#1a73e8>作者：</font>** Zhifa Geng, Subin Huang, Hao Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal sentiment analysis aims to infer affective states by integrating language, visual, and acoustic cues. However, real-world multimodal inputs are often incomplete or corrupted, which can weaken cross-modal complementarity and introduce misleading information into downstream fusion. Existing proxy-based methods for incomplete MSA commonly rely on one-shot proxy construction to compensate for degraded language information, but the generated proxy may be coarse or unreliable at initialization. Prematurely injecting such a proxy into multimodal reasoning can propagate initial errors and compromise sentiment prediction. To address this limitation, we propose an iterative proxy correction framework for robust incomplete MSA. Our method constructs a language-oriented proxy from non-language modalities and progressively refines it under multimodal context through gated residual correction. The corrected proxy is then adaptively fused with the observed language representation according to an estimated language reliability score, allowing the model to balance proxy-based compensation and trustworthy linguistic evidence. In addition, we introduce a stage-wise latent correction objective that uses the complete language representation as a training-time semantic anchor to stabilize the proxy refinement trajectory. Extensive experiments on MOSI, MOSEI, and SIMS under diverse missing-modality settings demonstrate that the proposed framework consistently outperforms competitive baselines and achieves robust sentiment prediction under incomplete inputs.

---


### 104. [STEP: Score-Based Temporal Energy for Human Pose Video Anomaly Detection](https://arxiv.org/abs/2608.19987)

**<font color=#1a73e8>作者：</font>** Jakub Micorek, Mateusz Koziński, Horst Possegger  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Skeleton-based Video Anomaly Detection (VAD) offers a robust, privacy-preserving solution for identifying abnormal behaviors. To model the distribution of normal static and moving poses, recent methods train Energy-Based Models (EBMs) via Denoising Score Matching (DSM). However, directly injecting noise, required for training, into raw joint coordinates creates physically impossible poses, and this structural collapse severely worsens as the temporal window expands. To address this, we introduce STEP, a simple framework that utilizes Principal Component Analysis (PCA) to project pose sequences into a compact, whitened PC-space. Learning the data density within this well-behaved PC-space ensures that the injected noise translates into physically plausible variations, which allows the model to process longer video sequences without the performance collapse of raw coordinate baselines. Additionally, to mitigate inherent pose estimation inaccuracies arising from occlusions or motion blur, we integrate a sequence-level weighting mechanism based on the estimator's confidence scores. Operating at real-time computational efficiency, our simple and lightweight framework outperforms the previous skeleton-based state-of-the-art by 12.2% (90.1% AUROC) on the challenging UBnormal dataset and achieves highly competitive results by improving on the ShanghaiTech benchmark.

---


### 105. [Green BOA: Determining the environmental break-even point for ML-based data compression](https://arxiv.org/abs/2608.19994)

**<font color=#1a73e8>作者：</font>** Caterina Doglioni, Akshat Gupta, Thomas Elliott 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We summarise the outcome of two summer internship projects based at the University of Manchester, focused on the break-even point in terms of environmental sustainability for ML-based data compression algorithms. Using the example of a ML-based lossless compression algorithm, we compare estimates for the carbon-equivalent of the infrastructure needed for ML training and inference with the carbon-equivalent savings from reduced disk storage requirements, and discuss their break-even point.

---


### 106. [Point-Based 3D Reconstruction from Sparse Views under Known Illumination](https://arxiv.org/abs/2608.20000)

**<font color=#1a73e8>作者：</font>** Magnus Kaufmann Gjerde, Joakim Bruslund Haurum, Jeppe Revall Frisvad 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse view 3D reconstruction is commonly addressed with neural implicit surfaces or dense point-based representations such as Gaussian splatting. Surface-aware splatting methods improve extracted geometry through oriented primitives and regularization, while RadiosityGS incorporates differentiable light transport through a radiosity inspired finite-element surfel formulation. We propose a differentiable point rendering method based on opacity-bearing beta surfels. An opacity explicit adjoint light transport formulation provides gradients for surfel geometry and appearance parameters, allowing physically based light transport to constrain reconstruction.
Across five synthetic objects reconstructed from ten posed views, our method achieves the lowest mean symmetric Chamfer distance among the evaluated baselines and reduces mean Chamfer distance by 28.5% relative to the strongest point-based baseline while using only 267 surfels on average, approximately ~161 fewer primitives. Directional Chamfer results further show improved accuracy and competitive completion relative to related point-based methods. These results show that, in the controlled direct illumination setting, compact beta surfels combined with transport-based optimization can recover surfaces without relying on the tens to hundreds of thousands of primitives used by the evaluated baselines.

---


### 107. [ExPhy: A Benchmark for Explicit Physical Property Learning in Multi-Object Trajectory Forecasting](https://arxiv.org/abs/2608.20009)

**<font color=#1a73e8>作者：</font>** Rui Wang, Yeteng Wu, Xianlin Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Understanding object dynamics requires not only predicting future trajectories but also examining whether a model captures the physical properties that govern motion. However, existing benchmarks rarely expose object-level physical properties as explicit evaluation targets alongside trajectory forecasting. To address this gap, we introduce \emph{ExPhy}, a multi-object trajectory forecasting benchmark containing 24,000 simulated physical scenes with explicit object-level labels for mass, friction, and restitution. ExPhy provides observed and future trajectories together with an in-distribution (ID) split and two out-of-distribution (OOD) splits over physical parameters (OOD-Parameter) and initial states (OOD-Initial) for jointly evaluating trajectory forecasting and physical property estimation. We further instantiate \textsc{PhyODE}, a physics-guided model with an explicit property interface that estimates physical properties from observed trajectories and uses them for differentiable future rollout. On the long-horizon OOD-Initial setting, \textsc{PhyODE} reduces ADE and FDE by 33.1\% and 31.0\%, respectively, compared with the strongest baseline. Zero-shot evaluation on ComPhy further assesses cross-benchmark transfer. Property-level analyses reveal that accurate trajectory forecasting does not necessarily imply accurate recovery of the underlying physical properties. Code and data are available at this https URL.

---


### 108. [Manifold Drift in Flow Preference Optimization: A Root Cause of Reward Hacking](https://arxiv.org/abs/2608.20011)

**<font color=#1a73e8>作者：</font>** Yansen Han, Shengyi Liao, Yuanxing Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Preference optimization is a standard alignment method for generative models, yet extending it to continuous-time dynamics remains non-trivial. In flow matching, reward-driven updates modify transport trajectories without an inherent constraint to the pretrained data manifold and can move terminal samples off the pretrained support. We formalize this failure mode as manifold drift. Theoretically, we show that optimal flow matching recovers the terminal data distribution, whereas a preference update leaves the pretrained manifold whenever its induced terminal displacement has a nonzero normal component. As a remedy, we propose ThermoDPO, a temperature-controlled objective that anchors pairwise preference optimization on preferred samples. Across temperature regimes, this objective connects rejection sampling fine-tuning and FlowDPO and controls a pointwise reconstruction-based surrogate for manifold distance. To counteract diminished signals at low temperatures, we further introduce a weighted variant, ThermoDPO-weighted. On the main toy benchmark, ThermoDPO-weighted attains a StrictScore of 0.899, compared with 0.629 for FlowDPO and 0.857 for FlowDPO+RFT. On SD3.5-M at CFG = 4.5, it improves OCR by 47.5% and the average of four metrics by 16.0%.

---


### 109. [Contrastive Mixed Prompt Learning for Incomplete Multimodal Sentiment Analysis with Unseen Modality Combination](https://arxiv.org/abs/2608.20019)

**<font color=#1a73e8>作者：</font>** Kaixin Xu, NaiJin Liu, Yulin Kang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Incomplete multimodal sentiment analysis has garnered significant attention in recent years. Existing approaches typically assume that data is missing at random or are designed specifically for certain missing patterns, ignoring the modality combination inconsistency between training and testing phases. However, in real-world scenarios, the testing phase often encounters modal combinations that were not present during the training phase, which leads to insufficient generalization capabilities and unstable performance. In this paper, we introduce the problem of Incomplete Multimodal Sentiment Analysis with Unseen Modality Combinations (IMSAUMC), aiming to enhance model generalization for unseen modality combinations. To address this challenge, we propose the model named $\textbf{C}$ontrastive $\textbf{M}$ixed $\textbf{P}$rompt $\textbf{L}$earning ($\textsf{CMPL}$) for IMSAUMC. It introduces a label-guided contrastive feature learning mechanism to learn robust and discriminative cross-modal representations. Additionally, we design modality-combination prompts with a soft router to facilitate better learning of various modality combinations. Furthermore, we introduce three prompt contrastive learning strategies, which enable effective learning of prompts corresponding to unseen modality combinations, thereby significantly strengthening the model's generalization capabilities in diverse testing scenarios. Extensive experiments on three widely used datasets demonstrate that $\textsf{CMPL}$ achieves more than a 5% improvement in accuracy compared to state-of-the-art approaches.

---


### 110. [Systematic Evaluation of TabPFN-TS for Zero-Shot Probabilistic Heat Load Forecasting in District Heating Networks](https://arxiv.org/abs/2608.20024)

**<font color=#1a73e8>作者：</font>** Ben Spoek, Karim K. Ben Hicham, Kai Derzsi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> District heating energy hubs require reliable heat load forecasts for efficient operational scheduling. Conventional forecasting workflows train system-specific models on historical data, which can become burdensome when networks change through new consumers, retrofits, or changing operating regimes. Zero-shot time-series foundation models and in-context forecasting offer a promising alternative: they can adapt at inference time from recent observations rather than by repeated retraining. This study systematically evaluates TabPFN-TS against time-series foundation models and trained machine-learning baselines for probabilistic heat load forecasting in district heating networks. Unlike foundation models pretrained on large collections of real time series, TabPFN-TS relies on synthetic pretraining data, which avoids direct pretraining-test overlap but raises the question of whether the learned prior captures district heating dynamics. We analyze covariate choice, context length, temporal resolution, and prediction horizon on representative operating weeks, validate the selected configuration over a full year, and test transferability on a second network. The results identify hourly 24-hour forecasting with a 12-week rolling context and ambient temperature as a parsimonious high-performing configuration; longer context windows do not improve accuracy. TabPFN-TS remains close to Chronos-2 in deterministic accuracy, reaching CVRMSE values of 13.06% versus 12.48% on the main dataset, and lies within the critical-difference threshold in the daily-rank comparison. Although Chronos-2 achieves the lowest aggregate full-year error, TabPFN-TS shows better empirical calibration. Finally, the diagnostic findings motivate a Multi-Resolution Residual-Correction Forecaster that combines a low-frequency Base Forecaster with a short-horizon Residual Forecaster to improve longer-horizon planning accuracy.

---


### 111. [CLaST: Context-aware Contrastive VAE for Probabilistic Time Series Forecasting](https://arxiv.org/abs/2608.20025)

**<font color=#1a73e8>作者：</font>** Alexander Marusov, Dmitry Anikin, Petr Sokerin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Probabilistic forecasting models are widely used for time series forecasting in domains such as energy systems, finance, medicine, and transportation. In recent years, deep generative models have shown strong results on probabilistic forecasting, yet many conventional approaches struggle to capture internal temporal dependencies, leading to latent representations with limited expressive power. To address this limitation, we propose \textit{CLaST}, a VAE framework for probabilistic multivariate time series forecasting. Unlike existing generative models, CLaST learns embeddings that preserve contextual similarity between observations through our contrastive loss function. Experiments across nine widely adopted benchmarks demonstrate that CLaST consistently surpasses strong baseline methods. In short-term forecasting tasks, our approach achieves improvements of up to $16.4\%$ in CRPS and $14.4\%$ in NMAE over the second-best method. Furthermore, in long-term prediction CLaST attains superior overall performance, exceeding the second-best method by up to $48.6\%$ and $25.1\%$ in CRPS and NMAE, respectively.

---


### 112. [An Inclusive and Lightweight Approach to Federated Continual Learning for Cultural Heritage](https://arxiv.org/abs/2608.20038)

**<font color=#1a73e8>作者：</font>** Ioannis Theologitis, Debin Meng, Stylianos Eleftheriadis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence can support cultural heritage and digital humanities through large-scale retrieval and analysis of digitized collections. However, cultural heritage data are often distributed across institutions, constrained by ownership and access restrictions, and continuously evolving over time. Federated Continual Learning (FCL) is well suited to this setting, as it enables models to learn from distributed and sequential data without sharing raw collections. In this paper, we propose FedCurv-DR, a lightweight, regularisation-based FCL strategy. The method accumulates parameter-importance estimates across clients and experiences to protect learned knowledge, while updating them only at fixed intervals to minimize communication and computation overhead. We evaluate FedCurv-DR in a continual learning scenario using the WikiArt image dataset for genre classification with evolving styles, reporting performance, energy, and fairness metrics. Our results show that FedCurv- DR reduces forgetting and balances performance, fairness, and energy efficiency for sustainable AI in cultural heritage.

---


### 113. [A three-dimensional typology of agency for advanced AI systems](https://arxiv.org/abs/2608.20041)

**<font color=#1a73e8>作者：</font>** Willem Fourie  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Research on the agency of advanced artificial intelligence (AI) systems focuses on agency as a normative concept and on the agency of particularly agentic AI systems. While recent work also focuses on the different profiles of agentic systems, no framework exists to address the question of the type of agency instantiated by advanced AI systems, particularly when considering non-moral forms of agency. Based on established theoretical positions in philosophy, ethics, legal theory and sociology, we develop a typology of agency for frontier AI systems consisting of three dimensions: the nature of agency (moral or legal), its mode (individual or collective) and its locus (human or non-human). Combining these dimensions produces eight possible instantiations of agency, which we classify as conventional, contested or controversial. The typology separates legal from moral agency and thereby creates conceptual space for considering individual, legal, non-human agency without presupposing that advanced AI systems are moral agents. We argue that this distinction is increasingly relevant where instrumental goal pursuit complicates the attribution of AI actions to particular human actors.

---


### 114. [End-to-end Early Classification of Time Series in Non-Stationary Environments](https://arxiv.org/abs/2608.20044)

**<font color=#1a73e8>作者：</font>** Aurélien Renault, Alexis Bondu, Antoine Cornuéjols 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Early Classification of Time Series (ECTS) requires making accurate decisions as early as possible in inherently online and evolving environments. Yet, most existing methods assume stationarity and rely on separable designs, where classification and triggering are optimized independently, an assumption that fundamentally limits their adaptability under drift. In this work, we challenge this paradigm and study ECTS under non-stationary conditions. We provide the first systematic comparison between separable and end-to-end approaches across controlled drifting scenarios. Building on Reinforcement Learning, we introduce DQeND, a unified architecture that jointly learns representation, classification, and triggering decisions, while remaining directly comparable to state-of-the-art separable baselines. Across a wide range of drifts, DQeND demonstrates strong robustness across various non-stationary scenarios, consistently outperforming separable baselines. An ablation study further highlights that jointly updating representation and decision modules is critical to these gains. Overall, our results indicate that end-to-end learning can offer improved adaptation capabilities for ECTS in dynamic environments, and motivate further investigation of alternatives to separable designs.

---


### 115. [DecoVAE: a Lightweight Interpretable Trend-Seasonal VAE Framework for Efficient Probabilistic Time Series Forecasting](https://arxiv.org/abs/2608.20052)

**<font color=#1a73e8>作者：</font>** Alexander Marusov, Dmitry Anikin, Alexey Zaytsev  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Probabilistic time series forecasting remains challenging, largely because modeling distinct trend and seasonal dynamics requires specialized approaches. Existing methods often fail to capture the unique inner properties of these components, lack interpretability, or suffer from heavy memory and runtime overhead. To address these limitations, we propose DecoVAE, a lightweight interpretable trend-seasonal VAE framework that explicitly decomposes time series into trend and seasonal components by applying domain-specific inductive biases. The trend stream enforces structural smoothness using a differential regularizer on the latent trajectory, analogous to the Hodrick-Prescott filter. Concurrently, the seasonal stream operates in the frequency domain via a complex Gaussian VAE, natively capturing the amplitude and phase of periodic patterns. Extensive evaluations across seven real-world benchmarks show that DecoVAE consistently outperforms strong baselines. It achieves reductions of up to 14.96\% in CRPS and 23.30\% in NMAE for short-term forecasting, and up to 52.68\% and 26.51\% for long-term horizons. Crucially, DecoVAE yields these accuracy gains while remaining highly efficient, reducing model weight by up to 93\% and accelerating speed by up to 74\% compared to the second-best method.

---


### 116. [On the Applicability of Safety Nets: A Safety-By-Design Solution for Certifying Neural Networks](https://arxiv.org/abs/2608.20053)

**<font color=#1a73e8>作者：</font>** Johann Maximilian Christensen, Thomas Stefani, Elena Hoemann 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The integration of Artificial Intelligence (AI) in safety-critical aviation systems presents significant challenges for certification and deployment. Aviation, often regarded as the safest form of transportation, relies on numerous safety-critical systems. For future safety-critical AI-based systems, EASA requires a Safety-by-Design approach, which can be achieved by using Safety Nets that combine neural network compression with lookup tables to ensure 100 % correct runtime behavior across the discretized operational design domain. Although Safety Nets have been studied, no comprehensive study of their performance characteristics and system design trade-offs has been conducted. This work presents the first systematic analysis of the trade-off between neural network and lookup table size in Safety Nets. By systematically comparing neural networks with diverse architectures, this study identifies optimal design parameters that minimize overall storage and memory requirements while maintaining certification compliance. Results demonstrate that architectures with 3 to 5 hidden layers, each with approximately 50 to 100 nodes, combined with one-hot encoding, achieve the best balance. In these configurations, neural networks accurately represent at least 97 % of the data, while compact lookup tables handle the remaining errors. The resulting Safety Nets reduce the system size by almost three orders of magnitude, fitting within the memory budget of current avionics hardware while guaranteeing 100 % correct outputs across the entire discretized input space, as required by EASA guidelines. This work provides the first-ever open-source implementation of Safety Nets for HCAS and VCAS with replicable results, demonstrating a practical pathway toward certifiable AI-based systems in aviation and establishing Safety Nets as a viable Safety-by-Design solution for safety-critical applications.

---


### 117. [Gravity-aware partially calibrated absolute pose estimation from affine- or rotation-covariant features](https://arxiv.org/abs/2608.20056)

**<font color=#1a73e8>作者：</font>** Marcus Valtonen Örnhag, Alberto Jaenal, Stefan Adalbjörnsson  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Inertial measurement units (IMUs) are now standard in most consumer devices, such as smartphones, drones, and extended reality (XR) headsets. By fusing visual and inertial data, localization systems gain significantly in speed and robustness compared to vision-only or IMU-only approaches. However, traditional pose estimation methods fail to utilize the local geometric information embedded in feature descriptors like SIFT. Recent work has proved the advantages of leveraging this information for relative and absolute pose estimation, but its application to partially calibrated absolute pose estimation remains unexplored. In this paper, we derive novel constraints for joint estimation of absolute pose and focal length, making use of a gravity vector obtained from IMU data and the feature-induced local geometry, which we use to construct two efficient solvers: UP1PfAC, that operates given a single affine correspondence and UP2PfORI, which requires two orientation-covariant features. Unlike traditional, semi-calibrated absolute pose methods requiring four point correspondences, our solvers benefit from fewer samples and lower computational cost, simplifying robust estimation in modern RANSAC-like frameworks. We evaluate the proposed solvers against the state-of-the-art on large-scale public datasets and demonstrate that our method achieves fast and accurate localization and focal length estimation.

---


### 118. [Orthogonal JEPA: Factorized Predictive States for Latent World Models](https://arxiv.org/abs/2608.20065)

**<font color=#1a73e8>作者：</font>** Taoyong Cui, Pheng Ann Heng, Wanli Ouyang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models construct latent states that support prediction, planning, and reasoning about an underlying system. Joint-embedding predictive architectures (JEPAs) offer a direct way to learn such states by predicting targets in representation space instead of reconstructing every detail of the observation. Standard JEPAs, however, organize all predictable content through one target embedding and one prediction pathway. In complex systems, this monolithic state can allocate redundant capacity to dominant signals while providing weak or conflicting gradients to less dominant predictive structure. We introduce \method, a latent world-modeling framework based on orthogonal predictive factorization. Learned basis matrices analyze each target state into multiple components, and a dedicated prediction branch estimates each component from a shared context representation. Predictive regression preserves the factor magnitudes required for state synthesis, an orthogonality objective discourages repeated directions, factor-activity regularization maintains variation in projected targets, and online variance regularization discourages coordinate-wise encoder collapse. Predicted components are synthesized into a complete latent state that can be used by a readout, decoder, planner, or autoregressive rollout. The same predictive-state mechanism applies when the target is temporally future, spatially hidden, or another partial observation of the same system. Experiments on controlled vision, single-cell transcriptomics, longitudinal health records, continuous control, and molecular dynamics evaluate representation quality, forecasting, planning, and long-horizon stability.

---


### 119. [SABET-QA: Temporal Knowledge Graph Question Answering](https://arxiv.org/abs/2608.20083)

**<font color=#1a73e8>作者：</font>** Brahim Touayouch, Mirette Moawad, Dmitry Akulov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Question Answering over Temporal Knowledge Graphs (TKGQA) requires reasoning over time-sensitive facts, yet existing embedding-based methods struggle with multi-step queries due to single-pass reasoning pipelines. We propose SABET-QA, a framework that iteratively refines reasoning states across multiple hops via a bidirectional entity-temporal scoring mechanism and a slot-aware contextualization module that aligns question semantics with temporal KG embeddings. A differentiable working memory enables progressive hypothesis refinement, while auxiliary temporal boundaries serve as coarse supervision when available. Experiments on CronQuestions, Complex-CronQuestions, MultiTQ, and TimeQuestions demonstrate consistent improvements over strong baselines, particularly on complex multi-step temporal queries.

---


### 120. [What Do Visualization Instructors Want Students to Learn? Introducing a Concept Inventory for Visualization Design](https://arxiv.org/abs/2608.20090)

**<font color=#1a73e8>作者：</font>** Medina Lamkin, Heer Patel, Sayamindu Dasgupta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The term "visualization design" encompasses multiple concepts and skills that go well beyond current assessments of graphical perception and visualization literacy. In the context of education, what exactly should a student be able to do if they "know" visualization design? To answer this question, we draw on existing methodology from the field of education to propose a concept inventory for visualization design, i.e., a theoretical model capturing the most important concepts and skills commonly associated with visualization design. We initially draft the concept inventory using a qualitative analysis of course objectives from visualization course syllabi. Then, we iteratively refine the concept inventory by soliciting feedback from instructors through semi-structured interviews. Based on our experiences in developing the concept inventory, we reflect on open questions and future research directions in visualization education, such as developing assessments for visualization design (similar to those for visualization literacy) and providing automated assistance for learning and teaching visualization design. Our supplemental materials are available at this https URL.

---


### 121. [HandMvNet: Real-Time 3D Hand Pose Estimation Using Multi-View Cross-Attention Fusion](https://arxiv.org/abs/2608.20093)

**<font color=#1a73e8>作者：</font>** Muhammad Asad Ali, Nadia Robertini, Didier Stricker  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work, we present HandMvNet, one of the first real-time method designed to estimate 3D hand motion and shape from multi-view camera images. Unlike previous monocular approaches, which suffer from scale-depth ambiguities, our method ensures consistent and accurate absolute hand poses and shapes. This is achieved through a multi-view attention-fusion mechanism that effectively integrates features from multiple viewpoints. In contrast to previous multi-view methods, our approach eliminates the need for camera parameters as input to learn 3D geometry. HandMvNet also achieves a substantial reduction in inference time while delivering competitive results compared to the state-of-the-art methods, making it suitable for real-time applications. Evaluated on publicly available datasets, HandMvNet qualitatively and quantitatively outperforms previous methods under identical settings. Code is available at this http URL.

---


### 122. [Structured Affinity for Unsupervised Visual Class-Incremental Memory in Deep Artificial Immune Networks](https://arxiv.org/abs/2608.20104)

**<font color=#1a73e8>作者：</font>** Siphesihle Sithungu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Artificial immune networks (AINs) are naturally memory-forming systems, but conventional visual AINs often rely on flattened vector affinity that ignores spatial structure. This paper studies whether structured, gradient-free immune affinity can make Deep AINs viable as replay-free visual class-incremental representation-memory learners. Visual B-cells are formalized as structured templates, including shifted-template affinity, zero-normalized cross-correlation (ZNCC) filters, and feature-map binding profiles. A repertoire is treated both as memory and as a representation-inducing basis, while depth is obtained by passing binding-profile response maps to subsequent immune layers. The resulting Deep AIN exhibits adaptive latent coordinate reorganization: as new classes arrive, the binding-profile space evolves while retaining recoverable structure for earlier classes. Experiments on sklearn digits, MNIST, Fashion-MNIST, and KMNIST show that preserving response maps is critical. Scalar binding-profile variants underperform, whereas feature-map Deep AINs learn class-discriminative visual memory without replay, label-driven immune updates, or backpropagation through the immune layers. On sklearn digits, downstream probes fitted on the learned binding profiles reach 0.939 final balanced accuracy with logistic regression and 0.902 with 1-nearest-neighbour after all ten classes are encountered, with initial-class retention of 0.978. Adaptive layer-wise scale calibration further improves the two-layer feature-map Deep AIN to 0.978 balanced accuracy. With the same calibration rule, Fashion-MNIST reaches 0.814 and KMNIST reaches 0.853. These probes are external validation tools, not components of the AIN. The results identify structured affinity, response-map preservation, adaptive latent reorganization, and layer-wise scale calibration as key mechanisms for replay-free visual immune memory.

---


### 123. [A Meta-Study on Replication Papers in Usable Security & Privacy](https://arxiv.org/abs/2608.20108)

**<font color=#1a73e8>作者：</font>** Christian Mack, Benjamin Berens, Hanna Algedri 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The field of usable security and privacy research is a young and expanding field, which is still developing standards for its research, e.g. regarding replications. We used a mixed-method approach, in order to get a better understanding of the current state of replications in the field of usable security and privacy: (1) we examine the Call for Papers of 13 venues spanning security, privacy, and human-computer interaction; (2) we conduct a systematic search for papers reporting replicated user studies published across these venues between 2016 and 2025, yielding 24 relevant publications; (3) we categorized these 24 papers employing the replication taxonomy proposed by Olszewski et al. (2025); (4) we distributed a survey to the authors of these papers to understand their motivations for conducting replications. Our analysis reveals four key insights: (A) Calls for Papers would benefit from clearer guidelines for authors and reviewers regarding replication work; (B) determining what modifications were made relative to the original study proves difficult when reading replication papers; (C) strict exact replications do not exist in our sample. Approximately two-thirds of the 24 studies altered multiple aspects of the original work; (D) temporal and contextual changes affecting results emerged as one of the most frequently cited motivations for replication. Based on these findings, we offer practical recommendations for venues, researchers, and peer reviewers to strengthen replication practices in usable security and privacy research.

---


### 124. [DECOWAM: Decoupled Whole-Body World-Action Model for Legged Mobile Manipulation](https://arxiv.org/abs/2608.20114)

**<font color=#1a73e8>作者：</font>** Siyuan Ma, Boshi Zhang, Yutian Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mobile manipulation requires a robot to predict how locomotion and arm motion jointly alter future observations and control. Existing world-action models, developed largely for fixed-base platforms, do not explicitly distinguish camera ego-motion from base and arm actions. Here we introduce DECOWAM, a whole-body world-action model that separates these factors through dedicated conditional interfaces. DECOWAM freezes an adapted FastWAM backbone and trains residual adapters, an action-equivalent future bottleneck distilled from privileged observations, adversarially separated base and arm latents, and base-velocity conditioning for video prediction. We further introduce ARMDOG, a real-robot dataset that synchronizes video, whole-body state and action, and language. On a fixed replay protocol, DECOWAM improved both future-video and action prediction over FastWAM, reducing action MSE by 21.7% with 25.95M trainable adaptation parameters. Across 79 closed-loop trials per method, it achieved the highest observed whole-body coordination and base-displacement robustness among the compared systems, while task completion remained comparable to the strongest baseline. These results show that embodiment-aware factorization can support parameter-efficient joint visual prediction and whole-body control under moving viewpoints.

---


### 125. [SAE-Xplainers: Rule-Based Feature Interpretation for Extreme Earth Events](https://arxiv.org/abs/2608.20117)

**<font color=#1a73e8>作者：</font>** Hugo Porta, Emanuele Dalsasso, Chang Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The emergence of large-scale Weather and Climate (W&C) datasets offers new opportunities for modeling extreme Earth events (ExEE) and their impacts using deep learning. However, their adoption in operational settings remains limited by the lack of models' interpretability. While for conventional text and image modalities, tools such as Sparse Autoencoders (SAEs) have proven effective for extracting human-understandable concepts, their use for the analysis of ExEE remains challenging due to the nature of W&C data. To address this, we introduce (i) a geographic location-based modulation of the inputs of SAE to capture the local semantic meaning of environmental patterns, and (ii) an ensemble of rule-based SAE-Xplainers to interpret the resulting high-dimensional features derived from complex, multi-modal environmental predictors. We evaluate our method on three ExEE types: the prediction of fires, and the detection of tropical cyclones and atmospheric rivers. We show that SAE input modulation improves both reconstruction performance and feature utilization, and that our SAE-Xplainers enable faithful interpretation of complex climatic patterns by unfolding them into human-understandable rules that are consistent with the scientific literature, while also supporting the identification of feature absorption.

---


### 126. [Privacy-Preserving Detection of Rare Disease-Associated Cell Subsets via Secure Multi-Party Computation](https://arxiv.org/abs/2608.20118)

**<font color=#1a73e8>作者：</font>** Ş. Selcan Magara, Esther Havemann, Debora Jutz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The detection of rare disease-associated cell subsets from high-dimensional single-cell measurements is critical for understanding diseases such as leukaemia and viral infections. CellCnn, a convolutional neural network (CNN) designed for this task, has demonstrated the ability to identify phenotype-associated cell populations at frequencies as low as 0.01\%. Training such models reliably requires patient cohorts that are larger and more diverse than any single institution can typically assemble, and the underlying single-cell data is too sensitive to share across institutional boundaries under existing privacy regulations. We propose a secure multi-party computation (MPC) framework that enables the training and inference of CellCnn entirely on secret-shared data. This ensures that neither the participants nor the computing servers ever observe raw patient data or intermediate values. Evaluated on benchmark single-cell datasets for cytomegalovirus infection (CMV) and acute myeloid leukaemia (AML), our implementation preserves accuracy close to its plaintext counterpart while outperforming the prior privacy-preserving baseline. In contrast to earlier privacy-preserving approaches that removed components such as ReLU activations and bias terms, our method retains these key parts of the CellCnn architecture and supports accurate analysis without exposing raw patient data.

---


### 127. [ID-VTG: Image-Disambiguated Video Temporal Grounding](https://arxiv.org/abs/2608.20127)

**<font color=#1a73e8>作者：</font>** Minghang Zheng, Jingli Wei, Hongyi Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Temporal Grounding (VTG) faces significant challenges when natural language queries must distinguish between multiple events involving visually similar entities, particularly when relying on fine-grained visual attributes that are difficult to describe accurately in words alone. To address this, we introduce Image-Disambiguated Video Temporal Grounding (ID-VTG), a task that leverages multimodal queries combining a reference image and a text description to precisely localize segments where a specific instance performs a described action. To facilitate research, we construct two benchmarks: IDVTG-Gym, focusing on fine-grained, compositionally ordered gymnastics actions with athletes in similar uniforms; and IDVTG-InternVid, an open-world dataset featuring diverse entities (e.g., humans, animals, fictional characters) and significant temporal distractors. Methodologically, we propose the Visually-Guided Disambiguation Aggregation (VGD-Agg) framework based on a dual-branch fast-slow architecture. The fast branch efficiently generates preliminary event proposals, while the slow branch performs fine-grained frame-level matching between video frames and the reference image. We enhance discriminability via two learnable tokens: a Compare Token, which represents hard negatives to probe for the presence of the target instance (as referred to by the query image), and a Depress Value, which represents text-irrelevant events. Proposals that the Compare Token identifies as lacking the target instance are pushed toward the Depress Value, thus easing disambiguation via the text query. Extensive experiments validate our approach, which achieves state-of-the-art results on the proposed benchmarks. Code is available at this https URL.

---


### 128. [Navigating and Retrieving Information in Immersive Model-Based Design Reviews: An Exploratory Study](https://arxiv.org/abs/2608.20128)

**<font color=#1a73e8>作者：</font>** Victor Romero, Romain Pinquié, Frédéric Noel  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Digital engineering uses many models from different perspectives, creating a connected set of digital artefacts across a product's life cycle. Designers seeking a holistic view must navigate numerous models and views, requiring domain-specific software, languages, and representations. This can lead to getting lost in scattered information and the cognitive burden of mentally integrating details across diagrams. To overcome these issues, we developed the virtual environment GraphXplore. GraphXplore enhances perceptual and conceptual integration by linking all relevant visual items from different perspectives into an interactive, layered 3D graph displayed in virtual reality, providing a holistic view of the system. We compared GraphXplore with a conventional on-screen setup using a PowerPoint slide deck with model screenshots viewed on a desktop PC. In an experiment with N=33 volunteers (mainly industrial product design postgraduates and professors), we conducted a baseline usability study focused on fundamental information retrieval tasks for model-based design comprehension, as identifying basic model elements is the fundamental prerequisite in design reviews. Our findings indicate that for simple retrieval tasks, the correctness of answers, completion time, recall score, and perceived confidence are comparable in both environments. However, the virtual environment demonstrated practical advantages, achieving a "good" average System Usability Scale (SUS) score of 73.1 compared to the slide setup's borderline score of 66.4. Furthermore, GraphXplore users reported a lower perceived cognitive workload (mean NASA-TLX score of 43.8) compared to the traditional setup (50.4). Future work will enhance this experiment to yield empirical results across massive industrial datasets, refine GraphXplore, and extend to new design review objectives.

---


### 129. [Feature Evolution and Migration during Vision Transformer Training](https://arxiv.org/abs/2608.20134)

**<font color=#1a73e8>作者：</font>** Joonas Järve, Halil Ibrahim Aysel, Tarun Khajuria 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a novel view on feature evolution in Vision Transformers (ViTs) by visualizing the training process over two dimensions -- network depth (layer) and training time (epochs). We employ Sparse Autoencoders (SAEs) to extract candidate sparse features from CLS-token representations and compare their activation profiles across epoch--layer pairs. This allows us to study feature-level dynamics that are not directly visible from representation-level similarity measures. Furthermore, we demonstrate how this framework of feature evolution allows us to describe feature migration, the change in the layer where a feature is most detectable during training. Our experiments show that migration is concentrated early in training, occurs more often toward earlier layers than toward deeper layers, and declines as feature organization stabilizes. We further find that deeper layers stabilize earlier and more strongly than shallow layers. The results show that our approach can be employed as a tool for understanding how ViTs learn and evolve.

---


### 130. [PelviNeXt: A Modality-Agnostic Hybrid Network for Pelvic Imaging in Women's Health](https://arxiv.org/abs/2608.20144)

**<font color=#1a73e8>作者：</font>** Siam Tahsin Bhuiyan, Rashedur Rahman, Sefatul Wasi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Women's health remains substantially under-resourced in medical imaging research, with pelvic pathologies such as polycystic ovary syndrome (PCOS) and pelvic fracture both suffering from a scarcity of public, well-annotated benchmark data despite their clinical importance. We introduce PelviNeXt, a modality-agnostic hybrid architecture combining a dense convolutional feature extractor, hierarchical channel-spatial attention (H-CBAM), a multi-scale fusion module (MSFM), and talking-heads multi-head self-attention (TH-MHSA), applied without modification to both pelvic ultrasound and X-ray inputs. While benchmarking PelviNeXt on PCOSGen, the only gynaecologist-annotated public PCOS ultrasound dataset, we identified extensive exact and near-duplicate contamination within and across the dataset. We audit this contamination via perceptual hashing, publicly release a deduplicated version of the dataset, and establish the first integrity-audited evaluation protocol and baseline for PCOSGen under 5-fold cross-validation. On the only publicly available pelvic fracture X-ray dataset (PXR150), PelviNeXt exceeds previously reported state-of-the-art results across accuracy, recall, specificity, and AUROC. Ablation studies confirm that each architectural component contributes to performance on both tasks. Our results demonstrate that a single architecture, applied without task-specific modification, can serve as a reliable foundation for pelvic imaging across modalities in data-scarce, under-researched areas of women's health.

---


### 131. [Trustworthy mobile edge caching: a blockchain approach to mitigate malicious nodes and incentivize cache sharing](https://arxiv.org/abs/2608.20145)

**<font color=#1a73e8>作者：</font>** Motahare Ebrahimi, Nastooh Taheri Javan, Seyedakbar Mostafavi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As mobile network traffic continues to grow, content caching on edge servers is critical for reducing latency. However, challenges such as malicious edge servers that may delete or manipulate cached content, along with the limited capacity of these servers, need to be addressed. To overcome the capacity limitations, helper mobile nodes can contribute their cache resources. However, due to their selfish behavior, an incentive mechanism is necessary to encourage resource sharing. Additionally, these helper nodes can also be malicious. This paper proposes a blockchain-based trust management mechanism that addresses these challenges by accurately identifying trustworthy edge servers and mobile nodes. The proposed mechanism calculates both direct and indirect trust using smart contracts, ensuring that malicious nodes are effectively filtered out. Trustworthiness is determined based on mobile node satisfaction with the quality of service, and trust data is securely stored on the blockchain. To combat node selfishness, a reward mechanism is introduced to incentivize cache sharing. Furthermore, a blockchain-based authentication mechanism protects against node impersonation. Our approach optimizes trust, cache capacity, and cost efficiency while considering mobile node mobility, energy consumption, and computational power constraints during the consensus process. Simulation results show that the proposed method can accurately distinguish between honest and malicious servers, even with a 10% noise in data.

---


### 132. [Evaluating Neural Cartographic Relief Shading for Urban Environments: A Downtown Calgary Study Using High-Resolution DEM and DSM Data](https://arxiv.org/abs/2608.20149)

**<font color=#1a73e8>作者：</font>** Emmanuel Stefanakis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This article explores the performance of analytical and neural-based hillshading methods in a dense urban environment using high-resolution digital elevation model (DEM) and digital surface model (DSM) data for downtown Calgary. The study compares single-direction and multi-direction analytical hillshading with relief shading generated in Eduard, a machine-learning system originally developed to emulate Swiss-style shaded relief trained primarily on mountainous landscapes. Because Eduard was not designed for buildings, bridges, streets, trees, and other urban infrastructures, the central question is not whether it perfectly reproduces urban morphology, but whether parameter tuning can nevertheless produce visually strong, cartographically useful, and in some cases superior results when compared with conventional analytical methods. The analysis focuses especially on terrain type, micro and macro generalization, and flat-area detail parameters, while keeping the large-scale shading style constant throughout the neural experiments. The article is structured as an exploratory comparison rather than a benchmark of universal best practice. It aims to identify where analytical hillshading remains more reliable, where Eduard offers unexpected strengths, and where neural shading fails because of its training bias toward alpine terrain. The study contributes to current work on terrain representation by testing whether a neural approach designed for natural landforms can be adapted to a highly built urban setting, and it concludes by arguing for future model training and evaluation specifically targeted at urban relief shading.

---


### 133. [Artificial Intelligence for Workflow Analysis in Colorectal Surgery: A Multicentric, Cross-Procedural Development and Generalization Study](https://arxiv.org/abs/2608.20154)

**<font color=#1a73e8>作者：</font>** Pietro Mascagni, Julia Alekseenko, Pooja P Jain 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Minimally invasive colorectal surgeries (MIS-CRS) are characterised by significant variability and inconsistent outcomes. ColoWorkflow, a tool for the video-based assessment (VBA) of MIS-CRS workflow, was recently validated. However, manual VBA is time-consuming, limiting implementation. This study presents AI-ColoWorkflow, a deep learning model for automated surgical workflow analysis across MIS-CRS. Operative videos of MIS-CRS were collected from 4 centres and a publicly available dataset. Phases and steps were manually annotated according to ColoWorkflow. A deep learning model combining a fine-tuned DINOv3 vision transformer for per-frame visual feature extraction with a hierarchical multi-stage temporal convolutional network was jointly optimized for phase and step recognition. The model trained on pooled multicentric data, namely AI-ColoWorkflow was compared against centre-specific and procedure-specific models on a held-out test set. The following metrics were used for evaluation: macro F1 score, balanced accuracy, precision, and recall. AI-ColoWorkflow achieved a macro F1 of 73.01% $\pm$ 10.27 (balanced accuracy 73.43%) for phase recognition and 39.82% $\pm$ 7.06 (balanced accuracy 38.65%) for step recognition. The global model outperformed centre- and procedure-specific models in most experiments except procedure-specific step recognition. In the generalization analysis, mean F1 was 48.42% for phase recognition. AI-ColoWorkflow can reliably recognize MIS-CRS phases. A single model trained on pooled, multicentric, multi-procedural data generalises at least as well as and often better than centre- or procedure-specific models for phase recognition in MIS-CRS, while procedure-specific step models retain advantages for certain procedure types, motivating hybrid training strategies for future surgical AI development.

---


### 134. [G3Ego: Gaze-Guided Graphs for Egocentric Action Understanding](https://arxiv.org/abs/2608.20157)

**<font color=#1a73e8>作者：</font>** Marko Haralović, Akash Ramakrishnan, Estefania Talavera Martinez  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Egocentric action understanding is often addressed using large video models pretrained on extensive exocentric datasets. However, many first-person actions depend on a small number of hand-object interactions involving only a few relevant entities.
We propose G3Ego, a graph-based framework for egocentric action understanding that uses gaze as a structural cue to identify action-relevant entities in the scene. From sparsely sampled frames, G3Ego constructs action scene graphs from vision-language descriptions, grounded objects, and hand cues, and then prunes irrelevant entities using the camera wearer's gaze.
The resulting graph embeddings are temporally aggregated for action recognition and anticipation. Unlike prior work that uses gaze primarily as an auxiliary modality or attention signal, G3Ego incorporates gaze directly into graph construction, producing efficient and interpretable representations focused on action-relevant interactions.
Experiments on EGTEA Gaze+ and MECCANO show that G3Ego achieves competitive performance compared with video-based approaches and consistently improves Macro-F1 under class-imbalanced evaluation, while avoiding reliance on computationally expensive video pretraining. These results demonstrate the effectiveness of gaze-guided graph representations for egocentric action understanding.

---


### 135. [Chameleon: Robust Defense Against Tor Website Fingerprinting via Many-to-Many Traffic Morphing](https://arxiv.org/abs/2608.20160)

**<font color=#1a73e8>作者：</font>** Yuwen Cui, Kai Wei, Kehan Shen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Website fingerprinting (WF) attacks can infer users' browsing activities from encrypted Tor traffic by exploiting side-channel features. Although many WF defenses have been proposed, we find that most existing defenses create learnable web trace mapping features. We further show that robustness against adversarial training does not necessarily imply robustness against defense-aware autoencoder (DAAE)-based attacks.
To address these limitations, we present Chameleon, a robust WF defense based on many-to-many randomized traffic morphing. Chameleon selects morphing candidates with high intra-class diversity and low inter-class disparity. Chameleon randomly maps each webpage trace to multiple candidates, and allows different webpages to share morphing targets, thereby increasing adversarial uncertainty. For practical Tor deployment, Chameleon introduces a radix-trie-based synchronization mechanism that enables pluggable transport (PT) endpoints to identify consistent morphing traces using packet-direction prefixes, together with trace mutation and normalized prefix matching to reduce overhead. We evaluate Chameleon against six state-of-the-art defenses and five WF attacks on three public datasets in closed- and open-world settings. Compared with Adaptive Tamaraw, Chameleon reduces adversarial-training-based attack accuracy by up to 36.74% while reducing bandwidth and time overhead by 34.12% and 60.38%, respectively. Under DAAE-based RF attacks on GTT23, Chameleon limits attack performance to 35.19% F1-score while Adaptive Tamaraw only limits it to 88.22% F1-score. In the real-world PT bridge evaluation, Chameleon substantially reduces the effectiveness of strong WF attacks while incurring only 16.25% time overhead.

---


### 136. [Ask Self, Ask Others: Relation Is All You Need](https://arxiv.org/abs/2608.20172)

**<font color=#1a73e8>作者：</font>** Yuting Ge, Pengju Yang, Mingkai Nie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Attention directly derives normalized information flow from pairwise scores. We introduce Relation, an alternative token-mixing primitive that first organizes pairwise evidence into explicit Self and Exchange relations and derives information flow afterward. This relational organization gives rise to Full Relation, FlashRelation, Linear Relation, Hybrid Relation, and a KV-style Relation Cache. Across matched decoder-only models at approximately 10M, 30M, and 100M parameters, Full Relation achieves lower final validation NLL than MHA at all three scales. In a fixed-context reference benchmark, FlashRelation is 3.60-4.41x faster than the materialized Full Relation implementation. Across scale-matched production workloads, it reaches 76.4-84.9% of PyTorch FlashAttention throughput while executing the Full Relation operator. Hybrid Relation uses 75% Linear Relation layers and achieves strong language-modeling quality. These results support a relation-first view of token mixing: ask Self, ask Others, then let Flow follow Relation.

---


### 137. [A Standardized Framework for Machine Learning in Power System Protection](https://arxiv.org/abs/2608.20181)

**<font color=#1a73e8>作者：</font>** Julian Oelhaf, Georg Kordowich, Paula Andrea Pérez-Toro 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Studies of machine-learning-based power-system protection increasingly report near-perfect scores, yet the meaning of those scores depends strongly on the evaluation setting. Protection task, physical scope, measurements, timing, targets, preprocessing, and validation often vary jointly and remain incompletely specified. This paper proposes a standardization-oriented framework that treats evaluation design as part of the scientific contribution. It defines seven required study dimensions: protection objective, physical scope, observability, timing and decision windows, targets and sample validity, validation protocol, and evaluation outputs. The framework is instantiated in a bounded case study on the public PROTECT-90 electromagnetic-transient benchmark, comprising 9022 simulated episodes from a 90 kV double-line topology, for onset-conditioned fault classification and localization. Under centralized sensing, simulation-metadata-aligned 20 ms windows, and episode-grouped validation, a multi-layer perceptron (MLP) achieved a five-fold mean macro-averaged F1 score of 0.991 +/- 0.001 for classification and a localization mean absolute error of 10.20 +/- 0.25% of line length (mean +/- std across episode-grouped folds). Extending the decision horizon to 50 ms preserved this task-dependent performance asymmetry, while reduced observability approximately doubled the MLP localization error but had little effect on classification. A synchronized two-ended conventional locator outperformed the learning locators under its richer clean information set, and measurement degradation showed that clean predictive performance did not determine robustness. The framework turns evaluation assumptions into explicit, reproducible evidence and provides a basis for more comparable, auditable evaluation and future certification-oriented assessment of machine-learning protection functions.

---


### 138. [Exact Algebraic Computation of Learning Coefficients for Two-Dimensional Singular Models](https://arxiv.org/abs/2608.20183)

**<font color=#1a73e8>作者：</font>** Grégoire Sergeant-Perthuis, Elias Tsigaridas, Jules Tsukahara  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Classical information criteria such as the Bayesian Information Criterion (BIC) rely on regularity assumptions that break down for singular models, leading to incorrect model selection in settings such as deep learning. The Widely Applicable Bayesian Information Criterion (WBIC) relies on local learning coefficients $\lambda$, which in the analytic case coincides with local Real Log Canonical Thresholds (RLCT) of the Kullback-Leibler divergence of the model, to capture correct marginal likelihood asymptotics. Exact computation of the learning coefficients has been limited to special cases, and only sampling-based estimation methods are generally applicable. We present the first deterministic algorithm that computes local RLCTs exactly for any two-dimensional model whose Kullback-Leibler distance is contact equivalent to a polynomial, derive a bound on its complexity, and demonstrate its effectiveness for a broad class of models, with applications including polynomial neural networks. Beyond providing ground truth to calibrate sampling-based estimators, exact computation reveals algebraic structure in learning coefficients that sampling cannot and out-speeds it in the shallow regime.

---


### 139. [The Third Restructuring of Software Form: From the Three-Tier Architecture to Storage, Models, and Agents](https://arxiv.org/abs/2608.20201)

**<font color=#1a73e8>作者：</font>** Wei Lin, Tao Zhou, Zhaofei Xie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Software form has undergone two paradigm shifts since its inception: Software 1.0, in which instructions determine behavior, and Software 2.0, in which data determines behavior (machine learning). This paper argues that a third shift - Software 3.0, in which context and reasoning determine behavior - is now underway, and contends that its terminal form converges to three elements: a generalized database (the unified abstraction of all persistent state and memory), a large model (the intelligence core that performs reasoning and generation), and an agent (the execution loop connecting the first two). The core argument is as follows: in the traditional three-tier architecture, the user-interface layer will be absorbed by the model's ability to generate interfaces on demand, the business-logic layer will be re-partitioned along "expressibility x criticality" into model reasoning and storage constraints (with residual deterministic logic retained as tools), and only the data layer will be elevated into the sole persistent infrastructure. We formalize this convergence thesis, present a minimal reference architecture, report evidence from real prototypes and a live model, and systematically analyze both the conditions under which it holds and the boundaries where it fails - determinism, cost, security, and verifiability delimit the thesis's domain of applicability. We argue that the thesis holds in task domains that are expressible, verifiable, externally stateful, and tool-complete, and that it will reshape the roles of developers, the database industry, and the software-engineering discipline.

---


### 140. [RoMAN-Flow: Taming Autoregressive Normalizing Flows for Offline Reinforcement Learning in Robotic Manipulation](https://arxiv.org/abs/2608.20208)

**<font color=#1a73e8>作者：</font>** Shaoxuan Wang, Guangting Zheng, Rui Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Offline reinforcement learning improves robotic policies using previously collected data without further environment interaction. Yet prevalent diffusion- and flow-matching robot policies lack tractable likelihoods, limiting their use in likelihood-based offline RL post-training. AR-NFs offer both expressive action modeling and exact likelihood evaluation, but their sequential sampling incurs substantial sampling overhead during policy optimization and deployment. We present RoMAN-Flow (Robotic Manipulation with Autoregressive Normalizing Flows), an offline reinforcement learning framework that makes AR-NF policies practical for robotic manipulation by addressing this sampling bottleneck in both stages. During policy optimization, RoMAN-Flow employs a sampling-free, advantage-weighted likelihood objective that assigns higher likelihood to high-advantage actions from the offline dataset without sampling from the autoregressive policy. For efficient deployment, it distills the optimized autoregressive policy into a one-step action generator, enabling low-latency action prediction. Experiments across multiple simulated manipulation benchmarks and real-world robotic platforms demonstrate that RoMAN-Flow achieves competitive policy performance while substantially reducing inference latency. Code is available at this https URL.

---


### 141. [Electronic Navigational Chart Change Classification](https://arxiv.org/abs/2608.20218)

**<font color=#1a73e8>作者：</font>** Jacob Arndt, Abhishek Potnis, Alexandre Sorokine  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Electronic Navigational Charts (ENCs) are geospatial vector datasets used in maritime navigation systems that represent hydrographic and navigational information such as depths, navigational aids, traffic schemes, and hazards. A major challenge for hydrographic offices is determining whether a given chart change poses a critical or non-critical risk to maritime safety. Existing workflows rely heavily on manual review and verification, which is labor-intensive, scales poorly with the volume of incoming chart updates, and introduces inter-analyst inconsistencies. To address this challenge, we propose a method for automated classification of ENC changes. We establish a baseline encoding scheme to translate complex vector data changes into a structured tabular format for classification models. The two crucial components of the encoding scheme include a spatial context encoder to enrich the change representations with surrounding geographic features, and an ENC attribute encoder to represent nuanced attribute-value descriptions of the modified objects. We evaluate the proposed approach across two distinct operational datasets, comprising 1,308 chart pairs containing over 100,000 individual chart modifications. Tuned gradient-boosted trees leveraging the proposed encoding schemes achieve accuracies of 90% and 94% on the two datasets, yielding a 5-7% improvement over default hyperparameterized models trained on encodings without spatial context and attribute embeddings. These results demonstrate the viability of integrating machine learning into operational geospatial pipelines to improve ENC maintenance and enhance maritime safety. Finally, our experiments demonstrate the effectiveness of simple location and spatial aggregation methods, providing a foundation for evaluating more sophisticated spatial representation learning techniques for this application.

---


### 142. [Prompt-Conditioned Channel Attention for Hierarchical Feature Modulation toward Anatomy-Agnostic Segmentation](https://arxiv.org/abs/2608.20229)

**<font color=#1a73e8>作者：</font>** Mosharof Hossain, Md Rabiul Islam, Limon Halder 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Anatomically plausible segmentation remains challenging because of low contrast, ambiguous boundaries, and modality-specific artifacts. Interactive segmentation has emerged as a promising strategy to guide feature extraction and improve localization, particularly in structurally ambiguous regions. However, existing methods integrate prompts through late-stage fusion and lack explicit mechanisms for prompt-driven channel-wise modulation across hierarchical feature representations, limiting their ability to capture deeper contextual and modality-specific variations. To address these limitations, we introduce Prompt-Conditioned Channel Attention (PCCA), a novel modulation mechanism that enables deep, hierarchical integration of semantic prompts within encoder-decoder networks. PCCA extracts compact channel descriptors via pooling, projects them into a shared space, and fuses them through a gated excitation mechanism to compute prompt-aware channel attention weights. These weights adaptively recalibrate feature responses across multiple network stages, enabling prompt-conditioned, semantically enriched hierarchical representations. Building on this, we propose PROMISE-Net, instantiated in two network variants: a convolutional model (PROMISE-CNN) and a transformer-based model (PROMISE-Txformer). Across the ISIC-Lesion, Kvasir-Polyp, CAMUS-Cardiac, and Kvasir-Instrument benchmarks, integrating PCCA into PROMISE-CNN yielded relative IoU gains of 10.4%, 8.7%, 0.8%, and 3.4%, respectively, over the baseline U-Net, while PROMISE-Txformer achieved corresponding gains of 7.6%, 23.0%, 2.1%, and 1.1%, respectively, over the baseline UNETR. These results show consistent improvements across architectures, imaging modalities, and anatomical targets, establishing PCCA and PROMISE-Net as a scalable, generalizable framework for prompt-aware hierarchical feature modulation in medical image segmentation.

---


### 143. [QUASAR: A Quantum-Classical Neural Network for SAR Satellite Physical-Layer Authentication](https://arxiv.org/abs/2608.20240)

**<font color=#1a73e8>作者：</font>** Vincenzo Sammartino, Nathanael Denis, Roberto Di Pietro  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> X-band SAR satellites (8-12 GHz) play a critical role in disaster response, environmental monitoring, and military intelligence. Yet, they lack robust physical-layer authentication (PLA), a security layer orthogonal to cryptographic solutions. Existing PLA systems, typically based on radio-frequency fingerprinting, are often limited to sub-6 GHz frequencies and rely on classical deep learning. However, this approach underfits the IQ phase nonlinearities that distinguish satellite hardware. In this paper, we present QUASAR, to the best of our knowledge the first quantum-classical hybrid architecture that fuses a CNN spectrogram encoder with a variational quantum circuit (VQC) to provide PLA to X-band SAR signals. Our solution enjoys two distinctive features: (i) it is markedly more data-efficient than classical machine learning, requiring only 10% of the training data to match the accuracy of classical baselines -- data collection being notoriously the most time-consuming phase of PLA; and, (ii) at an equal data budget, it improves classification accuracy over those baselines. In detail, we test our solution under three adversarial scenarios: replay, crafted-IQ injection, and space-borne spoofing. QUASAR rejects spoofed transmissions in 89.7%, 94.1%, and 81.3% of attempts, respectively, establishing the first quantum-enhanced physical-layer classifier for satellite constellations. The fully detailed framework and the supporting results, other than being interesting on their own, show a novel research avenue for physical-layer authentication.

---


### 144. [DICS: Data-Informed Centroid Splitting for Decision Tree Classifiers](https://arxiv.org/abs/2608.20258)

**<font color=#1a73e8>作者：</font>** MD Saifur Rahman Mazumder, Feng Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decision tree-based models are widely used in machine learning due to their interpretability and strong empirical performance. However, training decision trees can be computationally expensive, particularly for large and high-dimensional datasets, largely due to the exhaustive search over candidate splits at each node. To improve computational efficiency, we propose Data-Informed Centroid Splitting (DICS), a clustering-based framework that constructs a compact and informative set of candidate splits using data-driven priors. By incorporating class-aware structure, DICS significantly reduces the split search space for classification tasks while preserving predictive performance. We further provide theoretical analysis showing that under the stated assumptions, DICS does not degrade the performance of classification trees compared to exhaustive split search. DICS can be incorporated into classification trees, random forests, and gradient-boosting models. Extensive experiments demonstrate that DICS achieves comparable accuracy while substantially reducing training time across synthetic and benchmark datasets, highlighting the benefit of integrating data-informed priors into split selection for scalable classification tree learning.

---


### 145. [Ultra-High-Definition Restoration Transformers with Correlation Matching Transformation](https://arxiv.org/abs/2608.20263)

**<font color=#1a73e8>作者：</font>** Cong Wang, Liyan Wang, Jinshan Pan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose UHDformer++, a general Transformer-based framework to solve numerous Ultra-High-Definition (UHD) image restoration tasks. UHDformer++ operates across $4$ coordinated learning spaces: 1) a high-resolution space (HR) for multi-level feature extraction, 2) a low-resolution space (LR) for learning compact, representative features, 3) a super-resolution space (SR) for upsampling low-resolution features from SR, and 4) a low-high fusion and reconstruction space (LHFR) for final image restoration. Specifically, HR extracts multi-scale high-resolution features and fuses them with low-resolution cues to produce residual images, while LR distills complementary representations from HR to improve restoration quality. To supply LHFR with richer features, SR super-resolves LR outputs before fusion. We further introduce two modules to bridge the high- and low-resolution spaces. The Feature-Refined Correlation Matching Transformation (FR-CMT) module selects the top $C/r~(C~\text{denotes the number of channels;~}r\geq1~\text{controls the squeezing level})$, from the fusion between max- and mean-pooled high-resolution features to replace less informative channels in the low-resolution Transformer. The Adaptive Channel Modulator (ACM) adaptively recalibrates multi-scale high-resolution features, ensuring that only task-relevant information propagates to LR. Extensive experiments demonstrate that UHDformer++ reduces model parameters by at least 86\% compared with recent state-of-the-art methods while achieving substantial performance gains across $5$ UHD restoration tasks, including low-light image enhancement, dehazing, deblurring, deraining, and desnowing. Code will be released at this https URL.

---


### 146. [Catching the Rug: Early Prediction of Fraudulent Memecoins on Solana via Machine Learning](https://arxiv.org/abs/2608.20271)

**<font color=#1a73e8>作者：</font>** Jianghai Li, Pavel Kuznetsov, Yury Yanovich 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid proliferation of memecoins on blockchain platforms has increased the risk of fraudulent activities, particularly rug pulls. While previous studies have focused on Ethereum-based tokens, this paper shifts the spotlight to Solana, the leading blockchain for memecoins by trading volume and token count. Unlike Ethereum, where rug pulls often exploit smart contract backdoors, Solana memecoin rug pulls are predominantly driven by liquidity manipulation and social dynamics. This research pioneers large-scale rug pull early detection in the Solana ecosystem by assembling a dataset of 6.4 million tokens over 7 months. Market analysis reveals that a vast majority of these memecoins exhibit rug pull characteristics within one hour of launch, highlighting the urgency of short-horizon prediction. Despite the absence of code-level features, we demonstrate that classic machine learning models, particularly Gradient Boosting (XGBoost), achieve robust performance in detecting potential rug pulls using only the first 5 minutes of trading data. Furthermore, we evaluate cross-platform generalization between PumpFun and Raydium, revealing that multi-source data fusion significantly mitigates domain shift and improves detection reliability. This study advances the understanding of DeFi fraud on high-throughput chains and provides a practical framework for protecting investors.

---


### 147. [Towards Surgical World-Action Modeling: A Preliminary Joint Visual-Trajectory Forecasting for Surgical Motion Planning](https://arxiv.org/abs/2608.20284)

**<font color=#1a73e8>作者：</font>** Weiliang Huang, Huanrong Liu, Bob Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable surgical planning requires models to anticipate not only how instruments will move, but also how the operative visual state will evolve together with such motion. Existing approaches typically treat future scene generation and instrument trajectory prediction as two separate tasks. Scene-only models cannot directly evaluate the accuracy of future instrument motion at the trajectory level, while trajectory-only models fail to capture the visual consequences of instrument movement, leaving the consistency between predicted trajectories and future scene evolution unaddressed. Jointly forecasting both provides a more complete account of surgical action-scene dynamics by enabling explicit trajectory-level evaluation while simultaneously modeling the corresponding visual evolution. To bridge this gap, we present a preliminary joint visual-trajectory world-action model that simultaneously forecasts future visual states and instrument trajectories from historical surgical observations. Specifically, we encode historical video frames and tool trajectories into latent representations, which are processed by a temporal-spatial encoder and subsequently decoded through separate visual-state and trajectory prediction heads. Based on this preliminary architecture, a chunked autoregressive rollout is repeatedly applied to predict fifteen future steps. The chunked strategy consistently outperforms direct one-shot prediction across all evaluated horizons, improving first-segment PSNR from 18.86 to 23.11 dB and reducing ADE from 45.77 to 22.22 pixels. These results demonstrate the initial feasibility of joint visual-motion forecasting. However, we observe progressive visual degradation and accumulated trajectory errors over longer prediction horizons, which remain important challenges for future surgical world-action modeling.

---


### 148. [Dynamic Structural Causal Modeling for Sleep](https://arxiv.org/abs/2608.20285)

**<font color=#1a73e8>作者：</font>** Ranveer Singh, Saurabh Mathur, Pranuthi Tenali 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The causal dynamics of sleep-disordered breathing are complex and vary across patient populations, hindering the development of targeted interventions. We learn dynamic causal graphs of sleep-disordered breathing from Home Sleep Apnea Test (HSAT) recordings, revealing systematic differences in causal structure across sex and age subcohorts. We do so using the PCMCI+ algorithm on windowed fractional variables derived from 105 HSAT recordings, exploiting domain knowledge via edge blacklisting and employing bootstrap aggregation to address small subcohort sizes. The learned graphs show that temporal self-dependencies and the apnea-desaturation relationship persist across all cohorts, while other relationships vary substantially.

---


### 149. [Physical-Support Confidence Sets for Highly Coherent Dictionaries](https://arxiv.org/abs/2608.20295)

**<font color=#1a73e8>作者：</font>** Guan-Ju Peng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse pursuit after dictionary learning can yield a precise atom support even when its physical interpretation is not justified by the calibration data, especially for highly coherent dictionaries where alternative calibration-compatible dictionaries may assign different physical meanings to the same selected support. We develop resolution-aware physical-support inference that jointly accounts for uncertainty in the learned dictionary and in the representation of a deployment signal. Our cross-dictionary confidence correspondence retains calibration-compatible dictionaries and deployment-compatible sparse representations, then projects the surviving explanations onto physical-support space. For local coherent-atom classes with separation scale s, once the deployment data resolve the coherent-block explanation and its atom support, the minimax physical resolution from N calibration signals satisfies $\delta_{\mathrm{opt}}(N,s)\asymp\min\{s,\frac{1}{\sqrt{N}s^2}\}$, with relative resolution governed by the orientation-information scale $Ns^6$. Deployment replication improves physical localization only when orientation changes cannot be absorbed by adjusting the active coefficients. For computation, we introduce active endpoint bracketing (AEB), an adaptive finite-bank procedure that evaluates only candidates that can still affect the physical report and otherwise safely coarsens or abstains. Finite-bank experiments, including a four-region synthetic application, show that a point-valued plug-in selector can be physically overprecise, whereas AEB avoids unsupported refinement with fewer candidate evaluations.

---


### 150. [CalcSeg: Confidence-aware 3D Latent Context Curriculum Learning For Myocardial Scar Segmentation From Single-Stack LGE-CMRs](https://arxiv.org/abs/2608.20305)

**<font color=#1a73e8>作者：</font>** Nivetha Jayakumar, Hannah Kim, Amit R. Patel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Myocardial scar segmentation from single-stack late gadolinium-enhanced cardiac magnetic resonance (LGE-CMR) imaging has been a longstanding and clinically important challenge, particularly in the presence of low tissue contrast, diffuse, and small scar regions. These challenges are further intensified by the limited availability of 3D spatial context. This paper presents CalcSeg, a Confidence-aware latent context curriculum learning framework that leverages fused 3D feature representations from single-stack 2D LGE-CMR images for robust scar segmentation. Specifically, we introduce a dynamic semi-supervised curriculum learning strategy that progressively expands training from easier to more challenging scar cases using a learned confidence-aware scoring function. Such a function integrates errors in the predicted scar maps with quantified epistemic uncertainty and scar burden estimation to automatically assess sample difficulty without requiring manual labels. To compensate for the limited spatial context in single-stack acquisitions, we then develop a latent slice-wise self-attention to capture inter-slice dependencies and infer 3D spatial representations from sparse 2D inputs. We evaluate CalcSeg on multi-center clinical LGE-CMR datasets and benchmark against existing scar segmentation networks. Experimental results show that CalcSeg consistently outperforms all competing methods, particularly with substantial improvements on clinically challenging cases. Our code is released on Github.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-155](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
