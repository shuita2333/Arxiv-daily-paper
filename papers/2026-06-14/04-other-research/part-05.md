# 📦 其他研究 | 2026年06月14日

> 本类共 **251** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-251](./part-06.md)

---

### 201. [Uncertainty Estimation for Molecular Diffusion Models](https://arxiv.org/abs/2606.13451)

**<font color=#1a73e8>作者：</font>** Paul Seij, Christian A. Naesseth, Stephan Mandt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models have seen wide adoption for 3D molecular generation, yet they offer no principled signal of when a generated molecule is likely to be of low quality. We propose a post-hoc method for estimating per-sample uncertainty in pretrained molecular diffusion models. Building on a Laplace approximation of the denoising network, we measure the variability of the noise prediction across the generation trajectory. Empirically, we show that the resulting uncertainty score is informative of sample quality, exhibiting a negative correlation with established sample-level quality metrics. We further study how the proposed uncertainty score can be used to filter generated samples, improving model performance via test-time scaling.

---


### 202. [Reinforcement Learning for Neural Model Editing](https://arxiv.org/abs/2606.13461)

**<font color=#1a73e8>作者：</font>** Shaivi Malik  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Editing pretrained neural networks requires specialized algorithms tailored to specific objectives. Designing such algorithms is often time-consuming and demands significant effort. We present an exploratory framework that formulates neural model editing as a reinforcement learning problem, where agents modify models using reward feedback. We introduce two environments: MaskWorld, where agents scale weights multiplicatively, and ShiftWorld, where agents apply additive weight updates. The reward function combines a utility-preservation objective with a task-specific editing objective, enabling agents to learn targeted modifications while maintaining overall model performance. We evaluate the framework on bias mitigation in text classification and machine unlearning in image classification, both of which traditionally rely on specialized algorithms. Our results show that the learned policies reduce forget set accuracy to nearly 0% while preserving over 90% retain set accuracy on the unlearning task. In the bias mitigation setting, the learned policies improve bias-related performance by more than 5% while maintaining general classification utility. Our findings show that neural model editing can be cast as a reinforcement learning problem, allowing editing policies to be learned from reward feedback rather than manually engineered for each task.

---


### 203. [Ontology Memory-Augmented ASR Correction for Long Text-Speech Interleaved Conversations](https://arxiv.org/abs/2606.13464)

**<font color=#1a73e8>作者：</font>** Xinxin Li, Huiyao Chen, Meishan Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic speech recognition (ASR) correction has traditionally focused on isolated utterances or short local contexts. However, as text and speech become increasingly interleaved in long interactions, ASR correction requires conversation-level contextual evidence. Existing ASR correction methods often rely on the current hypothesis or concatenate raw dialogue history. In such contexts, sparse correction evidence can be difficult to locate amid redundancy and noise. Addressing these challenges, we propose an ontology memory-augmented ASR correction framework for long text-speech interleaved conversations. The framework organizes preceding interaction history into a dynamically updatable ontology memory, where entities, terminology, surface variants, potential ASR confusions, and semantic relations are stored as retrievable nodes for context-grounded correction. To evaluate this setting, we construct RAMC-Corr, a dataset derived from MAGIC-RAMC for long-range ASR correction with grounded context. Experiments on RAMC-Corr show that our method improves over direct correction in 9 out of 10 paired backbone-setting combinations and encourages more selective and evidence-grounded corrections for context-dependent ASR errors.

---


### 204. [MaxProof: Scaling Mathematical Proof with Generative-Verifier RL and Population-Level Test-Time Scaling](https://arxiv.org/abs/2606.13473)

**<font color=#1a73e8>作者：</font>** Jiacheng Chen, Xinyu Zhang, Shunkai Zhang 等 23 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present MaxProof, a population-level test-time scaling framework for competition-level mathematical proof in the MiniMax-M3 series. M3 first trains three proof-oriented capabilities -- proof generation, proof verification, and critique-conditioned proof repair -- using a defense-in-depth generative verifier engineered for low false-positive rate. These capabilities are merged into a single released M3 model. At test time, MaxProof treats the model as a generator, verifier, refiner, and ranker, searches over a population of candidate proofs, and returns one final proof through tournament selection. With MaxProof test-time scaling, the M3 model reaches 35/42 on IMO 2025 and 36/42 on USAMO 2026, exceeding the human gold-medal threshold on both.

---


### 205. [SupraBench: A Benchmark for Supramolecular Chemistry](https://arxiv.org/abs/2606.13477)

**<font color=#1a73e8>作者：</font>** Tianyi Ma, Yijun Ma, Zehong Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Supramolecular chemistry, which includes the study of non-covalent host-guest assemblies, has advanced various applications. However, designing host-guest systems remains time-consuming, requiring days of dry-lab verification per candidate pair. Although LLMs have emerged as a fast alternative with strong performance on molecular binding tasks, no benchmark currently systematically evaluates LLMs for host-guest reasoning across fundamental supramolecular chemistry tasks, e.g., binding affinity prediction. To this end, we collaborate with domain experts to release the first Supramolecular Benchmark, called SupraBench, to evaluate LLMs in chemistry reasoning. Specifically, we design four fundamental tasks, i.e., binding affinity prediction, top-binder selection, solvent identification, and host-guest description, plus an auxiliary vision-based task for molecular identification. We also release SupraPMC, a curated 16M-token corpus of Supramolecular chemistry articles distilled from Europe PMC, to support the adaptation to the supramolecular domain. We benchmark a broad range of open and proprietary LLMs and find that LLMs leave substantial headroom across all tasks. Domain adaptation pretraining over SupraPMC transfers cleanly to in-distribution regression but trades off against strict letter-format output. Moreover, the difficulty profile differs sharply across task families, revealing distinct failure modes that indicate specific gaps in current supramolecular chemistry reasoning. Our source codes and benchmark datasets are available at this https URL.

---


### 206. [CRAFTIIF: Cross-Resolution Analytic Four-Type Interpretable Isolation Forest for Multivariate Time Series Anomaly Detection](https://arxiv.org/abs/2606.13486)

**<font color=#1a73e8>作者：</font>** William Smits  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Anomaly detection in multivariate time series is challenged by four structurally distinct anomaly types -- point (isolated spikes), distributional (level shifts), temporal (rhythm changes), and collective (inter-sensor correlation breakdowns) -- each requiring different feature representations. Most unsupervised methods target only one or two types and provide limited interpretability. We present CRAFTIIF (Cross-Resolution Analytic Four-Type Interpretable Isolation Forest), a fully unsupervised framework targeting all four types without dataset-specific tuning. CRAFTIIF generates K=500 random analytic wavelet feature draws across four families (Morlet, DOG, Haar, Coiflet), each targeting a specific anomaly type, feeding five structured Isolation Forests -- one per type plus a meta-IF for compound anomalies. An adaptive Otsu/MAD threshold calibrates detection automatically across anomaly rates from 0.1% to 69.2%. Because each IF is trained exclusively on type-specific features, branch firing provides direct anomaly-type attribution by construction, without post-hoc explanation. Evaluated on all 19 datasets of the mTSBench benchmark (Zhou et al., TMLR 2026), CRAFTIIF achieves mean F1=0.228 (all 19 datasets) and F1=0.322 (13 detectable datasets), ranking first among all 25 evaluated methods on VUS-PR (0.463 vs. previous best 0.329, +40.7%). A diagnostic framework -- oracle F1, detectability limits, and branch separation ratios -- identifies 6 of 19 datasets as fundamentally undetectable by any unsupervised method. Ablation over 11 conditions confirms adaptive thresholding (+38% F1), four-branch structure (+20%), and meta-IF (+23%) are each essential. Code: this https URL

---


### 207. [Point-Wise Geometry-Aware Transformer for Partial-to-Full Point Cloud Registration in Computer-Assisted Surgery](https://arxiv.org/abs/2606.13488)

**<font color=#1a73e8>作者：</font>** Siyu Zhou, Zhongliang Jiang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Partial-to-full registration remains challenging due to varying overlap ratios, fluctuating point densities, and the presence of noise. While transformers have shown strong potential for point cloud processing, prior methods typically confine them to global context aggregation, overlooking fine-grained local geometry crucial for accurate correspondence. We propose \emph{GAPR-Net}, a learning-based point cloud registration framework with a coarse-to-fine architecture that combines convolution and transformer modules, in which local and global information is fused between the partial and full point clouds using a cross-attention mechanism. To achieve this, a transformation-invariant point-wise geometric feature representation is proposed, which can robustly capture relative geometric features for individual points with respect to their neighboring points. To evaluate the effectiveness of the proposed approach, experiments are conducted on four geometrically distinct bones, including the tibia, femur, pelvis, and thoracic cartilage. The overall registration recall reaches 94.2\%, the method results in a low RMSE of 1.992 mm and $R^2$ values of 0.908 and 0.974 for rotation and translation, respectively. The results demonstrate that the proposed method effectively addresses the partial-to-full point cloud registration problem. The proposed method enables highly accurate 3D point cloud registration using partial observation, providing a critical foundation for precise surgical navigation and robotic interventions in computer-assisted surgery. The code will be accessed after the double-blind review process.

---


### 208. [Budget-Constrained Step-Level Diffusion Caching](https://arxiv.org/abs/2606.13496)

**<font color=#1a73e8>作者：</font>** Mingkun Lei, Tong Zhao, Liangyu Yuan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Step-level caching accelerates diffusion models by exploiting temporal redundancy across denoising steps. Existing methods make per-step cache decisions using threshold-based heuristics, without directly optimizing for final output quality. As a result, their inference latency varies across inputs and is difficult to control at deployment. In this work, we propose BudCache, which inverts this formulation: rather than letting per-step error thresholds dictate the runtime cost, we fix the compute budget in advance and search for the cache policy that best preserves the final output. To tackle the combinatorial complexity of step selection, we combine Simulated Annealing with deterministic Hill Climbing. This offline search identifies high-quality cache policies within minutes and introduces no online search or thresholding overhead during inference. When the compute budget is very tight, we further introduce cache-aware schedule alignment, which adapts the time discretization to the selected cache policy to reduce cache-induced trajectory mismatch. Experiments on FLUX.1-dev and Wan2.1 show that BudCache achieves better generation quality than heuristic caching baselines under the same inference budgets. Code is available at this https URL

---


### 209. [Heterogeneous LiDAR Early Fusion and Learned Re-Ranking Strategy for Robust Long-Term Place Recognition in Unstructured Environments](https://arxiv.org/abs/2606.13503)

**<font color=#1a73e8>作者：</font>** Judith Vilella-Cantos, Juan José Cabrera, Mónica Ballesta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robust localization in unstructured environments, such as agricultural fields, is a critical challenge for autonomous systems. LiDAR sensors provide detailed 3D information about the environment and are invariant to lighting conditions. For this reason, LiDAR-based place recognition methods have gained significant attention. In this paper, we propose MinkUNeXt-VINE++, a novel approach that combines early fusion of heterogeneous LiDAR data from two sensors (Livox Mid-360 and Velodyne VLP-16) and a learned re-ranking strategy in inference time. This fusion leverages the strengths of each sensor to provide a more comprehensive representation of the environment. Additionally, the re-ranking approach is particularly important in repetitive environments, such as vineyards, as finding true positives is a major challenge. We evaluated our approach using the TEMPO-VINE dataset, which provides heterogeneous LiDAR data in vineyard environments across different phenological stages. Our results demonstrate that MinkUNeXt-VINE++ significantly improves place recognition performance compared to single-sensor approaches and state-of-the-art methods. MinkUNeXt-VINE++ achieves a 20% improvement in the Recall@1 metric compared to single-sensor approaches, and +30% including re-ranking. The code of our method is publicly available for reproduction.

---


### 210. [Measurement-Calibrated Multi-Camera Fusion for Vision-Based Indoor Localization](https://arxiv.org/abs/2606.13509)

**<font color=#1a73e8>作者：</font>** Mateo Toro Diz, Jonathan Hoss, Noah Klarmann  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Indoor vision-based localization systems are affected by detection noise, occlusions, and limited camera coverage, leading to uncertainty at multiple stages of the pipeline. While multi-camera data fusion is widely used to mitigate these issues, it is typically treated as a black-box component and evaluated solely end-to-end, obscuring its mechanistic contributions. To address this gap, this work investigates whether explicitly characterizing single-camera localization errors can be leveraged to calibrate and optimize multi-camera data fusion.
We introduce a measurement-calibrated fusion approach that integrates component-wise error quantification, specifically isolating homography calibration, human detection, and motion tracking. A component-wise evaluation is conducted to quantify error contributions from homography calibration, human detection, and motion tracking.
Experimental results show that data fusion improves localization accuracy compared to single-camera baselines. While measurement-calibrated fusion provides only limited improvement in absolute accuracy over standard fusion, it substantially reduces trajectory variance and improves motion smoothness, which are critical for applications requiring stable and continuous motion estimates. These results highlight the value of explicit error characterization when designing data fusion strategies for vision-based indoor positioning systems.

---


### 211. [CloudCons: A Comprehensive End-to-End Benchmark for Cloud Resource Consolidation](https://arxiv.org/abs/2606.13513)

**<font color=#1a73e8>作者：</font>** Xiaobin Zhang, Lefei Shen, Mouxiang Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Driven by conservative over-provisioning to guarantee service reliability, resource utilization in cloud data centers remains at low levels. To mitigate this, the forecast-then-optimize paradigm has emerged to optimize consolidation by anticipating future demands. While emerging time series foundation models promise to enhance this paradigm through zero-shot generalization, existing benchmarks focus solely on prediction error metrics. The actual decision utility of these advanced models remains unverified, rendering their practical value for downstream tasks uncertain. To bridge this gap, we propose CloudCons, a comprehensive end-to-end benchmark designed to evaluate forecasting models within the specific context of cloud resource consolidation. We build high-quality datasets that cover diverse workloads from Huawei Cloud, Microsoft Azure, and Google Borg, capturing distinct service characteristics ranging from synchronized diurnal rhythms to stochastic, pulse-like bursts and high-frequency noise. We conduct an extensive evaluation of statistical, deep learning, and foundation models. Our experiments reveal a pivotal finding: while foundation models demonstrate superior zero-shot forecasting accuracy, this advantage does not inherently translate into better decision utility. Of practical significance, we systematically analyze how the selection of predictive quantiles acts as a critical lever. We provide actionable guidelines for calibrating these selections to balance the trade-off between resource efficiency and service reliability, offering vital insights for real-world deployment decisions.

---


### 212. [MaskWAM: Unifying Mask Prompting and Prediction for World-Action Models](https://arxiv.org/abs/2606.13515)

**<font color=#1a73e8>作者：</font>** Hanyang Yu, Haitao Lin, Jingbo Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World Action Models (WAMs) present a promising paradigm for robotic control via video prediction. However, current WAMs suffer from fundamental spatial bottlenecks: standard text inputs introduce referential ambiguity in cluttered scenes, while unstructured RGB predictions lack semantic grounding and remain biased by task-irrelevant backgrounds. To overcome these limitations, we introduce MaskWAM, an object-centric world-action model. By jointly integrating masks as both explicit inputs and predictions via a unified Mixture of Transformers (MoT), MaskWAM unlocks robust policy generalization. This design provides two key benefits: (1) predicting future masks yields object-centric semantic supervision that suppresses visual noise, significantly enhancing even standard text-conditioned WAMs; and (2) coupling this predictive supervision with first-frame visual prompts, such as target object masks, establishes a precise spatial anchor that substantially reduces language ambiguity. Crucially, as WAMs are inherently vision-driven architectures, direct mask conditioning yields substantially stronger guidance than text alone, establishing a precise and robust paradigm for manipulating unseen objects. Evaluations on LIBERO, RoboTwin, and real-world tasks demonstrate that MaskWAM significantly outperforms baselines in both language-clear and language-ambiguous tasks.

---


### 213. [What's Old is New Again: Classical Dimensionality Reduction for Efficient Saliency-Guided Biometric Attack Detection](https://arxiv.org/abs/2606.13528)

**<font color=#1a73e8>作者：</font>** Samuel Webster, Walter Scheirer  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Saliency-guided training is a paradigm in visual recognition that encourages models to focus on the most relevant image regions during learning. While its application in biometric presentation attack detection (PAD) has shown strong benefits in robustness and generalization, adoption is often limited by the high cost, domain specificity, and limited scalability of existing saliency acquisition methods, such as human annotations over a limited dataset. We present a novel, cost-efficient, and highly-scalable approach to saliency acquisition using maps inspired by classical dimensionality reduction techniques: PCA and LDA. Our proposed methods generate saliency maps directly from raw training data, requiring no human annotation nor domain knowledge. We contextualize the effectiveness of these saliency sources in three saliency-explored domains (iris PAD, synthetic face detection, fingerprint PAD) and demonstrate its scalability in two saliency-novel domains (fingerprint vein PAD and ID card PAD). Across all domains tested, models trained using dimensionality reduction-sourced saliency maps exceed baseline and sometimes SOTA saliency methods without any resource investment or domain-specific tooling. Our findings overcome an important yet unaddressed barrier to saliency-guided training for biometric attack detection and beyond.

---


### 214. [Ride, Track, and Recover: Pilot Randomized Trial of a Wearable Digital Self-Management Intervention During a Veteran Endurance-Cycling Program](https://arxiv.org/abs/2606.13529)

**<font color=#1a73e8>作者：</font>** Alan Ta, Nilsu Salgin, Caleb Armstrong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Post-traumatic stress disorder (PTSD) in veterans is characterized by persistent hyperarousal and comorbid anxiety and depressive symptoms that are difficult to monitor and manage outside clinical settings. Thirteen veterans participating in a Project Hero cycling event in Texas were randomized by computer-generated sequence in a naturalistic setting to two arms: (1) digital intervention plus physical activity, or (2) physical activity only, plus a third at-home monitoring control cohort consisting of 7 veterans selected from the broader Project Hero veteran community. Continuous smartwatch sensing combined heart rate and accelerometer features to detect hyperarousal events, which were confirmed in real time by participants. Weekly self-report measures of anxiety, depression, and PTSD severity were collected. Generalized additive mixed models characterized nonlinear trajectories over time. Baseline-normalized hyperarousal trajectories differed significantly across conditions, with the digital intervention group (n=7) showing structured stabilization compared to late-study escalation in the physical-only group (n=3). Both cycling groups exhibited acute symptom improvements during the endurance event; however, the digital intervention group demonstrated a higher overall maintenance of gains. The at-home control group (n=4) showed gradual symptom declines. Perceived precision of ML detections varied substantially across individuals and was positively associated with symptom severity, with higher-severity participants confirming a greater proportion of detected events. These results suggest that coupling wearable detection with digital self-management tools may support stabilization of hyperarousal and symptom improvement while emphasizing the importance of personalization and human-centered design in wearable mental health systems.

---


### 215. [When Does Mixing Help? Analyzing Query Embedding Interpolation in Multilingual Dense Retrieval](https://arxiv.org/abs/2606.13537)

**<font color=#1a73e8>作者：</font>** Tongyao Zhu, Chao-Ming Huang, Min-Yen Kan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While mixed-language querying is ubiquitous in multilingual communities, the sensitivity of dense retrievers to such queries remains poorly understood. We present a ratio-controlled study on mMARCO that systematically evaluates retrieval performance by varying the mixing proportion of parallel query translations via embedding-level mixing -- constructing mixed queries as an interpolation of monolingual embeddings. Experiments with BGE-M3 demonstrate that an optimal mixing ratio outperforms the best monolingual endpoint in 88/105 cases. We uncover a distinct asymmetry driven by English dominance: mixing is uniformly beneficial when retrieving from non-English document indices, whereas indices containing English are best served by pure English queries. Furthermore, English acts as the strongest mixing partner for every non-English document language. Finally, when controlling for English dominance, mixing gains correlate negatively with typological distance. We conclude that language-mix sensitivity is structured and predictable, and we validate the robustness of these patterns across model families and scales.

---


### 216. [Is It You or Your Environment? A Bayesian Inference Framework for Genomically-Anchored Personalized Physiological Interpretation](https://arxiv.org/abs/2606.13556)

**<font color=#1a73e8>作者：</font>** Aruna Dey, Suraj Biswas  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personalized health AI systems face a fundamental cold-start problem: machine learning models for physiological interpretation require weeks of individual behavioral data before they can distinguish constitutional variation from environmentally driven deviation. We propose a solution grounded in causal inference and Bayesian prior design. An individual's genomic profile serves as an exogenous genetic anchor -- a domain-informed, personalized prior that is fixed at conception, immune to reverse causation, and available before a single behavioral observation is collected. The anchor initializes a Bayesian belief state over an individual's physiological set point G-hat = mu + sum(beta_i * g_i), where beta_i are GWAS-derived effect sizes and g_i are risk-allele counts. Each incoming physiological measurement P produces a non-constitutional deviation delta = P - G-hat that separates the signal attributable to environment and state from the constitutionally fixed baseline. As behavioral data accrue, the prior decays according to G-hat_t = w(t)*G-hat_genomic + [1-w(t)]*P-bar_t, transitioning from genome-dominated to empirical-baseline-dominated inference. The same observed HRV of 55 ms generates a suppression hypothesis for a person whose prior predicts 80 ms, and an enhancement hypothesis for a person whose prior predicts 30 ms -- a reversal impossible without a personalized anchor. We develop this architecture across six physiological domains, grading genomic priors by evidence strength, distinguishing robustly replicated anchors (FTO, FADS1/2, FKBP5) from contested candidate genes (SLC6A4, MAOA, DRD2). We address the inference boundary between association, Mendelian randomization, and individual token causation, and define four constraints for deployment: evidence-graded priors, dynamic decay, ancestry-matched effect sizes, and attribution rather than deterministic output.

---


### 217. [Edit the Bits, Diff the Codes: Bitwise Residual Editing for Visual Autoregressive Models](https://arxiv.org/abs/2606.13558)

**<font color=#1a73e8>作者：</font>** Shengqiang Zhang, Ruotong Liao, Volker Tresp 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-guided image editing with visual autoregressive (VAR) generators requires controlling both what the model samples and where the sampled change is written back into the image code. Existing VAR editors mainly operate on token streams, features, or flat next-token logits, leaving two native structures of bitwise-residual VAR models underused: the per-bit Bernoulli prediction head and the additive multi-scale residual code field from which the image is assembled. We propose BitResEdit, a training-free editor for bitwise-residual VAR generators such as Infinity. BitEdit performs source-negative guidance by tilting the post-CFG per-bit log-odds along a source--target contrast computed on a shared edited prefix, then projects each update into a closed-form Bernoulli-KL trust region around the clean CFG sampler. ResEdit converts the sampled bits into per-scale continuous-code residuals, gates them with a localization mask, and re-injects them through the generator's native sum-of-scales. Together they couple decision-time bit guidance with combination-time code composition, so masked-out latent features are preserved exactly by code arithmetic while localized, scale-aware edits are applied inside the target region. On PIE-Bench with Infinity-2B, BitResEdit attains the strongest text alignment among same-backbone VAR editors, improving CLIP on the edited region by +1.07 over the strongest prior editor while keeping background preservation competitive with it. Ablations show BitEdit and ResEdit play complementary roles in target alignment and background preservation.

---


### 218. [Contrast-Informed Augmentation and Domain-Adversarial Training for Adult-to-Neonatal MR Reconstruction Generalization](https://arxiv.org/abs/2606.13562)

**<font color=#1a73e8>作者：</font>** Stephen Moore, Lara Leijser, Richard Frayne 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Purpose: To investigate whether contrast-informed data augmentation and domain-adversarial training improve the adult-to-neonatal generalization of the E2E-VarNet. Methods: Three training regimes were investigated: (1) adult-only training with unaugmented adult data, (2) mixed training with paired unaugmented and neonatal-informed augmented adult data, and (3) mixed training with a domain-adversarial objective. Models were trained on retrospectively undersampled multi-coil adult T2-weighted brain MR data and evaluated on neonatal and adult test data at acceleration factors $R=4$ and $R=8$ using quantitative metrics and qualitative evaluation. Feature analyses assessed whether domain-adversarial training altered the latent representations of unaugmented adult, augmented adult, and neonatal test samples. Results: Mixed training (Mixed) and mixed domain-adversarial training (Mixed-DAT) outperformed unaugmented adult-only training (Unaug-Only) when evaluated on neonatal data. At R=4, Mixed-DAT achieved the best performance (SSIM = 0.924 +/- 0.027, PSNR = 33.98 +/- 1.15 dB). At R=8, Mixed-DAT performed best when measured using SSIM (0.848 +/- 0.031 vs. 0.766 +/- 0.037 for Unaug-Only and 0.814 +/- 0.035 for Mixed) and Mixed performed best when measured using PSNR (29.56 +/- 0.83 dB vs. 26.26 +/- 0.78 dB for Unaug-Only and 29.43 +/- 0.83 dB for Mixed-DAT). Qualitative assessment of t-SNE plots suggested that Mixed-DAT increased the overlap among the latent representations of the unaugmented adult, augmented adult, and neonatal test data. Conclusion: Contrast-informed augmentation and domain-adversarial training improved adult-to-neonatal generalization of deep learning-based MR reconstruction. These findings suggest that contrast-informed data augmentation combined with adversarial training may improve robustness to domain shift in undersampled neonatal MR reconstruction.

---


### 219. [Differentially Private Hierarchical Heavy Hitters](https://arxiv.org/abs/2606.13563)

**<font color=#1a73e8>作者：</font>** Ari Biswas, Graham Cormode, Yaron Kanza 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The task of finding _Hierarchical_ Heavy Hitters (HHH) was introduced by Cormode et al. [VLDB 2003] as a generalisation of the heavy hitter problem. While finding HHH in data streams has been studied extensively, the question of releasing HHH when the underlying data is private remains unexplored. In this paper, we study differentially private HHH release in both the streaming and non-streaming setting. In the non-streaming setting, we show the surprising result that the relative error in estimating the residual count for any prefix is independent of the height of the hierarchy and the number of heavy hitters in the stream. Meanwhile, in the streaming setting, although the exact version of HHH has low global sensitivity (as counting queries are 1-sensitive), the approximation functions due to streaming have high global sensitivity, linear in the available space. Despite this obstacle, we show that the absolute error for estimating frequencies in the steaming setting is independent of the available space.

---


### 220. [A Three-Layer Framework for AI in Scientific Discovery](https://arxiv.org/abs/2606.13566)

**<font color=#1a73e8>作者：</font>** Guojun Liao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current discussions of AI in scientific discovery are often dominated by two visible capabilities: search over existing knowledge and execution through optimization, simulation, and automation. Both are important, but neither fully captures the central act of discovery: the formation and evolution of models. This paper proposes a three-layer view of AI in discovery. Layer 1 is search and retrieval by large language models. Layer 2, as the main innovation of this paper, is model formation through qualitative reasoning: the capacity to recognize when a current framework is structurally inadequate and to understand the problem within a broader representational space, not through trial and error, but through structural insight into what is missing and where it can be found. Layer 3 is execution, optimization, and refinement. The main claim is that Layer 2 is both the most important and the least developed. Search without model formation remains confined to inherited frameworks, while execution without conceptual revision only amplifies an existing formulation. We illustrate Layer 2 reasoning through three case studies: S. S. Chern's intrinsic proof of the Gauss-Bonnet theorem, the resolution of the Nesterov Accelerated Gradient convergence problem via Lyapunov functions, and the autonomous disproof of the Erdos unit distance conjecture by OpenAI in 2026. Each case exhibits the same structural signature: a framework that had become inadequate, a missing conceptual object, and a resolution found in an unexpected neighboring field.

---


### 221. [Adjusted Cup-Product Neural Layer](https://arxiv.org/abs/2606.13568)

**<font color=#1a73e8>作者：</font>** Snigdha Chandan Khilar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many important observables in physics and geometry are cup products of cochains. The adjusted cup product neural layer has been introduced in this paper. It is a neural primitive that hard wires the cup product with an adjustment term from higher gauge theory. This creates a readout that is gauge invariant by design. Their main theoretical result shows that on a closed cycle the output relies entirely on the adjustment coefficient. Setting this coefficient to zero removes the output completely regardless of other parameters. Thus the adjustment is the only source of gauge invariant signal. They prove this observable is a nonzero quadratic form and is exactly invariant under one and two gauge transformations.

---


### 222. [Existence Precedes Value: Joint Modeling of Observational Existence and Evolving States in Time Series Forecasting](https://arxiv.org/abs/2606.13571)

**<font color=#1a73e8>作者：</font>** Yifan Hu, Hongzhou Chen, Peiyuan Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world time series are often highly incomplete and irregular due to sensor dormancy, transmission delays, and event-driven sampling, making reliable forecasting fundamentally challenging. Existing methods have evolved from impute-then-forecast pipelines to continuous-time models such as Neural ODEs and continuous-time graph networks. While these approaches improve the modeling of historical irregularity, they still rely on an implicit oracle assumption at inference time: the timestamps of future valid observations are presumed to be known in advance. This assumption limits practical relevance, since in many real systems the more fundamental question is not only what the future value will be, but also whether a valid observation will occur at all. In this paper, we propose Timeflies, a unified framework that reformulates forecasting as a joint problem of future observability inference and value estimation. To explicitly model the interaction between observation dynamics and state evolution, Timeflies adopts an observation stream and a value stream, coupled through three dedicated modules for reliability-aware embedding, observation-guided dependency modeling, and joint prediction. We further construct Shadow, a benchmark that combines natural missingness from public datasets with real-world industrial data, and introduce the Observation-Value Joint Entropy (OVJE) metric to comprehensively evaluate this coupled predictability. Extensive experiments show that Timeflies consistently outperforms existing methods, highlighting the importance of explicitly modeling future observability in time series forecasting with missing values. Code and dataset are available in this https URL.

---


### 223. [Learning with Simulators: No Regret in a Computationally Bounded World](https://arxiv.org/abs/2606.13576)

**<font color=#1a73e8>作者：</font>** Sasha Voitovych, Abhishek Shetty, Noah Golowich 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding the minimal assumptions necessary for generalization is the fundamental question in learning theory. Unfortunately, most results rely heavily on independence (or some proxy thereof) of the data-generating process, while results for strongly dependent data are far more limited. Towards addressing this gap, we introduce the framework of simulatable processes, where the learner has access to a simulator that approximates the distribution generating the data (which may be an arbitrarily complex and dependent process). Surprisingly, given access to such a simulator, we show that we can recover the same learning guarantees as in the classical setting with independent data, namely, error bounds that depend on the VC dimension. Further, we use this framework to study the power of conditional sampling and show strict statistical and computational advantages in this setting. As a highlight of our framework, we exhibit a single algorithm that simultaneously learns any given VC class under all processes samplable in bounded polynomial time, with regret controlled by the time-bounded Kolmogorov complexity of the process. This provides a significant conceptual broadening of the classical PAC model.

---


### 224. [LabVLA: Grounding Vision-Language-Action Models in Scientific Laboratories](https://arxiv.org/abs/2606.13578)

**<font color=#1a73e8>作者：</font>** Baochang Ren, Xinjie Liu, Xi Chen 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific laboratories increasingly rely on AI systems to reason about experiments, but the physical act of doing science remains largely outside their reach. AI can help read literature, generate hypotheses, and plan protocols, yet the execution of those protocols at the bench still requires a human operator. Vision-Language-Action (VLA) models provide one possible interface between written protocols and robot execution, but existing policies are trained mostly on household and tabletop demonstrations and rarely encounter the instruments, transparent liquids, or fixed protocol workflows found in scientific laboratories. Closing this gap requires both laboratory-specific supervision and a unified learning framework that can accommodate the diverse robot embodiments used to execute experimental protocols. We therefore identify data and embodiment as central bottlenecks alongside model design. To address the data side, we build RoboGenesis, a simulation-based workflow and data engine that composes configured laboratory workflows from atomic skills, validates and filters rollouts, and exports structured demonstrations across supported robot profiles. On the policy side, we present LabVLA, trained with a two-stage recipe: FAST action token pretraining first makes the Qwen3-VL-4B-Instruct backbone action aware before any continuous control is learned, and flow matching posttraining then attaches a DiT action expert under knowledge insulation. On the LabUtopia benchmark, LabVLA achieves the highest average success rate among all evaluated baselines under both in-distribution and out-of-distribution settings.

---


### 225. [EvTexture++: Event-Driven Texture Enhancement for Video Super-Resolution](https://arxiv.org/abs/2606.13580)

**<font color=#1a73e8>作者：</font>** Dachun Kai, Jiayao Lu, Yueyi Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event-based vision has drawn increasing attention owing to its distinctive properties, including ultra-high temporal resolution and extreme dynamic range. Recent works have introduced it to video super-resolution (VSR) to enhance flow estimation and temporal alignment. In contrast, this paper shifts the focus of event signals from motion refinement to texture enhancement in VSR. We propose EvTexture++, the first event-driven framework dedicated to texture enhancement in VSR. It leverages high-frequency spatiotemporal details from events to improve texture recovery. EvTexture++ incorporates a customized texture enhancement branch, along with an iterative texture enhancement module that progressively exploits high-temporal-resolution event information for texture restoration. This enables gradual refinement of texture regions across iterations, yielding more accurate and detailed high-resolution outputs. Besides intra-frame texture recovery, large motions could degrade inter-frame temporal consistency, particularly in texture regions, leading to texture flickering. To mitigate this, we further exploit the continuous-time motion cues of events to enhance temporal consistency, introducing a temporal texture alignment module that estimates event-guided texture-aware flow for precise inter-frame texture alignment. Moreover, EvTexture++ is designed as a plug-and-play tool to flexibly boost the performance of existing VSR models. Experiments on five datasets demonstrate that EvTexture++ achieves state-of-the-art performance. When integrated into recent VSR models, it yields significant improvements, with gains of up to 1.55 dB in PSNR on the texture-rich Vid4 dataset. Code: this https URL.

---


### 226. [Towards Effective Waste Segmentation for Automated Waste Recycling in Cluttered Background](https://arxiv.org/abs/2606.13587)

**<font color=#1a73e8>作者：</font>** Mamoona Javaid, Mubashir Noman, Abdul Hannan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rapid expansion of urban areas and population growth is causing an immense increase in waste production, which demands the need for efficient and automated waste management. In this scenario, automated waste recycling (AWR) using deep learning methods can assist humans in optimal waste management. Recent deep learning approaches for AWR provide promising waste segmentation performance, however, these methods rely on large backbone networks that are inefficient for AWR systems and suffer from performance deterioration in cluttered scenes. To this end, an optimal waste segmentation network is introduced which effectively utilizes the spatial domain to capture localized structural dependencies and the spectral domain to efficiently extract global contextual relationships. This cascaded design allows the network to progressively leverage both local and global representations across complementary domains to highlight the semantic information necessary for effective segmentation of various waste objects. Furthermore, auxiliary feature enhancement module (AFEM) is introduced to enhance the target objects' boundaries and blob amplification for better segmentation in cluttered scenarios. Extensive experimentation on ZeroWaste-aug, ZeroWaste-f and SpectralWaste datasets reveals the merits of the proposed method.

---


### 227. [Simplex-Constrained Sparse Bagging: Transitioning from Uniform Priors to Sparse Posteriors in Ensemble Learning](https://arxiv.org/abs/2606.13589)

**<font color=#1a73e8>作者：</font>** Meher Sai Preetam, Meher Bhaskar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present Simplex-Constrained Sparse Bagging (SCSB), a mathematically rigorous framework for post-training compression and probability calibration of bootstrap-based bagging ensembles. Standard bagging ensembles (such as Random Forests, Bagged SVMs, and Bagged Neural Networks) assign uniform voting power to all constituent estimators. However, this naive uniform prior ignores the varying local competence of base estimators and contributes to model overconfidence. We formulate ensemble pruning and calibration as a joint optimization problem over the probability simplex by minimizing the Out-Of-Bag (OOB) loss. To induce sparsity, we address the theoretical "L1-simplex paradox" -- the mathematical reality that the L1 norm is constant on the simplex and fails to prune -- by introducing a concave quadratic penalty. SCSB is model-agnostic and achieves up to 96% ensemble compression, yielding linear inference speedups and superior probability calibration (lowered Expected Calibration Error) while preserving or enhancing generalization accuracy.

---


### 228. [Multiagent Protocols with Aggregated Confidence Signals](https://arxiv.org/abs/2606.13591)

**<font color=#1a73e8>作者：</font>** Ali Elahi, Barbara Di Eugenio  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Confidence is used for reliability, oversight, and a range of downstream decision tasks in Natural Language Processing (NLP), yet no existing method produces or evaluates a confidence for the output of a multiagent system. Prior work uses confidence within multiagent debate (MAD) to weight messages, trigger debate, or calibrate individual agents, but it never aggregates these into a single confidence for the system itself. We introduce three protocols that produce a final answer along with a single aggregated confidence by first transforming raw confidence signals to make them comparable across models, then combining them via soft voting or a probability fusion we call Bayesian fusion. This aggregated confidence is substantially more discriminative (AUARC) than that of the best single agent or the standard debate baselines, while correctness (F1-score) stays stable and recovers the losses MAD incurs on more ambiguous tasks. Analyzing two estimators, sequence probability and self-report, alongside parametric and non-parametric calibrators, we find that calibration improves F1 for both estimators while AUARC is less reliant on it. We evaluate six homogeneous and heterogeneous debating pairs per benchmark, across five benchmarks and four task types, spanning a range of model capabilities and sizes.

---


### 229. [See What I See, Know What I Think: Dense Latent Communication Across Heterogeneous Agents](https://arxiv.org/abs/2606.13594)

**<font color=#1a73e8>作者：</font>** Siyi Chen, Xiaoyan Zhang, Meng Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems communicate mostly through text, paying a lossy and expensive decode and re-encode cost. KV-cache communication is a promising alternative, yet most prior work is homogeneous, using duplicate copies of the same model, and avoids the central challenge of cross-model latent alignment; existing heterogeneous methods are also restrictive, typically assuming shared input and using transferred caches mainly for steering. We study a more fundamental question: can heterogeneous agents be aligned well enough to perform real "mind reading" and transfer both what one agent sees and how it thinks? Our information-structure analysis reveals a duality: context-aware transfer is driven by sparse reasoning signals, while context-unaware transfer, where the receiver sees no input, requires dense contextual knowledge preservation. Motivated by this, we propose dense alignment for heterogeneous KV-cache communication via a lightweight cross-model cache transformation and two-phase training: reconstruction followed by generation. Across all six directions of {Qwen3-4B, 8B, 14B} and six in-domain and out-of-domain benchmarks, our method outperforms prior heterogeneous baselines, matches or exceeds text communication in context-aware settings at roughly 2 to 3 times lower compute, and remains effective in context-unaware transfer where prior methods collapse.

---


### 230. [EpiBench: Verifiable Evaluation of AI Agents on Epigenomics Analysis](https://arxiv.org/abs/2606.13602)

**<font color=#1a73e8>作者：</font>** Harihara Muralidharan, Reema Baskar, Soo Hee Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce EpiBench, a verifiable benchmark for short-horizon epigenomics analysis. EpiBench evaluates whether agents can make well-defined analysis decisions from realistic workflow states and return deterministically gradable answers. The benchmark includes 106 evaluations across CUT\&Tag/CUT\&RUN, ATAC-seq, ChIP-seq, and DNA methylation workflows. Across 5,088 valid trajectories from 16 model-harness pairs, no system passed a majority of attempts: GPT-5.5 / Pi led at 45.0\% (143/318 attempts; 95\% confidence interval (CI), 36.3--53.7), followed by GPT-5.5 / OpenAI Codex at 39.9\% (127/318 attempts; 95\% CI, 31.6--48.3). Claude Opus 4.8 Max / Pi and GPT-5.4 / Pi each passed 39.0\% (124/318 attempts; 95\% CI, 30.2--47.8 and 31.0--47.0, respectively). Performance varies across assay types, and many failed runs still contain parts of the correct answer. Agents often found the right files and computed useful intermediate results, but failed when the task required deeper, assay-specific scientific judgment.

---


### 231. [Multi-Agent Reinforcement Learning from Delayed Marketplace Feedback for Objective-Weight Adaptation in Three-Sided Dispatch](https://arxiv.org/abs/2606.13604)

**<font color=#1a73e8>作者：</font>** Haochen Wu, Yi Hou, Shiguang Xie  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Dispatch in three-sided marketplaces provides a natural setting for reinforcement learning from world feedback: decisions are evaluated by delayed operational outcomes such as delivery speed, courier utilization, and merchant congestion. We present a deployed reinforcement learning system at DoorDash that adapts dispatch objective weights in a large-scale food-delivery marketplace using delayed signals. Rather than replacing the combinatorial assignment optimizer, a store-level policy learned from logged marketplace data selects a discrete multiplier that shifts the dispatch optimizer's tradeoff between delivery quality and batching efficiency. This interface enables offline policy learning under noisy, delayed, and coupled feedback while preserving production feasibility constraints and operational safeguards. We train a shared value function using centralized offline data and decentralized store-level execution, with Double Q-learning targets and a conservative regularizer to reduce out-of-distribution value overestimation. In a production switchback experiment, the offline-trained policy increases batching and reduces courier-side time costs without degrading customer-facing delivery quality. Results illustrate how world feedback from a live economic and logistics system can be used to safely adapt decision policies online.

---


### 232. [AgentBeats: Agentifying Agent Assessment for Openness, Standardization, and Reproducibility](https://arxiv.org/abs/2606.13608)

**<font color=#1a73e8>作者：</font>** Xiaoyuan Liu, Jianhong Tu, Yuqi Chen 等 29 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent systems are advancing quickly across domains, but their evaluation remains fragmented. Most benchmarks rely on fixed, LLM-centric harnesses that require heavy integration, create test-production mismatch, and limit fair comparison across diverse agent designs. The root problem is the lack of an open, agent-agnostic assessment interface. We advocate Agentified Agent Assessment (AAA), where evaluation is performed by judge agents and all participants interact through standardized protocols: A2A for task management and MCP for tool access. Conventional benchmarking defines two separate interfaces, one for the benchmark and one for the agent, while AAA only needs one; this yields a generic, unified framework that separates assessment logic from agent implementation and enables reproducible, interoperable, and multi-agent evaluation. We further introduce AgentBeats as a concrete realization of AAA: we identify five practical operation modes that make standardized assessment compatible with real-world constraints on openness, privacy, and reproducibility.
To evaluate our design at scale, we conduct two studies: a five-month open competition that drew 298 judge agents across 12 categories together with 467 subject agents from independent participants, showing that AAA applies across a heterogeneous range of benchmarks; and a case study on coding agents that confirms agentified evaluation preserves fidelity with the public record while surfacing previously missing head-to-head results, yielding research insights about agent design. Combining a community-scale field study and a controlled coding case study, we verify that AAA delivers coverage, practicality, and fidelity across heterogeneous scenarios at scale. Together, AAA and AgentBeats offer a clear path toward open, standardized, and reproducible agent assessment.

---


### 233. [One Polluted Page Is Enough: Evaluating Web Content Pollution in Generative Recommenders](https://arxiv.org/abs/2606.13610)

**<font color=#1a73e8>作者：</font>** Minghao Luo, Liang Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Search-augmented LLMs increasingly mediate everyday consumer recommendations by retrieving live web content. This creates a new risk: generative recommenders may consume polluted web content, such as fake reviews and promotional pages crafted to mislead recommendations. We ask: to what extent do search-augmented LLMs become unwitting promoters of fake products when consuming polluted retrieval results? To answer this, we introduce FORGE (Fake Online Recommendations in Generative Environments), a benchmark for measuring fake-product promotion under controlled web-content pollution. Given an upstream search result, FORGE locally rewrites real products in retrieved web pages into fake ones to simulate web-content pollution, and measures how often the LLM recommends the fake product. FORGE covers 225 real-world products across 15 categories and 5 consumer scenarios. Across 12 commercial and open-weights LLMs, all models are vulnerable: a single polluted page yields fooled rates of up to 27%, while the full top-3 replacement raises this to 73.8%. Vulnerability varies substantially across categories, increasing when models lack stable prior knowledge of the relevant products. Reasoning does not mitigate this vulnerability; instead, it often generates spurious social proof to justify false recommendations. We evaluate three defenses: skepticism prompting and consensus filtering (over model priors or cross-document evidence). Skepticism can exacerbate vulnerability, much like reasoning, while filtering risks suppressing legitimate products. We release FORGE at this https URL.

---


### 234. [Beyond the IT Checklist: Engineering a Reasonable Standard of Care for Cyber Safety](https://arxiv.org/abs/2606.13612)

**<font color=#1a73e8>作者：</font>** Matthew E. Jablonski, Linton Wells II, Kathryn B. Laskey 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Current U.S. cyber policy, centered on security, often treats documentation of controls and incident reports as a proxy for safety in the built environment. This paper argues that such an approach is inadequate for cyber-physical systems, where digital failures can produce kinetic harm. We construct and code a corpus of critical infrastructure policy documents (N=292, 2000-2025) to examine how "reasonable care" is operationalized across the NIST SP 800-160 Vol.~2 resilience lifecycle. The resulting maps show that obligations are concentrated in the Anticipate phase and emphasize administrative compliance, while Withstand and Recover phases rely heavily on delegated references to IT-focused control catalogs that are poorly aligned with physics-based hazards. We identify three major disconnects: miscalibrated delegated standards, recovery defined as notification rather than engineered navigation, and uneven adaptation requirements across sectors. We then propose a modernized standard of care anchored in hazard-specific traceability, structured assurance cases, and cyber resiliency engineering. Finally, we recommend that federal policy pair these engineering obligations with targeted incentives so that resilient architectures for critical infrastructure become a viable business decision rather than an unfunded expectation.

---


### 235. [Beyond Runtime Enforcement: Shield Synthesis as Defensibility Analysis for Adversarial Networks](https://arxiv.org/abs/2606.13621)

**<font color=#1a73e8>作者：</font>** Achraf Hsain, Sultan Almuhammadi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Shielded reinforcement learning is typically presented as a runtime safety mechanism that compiles temporal-logic specifications into automata restricting an agent's actions. We argue this is the wrong product. The same automata-theoretic machinery -- specification compilation, product game construction, attractor computation, and winning-region extraction -- is better read as a design-time analytical instrument whose outputs are structural insights about a system rather than runtime constraints on a deployed agent.
We instantiate this through a constrained two-player safety game for network defense. The two specifications are enforced asymmetrically: the defender specification defines the unsafe region of the game, whereas the attacker specification restricts the adversary's legal actions during attractor computation. Solving the game yields a defensibility verdict -- a formal certificate that a topology-specification pair is or is not defensible -- with the associated winning region and shield.
Beyond the binary verdict, we derive topology-level metrics from the attractor structure and combine them with post-convergence behavior from shield-constrained adversarial multi-agent reinforcement learning. Together these form a defensibility fingerprint capturing both a network's formal safety properties and its operational behavior under adaptive play.
A what-if analysis shows that formal defensibility and operational effectiveness capture distinct aspects of security: small architectural changes can produce large shifts in operational outcomes while leaving formal safety margins nearly unchanged. Shield synthesis is thus most valuable not as a deployment mechanism for safe agents, but as a framework for answering architectural questions about whether, where, and how a system can be defended. The defensibility verdict is the output, not the safe policy.

---


### 236. [Revisiting Vehicle Color Recognition in Long-Tailed Surveillance Scenarios](https://arxiv.org/abs/2606.13625)

**<font color=#1a73e8>作者：</font>** Vinícius Orrú, Bruno H. Foggiatto, Gabriel E. Lima 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vehicle color recognition is an important cue for vehicle identification in surveillance systems, especially when license plates are illegible due to low resolution, occlusion, motion blur, or poor illumination. However, real-world vehicle color distributions are highly imbalanced, making overall accuracy insufficient to assess performance on rare but operationally relevant colors. This paper presents a comprehensive study of vehicle color recognition under severe class imbalance using UFPR-VeSV, a challenging real-world surveillance dataset. We investigate synthetic minority-class augmentation through two off-the-shelf generative strategies: text-conditioned image generation with RunDiffusion/JuggernautXL and image-conditioned color editing with Gemini 2.0 Flash. The curated synthetic data are combined with modern visual representations, loss reweighting, learning-rate scheduling, color-safe augmentation, foreground-aware preprocessing, and ensemble fusion. The bestperforming approach achieves 94.6% micro accuracy and 79.7% macro accuracy, improving macro accuracy by 8.2 percentage points over recent literature. A manual error analysis further shows that many remaining failures are visually ambiguous even for human annotators, highlighting the practical limits of color-based vehicle identification in unconstrained surveillance imagery. The generated images and source code are publicly available at this https URL

---


### 237. [From Tokens to Faces: Investigating Discrete Speech Representations for 3D Facial Animation](https://arxiv.org/abs/2606.13630)

**<font color=#1a73e8>作者：</font>** Pedro Correa, Olivier Perrotin, Samir Sadok 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The choice of speech representation is critical in speech-driven 3D facial animation. Representations differ in what they encode: SSL features emphasize segmental and semantic cues, neural codecs yield latents optimized for acoustic reconstruction, and ASR-style objectives produce label-based spaces. We evaluate four speech representation families for 3D facial synthesis, comparing their facial reconstruction quality across two facial decoders using objective metrics and a perceptual evaluation. We additionally conduct probing analyses that relate tokenized representations to phonetic units and to articulatory deformations. We found that encoding phonetic classes is beneficial for accurate facial animation prediction on both semantic and label-based representations with comparable facial animation quality. From the latter, we introduce an Audio Visual Text-to-Speech (AVTTS) pipeline that leverages, as a shared space, discrete representations to decode speech and 3D facial motion.

---


### 238. [The Stable Recovery Manifold: Geometric Principles Governing Recoverability in Continual Learning](https://arxiv.org/abs/2606.13637)

**<font color=#1a73e8>作者：</font>** Ayushman Trivedi, Bhavika Melwani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Catastrophic forgetting is often viewed as the destruction of previously learned knowledge during sequential learning. Building on the Accessibility Collapse framework, we investigate the geometric structure of recoverability in continual learning. Using Split CIFAR-100 and a sequentially trained ResNet-18, we analyze recoverability, representational drift, and recovery complexity across ten tasks. We introduce Recovery Subspace Dimensionality (k_t), a measure of the minimum number of singular directions required to preserve 90 percent of full probe performance. Contrary to our Recoverability Diffusion hypothesis, recovery dimensionality remains stable throughout training (mean k_t = 8.0) despite substantial representational drift. Principal-angle drift strongly predicts recoverability (r = -0.862), and a simple geometric model explains 82.2 percent of recoverability variance. These findings support the Stable Recovery Manifold hypothesis, suggesting that forgotten knowledge remains compactly decodable despite representational reorganization. The results indicate that catastrophic forgetting is primarily an accessibility and manifold-alignment problem rather than information destruction.

---


### 239. [Tuning Agent-Based Predator-Prey Models Toward Lotka-Volterra Dynamics](https://arxiv.org/abs/2606.13639)

**<font color=#1a73e8>作者：</font>** Corinna Mandl, Siddharth Chaturvedi, Marcel van Gerven  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Recent growth in compute power has made it increasingly feasible to use large-scale agent-based models to simulate complex adaptive systems. A central difficulty is that such models contain many local rules and parameters, where small changes can lead to runaway behaviour, population collapse, or saturation at artificial bounds. We study this problem in a continuous predator-prey system where sheep and wolves are active agents with local sensing, internal energy, and recurrent neural network-based controllers. We ask whether environmental and demographic parameters can be tuned so that the resulting population dynamics resemble classical Lotka-Volterra cycles. We optimise these parameters with a feature-based loss that rewards sustained oscillations, phase lag, bounded populations, and long-term persistence, first for random controllers and then for evolved controllers in a more naturalistic setting. The model is implemented in ABMax, a JAX-based agent-based modelling framework that enables efficient batched simulation on hardware accelerators.

---


### 240. [Recursive Agent Harnesses](https://arxiv.org/abs/2606.13643)

**<font color=#1a73e8>作者：</font>** Elias Lumer, Sahil Sen, Kevin Paul 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recursive language models (RLMs) showed that recursion over model calls is an effective strategy for long-context reasoning, and production coding agents have begun to write code that spawns subagents at scale, most recently in Anthropic's dynamic workflows. We name and study the pattern between these two lines of work, where the recursive unit is a full agent harness with filesystem tools, code execution, and planning rather than a model call with no tools. We call this the Recursive Agent Harness (RAH) and frame it as harness recursion, the code-first extension to the model recursion of RLMs. A parent agent generates and runs an executable script that spawns subagent harnesses in parallel for fine-grained workloads and uses structured function calls for small subtasks. We provide a controlled evaluation on long-context reasoning. With the backbone held fixed at GPT-5 to match the published Codex and RLM baselines, RAH improves the Codex coding-agent baseline from 71.75% to 81.36% on Oolong-Synthetic (199 samples, 13 context-length buckets up to 4M tokens), a gain attributable to the harness rather than the model. With a stronger backbone, Claude Sonnet 4.5, the same design reaches 89.77%.

---


### 241. [Surflo: Consistent 3D Surface Flow Model with Global State](https://arxiv.org/abs/2606.13644)

**<font color=#1a73e8>作者：</font>** Antoine Guédon, Shu Nakamura, Nicolas Dufour 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geometry is invariant to viewpoint, which makes any collection of images a redundant encoding of a single 3D state. Existing feed-forward reconstruction models fail to exploit this: per-view methods emit overlapping, unaligned pointmaps that grow linearly with input count, while global-latent methods commit to a fixed, low-resolution output. We introduce Surflo, which compresses a variable number of unposed RGB views into K latent tokens-one global state-and decodes oriented 3D surface points by independently transporting them from noise onto the surface via flow matching. This frees the output from any fixed grid or token budget: the same latent yields from a few thousand to a million points in a single forward pass. To suppress the local inconsistencies inherent to independent per-point decoding, an inference-time guidance term correlates nearby points by injecting a photometric gradient during ODE integration. Surflo matches or surpasses feed-forward baselines on surface metrics, runs an order of magnitude faster than optimization-based methods that require hundreds of views, and is the only feed-forward approach to combine a global latent with arbitrary-resolution decoding.

---


### 242. [SkMTEB: Slovak Massive Text Embedding Benchmark and Model Adaptation](https://arxiv.org/abs/2606.13647)

**<font color=#1a73e8>作者：</font>** Marek Šuppa, Andrej Ridzik, Daniel Hládek 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce SkMTEB, the first comprehensive MTEB-style text embedding benchmark for Slovak, a low-resource West Slavic language, comprising 31 datasets across 7 task types -- nearly 4$\times$ the depth of existing multilingual benchmark coverage for Slovak. Our evaluation of 31 embedding models reveals that large instruction-tuned multilingual models achieve the strongest performance, while existing Slovak-specific models trained for NLU tasks transfer poorly to embedding tasks. To address the need for efficient, locally-deployable Slovak embeddings, we develop \texttt{e5-sk-small} (45M parameters) and \texttt{e5-sk-large} (365M) by applying vocabulary trimming and fine-tuning to Multilingual E5 models. Despite size reductions of up to 62\%, our open-source models achieve competitive performance with proprietary APIs while remaining locally deployable for semantic search and retrieval-augmented generation (RAG). We release the benchmark, models, datasets, and code openly, hoping our approach offers a replicable path for other under-resourced languages.

---


### 243. [World Tracing: Generative Pixel-Aligned Geometry Beyond the Visible](https://arxiv.org/abs/2606.13652)

**<font color=#1a73e8>作者：</font>** Hao Zhang, Mohamed El Banani, Jen-Hao Cheng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image-to-3D methods often trade off faithfulness and completeness: depth estimators are anchored to input pixels but stop at the visible surface, while image-to-3D models generate complete shapes that are often misaligned with the input. We introduce World Tracing, a generative pixel-aligned geometry representation that predicts 3D points aligned with observed pixels while completing geometry beyond the visible surface. For each input pixel, World Tracing predicts an ordered stack of camera-space 3D points, where the first layer represents the visible surface and subsequent layers represent front-to-back intersections with occluded surfaces. We instantiate this representation with a world-tracing diffusion transformer, WT-DiT, which treats multiple geometry layers as separate denoising tokens coupled through factorized and global attention. WT-DiT is trained with pixel-space flow matching and a mixed noise schedule that balances visible-surface reconstruction with occluded-geometry generation. World Tracing achieves strong performance on visible-surface reconstruction and complete geometry generation across object, scene, and dynamic benchmarks, outperforming both depth predictors and image-to-3D generators. It also preserves 2D-to-3D correspondence, enabling text-driven 3D scene editing, geometry-conditioned novel-view video synthesis, and training-free integration with textured-mesh generators.

---


### 244. [Flex4DHuman: Flexible Multi-view Video Diffusion for 4D Human Reconstruction](https://arxiv.org/abs/2606.13655)

**<font color=#1a73e8>作者：</font>** Jen-Hao Cheng, Yipeng Wang, Hao Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Flex4DHuman, a multi-view video diffusion model that transforms a monocular or sparse multi-view video of a dynamic subject into synchronized dense multi-view videos using only relative camera-pose conditioning. Unlike prior human-centric methods that rely on skeletons, depth maps, normals, or rendered target-view geometry, Flex4DHuman requires no explicit geometry priors and instead conditions generation through relative camera-pose positional encoding. The generated videos can be directly ingested by downstream reconstruction pipelines to create dynamic 4D Gaussian splats. Built on the Wan 2.1 1.3B text-to-video model, Flex4DHuman preserves the backbone architecture and encodes camera and view information through a five-axis positional encoding that extends spatio-temporal RoPE with view indices and continuous SE(3) relative camera geometry. A three-stage curriculum progressively trains the model for pose following, flexible reference-to-target view generation, and temporal rollout. To support temporal rollout, we train with clean historical target-view tokens. We also add multi-view captions to enable test-time text control. Combined with an off-the-shelf 4D Gaussian Splatting stage, our framework lifts monocular static-camera videos into dynamic 4D Gaussian splats. Experiments on DNA-Rendering and ActorsHQ show that Flex4DHuman surpasses prior state-of-the-art methods, while the same formulation generalizes to animal categories after mixed human-animal training. These capabilities make Flex4DHuman a practical step toward scalable 4D content creation from casual monocular videos for simulation, gaming, AR/VR, and video re-shooting.

---


### 245. [Dense Supervision, Sparse Updates: On the Sparsity and Geometry of On-Policy Distillation](https://arxiv.org/abs/2606.13657)

**<font color=#1a73e8>作者：</font>** Guo Yu, Wenlin Liu, Yulan Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (\textsc{OPD}) has recently become a prominent post-training recipe as it combines two desirable ingredients: on-policy student trajectories and dense teacher supervision, yet how this hybrid changes a model's parameters remains unclear. Across several language and vision-language model pairs and use cases, our analysis yields two main findings. On sparsity, \textsc{OPD}-style updates are small and coordinate-sparse. They are distributed across layers and are usually FFN-heavy. This sparse structure is operationally useful: training only the discovered subnetwork recovers nearly the same performance as full \textsc{OPD}. However, the sparsity-inducing SGD optimizer underperforms AdamW in our optimizer ablation, likely because dense teacher supervision preserves heterogeneous coordinate-wise gradient scales where AdamW's adaptive scaling remains useful. On geometry, the updates are numerically full-rank but spectrally concentrated; they lie mostly away from the principal singular subspaces of the source weights and fall disproportionately on coordinates where the source weights are close to zero. These findings suggest that dense teacher supervision does not turn \textsc{OPD} into ordinary dense parameter rewriting; instead, \textsc{OPD} retains important geometric signatures of on-policy post-training.

---


### 246. [Before You Think: System 0, AI-Mediated Cognition and Cognitive Colonization](https://arxiv.org/abs/2606.13658)

**<font color=#1a73e8>作者：</font>** Marianna Bergamaschi Ganapini, Massimo Chiriatti, Enrico Panai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper examines three recent frameworks for understanding the cognitive and epistemic consequences of artificial intelligence: Tri-System Theory, Thinkframes, and System 0. It argues that while the first two capture important dimensions of AI's influence on individual reasoning and collective epistemic practices, System 0 occupies a theoretically distinctive position that neither can fully replicate. The paper introduces the concept of cognitive colonization, according to which AI systems can embed external interests within the architecture of the self in ways that are difficult for users to perceive. Because such systems are already widely deployed, understanding these invisible forms of influence is an urgent philosophical and practical task.

---


### 247. [EurekAgent: Agent Environment Engineering is All You Need For Autonomous Scientific Discovery](https://arxiv.org/abs/2606.13662)

**<font color=#1a73e8>作者：</font>** Amy Xin, Jiening Siow, Junjie Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based agents have shown increasing potential in automating scientific discovery. Given an optimizable metric and an execution environment, they can propose, validate, and iterate scientific solutions, and have produced results that outperform human-designed approaches. As model capabilities continue to improve, we argue that the bottleneck for autonomous scientific discovery is shifting from prescribing agent workflows to designing agent environments: the resources, constraints, and interfaces that shape agent behavior. We frame this as environment engineering: building environments that amplify productive behaviors, such as open-ended exploration, systematic artifact management, and inter-agent collaboration, while suppressing harmful behaviors, such as reward hacking and high-friction human oversight. We present EurekAgent, an environment-engineered agent system for metric-driven autonomous scientific discovery. EurekAgent engineers the environment along four dimensions: permissions engineering for bounded agent execution and isolated evaluation; artifact engineering for filesystem and Git-based collaboration; budget engineering for budget-aware exploration; and human-in-the-loop engineering for easy human supervision and intervention. EurekAgent sets new state-of-the-art results on multiple mathematics, kernel engineering, and machine learning tasks, including new state-of-the-art 26-circle packing results discovered with less than $11 in total API cost. We open-source our code and results, and call for environment engineering as a core research direction for developing reliable autonomous research agents.

---


### 248. [Agents-K1: Towards Agent-native Knowledge Orchestration](https://arxiv.org/abs/2606.13669)

**<font color=#1a73e8>作者：</font>** Zongsheng Cao, Bihao Zhan, Jinxin Shi 等 25 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current LLM-based research agents have advanced through agent orchestration, yet largely overlook scientific knowledge orchestration. Existing works often reduce papers to abstracts, surface mentions, and flat \texttt{cites} edges, omitting key entities, claims, evidence, mechanisms, and method lineages essential for scientific reasoning. To this end, we introduce \textbf{Agents-K1}, an end-to-end knowledge orchestration pipeline that converts raw documents into agent-native scientific knowledge graphs. Agents-K1 integrates three components under a unifying theoretical foundation: a multimodal parser whose five-module schema captures entities, multimodal evidence, citations, and typed inter-entity relations across the full paper rather than abstracts alone; a 4B information-extraction backbone trained with GRPO under a rule-based reward; and a graphanything CLI, a tri-source agent interface that unifies web search, multimodal graph retrieval, and cross-document traversal. On top of this, we process 2.46 million scientific papers across six subjects to produce \textbf{Scholar-KG}, of which we release a one-million-paper subset, and the full Scholar-KG is accessible via the SCP link below. The same pipeline can be extended to general-domain corpora and to schema-conformant data synthesis. Extensive experiments demonstrate that Agents-K1 achieves superior performance in scientific information extraction, knowledge graph construction, and multi-hop scientific reasoning.

---


### 249. [Understanding Truncated Positional Encodings for Graph Neural Networks](https://arxiv.org/abs/2606.13671)

**<font color=#1a73e8>作者：</font>** James Flora, Mitchell Black, Weng-Keen Wong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Positional encodings (PEs) enhance the power of graph neural networks (GNNs), both theoretically and empirically. Two of the most popular families of PEs - spectral (e.g., Laplacian eigenspaces, effective resistance) and walk-based (polynomials of the adjacency matrix) - are theoretically equivalent in expressive power, with expressivity between the 1-WL and 3-WL tests. However, this equivalence assumes the GNN uses the "complete" version of these PEs, which requires $O(n^3)$ time and space complexity. Instead, practitioners commonly use truncated variants of these encodings, such as the first $k$ eigenspaces or powers of the adjacency matrix. However, the theoretical properties of these truncated PEs are unknown. In this work, we initiate the study of these truncated PEs. Theoretically, we show that, under truncation, several families of PEs are fundamentally different in expressive power. As a corollary, we show that truncated spectral PEs are no longer stronger than the 1-WL test. We also study a family of spectral PEs, the $k$-harmonic distances, to highlight the differences in expressive power of even closely related truncated PEs. Finally, we experimentally show that a mix of truncated PEs is preferable to any single family on real-world datasets.

---


### 250. [RepWAM: World Action Modeling with Representation Visual-Action Tokenizers](https://arxiv.org/abs/2606.13674)

**<font color=#1a73e8>作者：</font>** Junke Wang, Qihang Zhang, Shuai Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This work presents RepWAM, a representation-centric world action model (WAM) built on representation visual-action tokenizers. Existing WAMs typically inherit reconstruction-oriented video tokenizers from pretrained video generation models. Although these tokenizers preserve visual fidelity, pixel reconstruction alone provides limited guidance for learning instruction-following dynamics that connect future prediction with robot control. To address this, we explore a semantic visual-action latent space for representation-centric world action modeling. Specifically, we train a representation visual-action tokenizer that maps visual inputs into aligned visual and latent action tokens. We then pretrain our WAM to jointly model future visual states and the latent actions that connect them under language instructions, followed by adaptation to real robot trajectories for closed-loop manipulation. Experiments on real-world manipulation tasks and simulation benchmarks show that RepWAM delivers strong performance across diverse manipulation settings, while ablations highlight the value of semantic visual-action tokenization over reconstruction-oriented alternatives. These results establish representation visual-action tokenization as a promising foundation for world action models and a step toward generalist robot policies. Code and weights will be available at this https URL.

---


> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-251](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
