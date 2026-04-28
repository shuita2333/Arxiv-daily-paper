# 📦 其他研究 | 2026年04月29日

> 本类共 **437** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-437](./part-09.md)

---

### 251. [Graph Memory Transformer (GMT)](https://arxiv.org/abs/2604.23862)

**<font color=#1a73e8>作者：</font>** Nicola Zanarini, Niccolò Ferrari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate whether the Feed-Forward Network (FFN) sublayer in a decoder-only transformer can be replaced by an explicit learned memory graph while preserving the surrounding autoregressive architecture. The proposed Graph Memory Transformer (GMT) keeps causal self-attention intact, but replaces the usual per-token FFN transformation with a memory cell that routes token representations over a learned bank of centroids connected by a learned directed transition matrix. In the base GMT v7 instantiation studied here, each of 16 transformer blocks contains 128 centroids, a 128 * 128 edge matrix, gravitational source routing, token-conditioned target selection, and a gated displacement readout. The cell therefore returns movement from an estimated source memory state toward a target memory state, rather than a retrieved value. The resulting model is a fully decoder-only language model with 82.2M trainable parameters and no dense FFN sublayers, compared with a 103.0M-parameter dense GPT-style baseline used in the evaluation. The base v7 model trains stably and exposes centroid usage, transition structure, and source-to-target movement as directly inspectable quantities of the forward computation. It remains behind the larger dense baseline in validation loss and perplexity (3.5995/36.58 vs. 3.2903/26.85), while showing close zero-shot benchmark behavior under the evaluated setting. These results are not intended as a state-of-the-art claim; they support the viability and structural interpretability of replacing dense within-token transformation with graph-mediated memory navigation. Broader scaling, optimized kernels, and more extensive benchmark evaluation are left for subsequent work.

---


### 252. [Learning Interpretable PDE Representations for Generative Reconstructions with Structured Sparsity](https://arxiv.org/abs/2604.23867)

**<font color=#1a73e8>作者：</font>** Valerie Tsao, Nathaniel Chaney, Manolis Veveakis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific measurements are often bottlenecked by suboptimal conditions, whether that be noise, incomplete spatial coverage, or limited resolution, rendering accurate field reconstruction a difficult task. We introduce LatentPDE, a latent diffusion framework designed to simultaneously resolve sparse-observation reconstruction and super-resolution. While existing physics-guided diffusion models typically rely on soft loss penalties or uninterpretable representations, our approach enforces physical compliance by constructing an inherently interpretable latent space. Specifically, we parameterize the latent variables directly as the coefficients and source terms of an assumed governing PDE. In doing so, LatentPDE is able to reliably reconstruct dynamics across highly disparate and structured data gaps. Empirical results on diverse configurations demonstrate that our model achieves high-fidelity recovery at any desired resolution while also tracking the underlying predictive uncertainty.

---


### 253. [Risk-Aware Robust Learning: Reducing Clinical Risk under Label Noise in Medical Image Classification](https://arxiv.org/abs/2604.23875)

**<font color=#1a73e8>作者：</font>** Maycon R. S. Pereira, Filipe R. Cordeiro  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Noisy labels are a pervasive challenge in medical image classification, where annotation errors arise from inter-observer variability and diagnostic ambiguity. Although several noise-robust learning methods have been proposed, their evaluation predominantly relies on accuracy-oriented metrics, overlooking the clinical implications of asymmetric error costs. In medical diagnosis, a false negative (missed disease) carries substantially higher consequences than a false positive (false alarm), as delayed treatment can directly impact patient outcomes. In this work, we investigate whether noise-robust training methods preserve clinical safety under label noise. We conduct a systematic risk-aware evaluation of the state-of-the-art noise-robust methods Coteaching, DivideMix, UNICON, and a GMM-based filtering approach on binarized DermaMNIST and PathMNIST datasets under clean and label noise rates of 20%, and 40%. Beyond balanced accuracy, we adopt a cost-sensitive Global Risk formulation that explicitly penalizes false negatives. Our analysis reveals that the robustness of state-of-the-art methods does not guarantee clinical safety. Furthermore, we demonstrate that integrating cost-sensitive optimization into noise-robust training significantly reduces clinical risk, while mantaining model utility. These findings demonstrate that noise-robust learning must be evaluated through a clinical risk lens, and that combining robust training with cost-sensitive optimization can meaningfully reduce risk in noisy-label medical imaging scenarios.

---


### 254. [Cardiac Stability Theory: An Axiomatically Grounded Framework for Continuous Cardiac Health Monitoring via Smartphone Photoplethysmography](https://arxiv.org/abs/2604.23876)

**<font color=#1a73e8>作者：</font>** Timothy Oladunni, Farouk Ganiyu Adewumi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present Cardiac Stability Theory (CST), an axiomatically grounded framework formally defining cardiovascular health as a stability margin around a cardiac dynamical attractor. From four axioms we derive the Cardiac Stability Index (CSI), a composite scalar in [0,1] integrating the largest Lyapunov exponent, recurrence determinism, and signal entropy via time-delay embedding. The ECG-based model (CSISurrogateV2, CNN-Transformer) achieves $R^2=0.8788$, MAE$=0.0234$ on PTB-XL (21,799 recordings). We extend CSI to smartphone PPG via Complementary Domain Transfer (CDT): CSISurrogateV2 generates pseudo-labels for the BUT PPG dataset (48 recordings, 12 subjects), training TinyCSINet (122,849 parameters), achieving MAE$=0.0557$, $\rho=0.660$ on the held-out test set ($n=1065$ windows) at ${<}30$ ms mobile latency. CDT is validated on BIDMC, Welltory, and RWS-PPG. Paired validation on 5,035 BIDMC windows yields $r=0.454$ ($\rho=0.485$, $p<10^{-295}$), confirming correlated cardiac stability across modalities. CSI is negatively correlated with age (slope $= -0.000225$ CSI/year, PTB-XL), discriminates atrial fibrillation from normal sinus rhythm (AUROC$=0.89$), and is robust under Perturbation Invariance Training (max AUC drop 1.65\%). We derive HeartSpan, a longitudinal stability metric relative to population age norms, enabling continuous non-invasive cardiac monitoring from commodity smartphones for longevity tracking and cardiac risk stratification.

---


### 255. [ZenBrain: A Neuroscience-Inspired 7-Layer Memory Architecture for Autonomous AI Systems](https://arxiv.org/abs/2604.23878)

**<font color=#1a73e8>作者：</font>** Alexander Bering  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Despite a century of empirical memory research, existing AI agent memory systems rely on system-engineering metaphors (virtual-memory paging, flat LLM storage, Zettelkasten notes), none integrating principles of consolidation, forgetting, and reconsolidation.
We present ZenBrain, a multi-layer memory architecture integrating fifteen neuroscience models. It implements seven memory layers (working, short-term, episodic, semantic, procedural, core, cross-context) orchestrated by nine foundational algorithms (Two-Factor Synaptic Model, vmPFC-coupled FSRS, Simulation-Selection sleep, Bayesian confidence, and five more) plus six new Predictive Memory Architecture (PMA) components: a four-channel NeuromodulatorEngine, prediction-error-gated ReconsolidationEngine, TripleCopyMemory with divergent decay, four-dimensional PriorityMap with amygdala fast-path, StabilityProtector (NogoA/HDAC3 analogue), and MetacognitiveMonitor for bias detection.
The 15-algorithm ablation reveals a cooperative survival network: under stress, 9 of 15 algorithms become individually critical (delta-Q up to -93.7%, Wilcoxon, 10 seeds, alpha=0.005). Simulation-Selection sleep achieves 37% stability improvement (p<0.005) with 47.4% storage reduction. TripleCopyMemory retains S(t)=0.912 at 30 days; PriorityMap reaches NDCG@10=0.997.
Multi-layer routing beats a flat single-layer baseline by 20.7% F1 on LoCoMo (p<0.005) and 19.5% on MemoryArena (p=0.015). On LongMemEval-500, ZenBrain holds the highest mean rank on all 12 system-judge cells (4 systems x 3 LLM judges), three-judge mean J=0.545 vs letta=0.485, a-mem=0.414, mem0=0.394; all 9 pair-wise contrasts clear Bonferroni (alpha=0.05/18, min p=6.2e-31, d in [0.18, 0.52]). Under LongMemEval's binary judge, ZenBrain reaches 91.3% of oracle accuracy at 1/106th the per-query token budget. Open-source with 11,589 automated test cases.

---


### 256. [Geometry Preserving Loss Functions Promote Improved Adaptation of Blackbox Generative Model](https://arxiv.org/abs/2604.23888)

**<font color=#1a73e8>作者：</font>** Sinjini Mitra, Constantine Kyriakakis, Shenyuan Liang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adaptation of blackbox generative models has been widely studied recently through the exploration of several methods including generator fine-tuning, latent space searches, leveraging singular value decomposition, and so on. However, adapting large-scale generative AI tools to specific use cases continues to be challenging, as many of these industry-grade models are not made widely available. The traditional approach of fine-tuning certain layers of a generative network is not feasible due to the expense of storing and fine-tuning generative models, as well as the restricted access to weights and gradients. Recognizing these challenges, we propose a novel end-to-end pipeline aimed at domain adaptation by leveraging geometry-preserving loss functions in conjunction to pre-trained generative adversarial networks (GANs). Our method rethinks the problem of adaptation by re-contextualizing the role of GAN inversion in obtaining accurate latent space representations. Extending the ability of existing state-of-the-art inverters, we preserve pair-wise distances between tangent spaces to successfully train a latent generative model to produce samples from the target distribution. We evaluate our proposed pipeline on StyleGANs with real distribution shifts and demonstrate that the introduction of the geometry preserving loss function lends to improved adaptation of generative models compared to other traditional loss functions.

---


### 257. [From Trust to Appropriate Reliance: Measurement Constructs in Human-AI Decision-Making](https://arxiv.org/abs/2604.23896)

**<font color=#1a73e8>作者：</font>** Muhammad Raees, Konstantinos Papangelis  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> While human-AI decision-making research has primarily used trust measurements to assess the practical usage of AI systems by their end-users, recent empirical evidence suggests that trust measurements do not inform users' appropriate reliance on AI systems. While examining the human-AI decision-making literature, in this work, we review empirical studies that assess people's appropriate reliance on AI advice, differentiating measurements and constructs of appropriate reliance from trust and mere reliance. Our analysis of literature shows that constructs for human-AI appropriate reliance are still fragmented in research. We present three views on appropriate reliance, namely Traditional, Appropriateness, and Dominance, as discussed in research. Using these views, we evaluate objective metrics reported in studies and argue for their consensus to facilitate the comparison across empirical research. We also discuss how studies employ objective metrics and examine their validity in application contexts. Our work contributes to the critical body of research on exploring objective metrics for assessing humans' appropriate reliance on AI advice.

---


### 258. [MarketBench: Evaluating AI Agents as Market Participants](https://arxiv.org/abs/2604.23897)

**<font color=#1a73e8>作者：</font>** Andrey Fradkin, Rohit Krishnan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Markets are a promising way to coordinate AI agent activity for similar reasons to those used to justify markets more broadly. In order to effectively participate in markets, agents need to have informative signals of their own ability to successfully complete a task and the cost of doing so. We propose MarketBench, a benchmark for assessing whether AI agents have these capabilities. We use a 93-task subset of SWE-bench Lite, a software engineering benchmark, with six recently released LLMs as a demonstration. These LLMs are miscalibrated on both success probability and token usage, and auctions built from these self-reports diverge from a full-information allocation. A follow-up intervention where we add information about capabilities from prior experiments to the context improves calibration, but only modestly narrows the gap to a full-information benchmark. We also document the performance of a market-based scaffolding with these LLMs. Our results point to self-assessment as a key bottleneck for market-style coordination of AI agents.

---


### 259. [Mammographic Lesion Segmentation with Lightweight Models: A Comparative Study](https://arxiv.org/abs/2604.23899)

**<font color=#1a73e8>作者：</font>** Helder Oliveira  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Breast cancer is a leading cause of cancer-related mortality among women worldwide, with mammography as the primary screening tool. While deep learning models have shown strong performance in lesion segmentation, most rely on computationally intensive architectures that limit their use in resource-constrained environments. This study evaluates the performance and efficiency of lightweight models for mammographic lesion segmentation. Architectures including MobileNetV2, EfficientNet Lite, ENet, and Fast-SCNN were compared against a U-Net baseline using the INbreast dataset with 5-fold cross-validation. Performance was assessed using Dice score, Intersection over Union (IoU), and Recall, alongside model complexity. MobileNetV2 with Squeeze-and-Excitation (SCSE) achieved the best performance, with a Dice score of 0.5766 while using approximately 75\% fewer parameters than U-Net. Cross-dataset evaluation on the DMID dataset showed reduced accuracy due to domain shift but preserved recall. These results demonstrate that lightweight architectures offer a practical balance between performance and efficiency for deployable CAD systems.

---


### 260. [SMSI: System Model Security Inference: Automated Threat Modeling for Cyber-Physical Systems](https://arxiv.org/abs/2604.23905)

**<font color=#1a73e8>作者：</font>** RoÝah Radaideh, Ali Khreis  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Threat modeling for cyber-physical systems (CPS) remains a largely manual exercise. This project presents SMSI (System Model Security Inference), a hybrid neuro-symbolic pipeline that starts from a SysML architecture model and produces a prioritized list of NIST 800-53 security controls. The prototype has three main stages: a deterministic parser mapping system components to vulnerabilities via the NVD; a family of retrieval and classification models linking vulnerabilities to MITRE ATT&CK techniques; and a control recommender. We explore three approaches for CVE-to-ATT&CK mapping: a supervised classifier using fine-tuned SecureBERT+, retrieval-based dense encoders, and a zero-shot LLM approach using Gemma-4 26B. We validate the pipeline on a healthcare IoT gateway with nine software components. For the ATT&CK-to-NIST stage, pretrained SecureBERT achieves the highest control retrieval scores, demonstrating that dense embeddings provide a strong basis for automated control recommendation.

---


### 261. [Machine Learning and Deep Learning Models for Short Term Electricity Price Forecasting in Australia's National Electricity Market](https://arxiv.org/abs/2604.23908)

**<font color=#1a73e8>作者：</font>** Wei Lu, Jay Wang, Dingli Duan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Short term electricity price forecast is essential in competitive power markets, yet electricity price series exhibit high volatility, irregularity, and non-stationarity. This phenomenon is pronounced in the South Australian region of the National Electricity Market, where high renewable penetration drives price volatility and frequent negative price intervals, while structural changes such as the transition to five-minute settlement further complicate forecast. To address these challenges, this study develops a unified benchmark framework. Under identical data preprocessing, feature engineering with lag features, rolling statistics, cyclic temporal encodings, and so on, and an 85% to 15% chronological train test split, six algorithms are systematically compared, including AWMLSTM, CatBoost, GBRT, LSTM, LightGBM, and SVR. The results show that for price prediction, tree-based models, especially GBRT with an R squared value of 0.88, generally outperform LSTM and SVR. However, all models achieve a mean absolute percentage error above 90%, and more than 65% of GBRT predictions have relative errors above 10%, which highlights the inherent difficulty of price forecast. For demand prediction, all models perform substantially better than in price prediction. AWMLSTM and GBRT achieve an R2 value of 0.96 with mean absolute percentage error below 32%, and GBRT has 74.37% of samples within 5% error, while LSTM and SVR perform less accurately in both tasks. Future improvements should focus on hybrid models such as tree plus transformers, data augmentation for extreme events, and error correction to better capture price spikes.

---


### 262. [AMAVA: Adaptive Motion-Aware Video-to-Audio Framework for Visually-Impaired Assistance](https://arxiv.org/abs/2604.23909)

**<font color=#1a73e8>作者：</font>** Benjamin Klein, Kazi Ruslan Rahman, Sanchita Ghose  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Navigational aids for blind and low vision individuals struggle conveying dynamic real-world environments, leading to cognitive overload from continuous, undifferentiated feedback. We present AMAVA, a novel real-time video-to-audio framework that converts mobile device video into contextually relevant sound effects or text-to-speech descriptions. We propose a motion-aware pipeline using a lightweight AI classification model to distinguish between low and high-movement scenes followed by a real-time text-to-audio synthesis pipeline to enhance environmental perception more efficiently. In static environments, AMAVA generates spoken audio scene descriptions for situational awareness. In high-movement situations, it prioritizes safety by delivering sound cues, such as spoken hazard alerts and environmental sound effects. These audio outputs are produced by a decoder-only transformer-based vision-language model with mixture-of-experts and cross-modal attention for visual understanding, in conjunction with neural text-to-speech and natural sound synthesis networks. The proposed framework uses prompt-based caching and category-specific throttling to avoid auditory clutter and minimize latency. We present a comprehensive evaluation of the system, including a real-time navigation study comparing a white cane alone versus with AMAVA, that shows a significant increase in user confidence and perceived safety.

---


### 263. [Gromov-Wasserstein Methods for Multi-View Relational Embedding and Clustering](https://arxiv.org/abs/2604.23912)

**<font color=#1a73e8>作者：</font>** Rafael Pereira Eufrazio, Eduardo Fernandes Montesuma, Charles Casimiro Cavalcante  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning low-dimensional representations from multi-view relational data is challenging when underlying geometries differ across views. We propose Bary-GWMDS, a Gromov-Wasserstein-based method that operates directly on distance matrices to learn a consensus embedding preserving shared relational structure. By leveraging intrinsic distances, the approach naturally handles nonlinear distortions across views. We also introduce Mean-GWMDS-C, a clustering-oriented formulation that averages distance matrices and learns reduced-support representations via a consensus Gromov-Wasserstein transport. Experiments on synthetic and real-world datasets show that the proposed framework yields stable and geometrically meaningful embeddings.

---


### 264. [Crystal structure prediction using graph neural combinatorial optimization](https://arxiv.org/abs/2604.23921)

**<font color=#1a73e8>作者：</font>** Stavros Gerolymatos, J. Kyle Brubaker, Martin J. A. Schuetz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Crystalline materials are widely used in technological applications, yet their discovery remains a significant challenge. As their properties are driven by structure, crystal structure prediction (CSP) methods play a central role in computational approaches aiming to accelerate this process. Previously, CSP has been approached from a combinatorial optimization perspective, with the core challenge of allocating atoms on a fine grid of predefined discrete positions within a unit cell while minimizing their interaction energy. Exact mathematical optimization methods provide guaranteed solutions, but they become computationally expensive for large-scale instances, where the atomic configuration space grows rapidly, particularly in the absence of additional symmetry constraints. In this work, we introduce a neural combinatorial optimization approach to the atom allocation challenge and, subsequently, CSP, based on graph neural networks (GNNs), which can effectively sample from the distribution of feasible structures in an unsupervised manner. We leverage expander graphs to construct computational graphs over discrete positions that capture both short- and long-range interactions between atoms, and employ the Gumbel-Sinkhorn approach to enforce the desired stoichiometry of the generated structures. We demonstrate that our method outperforms classical heuristic approaches and is competitive with a commercial optimization solver across a range of chemical compositions. This enables the use of ever-expanding GPU infrastructure to tackle the inherent combinatorial challenges of CSP, paving the way for scaling beyond current capabilities.

---


### 265. [Towards Localizing Conversation Partners using Head Motion](https://arxiv.org/abs/2604.23927)

**<font color=#1a73e8>作者：</font>** Payal Mohapatra, Calvin Murdock, Ali Aroudi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Many individuals struggle to understand conversation partners in noisy settings, particularly amid background speakers or due to hearing impairments. Emerging wearables like smartglasses offer a transformative opportunity to enhance speech from conversation partners. Crucial to this is identifying the direction in which the user wants to listen, which we refer to as the user's acoustic zones of interest. While current spatial audio-based methods can resolve the direction of vocal input, they are agnostic to listening preferences and have limited functionality in noisy settings with interfering speakers. To address this, behavioral cues are needed to actively infer a user's acoustic zones of interest. We explore the effectiveness of head-orienting behavior, captured by Inertial Measurement Units (IMUs) on smartglasses, as a modality for localizing these zones in seated conversations. We introduce HALo, a head-orientation-based acoustic zone localization network that leverages smartglasses' IMUs to non-invasively infer auditory zones of interest corresponding to conversation partner locations. By integrating an a priori estimate of the number of conversation partners, our approach yields a 21% performance improvement over existing methods. We complement this with CoCo, which classifies the number of conversation partners using only IMU data, achieving 0.74 accuracy and a 35% gain over rule-based and generic time-series baselines. We discuss practical considerations for feature extraction and inference and provide qualitative analyses over extended sessions. We also demonstrate a minimal end-to-end speech enhancement system, showing that head-orientation-based localization offers clear advantages in extremely noisy settings with multiple conversation partners.

---


### 266. [Robust and Clinically Reliable EEG Biomarkers: A Cross Population Framework for Generalizable Parkinson's Disease Detection](https://arxiv.org/abs/2604.23933)

**<font color=#1a73e8>作者：</font>** Nicholas R. Rasmussen, Longwei Wang, Rodrigue Rizk 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Developing robust and clinically reliable EEG biomarkers requires evaluation frameworks that explicitly address cross population generalization in multi site settings such as Parkinsons disease (PD) detection. Models trained under i.i.d. assumptions often capture population specific artifacts rather than disease relevant neural structure, leading to poor generalization across clinical cohorts. EEG further amplifies this challenge due to low signal to noise ratio and heterogeneous acquisition conditions. We propose a population aware evaluation framework to assess the robustness and clinical reliability of EEG biomarkers under distribution shift. Using an n gram expansion strategy, we enumerate all cross population train test configurations across five independent cohorts, resulting in 75 directional evaluations. A nested cross validation design with integrated channel selection ensures prospective biomarker identification without population leakage. Results show that cross population transfer is asymmetric and that both accuracy and biomarker stability improve with increasing training population diversity, achieving up to 94.1% accuracy on held out cohorts. A theoretical analysis based on mixture risk optimization and hypothesis space contraction explains these trends, showing that multi population training promotes population robust representations. This work establishes a principled framework for learning robust, generalizable, and clinically reliable EEG biomarkers for multi site biomedical applications.

---


### 267. [2nd of the 5th PVUW MeViS-Audio Track: ASR-SaSaSa2VA](https://arxiv.org/abs/2604.23935)

**<font color=#1a73e8>作者：</font>** Zhiyu Wang, Xudong Kang, Shutao Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio-based video object segmentation aims to locate and segment objects in videos conditioned on audio cues, requiring precise understanding of both appearance and motion. Recent audio-driven video segmentation methods extend MLLMs by fusing audio and visual features for end-to-end localization. Despite their promise, these approaches are computationally intensive, struggle with aligning temporal audio cues to dynamic video content, and depend on large paired audio-video datasets. To address these challenges, we present ASR-SaSaSa2VA, a resource-efficient framework for audio-guided video segmentation. The key idea is to convert audio inputs into textual motion descriptions via automatic speech recognition (ASR) models and then leverage pre-trained text-based referring video segmentation models (e.g., SaSaSa2VA) for pixel-level predictions. To further enhance robustness, we incorporate a no-target expression detection module, implemented by a fine-tuned audio-based MLLM, which filters out audio clips that do not refer to any target object. This design allows the system to exploit strong pre-trained models while effectively handling ambiguous or irrelevant audio inputs. Our approach achieves a final score of 80.7 in the 5th PVUW Challenge (MeViS-v2-Audio track), earning the second-place ranking.

---


### 268. [GoClick: Lightweight Element Grounding Model for Autonomous GUI Interaction](https://arxiv.org/abs/2604.23941)

**<font color=#1a73e8>作者：</font>** Hongxin Li, Yuntao Chen, Zhaoxiang Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Graphical User Interface (GUI) element grounding (precisely locating elements on screenshots based on natural language instructions) is fundamental for agents interacting with GUIs. Deploying this capability directly on resource-constrained devices like mobile phones is increasingly critical for GUI agents requiring low latency. However, this goal faces a significant challenge, as current visual grounding methods typically employ large vision-language model (VLM) (more than 2.5B parameters), making them impractical for on-device execution due to memory and computational constraints. To address this, this paper introduces GoClick, a lightweight GUI element grounding VLM with only 230M parameters that achieves excellent visual grounding accuracy, even on par with significantly larger models. Simply downsizing existing decoder-only VLMs is a straightforward way to design a lightweight model, but our experiments reveal that this approach yields suboptimal results. Instead, we select an encoder-decoder architecture, which outperforms decoder-only alternatives at small parameter scales for GUI grounding tasks. Additionally, the limited capacity of small VLMs encourages us to develop a Progressive Data Refinement pipeline that utilizes task type filtering and data ratio adjustment to extract a high-quality 3.8M-sample core set from a 10.8M raw dataset. Training GoClick using this core set brings notable grounding accuracy gains. Our experiments show that GoClick excels on multiple GUI element grounding benchmarks while maintaining a small size and high inference speed. GoClick also enhances GUI agent performance when integrated into a device-cloud collaboration framework, where GoClick helps cloud-based task planners perform precise element localization and achieve higher success rates. We hope our method serves as a meaningful exploration within the GUI agent community.

---


### 269. [GAMED.AI: A Hierarchical Multi-Agent Framework for Automated Educational Game Generation](https://arxiv.org/abs/2604.23947)

**<font color=#1a73e8>作者：</font>** Shiven Agarwal, Yash Shah, Ashish Raj Shekhar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce GameDAI, a hierarchical multi-agent framework that transforms instructor-provided questions into fully playable, pedagogically grounded educational games validated through formal mechanic contracts. Built on phase-based LangGraph sub-graphs, deterministic Quality Gates, and structured Pydantic schemas, GameDAI supports two template families encompassing 15 interaction mechanics across spatial reasoning, procedural execution, and higher-order Bloom's Taxonomy objectives. Evaluated on 200 questions spanning five subject domains, the system achieves a 90% validation pass rate, 98.3% schema compliance, and 73% token reduction over ReAct agents (${\sim}$73,500 $\rightarrow$ ${\sim}$19,900 tokens/game) at $0.46 per game. Within this model configuration, these results suggest that phase-bounded architectural structure correlates more strongly with alignment quality than prompting strategy alone. Our demonstration lets attendees generate Bloom's-aligned games from natural language in under 60 seconds, inspect Quality Gate outputs at each pipeline phase, and browse a curated library of 50 games spanning all 15 mechanic types.

---


### 270. [KOMBO: Korean Character Representations Based on the Combination Rules of Subcharacters](https://arxiv.org/abs/2604.23948)

**<font color=#1a73e8>作者：</font>** SungHo Kim, Juhyeong Park, Yeachan Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The Korean writing system, \textit{Hangeul}, has a unique character representation rigidly following the invention principles recorded in \textit{Hunminjeongeum}.\footnote{\textit{Hunminjeongeum} is a book published in 1446 that describes the principles of invention and usage of \textit{Hangeul}, devised by King Sejong \cite{Hunminjeongeum_Guide}.} However, existing pre-trained language models (PLMs) for Korean have overlooked these principles. In this paper, we introduce a novel framework for Korean PLMs called KOMBO, which firstly brings the invention principles of \textit{Hangeul} to represent character. Our proposed method, KOMBO, exhibits notable experimental proficiency across diverse NLP tasks. In particular, our method outperforms the state-of-the-art Korean PLM by an average of 2.11\% in five Korean natural language understanding tasks. Furthermore, extensive experiments demonstrate that our proposed method is suitable for comprehending the linguistic features of the Korean language. Consequently, we shed light on the superiority of using subcharacters over the typical subword-based approach for Korean PLMs. Our code is available at: [this https URL](this https URL).

---


### 271. [Viewport-Unaware Blind Omnidirectional Image Quality Assessment: A Unified and Generalized Approach](https://arxiv.org/abs/2604.23953)

**<font color=#1a73e8>作者：</font>** Jiebin Yan, Kangcheng Wu, Jingwen Hou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Blind omnidirectional image quality assessment (BOIQA) presents a great challenge to the visual quality assessment community, due to different storage formats and diverse user viewing behaviors. The main paradigm of BOIQA models includes two steps, ie, viewport generation, and quality prediction, which brings an extra computational burden and is hard to generalize to other visual contents (eg, 2D planar image). Thus, in this paper, we make an attempt to solve these issues. First, we experimentally find that BOIQA can be formulated as a blind (2D planar) image quality assessment (BIQA) problem, ie, the first step - viewport generation - is no longer needed, which narrows the natural gap between BOIQA and BIQA. Then, we present a new BOIQA approach, which has three merits: ie, viewport-unaware - it accepts an omnidirectional image in the widely used equirectangular projection format as input without any transformation; unified - it can also be applied to BIQA; and generalized - it shows better generalizability against other competitors. Finally, we validate its promise by held-out test, cross-database validation, and the well-established gMAD competition.

---


### 272. [An empirical evaluation of the risks of AI model updates using clinical data: stability, arbitrariness, and fairness](https://arxiv.org/abs/2604.23954)

**<font color=#1a73e8>作者：</font>** Ioannis Bilionis, Ricardo C. Berrios, Luis Fernandez-Luque 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial Intelligence and Machine Learning (AI/ML) models used in clinical settings are increasingly deployed to support clinical decision-making. However, when training data become stale due to changes in demographics, environment, or patient behaviors, model performance can degrade substantially. While updating models with new training data is necessary, such updates may also introduce new risks. We evaluated the proposed monitoring framework on four publicly available U.S.-based Type 1 Diabetes datasets containing high-resolution continuous glucose monitoring (CGM) data, comprising approximately 11,300 weekly observations from 496 participants under 20 years of age. All datasets included structured sociodemographic information. Using the prediction of severe hyperglycemia events in children with type 1 diabetes as a case study, we examine how different model update strategies can adversely affect model stability (e.g., by causing predictions to "flip" for a large number of cases after an update), increase arbitrariness in predictions, or worsen accuracy equity and the balance of error rates across subpopulations. We propose multiple dimensions for continuous monitoring to detect these issues and argue that such monitoring is essential for the development of trustworthy clinical decision support systems.

---


### 273. [LAVA: Layered Audio-Visual Anti-tampering Watermarking for Robust Deepfake Detection and Localization](https://arxiv.org/abs/2604.23957)

**<font color=#1a73e8>作者：</font>** Bokang Zeng, Zheng Gao, Xiaoyu Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Proactive watermarking offers a promising approach for deepfake tamper detection and localization in short-form videos. However, existing methods often decouple audio and visual evidence and assume that watermark signals remain reliable under real-world degradations, making tamper localization vulnerable to multimodal misalignment and compression distortions. Moreover, existing semi-fragile visual watermarking methods often degrade significantly under codec compression because their embedding bands overlap with compression-sensitive frequency regions. To address these limitations, we propose Layered Audio-Visual Anti-tampering Watermarking (LAVA), a calibration-aware audio-visual watermark fusion framework for deepfake tamper detection and localization. LAVA leverages cross-modal watermark fusion and calibration-aware alignment to preserve consistent and reliable tamper evidence under compression and audio-visual asynchrony, enabling robust tamper localization. Extensive experiments demonstrate that LAVA achieves near-perfect detection performance (AP = 0.999), remains robust to compression and multimodal misalignment, and significantly improves tamper localization reliability over existing audio-visual fusion baselines.

---


### 274. [Task-guided Spatiotemporal Network with Diffusion Augmentation for EEG-based Dementia Diagnosis and MMSE Prediction](https://arxiv.org/abs/2604.23964)

**<font color=#1a73e8>作者：</font>** Xiaoyu Zheng, Xu Tian, Bin Jiao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Patients with dementia typically exhibit cognitive impairment, which is routinely assessed using the Mini-Mental State Examination (MMSE). Concurrently, their underlying neurophysiological abnormalities are reflected in Electroencephalography (EEG), providing a basis for joint modeling. However, traditional multi-task approaches suffer from feature entanglement, which leads to inter-task interference when handling heterogeneous this http URL address this challenge, we propose a task-guided spatiotemporal network (TGSN) with diffusion augmentation for EEG-based dementia diagnosis and MMSE prediction. Specifically, TGSN integrates a multi-band feature fusion module to capture complementary spectral information from EEG. Meanwhile, a pre-trained data augmentation module utilizing a diffusion process is introduced toincrease sample diversity. To model the complex spatiotemporal patterns of EEG, we propose a gated spatiotemporal attention module that captures long-range spatial dependencies and temporal dynamics. Moreover, we design a task-guided query module to achieve task-specific feature extraction, thereby mitigating task interference. The effectiveness of TGSN is evaluated on the XY02 dataset. Experimental results demonstrate that the proposed network outperforms several state-of-the-art methods, achieving classification accuracies of 97.78\% for Alzheimer's Disease (AD)/Frontotemporal Dementia (FTD) and 83.93\% for AD/FTD/Vascular Cognitive Impairment (VCI), which exceed the best baselines by 16.39\% and 8.28\%, respectively. In parallel, it reduces the RMSE for MMSE prediction to 1.93 and 2.38, achieving significant error reductions of 1.44 and 1.43 compared to the best baselines. Additionally, validation on the DS004504 dataset demonstrates strong cross-dataset generalization...

---


### 275. [DecompKAN: Decomposed Patch-KAN for Long-Term Time Series Forecasting](https://arxiv.org/abs/2604.23968)

**<font color=#1a73e8>作者：</font>** Naveen Mysore  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate time series forecasting in scientific domains such as climate modeling, physiological monitoring, and energy systems benefits from both competitive predictions and model transparency. This work proposes DecompKAN, a lightweight attention-free architecture that combines trend-residual decomposition, channel-wise patching, learned instance normalization, and B-spline Kolmogorov-Arnold Network (KAN) edge functions. Each KAN edge learns an explicit, inspectable 1D scalar function over learned patch-embedding coordinates that can be directly visualized. On standard benchmarks, DecompKAN achieves best or tied-best MSE on 15 of 32 dataset-horizon combinations among selected published baselines, and achieves best or tied-best MSE on 20 of 36 comparisons under a controlled same-recipe evaluation across 9 datasets including the physiological PPG-DaLiA benchmark. The architecture shows particular strength on datasets with smooth temporal dynamics (Solar -17%, ECL -10% vs. iTransformer, Weather) and physiological time series. Visualization of learned edge functions reveals qualitatively different latent nonlinearities across domains. Ablation analysis shows that the architectural pipeline (decomposition, patching, normalization) drives performance more than the choice of nonlinear layer, while the KAN formulation enables inspection of learned latent transformations.

---


### 276. [Quantum Knowledge Graph: Modeling Context-Dependent Triplet Validity](https://arxiv.org/abs/2604.23972)

**<font color=#1a73e8>作者：</font>** Yao Wang, Zixu Geng, Jun Yan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge graphs (KGs) are increasingly used to support large lan guage model (LLM) reasoning, but standard triplet-based KGs treat each relation as globally valid. In many settings, whether a relation should count as evidence depends on the context. We therefore formulate triplet validity as a triplet-specific function of context and refer to this formulation as a Quantum Knowledge Graph (QKG). We instantiate QKG in medicine using a diabetes-centered PrimeKG subgraph, whose 68,651 context-sensitive relations are further annotated with patient-group-specific constraints. We evaluate it in a reasoner--validator pipeline for medical question answering on a KG-grounded subset of MedReason containing 2,788 questions. With Haiku-4.5 as both the Reasoner and the Validator, KG-backed validation significantly improves over a no-validator baseline ($+0.61$ pp), and QKG with context matching yields the largest gain, outperforming both KG validation without context matching ($+0.79$ pp) and the no-validator baseline ($+1.40$ pp; paired McNemar, all $p<0.05$). Under a stronger validator (Qwen-3.6-Plus), the raw QKG gain over the no-validator baseline grows from $+1.40$ pp to $+5.96$ pp; the context-matching gap is non-significant ($p=0.73$) on the raw set but becomes borderline significant ($p=0.05$) after adjustment for knowledge leakage and suspicious questions, consistent with a benchmark-gold ceiling rather than a QKG limitation. Taken together, the results support the view that the value of a KG in LLM-based clinical reasoning lies not merely in storing medically related facts, but in representing whether those facts are applicable to the specific patient context. For reproducibility and further research, we release the curated QKG datasets and source code.\footnote{this https URL}

---


### 277. [Propagation Structure-Semantic Transfer Learning for Robust Fake News Detection](https://arxiv.org/abs/2604.23974)

**<font color=#1a73e8>作者：</font>** Mengyang Chen, Lingwei Wei, Han Cao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fake news generally refers to false information that is spread deliberately to deceive people, which has detrimental social effects. Existing fake news detection methods primarily learn the semantic features from news content or integrate structural features from propagation. However, in practical scenarios, due to the semantic ambiguity of informal language and unreliable user interactive behaviors on social media, there are inherent semantic and structural noises in news content and propagation. Although some recent works consider the effect of irrelevant user interactions in a hybrid-modeling way, they still suffer from the mutual interference between structural noise and semantic noise, leading to limited performance for robust detection. To alleviate this issue, this paper proposes a novel Propagation Structure-Semantic Transfer Learning framework (PSS-TL) for robust fake news detection under a teacher-student architecture. Specifically, we design dual teacher models to learn semantics knowledge and structure knowledge from noisy news content and propagation structure independently. Besides, we design a Multi-channel Knowledge Distillation (MKD) loss to enable the student model to acquire specialized knowledge from the teacher models, thereby avoiding mutual interference. Extensive experiments on two real-world datasets validate the effectiveness and robustness of our method.

---


### 278. [Hindsight Preference Optimization for Financial Time Series Advisory](https://arxiv.org/abs/2604.23988)

**<font color=#1a73e8>作者：</font>** Yanwei Cui, Guanghui Wang, Xing Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series models predict numbers; decision-makers need advisory -- directional signals with reasoning, actionable suggestions, and risk management. Training language models for such predictive advisory faces a fundamental challenge: quality depends on outcomes unknown at prediction time. We bridge two ideas from reinforcement learning -- using information unavailable during execution to retrospectively generate training signal, and preference alignment -- and propose Hindsight Preference Optimization: observed outcomes let an LLM judge rank candidate advisories on dimensions that scalar metrics cannot capture, producing preference pairs for DPO without human annotation. We apply this to Vision-Language-Model-based predictive advisories on S&P 500 equity time series, demonstrated by a 4B model outperforming its 235B teacher on both accuracy and advisory quality.

---


### 279. [Fix Initial Codes and Iteratively Refine Textual Directions Toward Safe Multi-Turn Code Correction](https://arxiv.org/abs/2604.23989)

**<font color=#1a73e8>作者：</font>** Yuto Tanaka, Issei Sato  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work on large language models (LLMs) has emphasized the importance of scaling inference compute. From this perspective, the state-of-the-art method Scattered Forest Search (SFS) has been proposed, employing Monte Carlo Tree Search with carefully crafted initial seeds and textual optimization for multi-turn code correction. However, its complexity makes it unclear what factors contribute to improvements in inference performance. To address this problem, we analyze SFS and propose a simpler method, Iterative Refinement of Textual Directions (IRTD), which fixes initial codes and iteratively refines textual directions. Because of the simplicity of IRTD, we theoretically establish the safety of IRTD using Oracle-Guided Inductive Synthesis (OGIS). Experiments on several code generation benchmarks suggest that IRTD achieves inference performance comparable to state-of-the-art methods. These results indicate that, even without complex search structures, refining initial codes with high-quality textual directions alone can effectively improve inference performance.

---


### 280. [Failure-Centered Runtime Evaluation for Deployed Trilingual Public-Space Agents](https://arxiv.org/abs/2604.23990)

**<font color=#1a73e8>作者：</font>** M. Meng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents PSA-Eval, a failure-centered runtime evaluation framework for deployed trilingual public-space agents. The central claim is that, when the evaluation object shifts from a static input-output mapping to a runtime system, the basic unit of analysis should shift from score to failure. PSA-Eval extends the conventional chain Question -> Answer -> Score -> End into Question -> Batch -> Run -> Score -> Failure Case -> Repair -> Regression Batch, making failures traceable, reviewable, repairable, and regression-testable.
The framework uses trilingual equivalent inputs as controlled probes for observing group-level cross-language policy drift. We conduct a pilot study on a real trilingual digital front-desk system deployed in the lobby of an international financial institution. The pilot uses a simplified single-foundation-model setting (MA = MB), so the observed drift should not be interpreted as an A/B foundation-model difference. The study contains 81 samples organized into 27 trilingual equivalent question groups. Although the system achieves an average score of 23.15/24, 14 groups show non-zero cross-language score drift, 5 groups show drift of at least 3 points, and the maximum drift reaches 9 points. These results provide initial evidence that failure-centered runtime evaluation can expose structured deployment signals hidden by aggregate scoring.

---


### 281. [EPM-RL: Reinforcement Learning for On-Premise Product Mapping in E-Commerce](https://arxiv.org/abs/2604.23993)

**<font color=#1a73e8>作者：</font>** Minhyeong Yu, Wonduk Seo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Product mapping, the task of deciding whether two e-commerce listings refer to the same product, is a core problem for price monitoring and channel visibility. In real marketplaces, however, sellers frequently inject promotional keywords, platform-specific tags, and bundle descriptions into titles, causing the same product to appear under many different names. Recent LLM-based and multi-agent frameworks improve robustness and interpretability on such hard cases, but they often rely on expensive external APIs, repeated retrieval, and complex inference-time orchestration, making large-scale deployment costly and difficult in privacy-sensitive enterprise settings. To address these issues, we present EPM-RL, a reinforcement-learning-based framework for building an accurate and efficient on-premise e-commerce product mapping model. Our central idea is to distill high-cost agentic reasoning into a trainable in-house model. Starting from a curated set of product pairs with LLM-generated rationales and human verification, we first perform parameter-efficient fine-tuning (PEFT) on a small student model using structured reasoning outputs. We then further optimize the model with Reinforcement Learning (RL) using an agent-based reward that jointly evaluates output-format compliance, label correctness, reasoning--preference scores from specially designed judge models. Preliminary results show that EPM-RL consistently improves over PEFT-only training and offers a stronger quality--cost trade-off than commercial API-based baselines, while enabling private deployment and lower operational cost. These findings suggest that reinforcement learning can turn product mapping from a high-latency agentic pipeline into a scalable, inspectable, and production-ready in-house system.

---


### 282. [CT-FineBench: A Diagnostic Fidelity Benchmark for Fine-Grained Evaluation of CT Report Generation](https://arxiv.org/abs/2604.24001)

**<font color=#1a73e8>作者：</font>** Ruifeng Yuan, Wanxing Chang, Weiwei Cao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The evaluation of generated reports remains a critical challenge in Computed Tomography (CT) report generation, due to the large volume of text, the diversity and complexity of findings, and the presence of fine-grained, disease-oriented attributes. Conventional evaluation metrics offer only coarse measures of lexical overlap or entity matching and fail to reflect the granular diagnostic accuracy required for clinical use. To address this gap, we propose CT-FineBench, a benchmark built from CT-RATE and Merlin to evaluate the fine-grained factual consistency of CT reports, constructed from CT-RATE and Merlin. Our benchmark is constructed through a meticulous, Question-Answering (QA) based process: first, we identify and structure key, finding-specific clinical attributes (like location, size, margin). Second, we systematically transform these attributes into a QA dataset, where questions probe for specific clinical details grounded in gold-standard reports. The evaluation protocol for CT-FineBench involves using this QA dataset to query a machine-generated report and scoring the correctness of the answers. This allows for a comprehensive, interpretable, and clinically-relevant assessment, moving beyond superficial lexical overlap to pinpoint specific clinical errors. Experiments show that CT-FineBench correlates better with expert clinical assessment and is substantially more sensitive to fine-grained factual errors than prior metrics.

---


### 283. [TCOD: Exploring Temporal Curriculum in On-Policy Distillation for Multi-turn Autonomous Agents](https://arxiv.org/abs/2604.24005)

**<font color=#1a73e8>作者：</font>** Jiaqi Wang, Wenhao Zhang, Weijie Shi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) has shown strong potential for transferring reasoning ability from frontier or domain-specific models to smaller students. While effective on static single-turn tasks, its behavior in multi-turn agent settings remains underexplored. In this work, we identify a key limitation of vanilla OPD in such settings, which we term Trajectory-Level KL Instability. Specifically, we observe that KL divergence increases together with a drop in success rate, and even after convergence, the KL remains high, leading to unstable training. This instability arises from inter-turn error compounding: as errors accumulate, the student is driven beyond the teacher's effective support, rendering the supervision signal unreliable. To address this, we propose TCOD (Temporal Curriculum On-Policy Distillation), a simple yet effective framework that controls the trajectory depth exposed to the student and progressively expands it from short to long with a curriculum this http URL results across four student-teacher pairs on three multi-turn agent benchmarks (ALFWorld, WebShop, ScienceWorld) show that TCOD mitigates KL escalation and enhances KL stability throughout training, improving agent performance by up to 18 points over vanilla OPD. Further evaluations show that TCOD can even surpass the teacher's performance and generalize to tasks on which the teacher fails.

---


### 284. [FedSLoP: Memory-Efficient Federated Learning with Low-Rank Gradient Projection](https://arxiv.org/abs/2604.24012)

**<font color=#1a73e8>作者：</font>** Yutong He, Zhengyang Huang, Jiahe Geng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning enables a population of clients to collaboratively train machine learning models without exchanging their raw data, but standard algorithms such as FedAvg suffer from slow convergence and high communication and memory costs in heterogeneous, resource-constrained environments. We introduce FedSLoP, a federated optimization algorithm that combines stochastic low-rank subspace projections of gradients, thereby reducing the dimension of communicated and stored updates while preserving optimization progress. On the theoretical side, we develop a detailed nonconvex convergence analysis under standard smoothness and bounded-variance assumptions, showing that FedSLoP is guaranteed to converge to a first-order stationary point at a rate of $O(1/\sqrt{NT})$. On the empirical side, we conduct extensive experiments on federated MNIST classification with heterogeneous data partitions, showing that FedSLoP substantially reduces communication volume and client-side memory while achieving competitive or better accuracy compared with FedAvg and representative sparse or low-rank baselines. Together, our results demonstrate that random subspace momentum methods such as FedSLoP provide a principled and effective approach to communication- and memory-efficient federated learning. Codes are available at: this https URL.

---


### 285. [Geometry-Aware Offline-to-Online Learning in Linear Contextual Bandits](https://arxiv.org/abs/2604.24016)

**<font color=#1a73e8>作者：</font>** Zean Han, Ruihan Lin, Zezhen Ding 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study offline-to-online learning in linear contextual bandits with biased offline regression data: the offline parameter need not match the online one, so history should not be treated as a single warm start. We model directional transfer with a shift certificate $(M_{\mathrm{shift}},\rho)$ and offline ridge estimation, yielding a geometry-aware confidence region for the online parameter rather than an isotropic radius. We propose \emph{Ellipsoidal-MINUCB}, which combines a standard online branch with an offline-informed pooled branch and uses offline information only when it tightens uncertainty. With high probability, regret is bounded by the minimum of a standard SupLinUCB-style fallback and a pooled term that separates statistical width from a certificate-weighted shift penalty. Under a simple alignment condition, the pooled term further simplifies to a rate governed by an effective dimension induced by the offline geometry. We also show that a purely Euclidean (scalar) shift bound, by itself, does not determine which feature directions are transferable. Beyond this fixed certificate, we show how to learn a data-driven certificate from data at finitely many refresh times and establish a high-probability regret bound for Ellipsoidal-MINUCB with epoch-wise learned certificates. Experiments match the main prediction: gains are strongest at intermediate horizons when offline coverage and transferability align, while the method otherwise tracks the safe online baseline.

---


### 286. [Poster: ClawdGo: Endogenous Security Awareness Training for Autonomous AI Agents](https://arxiv.org/abs/2604.24020)

**<font color=#1a73e8>作者：</font>** Jiaqi Li, Yang Zhao, Bin Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous AI agents deployed on platforms such as OpenClaw face prompt injection, memory poisoning, supply-chain attacks, and social engineering, yet existing defences address only the platform perimeter, leaving the agent's own threat judgement entirely untrained. We present ClawdGo, a framework for endogenous security awareness training: we teach the agent to recognise and reason about threats from the inside, at inference time, with no model modification. Four contributions are introduced: TLDT (Three-Layer Domain Taxonomy) organises 12 trainable dimensions across Self-Defence, Owner-Protection, and Enterprise-Security layers; ASAT (Autonomous Security Awareness Training) is a self-play loop where the agent alternates attacker, defender, and evaluator roles under weakest-first curriculum scheduling; CSMA (Cross-Session Memory Accumulation) compounds skill gains via a four-layer persistent memory architecture and Axiom Crystallisation Promotion (ACP); and SACP (Security Awareness Calibration Problem) formalises the precision-recall tradeoff introduced by endogenous training. Live experiments show weakest-first ASAT raises average TLDT score from 80.9 to 96.9 over 16 sessions, outperforming uniform-random scheduling by 6.5 points and covering 11 of 12 dimensions. CSMA retains the full gain across sessions; cold-start ablation recovers only 2.4 points, leaving a 13.6-point gap. E-mode generates 32 TLDT-conformant scenarios covering all 12 dimensions. SACP is observed when a heavily trained agent classifies a legitimate capability assessment as prompt injection (30/160).

---


### 287. [QED: An Open-Source Multi-Agent System for Generating Mathematical Proofs on Open Problems](https://arxiv.org/abs/2604.24021)

**<font color=#1a73e8>作者：</font>** Chenyang An, Qihao Ye, Minghao Pan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We explore a central question in AI for mathematics: can AI systems produce original, nontrivial proofs for open research problems? Despite strong benchmark performance, producing genuinely novel proofs remains an outstanding challenge for LLMs. Through systematic experiments with frontier LLMs on research-level proof tasks, we identify seven failure modes that prevent reliable proof generation, including context contamination, citation hallucination, hand-waving on key steps and misallocation of proof effort, unstable proof plans, unfocused verification, problem modification and single-model bottleneck. We argue that the gap between benchmark success and research-level proving is primarily one of system design, due to those failure modes. We present QED, an open-source multi-agent proof system in which each architectural decision directly addresses a specific failure mode. Evaluated on five open problems in applied analysis and PDEs contributed by domain experts, QED produces correct proofs for three problems, each verified by the contributing experts as original and nontrivial. QED is released as open-source software at this https URL.

---


### 288. [ServImage: An Image Generation and Editing Benchmark from Real-world Commercial Imaging Services](https://arxiv.org/abs/2604.24023)

**<font color=#1a73e8>作者：</font>** Fengxian Ji, Jingpu Yang, Zirui Song 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent image generation and editing models demonstrate robust adherence to instructions and high visual quality on academic benchmarks. However, their performance on paid, real-world design projects remains uncertain. We introduce \textbf{ServImage}, a benchmark that explicitly correlates model outputs with economic value in commercial design projects. ServImage consists of (i) \textbf{\textit{ServImageBench}}: a dataset of 1.07k paid commercial design tasks and 2.05k designer deliverables totaling over \$295k, covering portrait, product, and digital content, along with 33k candidate images and 33k human annotations. (ii) \textbf{\textit{ServImageScore}}: an integrated scoring system that combines three quality dimensions: baseline requirements fulfilment, visual execution quality, and commercial necessity satisfaction. These three dimensions are designed to characterize the factors that drive human payment decisions and indicate whether an image is commercially acceptable. (iii) \textbf{\textit{ServImageModel}}: under this scoring system, we propose a payment prediction model trained on the human-annotated candidate images, achieving 82.00\% accuracy in predicting human payment decisions and producing calibrated payment probabilities. ServImage provides a comprehensive foundation for assessing the commercial viability of image generation models and offers a scalable resource for future research on economically grounded vision systems \href{this https URL}{Github.}

---


### 289. [Breaking the Scalability Limit of Multi-Projector Calibration with Embedded Cameras](https://arxiv.org/abs/2604.24024)

**<font color=#1a73e8>作者：</font>** Takumi Kawano, Kohei Miura, Daisuke Iwai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conventional multi-projector calibration requires projecting and capturing structured light patterns for each projector sequentially, causing calibration time and effort to increase linearly with the number of projectors. This scalability bottleneck has long limited the deployment of large-scale projection mapping systems. We present a new calibration framework that breaks this limitation by embedding cameras into the surface of the calibration target. The embedded cameras directly capture the incoming projection light, enabling the separation of simultaneously projected structured light patterns from multiple projectors according to their incident directions. Our method establishes correspondences between the optical centers of the embedded cameras and the projector pixels, allowing the intrinsic and extrinsic parameters of all projectors to be simultaneously estimated. We further introduce a correction technique for small misalignments between the calibration board and camera optical centers. As a result, our system achieves calibration accuracy comparable to conventional methods while reducing the required number of projection-capture cycles from linear to nearly constant with respect to the number of projectors, dramatically improving scalability for dense multi-projector systems with overlapping projection regions, such as high-brightness stacking, super-resolution, light-field, and shadow-suppression displays.

---


### 290. [From Skill Text to Skill Structure: The Scheduling-Structural-Logical Representation for Agent Skills](https://arxiv.org/abs/2604.24026)

**<font color=#1a73e8>作者：</font>** Qiliang Liang, Hansi Wang, Zhong Liang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly rely on reusable skills, capability packages that combine instructions, control flow, constraints, and tool calls. In most current agent systems, however, skills are still represented by text-heavy artifacts, including this http URL-style documents and structured records whose machine-usable evidence remains embedded largely in natural-language descriptions. This poses a challenge for skill-centered agent systems: managing skill collections and using skills to support agent both require reasoning over invocation interfaces, execution structure, and concrete side effects that are often entangled in a single textual surface. An explicit representation of skill knowledge may therefore help make these artifacts easier for machines to acquire and leverage. Drawing on Memory Organization Packets, Script Theory, and Conceptual Dependency from Schank and Abelson's classical work on linguistic knowledge representation, we introduce what is, to our knowledge, the first structured representation for agent skill artifacts that disentangles skill-level scheduling signals, scene-level execution structure, and logic-level action and resource-use evidence: the Scheduling-Structural-Logical (SSL) representation. We instantiate SSL with an LLM-based normalizer and evaluate it on a corpus of skills in two tasks, Skill Discovery and Risk Assessment, and superiorly outperform the text-only baselines: in Skill Discovery, SSL improves MRR from 0.573 to 0.707; in Risk Assessment, it improves macro F1 from 0.744 to 0.787. These findings reveal that explicit, source-grounded structure makes agent skills easier to search and review. They also suggest that SSL is best understood as a practical step toward more inspectable, reusable, and operationally actionable skill representations for agent systems, rather than as a finished standard or an end-to-end mechanism for managing and using skills.

---


### 291. [JSSFF: A Joint Structural-Semantic Fusion Framework for Remote Sensing Image Captioning](https://arxiv.org/abs/2604.24031)

**<font color=#1a73e8>作者：</font>** Swadhin Das, Vivek Yadav  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The encoder-decoder framework has become widely popular nowadays. In this model, the encoder extracts informative visual features from an input image, and the decoder employs a sequence-to-sequence formulation to generate the corresponding textual description from these features. The existing models focus more on the decision part. However, extracting meaningful information from the image can help the decoder generate an accurate caption by providing information about the objects and their relationship. Remote sensing images are highly complex. One major challenge is detecting objects that extend beyond their visible boundaries due to occlusion, overlapping structures, and unclear edges. Hence, there is a need to design an approach that can effectively capture both high-level semantics and low-level spatial details for accurate caption generation. In this work, we have proposed an edge-aware fusion method by incorporating the original image and its edge-aware version into the encoder to enhance feature representation and boundary awareness. We used a comparison-based beam search (CBBS) to generate captions to achieve a balanced trade-off between quantitative metrics and qualitative caption relevance through fairness-based comparison of candidate captions. Experimental results demonstrate our model's superiority over several baseline models in quantitative and qualitative perspectives.

---


### 292. [AgentPulse: A Continuous Multi-Signal Framework for Evaluating AI Agents in Deployment](https://arxiv.org/abs/2604.24038)

**<font color=#1a73e8>作者：</font>** Yuxuan Gao, Megan Wang, Yi Ling Yu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Static benchmarks measure what AI agents can do at a fixed point in time but not how they are adopted, maintained, or experienced in deployment. We introduce AgentPulse, a continuous evaluation framework scoring 50 agents across 10 workload categories along four factors (Benchmark Performance, Adoption Signals, Community Sentiment, and Ecosystem Health) aggregated from 18 real-time signals across GitHub, package registries, IDE marketplaces, social platforms, and benchmark leaderboards. Three analyses ground the framework. The four factors capture largely complementary information (n=50; $\rho_{\max}=0.61$ for Adoption-Ecosystem, all others $|\rho| \leq 0.37$). A circularity-controlled test (n=35) shows the Benchmark+Sentiment sub-composite, which contains no GitHub-derived signals, predicts external adoption proxies it does not aggregate: GitHub stars ($\rho_s=0.52$, $p<0.01$) and Stack Overflow question volume ($\rho_s=0.49$, $p<0.01$), with VS Code installs ($\rho_s=0.44$, $p<0.05$) reported as illustrative given that only 11 of 35 agents have non-zero installs. On the n=11 subset with published SWE-bench scores, composite and benchmark-only rankings are nearly uncorrelated ($\rho_s=0.25$; 9 of 11 agents shift by at least 2 ranks), driven by a strong negative Adoption-Capability correlation among closed-source high-capability agents within this subset. This is precisely why we rest the framework's validity claim on the broader n=35 test rather than the SWE-bench overlap. AgentPulse surfaces deployment signal absent from benchmarks; it is a methodology, not a ground-truth ranking. The framework, all collected signals, scoring outputs, and evaluation harness are released under CC BY 4.0.

---


### 293. [Improving Robustness of Tabular Retrieval via Representational Stability](https://arxiv.org/abs/2604.24040)

**<font color=#1a73e8>作者：</font>** Kushal Raj Bhandari, Adarsh Singh, Jianxi Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transformer-based table retrieval systems flatten structured tables into token sequences, making retrieval sensitive to the choice of serialization even when table semantics remain unchanged. We show that semantically equivalent serializations, such as $\texttt{csv}$, $\texttt{tsv}$, $\texttt{html}$, $\texttt{markdown}$, and $\texttt{ddl}$, can produce substantially different embeddings and retrieval results across multiple benchmarks and retriever families. To address this instability, we treat serialization embedding as noisy views of a shared semantic signal and use its centroid as a canonical target representation. We show that centroid averaging suppresses format-specific variation and can recover the semantic content common to different serializations when format-induced shifts differ across tables. Empirically, centroid representations outrank individual formats in aggregate pairwise comparisons across $\texttt{MPNet}$, $\texttt{BGE-M3}$, $\texttt{ReasonIR}$, and $\texttt{SPLADE}$. We further introduce a lightweight residual bottleneck adapter on top of a frozen encoder that maps single-serialization embeddings towards centroid targets while preserving variance and enforcing covariance regularization. The adapter improves robustness for several dense retrievers, though gains are model-dependent and weaker for sparse lexical retrieval. These results identify serialization sensitivity as a major source of retrieval variance and show the promise of post hoc geometric correction for serialization-invariant table retrieval. Our code, datasets, and models are available at $\href{this https URL}{this https URL}$.

---


### 294. [End-to-End Learning for Partially-Observed Time Series with PyPOTS](https://arxiv.org/abs/2604.24041)

**<font color=#1a73e8>作者：</font>** Wenjie Du, Yiyuan Yang, Tianxiang Zhan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Partially-observed time series (POTS) is ubiquitous in real-world applications, yet most existing toolchains separate missing-value handling from downstream learning, which limits reproducibility and overall performance. This tutorial introduces PyPOTS, an open-source Python ecosystem for end-to-end data mining and machine learning on POTS. We present practical workflows spanning missingness simulation, data preprocessing, model training, and evaluation across core tasks, including imputation, forecasting, classification, clustering, and anomaly detection. The tutorial consists of two parts: Part I emphasizes hands-on application for practitioners through unified APIs and benchmark-oriented experiments. Part II targets developers and researchers, focusing on extending PyPOTS with custom models, domain-specific constraints, and contribution-ready engineering practices. Participants will gain both conceptual understanding and implementation experience for building robust, transparent, and reusable POTS pipelines in research and production settings. PyPOTS is publicly available at this https URL

---


### 295. [CLLAP: Contrastive Learning-based LiDAR-Augmented Pretraining for Enhanced Radar-Camera Fusion](https://arxiv.org/abs/2604.24044)

**<font color=#1a73e8>作者：</font>** Bingyi Liu, Chuanhui Zhu, Hongfei Xue 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate 3D object detection is critical for autonomous driving, necessitating reliable, cost-effective sensors capable of operating in adverse weather conditions. Camera and millimeter-wave radar fusion has emerged as a promising solution; however, these methods often rely on finely annotated radar data, which is scarce and labor-intensive to produce. To address this challenge, we present CLLAP, a Contrastive Learning-based LiDAR-Augmented Pretraining framework that enhances the performance of existing radar-camera fusion methods for 3D object detection. CLLAP leverages abundant LiDAR data to generate pseudo-radar data using the proposed L2R (LiDAR-to-Radar) Sampling method. Then, it incorporates this data into a novel dual-stage, dual-modality contrastive learning strategy, enabling effective self-supervised learning from paired pseudo-radar and image data. This approach facilitates effective pretraining of existing radar-camera fusion models in a plug-and-play manner, enhancing their feature extraction capabilities and improving detection accuracy and robustness. Experimental results using NuScenes and Lyft Level 5 datasets demonstrate significant performance improvements across three baseline models, highlighting CLLAP's effectiveness in advancing radar-camera fusion for autonomous driving applications.

---


### 296. [Generalising maximum mean discrepancy: kernelised functional Bregman divergences](https://arxiv.org/abs/2604.24047)

**<font color=#1a73e8>作者：</font>** Russell Tsuchida, Frank Nielsen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bregman divergences play a pivotal role in statistics, machine learning and computational information geometry. Particularly in the context of machine learning, they are central to clustering, exponential families, parameter estimation and optimisation, among other things. Despite this, the full toolkit of Hilbert spaces and in particular reproducing kernel Hilbert spaces have not been systematically developed and applied to functional Bregman divergences, where points are functions rather than finite-dimensional parameter vectors. While other types of functional Bregman divergences have been studied, these are typically in a Banach space rather than more directly aligned with kernel methods and Hilbert-space geometry commonly used in machine learning. We consider functional Bregman divergences on a Hilbert space, where the self-dual pairing and Riesz representer afford us particularly convenient calculus. Further specialising Bregman generators as a composition involving a kernel mean embedding makes such divergences easy to estimate. We discuss applications in clustering, universal estimation, robust estimation and generative modelling, and contrast our approach with other types of Bregman divergences.

---


### 297. [System-aware contextual digital twin for ICS anomaly diagnosis](https://arxiv.org/abs/2604.24051)

**<font color=#1a73e8>作者：</font>** Eungyu Woo, Yooshin Kim, Wonje Heo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Industrial Control Systems (ICS) integrate computing, physical processes, and communication to operate critical infrastructures such as power grids, water treatment plants, and oil and gas facilities. As ICS become increasingly targeted by cyberattacks, timely and reliable anomaly diagnosis is essential for protecting operational safety. However, existing ICS anomaly detection approaches face practical limitations: supervised methods require extensive labeled attack data and suffer from class imbalance, while model-based detectors often lack the ability to provide deep insight into the root causes of anomalies, leading to elevated false alarms and making it difficult for operators to initiate a timely response. In this work, we propose a system-aware unsupervised framework for ICS anomaly diagnosis that combines lightweight online detection with contextual explanation. The system identifies deviations from observed normal behaviors without prior knowledge of system topology. To support actionable response, we further concatenate a contextual digital twin augmented with an Large Language Model (LLM) to enhance interpretability, which translates detection evidence into grounded diagnostic hypotheses and verification steps for operators. Experiments on public ICS benchmarks demonstrate that the proposed framework achieves real-time detection efficiency and provides consistent, interpretable anomaly diagnoses, enabling low-latency warning and practical deployment in complex industrial environments.

---


### 298. [Light 'em Up: Enabling Few-Shot Low-Light 3D Gaussian Splatting with Multi-Scale Explicit Retinex Illumination Decoupling](https://arxiv.org/abs/2604.24053)

**<font color=#1a73e8>作者：</font>** YuHao Yin, Zongji Wang, Yuanben Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Full 360$^\circ$ novel view synthesis under low-light conditions remains challenging. Insufficient illumination, noise amplification, and view-dependent photometric inconsistencies prevent existing methods from jointly preserving geometric consistency and photorealism. Unsupervised approaches often exhibit color drift under large viewpoint variations, while supervised low-light enhancement models, though effective for 2D tasks, struggle to generalize to new scenes and typically require retraining. To address this issue, we propose MERID-GS, a Multi-Scale Explicit Retinex Illumination-Decoupled Gaussian framework for low-light 360$^\circ$ synthesis. Based on Retinex theory, the method explicitly separates illumination and reflectance, and suppresses noise propagation while enhancing dark-region structures via a learnable gain and Illumination-State-Guided Frequency Gating. Combined with lightweight Reflection Head and 3D Gaussian Splatting, MERID-GS adapts to new scenes with only a few shots and enables stable low-light novel view synthesis from sparse-view observations. In addition, we construct a low-light multi-view dataset covering full 360$^\circ$ scenes for joint evaluation. Thorough experiments across multiple datasets in this area demonstrate that MERID-GS achieves SOTA performance, exhibiting superior cross-scene generalization and view consistency. The source code and pre-trained models are available at this https URL..

---


### 299. [Listen to the Voices of Everyday Users: Democratizing Privacy Ratings for Sensitive Data Access in Mobile Apps](https://arxiv.org/abs/2604.24066)

**<font color=#1a73e8>作者：</font>** Liu Wang, Tianshu Zhou, Haoyu Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mobile apps frequently request excessive data access, raising significant privacy concerns. While regulations like GDPR emphasize data minimization, they provide limited guidance on concretely defining and enforcing necessary data access. Existing regulatory mechanisms primarily rely on expert-driven audits that face challenges in scalability, neutrality, and alignment with user expectations. In this paper, we propose a novel paradigm--democratizing privacy assessment, inspired by prior work on user-centric privacy perceptions--which repositions users as active evaluators in the privacy auditing process, recognizing that user perceptions of data usage play a crucial role in assessing the appropriateness and necessity of data access. To operationalize this paradigm, we introduce DePRa, a prototype system developed through participatory design, featuring contextual explanation provision, category-based representative selection, an intuitive rating interface, and preference-based rating adjustment. We evaluated DePRa with 200 everyday mobile app users, analyzing how effectively it captures user opinions on sensitive data access, comparing their privacy ratings with expert assessments, and exploring risk preference-based score calibration. Our findings show the feasibility and promise of democratized privacy assessment, highlighting its potential to complement expert auditing and support inclusive privacy evaluation.

---


### 300. [Distilling Self-Consistency into Verbal Confidence: A Pre-Registered Negative Result and Post-Hoc Rescue on Gemma 3 4B](https://arxiv.org/abs/2604.24070)

**<font color=#1a73e8>作者：</font>** Jon-Paul Cacioli  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Small instruct-tuned LLMs produce degenerate verbal confidence under minimal elicitation: ceiling rates above 95%, near-chance Type-2 AUROC, and Invalid validity profiles. We test whether confidence-conditioned supervised fine-tuning (CSFT) with self-consistency-derived targets can close the gap between internal information and verbal readout. A pre-registered Phase 0 protocol on Gemma 3 4B-it with a modal filter restricting training to items with correct modal answers produced a negative result: AUROC2 dropped from 0.554 to 0.509 due to label-entropy collapse in the training targets. An exploratory rescue removed the filter, training on all 2,000 calibration items. This produced a binary verbal correctness discriminator with AUROC2 = 0.774 on held-out TriviaQA, compressing a 10-sample self-consistency signal (AUROC2 = 0.999) into a single-pass readout exceeding logit entropy (0.701). The shuffled-target control showed no improvement (0.501). On MMLU, accuracy improved from 54.2% to 77.4% with the shuffled model at baseline (56.1%), supporting a target-dependent interpretation. The result is exploratory, binary rather than continuously calibrated, and observed at a single scale. It identifies two design lessons: confidence training requires label entropy, and correct targets regularise output format.

---


> [!TIP]
> 当前位于：**251-300**（第 6/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-437](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
