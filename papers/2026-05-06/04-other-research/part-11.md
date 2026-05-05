# 📦 其他研究 | 2026年05月06日

> 本类共 **511** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**501-511**（第 11/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-511**

---

### 501. ["I Don't Have Faith in the Developers to Use My Feedback": Understanding Player Values and Expectancy for Reporting Systems in Video Games](https://arxiv.org/abs/2605.02842)

**<font color=#1a73e8>作者：</font>** Michael Yin, Chenxinran, Shen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Reporting systems in multiplayer video games allow players to express their dissatisfaction with others and combat in-game toxicity. In this work, we examined the act of reporting through the lens of expectancy-value theory. Using a distributed survey (n = 98) and follow-up interviews (n = 19), we explored the value players place on reporting, their desired outcomes, and their expectations that these outcomes will be achieved. Our findings revealed that reporting is motivated by both altruistic and retributive factors, with players seeking short-term revenge while also looking to foster an improved long-term community. Yet, players felt that reporting may not always meet these goals, with belief in the system being mediated by factors such as developer reputation, reporting transparency, and alignment with the community. By understanding the value and expectancy of reporting systems, we discuss their implications on broader digital moderation and consider current and potential future designs of reporting systems.

---


### 502. [Active Sampling for Ultra-Low-Bit-Rate Video Compression via Conditional Controlled Diffusion](https://arxiv.org/abs/2605.02849)

**<font color=#1a73e8>作者：</font>** Amirhosein Javadi, Shirin Saeedi Bidokhti, Tara Javidi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models provide a powerful generative prior for perceptual reconstruction at ultra-low bitrates, but effective video compression requires controlling the generative process using highly compact conditioning signals. In this work, we present ActDiff-VC, a diffusion-based video compression framework for the ultra-low-bitrate regime. Our method partitions videos into variable-length segments, transmits keyframes only when needed, and summarizes temporal dynamics using a compact set of tracked point trajectories. Conditioned on these sparse signals, a conditional diffusion decoder synthesizes the remaining frames, enabling perceptually realistic reconstruction under severe rate constraints. To support this design, we introduce two mechanisms: content-adaptive keyframe selection and budget-aware sparse trajectory selection, which together enable compact yet effective conditioning for generative reconstruction. Experiments on the UVG and MCL-JCV benchmarks show that ActDiff-VC achieves up to 64.6\% bitrate reduction at matched NIQE, improves KID by up to 64.6\% and FID by up to 37.7\% at comparable bitrates against strong learned codecs, and delivers favorable perceptual rate--distortion trade-offs relative to learned and diffusion-based baselines in the ultra-low-bitrate regime.

---


### 503. [Trust, but Verify: Peeling Low-Bit Transformer Networks for Training Monitoring](https://arxiv.org/abs/2605.02853)

**<font color=#1a73e8>作者：</font>** Arian Eamaz, Farhang Yeganegi, Mojtaba Soltanalian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding whether deep neural networks are effectively optimized remains challenging, as training occurs in highly nonconvex landscapes and standard metrics provide limited visibility into layer-wise learning quality. This challenge is particularly acute for transformer-based language models, where training is expensive, models are often reused in frozen form, and poorly optimized layers can silently degrade performance. We propose a layer-wise peeling framework for monitoring training dynamics, in which each transformer layer is locally optimized against intermediate representations of the trained model. By constructing lightweight, layer-specific reference solutions and projecting layers onto multiple intermediate outputs via different permutations, we obtain achievable baselines that enable fine-grained diagnosis of under-optimized layers. Experiments on decoder-only transformer models show that these layer-wise reference bounds can match or even surpass the trained model at various stages of training, exposing inefficiencies that remain hidden in aggregate loss curves. We further demonstrate that this analysis remains effective under binarization and quantized settings, where training dynamics are particularly fragile. Across all numerical results, the proposed bounds consistently separate apparent convergence from effective optimality, highlighting optimization opportunities that are invisible when relying on training loss alone.

---


### 504. [The 1-Bit Barrier is Universal: k-Stage Pipeline Composition and Unified Leakage Bounds for Standard Modular Reductions in PQC Hardware](https://arxiv.org/abs/2605.02856)

**<font color=#1a73e8>作者：</font>** Ray Iskander, Khaled Kirah  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This is Paper 7 of a series of formally-verified analyses of masked NTT hardware for post-quantum cryptography; Paper 1 [1] established structural dependency analysis of the QANARY platform, and Paper 2 [2] quantified security margins under partial NTT masking. Arbitrary-depth $k$-stage masked NTT pipelines with fresh inter-stage masking and per-stage PF-PINI($\leq 2$) gadgets satisfy a per-observation cardinality bound of $2 \cdot q^{2k-2}$ on the preimage of any output value, machine-checked in Lean 4 with zero \texttt{sorry}. Under the standard (informal) semantic translation that divides this cardinality by the total mask-tuple space size $q^{2k-1}$, the per-observation conditional probability bound is $2/q$, independent of pipeline depth $k$. The QANARY program has previously established machine-checked cardinality bounds on the per-observation leakage of masked NTT hardware: PF-PINI(2) for Barrett reduction (Paper 5 [3]), 2-stage composition with fresh inter-stage masking (Paper 6 [4]), an underlying universality theorem (Paper 3 [5]), and PF-PINI(1) for butterfly wires (Paper 4 [6]). This paper closes the program with four contributions. First, a $k$-stage composition theorem generalizing Paper 6's two-stage result to arbitrary $k \geq 1$ gives the last-stage-determined bound $G_{k-1}.\texttt{maxMult} \cdot q^{2k-2}$: only the last stage's PF-PINI parameter survives, with intermediate parameters erased by fresh inter-stage masking. Second, Montgomery reduction satisfies PF-PINI(2) with tight max-multiplicity 2. Third, we assemble these into the end-to-end bound $2 \cdot q^{2k-2}$ for any depth-$k$ PF-PINI($\leq 2$) pipeline under fresh inter-stage masking. Fourth, a Lean-verified hypothesis-violation conditional anchors the prior empirical and structural Adams Bridge analyses ([1, 2, 7, 8]).

---


### 505. [Pixel Perfect: Relational Image Quality Assessment with Spatially-Aware Distortions](https://arxiv.org/abs/2605.02863)

**<font color=#1a73e8>作者：</font>** Fadeel Sher Khan, Long N. Le, Abhinau K. Venkataramanan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traditional image quality assessment (IQA) methods rely on mean opinion scores (MOS), which are resource-intensive to collect and fail to provide interpretable, localized feedback on specific image distortions. We overcome these limitations by shifting from absolute quality prediction to a relational and directional assessment. Our approach utilizes a self-supervised synthetic distortion engine to generate training data, eliminating the need for manual annotation. A distortion prediction network is trained with an anti-symmetric objective to produce spatially-aware, disentangled maps that identify the type, intensity, and direction of distortions relative to a reference image. Subsequently, a scoring network is trained via contrastive learning on ordinally ranked image sets to predict a relational quality score. Our method provides a more granular and interpretable approach to IQA for the targeted optimization of image processing algorithms without requiring any human-labeled quality scores.

---


### 506. [Laplacian Frequency Interaction Network for Rural Thematic Road Extraction](https://arxiv.org/abs/2605.02866)

**<font color=#1a73e8>作者：</font>** Baiyan Chen, Weixin Zhai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rural thematic road network construction aims to extract topological road structures from movement trajectory images of agricultural machinery. However, this task faces challenges where downsampling methods commonly used in existing studies tend to blur the sparse high-frequency road structures, and the heavy noise from dense field operations often leads to fragmented or redundant topologies in the extracted networks. To address these challenges, we propose LFINet, a Laplacian Frequency Interaction Network. The network begins with a Laplacian Multi-scale Separator (LMS) to decouple the image into low-frequency semantic contexts and high-frequency structural details. These components are then processed by the Cross-Frequency Interaction Block (CFIB) through a dual-pathway architecture in which a High-Frequency Block (HFB) refines local structures while a Spatial Transformer (ST) captures global semantics. Subsequently, a Frequency Gated Modulation (FGM) mechanism integrates the features from pathways by leveraging semantic contexts to calibrate the structural details. Finally, a Progressive Reconstruction Decoder iteratively fuses multi-scale features to ensure topological consistency. Experiments conducted on a real-world agricultural trajectories dataset from Henan Province, China, show that LFINet establishes a new state-of-the-art. Specifically, it achieves an F1-score of 92.54% and an IoU of 86.12%, surpassing the second-ranked method by 0.64% and 1.1%, respectively. This confirms its capability to effectively construct topological road networks from noisy and sparse field data.

---


### 507. [Enhancing RL Generalizability in Robotics through SHAP Analysis of Algorithms and Hyperparameters](https://arxiv.org/abs/2605.02867)

**<font color=#1a73e8>作者：</font>** Lingxiao Kong, Cong Yang, Oya Deniz Beyan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite significant advances in Reinforcement Learning (RL), model performance remains highly sensitive to algorithm and hyperparameter configurations, while generalization gaps across environments complicate real-world deployment. Although prior work has studied RL generalization, the relative contribution of specific configurations to the generalization gap has not been quantitatively decomposed and systematically leveraged for configuration selection. To address this limitation, we propose an explainable framework that evaluates RL performance across robotic environments using SHapley Additive exPlanations (SHAP) to quantify configuration impacts. We establish a theoretical foundation connecting Shapley values to generalizability, empirically analyze configuration impact patterns, and introduce SHAP-guided configuration selection to enhance generalization. Our results reveal distinct patterns across algorithms and hyperparameters, with consistent configuration impacts across diverse tasks and environments. By applying these insights to configuration selection, we achieve improved RL generalizability and provide actionable guidance for practitioners.

---


### 508. [EvoPoC: Automated Exploit Synthesis for DeFi Smart Contracts via Hierarchical Knowledge Graphs](https://arxiv.org/abs/2605.02868)

**<font color=#1a73e8>作者：</font>** Ruichao Liang, Jing Chen, Xianglong Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Smart contract vulnerabilities in Decentralized Finance caused over billions of dollars losses every year, yet the security community faces a critical bottleneck: identifying a vulnerability is not the same as proving it is exploitable. Manual PoC construction is prohibitively labor-intensive, leaving most disclosed vulnerabilities unverified and protocols exposed long before mitigation is applied. In this paper, we propose \sys, a knowledge-driven agentic system for end-to-end contract vulnerability detection and exploit synthesis. Our core insight is that exploit synthesis is not a code generation task but a \emph{structured reasoning problem} that requires grounded knowledge of protocol semantics, failure root cause, and exploit primitives. \sys organizes this knowledge into a \emph{Hierarchical Knowledge Graph} (HKG) that serves as structured memory for LLM-guided multi-hop reasoning. To validate exploit feasibility beyond code synthesis, \sys employs a two-stage validation framework that checks exploit-path reachability via SMT solving and profit realizability via asset-level state simulation, ensuring generated PoCs satisfy both logical and economic viability constraints. Evaluated on 88 real-world DeFi attacks and 72 audited projects (2,573 contracts), \sys achieves 98\% recall and 0.9 F1-score in detection, and a 96.6\% exploit success rate (ESR), reproducing 85 historical exploits and recovering over \$116.2M revenue. \sys outperforms SOTA fuzzers (\textsc{Verite}, \textsc{ItyFuzz}) by up to $5\times$ in ESR and $300\times$ in recoverable value, and the LLM-based exploit generator \textsc{A1} by $2\times$ and $8.5\times$ respectively. In bug bounty evaluation, \sys identified 16 confirmed 0-day vulnerabilities, helping secure over \$70.6M and earning \$2,900 in bounties.

---


### 509. [Unsupervised Machine Learning for Detecting Structural Anomalies in European Regional Statistics](https://arxiv.org/abs/2605.02884)

**<font color=#1a73e8>作者：</font>** Bogdan Oancea  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ensuring the coherence of regional socio-economic statistics is a central task for national statistical institutes. Traditional validation tools, such as range edits, ratio checks, or univariate outlier detection, are effective for identifying extreme values in individual series but are less suited for detecting unusual combinations of indicators in high-dimensional settings. This paper proposes an unsupervised machine learning framework for identifying structurally atypical regional profiles within Europe using publicly available Eurostat data. We construct a cross-sectional dataset of NUTS2 regions (2022) covering four key indicators: GDP per capita in PPS, unemployment rate, tertiary educational attainment, and population density. We apply and compare five anomaly detection techniques, univariate z-scores, Mahalanobis distance, Isolation Forest, Local Outlier Factor, and One-Class SVM, and classify a region as a structural anomaly if it is flagged by at least three of the five methods. The findings show that machine learning methods identify a consistent set of regions whose multivariate profiles diverge substantially from the EU-wide pattern. These include both highly developed metropolitan economies (Brussels, Vienna, Berlin, Prague) and regions with persistent socio-economic disadvantages (Central and Western Slovakia, Northern Hungary, Castilla-La Mancha, Extremadura), as well as Istanbul, whose profile differs markedly from EU capital regions. Importantly, these anomalies do not necessarily signal data quality issues; rather, they reflect meaningful structural divergence that warrants analytical or policy attention. The proposed framework is fully reproducible, scalable, and compatible with existing validation workflows, offering a flexible tool for early detection of unusual regional configurations within the European Statistical System.

---


### 510. [SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection](https://arxiv.org/abs/2605.02888)

**<font color=#1a73e8>作者：</font>** Shikhar Shukla  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates large language model (LLM) inference by using a small draft model to propose candidate tokens that a larger target model verifies. A critical hyperparameter in this process is the speculation length~$\gamma$, which determines how many tokens the draft model proposes per step. Nearly all existing systems use a fixed~$\gamma$ (typically~4), yet empirical evidence suggests that the optimal value varies across task types and, crucially, depends on the compression level applied to the target model. In this paper, we present \textbf{SpecKV}, a lightweight adaptive controller that selects~$\gamma$ per speculation step using signals extracted from the draft model itself. We profile speculative decoding across 4~task categories, 4~speculation lengths, and 3~compression levels (FP16, INT8, NF4), collecting 5,112 step-level records with per-step acceptance rates, draft entropy, and draft confidence. We demonstrate that the optimal~$\gamma$ shifts across compression regimes and that draft model confidence and entropy are strong predictors of acceptance rate (correlation~$\approx 0.56$). SpecKV uses a small MLP trained on these signals to maximize expected tokens per speculation step, achieving a 56.0\% improvement over the fixed-$\gamma$=4 baseline with only 0.34\,ms overhead per decision ($<$0.5\% of step time). The improvement is statistically significant ($p < 0.001$, paired bootstrap test). We release all profiling data, trained models, and notebooks as open-source artifacts.

---


### 511. [AlbumFill: Album-Guided Reasoning and Retrieval for Personalized Image Completion](https://arxiv.org/abs/2605.02892)

**<font color=#1a73e8>作者：</font>** Yu-Ju Tsai, Brian Price, Qing Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Personalized image completion aims to restore occluded regions in personal photos while preserving identity and appearance. Existing methods either rely on generic inpainting models that often fail to maintain identity consistency, or assume that suitable reference images are explicitly provided. In practice, suitable references are often not explicitly provided, requiring the system to search for identity-consistent images within personal photo collections. We present AlbumFill, a training-free framework that retrieves identity-consistent references from personal albums for personalized completion. Given an occluded image and a personal album, a vision-language model infers missing semantic cues to guide composed image retrieval, and the retrieved references are used by reference-based completion models. To facilitate this task, we introduce a dataset containing 54K human-centric samples with associated album images. Experiments across multiple baselines demonstrate the difficulty of personalized completion and highlight the importance of identity-consistent reference retrieval. Project Page: this https URL

---


> [!TIP]
> 当前位于：**501-511**（第 11/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-511**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
