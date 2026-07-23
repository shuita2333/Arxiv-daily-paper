# 📦 其他研究 | 2026年07月24日

> 本类共 **192** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-192](./part-04.md)

---

### 101. [Overview of FinMMEval 2026 Task 2: Multilingual Financial Short-Answer Question Answering](https://arxiv.org/abs/2607.19867)

**<font color=#1a73e8>作者：</font>** Zhuohan Xie, Xueqing Peng, Georgi Georgiev 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> FinMMEval 2026 Task 2 evaluates short-answer financial question answering over multilingual evidence. Each final-test item pairs an English question with financial statements and news in English, Chinese, Japanese, Spanish, and Greek. Participating systems submit one concise answer per item in JSONL format. The final-test set contains 256 items, split evenly between easy and expert tiers; each tier contains four question templates instantiated over 32 company-report groups. Gold answers were withheld during submission, and systems were ranked by macro-averaged item-level ROUGE-1 F1 against organizer-held reference answers. The final leaderboard includes 12 ranked submissions. The strongest systems are closely clustered, with the top four separated by less than one percentage point in ROUGE-1 F1. The submitted system papers document retrieval-augmented generation, cross-lingual evidence handling, structured prompting, answer compression, and validation strategies.

---


### 102. [Robust Activation Map Rectification for Weakly Supervised Volumetric Segmentation: Temporal Coherence as a Free Lunch](https://arxiv.org/abs/2607.19877)

**<font color=#1a73e8>作者：</font>** Renshu Gu, Jialiang Chen, Fei Gao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Weakly supervised segmentation relies heavily on class activation maps (CAMs) to initially localize target regions. However, CAMs are often noisy and prone to catastrophic failures. Existing remedies typically introduce additional training stages or prototype learning, increasing computational cost and reducing robustness. In this paper, we propose a training-free prototype-free framework that rectifies unreliable CAMs by exploiting temporal and structural coherence in volumetric data as a free lunch. Our approach is built on two key components. First, we introduce Variance-Reduced Activation Aggregation (VRAA) which suppresses noise and amplify coherent semantic signals. We provide a theoretical justification by modeling CAMs as high-dimensional random vectors and show that aggregation yields provable variance reduction. Second, we design a Bidirectional Extremity Rectification (BER) mechanism that detects and rectifies implausible activations through bidirectional extremity checks, effectively mitigating extreme-value failures without learning additional parameters. Our method is model-agnostic and can be seamlessly integrated with existing pipelines. Extensive experiments on multiple public benchmarks demonstrate substantial improvements over state-of-the-art weakly supervised methods, achieving up to 20% Dice and 40% mIoU gains while reducing inference time by more than 5 times. These results indicate that leveraging coherence as an implicit inductive bias yields a principled and efficient approach to stabilizing weakly supervised volumetric segmentation. Our code will be available.

---


### 103. [Current Injection Spiking Neural Network for Infrared and Visible Image Fusion](https://arxiv.org/abs/2607.19879)

**<font color=#1a73e8>作者：</font>** Rui Zhao, Zhuoyuan Li, Wenrui Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrared and visible image fusion (IVIF) integrates the complementary information of two modalities into a single image with richer scene content. While existing methods are largely built on artificial neural networks (ANNs), which densely compute over all activations, spiking neural networks (SNNs) communicate through sparse binary spikes and compute only where and when a spike occurs, offering a route to more energy-efficient fusion. However, directly applying SNNs to IVIF creates a fundamental tension: cross-modal fusion relies on fine-grained responses from both modalities, whereas binary spikes can discard complementary cues that remain below the firing threshold. The membrane potential retains these subthreshold responses before firing, letting both modalities jointly shape the output when integrated at this stage. Building on this, we propose CIS-Fuse, a spiking network that performs cross-modal fusion directly at the membrane-potential level. At its core is the current injection spiking (CIS) operator, which injects one modality as a gated auxiliary current into the driving neuron of the other, so the two integrate before spike firing, with a per-channel learnable injection strength that adaptively regulates the modulation magnitude. Building on CIS, we construct a bidirectional cross-modal fusion (BCMF) module and deploy it on a dual-branch architecture with asymmetric stacking depths, where the two branches develop a clear functional specialization. Extensive experiments on four IVIF benchmarks and on downstream detection and segmentation show that CIS-Fuse achieves fusion quality on par with state-of-the-art ANN-based methods while inheriting the energy efficiency of spike-based computation, with roughly an order of magnitude lower inference energy than the similarly-sized ANN-based DCEvo. Code will be released upon publication.

---


### 104. [OSVE: One Step Video Editing with One Step Diffusion Models](https://arxiv.org/abs/2607.19895)

**<font color=#1a73e8>作者：</font>** Habin Lim, Gyeong-Moon Park  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-guided video editing with diffusion models is impractically slow, hindered by costly multi-step sampling and inversion. We present OSVE, the first framework to successfully adapt one-step Text-to-Image (T2I) models for high-quality video editing, addressing the core challenges of inversion, editability, and temporal consistency. To bypass slow iterative inversion, we train a learnable encoder that predicts the initial noise for each frame in a single forward pass. This encoder is trained with a novel Structure-Aware Editing (SAE) loss on a curated dataset of structurally-aligned image pairs, teaching it to preserve the source video's geometry during edits. For temporal coherence, we introduce Unified-Frame Editing (UFE), a technique that concatenates frame latents to facilitate cross-frame attention in a single generation step. Furthermore, for long videos, a sliding-window strategy with an anchor frame maintains global consistency. Our extensive experiments demonstrate that OSVE achieves editing quality comparable or superior to state-of-the-art multi-step methods, while operating approximately 155--171 times faster. This breakthrough paves the way for practical, real-time video editing applications. Code is available at this https URL.

---


### 105. [Harnessing Disagreement: Detecting Correlated Agreement Blindness in Multi-Agent Triage](https://arxiv.org/abs/2607.19899)

**<font color=#1a73e8>作者：</font>** Shay Seiya McDonnell, Avantika Singh, Quoc-Viet Pham 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Disagreement-triggered escalation can create a structural blind spot in multi-agent arbitration: as base learners improve, they tend to converge, weakening safety monitoring where correlated failures concentrate. We term this correlated agreement blindness and present ARAT (Arbitrated Reasoning Agents for Alarm Triage), a directed-star system combining an inductive Random Forest (RF) agent, an analogical case-based k-nearest neighbour (k-NN) agent, and a calibrated meta-model to mitigate this effect. On 82,332 holdout samples from the UNSW-NB15 network intrusion detection dataset, 57.2% of errors occur under agreement and 90.6% of dangerous under-predictions evade disagreement-based monitoring even after conservative override; ablation shows that strengthening base learners increases error correlation while reducing disagreement. ARAT reduces under-prediction relative to soft voting from 4.80% to 1.70% via conservative override (-2.6pp) and a safety-flag gate (-0.5pp), demonstrating architectural gains. Cross-dataset validation on clinical readmission supports these indicators, suggesting that diversification improves safety only when it generates productive disagreement rather than convergence. These results indicate that disagreement-triggered escalation can be blind to correlated failure, a risk that may intensify as agentic pipelines deploy increasingly capable, correlated models.

---


### 106. [StrokeSeg2: Stroke Lesion Segmentation in Clinical Research Workflows](https://arxiv.org/abs/2607.19901)

**<font color=#1a73e8>作者：</font>** Youwan Mahé, Axel Plessis, Stéphanie Leplaideur 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning frameworks like nnU-Net achieve state-of-theart brain lesion segmentation performance but remain difficult to deploy in clinical research environments due to, among other reasons, software dependencies and computational requirements. We introduce StrokeSeg2, a lightweight, modular, cross-platform C++/Qt framework designed to adapt resource-intensive 3D stroke segmentation pipelines into portable and reproducible applications. To improve compatibility with standard clinical workstations, we investigate the combined effect of architectural compression through knowledge distillation and inference optimisation using ONNX Runtime with Float16 quantisation. Across heterogeneous hardware configurations (CPU, integrated GPU, and dedicated GPU) architectural distillation emerged as the primary contributor to efficiency gains, contributing to over 90% reduction in energy consumption and an average 84% reduction in inference time. Specifically, we identify a 0.84M-parameter student model as the most favourable trade-off, reducing the original 102.3M-parameter teacher architecture to a 2.1 MB disk footprint while preserving robust lesion localisation and competitive segmentation performance. This small footprint supports the development of a self-contained installer for clinical workstation targets. Finally, StrokeSeg2 packages these optimisations into standalone installers for Windows, macOS, and Linux. By providing both graphical and commandline interfaces without Docker or external environment dependencies, StrokeSeg2 facilitates deployment of high-performance segmentation workflows for routine clinical research pipelines.

---


### 107. [Nonlinear Bias-Compensated Adaptive Filter and Its Application for Time-Series Prediction](https://arxiv.org/abs/2607.19902)

**<font color=#1a73e8>作者：</font>** Yi Peng, Haiquan Zhao, Jinhui Hu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most existing nonlinear adaptive filtering algorithms only account for output noise, neglecting the fact that input noise is also prevalent in practice. Although the recently proposed bias-compensated kernel least mean square (BCKLMS) algorithm addresses input noise in the nonlinear errors-in-variables (EIV) model, it still suffers from two major limitations. First, the use of a fixed-size dictionary restricts network growth but also prevents it from fully capturing the characteristics of the input signal. Second, as an least mean square (LMS) based algorithm, it exhibits poor robustness in the presence of non-Gaussian noise in the output signal. To overcome these issues, this paper proposes the random Fourier bias-compensated filter under general adaptive function (RFFBCGA) algorithm. Within the random Fourier feature based bias-compensated (RFFBC) framework, the proposed algorithm not only maintains a fixed network structure and effectively mitigates input noise interference through the BC term, but also achieves improved characterization of the input signal. Moreover, by leveraging the flexible form of the general adaptive (GA) function, the algorithm's robustness across various noise scenarios is further enhanced. Extensive simulations, including real-world time series prediction tasks, demonstrate the superiority of the proposed method.

---


### 108. [TargetFinder: Detecting Widgets from Pixels on Desktop Interfaces](https://arxiv.org/abs/2607.19907)

**<font color=#1a73e8>作者：</font>** Ahmed Ben Akouche, Géry Casiez, Mathieu Nancel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> ''Target-aware'' pointing techniques, like Bubble Cursor or Semantic Pointing, outperform traditional pointing by leveraging knowledge of target locations. Yet the lack of application-agnostic widget geometry information limits their adoption across the desktop. We present TargetFinder, a computer vision-based system for real-time detection of GUI widgets. TargetFinder leverages several fine-tuned YOLO networks trained on a new dataset of 520 annotated desktop screenshots (~38,000 annotations) spanning Windows, macOS, Ubuntu, and web interfaces. TargetFinder uses lightweight screen monitoring and low-latency detection, achieving millisecond responsiveness suitable for interactive use. Evaluations show that TargetFinder outperforms the baseline methods (OmniParser and REMAUI), while system-wide implementations of Bubble Cursor and Semantic Pointing demonstrate the feasibility of deploying universal target-aware techniques that work across applications. We release the dataset, models, annotation tool, and an open-source library for research and applications.

---


### 109. [LoRFT: Benchmarking Long-Range Vehicle Trajectory Reconstruction from Fixed Highway Cameras](https://arxiv.org/abs/2607.19911)

**<font color=#1a73e8>作者：</font>** Yufan Zhu, Kefu Yi, Xueju Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-range vehicle trajectories provide important spatio-temporal evidence for traffic safety analysis, autonomous driving evaluation, and data-driven traffic management, yet continuously recovering them from fixed highway cameras remains difficult. As vehicles recede into distant road regions, perspective compression and scale decay often fragment or prematurely terminate automatic tracklets, even when their continuation remains identifiable from motion consistency across neighboring frames. We formulate this problem as recovering the far-range continuation of a vehicle trajectory from a reliable near-field tracklet. We introduce LoRFT, to our knowledge the first open benchmark dedicated to long-range vehicle trajectory reconstruction from fixed highway cameras. LoRFT comprises 22 expressway surveillance scenes, 366,109 video frames, 6,601 manually verified trajectories, 2,694,889 bounding boxes, road-geometry annotations, scene-level splits, and evaluation scripts. We further propose Map-RSTNet, a map-aware residual sequence-to-sequence model that reconstructs distant trajectories in a road-geometry-aligned state space and dynamically refreshes local road geometry during decoding. On LoRFT, Map-RSTNet reduces ADE, FDE, and 5-second RMSE by 11.0%, 15.4%, and 10.5%, respectively, relative to the strongest baseline. These results demonstrate that road-geometry-aware reconstruction can extend usable trajectory records from existing fixed-camera infrastructure. LoRFT provides a reproducible testbed for long-range vehicle trajectory reconstruction.

---


### 110. [JANUS: Foreseeing Latent Risk for Long-Horizon Agent Safety](https://arxiv.org/abs/2607.19913)

**<font color=#1a73e8>作者：</font>** Yuan Xiong, Linji Hao, Shizhu He 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent safety is moving from content moderation toward preventing operational failures before tool-using agents act. We propose Janus, a foresight-oriented framework for long-horizon agent safety that trains guards to anticipate delayed risks from partial trajectories. Janus synthesizes diverse agent trajectories via multi-agent simulation and learns a shared policy with two coupled tasks: an anticipation task that forecasts safety-relevant futures and an adjudication task that decides safety from both the observed prefix and anticipated future. The two tasks are jointly optimized with CoAA-RL, which rewards forecasts by their utility for downstream safety judgment. The resulting guard model, Vanguard, blocks unsafe actions before execution. Across four agent-safety benchmarks, Vanguard improves average protection by 15.9 percentage points over baseline guards while increasing benign task completion by 5.1 percentage points.

---


### 111. [Long-Term Sequential Decision Making under Risk](https://arxiv.org/abs/2607.19914)

**<font color=#1a73e8>作者：</font>** Irmaan, Mirzanejad, Nadjet Bourdache 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study finite-horizon MDP planning under \emph{root-based} (resolute) risk objectives that apply a rank-dependent functional to the distribution of total returns. Such objectives are non-linear in the return distribution and generally break Bellman optimality, so direct optimization by scenario-tree enumeration is intractable. We propose \textbf{ERQDP}, an enumeration-free and sampling-free method that solves a rank--quantile surrogate via exact DP (Dynamic Programming), evaluates candidate policies exactly by DP over return Probability Mass Functions (PMFs) on a discretized return grid (with an explicit rounding bound), and refines the surrogate in an anytime loop that reports an explicit upper--lower gap (certificate) for the target objective up to discretization budgets. Across tested benchmarks, ERQDP returns certified solutions or explicit residual gaps, enables fast risk-parameter sweeps with substantial runtime gains, and supports both risk-averse and risk-seeking behaviors.

---


### 112. [A Framework of User Experience Principles for Human-AI Agent Interaction in the Workplace](https://arxiv.org/abs/2607.19941)

**<font color=#1a73e8>作者：</font>** Kathrin Paimann, Elizangela Valarini, Sebastian Juhl  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As AI agents become integral to business workflows, establishing guiding user experience (UX) principles is crucial for ensuring user trust and successful adoption. To address this, our study uses a multi-method approach - combining participatory design workshop, paper-and-pencil, expert review, meta-analysis, and in-depth interviews - to identify and validate a design framework of eight core UX principles for human-AI agent interaction in the workplace. Together with their underlying criteria, these principles provide actionable guardrails for designers and software engineers, creating a foundation for developing effective and human-centered AI agent interactions. This study contributes to a structured foundation for future empirical studies on agentic AI in enterprise settings.

---


### 113. [G-MAD: A Game-Based Data Generation Framework for Multi-View RGB-T Aerial Object Detection](https://arxiv.org/abs/2607.19942)

**<font color=#1a73e8>作者：</font>** Yechan Kim, JongHyun Park, Dongho Yoon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This work introduces G-MAD, an open-source framework that uses Arma3 to generate synchronized multi-view RGB-T data for aerial object detection. G-MAD addresses key limitations of real-world aerial dataset construction, including limited viewpoint control, imperfect RGB-T alignment and high annotation cost. The framework supports structured scenario specification, controllable multi-view camera placement, simultaneous visible/thermal capture, and automatic bounding box annotation using engine-level geometric metadata. These capabilities enable controlled studies of viewpoint variation, multi-modal fusion, and synthetic-to-real transfer in aerial object detection. Besides, using G-MAD, we construct and release AMOD, a new large-scale multi-view aerial RGB-T object detection benchmark. The source code and the dataset are available at this https URL.

---


### 114. [SIINR: Structurally Informed Implicit Neural Representations for super-resolution with uncertainty quantification of clinical quality diffusion MRI datasets](https://arxiv.org/abs/2607.19943)

**<font color=#1a73e8>作者：</font>** Tom Hendriks, William Consagra, Anna Vilanova 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Magnetic Resonance Imaging (dMRI) is a powerful tool for probing brain microstructure, but clinical acquisitions are often limited by low out-of-plane resolution, resulting in degraded structural information and reduced utility for advanced analysis. We introduce SIINR (Structurally Informed Implicit Neural Representations), a general framework for super-resoltion of clinical dMRI datasets while quantifying uncertainty in the reconstructed outputs. SIINR utilizes a supervised 3D U-net as a prior and combines it with a self-supervised implicit neural representation (INR) that fuses the high-resolution prior and the original low-resolution data. The INR enables joint modeling across spatial and angular domains, enforces data consistency, and provides analytic approximate posterior distributions for downstream uncertainty quantification. We validate the framework on a diverse set of open-access dMRI datasets, demonstrating that SIINR outperforms standard interpolation methods in both quantitative error metrics and qualitative anatomical fidelity. Experiments on clinical cases, including subjects with multiple sclerosis and brain lesions, illustrate the framework its ability to propagate intensity changes and flag uncertain regions in challenging scenarios. SIINR is flexible, modular, and can be adapted to different upsampling ratios and downstream tasks, providing a principled approach for enhancing clinical dMRI and supporting robust interpretation of derived neuroimaging metrics.

---


### 115. [SenWorld: A Digital-Twin Simulation for Generating Context-Rich Evaluation Data](https://arxiv.org/abs/2607.19949)

**<font color=#1a73e8>作者：</font>** Zenghui Zhou, Xiaoyang Li, Xiaoxuan Qiao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Smartphone personal assistants reason over longitudinal personal data, yet evaluating them requires context-rich evaluation data whose correct answers are known, and real device traces are too privacy-sensitive to share. To address this challenge, we present SenWorld, a physically grounded, deterministic, event-sourced digital-twin simulation that generates such data with ground truth fixed by construction. In SenWorld, personas live through a full day in a world built from real map, weather, holiday, and network data; every observable signal is archived in full-system snapshots; and each evaluation case is labeled by a pointer to an existing record rather than by post-hoc annotation or a large language model (LLM) judge. We evaluate this method with 16 personas in Beijing. The generated data closely matches the held-out real-user benchmark in category distribution (Jensen--Shannon divergence (JSD) 0.070) and in the daily rhythm of communication records (JSD below 0.1), though generated records remain shorter than real ones. Without scripted interaction, personas form a fully reciprocated dialogue subgraph and differentiated behavioral repertoires. Projected into 717 evaluation cases, the generated data exposes 78 failures in a production smartphone assistant, concentrating on call and Short Message Service (SMS) records while contacts, schedules, and alarms never fail. The snapshot pointer confirms each failure as an assistant-side retrieval error, with no LLM judge involved. Overall, SenWorld offers a privacy-safe, reproducible, and distribution-checked path to evaluation data whose labels are fixed by construction.

---


### 116. [OffNadirLoc: Benchmark and Framework for Challenging UAV-to-Satellite Geo-Localization under Large Off-Nadir Views](https://arxiv.org/abs/2607.19951)

**<font color=#1a73e8>作者：</font>** Qian Qiao, Wenye Liu, Ting Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-view geo-localization between UAV and satellite imagery remains a fundamental yet highly challenging task, especially under large off-nadir views where drastic perspective distortions, occlusions, and appearance gaps occur. Existing benchmarks and methods primarily focus on near-nadir scenarios and often overlook the importance of structural scene understanding and intra-domain relational constraints, limiting their performance in real-world deployments. In this work, we introduce OffNadirLoc, a new benchmark for large off-nadir UAV-to-satellite geo-localization. To tackle the unique challenges posed by off-nadir perspectives, we further propose ONLoc, a framework that incorporates a structure-aware contextual weighting mechanism to dynamically emphasize reliable local features while suppressing ambiguous or repetitive regions. Additionally, we design a view-coherent learning strategy, which treats one satellite image and the corresponding UAV images from multiple views as a cohesive semantic group. This set-level supervision enables the model to learn viewpoint-invariant and discriminative features, making it more effective at capturing multi-view consistency than conventional pairwise contrastive learning. Extensive experiments on the OffNadirLoc benchmark and four near-nadir datasets demonstrate that our method consistently outperforms state-of-the-art approaches while exhibiting strong zero-shot generalization to unseen datasets without additional training. The code will be released at this https URL.

---


### 117. [A Multi-Dimensional Evaluation of Explainability in Media Bias Detection](https://arxiv.org/abs/2607.19954)

**<font color=#1a73e8>作者：</font>** Ting Chen, Raina Zhang, Benjamin M. Ampel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Detecting media bias automatically is difficult because biased framing is often subtle, yet in domains such as news analysis, accurate predictions alone are insufficient without explanations that reflect the model's underlying reasoning. We present a multi-dimensional evaluation of explainability in encoder-based media bias detection using the Bias Annotations By Experts (BABE) dataset. Specifically, we study BERT and RoBERTa as classifiers (base and large variants) along three complementary axes: predictive performance, explanation plausibility (token-level alignment with expert rationales), and mechanistic faithfulness (whether compact sets of attention heads recover predictive signal under counterfactual rationale masking). To induce variation in plausibility, we additionally investigate attention-supervised finetuning, which incorporates expert rationale annotations as an auxiliary training signal. Attention supervision serves as an intervention on attribution plausibility, while the effectiveness of attribution methods varies substantially across architectures. Circuit analysis further reveals substantial variation in mechanistic recoverability across architectures, suggesting that model scale alone does not determine circuit compressibility. Taken together, our findings suggest that predictive performance, attribution plausibility, and mechanistic faithfulness characterize different aspects of model behavior and should be evaluated separately when studying explainability in media bias detection.

---


### 118. [When Does Knowledge Distillation Hurt? Reliability-Aware Distillation for Low-Resource Language Summarization](https://arxiv.org/abs/2607.19956)

**<font color=#1a73e8>作者：</font>** Dipto Sumit, Ankan Kumar Roy Srizon, Sadia Khair Rodela 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation (KD) is a standard approach for compressing sequence-to-sequence models, but its per-sample effects are rarely examined. On the BanSum Bangla summarization benchmark, we find that standard KD improves ROUGE-L by only +0.0003 over a cross-entropy baseline, and that approximately 51.3% of training samples are estimated to actively harm student validation loss under standard KD. We propose two complementary reliability-aware distillation methods. CHAD (Counterfactual Harm-Aware Distillation) measures per-sample KD usefulness via gradient alignment with the validation loss direction and trains a lightweight gate that generalizes this counterfactual judgment to the full training set. EWAD+CPDP combines token-level entropy-weighted adaptive distillation with a capacity-proportional geometric constraint from a second, vocabulary-incompatible teacher. On BanSum, both methods substantially outperform standard KD: CHAD by +0.0173 ROUGE-L and EWAD+CPDP by +0.0219 ROUGE-L, where standard KD itself improves ROUGE-L by only +0.0003; despite using only 60M parameters, both outperform a fine-tuned Qwen 2.5-3B model (50x larger). We further evaluate the stronger method, EWAD+CPDP, across 15 typologically diverse XL-Sum languages organised into three sets, beating the CE-only baseline on 10/15 languages; gains are most reliable where the two teachers contribute complementary signal, and weakest where they have saturated or jointly weak target-language coverage. We release code and trained models to support reproducibility and further research on selective distillation.

---


### 119. [The Giant Hippocampus: From Structural Monoculture to a System of Systems](https://arxiv.org/abs/2607.19973)

**<font color=#1a73e8>作者：</font>** Jaeho Seol  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI researchers describe state-of-the-art models as one thing repeated at scale: the Transformer, wired identically for text, pixels, or speech. Neuroscientists describe the cortex as a mosaic - dense Layer 4 in visual cortex for spatial encoding, thick Layers 5/6 in motion cortex for temporal integration - different jobs solved by different structures. This paper argues the gap is a structural error, not a stylistic one, and is measurable. A century of cytoarchitecture, from Brodmann to single-cell Patch-seq, shows distinct cognitive functions are implemented by qualitatively different structures, not by rescaling one template. The convolutional neural network is the field's own proof: local receptive fields and hierarchical depth encoded this prior directly, reaching strong image recognition on far less data than later architectures needed. The paper traces how this lesson was discarded: the "Hardware Lottery" made the Transformer the path of least resistance, not the principled choice, and Mixture-of-Experts, often cited as diversity, in fact partitions parameters among identical experts. A functionalist analysis shows the Transformer is best understood as a functional analog of the hippocampal formation, not a general-purpose cortex - the same mistake as treating cortex as one giant Broca's area, except the field has now standardized on a giant hippocampus, applied to tasks it was never built for: audition, executive gating, working memory. The paper closes with an alternative: a Heterogeneous Topological Network, a System of Systems in which distinct modules keep the inductive bias their computation demands and communicate through standardized interfaces. This is a design discipline for AI architects, not cognitive science: specify modularity before training, using structural evidence as a design input rather than reverse-engineering architecture from a trained model's behavior.

---


### 120. [Time Series Network Utilization KPI Forecasting Using Advanced AI/ML Models](https://arxiv.org/abs/2607.19974)

**<font color=#1a73e8>作者：</font>** Niraj Gadhe, Kirti Bhardwaj, Moulik Jain 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid proliferation of data-intensive applications, cloud infrastructure, and IoT ecosystems has made proactive resource provisioning critical for maintaining optimal network performance. However, network administrators face a constant battle against capacity constraints, where traditional reactive approaches fail to accurately anticipate traffic fluctuations. This inability to foresee demand leads to costly over-provisioning, unexpected downtime, and degraded quality of service directly impacting operational budgets and business continuity. To achieve efficient capacity planning, accurate forecasting of bandwidth utilization is essential. This study addresses the challenge by evaluating a diverse spectrum of models including seasonal decomposition, Prophet, Random Forest, XGBoost, Support Vector Regression, and advanced deep learning architectures like bidirectional and Convolutional LSTMs - using a common interface dataset benchmarked across MAPE, NRMSE, and R-square metrics. Ultimately, this research delivers actionable insights into the trade-offs between model accuracy and computational efficiency, empowering engineers, operators, and business owners to select the optimal forecasting model for their specific infrastructure needs.

---


### 121. [Coordinating from Memory: Graph-Structured Experience Reuse for Multi-Agent Adaptation in Dynamic Manufacturing](https://arxiv.org/abs/2607.19985)

**<font color=#1a73e8>作者：</font>** Chengxiao Dai, Zhanhui Lin, Zhaokun Yan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Dynamic manufacturing environments require multi-agent systems to coordinate effectively under frequent operational disturbances such as machine failures, urgent job arrivals, and processing time variations. Existing multi-agent reinforcement learning approaches treat each disturbance episode independently, discarding valuable coordination experience that could accelerate future adaptation. In this paper, we propose a Graph-Structured Experiential Memory (GSEM) framework for multi-agent coordination in dynamic manufacturing. The framework encodes historical coordination episodes as heterogeneous relational graphs that capture task dependencies, machine states, and inter-agent collaboration patterns. When a new disturbance occurs, a graph neural network-based retrieval mechanism identifies structurally similar past episodes, enabling experience-guided policy adaptation rather than learning from scratch. Experiments on dynamic flexible job-shop scheduling benchmarks with three disturbance types show that GSEM reduces makespan by 4.1%-10.0% and adaptation time by 33%-38% compared to the strongest memory-augmented baseline, with the advantage increasing under higher disturbance frequency. Ablation studies and cross-disturbance transfer experiments further validate the necessity of graph-structured encoding and similarity-based retrieval and demonstrate the cross-disturbance generalizability of learned coordination patterns.

---


### 122. [STEREOFLOW: Progressive Stereo Matching with StereoDiT and Transition Flow Matching](https://arxiv.org/abs/2607.19986)

**<font color=#1a73e8>作者：</font>** Hao Wang, Haoran Geng, Xiaotong Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Stereo matching is a fundamental task in 3D reconstruction. Despite remarkable advances, the prevailing paradigms formulate stereo matching as a deterministic regression problem, collapsing the multimodal distribution modeling into a single-point estimation. This formulation suffers from a regression-to-mean bias, frequently struggling with ambiguous regions. In contrast, we introduce a prior-guided generative framework that integrates deterministic matching regression and generative distribution modeling within a complementary formulation. Built upon this formulation, we introduce StereoFlow through three key components: (i) a two-stage progressive cascade matching network that progressively produces multi-resolution stereo conditions with complementary matching cues; (ii) a pixel diffusion transformer (termed StereoDiT) with a frequency-decoupled architecture for modeling correspondence ambiguity; (iii) a few-step flow matching objective (termed Transition Flow Matching) for efficient optimization. In summary, \textsc{\textbf{StereoFlow}} achieves strong geometric consistency and rich fine-grained details in ill-posed, discontinuous regions and under zero-shot generalization. Extensive experiments demonstrate that the proposed StereoFlow establishes multiple state-of-the-art results across benchmarks, including Scene Flow, KITTI, ETH3D, and Middlebury.

---


### 123. [Toward Seasonal Guidelines for Robust Deep-Learning Sentinel-2 Building Detection in Different Area Types](https://arxiv.org/abs/2607.19994)

**<font color=#1a73e8>作者：</font>** Michał Romaszewski, Kamil Drejer, Katarzyna Kołodziej 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sentinel-2 imagery offers open access, global coverage, and frequent revisit times, making it attractive for practical building mapping at scale; however, its native 10m resolution makes building vs non-building classification challenging, particularly for small or sub-pixel buildings, and performance can vary with both seasonality and the heterogeneity of built-up environments. This paper introduces a Sentinel-2 building-detection framework designed to systematically quantify these effects and to support more formalised, practice-oriented model selection. We construct a dedicated multi-temporal Sentinel-2 dataset over the Warsaw region and derive binary ground-truth masks by rasterising official Polish topographic database (BDOT10k) building footprints onto the Sentinel-2 pixel grid. Using two established convolutional segmentation backbones (U-Net and DeepLabV3+), we first perform scene-specific fine-tuning to select a robust architecture and identify the best monthly models for L1C and L2A products separately. We then conduct cross-temporal inference by applying each best monthly model to all scenes, enabling an assessment of (i) which months provide favourable training and inference conditions, (ii) how performance transfers between seasons, (iii) the impact of processing level, and (iv) how these effects differ across built-up typologies. Based on these results, we provide practical guidance for routine Sentinel-2 building classification under varying acquisition periods and settlement characteristics.

---


### 124. [CLARK: Closed-loop Learning for Adaptive Reasoning over Knowledge Graphs](https://arxiv.org/abs/2607.19996)

**<font color=#1a73e8>作者：</font>** Yousef Khan, Luca Gherardini, Marco Maratea 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Machine Learning models are widely used for automating classification tasks by extracting statistical patterns from data. However, their performance deteriorates if the data distribution changes, making them ill-suited to handle uncertain and evolving information. Moreover, they provide limited support for integrating prior knowledge. To address these limitations, we present CLARK (Closed-loop Learning for Adaptive Reasoning over Knowledge Graphs), a framework that integrates knowledge graphs, symbolic rule mining, and probabilistic reasoning under the Logic Programs with Markov Logic Networks (LP$^{\text{MLN}}$) formalism. Starting from CACTUS-derived KGs, CLARK translates graph structure into an LP$^{\text{MLN}}$ program and iteratively enriches it with candidate rules proposed by symbolic learners. These rules are calibrated through probabilistic weight learning, enabling reasoning under uncertainty and refinement of the underlying graph structure. We evaluate CLARK on two medical datasets, analysing both rule quality and downstream classification performance. Results demonstrate that CLARK leads to improved classification performance and more generalisable inference. Overall, CLARK provides a principled approach to constructing adaptive, interpretable, knowledge-driven models for classification.

---


### 125. [Good Practice Guide for quantifying uncertainties for machine learning models applied to photoplethysmography signals](https://arxiv.org/abs/2607.19999)

**<font color=#1a73e8>作者：</font>** P. Harris, C. Bench, M. Rinkevičius 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This Good Practice Guide presents work done in the QUMPHY project (Uncertainty quantification for machine learning models applied to photoplethysmography signals) that considered both machine learning and uncertainty quantification for problems which used photoplethysmography (PPG) signals from wearable devices as input. It provides high-level guidance on what types of machine learning model might be used and how different models compare when applied to both regression and classification tasks. It provides guidance on the implementation of different methods for uncertainty quantification, covering both model-dependent and model-independent techniques, and on the validation of the results provided by those methods. It also describes six benchmark problems together with pointers to different benchmark datasets for each problem. Software is described that can assist practitioners in implementing the methods described herein and there is a brief consideration of ethical issues. It concludes with a summary and recommendations.

---


### 126. [Taming the Security-Energy Paradox: A Green AI Approach to Optimized Android Malware Detection](https://arxiv.org/abs/2607.20003)

**<font color=#1a73e8>作者：</font>** Shrinidhi Sridhar, Vikas K. Malviya  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> An increase in advanced Android malware requires the use of deep learning models, which can run on Android devices. But there is a trade-off between security and energy use, as strong detection models can drain the battery of devices fast. This work tests different Multi-Layer Perceptron (MLP) model configurations to balance malware detection performance and energy efficiency. In this work, we compared standard FP32 models with optimized INT8 quantized neural networks with different model depths using TUANDROMD and DREBIN datasets for both classification performance and energy consumption. The results show that INT8 quantization reduces model size by about 3.5 times with a decrease in energy consumption to 0.0189 mJ per inference, while maintaining more than 99.2\% detection accuracy. We found that shallow quantized architectures, such as 3-layer and 4-layer QNNs, reduce energy costs by improving throughput and shortening the time of CPU operating in a high-power state. This work shows that efficient malware protection can be achieved on resource-constrained smartphones and provides a foundation for Green AI in mobile security.

---


### 127. [Safe Remediation as Risk-Constrained Intervention Decision in Microservice Systems](https://arxiv.org/abs/2607.20005)

**<font color=#1a73e8>作者：</font>** Chengxiao Dai, Zhaokun Yan, Chenjun Lei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In modern IT operations (IT-Ops), the cost of an incorrect repair often exceeds the cost of no action at all. Yet existing automated remediation systems are designed to generate actions rather than to decide whether intervention is warranted, leaving safety as an afterthought enforced by manual approval. This paper makes three contributions to close this gap: (i) we reformulate safe remediation as a risk-constrained intervention decision problem and cast it as a Constrained Markov Decision Process (CMDP), in which the agent maximizes repair success subject to a bounded false remediation rate (FRR); (ii) we introduce a three-dimensional risk decomposition comprising blast radius, reversibility, and epistemic uncertainty, providing operators with an interpretable per-action safety interface; and (iii) we design a context-adaptive human-in-the-loop (HITL) gate that turns escalation from a binary failsafe into a bandwidth-aware control layer responsive to on-call load and business criticality. The full policy is learned offline from historical incident logs, enabling explicit control of the expected FRR. Experiments on the Train Ticket microservice benchmark with Chaos Mesh fault injection and an RCAEval-aligned fault taxonomy show that our framework reduces FRR by 39% while improving repair success by 2.5 points over a strong runbook baseline, and reduces on-call escalation load by 17% relative to a fixed-threshold variant.

---


### 128. [TalentCLEF at CLEF2026: Skill and Job Title Intelligence for Human Capital Management](https://arxiv.org/abs/2607.20009)

**<font color=#1a73e8>作者：</font>** Luis Gasco, Hermenegildo Fabregat, Laura García-Sardiña 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents the second edition of the TalentCLEF Challenge, which will run as an evaluation lab as part of CLEF 2026. The aim of TalentCLEF is to promote the development of systems and methods that use Natural Language Processing (NLP) in the field of Human Capital Management (HCM), fostering approaches that ensure fairness in results, operate across multiple languages, and adapt to diverse industries. To this end, TalentCLEF establishes public benchmarks where research teams can compare methods and share findings, moving the field toward more practical and impactful NLP solutions that effectively address the real needs of workforce management.
This year's lab will feature two tasks designed to foster the development and evaluation of systems that support key HCM activities such as talent matching, upskilling, reskilling, and skill gap detection: (i) Task A - Contextualized Job-Person Matching, focused on retrieving and ranking suitable candidates for specific job positions using context-rich and privacy-preserving data; and (ii) Task B - Job-Skill Matching with Skill Type Classification, centered on identifying relevant skills for a given job title and classifying them by their type within the job profile.
TalentCLEF website: this https URL

---


### 129. [Generalized Kalman filter based temporal difference reinforcement learning](https://arxiv.org/abs/2607.20010)

**<font color=#1a73e8>作者：</font>** Vasos Arnaoutis, Eric Lutters, Bojana Rosić  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we present a generalized temporal-difference (TD) reinforcement learning framework based on the theory of conditional expectations. The value and action-value (Q-value) functions are treated as uncertain quantities, and their estimation is formulated as a stochastic inference problem. Unlike classical Kalman-based temporal-difference learning, which relies on linear-Gaussian assumptions, the proposed formulation is derived directly from the conditional expectation framework and naturally extends to nonlinear models and non-Gaussian probability distributions. The proposed method recursively estimates not only the conditional expectation of the value function but also its second probabilistic moment, thereby quantifying the uncertainty associated with the learned value function throughout the learning process. To obtain a computationally tractable algorithm, the stochastic problem is discretized using either polynomial chaos expansions or ensemble-based approximations, providing efficient representations of the underlying random variables. The proposed framework is demonstrated on two optimal control problems: a linear mass--spring--damper system and a nonlinear heat conduction problem in a closed cavity. The numerical examples illustrate the capability of the proposed method to accurately estimate both the value function and its associated uncertainty, while extending classical Kalman-based temporal-difference learning to a broader class of stochastic systems.

---


### 130. [Global Difference Constraint Propagation for Constraint Programming](https://arxiv.org/abs/2607.20022)

**<font color=#1a73e8>作者：</font>** Lucas Kletzander, Jip J. Dekker, Andreas Schutt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Difference constraints of the form $x - y \leq d$ are well studied, with efficient algorithms for satisfaction and implication, because of their connection to shortest paths. Finite domain propagation algorithms, however, typically do not make use of these algorithms, and treat each difference constraint as a separate propagator. Propagation does guarantee completeness of solving, but can be needlessly slow. In this paper we describe how to build a (bounds consistent) global propagator for difference constraints that treats them all simultaneously. SAT modulo theory solvers have included theory solvers for difference constraints for some time. While a theory solver for difference constraints gives the basis of a global difference constraint propagator, we show how the requirements on the propagator are quite different. Crucially, we show how to explain propagations by a global difference constraint propagator, in order to use it within a lazy clause generation solver. We give experiments showing that treating difference constraints globally can substantially improve on the standard propagation approach.

---


### 131. [A Systematic Benchmark of Intensity Normalisation Methods for 3D Knee MRI Segmentation and Cross-Domain Generalisability](https://arxiv.org/abs/2607.20028)

**<font color=#1a73e8>作者：</font>** Oliver Mills, Philip Conaghan, Samuel Relton  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robust out-of-the-box performance is essential for the clinical deployment of deep learning models in medical imaging. An important but underexplored factor affecting model generalisability is intensity normalisation, particularly for magnetic resonance imaging (MRI), where image intensities vary across scanners and protocols. In this study, we systematically compared seven normalisation methods and their impact on the performance of a 3D U-Net model for meniscus segmentation from knee MRI. The methods included standard scaling approaches, histogram-based techniques, and a Gaussian Mixture Model (GMM)-based method. Models were trained on the IWOAI 2019 dataset and evaluated on both internal and external test sets (SKM-TEA) to assess generalisability. Performance was similar internally but differences were significant on external data, with Z-score, Nyúl histogram matching, and CLAHE showing greater robustness than other methods. However, these differences were small compared to the significant performance drop observed between datasets. Overall, while intensity normalisation had a measurable effect on model generalisability, its impact was limited relative to the effects of domain shift, highlighting the need for complementary strategies for robust deployment.

---


### 132. [Visual Indicators to Increase the Detection of Linguistic Media Bias](https://arxiv.org/abs/2607.20031)

**<font color=#1a73e8>作者：</font>** Smi Hinterreiter, Anna Chelsea Bahß, Ann-Christin Gah 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The influence of linguistic bias in online news articles is a growing concern, particularly in the context of shaping public opinion and rising political polarization. While there is a growing body of literature on indicators for misinformation, none have been sufficiently tested to counteract the influence of media bias. Hence, we design six indicators (Bias Bar, Bias Gauge, Bias Highlights, Political Scale, Sentiment Scale, and Trust Score) and test their impact on linguistic bias detection and perception in a two-phased experiment (n = 214). First, we expose participants to short, social-media-like statements along with one indicator and query bias perception. Second, we evaluate bias detection by removing the indicator and asking participants to mark biased words. In addition, we examine how trust, sharing discernment, and sentiment relate to bias perception and detection. Our results show that highlighting biased phrases and showing total bias with contextual information in a gauge significantly improve bias detection skills. However, the strongest predictor for reduced bias detection was political congruency between the statement and the participant. We conclude with design recommendations for linguistic media bias indicators in online news environments.

---


### 133. [Test Case Prioritization for DNNs via Neural Collapse Instability](https://arxiv.org/abs/2607.20046)

**<font color=#1a73e8>作者：</font>** Chunyu Liu, Mingyuan Li, Yang Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> With the widespread deployment of deep neural networks (DNNs) in safety-critical domains, reducing the cost of model validation under limited testing budgets has become increasingly important. Existing test case prioritization techniques often rely on single-checkpoint confidence signals derived from output probabilities. However, DNNs can be confidently wrong, and the confidence margin between the predicted and competing classes is frequently small, which weakens early fault discovery. To address this limitation, we propose a Neural-Collapse-Inspired Prioritization (NCIP) framework that replaces absolute confidence with cross-checkpoint prediction variability in the terminal training regime, where model geometry becomes highly structured. NCIP introduces two key components. First, it selects an NC-guided representative subset of training checkpoints using an equiangularity score of classifier weights, quantified as the standard deviation of pairwise cosine similarities among class weight vectors. Second, it prioritizes test inputs by their prediction variability across the selected checkpoints, surfacing boundary-adjacent and failure-prone samples that are unstable under checkpoint-induced decision boundary shifts. Extensive experiments across multiple datasets and architectures show that NCIP achieves strong performance in early fault discovery compared with competitive baselines, with 1.5 to 16.6 percent RAUC-ALL gains and 4.9 to 20.6 percent RAUC-500 gains under the same testing budget. NCIP further attains the best average performance across all dataset-model pairs.

---


### 134. [Experiential Versus Instructional Approaches for Eliciting Metacognitive Awareness in AI-Assisted Learning: A Short-Term Longitudinal Study](https://arxiv.org/abs/2607.20047)

**<font color=#1a73e8>作者：</font>** Pau Benazet i Montobbio, Janne Rotter, Davinia Hernández-Leo  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> With generative AI (GenAI) entering classrooms the question to which teaching approach best supports metacognitive skill acquisition in AI-assisted learning becomes pressing. In this short-term longitudinal study we investigate two contrasting approaches: experiential learning encompassing hands-on approaches and instructional learning such as classical lectures. We conducted a quasi-experiment with 126 university students from a first-year engineering course which were distributed across the two conditions and completed a two hour session on learning with GenAI in the corresponding learning style. Metacognitive awareness which encompasses both knowledge of cognition (understanding effective AI-use strategies) and regulation of cognition (applying that knowledge in practice) was measured before and after the session. Additionally, students longitudinal metacognitive awareness was tracked over the trimester and assessed again five weeks after the initial intervention. Results reveal that experiential methods outperform instructional approaches in engagement and knowledge of cognition immediately after the intervention. By five weeks, the two groups converged on these measures, while the experiential group showed a delayed, continuous within-group increase in regulation of cognition that was not observed in the instructional group. This suggests that the benefits of experiential approaches extend beyond conventional educational settings to AI-assisted learning, and that knowledge and regulation may develop on different timescales under experiential learning.

---


### 135. [Importance-Aware OBS Pruning for Diffusion Models](https://arxiv.org/abs/2607.20048)

**<font color=#1a73e8>作者：</font>** Ba-Thinh Lam, Srijan Das, Hieu Le  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose importance-aware pruning for diffusion models, a training-free framework that prioritizes preserving parameters critical to semantically salient image regions. To do so, we incorporate spatial importance maps -- derived from conditioning signals or model attention -- into the pruning objective. This produces parameter rankings aligned with perceptual relevance rather than uniform reconstruction error. On MS-COCO dataset, our proposed approach consistently retains subject fidelity and structural correctness at high compression ratios where conventional pruning causes visible degradation. These results demonstrate that content-aware objectives are key to perceptually faithful compression of generative models.

---


### 136. [TRUST-ESD: A Risk-Calibrated and Governance-Aware AI Framework for Enterprise Strategic Decision Support Under Uncertainty](https://arxiv.org/abs/2607.20065)

**<font color=#1a73e8>作者：</font>** Tian Qiu, Li Yan, Mahabubur Rahman Miraj 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise strategic decision support requires AI systems that are not only accurate, but also uncertainty-aware, risk-calibrated, explainable, and governance-compliant. This paper proposes TRUST-ESD, a risk-calibrated and governance-aware framework for enterprise decision support under uncertainty. TRUST-ESD evaluates feasible counterfactual strategies through predictive utility estimation, conformal uncertainty calibration, CVaR-based downside-risk scoring, risk-memory retrieval, policy-as-code governance, explainability, and human oversight. Unlike prediction-only methods that select actions by maximum expected utility, TRUST-ESD recommends strategies that balance value, reliability, risk exposure, and compliance. Experimental results show that TRUST-ESD improves risk-adjusted utility by 7.95%, reduces risk exposure by 23.22%, reduces CVaR by 23.78%, lowers calibration error by 13.89%, improves explanation fidelity by 10.90%, and increases governance compliance by 9.76% compared with strong uncertainty-aware baselines, while maintaining competitive predictive accuracy. Ablation and case-study analyses further confirm that uncertainty calibration, downside-risk scoring, risk memory, explainability, and governance validation jointly improve trustworthy enterprise decision-making.

---


### 137. [GaussianSeed: Hierarchical Gaussian Seeding for High-Resolution 3D Occupancy Prediction](https://arxiv.org/abs/2607.20071)

**<font color=#1a73e8>作者：</font>** Xinzhuo Li, Xianghui Pan, Jiayuan Du 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-centric 3D occupancy prediction provides dense scene representations essential for autonomous driving and robotic navigation, yet existing methods struggle to scale to high voxel resolutions due to prohibitive computational costs. To address this, we introduce GaussianSeed, a progressive multi-scale Gaussian occupancy prediction framework that organizes primitives into a coarse-to-fine hierarchy. Benefiting from this hierarchical design, GaussianSeed effectively circumvents the memory bottlenecks inherent in dense representations, successfully scaling to a $0.1\text{m}$ spatial resolution while maintaining real-time inference capabilities. To comprehensively evaluate high-resolution geometric perception, we further construct TJScenes, a panoramic six-camera occupancy dataset with highly detailed $0.1\text{m}$ annotations. Extensive experiments on Occ3D-nuScenes and TJScenes demonstrate that GaussianSeed delivers the lowest latency among all evaluated methods while maintaining highly competitive accuracy, advancing the efficiency-quality frontier of high-resolution 3D occupancy prediction.

---


### 138. [Factor-Informed Uncertainty Distillation for Gaze Estimation](https://arxiv.org/abs/2607.20072)

**<font color=#1a73e8>作者：</font>** Mohammadreza Jamalifard, Yaxiong Lei, Javier Fumanal Idocin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep gaze estimation works well in controlled capture but degrades in unconstrained settings, where systems must reject unreliable predictions. Single-pass uncertainty (e.g., heteroscedastic regression) infers uncertainty from pixels without explicit input-validity cues, while sampling based methods are often too costly for real time use. We propose Factor-Informed Uncertainty Distillation (FIUD), a teacher-student framework that aligns uncertainty with interpretable image-quality failure modes. A gradient-boosting teacher predicts expected gaze error from factors such as illumination, sharpness, eye visibility and symmetry; a neural student distills these signals via curriculum learning and ranking supervision into a lightweight single-pass uncertainty head. Across ETH-XGaze, Gaze360, and MPIIFaceGaze (>300k samples), FIUD improves uncertainty, error rank correlation and selective prediction versus deterministic and sampling-based baselines, with the largest gains in unconstrained settings.

---


### 139. [Evaluating and Mitigating Gender Bias in Pre-trained Embeddings for ML-based Recruitment](https://arxiv.org/abs/2607.20073)

**<font color=#1a73e8>作者：</font>** Farnaz Faramarzi Lighvan, Lynn Houthuys  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI-based recruitment systems that rely on machine learning models trained on historical CV data, risk perpetuating and amplifying social biases. A key challenge arises in unstructured CV text, where pre-trained language model embeddings may infer sensitive attributes such as gender even after explicit indicators are removed. In this paper, we evaluate nine pre-trained embedding models on the synthetic FairCVdb dataset, analyzing the informativeness of their embeddings for applicant scoring and their susceptibility to gender leakage, on both original and gender-scrubbed biographies. We further use a multi-task adversarial learning framework with gradient reversal to predict applicant suitability while suppressing gender information from learned representations. Finally, we use a multi-objective Pareto-front-based model selection to balance predictive utility and fairness. Our experimental results show that explicit gender scrubbing substantially reduces but does not eliminate gender leakage, while adversarial learning improves fairness mainly on original biographies and acts as a complementary strategy rather than a substitute for text-level debiasing.

---


### 140. [RALS: Resources and Baselines for Romanian Automatic Lexical Simplification](https://arxiv.org/abs/2607.20078)

**<font color=#1a73e8>作者：</font>** Fabian Anghel, Petru Theodor Cristea, Claudiu Creanga 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce the first dataset that jointly covers both lexical complexity prediction (LCP) annotations and lexical simplification (LS) for Romanian, along with a comparison of lexical simplification approaches. We propose a methodology for ordering simplification suggestions using a pairwise ranking approximation method, arranging candidates from simple to complex based on a separate set of human judgments. In addition, we provide human lexical complexity annotations for 3,921 word samples in context. Finally, we explore several novel pipelines for complexity prediction and simplification and present the first text simplification system for Romanian.

---


### 141. [The Two-Process Theory of Machine Self-Report](https://arxiv.org/abs/2607.20082)

**<font color=#1a73e8>作者：</font>** Hubert Plisiecki, Filip Chmielewski, Kacper Dudzic 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models are increasingly asked to self-report, informing safety evaluations, public understanding, and model-welfare debates. Yet their reports are elicited with human questionnaires never validated for models or ad hoc prompts of unknown reliability. We propose the first language-model-specific psychometric theory: a two-process theory of machine self-report. Self-description jointly reflects persona installation, through which post-training writes in a permitted inner life of warmth, absorption, and meaning (dimension B), and attribution gating, through which it suppresses first-person claims to "unsafe" experiences the model can readily ascribe to others (dimension A). Their emic structure comes from model responses to human items, not human psychology. Together they split prior work's dominant Pinocchio Axis. The split emerged in an exploratory reanalysis of the original data, informed the instrument's design, and was confirmed with new items, wordings, and models. It is itself a training effect: A and B are entangled in base checkpoints but separated by post-training. We operationalize the theory in a 48-item Pinocchio Inventory with human-instrument reliability and reproducible structure ($\alpha=.82$ to $.94$; cross-form convergence $r=.84$; recovery of the full-pool axes $r=.92$ to $.96$; eight-month stability $r=.93$), then test it on 206 open-weight models, including 67 same-checkpoint base/post-trained pairs. Post-training's clearest fingerprint is installation: B rises .20 in 62/67 pairs across all organizations. Gating is more selective: model scale is unrelated to A in base checkpoints ($r=+.11$) but predicts it after post-training ($r=-.42$). Thus, the dimensions are not fixed properties of language models: they reflect the structure imposed on self-report by a training regime and may differ under others.

---


### 142. [A Task Taxonomy for Edge and Trail Bundling](https://arxiv.org/abs/2607.20089)

**<font color=#1a73e8>作者：</font>** Markus Wallinger, Stephen G. Kobourov  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Edge bundling reduces visual clutter by aggregating similar edges, yet practitioners lack a structured vocabulary for reasoning about the tasks that bundled visualizations support. Such a vocabulary is needed both to evaluate the general utility of bundling and to compare different bundling approaches. We address this gap by assembling a corpus of 102 papers, 49 of which contain explicit bundling tasks, spanning node-link diagrams, geographic trail sets, and parallel coordinate plots. From this corpus, we derive a task taxonomy organized as a matrix of scope (Element, Bundle, Global, Multi-view) crossed with action (Verify, Identify, Characterize, Quantify, Compare, Assess), instantiated across the three representation types. We show that bundling simultaneously enables tasks (bundle-level and global reasoning) and disables others (element-level precision), a duality not captured by existing task frameworks. Our coded corpus and taxonomy are released as supplemental material on OSF (this http URL).

---


### 143. [Two-Step Occupation Coding](https://arxiv.org/abs/2607.20101)

**<font color=#1a73e8>作者：</font>** Alexander M. Esser, Jens Dörpinghaus  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Occupation coding links job titles in free text to occupational taxonomies and is a core task in labor market research. Existing approaches typically address this problem in a single end-to-end step, jointly identifying job titles and assigning occupational codes. This paper presents a novel two-step approach that separates these tasks. In the first step, a domain-specific Named Entity Recognition (NER) model identifies occupational titles in continuous text, even under noise such as OCR errors. In the second step, the extracted job titles are mapped to a taxonomy, enabling the classifier to focus exclusively on this mapping. We demonstrate that this separation improves accuracy, robustness, and interpretability compared to single-step approaches. The method has been developed for German documents but is transferable to other languages. We further introduce a margin-based confidence criterion for occupation coding, replacing common absolute thresholds. To support reproducibility, we publish the source code and evaluation scripts.

---


### 144. [RIM: A Retrieval-In-Matching Framework for Cross-Domain Global Visual Localization of UAVs](https://arxiv.org/abs/2607.20116)

**<font color=#1a73e8>作者：</font>** Xin Li, Siyuan Duan, Shang Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Global visual localization of unmanned aerial vehicles (UAVs) using remote-sensing reference maps has attracted increasing attention. However, acquisition-time and imaging-platform differences between UAV and reference imagery induce substantial cross-domain appearance and viewpoint shifts, challenging robust six-degree-of-freedom (6-DoF) pose estimation. We address these shifts by sampling UAV-viewpoint reference views from Google 3D Tiles across locations, altitudes, and orientations. A two-stage cross-domain fine-tuning recipe adapts SALAD using pose-near positives and geographically distant hard negatives, while local geometric consistency re-ranks the Top-K candidates. We further propose Retrieval-In-Matching (RIM), which freezes the adapted DINOv2-B retriever and distils a local-descriptor decoder that reuses its token field alongside a shallow VGG19 detail stream. One query-side DINOv2-B forward thus serves both SALAD retrieval and local description, eliminating a second foundation-model backbone while preserving retrieval descriptors by construction. We evaluate RIM zero-shot on the reconstructed EPFL Urbanscape and self-collected Chang'an Park datasets, both geographically disjoint from the training data. RIM outperforms ten recent retrieval baseline families. At 25/50 m under the full 3D distance metric, it improves Recall@1 over SALAD by 8.55/13.77 percentage points on EPFL and 4.45/8.94 points on Park. At Top-K=5, the complete measured localization query, including retrieval, candidate matching, and robust geometric verification, takes 67.9 ms end-to-end: 1.8 times faster than the strongest separate sparse-matching baseline and over 40 times faster than RoMa, while achieving comparable re-ranking accuracy. These results establish an efficient and deployable pipeline for UAV global visual localization in GNSS-challenged environments.

---


### 145. [OpenSkillRisk: Benchmarking Agent Safety When Using Real-World Risky Third-Party Skills](https://arxiv.org/abs/2607.20121)

**<font color=#1a73e8>作者：</font>** Qiyuan Liu, Tingfeng Hui, Kun Zhan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based agents leverage third-party skills to extend their capabilities in open-world scenarios. However, third-party skills can introduce extra security vulnerabilities, as seemingly harmless skills can contain latent safety risks that only emerge during actual execution. In this work, we conduct a systematic investigation into how well current agent systems recognize and avoid such risks. To support quantitative and qualitative evaluation, we construct OpenSkillRisk, a dedicated safety benchmark containing 263 risky skills collected from public skill marketplaces. We classify these skills into seven categories based on their threat types and pair each skill with a standardized user task and a corresponding sandbox for controlled evaluation. Distinct from prior benchmarks, OpenSkillRisk not only covers more realistic and diverse unsafe scenarios, but also provides a fine-grained analysis to diagnose the behavioral patterns of agents in such scenarios. We conduct comprehensive experiments covering three mainstream CLI agent frameworks and thirteen state-of-the-art LLMs. Experimental results show that no tested system handles risky skills reliably: even the safest configurations still execute unsafe actions in about 17% of cases. Context-dependent and system-level risks are especially difficult for current agent systems to avoid. Our behavioral analysis reveals three recurring failure patterns: agents may fail to recognize the risk, recognize it but fail to intervene before acting, or follow skill instructions beyond the user's intended scope. These findings highlight the need to improve both risk reasoning in LLMs and execution control in agent frameworks.

---


### 146. [Autonomous Collaborative Learning Among an Ensemble of Tsetlin Machines with Consensus-Based Inference](https://arxiv.org/abs/2607.20124)

**<font color=#1a73e8>作者：</font>** Yehuda Rudin, Osnat Keren, Michal Yemini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tsetlin Machine (TM) is a rule-based machine-learning algorithm comprising collectives of two-action Tsetlin Automata (TAs) that cooperatively form conjunctive logical clauses from Boolean inputs through stochastic feedback. Although few recent studies have examined TM Federated Learning, the broader area of distributed and decentralized TM learning has not received much attention in the existing literature and warrants further exploration. In this work, we propose a paradigm for decentralized collaborative learning under a vertical feature-partitioning setting among an ensemble of Tsetlin Machines using consensus-based inference. Within this decentralized paradigm, each agent maintains its own private TM model, and there is no exchange of raw data among agents. Inference combines individual agents model predictions into a global consensus. The paradigm accommodates heterogeneous TM-based agents with differing data acquisition means, local data distributions, or computational resources, thereby facilitating the integration and fusion of information in settings such as multi-modal sensing environments. Experiments conducted using two-dimensional grid and connected graph network topologies demonstrate that the classification accuracies achieved are comparable to those of centralized models.

---


### 147. [HeadCast: Casting Attention Heads for Efficient Autoregressive Video Generation](https://arxiv.org/abs/2607.20125)

**<font color=#1a73e8>作者：</font>** Jinliang Shen, Lianghao Su, Zheming Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive (AR) video diffusion models have become a promising paradigm for long and streaming video synthesis, but the continuously growing Key-Value (KV) cache makes attention the dominant inference cost, especially at high resolution where each frame contributes many tokens. Existing remedies either evict the cache with coarse heuristics that cause inter-frame flickering, or require model re-training. We propose HeadCast, a training-free, plug-and-play acceleration framework built on the observation that a pre-trained AR model's attention heads exhibit stable, heterogeneous behaviors. After a short warm-up, HeadCast performs a one-time classification at the maximum-noise step that sorts every head into one of four archetypes: Sink, Dummy, Spatial, and Global, and restructures the monolithic KV cache into head-specific pathways. Crucially, it retains the Global heads that preserve the long-range temporal consistency aggressive eviction destroys. Because the Spatial pathway operates on a fixed-size grid, its savings grow with resolution: across state-of-the-art AR models, HeadCast accelerates inference by up to 1.62x at 720P and 1.95x at 1080P, while keeping VBench quality on par with full attention and largely flicker-free. Code is available at this https URL .

---


### 148. [Back to Back with a Copy: A Computational Analysis of AI-Generated Visual Contemporary Art Pastiches](https://arxiv.org/abs/2607.20127)

**<font color=#1a73e8>作者：</font>** Anca Dinu, Andreiana Mihail, Andra-Maria Florescu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The aim of this paper is twofold. First, it investigates whether newer generative models are getting better at pastiching contemporary artworks. Second, it explores the consistency of the multidimensional nature of stylistic evaluation across different LLMs. Building on previous work, we analyze stylistic similarity between AI generated pastiches and the original artworks of twelve contemporary artists. We used five complementary computer vision models to capture texture, color, semantics, composition, and perceptual features through cosine distance in high-dimensional embedding spaces. The distances obtained show that the newer image generation model that we used has produced pastiches with improved semantic alignment and greater diversity than the model used in previous work. However, it was slightly less performant on shallow features such as color, texture, and perceptual adherence. Our findings confirm that artistic style is inherently multidimensional, and measuring it does not depend on any spatial architecture. These quantitative findings are contextualized through feedback from human evaluators, which are the artists themselves.

---


### 149. [Proceedings of The Fourth International Workshop on eXplainable AI for the Arts (XAIxArts 4)](https://arxiv.org/abs/2607.20131)

**<font color=#1a73e8>作者：</font>** Shuoyang Jasper Zheng, Terence Broad, Elizabeth Wilson 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The fourth workshop on Explainable AI for the Arts (XAIxArts) continues to bring together and expand a community of researchers and creative practitioners in Human-Computer Interaction (HCI), Interaction Design, AI, eXplainable AI (XAI), and Digital Arts to explore the role of XAI for the Arts. XAI is a key concern of Responsible and Human-Centred AI, emphasising HCI techniques that make opaque AI models more understandable to people. XAIxArts offers a distinctive lens to examine explainability through creative and artistic domains. The previous workshops explored the landscape and the speculative futures of AI in creative processes. To respond to emerging challenges and contribute to creative and societal transformation more broadly, this workshop focuses on the operationalisation of XAI in the Arts. Specifically, we will: i) critically reflect on emerging practices that encourage diversity and inclusivity in XAI; ii) collectively ideate a library of missing projects to encourage future collaborations and speculations; iii) scope the development of a resource hub for open XAIxArts projects to archive tangible XAI interventions and facilitate future community building with the wider discourse on Human-Centred AI.

---


### 150. [CURED: Creating, Understanding, and Repairing Errors Demonstrator](https://arxiv.org/abs/2607.20140)

**<font color=#1a73e8>作者：</font>** Nicholas Chandler, Sebastian Jäger, Philipp Jung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Detecting and cleaning errors in tabular data is a prerequisite for data intense software applications. Recent research at the intersection of Machine Learning (ML) and Database Management Systems (DBMS) highlights the potential of statistical learning algorithms for error detection and cleaning. This paper combines our recent work on ML-based data cleaning and error models in a unified demonstrator. The web application allows users to upload tabular data, perturb the data with realistic data dependent errors and use modern ML methods to clean and understand error mechanisms in data. Our demonstrator helps to bridge the gap between theoretical advancements and intuitive practical insights in the context of error models and data cleaning algorithms for tabular data. The demonstrator is available at this https URL

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-192](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
