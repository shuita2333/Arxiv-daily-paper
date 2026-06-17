# 📦 其他研究 | 2026年06月18日

> 本类共 **205** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-205](./part-05.md)

---

### 101. [Closing the Feedback Loop: From Experience Extraction to Insight Governance in Verbal Reinforcement Learning](https://arxiv.org/abs/2606.17591)

**<font color=#1a73e8>作者：</font>** Yanwei Cui, Xing Zhang, Yulong Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training-free verbal reinforcement learning enables LLM agents to learn from world feedback -- objective signals such as dynamic task outcomes, market returns, or demand forecasts -- by extracting verbal rules from experience and injecting them as context, updating the agent's behavior without parameter changes. However, in non-stationary environments these agents face a retention-forgetting dilemma: retaining stale insights causes negative transfer, while discarding them causes catastrophic forgetting when conditions recur. We identify four requirements for navigating this dilemma -- outcome-driven evaluation, persistent structured evidence, non-monotonic knowledge lifecycle, and compositional governance -- and show that existing methods invest heavily in experience extraction while underinvesting in insight governance. We propose a three-layer architecture -- rules, evidence, and skills -- connected by a feedback-driven curation loop that closes the governance gap. Rules capture distilled experience from world outcomes; evidence logs track each rule's reliability across episodes; skills govern which rules to apply, how to resolve conflicts, and when to abstain. On financial forecasting as a case study, where world feedback is naturally abundant, noisy, and non-stationary, we show that the same accumulated experience either degrades performance below the zero-shot baseline or dramatically improves accuracy and risk-adjusted returns, depending on whether the curation loop is present.

---


### 102. [Test-Time Training for Robust Text-Guided Open-Vocabulary Object Counting](https://arxiv.org/abs/2606.17601)

**<font color=#1a73e8>作者：</font>** Hao-Yuan Ma, Yuda Zou, Li Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-guided Open-vocabulary Object Counting (TOOC) enables counting arbitrary object categories specified by text prompts, offering substantially greater flexibility than conventional closed-set counting. However, existing TOOC methods are developed and evaluated primarily on ideal images, while real-world scenes often suffer from adverse conditions such as rain, fog, darkness, and sensor noise, which severely degrade visual quality and impair vision-language alignment. To bridge this gap, we introduce Robust-TOOC, the first benchmark for evaluating TOOC under diverse corruption conditions, which covers six representative degradation types: rain, fog, darkness, Gaussian noise, salt-and-pepper noise, and mixed corruption. To improve robustness while preserving the original counting architecture, we propose Dual-TTT, a dual-architecture test-time training framework for TOOC. Specifically, during test-time training, Dual-TTT updates only the Text-guided Lightweight Denoising module (TL-Denoiser), while keeping the original counting network frozen. Inspired by diffusion models, the TL-Denoiser is optimized to remove corruption-aware noise from image representations under degraded conditions. Since only the TL-Denoiser is trained at test time, Dual-TTT is annotation-free and can be seamlessly integrated into existing TOOC models without modifying their original architecture. Extensive experiments on multiple recent TOOC baselines demonstrate the effectiveness of our method.

---


### 103. [Expanding SPHERE-JEPA: A Family of Statistical Regularizers for the Hypersphere](https://arxiv.org/abs/2606.17603)

**<font color=#1a73e8>作者：</font>** Léo Nicollier, Enric Meinhardt-Llopis, Max Dunitz 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In Self-Supervised Learning (SSL), preventing representation collapse by explicitly enforcing a uniform distribution on the unit hypersphere has proven to be effective. However, current frameworks typically rely on sliced statistical regularizers such as SIGReg (used in LeJEPA) and SUSReg (used in SPHERE-JEPA), which approximate this continuous objective via Monte Carlo sampling along random 1D directions. This stochasticity injects projection variance into the training gradients, destabilizing optimization, and hindering convergence. In this work, we first show that analytically integrating out these random projections natively yields a deterministic Maximum Mean Discrepancy (MMD), bypassing the variance of sliced methods. Motivated by this equivalence, we formulate full-dimensional objectives for MMD, Kernel Stein Discrepancy (KSD), and Kullback-Leibler (KL) divergence directly on the sphere to enforce a uniform distribution. To prevent spatial bias, we equip these tests with rotationally invariant kernels constructed via spectral theory, systematically evaluating two canonical families: smooth exponential decay (Heat) and strict frequency cutoff (Bandlimited) filters. Empirically, removing projection-induced noise results in more stable optimization, faster convergence, and consistent improvements over stochastic sliced regularizers on ImageNet and Galaxy10. Furthermore, we reveal that the choice of the statistical test shapes the geometry of the learned latent space: MMD and KSD favor locally clustered organization suitable for object-centric domains, whereas the continuous KDE-based KL divergence promotes fine-grained instance separation, yielding the strongest results on unclustered procedural texture retrieval.

---


### 104. [Flux-Guard: Facial Identity Protection using diffusion models](https://arxiv.org/abs/2606.17606)

**<font color=#1a73e8>作者：</font>** Jie Wang, Tao Wang, Ru Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The widespread deployment of face recognition (FR) systems exposes personal images shared on social media and public platforms to identity linkage and privacy risks. Existing adversarial privacy protection methods can degrade unauthorized FR performance but are not compatible with generative face editing. Artificial intelligence-driven face editing tools are gaining popularity, which has significantly increased user demand for personalized portrait generation and social sharing. However, current editing methods often preserve identity features, making the edited images still susceptible to tracking by malicious FR systems. Thus, this paper proposes Flux-Guard, a privacy-preserving face editing framework based on adversarial attacks, which integrates face editing and privacy protection within a unified generative process. Specifically, we design a flow trajectory control method to align semantic manipulations with the generative process and introduce latent-space adversarial optimization with an adaptive perceptual-loss-driven weighting strategy, dynamically adjusting adversarial strength to maximize attack effectiveness while preserving visual quality.
Extensive experiments demonstrate that Flux-Guard supports face editing while significantly improving attack success rates against cross-domain face recognition models on the CelebA-HQ and LADN datasets. Furthermore, evaluation results for commercial APIs have confirmed its effectiveness in real-world applications. The code is released at this https URL.

---


### 105. [Towards Speech Impairment Prediction in German-Speaking Individuals with Amyotrophic Lateral Sclerosis](https://arxiv.org/abs/2606.17616)

**<font color=#1a73e8>作者：</font>** Monica Gonzalez-Machorro, Ricarda von Heynitz, Justine Hanslmeier 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Amyotrophic Lateral Sclerosis (ALS) is a neurodegenerative disease, often affecting speech due to bulbar dysfunction. In this study, we predict speech impairment in people with ALS (pwALS) using two clinical speech-related scores. We evaluate cross-sectional (across speakers) and personalised (within-speaker) modelling paradigms and analyse the utility of common speech tasks to contribute to the standardisation of speech data collection for pwALS. Experiments on a German-speaking cohort of 66 pwALS show that repetition tasks (/da/-/da/, /da/-/ba/) achieved the best cross-sectional performance (Concordance Correlation Coefficient (CCC) = 0.62) for predicting the Quality of Life in the Dysarthric Speaker questionnaire, while the within-speaker setting reached a CCC of 0.86. This study represents an initial step towards speech impairment prediction in German-speaking pwALS and highlights the potential of automated speech analysis as a supportive tool for speech impairment assessment.

---


### 106. [Divide, Deliberate, Decide: A Multi-Agent Framework for Fine-Grained Egocentric Action Recognition](https://arxiv.org/abs/2606.17627)

**<font color=#1a73e8>作者：</font>** Alessandro Sottovia, Alessandro Torcinovich, Oswald Lanz  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained action recognition in egocentric video is challenging for Vision-Language Models (VLMs): actions often differ only in small visual cues, and a single model tends to be biased toward a subset of these cues. We propose Divide, Deliberate, Decide, a fully-local, zero-shot multi-agent framework in which (i) a VLM orchestrator chunks the video and proposes a top-k candidate label list per segment, (ii) an ensemble of heterogeneous VLM specialists, drawn from different open model families, engages in a structured deliberation that includes a peer-consultation round of questions, and (iii) agent rankings are aggregated with a Borda count and the orchestrator re-ranks its own prediction in light of the specialists' evidence. The entire pipeline runs locally with no fine-tuning. Experiments show that our method positively improves zero-shot action recognition performance over the baseline, highlighting the influence of a heterogeneous deliberation step, showing that the gain stems from decorrelated model priors rather than from additional compute.

---


### 107. [OPD-Evolver: Cultivating Holistic Agent Evolver via On-Policy Distillation](https://arxiv.org/abs/2606.17628)

**<font color=#1a73e8>作者：</font>** Guibin Zhang, Xun Xu, Yanwei Yue 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Memory has become a standard substrate for self-evolving agents, yet retaining experience is not the same as learning how to evolve through it. Existing memory agents can store trajectories, retrieve reflections, or accumulate skills, but often lack the holistic competence to select useful experience, act on it, write reusable knowledge, and maintain a growing repository. We introduce OPD-Evolver, a slow-fast co-evolution framework that cultivates such an agent evolver through on-policy self-distillation. In the fast loop, OPD-Evolver interacts with a four-level memory hierarchy to read, use, write, and maintain experience for rapid test-time evolution. In the slow loop, outcome-calibrated memory attribution and privileged hindsight distill these four abilities into the deployable policy. Across multi-domain benchmarks, OPD-Evolver surpasses memory systems such as ReasoningBank by up to 11.5%, and training-based methods such as Skill0 by ~5.8%. Further analysis shows that OPD-Evolver internalizes high-value experience and memory management, enabling OPD-Evolver-9B to challenge giant counterparts such as Qwen3.5-397B-A17B and Step-3.5-Flash, pointing beyond memory-augmented agents toward genuinely qualified agent evolvers.

---


### 108. [AdaPT: Adaptive Lesson Plan Transformer for Cross-Regional and Differentiated Instruction](https://arxiv.org/abs/2606.17633)

**<font color=#1a73e8>作者：</font>** Yanjie Zhang, Jiajun Zhu, Minyu Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Due to educational inequality, high-quality lesson plans often mismatch the needs of disparate educational contexts. Teachers typically modify existing lesson plans to fit new contexts, but current tools instead focus on generating content from scratch, creating additional workload. Moreover, a critical gap remains in supporting teachers to quickly adapt to new learning profiles. To bridge these gaps, we present AdaPT, a system leverages LLMs to support transformation of existing lesson plans for cross-regional and differentiated instruction. AdaPT features an interactive interface that allows teachers to input student profiles, offers structured lesson representation, provides explanations for lesson-plan transformations, automatically adapts lesson content for new contexts, and supports iterative, teacher-in-the-loop refinement. We evaluated AdaPT through a user study with 9 teachers and an expert evaluation with 3 specialists. Results show that AdaPT supports workflows of teachers and offers a promising pathway toward promoting educational equity.

---


### 109. [Bounding Box Label Propagation for Re-Annotation of Document Layout Analysis Datasets](https://arxiv.org/abs/2606.17644)

**<font color=#1a73e8>作者：</font>** Nick Jochum, Tobias Alt-Veit, Christian Schön 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Datasets in practical document processing scenarios typically grow over time, and their class annotations undergo continuous refinement. This creates significant re-annotation efforts, which are time-consuming and costly. A promising remedy is to re-annotate only a small subset of available documents manually and apply semi-supervised learning techniques that leverage both labelled and unlabelled data. Although there are numerous approaches to tackle this problem for classification, there exists no adaptation for the problem of re-classifying object detection instances, e.g. for document layout analysis. To this end, we propose Bounding Box Label Propagation (BBLP), a pseudo-labelling framework for object detection. An object encoder integrates visual, textual, and positional embeddings from object detection samples to come up with a joint embedding that can be used for Label Propagation on partially annotated datasets in a plug-and-play fashion. Evaluation results indicate that the proposed approach produces high-quality class annotations of bounding boxes. In the D4LA layout analysis dataset, it achieves a mAP of 54.0%, corresponding to 81.6% of fully supervised performance, while using only 10% labelled data. Our work demonstrates the potential of Label Propagation for object detection and lays the groundwork for reducing manual annotation efforts in real-world document processing applications.

---


### 110. [SketchXplain: Intuitive Visual Explanations of Image Classifiers with Sketches](https://arxiv.org/abs/2606.17646)

**<font color=#1a73e8>作者：</font>** Wencan Zhang, Mario Michelessa, Xuejun Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Saliency map visualizations explain image-based AI predictions by pointing to regions, but these are often unintuitive and semantically unclear, leaving an interpretability gap. We argue that AI explanations should be intuitive -- coherent to user knowledge, yet simple and selective to accelerate interpretation. Inspired by artistic drawings, we propose SketchXplain to generate sketch-based visual explanations for intuitive image-based explainable AI (XAI). Combining techniques in saliency maps, concept-bottleneck models, and sketch optimization, SketchXplain integrates saliency to select coherent observation artifacts, concepts for knowledge coherence, cues to represent them, and abstraction for simplicity. Evaluating on face expression recognition, modeling and user studies showed that SketchXplain supported quicker interpretation with more aligned visualizations than saliency maps or simple drawings. Further evaluation on skin lesion diagnosis found that SketchXplain more coherently visualized disease symptoms, better supporting lay diagnosis. Thus, this work illustrates the value of sketches for intuitive, simple, coherent, and quick image-based XAI visualizations.

---


### 111. [MambaCount: Efficient Text-guided Open-vocabulary Object Counting with Spatial Sparse State Space Duality Block](https://arxiv.org/abs/2606.17650)

**<font color=#1a73e8>作者：</font>** Hao-Yuan Ma, Li Zhang, Minjie Qiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-guided Open-vocabulary Object Counting (TOOC) aims to estimate the number of objects described by text prompts, which is particularly challenging in dense scenes with large scale variations. Existing TOOC approaches predominantly rely on Transformers, whose quadratic complexity with respect to image resolution limits their scalability. Mamba offers a promising alternative due to its linear complexity. However, previous Mamba-based methods have two main limitations. On the one hand, the inherent causal formulation of Mamba constrains the bidirectional spatial dependency modeling required by non-causal vision tasks. On the other hand, existing Mamba-based vision models often overlook the unconstrained high entropy in the spatial token responses, which can weaken local details and high-frequency cues. To address these limitations, we propose MambaCount, an efficient framework built on the Spatial Sparse State Space Duality (S^4D) block. Specifically, we analyze and reconstruct the decay dynamics of hidden states in Mamba to alleviate the dependency constraints introduced by causal modeling. Moreover, we introduce a Spatial Token Selection (STS) sub-block to reduce the unconstrained high entropy in spatial token responses within Mamba. In addition, we design Multi-Granularity Prototypes (MGP) to identify object-like regions at different semantic levels, improving cross-modal alignment and interpretability. Extensive experiments on FSC-147 demonstrate that MambaCount achieves state-of-the-art performance among methods without secondary querying, obtaining a test MAE of 12.23, while retaining linear complexity.

---


### 112. [Physics-Constrained Neural Networks for Improved Short-Term Weather Forecasting: A Case Study over the South Pacific](https://arxiv.org/abs/2606.17659)

**<font color=#1a73e8>作者：</font>** Egor Bugaev, Fedor Buzaev, Dmitry Efremenko 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This study introduces enhancements to physics-constrained neural networks (PCNNs) that improve the accuracy and stability of hybrid short-term weather forecasting models. Building on the WeatherGFT architecture, three innovations are proposed. First, an upgraded numerical solver, combining a fifth-order weighted essentially non-oscillatory scheme (WENO-5), a beta-plane approximation, and subgrid-scale viscosity, permits a fourfold increase in the integration time step to 1200 s while reducing the daily mean squared error by up to 26%. Second, a unified autoregressive hybrid block replaces the original chain of 24 specialised modules, eliminating overfitting to specific lead times. Third, the physical core is integrated with two state-of-the-art neural backbones, resulting in PI-PredFormer and PI-IAM4VP. Evaluation on the WeatherBench South Pacific subset from 2000 to 2004 shows that these hybrids reduce root mean squared error at 1-12 h lead times by 8-22% compared to purely neural counterparts, while better preserving physical consistency. These results demonstrate that incremental refinement of hybrid components offers a practical route toward more accurate and efficient short-range weather forecasting.

---


### 113. [Handling Feature Heterogeneity with Learnable Graph Patches](https://arxiv.org/abs/2606.17667)

**<font color=#1a73e8>作者：</font>** Yifei Sun, Yang Yang, Xiao Feng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In recent years, the rapid development of foundation models and graph pre-training technologies has spurred increasing interest in constructing a universal pre-trained graph model or Graph Foundation Model (GFM). However, a significant challenge is that existing models are unable to address feature heterogeneity in graph data without textual information, which hinders the transferability of graph models across different datasets. To bridge this gap, we propose the concept of learnable graph patches, which we regard as the smallest semantic units of any graph data. We decompose the graph into learnable graph patches by unfolding the node features and constructing corresponding patch structures separately. We then design a framework that mines transferable information from graph data across domains. Specifically, after extracting graph patches, we propose a patch encoder to extract knowledge from each unit and a patch aggregator to learn how the units are combined into a whole. Due to its domain-agnostic nature, the model can be applied to downstream data across different domains. Furthermore, we analyze the connection between our method and existing graph models, as well as the transferability of the node embeddings it generates. Empirically, our method not only achieves the capability to use multi-domain graphs for pre-training, but also shows enhanced performance across various downstream datasets and tasks. Moreover, we observe consistent improvement in downstream performance as the volume of pre-training data increases.

---


### 114. [ASTEROID: A Spatiotemporal Information Transformer for Forecasting Multi-Step Time Series of Molecular Dynamics](https://arxiv.org/abs/2606.17668)

**<font color=#1a73e8>作者：</font>** Kexin Wu, Luonan Chen, Renxiao Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecular dynamics (MD) simulation is computationally demanding, particularly for large-scale systems requiring long-term analysis. Accurate forecast of the outcomes of a MD simulation is not only an attractive scientific challenge but also has substantial practical value. In this work, we developed a data-driven framework, termed ASTEROID (Advanced Spatiotemporal TransformER fOr Inferring Dynamics), that can directly predict multi-step atomic coordinates, avoiding conventional iterative integration. For this purpose, our ASTEROID reformulates MD trajectories as high-dimensional spatiotemporal sequences and integrates the Spatiotemporal Information (STI) Transformation equation into a Transformer architecture. The core innovation of ASTEROID lies in its ability to model multiscale spatiotemporal dependencies. In particular, for spatial dependencies, a local-global self-attention mechanism captures both short- and long-range interactions. For temporal dependencies, an encoder-decoder structure integrates global context with autoregressive forecasting. ASTEROID was evaluated on several quantum-mechanics derived molecular datasets. Our results indicate that ASTEROID achieved not only a higher level of accuracy in multi-step prediction than existing methods on various benchmarks, but also significantly reduced computational cost of conventional MD simulation. Moreover, the model supports iterative multi-step forecasting over an extended time scale. This work establishes a robust and generalizable data-driven paradigm for accelerating MD simulations.

---


### 115. [Do We Really Need Diffusion? A Fast U-Net for Paired Medical Image Translation](https://arxiv.org/abs/2606.17675)

**<font color=#1a73e8>作者：</font>** Alicia Pirwass, Birte Glimm, Michael Munz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Magnetic resonance imaging-signal fat fraction (MRI-SFF) quantifies tissue fat and serves as an established biomarker for metabolic and musculoskeletal disorders. The acquisition requires, however, specialized MRI sequences, which are not available routinely. We investigate whether SFF can be estimated from widely available T2-weighted (T2w) MRI via image-to-image translation (I2I). We further compare a lightweight 4-level U-Net to a state-of-the-art Denoising Diffusion Probabilistic Model (DDPM) using a dataset of 230 048 paired 2D images (183 517 train, 23 621 val, 22 910 test) from the German National Cohort (NAKO). Both models clearly outperform the identity baseline (Pearson correlation r = 0.769, mean absolute error MAE = 0.070 +/- 0.054), which confirms that the models learn a non-trivial cross-modal mapping. Interestingly, the lightweight U-Net outperforms the DDPM in both correlation (r = 0.975 vs. 0.962) and error (MAE = 0.014 +/- 0.015 vs. 0.019 +/- 0.019), while reducing inference time by a factor of 208 (25.2 ms vs. 5 227.2 ms per image using 50 Denoising Diffusion Implicit Model (DDIM) steps). The strong clinical performance at substantially reduced computational cost enables real-time clinical use.

---


### 116. [SuCo: Sufficiency-guided Continuous Adaptive Reasoning](https://arxiv.org/abs/2606.17687)

**<font color=#1a73e8>作者：</font>** Jiahao Wang, Bingyu Liang, Chenhao Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite remarkable performance on complex tasks, Large Reasoning Models (LRMs) often generate excessively long Chain-of-Thoughts (CoT), inflating computational costs even for simple queries. Existing efforts to mitigate this inefficiency typically rely on discrete reasoning modes or fixed budget tiers, lacking a principled criterion of when reasoning is sufficient. In this work, we introduce Minimal Sufficient CoT (MSC), defined as the shortest prefix of a CoT trajectory which is adequate for producing the correct answer. We empirically show that MSC not only reduces reasoning tokens, but also improves accuracy across difficulty levels. Building on MSC, we propose Sufficiency-guided Continuous Adaptive Reasoning (SuCo), a two-stage training framework for autonomous reasoning control along a continuous spectrum. In stage 1, MSC-Aligned Fine-Tuning (MFT) constructs MSC data using problem-adaptive sufficiency thresholds that naturally scale with question difficulty, then fine-tunes the model to internalize concise yet sufficient reasoning patterns. In stage 2, Sufficiency-Aware Policy Optimization (SAPO) further optimizes the model through reinforcement learning with dynamic complexity tracking and sufficiency-aware rewards that penalize both over- and under-thinking. Extensive experiments across mathematics, code, and science benchmarks show that SuCo consistently achieves improvements in both accuracy and reasoning efficiency.

---


### 117. [Delta-Based Target Reformulation for Short-Term Electricity Load Forecasting Using LSTM and Transformer Models](https://arxiv.org/abs/2606.17692)

**<font color=#1a73e8>作者：</font>** Vansh Bansal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate short-term electricity load forecasting is critical for the reliable and economic operation of modern power systems, under non-stationarity arising from weather variability, calendar effects, and evolving consumption patterns. While deep learning models such as LSTMs and Transformers show promising performance, most existing studies focus on direct absolute load prediction without explicitly addressing target non-stationarity.
Motivated by classical time-series differencing techniques in ARIMA models, this paper investigates a delta-based target reformulation for short-term electricity load forecasting using deep learning. Instead of directly predicting absolute load values, the proposed formulation trains models to predict the change in load between consecutive time steps, with final forecasts reconstructed using the last observed load. This aims to stabilize the learning target and reduce forecasting difficulty.
Using multi-year, hourly real-world electricity load data from India, augmented with meteorological variables from the NASA POWER project and calendar features, this study evaluates LSTM and Transformer models under both formulations, benchmarking them against LightGBM. Experiments are conducted for hour-ahead and day-ahead horizons, assessing performance via Mean Absolute Error (MAE) and Mean Absolute Percentage Error (MAPE).
Results show that delta-based reformulation consistently improves forecasting accuracy for hour-ahead prediction across all evaluated models, yielding MAPE reductions of over 50% compared to absolute formulations. For day-ahead forecasting, delta targets specifically benefit deep sequence models (LSTM and Transformer), while LightGBM remains competitive under the absolute formulation. These findings indicate that while delta reformulation is a powerful inductive bias for neural networks, its efficacy is model- and horizon-dependent.

---


### 118. [EComAgentBench: Benchmarking Shopping Agents on Long-Horizon Tasks with Distributed Hidden Intent](https://arxiv.org/abs/2606.17698)

**<font color=#1a73e8>作者：</font>** Zeyao Du, Tong Li, Haibo Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As LLM-based shopping agents enter production, existing benchmarks fail to capture how a shopper's requirements arrive: stated implicitly in the query, recorded in a profile, or revealed only when the right question is asked. Benchmarks that expose full intent upfront and grade only the final choice can neither pose this long-horizon challenge nor explain which requirement an agent missed. To address this gap, we introduce EComAgentBench, a benchmark of 662 tasks grounded in real Amazon products and reviews. Each task scatters these requirements across a visible query, a tool-gated profile, and scripted clarification; an agent must uncover hidden intent, verify candidates against attributes and review evidence, and commit to a single product within 100 tool calls. Moreover, typed, source-tagged rubrics grade every task, attributing each failure to a requirement and its source. Construction is automated yet reliable, with every answer fixed in code before any text is generated and every sample validated. Our evaluation of seven models reveals that even the strongest attains only 57.1% overall accuracy, and rubric satisfaction degrades from visible to hidden sources. Overall, we believe EComAgentBench will serve as a reproducible foundation for moving shopping agents from single-query search toward dependable assistance over long horizons.

---


### 119. [Confusion-Aware Transfer Teacher Curriculum Learning Framework: Disentangling Scoring and Pacing Effects](https://arxiv.org/abs/2606.17706)

**<font color=#1a73e8>作者：</font>** Savini Kommalage, Sanka Mohottala, Asiri Gawesha 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Curriculum learning couples two design choices, how samples are scored by difficulty and how harder samples are paced into training, making it difficult to attribute observed gains to either component. We disentangle these factors with two evaluation protocols: stage-wise test subsets that validate scoring functions independently of curriculum training, and a baseline that applies the same pacing schedule to randomly ordered data. Within the Transfer Teacher framework (TTF), we use these protocols to evaluate a confusion-aware difficulty score that considers both correct-class confidence and the probability distribution over incorrect classes. On CIFAR-10 with ResNet-18 and VGG-16, the proposed score produces model-interpretable difficulty rankings that align with human intuition. However, at full data, neither curriculum nor anti-curriculum ordering improves accuracy over standard training, indicating that improving the scoring function alone is insufficient to overcome the known failure modes of curriculum learning in TTF. In contrast, We find that confusion-aware curriculum ordering result in consistent data-efficiency benefits, outperforming random ordering by up to 8.7% points at the 20% data regime, suggesting the potential of TTF as a data-efficient training method.

---


### 120. [Structured Adversarial Camouflage via Voronoi Diagrams](https://arxiv.org/abs/2606.17711)

**<font color=#1a73e8>作者：</font>** Jens Bayer, Stefan Becker, David Münch 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pixel-wise adversarial patches are computationally heavy and often visually detectable, limiting utility in security-critical systems. We present adversarial Voronoi camouflage that optimizes only seed-point locations under fixed, printable palettes using a soft assignment, producing structured, splinter camouflage-like patterns without additional regularization. Evaluated on person detection with COCO-style AP@[.5:.95], naive placement (Inria -> COCO) performs comparably bad, while garment-level application via segmentation mask (3DPeople) results in a significant AP drop. The attack transfers to out-of-domain backgrounds and across detector families (YOLOv9/10/11/12), indicating robustness in black-box settings. Repainting with different palettes largely nullifies the effect, and single-color tweaks show limited tolerance (<=0.17), highlighting a structure-palette coupling. The parameter-efficient, palette-constrained design improves visual plausibility while degrading real-time detector performance. Physical validation and color calibration are left for future work.
Code: this https URL
This paper was originally presented at the International Conference on Military Communication and Information Systems (ICMCIS), organized by the Information Systems Technology (IST) Scientific and Technical Committee, IST-224-RSY - the ICMCIS, held in Bath, United Kingdom, 12-13 May 2026.

---


### 121. [Heterogeneous SAR-optical fusion for near-real-time land use and land cover mapping under cloud contamination: A novel framework and global benchmark dataset](https://arxiv.org/abs/2606.17713)

**<font color=#1a73e8>作者：</font>** Jiangong Xu, Weibao Xue, Xiaoyu Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optical remote sensing imagery is frequently degraded by cloud and cloud-shadow contamination, which limits its reliability for near-real-time land use and land cover (LULC) mapping. Although synthetic aperture radar (SAR) can provide cloud-penetrating structural information, existing SAR-optical fusion methods often assume reliable optical observations and insufficiently address the semantic uncertainty introduced by cloud contamination. To address this issue, we propose CloudLULC-Net, an end-to-end heterogeneous SAR-optical fusion framework that directly predicts LULC maps from cloud-contaminated Sentinel-2 imagery and temporally adjacent Sentinel-1 SAR observations. The proposed network incorporates optical reliability modulation to suppress unreliable optical responses, heterogeneous information adaptive aggregation to model high-order spatial-channel interactions between optical and SAR representations, and a unified semantic mapping transformer to organize fused features in a LULC-oriented latent space. A semantic anchor-guided optimization strategy is further introduced to improve the consistency of intermediate semantic representations. To support this task, we construct CloudLULC-Set, a large-scale benchmark dataset containing 40,223 curated SAR-optical-label triplets with pixel-level LULC annotations across diverse geographic regions and cloud conditions. Experimental results show that CloudLULC-Net achieves an OA of 86.60%, an F1-score of 83.29%, and an mIoU of 73.51%, outperforming representative heterogeneous reconstruction-first and end-to-end SAR-optical mapping methods. Comparisons with existing global LULC products and analyses under different cloud-cover levels further demonstrate the robustness and practical value of CloudLULC-Net for target-date LULC mapping in cloud-prone this http URL project is publicly available at: this https URL

---


### 122. [GSPan: A Continuous Gaussian Primitive Representation for Arbitrary-Scale Pansharpening](https://arxiv.org/abs/2606.17722)

**<font color=#1a73e8>作者：</font>** Fangyi Li, Xiaoyuan Yang, Yixiao Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pansharpening aims to generate high-resolution multispectral (HRMS) images by fusing low-resolution multispectral (LRMS) and panchromatic (PAN) observations. Most existing deep learning methods treat pansharpening as fixed-grid prediction, which limits scale adaptation. To address this, we propose GSPan, a framework that introduces 2D Gaussian Splatting (GS) into pansharpening. Instead of directly predicting pixels, GSPan represents band-wise residual details as continuous and learnable 2D Gaussian primitives. We design a Dual-Stream Hierarchical Interaction (DSHI) architecture with a Spatial-Spectral Interactive Attention (SSIA) module to estimate these primitives from complementary PAN and MS observations. The predicted primitives are rendered as a residual detail field and injected into the upsampled MS image. This continuous representation allows GSPan to render fused images on arbitrary target sampling grids without scale-specific retraining. It further enables a Scale-Decoupled Asymmetric Inference (SDAI) strategy, which estimates primitives at a reduced resolution and renders the fused image at the target resolution for efficient large-scene pansharpening. Experiments on QuickBird, GaoFen-2, WorldView-3, and WorldView-3-4K datasets show that GSPan delivers state-of-the-art fusion performance. Moreover, SDAI markedly accelerates inference, achieving a favorable trade-off between computational efficiency and fusion quality. Our results demonstrate the potential of continuous Gaussian residual representations as a flexible and scale-decoupled alternative to fixed-grid prediction.

---


### 123. [LongWebBench: Evaluating Structural and Functional Webpage Generation in Long-Horizon Settings](https://arxiv.org/abs/2606.17727)

**<font color=#1a73e8>作者：</font>** Yi Zhao, Zhen Yang, Mengpan Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent vision-language models (VLMs) have shown promising progress in generating webpages from visual inputs, yet existing evaluations mainly focus on short, single-screen, and largely static webpages. We introduce LongWebBench, a benchmark for evaluating long-horizon webpage generation from both structural and functional perspectives. LongWebBench contains 490 real-world long webpages for structural fidelity evaluation and 507 goal-oriented interaction tasks over 129 webpages for functional evaluation. It employs two complementary protocols: a multi-dimensional VLM-based metric for assessing long-range structural coherence, and a DOM-augmented agent-based pipeline for end-to-end functional verification. We further examine the automatic evaluation protocols through human agreement analysis. Experiments with state-of-the-art open-source and proprietary VLMs under single-image and multi-image settings reveal that structural fidelity degrades as webpage length increases, while visually plausible generations often fail to support executable multi-step interactions. These results highlight the need to evaluate long webpage generation beyond visual similarity, with executable interaction as a core criterion. Our code and data are available at this https URL.

---


### 124. [BrainWorld: A Structural-Prior-Conditioned Generative Model for Whole-Brain 4D fMRI Dynamics](https://arxiv.org/abs/2606.17742)

**<font color=#1a73e8>作者：</font>** Junfeng Xia, Wenhao Ye, Junxiang Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Whole-brain 4D fMRI generation is valuable for modeling functional brain dynamics, yet existing fMRI foundation models mainly target representation learning and downstream prediction rather than conditional predictive generation. We introduce BrainWorld, a structural-prior-conditioned generative model for whole-brain 4D fMRI dynamics. BrainWorld uses sMRI as subject-level anatomical context to guide future fMRI generation, integrating structural information into the denoising process rather than treating it as a parallel modality. Evaluated on 22 datasets spanning diverse cohorts and brain states, BrainWorld generates stable 4D fMRI trajectories up to 400 frames, improves downstream performance through generated-example augmentation, and learns transferable multimodal representations that outperform baselines. Together, these results establish BrainWorld as a condition-aware generative framework for long-horizon brain dynamics modeling and multimodal representation learning.

---


### 125. [A fairness-aware extension of Stochastic Multicriteria Acceptability Analysis for ranking](https://arxiv.org/abs/2606.17756)

**<font color=#1a73e8>作者：</font>** Guilherme Dean Pelegrina, Renata Pelissari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fairness has become a central concern in ranking problems involving individuals or social groups, particularly under the Responsible Artificial Intelligence agenda. In Multi-Criteria Decision Analysis, Stochastic Multicriteria Acceptability Analysis (SMAA) provides a robust framework for handling uncertainty and incomplete preference information, but it does not explicitly address fairness in the resulting rankings. This paper proposes SMAA-Fair, a fairness-aware extension of SMAA for ranking problems. The approach reweights the simulated rankings generated by SMAA according to their level of group fairness, so that fairer rankings contribute more strongly to the acceptability indices and central weights vector. The framework is independent of the aggregation model and can incorporate different fairness metrics. In this study, Statistical Parity, normalized discounted Kullback--Leibler divergence (rKL) and normalized discounted cumulative Kullback--Leibler divergence (nDKL) are adopted. Rankings are derived from the fairness-adjusted acceptability matrix using expected ranking and maximum acceptability ranking. We also derive the central weight according to the degree of fairness in the obtained rankings. Numerical experiments with synthetic and real data show that SMAA-Fair improves the representation of protected groups among favourable ranking positions, while preserving robustness to preference uncertainty.

---


### 126. [Talking to Your Data: Exploring Embodied Conversation as an Interface for Personal Health Reflection](https://arxiv.org/abs/2606.17767)

**<font color=#1a73e8>作者：</font>** Nikola Kovacevic, Bastien Husler, Di Zhuang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Personal health data from wearables are typically presented through dashboards of charts and summary statistics, requiring users to actively interpret patterns and implications. We explore an alternative interaction paradigm: engaging with personal health data through an embodied conversational agent that facilitates objective data reflection in dialogue with the user. We present a system that combines lightweight preprocessing of wearable data with a Unity-based embodied character. Internally, the system follows a dual-agent design in which an Observer agent extracts descriptive statistics and temporal trends, and a Presenter agent communicates these findings through "spoken statistics," intentionally refraining from clinical advice to isolate the impact of the interaction modality. We evaluate this approach through a simulated-self user study (N=5) using a within-subject design. Participants adopted health personas and goals derived from the LifeSnaps dataset to compare traditional dashboard exploration with embodied conversational reflection. Our evaluation focuses on perceived understanding, the specificity of generated actions, and the cognitive shift from passive viewing to active sensemaking. The paper contributes a functional prototype, a design pattern for objective health data narrative generation, and early empirical insights into how embodiment affects the interpretation of personal health metrics.

---


### 127. [Blind Recovery of Latent Domains via Unsupervised Symmetry Discovery](https://arxiv.org/abs/2606.17782)

**<font color=#1a73e8>作者：</font>** Onur Efe, Arkadas Ozakin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Primary motivation in blind inverse problems is to recover signals of interest from corrupted observations without knowing the obfuscating mechanism. Blind deconvolution is a prominent approach when the corruption is convolutional, but it is not applicable when general linear transformations obfuscate the domain structure. In this work, we propose an unsupervised framework for recovering latent domains and signals by discovering symmetries of the data distribution. Our framework models observations as linear measurements of signals sampled from a latent random field, and optimizes a shallow group-convolutional network by imposing stationarity and locality regularization at the model output. The model learns a latent symmetry action and an appropriate filter, thereby mapping unstructured observations to a symmetry-based representation that reveals latent signals. Experiments on stochastic processes, Ising models, shuffled and bit-scrambled images, and neural recordings show that the method recovers latent domains and signals from unstructured observations, suggesting symmetry discovery as a new direction for unsupervised structure learning and blind inverse problems.

---


### 128. [Is It Real? Exploiting Virtual-Physical Discrimination Vulnerability in Mixed Reality](https://arxiv.org/abs/2606.17783)

**<font color=#1a73e8>作者：</font>** Xueyang Wang, Xihuan Yao, Yanming Xiu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Consumer mixed reality (MR) headsets seamlessly blend virtual content into physical environments with sufficient fidelity that users may be unable to distinguish virtual objects from physical ones. We identify this virtual-physical discrimination vulnerability as an exploitable security primitive. Through speculative design workshops with 12 experts from cybersecurity and MR/HCI, we develop a taxonomy of virtual-physical confusion attacks and implement four proof-of-concept attacks on Apple Vision Pro, evaluating them with 26 participants in realistic MR tasks. All four attacks altered user behavior, with success rates ranging from 85% to 100%, producing misdirected interactions, misjudged object identities, biased purchasing decisions, and altered navigation paths. Notably, the most successful attacks were also the hardest to detect according to participants' subjective ratings. Even participants who recognized virtual content still complied behaviorally, and no participant attributed anomalous events to adversarial causes. We propose platform-level provenance, interaction gating, and user education as countermeasures.

---


### 129. [Toward Accessible Psychotherapy Training Using AI-Driven Interactive Patient Avatars](https://arxiv.org/abs/2606.17786)

**<font color=#1a73e8>作者：</font>** Pascal Riachi, Sofie Kamber, Stella Brogna 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Training psychotherapists in evidence-based interventions such as Acceptance and Commitment Therapy (ACT) requires repeated practice with meaningful feedback, yet opportunities for safe, standardized training are limited by ethical, logistical, and resource constraints. We introduce a system designed to support ACT-oriented psychotherapy training through spoken dialogue with an embodied virtual patient. The system uses large language models to simulate patient behavior conditioned on profiles derived from real therapy sessions and configurable clinical scenarios, while a separate automated evaluator provides turn-by-turn feedback on therapist responses based on established ACT fidelity criteria. Rather than aiming to replace supervision, the system is intended to support deliberate practice by enabling experimentation, reflection, and immediate feedback in low-risk settings. Expert evaluation with practicing psychologists confirmed high realism in patient behavior and demonstrated that immediate turn-by-turn ACT feedback increased therapists' awareness of intervention choices and enabled effective experimentation with alternative responses. Quantitative evaluation across 49 therapy transcripts identified GPT-4o-mini as the optimal feedback model, achieving the lowest mean absolute error (MAE = 6.12) in replicating human supervisor ACT fidelity ratings with statistically significant agreement. This work demonstrates the potential of fidelity-aware simulated patients as a scalable complement to psychotherapy training.

---


### 130. [Continual Self-Improvement with Lightweight Experiential Latent Memories](https://arxiv.org/abs/2606.17803)

**<font color=#1a73e8>作者：</font>** Vaggelis Dorovatas, Nancy Kalaj, Rahaf Aljundi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models achieve strong reasoning performance by scaling inference-time compute, yet remain fundamentally stateless, discarding the rich, self-produced reasoning traces generated during this process. We investigate whether models can instead learn online from this experience, converting transient computation (reasoning traces) into persistent reusable knowledge, and without external supervision or access to future data. We show that In-Context Learning (ICL) over raw reasoning traces fails to generalize, reflecting a fundamental limitation of token-level reuse: individual traces lack the abstraction needed for transfer, even after refinement (e.g. self-reflection). In contrast, drawing inspiration from recent works on unsupervised reinforcement learning, we find that lightweight per-instance training with self-generated test-time signals (majority voting) as rewards yields substantial gains, often surpassing full-dataset offline training, motivating a shift from raw traces to learned latent representations. Building on this insight, we propose an online method that distills inference-time compute spent on encountered problems into compact modular latent memories capturing the underlying reasoning structure. These memories are stored and retrieved for future inputs, enabling continual improvement while avoiding catastrophic forgetting through modular design. Importantly, our method is highly efficient, parametrized as extremely lightweight soft prompt memories (~0.001% of model parameters) and trained with only a few gradient steps, yet achieving performance competitive with full parametric updates and offline training. Across challenging mathematical reasoning benchmarks, our approach significantly outperforms zero-shot and raw data ICL baselines, while transferring effectively across datasets.

---


### 131. [QueryMarket: Cost-Aware Online Active Learning in Data Markets](https://arxiv.org/abs/2606.17805)

**<font color=#1a73e8>作者：</font>** Xiwen Huang, Pierre Pinson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data acquisition is a major bottleneck for learning in real-time streams: analysts must decide on the fly which labels to purchase while respecting a rolling budget. However, existing online active learning rarely unifies pricing, information gain, and rolling budget constraints under concept drift. We introduce QueryMarket, a market-inspired framework that queries each incoming data point based on its estimated utility to the model and its price. Within this framework, we propose OVBAL (online variance-based active learning), which integrates data pricing with information-driven selection by estimating each sample's marginal utility via a D-optimality criterion with exponential forgetting and executing cost-aware purchases under rolling budget constraints. OVBAL yields a simple, fully online decision rule that adapts to nonstationary streams and heterogeneous label costs. Experiments on synthetic data and a real-world solar power generation forecasting task show that OVBAL is particularly effective under seller-centric pricing and yields a more favorable long-run error-cost trade-off in the real-world task under both pricing schemes.

---


### 132. [No-Free-Fairness: Fundamental Limits and Trade-offs in Learning Systems](https://arxiv.org/abs/2606.17810)

**<font color=#1a73e8>作者：</font>** Khoat Than  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we establish a set of theoretical impossibility results, termed the No-Free-Fairness theorems, that identify three fundamental sources of disparity in learning systems. First, we show that when a task exhibits irreducible cost on a subgroup, any decision rule must trade off overall performance with disparity, yielding an inherent fairness--cost frontier. Second, we prove that even in ideal, noise-free settings where a perfectly fair and accurate solution exists, finite-sample learning alone induces nontrivial subgroup disparity, ruling out distribution-free fairness guarantees. More seriously, enforcing strict relative fairness creates a statistical bottleneck: achieving low cost may require exponentially many samples. Third, we show that limitations of the model class can independently induce disparity: if the model cannot represent accurate solutions for a subgroup, fairness remains unattainable regardless of data or training procedure. Overall, these results demonstrate that unfairness is not solely a consequence of biased data or suboptimal optimization, but arises from the intrinsic structure of decision problems, the constraints of finite data, and the expressivity of models. Our framework applies broadly beyond standard supervised learning, and suggests that achieving fairness requires explicit trade-offs and should be treated as a core design consideration.

---


### 133. [Beyond Native Success: Auditing Deployment-Interface Exposure of CLIP Backdoors](https://arxiv.org/abs/2606.17815)

**<font color=#1a73e8>作者：</font>** Kunlan Xiang, Haomiao Yang, Wenbo Jiang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Contrastive Language-Image Pre-training models are widely reused across downstream interfaces, including feature extraction, retrieval, reranking, and selection. Existing CLIP backdoor, however, usually validate attacks on a small attack-native task, leaving unclear whether the same poisoned checkpoint remains exposed, weakens, or becomes not applicable when reused through other interfaces. We introduce DIFE, a Deployment-Interface Footprint Evaluation framework that audits backdoored CLIP checkpoints across deployment interfaces. DIFE makes various evaluations comparable by specifying each interface's component readout, trigger channel, target event, reference condition, and metric. DIFE also introduces effective-footprint diagnosis to identify the reusable CLIP component or component combination that carries exposure and explains where risk transfers. Auditing reproduced CLIP backdoors with DIFE reveals a structured landscape: native success is not a checkpoint-level risk certificate, exposure follows component footprints, text-side poisoning does not yield textual-encoder control, and some coupled attacks remain mechanism-bound. This audit reveals a import gapin existing CLIP backdoors: a textual encoder that itself becomes a reusable carrier of adversarial behavior. We therefore introduce BadTextTower to fill this gap. BadTextTower produces strong text-conditioned retrieval, reranking, and selection exposure while leaving visual-only reuse nearly clean.

---


### 134. [Conservation Laws for Modern Neural Architectures](https://arxiv.org/abs/2606.17816)

**<font color=#1a73e8>作者：</font>** Viet-Hoang Tran, Vinh Khanh Bui, Tan Lai Ngoc 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding gradient descent dynamics is key to explaining the success of over-parameterized models, where implicit bias manifests through conservation laws in gradient flow. While such laws are well understood for linear and ReLU networks, they remain largely unexplored for modern architectures. This work develops a unified framework to characterize conservation laws for contemporary models, including feedforward networks with GELU, SiLU, and SwiGLU activations, multihead attention with sinusoidal and rotary positional encodings, and Mixture-of-Experts architectures under diverse gating designs. Our theoretical findings are supported by experiments that validate the predicted invariants.

---


### 135. [Human-in-the-Loop Atlas-Based 3D Asset Segmentation for Interactive Content Workflows](https://arxiv.org/abs/2606.17824)

**<font color=#1a73e8>作者：</font>** Paul Julius Kühn, Saptarshi Neil Sinha, Jakob Hansen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Segmenting 3D assets into meaningful regions remains challenging, especially when segmentation criteria are application-dependent and require user control. We present a human-in-the-loop pipeline for generating a segmented 2D parameterized atlas from a 3D model for interactive media, game, and XR content workflows. Our method first selects a compact set of rendered views using a greedy set cover strategy over sampled surface points, and then supports interactive segmentation of these views with SAM~2 and Label Studio. The resulting masks are back-projected onto the model's UV parameterization to produce a unified segmented atlas that supports downstream production tasks such as segment-wise material assignment, style transfer, and semantic labeling. We assess the pipeline through a demonstration-based technical evaluation on eight cultural heritage objects. The results show that the approach can generate usable segmented atlases across diverse geometries while revealing recurring sources of manual correction, particularly fine structures, cavities, and weak appearance boundaries.

---


### 136. [When Multiple Scripts Matter: Evaluating ASR in Clinical Settings](https://arxiv.org/abs/2606.17826)

**<font color=#1a73e8>作者：</font>** Jean Seo, Minkyu Kim, Jeonguk Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic speech recognition (ASR) in non-English clinical settings is challenged by multiscript variability, where the same term may appear in multiple valid orthographic forms. Conventional string-matching evaluation metrics often underestimate ASR performance by treating orthographic variants as errors. To address this issue, we introduce MultiClin, a clinical ASR benchmark designed to evaluate robustness to multiscript variability. Experiments across diverse ASR models show that multiscript-aware evaluation provides a fairer assessment of recognition quality than conventional single-reference evaluation. We further investigate the impact of script consistency during training and find that inconsistent script mappings increase orthographic uncertainty and hinder model convergence, with a balanced 50% mapping ratio producing the highest entropy. In contrast, script unification consistently yields the best ASR performance. Our dataset and code are publicly available at: this https URL.

---


### 137. [Functional Equivalence in Attention: A Comprehensive Study with Applications to Linear Mode Connectivity](https://arxiv.org/abs/2606.17830)

**<font color=#1a73e8>作者：</font>** Viet-Hoang Tran, Vinh Khanh Bui, Van-Hoan Trinh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural network parameter spaces are inherently non-injective, as distinct parameter configurations can realize identical functions through functional equivalence. While this symmetry is well understood in classical fully connected and convolutional models, it becomes substantially more intricate in modern attention-based architectures. Existing analyses of multihead attention have largely focused on the vanilla formulation, overlooking positional encodings that fundamentally reshape architectural symmetries. In this work, we provide a formal study of functional equivalence in Transformers with positional encodings. Focusing on the two most widely used variants--sinusoidal and rotary positional encodings (RoPE)--we show that sinusoidal encodings preserve the equivalence structure of vanilla attention, whereas rotary encodings significantly reduce the symmetry group, thereby enhancing expressivity. This offers a principled explanation for the growing prominence of RoPE in practice. We further examine how positional encodings affect linear mode connectivity, and through an alignment algorithm, empirically demonstrate that the presence and variability of connectivity across Transformer settings crucially depend on the positional encoding.

---


### 138. [Perceptual compensation for tonal context in self-supervised speech models](https://arxiv.org/abs/2606.17835)

**<font color=#1a73e8>作者：</font>** James Kirby, Ioana Krehan, Michele Gubian  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study examines the extent to which the wav2vec2.0 architecture exhibits evidence of compensation for phonological context. We conducted a pseudo-replication of a perceptional compensation experiment on Mandarin Chinese tones, and compared the embedding similarities and probing classifier outputs between a purely self-supervised pre-trained model and a model fine-tuned for Mandarin ASR. No evidence of compensation was found in the embedding similarities of the purely pre-trained model. Probing classifiers showed some evidence of compensation in addition to the expected layer-wise improvements in categorization, but failed to replicate human performance on isolated test syllables. Our findings contrast with previous reports of sensitivity to phonological structure emerging through pre-training alone, and suggest that supervised objectives may be necessary to encourage the abstraction of at least some types of phonological regularities.

---


### 139. [High-Fidelity 3D Geometric Reconstruction of Pelvic Organs from MRI: A Hybrid Deep Learning and Iterative Optimization Approach](https://arxiv.org/abs/2606.17836)

**<font color=#1a73e8>作者：</font>** Hui Wang, Xiaowei Li, Chenxin Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Patient-specific 3D reconstruction of pelvic organ geometry from MRI is important for pelvic floor modeling and downstream patient-specific analysis. However, while previous studies have focused primarily on either image segmentation or downstream use of 3D models, the reconstruction of high-fidelity, high-quality geometries remains labor-intensive and poorly standardized. The study introduced a hybrid deformable shape modeling framework that integrates deep learning prediction with iterative optimization for the reconstruction of the bladder, uterus, and rectum. The framework consists of three core components: a geometry-aware multi-level deep learning architecture that preserves topological consistency of pelvic organs; a two-stage amortized optimization training strategy that balances global shape capture and local surface refinement; and a holistic synergy mechanism--where iterative optimization provides supervision for deep learning during the training phase, and during inference, deep learning rapidly predicts the global organ morphology, followed by iterative optimization to refine local surfaces and mesh quality. This framework demonstrated marked superiority in geometric fidelity than current mainstream deep learning-based organ reconstruction models. For individual anatomical structures, the reconstructed 3D geometries for the bladder, rectum, and uterus achieved significantly lower Chamfer Distance values and higher Dice Similarity Coefficient scores. In addition, while maintaining high computational efficiency, the proposed architecture yielded superior overall volumetric mesh quality. At the patient level, the framework achieved higher mean values for the 10 worst elements for both minSICN and minSIGE compared to traditional geometric post-processing algorithms.

---


### 140. [WallZero: Mastering the Game of WallGo with Strategic Analysis](https://arxiv.org/abs/2606.17847)

**<font color=#1a73e8>作者：</font>** Hsing-Yu Chen, Jérôme Arjonilla, I-Chen Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> WallGo is a recently introduced strategic board game popularized by the 2025 Netflix series The Devil's Plan. Although played on a small 7 x 7 board, its combination of stone movement and wall placement yields high game-tree complexity and intricate strategic interactions. Despite its growing popularity, WallGo remains underexplored. This paper presents WallZero, an AlphaZero-based agent for the two-player WallGo setting. We introduce tailored action and feature designs to improve playing performance significantly. In the evaluation, WallZero defeats two professional Go players who participated in this study, securing on average 1.98x more territory per game. Beyond its strength, we use WallZero to assess game fairness and identify key strategies for mastering WallGo. Interestingly, our results show that the opening used in the Netflix series yields a more balanced game. Our code is available at this https URL.

---


### 141. [A homotopy-type-theoretic generalization of neurosymbolic inference](https://arxiv.org/abs/2606.17851)

**<font color=#1a73e8>作者：</font>** Fernando Zhapa-Camacho, Robert Hoehndorf  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A wide range of neurosymbolic (NeSy) systems compute one functional: a belief-weighted sum of a logical quantity over a space of $\sigma$-structures, of which weighted model counting, fuzzy logic, and probabilistic logic are special cases. This account is built on sets, and a set deliberately forgets two things that are important for NeSy: when two $\sigma$-structures are the same up to a symmetry of the theory, and how many distinct proofs witness a query. Replacing the underlying sets by types, in the sense of homotopy type theory, preserves this information, and turns this functional into a belief-weighted homotopy cardinality, a notion of size that counts each object in inverse proportion to its symmetries. We develop the framework from scratch for NeSy systems, prove a conservativity theorem that recovers the classical functional when symmetries are trivial, and show that the symmetry our framework exposes is exactly the one behind reasoning shortcuts. The payoff is concrete: the shortcut-aware concept posterior that recent methods reach by ensembling or expressive density estimation is the only symmetry-invariant point of the confusion-set simplex, computable in closed form by averaging a single model over the symmetry group. On MNIST reasoning-shortcut benchmarks this single-model wrapper is better calibrated than a diversity-trained ensemble, while leaving label accuracy and identifiable concepts untouched. Code is freely available at this https URL.

---


### 142. [Meta-classification of one-class classification models using ranking correlation and nearest neighbor](https://arxiv.org/abs/2606.17858)

**<font color=#1a73e8>作者：</font>** Toshitaka Hayashi, Hamido Fujita, Dalibor Cimr 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine Learning (ML) techniques have been applied to various problems. However, applying ML to ML models is an unexplored direction. For this purpose, this paper considers a meta-classification of one-class classification (OCC) models, because all ML models could be approximated as OCC models. The proposal represents OCC models as normality rankings and classifies them using nearest-neighbor and ranking-correlation metrics. The experiment classifies OCC models, where classes correspond to training datasets, algorithms, and hyperparameters. The proposal achieves high accuracy when class labels are datasets. Moreover, it can classify algorithms when the training datasets contain the same class. In addition, the discussion highlights that the classification of OCC models is essentially the classification of datasets that treats multiple samples as a single input. The experiment demonstrates the classification of datasets using sleeping records. The proposed method can provide a unified solution for classifying OCC models, datasets, and rankings. Source code is uploaded to the public repository this https URL.

---


### 143. [GameCraft-Bench: Can Agents Build Playable Games End-to-End in a Real Game Engine?](https://arxiv.org/abs/2606.17861)

**<font color=#1a73e8>作者：</font>** Tongxu Luo, Rongsheng Wang, Jiaxi Bi 等 25 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Game generation is an emerging application of coding agents, requiring models to transform natural-language specifications into playable interactive systems. Unlike traditional coding tasks, game generation takes place within a game engine, where scripts, scenes, assets, rendering, and runtime interactions must jointly produce coherent gameplay. We formalize end-to-end game generation as the problem of producing a complete game artifact that realizes a specification through observable player-game interaction in a target environment. We argue that evaluating this setting requires three desiderata: Engine Grounding, Artifact Completeness, and Interactive Verification. We propose an interaction-grounded evaluation framework that assesses executable gameplay through replayed demonstrations and rubric-guided multimodal judging. We instantiate this framework as GameCraft-Bench, a benchmark comprising 140 Godot tasks across 15 game families. Evaluations of frontier coding agents show that end-to-end game generation remains highly challenging: the strongest agent achieves only 41.46%, and most agents score below 40%. Further analysis reveals that while agents often implement recognizable mechanics, they struggle to deliver complete games with sufficient content, functional visual feedback, and coherent presentation. See this https URL for demos, code, and data.

---


### 144. [Revisiting Structural Dependency in Autoregressive Multi-Task Table Recognition via Order-Independent Cell-Level Representations](https://arxiv.org/abs/2606.17874)

**<font color=#1a73e8>作者：</font>** Takaya Kawakatsu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-task table recognition jointly addresses table structure prediction, cell localization, and cell content recognition within a unified framework. Existing approaches often rely on autoregressive decoders to generate table structures and reuse their hidden states for cell localization and content recognition. This autoregressive generation process can make cell representations order-dependent, degrading global consistency across cells. This paper proposes a structural refinement module that produces order-independent cell features through non-causal attention. This design enables parallel inference of cell contents while conditioning each cell on global context encoded in the refined features. Experiments on two large datasets demonstrate consistent gains in cell localization and end-to-end recognition, while reducing overall inference time by around threefold.

---


### 145. [Structural Preservation and the Logical Expressiveness of Graph Neural Networks](https://arxiv.org/abs/2606.17882)

**<font color=#1a73e8>作者：</font>** Przemysław Andrzej Wałęga, Bernardo Cuenca Grau  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Bridges between graph neural networks (GNNs) and logical formalisms have been established by fixing architectural choices, such as the types of aggregation, combination, and activation functions. These choices define restricted classes of GNNs for which tight correspondences with logical formalisms can be obtained, by showing that logical formulae can be translated into equivalent GNNs and, conversely, that GNNs can be translated into equivalent formulae.
In this paper we take a semantic perspective by establishing the logical expressiveness of classes of GNN classifiers that are preserved under structural properties: embeddings (extensions), injective homomorphisms, and homomorphisms. We show that, for each such property, there exists a fragment of graded modal logic characterising the class of GNNs. In particular, preservation under embeddings, injective homomorphisms, and homomorphisms corresponds to existential graded modal logic, its existential-positive fragment, and existential-positive modal logic, respectively. These results characterise the expressiveness of broad classes of GNNs independently of specific architectural choices, but we also show that each of these classes admits a GNN architecture of the same expressiveness.
Technically, our approach uses a new well-quasi-order result for trees of bounded height, yielding finite representations of unravelling-invariant classes.

---


### 146. [Monotonic Kolmogorov-Arnold Networks: A Theoretical and Empirical Study of Monotonicity as an Inductive Bias](https://arxiv.org/abs/2606.17886)

**<font color=#1a73e8>作者：</font>** Mikhail Krasnov, Carolina Fortuna, Blaž Bertalanič  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Monotonicity has been a long-running architectural inductive bias for neural networks, motivated by tabular, scientific, and economic settings where outputs are known to respond monotonically to certain inputs. Existing approaches are MLP- or flow-based and lack per-edge functional transparency; the only Kolmogorov--Arnold Network (KAN) variant with monotonicity, MonoKAN, enforces the constraint only on a restricted parameter subset and requires a projection-style training procedure. We close this gap with \textbf{MKAN}, a KAN with hard monotonicity guaranteed for \emph{all} parameter values via exponential reparameterization of B-spline coefficients, positive edge weights, and a monotone base activation. Training reduces to standard unconstrained gradient descent. Our headline theoretical contribution is a \emph{representation-cost} theorem: any $C^K, K >0$ feature extractor inducing a ball-shaped semantic-neighborhood partition admits a monotone realization of the equivalent neighborhood structure at $N' = N^* + k \le 2N^*$, where $k$ is the number of non-monotone coordinates of the original. The bound is architecture-agnostic and gives a principled sizing rule for monotone encoders. Empirically, MKAN is competitive with state-of-the-art monotone NNs on the SMM/ICML-2024 benchmark while being the only method that combines hard unconstrained monotonicity with KAN's per-edge functional transparency; the $2N^*$ prediction is validated in a self-supervised feature-size sweep on four real datasets, and on a controlled monotone-generative dataset MKAN recovers ground-truth factors with substantially higher Spearman alignment than KAN, MLP, and linear baselines.

---


### 147. [AI Adoption Across a Multinational Workforce: Sociotechnical Conditions for GenAI Acceptance in Human Resources](https://arxiv.org/abs/2606.17887)

**<font color=#1a73e8>作者：</font>** Dalia Ali, Maria José Rodríguez Velázquez, Manoel Horta Ribeiro 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI (GenAI) deployment in the workplace is accelerating rapidly. Nevertheless, questions of who adopts, who benefits, and who is left behind and why are still understudied. In this paper, we investigate these dynamics in the context of a multinational tech company transitioning from a legacy Human Resources (HR) search system to a GenAI-supported system, analyzing search log data, survey data (n=25), and ten semi-structured interviews. Our findings show that adoption depended on the fit between the GenAI system's design assumptions and employees' work positionalities (role, spoken language, tenure). Further, we find that employees' trust in GenAI answers was built through source-checking, comparison among systems, and seeking input from colleagues or HR when in doubt. Our contribution is twofold. First, we provide empirical evidence of workplace GenAI adoption during a live organizational transition, showing that adoption is influenced by factors such as situational fit, search literacy, and trust calibration. It is also further shaped by knowledge conditions such as the system's content quality, employee training, and guidance. Second, we translate these findings into design considerations for inclusive deployment and adoption in high-stakes environments such as HR. We argue that organizations should design systems considering the role and context-sensitive benefits they yield to different social groups. They also need to treat the organizational knowledge infrastructure as AI infrastructure to improve the accountability and usability of GenAI systems

---


### 148. [Dimensionality Controls When Modularity Helps in Continual Learning](https://arxiv.org/abs/2606.17889)

**<font color=#1a73e8>作者：</font>** Kathrin Korte, Christian Medeiros Adriano, Joachim Winther Pedersen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Compositional learning systems must balance plasticity, the ability to acquire new knowledge, with stability, the preservation of previously learned components, especially when tasks share structure and risk interference. We study how modular architecture, task similarity, and representational dimensionality jointly shape compositional continual learning in a sequential A-B-A paradigm, comparing a task-partitioned recurrent network to a single-network baseline while inducing high- and low-dimensional regimes via weight-scale manipulations. In a high-dimensional "lazy" regime, both architectures achieve similar performance and internal geometry, suggesting that explicit modular structure has little impact when representations are weakly constrained. In a lower-dimensional "rich" regime, modularity becomes decisive: the modular network develops graded task-specific subspaces that overlap for similar tasks, partially align for moderately dissimilar tasks, and separate for dissimilar tasks, yielding a more compositional and interpretable organization than the single network. These findings identify the representational regime induced by initialization scale, which co-varies with representational dimensionality, as a key factor governing when compositional, modular structure is functionally beneficial in continual learning, and support viewing safety and robustness as problems of adaptive allocation of representational subspaces rather than fixed separation versus sharing.

---


### 149. [Learn to Quantify Social Interaction with Constraints for Pedestrian Walking](https://arxiv.org/abs/2606.17897)

**<font color=#1a73e8>作者：</font>** Xiaodan Shi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term human path forecasting in crowds is critical for autonomous moving platforms (like autonomous driving cars and social robots) to avoid collision and make high-quality planning. Although the current research take into account social interactions for prediction, they don't reveal the exact kinds of social interactions happened among people and how the social interactions affect the decision-making process of pedestrians, which further limits its robustness. Social interactions in pedestrian walking are intuitively massive and hard to label and quantify. In this paper, we explore creatively to quantify and interpret how pedestrians interact with others by proposing Learn to Cluster. Our clustering social interactions is probabilistic latent variable generative, learning directly from sequential trajectory observations, scalable to arbitrary number of pedestrians. Learn to cluster is label-free and can be naturally integrated into the training process of the prediction model. The latent variables will then serve as 'labels' to categorize social interactions. Extensive experiments over several trajectory prediction benchmarks demonstrate that our method is able to learn the patterns of social interactions and effectively integrate the patterns to pedestrian trajectory prediction.

---


### 150. [ChLogic: Evaluating Robustness of Logical Reasoning in Chinese Expressions](https://arxiv.org/abs/2606.17905)

**<font color=#1a73e8>作者：</font>** Peixian Zhou, Yuxu Chen, Chaorui Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models perform increasingly well on standardized logical reasoning benchmarks, but whether this ability remains robust beyond English is unclear. We introduce ChLogic, an English--Chinese aligned benchmark that tests whether models preserve logical reasoning performance when the same latent logical structure is expressed in English and diverse Chinese surface realizations. Built from formal logical templates, the benchmark contains three data sets: (i) the General aligned set, derived from 60 General Propositions across nine template families; (ii) the Difficult aligned set, derived from 40 Difficult Problems; and (iii) the Chinese-only set, covering 15 language-specific phenomenon types. Each aligned item pairs one English reference expression with five Chinese realizations. Experiments on Qwen3, Ministral, and GLM models reveal a persistent English--Chinese performance gap. Back-translation from standard Chinese into English often improves performance on the General aligned set, but produces mixed effects on the Difficult aligned set, where Qwen3-32B and GLM-5.1 perform worse after translation. These results indicate that Chinese surface realization, translation artifacts, and model-specific behavior jointly affect multilingual logical reasoning. Overall, ChLogic provides a useful stress test for the robustness of multilingual reasoning.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-205](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
