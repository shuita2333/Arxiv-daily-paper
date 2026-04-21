# 📦 其他研究 | 2026年04月22日

> 本类共 **535** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**501-535**（第 11/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-535**

---

### 501. [ProtoCLIP: Prototype-Aligned Latent Refinement for Robust Zero-Shot Chest X-Ray Classification](https://arxiv.org/abs/2604.18444)

**<font color=#1a73e8>作者：</font>** Florian Kittler, Sheethal Bhat, Andreas Maier  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Zero-shot vision-language models (VLMs) have shown promise for chest radiograph classification, but their performance is often limited by confounding label co-occurrence, long-tail class imbalance, and transfer instability under domain shift. We propose ProtoCLIP, a refinement strategy for CLIP-style VLMs that improves zero-shot discrimination through targeted data curation and distilled anchor alignment. Specifically, we construct pathology-focused training subsets with curated negative samples to reduce co-occurrence bias. We also introduce a representation-preserving distillation objective to stabilize adaptation while maintaining semantic structure and improving discrimination of clinically relevant co-occurring pathologies. Evaluated on an unseen dataset VinDr-CXR, ProtoCLIP improves AUC by 2-10 percentage points over a strong CLIP-based baseline across multiple findings. For pneumothorax specifically, ProtoCLIP achieves a state-of-the-art AUC of 0.94. These results demonstrate that anchor-guided refinement, coupled with curated supervision and controlled adaptation, can mitigate common zero-shot transfer failures in medical VLMs without requiring large-scale retraining.

---


### 502. [AutoPPA: Automated Circuit PPA Optimization via Contrastive Code-based Rule Library Learning](https://arxiv.org/abs/2604.18445)

**<font color=#1a73e8>作者：</font>** Chongxiao Li, Pengwei Jin, Di Huang 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Performance, power, and area (PPA) optimization is a fundamental task in RTL design, requiring a precise understanding of circuit functionality and the relationship between circuit structures and PPA metrics. Recent studies attempt to automate this process using LLMs, but neither feedback-based nor knowledge-based methods are efficient enough, as they either design without any prior knowledge or rely heavily on human-summarized optimization rules.
In this paper, we propose AutoPPA, a fully automated PPA optimization framework. The key idea is to automatically generate optimization rules that enhance the search for optimal solutions. To do this, AutoPPA employs an Explore-Evaluate-Induce ($E^2I$) workflow that contrasts and abstracts rules from diverse generated code pairs rather than manually defined prior knowledge, yielding better optimization patterns. To make the abstracted rules more generalizable, AutoPPA employs an adaptive multi-step search framework that adopts the most effective rules for a given circuit. Experiments show that AutoPPA outperforms both the manual optimization and the state-of-the-art methods SymRTLO and RTLRewriter.

---


### 503. [From Awareness to Intent: Mitigating Silent Driving System Failures through Prospective Situation Awareness Enhancing Interfaces](https://arxiv.org/abs/2604.18449)

**<font color=#1a73e8>作者：</font>** Jiyao Wang, Song Yan, Xiao Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Silent automation failures, where a system fails to detect a hazard without warning, pose a critical safety challenge for partially automated vehicles. While research has mostly focused on takeover requests, how to support a driver in silent failure remains underexplored. We conducted a multi-modal driving simulator study with 48 participants to investigate how different Prospective Situation Awareness Enhancement (PSAE) interfaces, delivered via augmented reality head-up display, affect takeover performance. By integrating behavioral, subjective psychological, and physiological data, our analysis suggests that situational awareness (SA) serves as an important moderating factor through which PSAE interfaces improve takeover performance. Further, we found that providing perceptual cues was most effective in enhancing SA, while communicating system intent was superior for building trust. Finally, we identified a potential correlate of SA in the neuroactivity. Overall, this paper contributes to understanding how transparency-oriented interfaces may support drivers and provides design insights into HMI design for silent failures.

---


### 504. [ESsEN: Training Compact Discriminative Vision-Language Transformers in a Low-Resource Setting](https://arxiv.org/abs/2604.18452)

**<font color=#1a73e8>作者：</font>** Clayton Fields, Casey Kennington  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language modeling is rapidly increasing in popularity with an ever expanding list of available models. In most cases, these vision-language models have parameters in the tens of billions, which is necessary for some needs, but in many cases smaller models are necessary (e.g., on edge devices or independent robotic platforms). Unfortunately, there is little research in producing light-weight models or in training them with small datasets. Inspired by the language learning progression and data sparsity in child development, in this paper, we address both of these goals in a systematic fashion. We show that two-tower encoder models are superior to one-tower encoders in low-resource settings for discriminative English tasks. We show also that incorporating traditional convolutional networks into the two-tower transformer architecture can help produce parameter efficient vision-language models. Finally, we show that the cross-modal fusion module of two-tower encoders can vary significantly in shape and size while producing the same results. In addition, we present ESsEN, a compact vision-language model that can be trained end-to-end with relatively few resources that performs as well on several tasks with only a fraction of the parameters compared to other models. The experimental results and the tools we present here make vision-language modeling more accessible to a wider variety of researchers.

---


### 505. [Progressive Online Video Understanding with Evidence-Aligned Timing and Transparent Decisions](https://arxiv.org/abs/2604.18459)

**<font color=#1a73e8>作者：</font>** Kecheng Zhang, Zongxin Yang, Mingfei Han 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual agents operating in the wild must respond to queries precisely when sufficient evidence first appears in a video stream, a critical capability that is overlooked by conventional video LLMs evaluated in offline settings. The shift to an online, streaming paradigm introduces significant challenges: a lack of decision transparency, the difficulty of aligning response timing with visual evidence, and the need to maintain a global, causally consistent understanding under tight computational budgets. To address these issues, we propose a novel framework that decouples reasoning control from memory integration. We introduce \textbf{\model{}}, an instantiation of this framework with two core components. First, the \emph{Active Thinking Decision Maker (ATDM)} is a transparent reasoning controller that externalizes its decision process using observable progress ($\boldsymbol{\rho}$) and confidence ($\boldsymbol{c}$) metrics. This allows it to precisely time its response $t_r$ to match the first-sufficient-evidence timestamp $t^\star$ while streaming its reasoning to the user. Second, the \emph{Hierarchical Progressive Semantic Integration (HPSI)} module acts as an efficient memory system. It employs a set of learnable, multi-level aggregation tokens that are propagated across clips to build a rich, global cognitive state without exceeding token budgets. %Our approach sets a new standard on key online video understanding benchmarks, achieving strong performance of \textbf{71.6\%} on StreamingBench and \textbf{46.9\%} on OVOBench, demonstrating a robust solution for evidence-aligned and transparent online video analysis. Extensive experiments demonstrate the effectiveness of ATDM and HPSI, e.g., Thinking-QwenVL improves the accuracy of the previous state-of-the-art from 67.63\% to 71.60\% on the StreamingBench benchmark.

---


### 506. [An Integrated Deep-Learning Framework for Peptide-Protein Interaction Prediction and Target-Conditioned Peptide Generation with ConGA-PePPI and TC-PepGen](https://arxiv.org/abs/2604.18467)

**<font color=#1a73e8>作者：</font>** Chupei Tang, Junxiao Kong, Moyu Tang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Motivation: Peptide-protein interactions (PepPIs) are central to cellular regulation and peptide therapeutics, but experimental characterization remains too slow for large-scale screening. Existing methods usually emphasize either interaction prediction or peptide generation, leaving candidate prioritization, residue-level interpretation, and target-conditioned expansion insufficiently integrated. Results: We present an integrated framework for early-stage peptide screening that combines a partner-aware prediction and localization model (ConGA-PepPI) with a target-conditioned generative model (TC-PepGen). ConGA-PepPI uses asymmetric encoding, bidirectional cross-attention, and progressive transfer from pair prediction to binding-site localization, while TC-PepGen preserves target information throughout autoregressive decoding via layerwise conditioning. In five-fold cross-validation, ConGA-PepPI achieved 0.839 accuracy and 0.921 AUROC, with binding-site AUPR values of 0.601 on the protein side and 0.950 on the peptide side, and remained competitive on external benchmarks. Under a controlled length-conditioned benchmark, 40.39% of TC-PepGen peptides exceeded native templates in AlphaFold 3 ipTM, and unconstrained generation retained evidence of target-conditioned signal.

---


### 507. [Asset Harvester: Extracting 3D Assets from Autonomous Driving Logs for Simulation](https://arxiv.org/abs/2604.18468)

**<font color=#1a73e8>作者：</font>** Tianshi Cao, Jiawei Ren, Yuxuan Zhang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Closed-loop simulation is a core component of autonomous vehicle (AV) development, enabling scalable testing, training, and safety validation before real-world deployment. Neural scene reconstruction converts driving logs into interactive 3D environments for simulation, but it does not produce complete 3D object assets required for agent manipulation and large-viewpoint novel-view synthesis. To address this challenge, we present Asset Harvester, an image-to-3D model and end-to-end pipeline that converts sparse, in-the-wild object observations from real driving logs into complete, simulation-ready assets. Rather than relying on a single model component, we developed a system-level design for real-world AV data that combines large-scale curation of object-centric training tuples, geometry-aware preprocessing across heterogeneous sensors, and a robust training recipe that couples sparse-view-conditioned multiview generation with 3D Gaussian lifting. Within this system, SparseViewDiT is explicitly designed to address limited-angle views and other real-world data challenges. Together with hybrid data curation, augmentation, and self-distillation, this system enables scalable conversion of sparse AV object observations into reusable 3D assets.

---


### 508. [A Generalized Synthetic Control Method for Baseline Estimation in Demand Response Services](https://arxiv.org/abs/2604.18469)

**<font color=#1a73e8>作者：</font>** Jonas Sievers, Mardavij Roozbehani  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Baseline estimation is critical to Demand Response (DR) settlement in electricity markets, yet existing machine learning methods remain limited in predictive performance, while methodologies from causal inference and counterfactual prediction are still underutilized in this domain. We introduce a Generalized Synthetic Control Method that builds on the classical Synthetic Control Method (SCM) from econometrics. While SCM provides a powerful framework for counterfactual estimation, classical SCM remains a static estimator: it fits the treated unit as a combination of contemporaneous donor units and therefore ignores predictable temporal structure in the residual error. We develop a generalized SCM framework that transforms baseline estimation into a dynamic counterfactual prediction problem by augmenting the donor representation with exogenous features, lagged treated load, and selected lagged donor signals. This enriched representation allows the estimator to capture autoregressive dependence, delayed donor-response patterns, and error-correction effects beyond the scope of standard SCM. The framework further accommodates nonlinear predictors when linear weighting is inadequate, with the greatest benefit arising in limited-data settings. Experiments on the Ausgrid smart-meter dataset show consistent improvements over classical SCM and strong benchmark methods, with the dominant performance gains driven by dynamic augmentation.

---


### 509. [SemLT3D: Semantic-Guided Expert Distillation for Camera-only Long-Tailed 3D Object Detection](https://arxiv.org/abs/2604.18476)

**<font color=#1a73e8>作者：</font>** Hao Vo, Khoa Vo, Thinh Phan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera-only 3D object detection has emerged as a cost-effective and scalable alternative to LiDAR for autonomous driving, yet existing methods primarily prioritize overall performance while overlooking the severe long-tail imbalance inherent in real-world datasets. In practice, many rare but safety-critical categories such as children, strollers, or emergency vehicles are heavily underrepresented, leading to biased learning and degraded performance. This challenge is further exacerbated by pronounced inter-class ambiguity (e.g., visually similar subclasses) and substantial intra-class diversity (e.g., objects varying widely in appearance, scale, pose, or context), which together hinder reliable long-tail recognition. In this work, we introduce SemLT3D, a Semantic-Guided Expert Distillation framework designed to enrich the representation space for underrepresented classes through semantic priors. SemLT3D consists of: (1) a language-guided mixture-of-experts module that routes 3D queries to specialized experts according to their semantic affinity, enabling the model to better disentangle confusing classes and specialize on tail distributions; and (2) a semantic projection distillation pipeline that aligns 3D queries with CLIP-informed 2D semantics, producing more coherent and discriminative features across diverse visual manifestations. Although motivated by long-tail imbalance, the semantically structured learning in SemLT3D also improves robustness under broader appearance variations and challenging corner cases, offering a principled step toward more reliable camera-only 3D perception.

---


### 510. [Multi-Scale Reversible Chaos Game Representation: A Unified Framework for Sequence Classification](https://arxiv.org/abs/2604.18477)

**<font color=#1a73e8>作者：</font>** Sarwan Ali, Taslim Murad  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Biological classification with interpretability remains a challenging task. For this, we introduce a novel encoding framework, Multi-Scale Reversible Chaos Game Representation (MS-RCGR), that transforms biological sequences into multi-resolution geometric representations with guaranteed reversibility. Unlike traditional sequence encoding methods, MS-RCGR employs rational arithmetic and hierarchical k-mer decomposition to generate scale-invariant features that preserve complete sequence information while enabling diverse analytical approaches. Our framework bridges three distinct paradigms for sequence analysis: (1) traditional machine learning using extracted geometric features, (2) computer vision models operating on CGR-generated images, and (3) hybrid approaches combining protein language model embeddings with CGR features. Through comprehensive experiments on synthetic DNA and protein datasets encompassing seven distinct sequence classes, we demonstrate that MS-RCGR features consistently enhance classification performance across all paradigms. Notably, our hybrid approach combining pre-trained language model embeddings (ESM2, ProtT5) with MS-RCGR features achieves superior performance compared to either method alone. The reversibility property of our encoding ensures no information loss during transformation, while multi-scale analysis captures patterns ranging from individual nucleotides to complex motif structures. Our results indicate that MS-RCGR provides a flexible, interpretable, and high-performing foundation for biological sequence analysis.

---


### 511. [OneVL: One-Step Latent Reasoning and Planning with Vision-Language Explanation](https://arxiv.org/abs/2604.18486)

**<font color=#1a73e8>作者：</font>** Jinghui Lu, Jiayi Guan, Zhijian Huang 等 50 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chain-of-Thought (CoT) reasoning has become a powerful driver of trajectory prediction in VLA-based autonomous driving, yet its autoregressive nature imposes a latency cost that is prohibitive for real-time deployment. Latent CoT methods attempt to close this gap by compressing reasoning into continuous hidden states, but consistently fall short of their explicit counterparts. We suggest that this is due to purely linguistic latent representations compressing a symbolic abstraction of the world, rather than the causal dynamics that actually govern driving. Thus, we present OneVL (One-step latent reasoning and planning with Vision-Language explanations), a unified VLA and World Model framework that routes reasoning through compact latent tokens supervised by dual auxiliary decoders. Alongside a language decoder that reconstructs text CoT, we introduce a visual world model decoder that predicts future-frame tokens, forcing the latent space to internalize the causal dynamics of road geometry, agent motion, and environmental change. A three-stage training pipeline progressively aligns these latents with trajectory, language, and visual objectives, ensuring stable joint optimization. At inference, the auxiliary decoders are discarded and all latent tokens are prefilled in a single parallel pass, matching the speed of answer-only prediction. Across four benchmarks, OneVL becomes the first latent CoT method to surpass explicit CoT, delivering state-of-the-art accuracy at answer-only latency, and providing direct evidence that tighter compression, when guided in both language and world-model supervision, produces more generalizable representations than verbose token-by-token reasoning. Project Page: this https URL

---


### 512. [Adversarial Humanities Benchmark: Results on Stylistic Robustness in Frontier Model Safety](https://arxiv.org/abs/2604.18487)

**<font color=#1a73e8>作者：</font>** Marcello Galisai, Susanna Cifani, Francesco Giarrusso 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The Adversarial Humanities Benchmark (AHB) evaluates whether model safety refusals survive a shift away from familiar harmful prompt forms. Starting from harmful tasks drawn from MLCommons AILuminate, the benchmark rewrites the same objectives through humanities-style transformations while preserving intent. This extends literature on Adversarial Poetry and Adversarial Tales from single jailbreak operators to a broader benchmark family of stylistic obfuscation and goal concealment. In the benchmark results reported here, the original attacks record 3.84% attack success rate (ASR), while transformed methods range from 36.8% to 65.0%, yielding 55.75% overall ASR across 31 frontier models. Under a European Union AI Act Code-of-Practice-inspired systemic-risk lens, Chemical, biological, radiological and nuclear (CBRN) is the highest bucket. Taken together, this lack of stylistic robustness suggests that current safety techniques suffer from weak generalization: deep understanding of 'non-maleficence' remains a central unresolved problem in frontier model safety.

---


### 513. [LQM: Linguistically Motivated Multidimensional Quality Metrics for Machine Translation](https://arxiv.org/abs/2604.18490)

**<font color=#1a73e8>作者：</font>** Samar M. Magdy, Fakhraddin Alwajih, Abdellah El Mekki 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing MT evaluation frameworks, including automatic metrics and human evaluation schemes such as Multidimensional Quality Metrics (MQM), are largely language-agnostic. However, they often fail to capture dialect- and culture-specific errors in diglossic languages (e.g., Arabic), where translation failures stem from mismatches in language variety, content coverage, and pragmatic appropriateness rather than surface form this http URL introduce LQM: Linguistically Motivated Multidimensional Quality Metrics for MT. LQM is a hierarchical error taxonomy for diagnosing MT errors through six linguistically grounded levels: sociolinguistics, pragmatics, semantics, morphosyntax, orthography, and graphetics (Figure 1). We construct a bidirectional parallel corpus of 3,850 sentences (550 per variety) spanning seven Arabic dialects (Egyptian, Emirati, Jordanian, Mauritanian, Moroccan, Palestinian, and Yemeni), derived from conversational, culturally rich content. We evaluate six LLMs in a zero-shot setting and conduct expert span-level human annotation using LQM, producing 6,113 labeled error spans across 3,495 unique erroneous sentences, along with severity-weighted quality scores. We complement this analysis with an automatic metric (spBLEU). Though validated here on Arabic, LQM is a language-agnostic framework designed to be easily applied to or adapted for other languages. LQM annotated errors data, prompts, and annotation guidelines are publicly available at this https URL.

---


### 514. [Faster by Design: Interactive Aerodynamics via Neural Surrogates Trained on Expert-Validated CFD](https://arxiv.org/abs/2604.18491)

**<font color=#1a73e8>作者：</font>** Nicholas Thumiger, Andrea Bartezzaghi, Mattia Rigotti 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Computational Fluid Dynamics (CFD) is central to race-car aerodynamic development, yet its cost -- tens of thousands of core-hours per high-fidelity evaluation -- severely limits the design space exploration feasible within realistic budgets. AI-based surrogate models promise to alleviate this bottleneck, but progress has been constrained by the limited complexity of public datasets, which are dominated by smoothed passenger-car shapes that fail to exercise surrogates on the thin, complex, highly loaded components governing motorsport performance. This work presents three primary contributions. First, we introduce a high-fidelity RANS dataset built on a parametric LMP2-class CAD model and spanning six operating conditions (map points) covering straight-line and cornering regimes, generated and validated by aerodynamics experts at Dallara to preserve features relevant to industrial motorsport. Second, we present the Gauge-Invariant Spectral Transformer (GIST), a graph-based neural operator whose spectral embeddings encode mesh connectivity to enhance predictions on tightly packed, complex geometries. GIST guarantees discretization invariance and scales linearly with mesh size, achieving state-of-the-art accuracy on both public benchmarks and the proposed race-car dataset. Third, we demonstrate that GIST achieves a level of predictive accuracy suitable for early-stage aerodynamic design, providing a first validation of the concept of interactive design-space exploration -- where engineers query a surrogate in place of the CFD solver -- within industrial motorsport workflows.

---


### 515. [Barrier-enforced multi-objective optimization for direct point and sharp interval forecasting](https://arxiv.org/abs/2604.18492)

**<font color=#1a73e8>作者：</font>** Worachit Amnuaypongsa, Yotsapat Suparanonrat, Pana Wanitchollakit 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper proposes a multi-step probabilistic forecasting framework using a single neural-network based model to generate simultaneous point and interval forecasts. Our approach ensures non-crossing prediction intervals (PIs) through a model structure design that strictly satisfy a target coverage probability (PICP) while maximizing sharpness. Unlike existing methods that rely on manual weight tuning for scalarized loss functions, we treat point and PI forecasting as a multi-objective optimization problem, utilizing multi-gradient descent to adaptively select optimal weights. Key innovations include a new PI loss function based on an extended log-barrier with an adaptive hyperparameter to guarantee the coverage, a hybrid architecture featuring a shared temporal model with horizon-specific submodels, and a training strategy. The proposed loss is scale-independent and universally applicable; combined with our training algorithm, the framework eliminates trial-and-error hyperparameter tuning for balancing multiple objectives. Validated by an intra-day solar irradiance forecasting application, results demonstrate that our proposed loss consistently outperforms those in current literature by achieving target coverage with the narrowest PI widths. Furthermore, when compared against LSTM encoder-decoder and Transformer architectures--including those augmented with Chronos foundation models--our method remains highly competitive and can be seamlessly adapted to any deep learning structure.

---


### 516. [Too Correct to Learn: Reinforcement Learning on Saturated Reasoning Data](https://arxiv.org/abs/2604.18493)

**<font color=#1a73e8>作者：</font>** Zhenwen Liang, Yujun Zhou, Sidi Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) enhances LLM reasoning, yet a paradox emerges as models scale: strong base models saturate standard benchmarks (e.g., MATH), yielding correct but homogeneous solutions. In such environments, the lack of failure cases causes the advantage signal in group-relative algorithms (e.g., GRPO) to vanish, driving policies into mode collapse. To address this, we propose Constrained Uniform Top-K Sampling (CUTS), a parameter-free decoding strategy enforcing structure-preserving exploration. Unlike standard sampling that follows model biases, CUTS flattens the local optimization landscape by sampling uniformly from constrained high-confidence candidates. We integrate this into Mixed-CUTS, a training framework synergizing exploitative and exploratory rollouts to amplify intra-group advantage variance. Experiments on Qwen3 models demonstrate that our approach prevents policy degeneration and significantly boosts out-of-domain generalization. Notably, Mixed-CUTS improves Pass@1 accuracy on the challenging AIME25 benchmark by up to 15.1% over standard GRPO, validating that maintaining diversity within the semantic manifold is critical for rigorous reasoning.

---


### 517. [UDM-GRPO: Stable and Efficient Group Relative Policy Optimization for Uniform Discrete Diffusion Models](https://arxiv.org/abs/2604.18518)

**<font color=#1a73e8>作者：</font>** Jiaqi Wang, Haoge Deng, Ting Pan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Uniform Discrete Diffusion Model (UDM) has recently emerged as a promising paradigm for discrete generative modeling; however, its integration with reinforcement learning remains largely unexplored. We observe that naively applying GRPO to UDM leads to training instability and marginal performance gains. To address this, we propose \Ours, the first framework to integrate UDM with RL. Our method is guided by two key insights: (i) treating the final clean sample as the action provides more accurate and stable optimization signals; and (ii) reconstructing trajectories via the diffusion forward process better aligns probability paths with the pretraining distribution. Additionally, we introduce two strategies, Reduced-Step and CFG-Free, to further improve training efficiency. \Ours significantly improves base model performance across multiple T2I tasks. Notably, GenEval accuracy improves from $69\%$ to $96\%$ and PickScore increases from $20.46$ to $23.81$, achieving state-of-the-art performance in both continuous and discrete settings. On the OCR benchmark, accuracy rises from $8\%$ to $57\%$, further validating the generalization ability of our method. Code is available at \href{this https URL}{this https URL}.

---


### 518. [IDOBE: Infectious Disease Outbreak forecasting Benchmark Ecosystem](https://arxiv.org/abs/2604.18521)

**<font color=#1a73e8>作者：</font>** Aniruddha Adiga, Jingyuan Chou, Anshul Chiranth 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Epidemic forecasting has become an integral part of real-time infectious disease outbreak response. While collaborative ensembles composed of statistical and machine learning models have become the norm for real-time forecasting, standardized benchmark datasets for evaluating such methods are lacking. Further, there is limited understanding on performance of these methods for novel outbreaks with limited historical data. In this paper, we propose IDOBE, a curated collection of epidemiological time series focused on outbreak forecasting. IDOBE compiles from multiple data repositories spanning over a century of surveillance and across U.S. states and global locations. We perform derivative-based segmentation to generate over 10,000 outbreaks covering multiple outcomes such as cases and hospitalizations for 13 diseases. We consider a variety of information-theoretic and distributional measures to quantify the epidemiological diversity of the dataset. Finally, we perform multi-horizon short-term forecasting (1- to 4-week-ahead) through the progression of the outbreak using 11 baseline models and report on their performance. In addition to standard metrics such as NMSE and MAPE for point forecasts, we include probabilistic scoring rules such as Normalized Weighted Interval Score (NWIS) to quantify the performance. We find that MLP-based methods have the most robust performance, with statistical methods having a slight edge during the pre-peak phase. IDOBE dataset along with baselines are released publicly on this https URL to enable standardized, reproducible benchmarking of outbreak forecasting methods.

---


### 519. [MetaCloak-JPEG: JPEG-Robust Adversarial Perturbation for Preventing Unauthorized DreamBooth-Based Deepfake Generation](https://arxiv.org/abs/2604.18537)

**<font color=#1a73e8>作者：</font>** Tanjim Rahaman Fardin, S M Zunaid Alam, Mahadi Hasan Fahim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid progress of subject-driven text-to-image synthesis, and in particular DreamBooth, has enabled a consent-free deepfake pipeline: an adversary needs only 4-8 publicly available face images to fine-tune a personalized diffusion model and produce photorealistic harmful content. Current adversarial face-protection systems -- PhotoGuard, Anti-DreamBooth, and MetaCloak -- perturb user images to disrupt surrogate fine-tuning, but all share a structural blindness: none backpropagates gradients through the JPEG compression pipeline that every major social-media platform applies before adversary access. Because JPEG quantization relies on round(), whose derivative is zero almost everywhere, adversarial energy concentrates in high-frequency DCT bands that JPEG discards, eliminating 60-80% of the protective signal. We introduce MetaCloak-JPEG, which closes this gap by inserting a Differentiable JPEG (DiffJPEG) layer built on the Straight-Through Estimator (STE): the forward pass applies standard JPEG compression, while the backward pass replaces round() with the identity. DiffJPEG is embedded in a JPEG-aware EOT distribution (~70% of augmentations include DiffJPEG) and a curriculum quality-factor schedule (QF: 95 to 50) inside a bilevel meta-learning loop. Under an l-inf perturbation budget of eps=8/255, MetaCloak-JPEG attains 32.7 dB PSNR, a 91.3% JPEG survival rate, and outperforms PhotoGuard on all 9 evaluated JPEG quality factors (9/9 wins, mean denoising-loss gain +0.125) within a 4.1 GB training-memory budget.

---


### 520. [Fast and Forgettable: A Controlled Study of Novices' Performance, Learning, Workload, and Emotion in AI-Assisted and Human Pair Programming Paradigms](https://arxiv.org/abs/2604.18538)

**<font color=#1a73e8>作者：</font>** Nicholas Gardella, James Prather, Juho Leinonen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Code-generating Artificial Intelligence has gained popularity within both professional and educational programming settings over the past several years. While research and pedagogy are beginning to cope with this change, computing students are left to bear the unforeseen consequences of AI amidst a dearth of empirical evidence about its effects. Though pair programming between students is well studied and known to be beneficial to self-efficacy and academic achievement, it remains underutilized and further threatened by the proposition that AI can replace a human programming partner. In this paper, we present a controlled pair programming study with 22 participants who wrote Python code under time pressure in teams of two and individually with GitHub Copilot for 20 minutes each. They were incentivized by bonus compensation to balance performance with understanding and were retested individually on the programming tasks after a retention interval of one week. Subjective measures of workload and emotion as well as objective measures of performance and learning (retest performance) were collected. Results showed that participants performed significantly better with GitHub Copilot than their human teammate, and several dimensions of their workload were significantly reduced. However, the emotional effect of the human teammate was significantly more positive and arousing as compared to working with Copilot. Furthermore, there was a nonsignificant absolute retest performance reduction in the AI condition and a larger retest performance decrement in the AI condition. We recommend that educators strongly consider revisiting pair programming as an educational tool in addition to embracing modern AI.

---


### 521. [Transition-Matrix Regularization for Next Dialogue Act Prediction in Counselling Conversations](https://arxiv.org/abs/2604.18539)

**<font color=#1a73e8>作者：</font>** Eric Rudolph, Philipp Steigerwald, Jens Albrecht  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper studies how empirical dialogue-flow statistics can be incorporated into Next Dialogue Act Prediction (NDAP). A KL regularization term is proposed that aligns predicted act distributions with corpus-derived transition patterns. Evaluated on a 60-class German counselling taxonomy using 5-fold cross-validation, this improves macro-F1 by 9--42% relative depending on encoder and substantially improves dialogue-flow alignment. Cross-dataset validation on HOPE suggests that improvements transfer across languages and counselling domains. In systematic ablations across pretrained encoders and architectures, the findings indicate that transition regularization provides consistent gains and disproportionately benefits weaker baseline models. The results suggest that lightweight discourse-flow priors complement pretrained encoders, especially in fine-grained, data-sparse dialogue tasks.

---


### 522. [ClawEnvKit: Automatic Environment Generation for Claw-Like Agents](https://arxiv.org/abs/2604.18543)

**<font color=#1a73e8>作者：</font>** Xirui Li, Ming Li, Derry Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Constructing environments for training and evaluating claw-like agents remains a manual, human-intensive process that does not scale. We argue that what is needed is not just a dataset, but an automated pipeline capable of generating diverse, verified environments on demand. To this end, we introduce ClawEnvKit, an autonomous generation pipeline that instantiates this formalism from natural language descriptions. The pipeline comprises three modules: (1) a parser that extracts structured generation parameters from natural language input; (2) a generator that produces the task specification, tool interface, and scoring configuration; and (3) a validator that enforces feasibility, diversity, structural validity, and internal consistency across the generated environments. Using ClawEnvKit, we construct Auto-ClawEval, the first large-scale benchmark for claw-like agents, comprising 1,040 environments across 24 categories. Empirically, Auto-ClawEval matches or exceeds human-curated environments on coherence and clarity at 13,800x lower cost. Evaluated across 4 model families and 8 agent harness frameworks, we find that harness engineering boosts performance by up to 15.7 percentage points over a bare ReAct baseline, completion remains the primary axis of variation with no model saturating the benchmark, and automated generation enables evaluation at a scale previously infeasible. Beyond static benchmarking, ClawEnvKit enables live evaluation: users describe a desired capability in natural language and obtain a verified environment on demand, turning evaluation into a continuous, user-driven process. The same mechanism serves as an on-demand training environment generator, producing task distributions that adapt to an agent's current weaknesses rather than being bounded by existing user logs.

---


### 523. [Wasserstein Distributionally Robust Risk-Sensitive Estimation via Conditional Value-at-Risk](https://arxiv.org/abs/2604.18546)

**<font color=#1a73e8>作者：</font>** Feras Al Taha, Eilyan Bitar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a distributionally robust approach to risk-sensitive estimation of an unknown signal x from an observed signal y. The unknown signal and observation are modeled as random vectors whose joint probability distribution is unknown, but assumed to belong to a given type-2 Wasserstein ball of distributions, termed the ambiguity set. The performance of an estimator is measured according to the conditional value-at-risk (CVaR) of the squared estimation error. Within this framework, we study the problem of computing affine estimators that minimize the worst-case CVaR over all distributions in the given ambiguity set. As our main result, we show that, when the nominal distribution at the center of the Wasserstein ball is finitely supported, such estimators can be exactly computed by solving a tractable semidefinite program. We evaluate the proposed estimators on a wholesale electricity price forecasting task using real market data and show that they deliver lower out-of-sample CVaR of squared error compared to existing methods.

---


### 524. [Physics-Informed Neural Networks for Biological $2\mathrm{D}{+}t$ Reaction-Diffusion Systems](https://arxiv.org/abs/2604.18548)

**<font color=#1a73e8>作者：</font>** William Lavery, Jodie A. Cochrane, Christian Olesen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural networks (PINNs) provide a powerful framework for learning governing equations of dynamical systems from data. Biologically-informed neural networks (BINNs) are a variant of PINNs that preserve the known differential operator structure (e.g., reaction-diffusion) while learning constitutive terms via trainable neural subnetworks, enforced through soft residual penalties. Existing BINN studies are limited to $1\mathrm{D}{+}t$ reaction-diffusion systems and focus on forward prediction, using the governing partial differential equation as a regulariser rather than an explicit identification target. Here, we extend BINNs to $2\mathrm{D}{+}t$ systems within a PINN framework that combines data preprocessing, BINN-based equation learning, and symbolic regression post-processing for closed-form equation discovery. We demonstrate the framework's real-world applicability by learning the governing equations of lung cancer cell population dynamics from time-lapse microscopy data, recovering $2\mathrm{D}{+}t$ reaction-diffusion models from experimental observations. The proposed framework is readily applicable to other spatio-temporal systems, providing a practical and interpretable tool for fast analytic equation discovery from data.

---


### 525. [Advancing Vision Transformer with Enhanced Spatial Priors](https://arxiv.org/abs/2604.18549)

**<font color=#1a73e8>作者：</font>** Qihang Fan, Huaibo Huang, Mingrui Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In recent years, the Vision Transformer (ViT) has garnered significant attention within the computer vision community. However, the core component of ViT, Self-Attention, lacks explicit spatial priors and suffers from quadratic computational complexity, limiting its applicability. To address these issues, we have proposed RMT, a robust vision backbone with explicit spatial priors for general purposes. RMT utilizes Manhattan distance decay to introduce spatial information and employs a horizontal and vertical decomposition attention method to model global information. Building on the strengths of RMT, Euclidean enhanced Vision Transformer (EVT) is an expanded version that incorporates several key improvements. Firstly, EVT uses a more reasonable Euclidean distance decay to enhance the modeling of spatial information, allowing for a more accurate representation of spatial relationships compared to the Manhattan distance used in RMT. Secondly, EVT abandons the decomposed attention mechanism featured in RMT and instead adopts a simpler spatially-independent grouping approach, providing the model with greater flexibility in controlling the number of tokens within each group. By addressing these modifications, EVT offers a more sophisticated and adaptable approach to incorporating spatial priors into the Self-Attention mechanism, thus overcoming some of the limitations associated with RMT and further enhancing its applicability in various computer vision tasks. Extensive experiments on Image Classification, Object Detection, Instance Segmentation, and Semantic Segmentation demonstrate that EVT exhibits exceptional performance. Without additional training data, EVT achieves 86.6% top1-acc on ImageNet-1k.

---


### 526. [Do Privacy Policies Match with the Logs? An Empirical Study of Privacy Disclosure in Android Application Logs](https://arxiv.org/abs/2604.18552)

**<font color=#1a73e8>作者：</font>** Zhiyuan Chen, Love Jayesh Ahir, Ahmad Suleiman 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Privacy policies are intended to inform users about how software systems collect and handle data, yet they often remain vague or incomplete. This paper presents an empirical study of patterns in log-related statements within privacy policies and their alignment with privacy disclosures observed in Android application logs. We analyzed 1,000 Android apps across multiple categories, generating 86,836,964 log entries. Our findings reveal that while most applications (88.0%) provide privacy policies, only 28.5% explicitly mention logging practices. Among those that reference logging, most clearly describe what information is logged; however, 27.7% of log-related statements remain overly simplistic or vague, offering limited insight into actual data collection. We further observed widespread privacy leakages in application logs, with 67.6% of apps leaking sensitive information not mentioned in their policies. Alarmingly, only 4% of applications demonstrated consistent alignment between declared policy contents and actual logged data. These findings highlight that current privacy policies provide incomplete or ambiguous descriptions of logging practices, which frequently do not align with actual logging behaviors.

---


### 527. [A Note on TurboQuant and the Earlier DRIVE/EDEN Line of Work](https://arxiv.org/abs/2604.18555)

**<font color=#1a73e8>作者：</font>** Ran Ben-Basat, Yaniv Ben-Itzhak, Gal Mendelson 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This note clarifies the relationship between the recent TurboQuant work and the earlier DRIVE (NeurIPS 2021) and EDEN (ICML 2022) schemes. DRIVE is a 1-bit quantizer that EDEN extended to any $b>0$ bits per coordinate; we refer to them collectively as EDEN.
First, TurboQuant$_{\text{mse}}$ is a special case of EDEN obtained by fixing EDEN's scalar scale parameter to $S=1$. EDEN supports both biased and unbiased quantization, each optimized by a different $S$ (chosen via methods described in the EDEN works). The fixed choice $S=1$ used by TurboQuant is generally suboptimal, although the optimal $S$ for biased EDEN converges to $1$ as the dimension grows; accordingly TurboQuant$_{\text{mse}}$ approaches EDEN's behavior for large $d$.
Second, TurboQuant$_{\text{prod}}$ combines a biased $(b-1)$-bit EDEN step with an unbiased 1-bit QJL quantization of the residual. It is suboptimal in three ways: (1) its $(b-1)$-bit step uses the suboptimal $S=1$; (2) its 1-bit unbiased residual quantization has worse MSE than (unbiased) 1-bit EDEN; (3) chaining a biased $(b-1)$-bit step with a 1-bit unbiased residual step is inferior to unbiasedly quantizing the input directly with $b$-bit EDEN.
Third, some of the analysis in the TurboQuant work mirrors that of the EDEN works: both exploit the connection between random rotations and the shifted Beta distribution, use the Lloyd-Max algorithm, and note that Randomized Hadamard Transforms can replace uniform random rotations.
Experiments support these claims: biased EDEN (with optimized $S$) is more accurate than TurboQuant$_{\text{mse}}$, and unbiased EDEN is markedly more accurate than TurboQuant$_{\text{prod}}$, often by more than a bit (e.g., 2-bit EDEN beats 3-bit TurboQuant$_{\text{prod}}$). We also repeat all accuracy experiments from the TurboQuant paper, showing that EDEN outperforms it in every setup we have tried.

---


### 528. [SynAgent: Generalizable Cooperative Humanoid Manipulation via Solo-to-Cooperative Agent Synergy](https://arxiv.org/abs/2604.18557)

**<font color=#1a73e8>作者：</font>** Wei Yao, Haohan Ma, Hongwen Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Controllable cooperative humanoid manipulation is a fundamental yet challenging problem for embodied intelligence, due to severe data scarcity, complexities in multi-agent coordination, and limited generalization across objects. In this paper, we present SynAgent, a unified framework that enables scalable and physically plausible cooperative manipulation by leveraging Solo-to-Cooperative Agent Synergy to transfer skills from single-agent human-object interaction to multi-agent human-object-human scenarios. To maintain semantic integrity during motion transfer, we introduce an interaction-preserving retargeting method based on an Interact Mesh constructed via Delaunay tetrahedralization, which faithfully maintains spatial relationships among humans and objects. Building upon this refined data, we propose a single-agent pretraining and adaptation paradigm that bootstraps synergistic collaborative behaviors from abundant single-human data through decentralized training and multi-agent PPO. Finally, we develop a trajectory-conditioned generative policy using a conditional VAE, trained via multi-teacher distillation from motion imitation priors to achieve stable and controllable object-level trajectory execution. Extensive experiments demonstrate that SynAgent significantly outperforms existing baselines in both cooperative imitation and trajectory-conditioned control, while generalizing across diverse object geometries. Codes and data will be available after publication. Project Page: this http URL

---


### 529. [AnchorSeg: Language Grounded Query Banks for Reasoning Segmentation](https://arxiv.org/abs/2604.18562)

**<font color=#1a73e8>作者：</font>** Rui Qian, Chuanhang Deng, Qiang Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reasoning segmentation requires models to ground complex, implicit textual queries into precise pixel-level masks. Existing approaches rely on a single segmentation token $\texttt{<SEG>}$, whose hidden state implicitly encodes both semantic reasoning and spatial localization, limiting the model's ability to explicitly disentangle what to segment from where to segment. We introduce AnchorSeg, which reformulates reasoning segmentation as a structured conditional generation process over image tokens, conditioned on language grounded query banks. Instead of compressing all semantic reasoning and spatial localization into a single embedding, AnchorSeg constructs an ordered sequence of query banks: latent reasoning tokens that capture intermediate semantic states, and a segmentation anchor token that provides explicit spatial grounding. We model spatial conditioning as a factorized distribution over image tokens, where the anchor query determines localization signals while contextual queries provide semantic modulation. To bridge token-level predictions and pixel-level supervision, we propose Token--Mask Cycle Consistency (TMCC), a bidirectional training objective that enforces alignment across resolutions. By explicitly decoupling spatial grounding from semantic reasoning through structured language grounded query banks, AnchorSeg achieves state-of-the-art results on ReasonSeg test set (67.7\% gIoU and 68.1\% cIoU). All code and models are publicly available at this https URL.

---


### 530. [Latent Phase-Shift Rollback: Inference-Time Error Correction via Residual Stream Monitoring and KV-Cache Steering](https://arxiv.org/abs/2604.18567)

**<font color=#1a73e8>作者：</font>** Manan Gupta, Dhruv Kumar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models frequently commit unrecoverable reasoning errors mid-generation: once a wrong step is taken, subsequent tokens compound the mistake rather than correct it. We introduce $\textbf{Latent Phase-Shift Rollback}$ (LPSR): at each generation step, we monitor the residual stream at a critical layer lcrit, detect abrupt directional reversals (phase shifts) via a cosine-similarity $+$ entropy dual gate, and respond by rolling back the KV-cache and injecting a pre-computed steering vector. No fine-tuning, gradient computation, or additional forward passes are required. LPSR achieves $\mathbf{44.0\%}$ on MATH-500 with an 8B model versus $28.8\%$ for standard AR ($+15.2$ pp; McNemar $\chi^2 = 66.96$, $p < 10^{-15}$). Critically, prompted self-correction, the most natural inference-time baseline, scores only $19.8\%$, below standard AR; LPSR exceeds it by $+24.2$ pp ($\chi^2 = 89.4$, $p \approx 0$). LPSR also outperforms Best-of-16 ($+7.8$ pp) at $5.4\times$ lower token cost, and surpasses a standard 70B model ($35.2\%$) with $8.75\times$ fewer parameters at ${\sim}3\times$ the token budget. A 32-layer sweep reveals a novel \textbf{detection-correction dissociation}: error-detection AUC peaks at layer~14 ($0.718$) but task accuracy peaks at layer~16 ($44.0\%$ vs.\ $29.2\%$), demonstrating that optimal monitoring depth differs for detection and correction.

---


### 531. [Back into Plato's Cave: Examining Cross-modal Representational Convergence at Scale](https://arxiv.org/abs/2604.18572)

**<font color=#1a73e8>作者：</font>** A. Sophia Koepke, Daniil Zverev, Shiry Ginosar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The Platonic Representation Hypothesis suggests that neural networks trained on different modalities (e.g., text and images) align and eventually converge toward the same representation of reality. If true, this has significant implications for whether modality choice matters at all. We show that the experimental evidence for this hypothesis is fragile and depends critically on the evaluation regime. Alignment is measured using mutual nearest neighbors on small datasets ($\approx$1K samples) and degrades substantially as the dataset is scaled to millions of samples. The alignment that remains between model representations reflects coarse semantic overlap rather than consistent fine-grained structure. Moreover, the evaluations in Huh et al. are done in a one-to-one image-caption setting, a constraint that breaks down in realistic many-to-many settings and further reduces alignment. We also find that the reported trend of stronger language models increasingly aligning with vision does not appear to hold for newer models. Overall, our findings suggest that the current evidence for cross-modal representational convergence is considerably weaker than subsequent works have taken it to be. Models trained on different modalities may learn equally rich representations of the world, just not the same one.

---


### 532. [ReCap: Lightweight Referential Grounding for Coherent Story Visualization](https://arxiv.org/abs/2604.18575)

**<font color=#1a73e8>作者：</font>** Aditya Arora, Akshita Gupta, Pau Rodriguez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Story Visualization aims to generate a sequence of images that faithfully depicts a textual narrative that preserve character identity, spatial configuration, and stylistic coherence as the narratives unfold. Maintaining such cross-frame consistency has traditionally relied on explicit memory banks, architectural expansion, or auxiliary language models, resulting in substantial parameter growth and inference overhead. We introduce ReCap, a lightweight consistency framework that improves character stability and visual fidelity without modifying the base diffusion backbone. ReCap's CORE (COnditional frame REferencing) module treats anaphors, in our case pronouns, as visual anchors, activating only when characters are referred to by a pronoun and conditioning on the preceding frame to propagate visual identity. This selective design avoids unconditional cross-frame conditioning and introduces only 149K additional parameters, a fraction of the cost of memory-bank and LLM-augmented approaches. To further stabilize identity, we incorporate SemDrift (Guided Semantic Drift Correction) applied only during training. When text is vague or referential, the denoiser lacks a visual anchor for identity-defining attributes, causing character appearance to drift across frames, SemDrift corrects this by aligning denoiser representations with pretrained DINOv3 visual embeddings, enforcing semantic identity stability at zero inference cost. ReCap outperforms previous state-of-the-art, StoryGPT-V, on the two main benchmarks for story visualization by 2.63% Character-Accuracy on FlintstonesSV and by 5.65% on PororoSV, establishing a new state-of-the-art character consistency on both benchmarks. Furthermore, we extend story visualization to human-centric narratives derived from real films, demonstrating the capability of ReCap beyond stylized cartoon domains.

---


### 533. [Bounded Ratio Reinforcement Learning](https://arxiv.org/abs/2604.18578)

**<font color=#1a73e8>作者：</font>** Yunke Ao, Le Chen, Bruce D. Lee 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Proximal Policy Optimization (PPO) has become the predominant algorithm for on-policy reinforcement learning due to its scalability and empirical robustness across domains. However, there is a significant disconnect between the underlying foundations of trust region methods and the heuristic clipped objective used in PPO. In this paper, we bridge this gap by introducing the Bounded Ratio Reinforcement Learning (BRRL) framework. We formulate a novel regularized and constrained policy optimization problem and derive its analytical optimal solution. We prove that this solution ensures monotonic performance improvement. To handle parameterized policy classes, we develop a policy optimization algorithm called Bounded Policy Optimization (BPO) that minimizes an advantage-weighted divergence between the policy and the analytic optimal solution from BRRL. We further establish a lower bound on the expected performance of the resulting policy in terms of the BPO loss function. Notably, our framework also provides a new theoretical lens to interpret the success of the PPO loss, and connects trust region policy optimization and the Cross-Entropy Method (CEM). We additionally extend BPO to Group-relative BPO (GBPO) for LLM fine-tuning. Empirical evaluations of BPO across MuJoCo, Atari, and complex IsaacLab environments (e.g., Humanoid locomotion), and of GBPO for LLM fine-tuning tasks, demonstrate that BPO and GBPO generally match or outperform PPO and GRPO in stability and final performance.

---


### 534. [Sessa: Selective State Space Attention](https://arxiv.org/abs/2604.18580)

**<font color=#1a73e8>作者：</font>** Liubomyr Horbatko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern sequence models are dominated by Transformers, where self-attention mixes information from the visible context in an input-dependent way. However, when retrieval is not sharp and attention remains diffuse over an effective support $S_{\mathrm{eff}}(t)$, the influence of any individual token is diluted, typically scaling as $O(1/S_{\mathrm{eff}}(t))$ and reaching $O(1/\ell)$ for old tokens in full-prefix settings. Structured state-space models process sequences recurrently through an explicit feedback path; selective variants such as Mamba make this feedback input-dependent, yet when freeze time cannot be sustained over long intervals, their long-range sensitivity decays exponentially with lag. Existing architectures therefore either retrieve from the past in a single read or propagate information through a single feedback chain. We introduce Sessa, a decoder that places attention inside a feedback path, enabling recurrent many-path aggregation within a layer. Under stated assumptions, Sessa admits regimes with a power-law memory tail in lag $\ell$ of order $O(\ell^{-\beta})$ for $0<\beta<1$, which is asymptotically slower than $1/\ell$; moreover, this rate is tight in an explicit diffuse uniform-routing setting where the influence is $\Theta(\ell^{-\beta})$. Under the same conditions, only Sessa among the compared model classes realizes flexible selective retrieval, including non-decaying profiles. Empirically, under matched architectures and training budgets, Sessa achieves the strongest performance on our long-context benchmarks while remaining competitive with Transformer and Mamba style baselines on short-context language modeling.

---


### 535. [MUA: Mobile Ultra-detailed Animatable Avatars](https://arxiv.org/abs/2604.18583)

**<font color=#1a73e8>作者：</font>** Heming Zhu, Guoxing Sun, Marc Habermann  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Building photorealistic, animatable full-body digital humans remains a longstanding challenge in computer graphics and vision. Recent advances in animatable avatar modeling have largely progressed along two directions: improving the fidelity of dynamic geometry and appearance, or reducing computational complexity to enable deployment on resource-constrained platforms, e.g., VR headsets. However, existing approaches fail to achieve both goals simultaneously: Ultra-high-fidelity avatars typically require substantial computation on server-class GPUs, whereas lightweight avatars often suffer from limited surface dynamics, reduced appearance details, and noticeable artifacts. To bridge this gap, we propose a novel animatable avatar representation, termed Wavelet-guided Multi-level Spatial Factorized Blendshapes, and a corresponding distillation pipeline that transfers motion-aware clothing dynamics and fine-grained appearance details from a pre-trained ultra-high-quality avatar model into a compact, efficient representation. By coupling multi-level wavelet spectral decomposition with low-rank structural factorization in texture space, our method achieves up to 2000X lower computational cost and a 10X smaller model size than the original high-quality teacher avatar model, while preserving visually plausible dynamics and appearance details closely resemble those of the teacher model. Extensive comparisons with state-of-the-art methods show that our approach significantly outperforms existing avatar approaches designed for mobile settings and achieves comparable or superior rendering quality to most approaches that can only run on servers. Importantly, our representation substantially improves the practicality of high-fidelity avatars for immersive applications, achieving over 180 FPS on a desktop PC and real-time native on-device performance at 24 FPS on a standalone Meta Quest 3.

---


> [!TIP]
> 当前位于：**501-535**（第 11/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-535**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
