# 📦 其他研究 | 2026年05月18日

> 本类共 **337** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-337](./part-07.md)

---

### 51. [A Systematic Evaluation of Imbalance Handling Methods in Biomedical Binary Classification](https://arxiv.org/abs/2605.14147)

**<font color=#1a73e8>作者：</font>** Jiandong Chen, Lingjie Su, Le Peng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Objective: The primary goal of this study was to systematically examine the impact of commonly used imbalance handling methods (IHMs) on predictive performance in biomedical binary classification, considering the interplay between model complexity and diverse data modalities.
Material and Methods: We evaluated five representative IHMs: random undersampling (RUS), random oversampling (ROS), SMOTE, re-weighting (RW), and direct F1-score optimization (DMO), against a raw training (RAW) baseline. The evaluation encompassed three public biomedical datasets: MIMIC-III (tabular), ADE-Corpus-V2 (text), and MURA (image), spanning three common biomedical data modalities. To assess varying model complexity, we employed a range of architectures, from classical logistic regression and random forest to deep neural networks, including multilayer perceptron (MLP), BiLSTM, BERT, DenseNet, and DINOv2.
Results: For simpler models such as logistic regression on tabular data, IHMs yielded no significant advantage over the RAW baseline, aligning with prior findings. However, clear benefits were observed for more complex models and unstructured data: (a) ROS and RW consistently enhanced the performance of powerful models; (b) direct F1-score optimization demonstrated utility primarily for unstructured text and image data; and (c) RUS and SMOTE consistently degraded performance and are therefore not recommended.
Conclusion: The effectiveness of IHMs depends on both model complexity and data modality. Performance gains are most pronounced when leveraging appropriate IHMs, such as ROS, RW, and DMO, on high-complexity models.

---


### 52. [ROK-FORTRESS: Measuring the Effect of Geopolitical Transcreation for National Security and Public Safety](https://arxiv.org/abs/2605.14152)

**<font color=#1a73e8>作者：</font>** Michael S. Lee, Yash Maurya, Drew Rein 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Safety evaluations for large language models (LLMs) increasingly target high-stakes National Security and Public Safety (NSPS) risks, yet multilingual safety is typically assessed through translation-only benchmarks that preserve the underlying scenario, and empirical evidence of how language and geopolitical context interact remains limited to a narrow set of language pairs. We introduce \emph{ROK-FORTRESS} this https URL, a bilingual, culturally adversarial NSPS benchmark that uses the English--Korean language pair and U.S.--ROK geopolitical axis as a case study, separating the effects of language and geopolitical grounding via a \emph{transcreation matrix}: adversarial intents are evaluated under controlled combinations of (i) English versus Korean language and (ii) U.S.\ versus Korean entities, institutions, and operational details. Each adversarial prompt is paired with a dual-use benign counterpart to quantify over-refusal. Model responses are then scored using calibrated LLM-as-a-judge panels, applying our expert-crafted, prompt-specific binary rubrics.
Across a dual-track set of frontier and Korean-optimized models, we find a consistent suppression effect in Korean variants and substantial model-to-model variation in how geopolitical grounding interacts with language. In many models, Korean grounding mitigates the Korean language-driven suppression -- with no model showing significant amplification in the other direction -- indicating that, at least in the English--Korean case, safety behavior is shaped by language-as-risk signals and context interactions that translation-only evaluations miss. The transcreation matrix methodology is designed to generalize to other language--culture pairs.

---


### 53. [Unsteady Metrics and Benchmarking Cultures of AI Model Builders](https://arxiv.org/abs/2605.14164)

**<font color=#1a73e8>作者：</font>** Stefan Baack, Christo Buschek, Maty Bohacek  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The primary way to establish and compare competencies in foundation and generative AI models has shifted from peer-reviewed literature to press releases and company blog posts, where model builders highlight results on selected benchmarks. These artifacts now largely define the state of the art for researchers and the public. Despite their prominence, which benchmarks model builders choose to highlight, and what they communicate through this selection, is underexamined. To investigate, we introduce and open-source Benchmarking-Cultures-25, a dataset of 231 benchmarks highlighted across 139 model releases in 2025 from 11 major AI builders, alongside an interactive tool to explore the data. Our analysis reveals a fragmented evaluation landscape with limited cross-model comparability: 63.2% of highlighted benchmarks are used by a single builder, and 38.5% appear in just one release. Few achieve widespread use (e.g., GPQA Diamond, LiveCodeBench, AIME 2025). Moreover, benchmarks are attributed different competencies by different builders, depending on their narrative. To disentangle these conflicting presentations, we develop a unified taxonomy mapping diverging terminology to a shared framework of measured signals based on what benchmark authors claim to measure. "General knowledge application" is the second most popular, yet vaguely defined, category. Qualitative analysis shows many such benchmarks deemphasize construct validity, instead framing results as indicators of progress toward AGI. Their authors claim to measure knowledge or reasoning broadly, yet mostly evaluate STEM subjects (especially math). We argue that highlighted benchmarks function less as standardized measurement tools and more as flexible narrative devices prioritizing market positioning over scientific evaluation. Data: this https URL tool: this https URL.

---


### 54. [DSTAN-Med: Dual-Channel Spatiotemporal Attention with Physiological Plausibility Filtering for False Data Injection Attack Detection in IoT-Based Medical Devices](https://arxiv.org/abs/2605.14165)

**<font color=#1a73e8>作者：</font>** Md Mehedi Hasan, Rafiqul Islam, Md Zakir Hossain  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> False data injection (FDI) attacks on Internet of Medical Things (IoMT) sensor streams falsify vital signs in transit, threatening patient safety and defeating clinical monitoring systems that lack cyber-physical anomaly detection capability. Existing deep learning detectors conflate inter-sensor spatial correlations with temporal dependencies in a shared latent space, preventing disentanglement of the distinct spatial and temporal signatures that FDI attacks imprint simultaneously; no current method exploits domain knowledge to constrain outputs against physiologically impossible attack patterns. We propose DSTAN-Med, a supervised framework comprising a Dual-channel Attention Mechanism (DAM) that routes multivariate sensor windows through independent sensor-wise (SWA) and time-wise (TWA) self-attention pathways operating on orthogonal tensor axes, a residual 1D-CNN block for local temporal feature extraction, and a zero-parameter Physiological Plausibility Filter (PPF) that suppresses attack signatures violating domain-knowledge bounds. Evaluated across three IoMT sensor datasets - PhysioNet/CinC 2012 (ICU vital signs), MIMIC-III Waveform (continuous ICU waveforms), and WESAD (wearable biosensor signals) - DSTAN-Med achieves mean sensitivity gains of 7.4-8.3 percentage points over the strongest Transformer baseline (TranAD), with improvements significant at p < 0.01 (McNemar's test, Holm-Bonferroni correction). The PPF contributes independent precision gains of 3.1-4.2 percentage points at negligible sensitivity cost across all three corpora. Ablation studies confirm that each component is individually necessary; removal of residual connections alone reduces sensitivity by 14.0 percentage points. The source code is publicly available at this https URL.

---


### 55. [You Only Landmark Once: Lightweight U-Net Face Super Resolution with YOLO-World Landmark Heatmaps](https://arxiv.org/abs/2605.14166)

**<font color=#1a73e8>作者：</font>** Riccardo Carraro, Anna Briotto, Endi Hysa 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face image super-resolution aims to recover high-resolution facial images from severely degraded inputs. Under extreme upscaling factors, fine facial details are often lost, making accurate reconstruction challenging. Existing methods typically rely on heavy network architectures, adversarial training schemes, or separate alignment networks, increasing model complexity and computational cost. To address these issues, we propose a lightweight U-Net based-architecture designed to reconstructs $128{ \times }128$ facial images from severely degraded $16{ \times }16$ inputs, achieving an $8 \times $ magnification. A key contribution is a novel auxiliary-training-free supervision strategy that leverages heatmaps generated by YOLO-World, an open-vocabulary object detector, to localize key facial features such as eyes, nose, and mouth. These heatmaps are converted into spatial weights to form a heatmap-guided loss that emphasizes reconstruction errors in semantically important regions. Unlike prior methods that require dedicated landmark or alignment networks, our approach directly reuses detector outputs as supervision, maintaining an efficient training and inference pipeline. Experiments on the aligned CelebA dataset demonstrate that the proposed loss consistently improves quantitative metrics and produces sharper, more realistic reconstructions. Overall, our results show that lightweight networks can effectively exploit detection-driven priors for perceptually convincing extreme upscaling, without adversarial training or increased computational cost.

---


### 56. [The Evaluation Trap: Benchmark Design as Theoretical Commitment](https://arxiv.org/abs/2605.14167)

**<font color=#1a73e8>作者：</font>** Theodore J Kalaitzidis  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Every AI benchmark operationalizes theoretical assumptions about the capability it claims to assess. When assumptions function as unexamined commitments, benchmarks stabilize the dominant paradigm by narrowing what counts as progress. Over time, narrow evaluation reorganizes capability concepts: architectures and definitions are selected for benchmark legibility until evaluation ceases to track an independent object and instead produces a version of the target defined by its own operational assumptions. The result is a trap: evaluation frameworks treat self-reinforcing assessments as valid, both creating and obscuring structural limits on what the current paradigm can accomplish. We introduce Epistematics, a methodology for deriving evaluation criteria directly from technical capability claims and auditing whether proposed benchmarks can discriminate the claimed capability from proxy behaviors. The contribution is meta-evaluative: an audit procedure, a failure mode taxonomy, and benchmark-design criteria for evaluating capability-evaluation coherence. We demonstrate the procedure through a worked audit of Dupoux et al. (2026), a proposal that revises the dominant paradigm's theoretical assumptions at the architectural level while reproducing them in its evaluation criteria, thereby entrenching the constraint it seeks to overcome in a form the evaluation cannot detect.

---


### 57. [Finite Sample Bounds for Learning with Score Matching](https://arxiv.org/abs/2605.14168)

**<font color=#1a73e8>作者：</font>** Devin Smedira, Abhijith Jayakumar, Sidhant Misra 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning of continuous exponential family distributions with unbounded support remains an important area of research for both theory and applications in high-dimensional statistics. In recent years, score matching has become a widely used method for learning exponential families with continuous variables due to its computational ease when compared against maximum likelihood estimation. However, theoretical understanding of the statistical properties of score matching is still lacking. In this work, we provide a non-asymptotic sample complexity analysis for learning the structure of exponential families of polynomials with score matching. The derived sample bounds show a polynomial dependence on the model dimension. These bounds are the first of its kind, as all prior work has shown only asymptotic bounds on the sample complexity.

---


### 58. [BOOKMARKS: Efficient Active Storyline Memory for Role-playing](https://arxiv.org/abs/2605.14169)

**<font color=#1a73e8>作者：</font>** Letian Peng, Ziche Liu, Yiming Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Memory systems are critical for role-playing agents (RPAs) to maintain long-horizon consistency. However, existing RPA memory methods (e.g., profiling) mainly rely on recurrent summarization, whose compression inevitably discards important details. To address this issue, we propose a search-based memory framework called BOOKMARKS, which actively initializes, maintains, and updates task-relevant pieces of bookmarks for the current task (e.g., character acting). A bookmark is structured as the answer to a question at a specific point in the storyline. For each current task, BOOKMARKS selects reusable existing bookmarks or initializes new ones (at storyline beginning) with useful questions. These bookmarks are then synchronized to the current story point, with their answers updated accordingly, so they can be efficiently reused in future grounding rounds. Compared with recurrent summarization, BOOKMARKS offers (1) active grounding for capturing task-specific details and (2) passive updating to avoid unnecessary computation. In implementation, BOOKMARKS supports concept, behavior, and state searches, each powered by an efficient synchronization method. BOOKMARKS significantly outperforms RPA memory baselines on 85 characters from 16 artifacts, demonstrating the effectiveness of search-based memory for RPAs.

---


### 59. [CSI-JEPA: Towards Foundation Representations for Ubiquitous Sensing with Minimal Supervision](https://arxiv.org/abs/2605.14171)

**<font color=#1a73e8>作者：</font>** Xuanhao Luo, Zhizhen Li, Yuchen Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Channel state information (CSI) provides a widely available sensing modality for human and environment perception, but existing CSI sensing models usually rely on task-specific supervised training and require substantial labeled data for each task, device, user, or environment. This limits their scalability in practical deployments where unlabeled CSI is abundant but labeled data is costly to collect. In this paper, we present CSI-JEPA, a self-supervised predictive representation learning framework for label-efficient, multi-task Wi-Fi sensing. CSI-JEPA learns reusable temporal-spectral representations from unlabeled CSI samples by predicting latent features of masked channel regions from visible context. To better match the physical structure of CSI, CSI-JEPA tokenizes channel-response amplitude windows along the time and subcarrier dimensions. It then introduces a channel variation-aware masking strategy that samples predictive targets from regions with stronger local temporal and subcarrier-domain variations. After pretraining, the encoder is frozen and used as a backbone, with lightweight task-specific adapters added for downstream sensing tasks. We evaluate CSI-JEPA on seven real-world Wi-Fi sensing tasks spanning diverse objectives and deployment settings. The results show that CSI-JEPA improves downstream sensing performance over competitive baselines, achieving up to 10.64 percentage points mean accuracy gain over state-of-the-art supervised Transformer and matched-budget label savings of up to 98.0%.

---


### 60. [CoReDiT: Spatial Coherence-Guided Token Pruning and Reconstruction for Efficient Diffusion Transformers](https://arxiv.org/abs/2605.14191)

**<font color=#1a73e8>作者：</font>** Zhuojin Li, Hsin-Pai Cheng, Hong Cai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformers (DiTs) deliver remarkable image and video generation quality but incur high computational cost, limiting scalability and on-device deployment. We introduce CoReDiT, a structured token pruning framework for DiTs across vision tasks. CoReDiT uses a linear-time spatial coherence score to estimate local redundancy in the latent token lattice and skips high coherence (redundant) tokens in self-attention. To maintain a dense representation and avoid visual discontinuities, we reconstruct skipped attention outputs via coherence-guided aggregation of spatially neighboring retained tokens. We further introduce a progressive, block-adaptive pruning schedule that increases pruning gradually and allocates larger budgets to blocks and denoising steps with higher redundancy. Across state-of-the-art diffusion backbones including PixArt-{\alpha} and MagicDrive-V2, CoReDiT achieves up to 55% self-attention FLOPs reduction and inference speedups of 1.33x on cloud GPUs and 1.72x on mobile NPUs, while maintaining high visual quality. Notably, CoReDiT also increases on-device memory head-room, enabling higher-resolution generation.

---


### 61. [How to Scale Mixture-of-Experts: From muP to the Maximally Scale-Stable Parameterization](https://arxiv.org/abs/2605.14200)

**<font color=#1a73e8>作者：</font>** Leena Chennuru Vankadara, Moritz Haas, Luke Hayward 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent frontier large language models predominantly rely on Mixture-of-Experts (MoE) architectures. Despite empirical progress, there is still no principled understanding of how hyperparameters should scale with network width $N$, expert width $N_e$, number of experts $M$, sparsity $K$, and depth $L$ to ensure both stability and optimal performance at scale. We take a principled step toward resolving this gap by analyzing three different scaling regimes: (I) co-scaling $N\asymp N_e$, (II) co-scaling $N\asymp M\asymp K$, and (III) full proportional scaling of $N, N_e, M$, and $K$. For each regime, we develop a novel Dynamical Mean Field Theory (DMFT) description of the limiting training dynamics of MoEs that provides a formal foundation for our analysis. Within this framework, we derive the unique parameterization for SGD and Adam satisfying all maximal-update ($\mu$) desiderata. We then show that the resulting $\mu$P prescription does not reliably induce monotonic improvement with scale or robust learning-rate transfer. We trace these pathologies to scale-dependent observables in the aggregation dynamics, which motivates a refined set of desiderata that we term maximal scale stability. Guided by this principle, we derive a Maximally Scale-Stable Parameterization (MSSP) for both SGD and Adam in all three scaling regimes, and characterize the corresponding limiting dynamics - qualitatively distinct from the $\mu$P limit - through a separate DMFT analysis. Experiments verify that MSSP robustly recovers learning rate transfer and monotonic improvement with scale across regimes. Combined with existing depth-scaling theory, these results provide a complete scaling prescription for MoE architectures as a function of width, depth, expert width, and number of experts.

---


### 62. [What Should Explanations Contain? A Human-Centered Explanation Content Model for Local, Post-Hoc Explanations](https://arxiv.org/abs/2605.14207)

**<font color=#1a73e8>作者：</font>** Helmut Degen  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Which categories of explanation content are relevant for users of industrial AI systems, and how can those categories be organized for local, post-hoc explanations? To address these questions, a hybrid inductive-deductive qualitative content analysis was applied to 325 meaning units drawn from six user studies in building technology, manufacturing, AI software development, and hospital cybersecurity. The inductive phase produced an initial twelve-code structure. A theory-informed coverage assessment and expert review then added two further codes, Rule base and What-if backward, that were not instantiated in the corpus but correspond to system architectures documented in the XAI literature. The resulting fourteen-code model is organized into four groups: rule-based, causal, epistemic (actual), and epistemic (similar), with twelve codes grounded in the corpus and two as theoretical extensions. An eleven-member expert panel supported the content adequacy of all codes (I-CVI $\geq$ 0.82; scale-level agreement of 0.93 for relevance, 0.92 for boundary clarity, and 0.94 for understandability). A stratified subsample of 82 units (25\% of the corpus), coded independently by two researchers using the finalized codebook, yielded Krippendorff's $\alpha = 0.920$ and Cohen's $\kappa = 0.920$. The paper therefore establishes content adequacy and coding reproducibility for a content-level explanation model intended to support elicitation, specification, and later evaluation of explanation content in industrial AI systems. Behavioral validation of downstream effects remains future work.

---


### 63. [Characterizing AI-Assisted Bot Traffic in Darknet Data: Implications for ICS and IIoT Security](https://arxiv.org/abs/2605.14209)

**<font color=#1a73e8>作者：</font>** Alex Carbajal, Caleb Faultersack, Jonahtan Vasquez 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rise of automated scanning tools and AI assisted reconnaissance agents has significantly altered internet background traffic patterns, threatening the baseline assumptions underlying intrusion detection systems (IDS) deployed in critical infrastructure networks. This paper characterizes the evolution of automated bot traffic by analyzing a longitudinal dataset of 192 million passive darknet packets captured across 2021 and 2025 from the Merit ORION Network Telescope. A modular analysis pipeline was developed to compute metrics including average packet rate, global Shannon entropy, inter-arrival time (IAT) burstiness, geographic attribution, and destination port targeting across key industrial protocols. Results reveal a highly distributed yet focused reconnaissance landscape, with traffic targeting ICS-relevant ports nearly doubling from 0.82% to 1.51% over the four-year period. Furthermore, burstiness analysis exposes intentional micro-pacing behaviors (1ms to 100ms delays) that allow modern botnets to artificially smooth their overall volume. Our simulated anomaly-based IDS demonstrates that these evasion techniques enable 97.47% of modern bot traffic to bypass standard volumetric thresholds undetected. Compensatory sensitivity tuning triggers a 68.10% false-positive rate, highlighting fundamental visibility and alerting gaps in operational technology (OT) environments.

---


### 64. [Towards Fine-Grained and Verifiable Concept Bottleneck Models](https://arxiv.org/abs/2605.14210)

**<font color=#1a73e8>作者：</font>** Yingying Fang, Haijie Xu, Shuang Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Concept Bottleneck Models (CBMs) offer interpretable alternatives to black-box predictors by introducing human-relatable concepts before the final output. However, existing CBMs struggle to verify whether predicted concepts correspond to the correct visual evidence, limiting their reliability. We propose a fine-grained CBM framework that grounds each concept in localized visual evidence, enabling direct inspection of where and how concepts are encoded. This design allows users to interpret predictions and verify that the model learns intended concepts rather than spurious correlations. Experiments on medical imaging benchmarks show that our learned concept space is information-complete and achieves predictive performance comparable to standard CBMs, while substantially improving transparency. Unlike post-hoc attribution methods, our framework validates both the presence and correctness of concept representations, bridging interpretability with verifiability. Our approach enhances the trustworthiness of CBMs and establishes a principled mechanism for human-model interaction at the concept level, paving the way toward more reliable and clinically actionable concept-based learning systems.

---


### 65. [ASH: Agents that Self-Hone via Embodied Learning](https://arxiv.org/abs/2605.14211)

**<font color=#1a73e8>作者：</font>** Benjamin Schneider, Xavier Schneider, Victor Zhong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon embodied tasks remain a fundamental challenge in AI, as current methods rely on hand-engineered rewards or action-labeled demonstrations, neither of which scales. We introduce ASH, an agentic system that learns an embodied policy from unlabeled, noisy internet video, without reward shaping or expert annotation. ASH follows a self-improvement loop; when it gets stuck, ASH learns an Inverse Dynamics Model (IDM) from its own trajectories, and uses its IDM to extract supervision from relevant internet video. ASH uses unsupervised learning to identify key moments from large-scale internet video and retains them as long-term memory -- allowing it to tackle long-horizon problems. We evaluate ASH on two complementary environments demanding multi-hour planning: Pokemon Emerald, a turn-based RPG, and The Legend of Zelda: The Minish Cap, a real-time action-adventure game. In both games, behavioral cloning, retrieval-augmented and zero-shot foundation-model baselines plateau, while ASH sustains progression across our 8-hour evaluation. ASH reaches an average of $11.2/12$ milestones in Pokemon Emerald and $9.9/12$ in Legend of Zelda, while the strongest baseline gets stuck in both environments at an average of $6.5/12$ and $6.0/12$ milestones, respectively. We demonstrate that self-improving agents are a scalable recipe for long-horizon embodied learning.

---


### 66. [MetaAgent-X : Breaking the Ceiling of Automatic Multi-Agent Systems via End-to-End Reinforcement Learning](https://arxiv.org/abs/2605.14212)

**<font color=#1a73e8>作者：</font>** Yaolun Zhang, Yujie Zhao, Nan Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automatic multi-agent systems aim to instantiate agent workflows without relying on manually designed or fixed orchestration. However, existing automatic MAS approaches remain only partially adaptive: they either perform training-free test-time search or optimize the meta-level designer while keeping downstream execution agents frozen, which creating a frozen-executor ceiling and leaving the end-to-end training of self-designing and self-executing agentic models unexplored. To address this, we introduce MetaAgent-X, an end-to-end reinforcement learning framework that jointly optimizes automatic MAS design and execution. MetaAgent-X enables script-based MAS generation, execution rollout collection, and credit assignment for both designer and executor trajectories. To support stable and scalable optimization, we propose Executor Designer Hierarchical Rollout and Stagewise Co-evolution to improve training stability and expose the dynamics of designer-executor co-evolution. MetaAgent-X consistently outperforms existing automatic MAS baselines, achieving up to 21.7% gains. Comprehensive ablations show that both designer and executor improve throughout training, and that effective automatic MAS learning follows a stagewise co-evolution process. These results establish end-to-end trainable automatic MAS as a practical paradigm for building self-designing and self-executing agentic models.

---


### 67. [GenCircuit-RL: Reinforcement Learning from Hierarchical Verification for Genetic Circuit Design](https://arxiv.org/abs/2605.14215)

**<font color=#1a73e8>作者：</font>** Noah Flynn  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Genetic circuit design remains a laborious, expert-driven process despite decades of progress in synthetic biology. We study this problem through code generation: models produce Python code in pysbol3 to construct genetic circuits in the Synthetic Biology Open Language (SBOL), a formal representation that supports automated verification. We introduce GenCircuit-RL, a reinforcement learning framework built around hierarchical verification rewards that decompose correctness into five levels, from code execution to task-specific topological checks, and a four-stage curriculum that shifts optimization pressure from code generation to functional reasoning. We also introduce SynBio-Reason, a benchmark of 4,753 circuits spanning six canonical circuit types and nine tasks from code repair to de novo design, with held-out biological parts for out-of-distribution evaluation. Hierarchical verification improves task success on functional reasoning tasks by 14 to 16 percentage points over binary rewards, and curriculum learning is required for strong design performance. The resulting models generate topologically correct circuits, generalize to novel biological parts, and rediscover canonical designs from the synthetic biology literature.

---


### 68. [Automatic Landmark-Based Segmentation of Human Subcortical Structures in MRI](https://arxiv.org/abs/2605.14221)

**<font color=#1a73e8>作者：</font>** Ahmed Rekik, R. Jarrett Rushmore, Sylvain Bouix 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Precise segmentation of brain structures in magnetic resonance imaging (MRI) is essential for reliable neuroimaging analysis, yet voxel-wise deep models often yield anatomically inconsistent results that diverge from expert-defined boundaries. In this research, we propose a landmark-guided 3D brain segmentation approach that explicitly mimics the manual segmentation protocol of the Harvard--Oxford Atlas. A Global-to-Local network automatically detects 16 landmarks representing key subcortical reference points. Then, a semantic segmentation model produces a coarse segmentation of 12 anatomical labels, each grouping multiple subcortical regions. Finally, a landmark-driven post-processing step separates these 12 labels into 26 distinct structures by enforcing local anatomical constraints. Experimental results demonstrate consistent improvements in boundary accuracy. Overall, integrating learned landmarks aligns segmentations more closely with manual protocols.

---


### 69. [Self-Regulated Learning in Essay Writing: Consistency of Strategies and Impact on Outcomes](https://arxiv.org/abs/2605.14228)

**<font color=#1a73e8>作者：</font>** Gloria Fernández-Nieto, Kiyoshige Garcés, Mladen Raković 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Background: Abilities for effective self-regulated learning (SRL) are critical for lifelong learning, particularly during adolescence when these skills consolidate and strongly influence future learning. Their importance has grown with the rise of online and blended education. Yet, little is known about how secondary school students self-regulate in online environments, how their SRL processes and strategies evolve, or how they affect outcomes. In secondary education, understanding these processes can reveal patterns and indicators of learning success, informing the design of online support mechanisms. Evidence from repeated-measures designs remains scarce. Objectives: This study aims to examine how secondary school students enact SRL strategies during online essay writing, how these strategies change over time, and how they relate to learning outcomes. Methods: We analysed metacognition-related trace data collected from secondary students during a two-wave online essay-writing task conducted one week apart in two Colombian schools (N = 93 for session 1, N = 95 for session 2) via a digital learning platform. Using a combination of process mining and unsupervised machine learning techniques, we identified dominant SRL strategies grounded in established SRL processes and examined their stability and association with learning outcomes. Results and conclusions: Three dominant SRL strategies were identified. Results showed variability: many students remained in or shifted to Read first, write next, while none used Write intensively, read selectively in session 2. Although less common, latter strategy was positively associated with learning outcomes.

---


### 70. [On the (non-)resilience of encrypted controllers to covert attacks](https://arxiv.org/abs/2605.14230)

**<font color=#1a73e8>作者：</font>** Philipp Binfet, Janis Adamek, Moritz Schulze Darup  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The security of networked control systems (NCS) is receiving increasing attention from both cyber-security and system-theoretic perspectives. The former focuses on classical IT security goals such as confidentiality, integrity, and availability of process data, while the latter investigates tailored attacks (and detection schemes), including covert and zero-dynamics attacks. Confidentiality in control systems can, for instance, be achieved by securely outsourcing the evaluation of the controller to third-party platforms, such as cloud services. The underlying technology enabling such secure computation often is homomorphic encryption (HE).
Recent works in encrypted control have proposed modifications to underlying HE schemes to achieve not only confidentiality but also resilience to certain types of integrity attacks. While extensions in this direction are desirable in principle, we show that the integrity problem in encrypted control cannot be solved by public-key HE schemes alone due to their inherent malleability. In other words, the same homomorphisms that enable encrypted control % in the first place can be leveraged not only constructively but also destructively. More precisely, we demonstrate that NCS are vulnerable to covert attacks, even when encrypted control is employed. Remarkably, this remains possible without knowledge of an unencrypted model.
Yet, resilience to such attacks can still be achieved through complementary techniques. We present an approach based on verifiable computation that integrates with modern homomorphic cryptosystems and is asymptotically secure while incurring no communication overhead.

---


### 71. [AudioMosaic: Contrastive Masked Audio Representation Learning](https://arxiv.org/abs/2605.14231)

**<font color=#1a73e8>作者：</font>** Hanxun Huang, Qizhou Wang, Xingjun Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Audio self-supervised learning (SSL) aims to learn general-purpose representations from large-scale unlabeled audio data. While recent advances have been driven mainly by generative reconstruction objectives, contrastive approaches remain less explored, partly due to the difficulty of designing effective audio augmentations and the large batch sizes required for contrastive pre-training. We introduce \textbf{AudioMosaic}, a contrastive learning-based audio encoder for general audio understanding. During pre-training, AudioMosaic constructs positive pairs by applying structured time-frequency masking to spectrogram patches, which reduces memory usage and enables efficient large-batch training. Compared with generative approaches, the AudioMosaic encoder learns more discriminative utterance-level representations that demonstrate strong transferability across datasets, domains, and acoustic conditions. Extensive experiments show that AudioMosaic achieves state-of-the-art performance on several standard audio benchmarks under both linear probing and fine-tuning. We further show that integrating the pretrained AudioMosaic encoder into audio-language models improves performance on audio-language tasks. The code is publicly available in our \href{this https URL}{GitHub repository}.

---


### 72. [Quantum Advantage in Multi Agent Reinforcement Learning](https://arxiv.org/abs/2605.14235)

**<font color=#1a73e8>作者：</font>** Simranjeet Singh Dahia, Claudia Szabo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present an empirical evaluation of quantum entanglement in agent coordination within quantum multi agent reinforcement learning (QMARL). While QMARL has attracted growing interest recently, most prior work evaluates quantum policies without provable baselines, making it impossible to rigorously distinguish quantum advantage from algorithmic coincidence. We address this directly by evaluating a decentralized QMARL framework with variational quantum circuit (VQC) actors with shared entangled states. In the CHSH game, which has a mathematically proven classical performance ceiling of 0.75 win rate, we show that entangled QMARL agents approach the Tsirelson limit of 0.854, providing clear evidence of their quantum advantage. We show that unentangled quantum circuits match the classical baseline, confirming that entanglement and not the quantum circuit itself is the active coordination mechanism. We also explore the effect of specific entanglement structures, as some Bell states enable coordination gains while others actively harm performance. On cooperative navigation (CoopNav), QMARL without entanglement achieves $\sim2\times$ improvement in success rate over classical MAA2C ($\sim$0.85 versus $\sim$0.40), with the hybrid configuration, quantum actor paired with a classical centralised critic, outperforming both fully classical and fully quantum solutions. We present our experimental analysis and discuss future work.

---


### 73. [Active Learners as Efficient PRP Rerankers](https://arxiv.org/abs/2605.14236)

**<font color=#1a73e8>作者：</font>** Jeremías Figueiredo Paschmann, Juan Kaplan, Francisco Nattero Santiago Mauricio Barron Bucolo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pairwise Ranking Prompting (PRP) elicits pairwise preference judgments from an LLM, which are then aggregated into a ranking, usually via classical sorting algorithms. However, judgments are noisy, order-sensitive, and sometimes intransitive, so sorting assumptions do not match the setting. Because sorting aims to recover a full permutation, truncating it to meet a call budget does not produce a dependable top-K. We thus reframe PRP reranking as active learning from noisy pairwise comparisons and show that active rankers are drop-in replacements that improve NDCG@10 per call in the call-constrained regime. Our noise-robust framework also introduces a randomized-direction oracle that uses a single LLM call per pair. This approach converts systematic position bias into zero-mean noise, enabling unbiased aggregate ranking without the cost of bidirectional calls.

---


### 74. [Good to Go: The LOOP Skill Engine That Hits 99% Success and Slashes Token Usage by 99% via One-Shot Recording and Deterministic Replay](https://arxiv.org/abs/2605.14237)

**<font color=#1a73e8>作者：</font>** Xiaohua Wang, Kai Yu, XuXiao Liang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deploying AI agents for repetitive periodic tasks exposes a critical tension: Large Language Models (LLMs) offer unmatched flexibility in tool orchestration, yet their inherent stochasticity causes unpredictable failures, and repeated invocations incur prohibitive token costs. We present the LOOP SKILL ENGINE, a system that achieves a combined 99% success rate and 99% token reduction for periodic agent tasks through a one-shot recording, deterministic replay paradigm. On its first run, the agent executes the task with full LLM reasoning while the system transparently intercepts and records the complete tool-call trajectory. A greedy length-descending template extraction algorithm then converts this recording into a parameterized, branch-free Loop Skill -- a deterministic execution plan that captures the task's functional intent while parameterizing time-dependent and result-dependent variables. All subsequent executions bypass the LLM entirely: the engine resolves template variables against real-time values and replays the tool sequence deterministically. We prove two theorems: (1) Replay Determinism -- the step sequence of a validated Loop Skill is invariant across all future executions; (2) Write Safety -- concurrent access to persistent configuration is serialized through reentrant locks and atomic file replacement. Across a benchmark of periodic agent tasks spanning intervals from 5 minutes to 24 hours, the Loop Skill Engine reduces monthly token consumption by 93.3%--99.98% and cuts execution latency by 8.7x while eliminating output non-determinism. A multi-layer degradation strategy guarantees that tasks never stall. We release the engine as part of the buddyMe open-source agent framework.

---


### 75. [Implicit spatial-frequency fusion of hyperspectral and lidar data via kolmogorov-arnold networks](https://arxiv.org/abs/2605.14239)

**<font color=#1a73e8>作者：</font>** Zekun Long, Judy X. Yang, Jing Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral image (HSI) classification is challenging in complex scenes due to spectral ambiguity, spatial heterogeneity, and the strong coupling between material properties and geometric structures. Although LiDAR provides complementary elevation information, most HSI-LiDAR fusion methods rely on CNNs or MLPs with fixed activation functions and linear weights. These methods struggle to model structural discontinuities in LiDAR data, intricate spectral features of HSI, and their interactions. In addition, fusion of the two modalities in both spatial and frequency domains with LiDAR guidance remains underexplored.
To address these issues, we propose the Implicit Frequency-Geometry Fusion Network (IFGNet), which leverages Kolmogorov-Arnold Networks (KANs) with learnable spline-based functions to adaptively capture highly nonlinear relationships between hyperspectral and LiDAR features. Furthermore, IFGNet introduces a LiDAR-guided implicit aggregation module in both spatial and frequency domains, enhancing geometry-aware spatial representations while capturing global structural patterns.
Experiments on the Houston 2013 and MUUFL benchmarks demonstrate that IFGNet consistently outperforms existing fusion methods in overall accuracy, average accuracy, and Cohen's Kappa, while maintaining an efficient architecture.

---


### 76. [Paraphrasing Attack Resilience of Various AI-Generated Text Detection Methods](https://arxiv.org/abs/2605.14240)

**<font color=#1a73e8>作者：</font>** Andrii Shportko, Inessa Verbitsky  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The recent large-scale emergence of LLMs has left an open space for dealing with their consequences, such as plagiarism or the spread of false information on the Internet. Coupling this with the rise of AI detector bypassing tools, reliable machine-generated text detection is in increasingly high demand. We investigate the paraphrasing attack resilience of various machine-generated text detection methods, evaluating three approaches: fine-tuned RoBERTa, Binoculars, and text feature analysis, along with their ensembles using Random Forest classifiers. We discovered that Binoculars-inclusive ensembles yield the strongest results, but they also suffer the most significant losses during attacks. In this paper, we present the dichotomy of performance versus resilience in the world of AI text detection, which complicates the current perception of reliability among state-of-the-art techniques.

---


### 77. [Artificial Intelligence-Assistant Cardiotocography: Unified Model for Signal Reconstruction, Fetal Heart Rate Analysis, and Variability Assessment](https://arxiv.org/abs/2605.14242)

**<font color=#1a73e8>作者：</font>** Xiaohua Wang, Kai Yu, XuXiao Liang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The monitoring of fetal heart rate (FHR) and the assessment of its variability are crucial for preventing fetal compromise and adverse outcomes. However, traditional methods encounter limitations arising from equipment performance, data transmission, and subjective assessments by doctors. We have developed a tailored AI-based FHrCTG model specifically for FHR monitoring, which effectively mitigates noise interference and precisely reconstructs signals. Our model was pre-trained on a massive dataset consisting of 558,412 unlabeled data points and further refined using 7,266 expert-reviewed entries. To validate FHR, we introduced the Intersection Overlapping Labels (IOL) approach, which transforms rate analysis into categorical judgments. Testing revealed that our model demonstrates high sensitivity and specificity in detecting critical FHR decelerations (89.13% and 87.78%, respectively) and accelerations (62.5% and 92.04%, respectively). Furthermore, based on Fischer's criteria for clinical application, our model achieved impressive AUC scores of 0.7214 and 0.9643 for verifying FHR periodicity and amplitude variation, respectively.

---


### 78. [Action-Conditioned Risk Gating for Safety-Critical Control under Partial Observability](https://arxiv.org/abs/2605.14246)

**<font color=#1a73e8>作者：</font>** Yushen Liu, Yin-Jen Chen, Ziyi Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many safety-critical control problems are modeled as risk-sensitive partially observable Markov decision processes, where the controller must make decisions from incomplete observations while balancing task performance against safety risk. Although belief-space planning provides a principled solution, maintaining and planning over beliefs can be computationally costly and sensitive to model specification in practical domains. We propose a lightweight risk-gated reinforcement learning approximation for risk-sensitive control under partial observability. The method constructs a compact finite-history proxy state and learns an action-conditioned predictor of near-term safety violation. This predicted candidate-action risk is used in two complementary ways: as a risk penalty during value learning, and as a decision-time gate that interpolates between optimistic and conservative ensemble value estimates. As a result, low-risk actions are evaluated closer to reward-seeking estimates, while high-risk actions are evaluated more conservatively. We evaluate the approach in two safety-critical partially observable domains: automated glucose regulation and safety-constrained navigation. Across adult and adolescent glucose-control cohorts, the method improves overall glycemic tradeoffs and substantially reduces runtime relative to a belief-space planning baseline. On Safety-Gym navigation benchmarks, it achieves a more favorable reward-cost balance than unconstrained RL and several standard safe-RL baselines. These results suggest that action-conditioned near-term risk can provide an effective local signal for approximate risk-sensitive POMDP control when full belief-space planning is impractical.

---


### 79. [Generative Deep Learning for Computational Destaining and Restaining of Unregistered Digital Pathology Images](https://arxiv.org/abs/2605.14251)

**<font color=#1a73e8>作者：</font>** Aarushi Kulkarni, Alarice Lowe, Pratik Shah  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conditional generative adversarial networks (cGANs) have enabled high-fidelity computational staining and destaining of hematoxylin and eosin (H&E) in digital pathology whole-slide images (WSI). However, their ability to generalize to out-of-distribution WSI across institutions without retraining remains insufficiently characterized. Previously developed cGAN models trained on 102 registered prostate core biopsy WSIs from Brigham and Women's Hospital were evaluated on 82 spatially unregistered WSIs acquired at Stanford University. To mitigate domain shift without retraining, a preprocessing pipeline consisting of histogram-based stain normalization for H&E-stained WSIs and channel-wise intensity calibration for unstained WSIs was developed. Because image registration was intentionally omitted for real-world deployment conditions, the reported quantitative results are conservative lower bounds reflecting both model performance and limited spatial alignment. Under these conditions, virtual destaining achieved a Pearson correlation coefficient (PCC) of 0.854, structural similarity index measure (SSIM) of 0.699, and peak signal-to-noise ratio (PSNR) of 18.41 dB. H&E restaining from computationally destained outputs outperformed direct staining from ground-truth unstained inputs across all metrics (PCC: 0.798 vs. 0.715; SSIM: 0.756 vs. 0.718; PSNR: 20.08 vs. 18.51 dB), suggesting that preprocessing quality may be more limiting than model capacity. Qualitative pathological review indicated preservation of benign glandular structures while showing that malignant glands were often rendered with vessel-like morphologies. These findings support the feasibility of applying cGAN-based computational H&E staining and destaining generative models to external WSI datasets using preprocessing-based adaptation alone while defining specific morphological targets for future domain adaptation.

---


### 80. [Towards Real-Time Autonomous Navigation: Transformer-Based Catheter Tip Tracking in Fluoroscopy](https://arxiv.org/abs/2605.14253)

**<font color=#1a73e8>作者：</font>** Harry Robertshaw, Yanghe Hao, Weiyuan Deng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Purpose: Mechanical thrombectomy (MT) improves stroke outcomes, but is limited by a lack of local treatment access. Widespread distribution of reinforcement learning (RL)-based robotic systems can be used to alleviate this challenge through autonomous navigation, but current RL methods require live device tip coordinate tracking to function. This paper aims to develop and evaluate a real-time catheter tip tracking pipeline under fluoroscopy, addressing challenges such as low contrast, noise, and device occlusion. Methods: A multi-threaded pipeline was designed, incorporating frame reading, preprocessing, inference, and post-processing. Deep learning segmentation models, including U-Net, U-Net+Transformer, and SegFormer, were trained and benchmarked using two-class and three-class formulations. Post-processing involved two-step component filtering, one-pixel medial skeletonization, and greedy arc-length path following with contour fall-back. Results: On manually-labeled moderate complexity fluoroscopic video data, the two-class SegFormer achieved a mean absolute error of 4.44 mm, outperforming U-Net (4.60 mm), U-Net+Transformer (6.20 mm) and all three-class models (5.19-7.74 mm). On segmentation benchmarks, the system exceeded state-of-the-art CathAction results with improvements of up to +5% in Dice scores for three-segmentation. Conclusion: The results demonstrate that the proposed multi-threaded tracking framework maintains stable performance under challenging imaging conditions, outperforming prior benchmarks, while providing a reliable and efficient foundation for RL-based autonomous MT navigation.

---


### 81. [Architecture-Aware Explanation Auditing for Industrial Visual Inspection](https://arxiv.org/abs/2605.14255)

**<font color=#1a73e8>作者：</font>** Sibo Jia, Zihang Zhao, Kunrong Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Industrial visual inspection systems increasingly rely on deep classifiers whose heatmap explanations may appear visually plausible while failing to identify the image regions that actually drive model decisions. This paper operationalizes an architecture-aware explanation audit protocol grounded in the native-readout hypothesis: the perturbation-based faithfulness of an explanation method is bounded by its structural distance from the model's native decision mechanism. On WM-811K wafer maps (9 classes, 172k images) under a three-seed zero-fill perturbation protocol, ViT-Tiny + Attention Rollout attains Deletion AUC 0.211 against 0.432-0.525 for Swin-Tiny / ResNet18+CBAM / DenseNet121 + Grad-CAM (abs(Cohen's d) > 1.1), despite lower classification accuracy. Swin-Tiny disentangles architecture family from readout structure: despite being a Transformer, its spatial feature-map hierarchy makes it Grad-CAM compatible, showing that the operative factor is readout structure rather than architecture family. A model-agnostic control (RISE) compresses all families to Deletion AUC about 0.1, indicating the gap arises from the explainer pathway; notably, RISE outperforms all native methods, so native readout is a compatibility principle rather than an optimality guarantee. A blur-fill sensitivity analysis shows that the family ordering reverses under a different perturbation baseline, reinforcing that faithfulness rankings are joint properties of (model, explainer, perturbation operator) triples. An exploratory boundary-condition study on MVTec AD (pretrained models) indicates that audit results are dataset/task dependent and identifies conditions requiring qualification. The protocol yields actionable guidance: explanation pathways should be co-designed with model architectures based on readout structure, and deployed heatmaps should be accompanied by quantitative faithfulness metrics.

---


### 82. [What Makes Words Hard? Sakura at BEA 2026 Shared Task on Vocabulary Difficulty Prediction](https://arxiv.org/abs/2605.14257)

**<font color=#1a73e8>作者：</font>** Adam Nohejl, Xuanxin Wu, Yusuke Ide 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We describe two types of models for vocabulary difficulty prediction: a high-accuracy black-box model, which achieved the top shared task result in the open track, and an explainable model, which outperforms a fine-tuned encoder baseline. As the black-box model, we fine-tuned an LLM using a soft-target loss function for effective application to the rating task, achieving r > 0.91. The explainable model provides insights into what impacts the difficulty of each item while maintaining a strong correlation (r > 0.77). We further analyze the results, demonstrating that the difficulty of items in the British Council's Knowledge-based Vocabulary Lists (KVL) is often affected by spelling difficulty or the construction of the test items, in addition to the genuine production difficulty of the words. We make our code available online at this https URL .

---


### 83. [Dynamics of the Transformer Residual Stream: Coupling Spectral Geometry to Network Topology](https://arxiv.org/abs/2605.14258)

**<font color=#1a73e8>作者：</font>** Jesseba Fernando, Grigori Guitchounts  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models are remarkably capable, yet how computation propagates through their layers remains poorly understood. A growing line of work treats depth as discrete time and the residual stream as a dynamical system, where each layer's nonlinear update has a local linear description. However, previous analyses have relied on scalar summaries or approximate linearizations, leaving the full spectral geometry of trained LLMs unknown. We perform full Jacobian eigendecomposition across three production--scale LLMs and show that training installs a monotonic spectral gradient through depth -- from non-normal, rotation-dominated early layers to near--symmetric late layers -- together with a cumulative low-rank bottleneck that funnels perturbations into a small fraction of the residual stream's effective dimensions. Our experiments reveal that this gradient and the dimensional collapse are learned rather than architectural, and is largely dissolved when structured non-normality is removed. We further show that the topological positioning of graph communities predicts whether the Jacobian amplifies or suppresses them, with the sign of the coupling determined by the local operator type, a relationship absent at initialization. These results map a learned spectral geometry in LLMs that links perturbation propagation and compression to the network's functional topology.

---


### 84. [Heuristic Pathologies and Further Variance Reduction via Uncertainty Propagation in the AIVAT Family of Techniques](https://arxiv.org/abs/2605.14261)

**<font color=#1a73e8>作者：</font>** Juho Kim, Tuomas Sandholm  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> How should an agent's performance in a multiagent environment be evaluated when there is a limited sample size or a high cost of running a trial? The AIVAT family of variance reduction techniques was proposed to address this challenge by introducing unbiased low-variance estimators of agents' expected payoffs. An important component of AIVAT is a heuristic value function that discriminates between potentially low- and high-value counterfactual histories. A notable gap in the literature is that there is little to no constraint or guideline on how the heuristic value function should be chosen or how uncertainty in its output should be handled.
In our first contribution, we parameterize the heuristic value function to highlight AIVAT's potential vulnerabilities: a) the sample variance can be set pathologically low by directly applying gradient descent on the sample variance, and b) one can p-hack to draw a desired statistical conclusion via gradient descent/ascent on the test statistic. The main takeaway is that the heuristic value function should be fixed prior to observing the evaluation data! In our second contribution, we show how the heuristic uncertainty can be propagated to quantify the uncertainty of AIVAT estimates. It is then possible to further reduce the variance using inverse-variance weighted averaging, but AIVAT's unbiasedness guarantee may have to be sacrificed. In our experiments, we use a dataset of 10,000 poker hands to demonstrate our heuristic pathology and uncertainty results, with the latter yielding a 43.0% reduction in the number of samples (poker hands) needed to draw statistical conclusions.

---


### 85. [Image Restoration via Diffusion Models with Dynamic Resolution](https://arxiv.org/abs/2605.14267)

**<font color=#1a73e8>作者：</font>** Yang Zheng, Wen Li, Zhaoqiang Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models (DMs) have exhibited remarkable efficacy in various image restoration tasks. However, existing approaches typically operate within the high-dimensional pixel space, resulting in high computational overhead. While methods based on latent DMs seek to alleviate this issue by utilizing the compressed latent space of a variational autoencoder, they require repeated encoder-decoder inference. This introduces significant additional computational burdens, often resulting in runtime performance that is even inferior to that of their pixel-space counterparts. To mitigate the computational inefficiency, this work proposes projecting data into lower-dimensional subspaces using dynamic resolution DMs to accelerate the inference process. We first fine-tune pre-trained DMs for dynamic resolution priors and adapt DPS and DAPS, which are two widely used pixel-space methods for general image restoration tasks, into the proposed framework, yielding methods we refer to as SubDPS and SubDAPS, respectively. Given the favorable inference speed and reconstruction fidelity of SubDAPS, we introduce an enhanced variant termed SubDAPS++ to further boost both reconstruction efficiency and quality. Empirical evaluations across diverse image datasets and various restoration tasks demonstrate that the proposed methods outperform recent DM-based approaches in the majority of experimental scenarios. The code is available at this https URL.

---


### 86. [PhyMotion: Structured 3D Motion Reward for Physics-Grounded Human Video Generation](https://arxiv.org/abs/2605.14269)

**<font color=#1a73e8>作者：</font>** Yidong Huang, Zun Wang, Han Lin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating realistic human motion is a central yet unsolved challenge in video generation. While reinforcement learning (RL)-based post-training has driven recent gains in general video quality, extending it to human motion remains bottlenecked by a reward signal that cannot reliably score motion realism. Existing video rewards primarily rely on 2D perceptual signals, without explicitly modeling the 3D body state, contact, and dynamics underlying articulated human motion, and often assign high scores to videos with floating bodies or physically implausible movements. To address this, we propose PhyMotion, a structured, fine-grained motion reward that grounds recovered 3D human trajectories in a physics simulator and evaluates motion quality along multiple dimensions of physical feasibility. Concretely, we recover SMPL body meshes from generated videos, retarget them onto a humanoid in the MuJoCo physics simulator, and evaluate the resulting motion along three axes: kinematic plausibility, contact and balance consistency, and dynamic feasibility. Each component provides a continuous and interpretable signal tied to a specific aspect of motion quality, allowing the reward to capture which aspects of motion are physically correct or violated. Experiments show that PhyMotion achieves stronger correlation with human judgments than existing reward formulations. These gains carry over to RL-based post-training, where optimizing PhyMotion leads to larger and more consistent improvements than optimizing existing rewards, improving motion realism across both autoregressive and bidirectional video generators under both automatic metrics and blind human evaluation (+68 Elo gain). Ablations show that the three axes provide complementary supervision signals, while the reward preserves overall video generation quality with only modest training overhead.

---


### 87. [Auditing Agent Harness Safety](https://arxiv.org/abs/2605.14271)

**<font color=#1a73e8>作者：</font>** Chengzhi Liu, Yichen Guo, Yepeng Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly run inside execution harnesses that dispatch tools, allocate resources, and route messages between specialized components. However, a harness can return a correct, benign answer over a trajectory that accesses unauthorized resources or leaks context to the wrong agent. Output-level evaluation cannot see these failures, yet most safety benchmarks score only final outputs or terminal states, even though many violations occur mid-trajectory rather than at termination. The central question is whether the harness respects user intent, permission boundaries, and information-flow constraints throughout execution. To address this gap, we propose HarnessAudit, a framework that audits full execution trajectories across boundary compliance, execution fidelity, and system stability, with a focus on multi-agent harnesses where these risks are most pronounced. We further introduce HarnessAudit-Bench, a benchmark of 210 tasks across eight real-world domains, instantiated in both single-agent and multi-agent configurations with embedded safety constraints. Evaluating ten harness configurations across frontier models and three multi-agent frameworks, we find that: (i) task completion is misaligned with safe execution, and violations accumulate with trajectory length; (ii) safety risks vary across domains, task types, and agent roles; (iii) most violations concentrate in resource access and inter-agent information transfer; and (iv) multi-agent collaboration expands the safety risk surface, while harness design sets the upper bound of safe deployment.

---


### 88. [CreFlow: Corrective Reflow for Sparse-Reward Embodied Video Diffusion RL](https://arxiv.org/abs/2605.14274)

**<font color=#1a73e8>作者：</font>** Zhenyang Ni, Yijiang Li, Ruochen Jiao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation models trained on heterogeneous data with likelihood-surrogate objectives can produce visually plausible rollouts that violate physical constraints in embodied manipulation. Although reinforcement-learning post-training offers a natural route to adapting VGMs, existing video-RL rewards often reduce each rollout to a low-level visual metric, whereas manipulation video evaluation requires logic-based verification of whether the rollout satisfies a compositional task specification. To fill this gap, we introduce a compositional constraint-based reward model for post-training embodied video generation models, which automatically formulates task requirements as a composition of Linear Temporal Logic constraints, providing faithful rewards and localized error information in generated videos. To achieve effective improvement in high-dimensional video generation using these reward signals, we further propose CreFlow, a novel online RL framework with two key designs: i) a credit-aware NFT loss that confines the RL update to reward-relevant regions, preventing perturbations to unrelated regions during post-training; and ii) a corrective reflow loss that leverages within-group positive samples as an explicit estimate of the correction direction, stabilizing and accelerating training. Experiments show that CreFlow yields reward judgments better aligned with human and simulator success labels than existing methods and improves downstream execution success by 23.8 percentage points across eight bimanual manipulation tasks.

---


### 89. [Parallelizing Counterfactual Regret Minimization](https://arxiv.org/abs/2605.14277)

**<font color=#1a73e8>作者：</font>** Juho Kim, Tuomas Sandholm  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Parallelization has played an instrumental role in the field of artificial intelligence (AI), drastically reducing the time taken to train and evaluate large AI models. In contrast to its impact in the broader field of AI, applying parallelization to computational game solving is relatively unexplored, despite its great potential. In this paper, we parallelize the family of counterfactual regret minimization (CFR) algorithms, which were central to important breakthroughs for solving large imperfect-information games. We present a generalized parallelization framework, reframing CFR as a series of linear algebra operations. Then, existing techniques for parallelizing linear algebra operations can be applied to accelerate CFR. We also describe how our technique can be applied to other tabular members of the CFR family of algorithms, including the state-of-the-art, such as CFR+, discounted CFR, and predictive variants of CFR. Experimentally, we show that our CFR implementation on a GPU is up to four orders of magnitude faster than Google DeepMind OpenSpiel's CFR implementations on a CPU.

---


### 90. [TILT: Target-induced loss tilting under covariate shift](https://arxiv.org/abs/2605.14280)

**<font color=#1a73e8>作者：</font>** Kakei Yamamoto, Martin J. Wainwright  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce and analyze Target-Induced Loss Tilting (TILT) for unsupervised domain adaptation under covariate shift. It is based on a novel objective function that decomposes the source predictor as $f+b$, fits $f+b$ on labeled source data while simultaneously penalizing the auxiliary component $b$ on unlabeled target inputs. The resulting fit $f$ is deployed as the final target predictor. At the population level, we show that this target-side penalty implicitly induces relative importance weighting at the population level, but in terms of an estimand $b^*_f$ that is self-localized to the current error, and remains uniformly bounded for any source-target pair (even those with disjoint supports). We prove a general finite-sample oracle inequality on the excess risk, and use it to give an end-to-end guarantee for training with sparse ReLU networks. Experiments on controlled regression problems and shifted CIFAR-100 distillation show that TILT improves target-domain performance over source-only training, exact importance weighting, and relative density-ratio baselines, with a stable dependence on the regularization parameter.

---


### 91. [Smooth Multi-Policy Causal Effect Estimation in Longitudinal Settings](https://arxiv.org/abs/2605.14284)

**<font color=#1a73e8>作者：</font>** Wenxin Chen, Weishen Pan, Kyra Gan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Comparative evaluation of multiple dynamic treatment policies is essential for healthcare and policy decisions, yet conventional longitudinal causal inference methods estimate each in isolation, preventing information sharing across counterfactuals. We demonstrate that this separate estimation paradigm induces a structurally uncontrolled second-order bias, inflating finite-sample variance even after standard debiasing with longitudinal targeted maximum likelihood estimation(LTMLE). To address this, we propose a policy-aware reparameterization of Iterative Conditional Expectation (ICE) Q-functions that enables joint estimation through shared representations. We implement this approach in the Policy-Encoded Q Network (PEQ-Net), an architecture centered on a shared policy encoder. The encoder is trained using kernel mean embeddings, ensuring that the learned representation space reflects population-level policy dissimilarities. After applying an LTMLE correction step, we prove this design imposes a structural constraint on the second-order remainder, thereby stabilizing finite-sample variance. Experiments on semi-synthetic datasets demonstrate that PEQ-Net consistently outperforms existing ICE-based methods, achieving substantial reductions in root-mean-square error, particularly when evaluating closely related policies.

---


### 92. [Web Agents Should Adopt the Plan-Then-Execute Paradigm](https://arxiv.org/abs/2605.14290)

**<font color=#1a73e8>作者：</font>** Julien Piet, Annabella Chow, Yiwei Hou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> ReAct has become the default architecture across LLM agents, and many existing web agents follow this paradigm. We argue that it is the wrong default for web agents. Instead, web agents should default to plan-then-execute: commit to a task-specific program before observing runtime web content, then execute it. The reason is that web content mixes inputs from many parties. An e-commerce product page may combine a seller's listing, customer reviews and sponsored advertisements. Under ReAct, all of this content flows into the model when deciding on the next action, creating a direct path for prompt injections to steer the agent's control flow. Plan-then-execute changes this boundary: untrusted data may influence values or branches inside a predefined execution graph, but it cannot redefine the user task or cause the model to synthesize new actions at runtime. We analyze WebArena, a popular web agent benchmark, and find that all tasks are compatible with plan-then-execute, while 80% can be completed with a purely programmatic plan, without any runtime LLM subroutine. We identify the main barrier to adopting plan-then-execute on the web: For it to work well, tools must map cleanly to semantic actions, with effects known before execution, so agents have enough information to plan. The web does not naturally expose that interface. Browser tools such as click, type, and scroll have page-dependent meanings. Planning at this layer is near-sighted: the agent can only see actions on the current page, and later actions appear only after it acts. Closing this gap requires typed interfaces that turn website interactions from clicks and keystrokes to task-level operations. This is an infrastructure problem, not a modeling problem. Web tasks do not need reactivity by default; they need typed, complete, auditable website APIs.

---


### 93. [Precise Verification of Transformers through ReLU-Catalyzed Abstraction Refinement](https://arxiv.org/abs/2605.14294)

**<font color=#1a73e8>作者：</font>** Hengjie Liu, Zhenya Zhang, Jianjun Zhao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Formal verification of transformers has become increasingly important due to their widespread deployment in safety-critical applications. Compared to classic neural networks, the inferences of transformers involve highly complex computations, such as dot products in self-attention layers, rendering their verification extremely difficult. Existing approaches explored over-approximation methods by constructing convex constraints to bound the output ranges of transformers, which can achieve high efficiency. However, they may sacrifice verification precision, and consequently introduce significant approximation error that leads to frequent occurrences of false alarms. In this paper, we propose a transformer verification approach that can achieve improved precision. At the core of our approach is a novel usage of ReLU, by which we represent a precise but non-linear bound for dot products such that we can further exploit the rich body of literature for convex relaxation of ReLU to derive precise bounds. We extend two classic approaches to the context of transformers, a rule-based one and an optimization-based one, resulting in two new frameworks for efficient and precise verification. We evaluate our approaches on different model architectures and robustness properties derived from two datasets about sentiment analysis, and compare with the state-of-the-art baseline approach. Compared to the baseline, our approach can achieve significant precision improvement for most of the verification tasks with acceptable compromise of efficiency, which demonstrates the effectiveness of our approach.

---


### 94. [Policy Optimization in Hybrid Discrete-Continuous Action Spaces via Mixed Gradients](https://arxiv.org/abs/2605.14297)

**<font color=#1a73e8>作者：</font>** Matias Alvo, Daniel Russo, Yash Kanoria  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study reinforcement learning in hybrid discrete-continuous action spaces, such as settings where the discrete component selects a regime (or index) and the continuous component optimizes within it -- a structure common in robotics, control, and operations problems. Standard model-free policy gradient methods rely on score-function (SF) estimators and suffer from severe credit-assignment issues in high-dimensional settings, leading to poor gradient quality. On the other hand, differentiable simulation largely sidesteps these issues by backpropagating through a simulator, but the presence of discrete actions or non-smooth dynamics yields biased or uninformative gradients. To address this, we propose Hybrid Policy Optimization (HPO), which backpropagates through the simulator wherever smoothness permits, using a mixed gradient estimator that combines pathwise and SF gradients while maintaining unbiasedness. We also show how problems with action discontinuities can be reformulated in hybrid form, further broadening its applicability. Empirically, HPO substantially outperforms PPO on inventory control and switched linear-quadratic regulator problems, with performance gaps increasing as the continuous action dimension grows. Finally, we characterize the structure of the mixed gradient, showing that its cross term -- which captures how continuous actions influence future discrete decisions -- becomes negligible near a discrete best response, thereby enabling approximate decentralized updates of the continuous and discrete components and reducing variance near optimality. All resources are available at this http URL.

---


### 95. [Matrix-Space Reinforcement Learning for Reusing Local Transition Geometry](https://arxiv.org/abs/2605.14304)

**<font color=#1a73e8>作者：</font>** Zuyuan Zhang, Carlee Joe-Wong, Tian Lan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Compositional generalization in sequential decision-making requires identifying which parts of prior rollouts remain useful for new tasks. Existing methods reuse skills or predictive models, but often overlook rich local transition geometry and dynamics. We propose Matrix-Space Reinforcement Learning (MSRL), a geometric abstraction that represents trajectory segments through positive semidefinite matrix descriptors aggregating first- and second-order statistics of lifted one-step transitions. These descriptors expose shared hidden structure, support algebraic composition in an abstract matrix space, and reveal opportunities for transfer. We prove that the descriptor is well defined up to coordinate gauge, complete for the induced low-order additive signal class, additive under valid segment composition, and minimally sufficient among admissible additive descriptors. We further show that conditioning value functions on the trajectory-segment matrix yields a first-order smooth approximation of action values, enabling source-learned matrix-to-value mappings to bootstrap learning in new tasks. MSRL is plug-in compatible with standard model-free and model-based methods, while obstruction filtering rejects implausible compositions. Empirically, MSRL achieves the best average finite-budget target AUC of 0.73, outperforming MSRL from scratch (0.65), TD-MPC-PT+FT (0.63), and TD-MPC (0.57).

---


### 96. [CoRDS: Coreset-based Representative and Diverse Selection for Streaming Video Understanding](https://arxiv.org/abs/2605.14310)

**<font color=#1a73e8>作者：</font>** Ailar Mahdizadeh, Puria Azadi, Muchen Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming video understanding with large vision-language models (VLMs) requires a compact memory that can support future reasoning over an ever-growing visual history. A common solution is to compress the key-value (KV) cache, but existing streaming methods typically rely on local token-wise heuristics, such as recency, temporal redundancy, or saliency, which do not explicitly optimize whether the retained cache is representative of the accumulated history. We propose to view KV-cache compression as a coreset selection problem: rather than scoring tokens independently for retention, we select a small subset that covers the geometry of the accumulated visual cache. Our method operates in a joint KV representation and introduces a bicriteria objective that balances coverage in key and value spaces, preserving both retrieval structure and output-relevant information. To encourage a more diverse retained subset, we further introduce an orthogonality-driven diversity criterion that favors candidates contributing new directions beyond the current selection, and connect this criterion to log-determinant subset selection. Across four open-source VLMs and five long-video and streaming-video benchmarks, our method improves over heuristic streaming compression baselines under a fixed cache budget. These results highlight that representative coreset selection offers a more effective principle, than token-wise pruning, for memory-constrained streaming video understanding.

---


### 97. [TurboVGGT: Fast Visual Geometry Reconstruction with Adaptive Alternating Attention](https://arxiv.org/abs/2605.14315)

**<font color=#1a73e8>作者：</font>** David Huang, Guile Wu, Chengjie Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent feed-forward 3D reconstruction methods, such as visual geometry transformers, have substantially advanced the traditional per-scene optimization paradigm by enabling effective multi-view reconstruction in a single forward pass. However, most existing methods struggle to achieve a balance between reconstruction quality and computational efficiency, which limits their scalability and efficiency. Although some efficient visual geometry transformers have recently emerged, they typically use the same sparsity ratio across layers and frames and lack mechanisms to adaptively learn representative tokens to capture global relationships, leading to suboptimal performance. In this work, we propose TurboVGGT, a novel approach that employs an efficient visual geometry transformer with adaptive alternating attention for fast multi-view 3D reconstruction. Specifically, TurboVGGT employs an end-to-end trainable framework with adaptive sparse global attention guided by adaptive sparsity selection to capture global relationships across frames and frame attention to aggregate local details within each frame. In the adaptive sparse global attention, TurboVGGT adaptively learns representative tokens with varying sparsity levels for global geometry modeling, considering that token importance varies across frames, attention layers operate tokens at different levels of abstraction, and global dependencies rely on structurally informative regions. Extensive experiments on multiple 3D reconstruction benchmarks demonstrate that TurboVGGT achieves fast multi-view reconstruction while maintaining competitive reconstruction quality compared with state-of-the-art methods. Project page: this https URL.

---


### 98. [Guided Diffusion Sampling for Precipitation Forecast Interventions](https://arxiv.org/abs/2605.14317)

**<font color=#1a73e8>作者：</font>** Ayumu Ueyama, Kazuhiko Kawamoto, Hiroshi Kera  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Extreme precipitation causes severe societal and economic damage, and weather control has long been discussed as a potential mitigation strategy. However, to the best of our knowledge, perturbation-based interventions for weather control using data-driven weather forecasting models have not yet been explored. While adversarial attacks also generate perturbations that alter forecasts, they aim to exploit model artifacts and do not account for physical plausibility. In this paper, we propose a gradient-based guidance framework for precipitation-reduction interventions through diffusion sampling in diffusion-based weather forecasting models. Instead of directly perturbing atmospheric states, our method steers the diffusion sampling trajectory, enabling precipitation reduction while maintaining consistency with the atmospheric distribution. To assess physical plausibility, we evaluate from three perspectives: (i) vertical and variable-wise perturbation profiles, (ii) latent-space trajectory deviation, and (iii) cross-model transferability. Experiments on extreme precipitation events from WeatherBench2 demonstrate that our method achieves effective precipitation reduction while yielding more physically plausible interventions than adversarial perturbations.

---


### 99. [Semantic Feature Segmentation for Interpretable Predictive Maintenance in Complex Systems](https://arxiv.org/abs/2605.14318)

**<font color=#1a73e8>作者：</font>** Emilio Mastriani, Alessandro Costa, Federico Incardona 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Predictive maintenance in complex systems is often complicated by the heterogeneity and redundancy of monitored variables,which can obscure fault-relevant information and reduce model interpretability. This work proposes a semantic feature segmentation framework that decomposes the monitored feature space into a canonical component,expected to retain the dominant predictive information, and a residual component containing structurally peripheral signals. The segmentation is defined through domain informed criteria and sets up monitoring variables into functional groups reflecting operational mechanisms such as throughput,latency,pressure,network activity,and structural state. To evaluate the effectiveness of this decomposition, we adopt a predictive perspective in which expected predictive risk is used as an operational proxy for task-relevant information. Experimental results obtained through time-aware cross-validation show that the canonical space consistently achieves lower predictive risk than the residual space across multiple temporal configurations, indicating that the semantic segmentation concentrates the most relevant information for fault anticipation. In addition, the canonical segments exhibit significantly stronger intra-segment coherence than inter-segment dependence, and this structural organization remains stable after redundancy reduction. When compared with the full feature space and with a Principal Component Analysis (PCA) representation, the canonical space carries out comparable predictive performance and furthermore preserves the semantic meaning of the original variables. These findings suggest that semantic feature segmentation provides an interpretable and information-preserving decomposition of monitoring signals, enabling competitive predictive performance without sacrificing the operational interpretability required in predictive maintenance applications.

---


### 100. [Are Agents Ready to Teach? A Multi-Stage Benchmark for Real-World Teaching Workflows](https://arxiv.org/abs/2605.14322)

**<font color=#1a73e8>作者：</font>** Zixin Chen, Peng Liu, Rui Sheng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language agents are increasingly deployed in complex professional workflows, with tutoring emerging as a particularly high-stakes capability that remains largely unmeasured in existing benchmarks. Effective tutor agents require more than producing correct answers or executing accurate tool calls: a robust tutor must diagnose learner state, adapt support over time, make pedagogically justified decisions grounded in educational evidence, and execute interventions within realistic learning-management systems. We introduce EduAgentBench, a source-grounded benchmark for holistically evaluating tutor agents across the full scope of teaching work. It contains 150 quality-controlled tasks across three capability surfaces: professional pedagogical judgment, situated multi-turn tutoring, and Canvas-style teaching workflow completion. Tasks are constructed through a pedagogical-insight-driven pipeline and evaluated with complementary verification signals and human review. Across a comprehensive evaluation of frontier models, our findings reveal that current models are generally capable of bounded pedagogical judgment, but still fall short of professional teaching standards in situated tutoring and autonomous teaching-workflow execution. To our knowledge, EduAgentBench is the first theory-grounded and realistic benchmark for evaluating the holistic teaching capability of tutor agents, providing a measurement foundation for developing future tutor agents that can support realistic teaching work.

---


> [!TIP]
> 当前位于：**51-100**（第 2/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-337](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
