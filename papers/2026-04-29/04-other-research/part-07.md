# 📦 其他研究 | 2026年04月29日

> 本类共 **437** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-350**（第 7/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-437](./part-09.md)

---

### 301. [PeeriScope: A Multi-Faceted Framework for Evaluating Peer Review Quality](https://arxiv.org/abs/2604.24071)

**<font color=#1a73e8>作者：</font>** Sajad Ebrahimi, Soroush Sadeghian, Ali Ghorbanpour 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The increasing scale and variability of peer review in scholarly venues has created an urgent need for systematic, interpretable, and extensible tools to assess review quality. We present PeeriScope, a modular platform that integrates structured features, rubric-guided large language model assessments, and supervised prediction to evaluate peer review quality along multiple dimensions. Designed for openness and integration, PeeriScope provides both a public interface and a documented API, supporting practical deployment and research extensibility. The demonstration illustrates its use for reviewer self-assessment, editorial triage, and large-scale auditing, and it enables the continued development of quality evaluation methods within scientific peer review. PeeriScope is available both as a live demo at this https URL and via API services at this https URL.

---


### 302. [FreeScale: Distributed Training for Sequence Recommendation Models with Minimal Scaling Cost](https://arxiv.org/abs/2604.24073)

**<font color=#1a73e8>作者：</font>** Chenhao Feng, Haoli Zhang, Shakhzod Ali-Zade 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern industrial Deep Learning Recommendation Models typically extract user preferences through the analysis of sequential interaction histories, subsequently generating predictions based on these derived interests. The inherent heterogeneity in data characteristics frequently result in substantial under-utilization of computational resources during large-scale training, primarily due to computational bubbles caused by severe stragglers and slow blocking communications. This paper introduces FreeScale, a solution designed to (1) mitigate the straggler problem through meticulously load balanced input samples (2) minimize the blocking communication by overlapping prioritized embedding communications with computations (3) resolve the GPU resource competition during computation and communication overlapping by communicating through SM-Free techniques. Empirical evaluation demonstrates that FreeScale achieves up to 90.3% reduction in computational bubbles when applied to real-world workloads running on 256 H100 GPUs.

---


### 303. [How Sensitive Are Safety Benchmarks to Judge Configuration Choices?](https://arxiv.org/abs/2604.24074)

**<font color=#1a73e8>作者：</font>** Xinran Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Safety benchmarks such as HarmBench rely on LLM judges to classify model responses as harmful or safe, yet the judge configuration, namely the combination of judge model and judge prompt, is typically treated as a fixed implementation detail. We show this assumption is problematic. Using a 2 x 2 x 3 factorial design, we construct 12 judge prompt variants along two axes, evaluation structure and instruction framing, and apply them using a single judge model, Claude Sonnet 4-6, producing 28,812 judgments over six target models and 400 HarmBench behaviors. We find that prompt wording alone, holding the judge model fixed, shifts measured harmful-response rates by up to 24.2 percentage points, with even within-condition surface rewording causing swings of up to 20.1 percentage points. Model safety rankings are moderately unstable, with mean Kendall tau = 0.89, and category-level sensitivity ranges from 39.6 percentage points for copyright to 0 percentage points for harassment. A supplementary multi-judge experiment using three judge models shows that judge-model choice adds further variance. Our results demonstrate that judge prompt wording is a substantial, previously under-examined source of measurement variance in safety benchmarking.

---


### 304. [Explaining Temporal Graph Predictions With Shapley Values](https://arxiv.org/abs/2604.24078)

**<font color=#1a73e8>作者：</font>** Lea-Marie Sussek, Stefan Heindorf  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Temporal Graph Neural Networks (TGNNs) have become increasingly popular in recent years due to their superior predictive performance by combining both spatial and temporal information. However, how these models utilize the information to make predictions is rather unexplored, leading to potentially faulty or biased models. This work introduces two novel model-agnostic explainers for local explanations of TGNNs based on Shapley and Owen values. The first method, an event-level (edge-level) Shapley explainer, applies the KernelSHAP algorithm to estimate contribution scores for individual temporal events, providing interpretable descriptions for model behavior. The second, a feature-level Shapley explainer, extends this framework by decomposing event-level Shapley values into Owen values, and thereby uncovers hierarchical dependencies of the event and its features. The explainers outperform SOTA explainers on different metrics and datasets. Additionally, the Feature Explainer reveals a faulty extraction of actual timestamps of a commonly used TGAT implementation, helping to further understand performance drops on very sparse explanations.

---


### 305. [The Kerimov-Alekberli Model: An Information-Geometric Framework for Real-Time System Stability](https://arxiv.org/abs/2604.24083)

**<font color=#1a73e8>作者：</font>** Hikmat Karimov, Rahid Zahid Alekberli  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This study introduces the Kerimov-Alekberli model, a novel information-geometric framework that redefines AI safety by formally linking non-equilibrium thermodynamics to stochastic control for the ethical alignment of autonomous systems. By establishing a formal isomorphism between non-equilibrium thermodynamics and stochastic control, we define systemic anomalies as deviations from a Riemannian manifold. The model utilizes the Kullback-Leibler divergence as the primary metric, governed by a dynamic threshold derived from the Fisher Information Metric. We further ground this framework in the Landauer Principle, proving that adversarial perturbations perform measurable physical work by increasing the system's informational entropy. Validation on the NSL-KDD dataset and unmanned aerial vehicle trajectory simulations demonstrated that our model achieves effective real-time detection via the FPT trigger, with strong performance metrics (e.g., high accuracy and low FPR) on benchmark datasets. This study provides a rigorous physical foundation for AI safety, transitioning from heuristic, rule-based ethical frameworks to a thermodynamics-based stability paradigm by grounding ethical violations in quantifiable physical work and entropic information.

---


### 306. [Evaluating Cryptographic API Misuse Detectors for Go](https://arxiv.org/abs/2604.24085)

**<font color=#1a73e8>作者：</font>** Vivi Andersson, Martin Monperrus  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cryptographic API misuse represents a critical vulnerability class that undermines the security foundations of modern software. Yet, it remains largely unexplored in Go despite its dominance in security-critical infrastructure. This paper presents the first comprehensive study of cryptographic API misuse detection in Go, identifying and analyzing 4 state-of-the-art tools (CodeQL, Gopher, Gosec, and Snyk Code) and establishing a consolidated taxonomy of 14 relevant misuse classes. Through an experimental evaluation of 328 security-critical open-source Go projects, we discovered 7,473 cryptographic API misuses, providing insights into the prevalence and distribution of these vulnerabilities. Our systematic comparison reveals significant variations in misuse coverage, with immediate practical implications for security engineers and long-term implications for research in this domain.

---


### 307. [BiMol-Diff: A Unified Diffusion Framework for Molecular Generation and Captioning](https://arxiv.org/abs/2604.24089)

**<font color=#1a73e8>作者：</font>** Aditya Hemant Shahane, Anuj Kumar Sirohi, Devansh Arora 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Bridging molecular structures and natural language is essential for controllable design. Autoregressive models struggle with long-range dependencies, while standard diffusion processes apply uniform corruption across positions, which can distort structurally informative tokens. We present BiMol-Diff, a unified diffusion framework for the paired tasks of text-conditioned molecule generation and molecule captioning. Our key component is a token-aware noise schedule that assigns position-dependent corruption based on token recovery difficulty, preserving harder-to-recover substructures during the forward process. On ChEBI-20 and M3-20M, BiMol-Diff improves molecule reconstruction with a 15.4% relative gain in Exact Match and achieves strong captioning results, attaining best BLEU and BERTScore among compared baselines. These results indicate token-aware noising improves fidelity in molecular structure-language modelling.

---


### 308. [Meta-Ensemble Learning with Diverse Data Splits for Improved Respiratory Sound Classification](https://arxiv.org/abs/2604.24096)

**<font color=#1a73e8>作者：</font>** June-Woo Kim, Miika Toikkanen, Heejoon Koo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training reliable respiratory sound classification models remains challenging due to the limited size and subject diversity of datasets. Ensemble methods can improve robustness, but when base models are trained on identical data, models tend to overfit and produce highly correlated predictions, thereby reducing the effectiveness of ensembling. In this work, we investigate a meta-ensemble learning methodology that enhances prediction diversity by training base models on diverse data splits and combining their outputs through a trained meta-model. Specifically, we train base models on the ICBHI dataset using two data split settings: fixed 80-20% split and five-fold cross-validation split, under two data granularity settings: patient- and sample-level. The resulting diversity in base model predictions enables the meta-model to better generalize. Our approach achieves new state-of-the-art performance on the ICBHI benchmark, reaching a Score of 66.49% and showing improved generalization on two out-of-distribution datasets, indicating its potential applicability to real-world clinical data.

---


### 309. [SemML 2.0: Synthesizing Controllers for LTL](https://arxiv.org/abs/2604.24102)

**<font color=#1a73e8>作者：</font>** Jan Křetínský, Tobias Meggendorfer, Maximilian Prokop  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Synthesizing a reactive system from specifications given in linear temporal logic (LTL) is a classical problem, finding its applications in safety-critical systems design. These systems are typically represented using either Mealy machines or AIGER circuits. We present the second version of SemML, which outperforms all state-of-the-art tools for finding either solution. Aside from implementing the classical automata-theoretic approach, our tool utilizes partial exploration and machine-learning guidance for obtaining solutions efficiently, and numerous heuristics and improvements of classic algorithms for extracting small representations of these solutions. We evaluate our tool against the existing state-of-the-art tools (in particular Strix, LtlSynt, and the previous version of SemML) on the dataset of the synthesis competition SYNTCOMP. We show that we solve significantly more instances and do so much faster than other tools, while maintaining state-of-the-art solution quality.

---


### 310. [Fed-DLoRA: Efficient Wireless Federated Learning with Dynamic Low-Rank Adaptation](https://arxiv.org/abs/2604.24103)

**<font color=#1a73e8>作者：</font>** Huaicheng Li, Junhui Zhao, Haoyu Quan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) offers a promising distributed learning paradigm for internet of vehicles (IoV) applications. However, it faces challenges from communication overhead and dynamic environments. Model compression techniques reduce computing and communication burden yet create trade-offs between compression ratios and vehicle participation strategies. In this paper, we propose a lightweight FL algorithm named federated learning with dynamic low-rank adaptation (Fed-DLoRA), which is combined with low-rank adaptation (LoRA) to effectively reduce parameters and communication costs while enhancing training efficiency. The convergence analysis of Fed-DLoRA is conducted through stochastic gradient descent optimization coupled with singular value decomposition. This analysis establishes the theoretical relationships among LoRA rank, vehicular scheduling strategies and the model's convergence characteristics. Building on these insights, we formulate a joint optimization problem aimed at maximizing system performance. To address this problem, we propose an adaptive rank, bandwidth and vehicle selection (ARBVS) algorithm that integrates enumeration with greedy optimization strategies. The algorithm provides efficient rank selection and resource scheduling strategies for each FL communication round, thereby achieving effective performance improvements for the FL system. Experimental results demonstrate that Fed-DLoRA achieves superior performance compared to conventional federated learning approaches, exhibiting enhanced accuracy, faster convergence, and improved communication efficiency.

---


### 311. [Factual and Edit-Sensitive Graph-to-Sequence Generation via Graph-Aware Adaptive Noising](https://arxiv.org/abs/2604.24104)

**<font color=#1a73e8>作者：</font>** Aditya Hemant Shahane, Anuj Kumar Sirohi, Tanmoy Chakraborty 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fine-tuned autoregressive models for graph-to-sequence generation (G2S) often struggle with factual grounding and edit sensitivity. To tackle these issues, we propose a non-autoregressive diffusion framework that generates text by iterative refinement conditioned on an input graph, named as Diffusion Language Model for Graphs (DLM4G). By aligning graph components (entities/relations) with their corresponding sequence tokens, DLM4G employs an adaptive noising strategy. The proposed strategy uses per-token denoising error as a signal to adaptively modulate noise on entity and relation tokens, improving preservation of graph structure and enabling localized updates under graph edits. Evaluated on three datasets, DLM4G consistently outperforms competitive G2S diffusion baselines trained on identical splits across both surface-form and embedding-based metrics. DLM4G further exceeds fine-tuned autoregressive baselines up to 12x larger (e.g., T5-Large) and is competitive with zero-shot LLM transfer baselines up to 127x larger. Relative to the strongest fine-tuned PLM baseline, DLM4G improves factual grounding (FGT@0.5) by +5.16% and edit sensitivity (ESR) by +7.9%; compared to the best diffusion baseline, it yields gains of +3.75% in FGT@0.5 and +23.6% in ESR. We additionally demonstrate applicability beyond textual graphs through experiments on molecule captioning, indicating the method's generality for scientific G2S generation.

---


### 312. [SemiSAM-O1: How far can we push the boundary of annotation-efficient medical image segmentation?](https://arxiv.org/abs/2604.24109)

**<font color=#1a73e8>作者：</font>** Yichi Zhang, Le Xue, Bichun Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semi-supervised learning (SSL) has become a promising solution to alleviate the annotation burden of deep learning-based medical image segmentation models. While recent advances in foundation model-driven SSL have pushed the boundary to extremely limited annotation scenarios, they fail to maintain robust competitive performance in complex imaging modalities. In this paper, we propose SemiSAM-O1, an annotation-efficient framework using only one annotated template image for segmentation. SemiSAM-O1 extends the specialist-generalist collaborative learning framework to the extreme one-label setting by fully exploiting the foundation model's feature representation capability beyond its prompting interface. SemiSAM-O1 operates in two stages. In the first stage, the foundation model's encoder extracts dense features from all volumes, and class prototypes derived from the single annotated template are propagated to the unlabeled pool via feature similarity to produce coarse initial pseudo-labels. In the second stage, an iterative training-and-refinement loop progressively improves both the segmentation model and the pseudo-labels over multiple rounds, where each round trains the model from scratch on current pseudo-labels and generates updated predictions with voxel-wise uncertainty estimates. An uncertainty-guided refinement step further leverages the foundation model's global feature space to correct high-uncertainty regions by aggregating labels from their most similar confident neighbors, establishing a virtuous cycle of mutual improvement. Extensive experiments on a wide range of segmentation tasks across different modalities and anatomical targets demonstrate that SemiSAM-O1 significantly narrows the performance gap between one-label semi-supervised learning and full supervision, while significantly reducing the computational overhead of online foundation model inference.

---


### 313. [IRIS: Interleaved Reinforcement with Incremental Staged Curriculum for Cross-Lingual Mathematical Reasoning](https://arxiv.org/abs/2604.24114)

**<font color=#1a73e8>作者：</font>** Navya Gupta, Rishitej Reddy Vyalla, Avinash Anand 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Curriculum learning helps language models tackle complex reasoning by gradually increasing task difficulty. However, it often fails to generate consistent step-by-step reasoning, especially in multilingual and low-resource settings where cross-lingual transfer from English to Indian languages remains limited. We propose IRIS: Interleaved Reinforcement with Incremental Staged Curriculum, a two-axis framework that combines Supervised Fine-Tuning on progressively harder problems (vertical axis) with Reverse Curriculum Reinforcement Learning to reduce reliance on step-by-step guidance (horizontal axis). We design a composite reward combining correctness, step-wise alignment, continuity, and numeric incentives, optimized via Group Relative Policy Optimization (GRPO). We release CL-Math, a dataset of 29k problems with step-level annotations in English, Hindi, and Marathi. Across standard benchmarks and curated multilingual test sets, IRIS consistently improves performance, with strong results on math reasoning tasks and substantial gains in low-resource and bilingual settings, alongside modest improvements in high-resource languages.

---


### 314. [An Analysis of the Coordination Gap between Joint and Modular Learning for Job Shop Scheduling with Transportation Resources](https://arxiv.org/abs/2604.24117)

**<font color=#1a73e8>作者：</font>** Moritz Link, Jonathan Hoss, Noah Klarmann  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Efficient job-shop scheduling with transportation resources is critical for high-performance manufacturing. With the rise of "decentralized factories", multi-agent reinforcement learning has emerged as a promising approach for the combined scheduling of production and transportation tasks. Prior work has largely focused on developing novel cooperative architectures while overlooking the question of when joint training is necessary. Joint training denotes the simultaneous training of job and automatic guided vehicle scheduling agents, whereas modular training involves independently training each agent followed by post-hoc integration. In this study, we systematically investigate the conditions under which joint training is essential for optimal performance in the job-shop scheduling problem with transportation resources. Through a rigorous sensitivity analysis of resource scarcity and temporal dominance, we quantify the coordination gap -- the performance difference between these two training modalities. In our evaluation, the joint training can produce superior performance compared to the best-performing combinations of dispatching rules and modular training. However, the coordination gap advantage diminishes in bottleneck environments, particularly under severe transport and processing constraints. These findings indicate that modular training represents a viable alternative in environments where a single scheduling task dominates. Overall, our work provides practical guidance for selecting between training modalities based on environmental conditions, enabling decision-makers to optimize reinforcement learning-based scheduling performance.

---


### 315. [TopoHR: Hierarchical Centerline Representation for Cyclic Topology Reasoning in Driving Scenes with Point-to-Instance Relations](https://arxiv.org/abs/2604.24119)

**<font color=#1a73e8>作者：</font>** Yifeng Bai, Zhirong Chen, Erkang Cheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Topology reasoning is crucial for autonomous driving. Current methods primarily focus on instance-level learning for centerline detection, followed by a sequential module for topology reasoning that relies on simplified MLP layers. Moreover, they often neglect the importance of \textit{point-to-instance} (P2I) relationships in topology reasoning. To address these limitations, we present TopoHR (Topological Hierarchical Representation), a novel end-to-end framework that establishes cyclic interaction between centerline detection and topology reasoning, allowing them to iteratively enhance each other. Specifically, we introduce a hierarchical centerline representation including point queries, instance queries, and semantic representations. These multi-level features are seamlessly integrated and fused within a hierarchical centerline decoder. Furthermore, we design a hierarchical topology reasoning module that captures both fine-grained P2I relationships and global instance-to-instance (I2I) connections within a unified architecture. With these novel components, TopoHR ensures accurate and robust topology reasoning. On the OpenLane-V2 benchmark, TopoHR refreshes state-of-the-art performance with significant improvements. Notably, compared with previous best results, TopoHR achieves +3.8 in $\mathrm{DET}_{\text{l}}$, +5.4 in $\mathrm{TOP}_{\text{ll}}$ on $\text{subset_A}$ and +11.0 in $\mathrm{DET}_{\text{l}}$, +7.9 in $\mathrm{TOP}_{\text{ll}}$ on $\text{subset_B}$, validating the effectiveness of the proposed components. The code will be shared publicly at this https URL.

---


### 316. [FDIM: A Feature-distance-based Generic Video Quality Metric for Versatile Codecs](https://arxiv.org/abs/2604.24123)

**<font color=#1a73e8>作者：</font>** Jiayi Wang, Lichun Zhang, Xiaoqi Zhuang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video technology is advancing toward Ultra High Definition (UHD) and High Dynamic Range (HDR), which intensifies the need for higher compression efficiency for these high-specification videos. Beyond advances in traditional codecs, neural video codecs (NVCs) have attracted significant research attention and have evolved rapidly over the past few years. The coding artifacts of NVCs often exhibit content-varying and generative characteristics, which differ from those of conventional codecs and are challenging for traditional video quality assessment (VQA) methods to capture. Therefore, VQA metrics are required to generalize across different codecs, content types, and dynamic ranges to better support video codec research and evaluation. In this paper, we propose FDIM, a feature-distance-based generic video quality metric for both traditional and neural video codecs across SDR and HDR formats. FDIM employs a hybrid architecture that integrates deep and hand-crafted features. The deep feature component learns multi-scale representations to capture distortions ranging from structural and textural fidelity degradation to high-level semantic deviations, while the hand-crafted feature component provides stable complementary cues to improve overall generalization. We trained FDIM on a large-scale subjective quality assessment dataset (DCVQA) consisting of over 16k video sequences encoded by traditional block-based hybrid video codecs and end-to-end perceptually optimized neural video codecs. Extensive experiments on ten SDR/HDR VQA datasets containing diverse, previously unseen codecs demonstrate that FDIM achieves strong generalization and high correlation with subjective assessment. The source code for FDIM and the DCVQA validation set will be released at this https URL.

---


### 317. [Psychologically-Grounded Graph Modeling for Interpretable Depression Detection](https://arxiv.org/abs/2604.24126)

**<font color=#1a73e8>作者：</font>** Rishitej Reddy Vyalla, Kritarth Prasad, Avinash Anand 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic depression detection from conversational interactions holds significant promise for scalable screening but remains hindered by severe data scarcity and a lack of clinical interpretability. Existing approaches typically rely on black-box deep learning architectures that struggle to model the subtle, temporal evolution of depressive symptoms or account for participant-specific heterogeneity. In this work, we propose PsyGAT (Psychological Graph Attention Network), a psychologically grounded framework that models conversational sessions as dynamic temporal graphs. We introduce Psychological Expression Units (PEUs) to explicitly encode utterance-level clinical evidence, structuring the session graph to capture transitions in psychological states rather than mere semantic dependencies. To address the critical class imbalance in depression datasets, we employ clinically approved persona-based data augmentation, enable robust model learning. Additionally, we integrate session-level personality context directly into the graph structure to disentangle trait-based behavior from acute depressive symptoms. PsyGAT achieves state-of-the-art performance, surpassing both strong graph-based baselines and closed-source LLMs like GPT-5, achieving 89.99 and 71.37 Macro F1 scores in DAIC-WoZ and E-DAIC, respectively. We further introduce Causal-PsyGAT, an interpretability module that identifies symptom triggers. Experiments show a 20% improvement in MRR for identifying causal indicators, effectively bridging the gap between depression monitoring and clinical explainability. The full augmented dataset is publicly available at this https URL.

---


### 318. [Detecting Avalanche Effect in Adversarial Settings: Spotting the Encryption Loops in Ransomware](https://arxiv.org/abs/2604.24131)

**<font color=#1a73e8>作者：</font>** Nanqing Luo, Xusheng Li, Haizhou Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Spotting encryption loops in binary-only ransomware is a critical reverse engineering task. Since the existence of avalanche effect, an intrinsic characteristic of any secure encryption algorithms, is unavoidable during a victim data encryption attack, it is a very promising direction to spot encryption loops through avalanche effect detection. Unfortunately, no existing work in this direction ensures that the being-checked effect is the avalanche effect itself. Although CipherXRay is inspired by avalanche effect, it only checks whether a "ripple effect" (i.e., a necessary but non-sufficient condition) of avalanche effect exists, allowing a straightforward counterattack to succeed. In this work, we present a new approach that checks the avalanche effect itself. Because the detection is conducted in adversarial settings (e.g., the ransomware author may obfuscate the code), a viable approach must tolerate inaccurate input \& output identification and must be resilient to adversarial evasion. These challenges are addressed by a novel record-and-replay detection mechanism that takes advantage of the statistical guarantees provided by the Shapiro-Wilk normality test. The experimental results show that our approach achieves 0.0\% false negative rate and 1.1\% false positive rate. When our tool is employed to reverse engineer real-world ransomware samples, it succeeds in analyzing all the ransomware samples selected from ten representative families.

---


### 319. [Bridging Restoration and Generation Manifolds in One-Step Diffusion for Real-World Super-Resolution](https://arxiv.org/abs/2604.24136)

**<font color=#1a73e8>作者：</font>** Shyang-En Weng, Yi-Cheng Liao, Yu-Syuan Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained diffusion models have revolutionized real-world image super-resolution (Real-ISR) but suffer from computational bottlenecks due to iterative sampling. Recent single-step distillation accelerates inference but faces a stark perception-distortion trade-off due to rigid timestep initialization, distributional trajectory mismatches, and fragile stochastic modulation. To address this, we present Adaptive Inversion and Degradation-aware Sampling for Real-ISR (IDaS-SR), a one-step framework bridging the deterministic restoration and stochastic generation manifolds. At its core, the Manifold Inversion Noise Estimator (MINE) resolves these initialization and trajectory mismatches by predicting a severity-aware timestep and inversion noise, precisely anchoring low-quality latents onto the diffusion trajectory. Furthermore, to mitigate fragile stochastic modulation, we propose CHARIOT, a continuous generative steering mechanism. By rescheduling trajectories and interpolating noise, it enables explicit navigation of the perception-distortion boundary without compromising structural priors. Extensive experiments demonstrate that IDaS-SR outperforms state-of-the-art methods, seamlessly transitioning from a rigorous structural restorer to a sophisticated texture hallucinator in a single inference step.

---


### 320. [Machine-Learning-Based Classification of Radio Frequency Building Loss](https://arxiv.org/abs/2604.24143)

**<font color=#1a73e8>作者：</font>** Jiayi Tan, Neelabhro Roy, James Gross 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate modeling of outdoor-to-indoor (O2I) and indoor-to-indoor (I2I) signal loss is important for improving indoor wireless network performance in dense urban areas. Traditional on-site measurements are expensive, time-consuming, and difficult to conduct across wide regions. Real-world datasets also tend to be noisy and imbalanced, which makes signal loss prediction challenging. This study presents a machine learning framework for classifying radio frequency (RF) building loss. The framework combines passively collected, crowdsourced user equipment (UE) data from 3GPP-compliant networks with public building information. We evaluated Random Forest, XGBoost, LightGBM, and a voting classifier using both supervised (SL) and semi-supervised learning (SSL). Compared to SL-only inference, the proposed SL and SSL framework improved both prediction accuracy and confidence under identical data constraints, achieving up to 12.6% relative accuracy gain for O2I loss and 3.4% for I2I loss, while reducing prediction entropy by up to 8.4%. Among the evaluated models, SSL XGBoost provided the most confident O2I loss classification, whereas SSL LightGBM achieved the best performance for I2I loss. These results demonstrate that the proposed approach provides a practical, data-driven alternative to traditional models, with promising potential to support better network planning and indoor coverage optimization.

---


### 321. [6thGrid-Net: Unified Remote Sensing Image Dehazing Based on Color Restoration and Edge-Preserving](https://arxiv.org/abs/2604.24149)

**<font color=#1a73e8>作者：</font>** Runci Bai, Kui Jiang, Xiang Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing images are frequently degraded by adverse weather conditions, particularly clouds and haze, which severely impair downstream applications. Existing restoration methods typically rely on computationally heavy architectures or sequential pipelines (e.g., detail enhancement followed by color rendition) that suffer from mutual interference and artifact accumulation. Furthermore, recent unified grid-based approaches utilize fixed, isotropic interpolation kernels, neglecting the intrinsic low-dimensional manifold of natural images and inevitably causing edge blur. To address these limitations, we propose 6th Grid-Net, a highly efficient and unified remote sensing image restoration framework tailored for resource-constrained edge devices. Specifically, we construct a novel six-dimensional fusion tensor that seamlessly integrates the color rendition capabilities of 3D LUTs with the spatial-luminance detail preservation of bilateral grids. To overcome the drawbacks of standard trilinear interpolation, we introduce a manifold-adaptive high-dimensional sampling mechanism. This mechanism dynamically adjusts the interpolation kernel based on local edge orientation, texture strength, and color similarity, enabling simultaneous global color stylization and local edge refinement in a single forward pass. Additionally, an edge-aware grid smoothing constraint and dynamic quantization are incorporated to suppress ghosting artifacts and significantly compress the model size. Extensive experiments on multiple benchmark datasets demonstrate that 6th Grid-Net achieves state-of-the-art restoration quality across various degradation scenarios.

---


### 322. [Right-to-Act: A Pre-Execution Non-Compensatory Decision Protocol for AI Systems](https://arxiv.org/abs/2604.24153)

**<font color=#1a73e8>作者：</font>** Gadi Lavi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current AI systems increasingly operate in contexts where their outputs directly trigger real-world actions. Most existing approaches to AI safety, risk management, and governance focus on post-hoc validation, probabilistic risk estimation, or certification of model behavior. However, these approaches implicitly assume that once a decision is produced, it is eligible for execution. In this work, we introduce the Right-to-Act protocol, a deterministic, non-compensatory pre-execution decision layer that evaluates whether an AI-generated decision is permitted to be realized at all. Unlike compensatory systems, where high-confidence signals can override failed conditions, the proposed framework enforces strict structural constraints: if any required condition is unmet, execution is halted or deferred. We formalize the distinction between compensatory and non-compensatory decision regimes and define a pre-execution legitimacy boundary. Through a scenario-based case study, we demonstrate how identical AI outputs can lead to divergent outcomes when evaluated under a Right-to-Act protocol, preserving reversibility and preventing premature or irreversible actions. The proposed approach reframes AI control from optimizing decisions to governing their admissibility, introducing a protocol-level abstraction that operates independently of model architecture or training methodology.

---


### 323. [Progressive Approximation in Deep Residual Networks: Theory and Validation](https://arxiv.org/abs/2604.24154)

**<font color=#1a73e8>作者：</font>** Wei Wang, Xiao-Yong Wei, Qing Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Universal Approximation Theorem (UAT) guarantees universal function approximation but does not explain how residual models distribute approximation across layers. We reframe residual networks as a layer-wise approximation process that builds an approximation trajectory from input to target, and prove the existence of progressive trajectories where error decreases monotonically with depth. It reveals that residual networks can implement structured, step-by-step refinement rather than end-to-end (E2E) black-box mapping. Building on this, we propose Layer-wise Progressive Approximation (LPA), a theoretically grounded training principle that explicitly aligns each layer with its residual target to realize such trajectories. LPA is architecture-agnostic: we observe progressive behavior in residual FNNs, ResNets, and Transformers across tasks including complex surface fitting, image classification, and NLP with LLMs for generation and classification. Crucially, this enables ``train once, use $N$ models": a single network yields useful predictions at every depth, supporting efficient shallow inference without retraining. Our work unifies approximation theory with practical deep learning, providing a new lens on representation learning and a flexible framework for multi-depth deployment. The source code will be released unpon acceptance at https://(open\_upon\_acceptance).

---


### 324. [Robust Deepfake Detection, NTIRE 2026 Challenge: Report](https://arxiv.org/abs/2604.24163)

**<font color=#1a73e8>作者：</font>** Benedikt Hopf, Radu Timofte, Chenfan Qu 等 57 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robustness is a long-overlooked problem in deepfake detection. However, detection performance is nearly worthless in the real world if it suffers under exposure to even slight image degradation. In addition to weaker degradations that can accidentally occur in the image processing pipeline, there is another risk of malicious deepfakes that specifically introduce degradations, purposefully exploiting the detector's weaknesses in that regard. Here, we present an overview of the NTIRE 2026 Robust Deepfake Detection Challenge, which specifically addresses that problem. Participants were tasked with building a detector that would later be tested on an unknown test-set, which included both common and uncommon degradations of various strengths. With a total number of 337 participants and 57 submissions to the final leaderboard, the first edition of the challenge was well received. To ensure the reliability of the results, participants were given only 24h to complete the test run with no labels provided, limiting the possibility of training on the test data. Furthermore, the top solutions were scored on a private test-set to detect any such overfitting. This report presents the competition setting, dataset preparation, as well as details and performance of methods. Top methods rely on large foundation models, ensembles, and degradation training to combine generality and robustness.

---


### 325. [PEPS: Positional Encoding Projected Sampling -- Extended](https://arxiv.org/abs/2604.24167)

**<font color=#1a73e8>作者：</font>** Guillaume Perez, Janarbek Matai, Takahiro Harada  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Implicit neural representations (INRs) are increasingly being used as tools to map coordinates to signals, encompassing applications from neural fields to texture compression, shape representations, and beyond. Most INR methods are based on using high-dimensional projections of the initial coordinates through encoders such as grid or positional encoding. Nevertheless, positional encoding is often insufficient and grids, as we show in this paper, require high resolution for being able to learn. In this paper, we demonstrate that positional encoding can be used not only as a high-dimensional embedding but also decomposed as a series of meaningful points. We propose the Positional Encoding Projected Sampling, where we treat the projection of the original coordinate at each frequency as a point of interest. We describe the motion of each point with respect to the frequencies and show that it follows a unique pattern. Finally, we use the unique motion of each point as a basis decomposition for doing learned positional encoding using grids. We prove, using three competitive applications; image representation, texture compression, and signed distance function; that the proposed approach outperforms the current state of the art methods, and often requires 25\% less parameters for equivalent reconstruction error or rendering.

---


### 326. [PointTransformerX:Portable and Efficient 3D Point Cloud Processing without Sparse Algorithms](https://arxiv.org/abs/2604.24169)

**<font color=#1a73e8>作者：</font>** Laurenz Reichardt, Nikolas Ebert, Oliver Wasenmüller  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D point cloud perception remains tightly coupled to custom CUDA operators for spatial operations, limiting portability and efficiency on non-NVIDIA, AMD, and embedded hardware. We introduce PointTransformerX (PTX), a fully PyTorch-native vision transformer backbone for 3D point clouds, removing all custom CUDA operators and external libraries while retaining competitive accuracy. PTX introduces 3D-GS-RoPE, a rotary positional embedding that encodes 3D spatial relationships directly in self-attention without neighborhood construction, and further replaces sparse convolutional patch embedding with a linear projection. PTX explores inference-time scaling of attention windows to improve accuracy without retraining. With a redesigned feed-forward network, PTX achieves 98.7\% of PointTransformer V3's accuracy on ScanNet with 79.2\% fewer parameters and executing 1.6\times faster while requiring just 253 MB memory. PTX runs natively on NVIDIA GPUs, AMD GPUs (ROCm), and CPUs, providing an efficient and portable foundation for point cloud perception.

---


### 327. [Credal Concept Bottleneck Models for Epistemic-Aleatoric Uncertainty Decomposition](https://arxiv.org/abs/2604.24170)

**<font color=#1a73e8>作者：</font>** Tanmoy Mukherjee, Thomas Bailleux, Pierre Marquis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Concept Bottleneck Models (CBMs) predict through human-interpretable concepts, but they typically output point concept probabilities that conflate epistemic uncertainty (reducible model underspecification) with aleatoric uncertainty (irreducible input ambiguity). This makes concept-level uncertainty hard to interpret and, more importantly, hard to act upon. We introduce CREDENCE (Credal Ensemble Concept Estimation), a CBM framework that decomposes concept uncertainty by construction. CREDENCE represents each concept as a credal prediction (a probability interval), derives epistemic uncertainty from disagreement across diverse concept heads, and estimates aleatoric uncertainty via a dedicated ambiguity output trained to match annotator disagreement when available. The resulting signals support prescriptive decisions: automate low-uncertainty cases, prioritize data collection for high-epistemic cases, route high-aleatoric cases to human review, and abstain when both are high. Across several tasks, we show that epistemic uncertainty is positively associated with prediction errors, whereas aleatoric uncertainty closely tracks annotator disagreement, providing guidance beyond error correlation. Our implementation is available at the following link: this https URL

---


### 328. [Explanation Quality Assessment as Ranking with Listwise Rewards](https://arxiv.org/abs/2604.24176)

**<font color=#1a73e8>作者：</font>** Thomas Bailleux, Tanmoy Mukherjee, Emmanuel Lonca 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We reformulate explanation quality assessment as a ranking problem rather than a generation problem. Instead of optimizing models to produce a single "best" explanation token-by-token, we train reward models to discriminate among multiple candidate explanations and learn their relative quality. Concretely, we construct per-instance candidate sets with graded quality levels and train listwise and pairwise ranking models (ListNet, LambdaRank, RankNet) to preserve ordinal structure and avoid score compression typical of pointwise regression or binary preference objectives. We observe three findings: First, ranking losses consistently outperform regression on score separation across all domains tested. Second, the optimal ranking loss depends on data characteristics: listwise objectives excel with well-separated quality tiers, while pairwise methods are more robust to noisy natural annotations. Third, when trained on carefully curated and well-structured data, small encoder models can match models that are orders of magnitude larger, suggesting that data quality matters more than model scale. Finally, when used as rewards in policy optimization, ranking-based scores enable stable convergence in settings where regression-based rewards fail entirely. Code and data are available at: this https URL

---


### 329. [Dynamic Cyber Ranges](https://arxiv.org/abs/2604.24184)

**<font color=#1a73e8>作者：</font>** Víctor Mayoral-Vilches, María Sanz-Gómez, Francesco Balassone 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As LLM-driven agents advance in cybersecurity, Jeopardy CTF benchmarks are approaching saturation and cyber ranges, the natural next evaluation frontier, offer diminishing resistance under their current static design. We validate this observation by deploying an LLM-driven Advanced Persistent Threat (APT) agent across three tiers of increasingly realistic infrastructure (PRO Labs, MHBench, military-grade CYBER RANGES). To counteract this trend, we propose Dynamic Cyber Ranges: cyber range environments augmented with LLM-driven Defender agents that harden infrastructure, monitor for intrusions, and respond in real time. Across evaluated scenarios, Defender agents reduce attacker success to 0-55%, achieving complete prevention on multiple configurations. Since attacker and defender agents draw from the same underlying model capabilities, Dynamic Cyber Ranges preserve evaluation headroom as models improve. Notably, a smaller, specialized on-premise model (alias2-mini) matched the frontier model's defensive outcomes on multiple scenarios under identical, untuned prompts, and detected the attacker 10x faster on a complex enterprise scenario, suggesting that privacy-preserving on-premise models can serve as competent defenders against frontier-class attackers. The experiments further surface emergent agent behaviors, including scope expansion and prompt exfiltration, with implications for AI benchmark integrity and agentic system design.

---


### 330. [Multivariate Gaussian NeRF for Wide Field-of-View Ultrasound Reconstruction](https://arxiv.org/abs/2604.24187)

**<font color=#1a73e8>作者：</font>** Patris Valera, Magdalena Wysocki, Felix Duelmer 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Wide Field-of-View (WFoV) reconstruction enhances 3D ultrasound imaging by providing valuable anatomical context for segmentation models and visualization. Clinical ultrasound volumes are predominantly acquired using convex probes, which generate expanding, diverging acoustic beams to maximize anatomical coverage. Stitching these sweeps together traditionally introduces significant compounding artifacts and aliasing due to depth-dependent resolution changes. Here, we introduce Ultra-Wide-NeRF, a Multivariate 3D Gaussian (MVG) NeRF-based method for WFoV ultrasound reconstruction. By explicitly modeling the complex beam geometry using distance-dependent convex volumetric sampling and anisotropic 3D Gaussians, our method inherently mitigates these compounding artifacts and provides anti-aliasing. Beyond simply reconstructing a static 3D grid, our NeRF-based approach yields a continuous neural representation of the tissue, enabling the synthesis of high-fidelity novel views from arbitrary virtual trajectories. We validate Ultra-Wide-NeRF for intracardiac echocardiography on phantom and porcine datasets, demonstrating that our method expands the spatial context important in intraoperative navigation. Code will be open-sourced upon publication.

---


### 331. [Omni-o3: Deep Nested Omnimodal Deduction for Deliberative Audio-Visual Reasoning](https://arxiv.org/abs/2604.24191)

**<font color=#1a73e8>作者：</font>** Zhicheng Zhang, Wentao Gu, Weicheng Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Omnimodal understanding entails a massive, highly redundant search space of cross-modal interactions, demanding focused and deliberative reasoning. Current reasoning paradigms rely on either sequential step-by-step generation or parallel sample-by-sample rollouts, leading to isolated reasoning trajectories. This inability to share promising intermediate paths severely limits exploration efficiency and causes compounding errors in complex audio-visual tasks. To break this bottleneck, we introduce Omni-o3, a novel framework driven by a deep nested deduction policy. By formulating reasoning as a dynamic recursive search, Omni-o3 inherently shares reasoning prefixes across branches, enabling the iterative execution of four atomic cognitive actions: expansion, selection, simulation, and backpropagation. To empower this framework, we propose a robust two-stage training paradigm: (1) cold-start supervised fine-tuning on 101K high-quality, long-chain trajectories distilled from 3.5M diverse omnimodal samples, enabling necessary recursive search patterns; and (2) nested group rollout-driven exploratory reinforcement learning on 18K complex multi-turn samples, explicitly guided by a novel multi-step reward model to stimulate deep nested reasoning. Extensive experiments demonstrate that Omni-o3 achieves competitive performance across 11 benchmarks, unlocking advanced capabilities in comprehensive audio-visual, visual-centric, and audio-centric reasoning tasks.

---


### 332. [Computer Vision-Based Early Detection of Container Loss at Sea](https://arxiv.org/abs/2604.24193)

**<font color=#1a73e8>作者：</font>** Vishakha Lall, Capt. Stanley S Pinto, Capt. Chu Xing Peng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Containerised shipping underpins global trade, yet container loss at sea remains a persistent safety, environmental, and economic challenge. Despite compliance with Cargo Securing Manuals, dynamic maritime conditions such as vessel motion, wind loading, and severe sea states can progressively destabilise container stacks, leading to overboard losses. With the new International Maritime Organisation's (IMO) mandatory reporting requirements for lost containers, there is an urgent need for a reliable, evidence-based early detection solution for destabilised containers. This study showcases a low-cost, retrofittable computer vision-based system for early detection of destabilised containers using existing onboard cameras. The framework integrates object segmentation to isolate container stacks, temporal object tracking using optical flow and individual objects' residual motion extraction to quantify relative movement. Experimental evaluation on real onboard ship footage demonstrates that the proposed pipeline effectively isolates container-level motion under challenging conditions of varying sea states and visibility conditions. By enabling early alerts for crew intervention and navigational adjustment, the proposed approach enhances cargo safety, operational resilience, and regulatory compliance.

---


### 333. [Seeing Is No Longer Believing: Frontier Image Generation Models, Synthetic Visual Evidence, and Real-World Risk](https://arxiv.org/abs/2604.24197)

**<font color=#1a73e8>作者：</font>** Shuai Wu, Xue Li, Yanna Feng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Frontier image generation has moved from artistic synthesis toward synthetic visual evidence. Systems such as GPT Image 2, Nano Banana Pro, Nano Banana 2, Grok Imagine, Qwen Image 2.0 Pro, and Seedream 5.0 Lite combine photorealistic rendering, readable typography, reference consistency, editing control, and in several cases reasoning or search-grounded image construction. These capabilities create large benefits for design, education, accessibility, and communication, yet they also weaken one of society's most common trust shortcuts: the belief that a plausible picture is a reliable record. This paper provides a source-grounded technical and policy analysis of synthetic visual risk. We first summarize the public capabilities of recent image models, then analyze public incidents involving fake crisis images, celebrity and public-figure imagery, medical scans, forged-looking documents, synthetic screenshots, phishing assets, and market-moving rumors. We introduce a capability-weighted risk framework that links model affordances to real-world harm in finance, medicine, news, law, emergency response, identity verification, and civic discourse. Our findings show that risk is driven less by photorealism alone than by the convergence of realism, legible text, identity persistence, fast iteration, and distribution context. We argue for layered control: model-side restrictions, cryptographic provenance, visible labeling, platform friction, sector-grade verification, and incident response. The paper closes with practical recommendations for model providers, platforms, newsrooms, financial institutions, healthcare systems, legal organizations, regulators, and ordinary users.

---


### 334. [CMGL: Confidence-guided Multi-omics Graph Learning for Cancer Subtype Classification](https://arxiv.org/abs/2604.24201)

**<font color=#1a73e8>作者：</font>** Boyang Fan, Hengchuang Yin, Siyu Yi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Motivation: Multi-omics integration can improve cancer subtyping, but modality informativeness and noise vary across cancer types and patients. Existing graph-based methods optimize modality weights jointly with the classification objective and therefore lack independent reliability estimates, so low-quality omics distort patient similarity graphs and amplify noise through message passing.
Results: We propose CMGL, a two-stage framework that estimates per-sample modality reliability through evidential deep learning and uses the frozen confidence scores to guide cross-omics fusion and graph construction. On four MLOmics cancer-subtype tasks and the 32-class pan-cancer task, CMGL consistently improves over the strongest baseline, surpassing it by 4.03% in average accuracy on the four single-cancer tasks. Its representations recover the PAM50 intrinsic subtypes of breast invasive carcinoma (BRCA), and the BRCA-trained model transfers without fine-tuning to kidney renal clear cell carcinoma (KIRC), stratifying patients into prognostically distinct groups.

---


### 335. [Converging Zero Trust and IoT Security: A Multivocal Literature Review](https://arxiv.org/abs/2604.24205)

**<font color=#1a73e8>作者：</font>** Mariam Wehbe, Laurent Bobelin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The convergence of Internet of Things (IoT) security and Zero Trust (ZT) principles is a trending topic, demanding a comprehensive, multi-perspective analysis. We present the first multivocal literature review (MLR) on this topic, combining 68 academic and 36 industrial studies. This comprehensive review identifies two complementary yet divergent perspectives: academia focuses on IoT compliance with ZT principles through IoT modifications, while industry prioritizes practical integration within existing ZT frameworks guided by NIST standards. The analysis reveals critical research gaps in socio-technical understanding, cost-benefit evaluation, and interdisciplinary collaboration, highlighting these as key directions for future research.

---


### 336. [Adaptive ToR: Complexity-Aware Tree-Based Retrieval for Pareto-Optimal Multi-Intent NLU](https://arxiv.org/abs/2604.24219)

**<font color=#1a73e8>作者：</font>** Hee-Kyong Yoo, Wonbae Kim, Hyocheol Ahn  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-intent natural language understanding requires retrieval systems that simultaneously achieve high accuracy and computational efficiency, yet existing approaches apply either uniform single-step retrieval that compromises recall or fixed-depth hierarchical decomposition that introduces excessive latency regardless of query complexity. This paper proposes Adaptive Tree-of-Retrieval (Adaptive ToR), a complexity-aware retrieval architecture that dynamically configures retrieval topology based on query characteristics. The system integrates four components: (1) a Query Tree Classifier computing a Query Complexity Index from weighted linguistic signals to route queries to either a rapid single-step path or an adaptive-depth hierarchical path; (2) a Tree-Based Retrieval module that recursively decomposes complex queries into focused sub-queries calibrated to predicted complexity; (3) an Adaptive Pruning Module employing two-stage filtering combining quantitative similarity gating with semantic relevance evaluation to suppress exponential node growth; and (4) a Retrieval Reranking Layer featuring a deduplicator-first pipeline and global LLM rescoring for production efficiency. Evaluation on the NLU++ benchmark (2,693 multi-intent queries across Banking and Hotel domains) yields 29.07% Subset Accuracy and 71.79% Micro-F1, a 9.7% relative improvement over fixed-depth baselines, while reducing latency by 37.6%, LLM invocations by 43.0%, and token consumption by 9.8%. Depth-wise analysis reveals that 26.92% of queries resolve within three seconds (2.45s mean latency) via single-step routing (d=0: 37.9% Subset Accuracy, 74.8% Micro-F1), while token consumption scales by 4.9x across depths, validating complexity-aware resource allocation and establishing Pareto-optimal balance across accuracy, latency, and computational efficiency.

---


### 337. [IMPA-Net: Meteorology-Aware Multi-Scale Attention and Dynamic Loss for Extreme Convective Radar Nowcasting](https://arxiv.org/abs/2604.24224)

**<font color=#1a73e8>作者：</font>** Haofei Cui, Guangxin He, Juanzhen Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Short-range prediction of convective precipitation from weather radar observations is essential for severe weather warnings. However, deep learning models trained with pixel-wise error metrics tend to produce overly smooth forecasts that suppress intense echoes critical for hazard detection. This issue is exacerbated by insufficient multi-scale feature interaction and suboptimal fusion of heterogeneous geophysical inputs. We propose IMPA-Net (Integrated Multi-scale Predictive Attention Network), a deterministic 0-2 hour nowcasting framework that addresses these limitations through meteorologically-informed designs at the input, architecture, and loss function levels. A parameter-free Spatial Mixer reorganizes heterogeneous input channels at the mesoscale-$\gamma$ neighborhood (~2 km) via deterministic channel permutation, providing a structured cross-field prior. An integrated multi-scale predictive attention module serves as the spatiotemporal translator, capturing dynamics from mesoscale-$\beta$ to mesoscale-$\gamma$ scales. A Meteorologically-Aware Dynamic Loss employs three-level asymmetric weighting -- adapting across training epochs, storm intensity, and forecast lead time -- to counteract regression-to-the-mean. Evaluated against seven baselines on a multi-source radar dataset over eastern China, IMPA-Net raises the Heidke Skill Score at $\geq$45 dBZ from 0.049 (SimVP baseline) to 0.143 under matched settings. Relative to pySTEPS, it provides a better trade-off between severe-event detection and false-alarm control. Spectral analysis confirms preserved energy across mesoscale bands where competing methods show progressive smoothing. These improvements are shown within a single domain and convective regime; generalizability to other orographic and climatic regions remains to be tested.

---


### 338. [Radiomics- and Clinical Feature-Driven Prediction of Volumetric Response in Skull-Base Meningioma after CyberKnife Radiosurgery](https://arxiv.org/abs/2604.24230)

**<font color=#1a73e8>作者：</font>** Yin Lin, Elena De Martin, Giacomo Conte 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Skull-base meningiomas are often characterized by favorable long-term prognosis, yet their anatomical complexity and proximity to critical neurovascular structures make treatment selection challenging. Stereotactic radiosurgery with CyberKnife represents an effective therapeutic option when surgical resection is not feasible; however, not all patients benefit equally from this treatment. Early identification of patients likely to respond to radiosurgery remains an open clinical problem. In this study, we propose a radiomics- and clinical feature-driven framework for predicting volumetric response in skull-base meningiomas treated with CyberKnife. Unlike most existing approaches that focus on progression-free survival or recurrence, our method targets volumetric response as an indicator of treatment efficacy. Pre-treatment MRI images from 104 patients were processed to extract radiomic features, which were combined with clinical variables and analyzed using six models. To ensure methodological rigor, the entire modeling process was implemented within a nested cross-validation scheme. Among the evaluated models, TabPFN achieved the best overall performance, with an AUC of 0.81 and consistently favorable classification metrics. These results suggest that advanced machine learning architectures, when combined with robust validation strategies, can effectively capture patterns associated with treatment response even in small-sample, high-dimensional settings.

---


### 339. [Graph-augmented Segmentation of Complex Shapes in Laser Powder bed Fusion for Enhanced In Situ Inspection](https://arxiv.org/abs/2604.24234)

**<font color=#1a73e8>作者：</font>** Stefano Raimondo, Matteo Bugatti, Marco Grasso  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The technological maturity of in situ inspection and monitoring methods in additive manufacturing is steadily increasing, enabling more efficient and practical qualification procedures. In this context, image segmentation of powder bed images in Laser Powder Bed Fusion (L-PBF) has been investigated by various authors, leveraging both edge detection and machine learning approaches to identify deviations from nominal geometry. Despite these developments, several challenges remain, including the sensitivity of segmentation performance to industrial illumination conditions and layer-to-layer variability in pixel intensity patterns. The study addresses these limitations by proposing a graph-augmented segmentation approach. The underlying principle consists of preserving the geometrical information at a global level rather than at pixel-wise level, modeling dependencies and relational information among spatial regions with a Graph Neural Network bottleneck embedded into a U-Net architecture. This allows enhancing the consistency and accuracy of the geometry reconstruction in the presence of spatial and layer-wise photometric variability systematically faced in real data. The method is evaluated against benchmark techniques for the in situ reconstruction of lattice structures produced by L-PBF, demonstrating its potential as a scalable solution for robust in situ inspection and geometric verification in industrial environments.

---


### 340. [Touchless Intraoperative Image Access System Based on Vision-Based Hand Tracking](https://arxiv.org/abs/2604.24235)

**<font color=#1a73e8>作者：</font>** Yin Lin, Domenico Aquino, Alberto Redaelli 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Touchless interaction with medical images is becoming increasingly important in the surgical field, where sterility and continuity of the operational workflow are essential requirements. This work presents a vision-based system for intraoperative navigation of medical images through hand gestures acquired using a single RGB camera. Unlike many existing solutions, the system does not require additional hardware or user-specific training. Hand tracking is performed in real time using MediaPipe Hands, which provides a 2.5D estimation of hand landmarks. Simple and intuitive gestures are then mapped into translation, rotation, and zoom commands, enabling continuous and natural interaction with the image viewer. The system architecture is independent from the visualization software and, for implementation simplicity, in this study it was integrated with PyVista. Performance was evaluated through frame-level logging and quantitative analysis of latency, stability, and interaction robustness metrics. Experimental results highlight real-time behavior, with reduced latencies and stable control, in line with the requirements of fluid interaction. The system demonstrates the feasibility of a low-cost touchless solution for intraoperative access to medical images, laying the groundwork for future clinical evaluations.

---


### 341. [GeoEdit: Local Frames for Fast, Training-Free On-Manifold Editing in Diffusion Models](https://arxiv.org/abs/2604.24238)

**<font color=#1a73e8>作者：</font>** Yiming Zhang, Sitong Liu, Ke Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models are a leading paradigm for data generation, but training-free editing typically re-runs the full denoising trajectory for every edit strength, making iterative refinement expensive. To address this issue, we instead edit near the data manifold, where small local updates can replace repeated re-synthesis. To enable this, we estimate a local manifold tangent space directly from perturbed samples and prove that this sample-based estimator closely approximates the true tangent. Building on this guarantee, we devise a Jacobian-free algorithm that constructs a tangent frame via small perturbations to the initial noise and alternates small tangent moves with diffusion-based projections. Updates within this frame follow principled on-manifold directions while suppressing off-manifold drift, enabling fine-grained edits without full re-diffusion or additional training. Edit strength is controlled by the number of steps for rapid, continuous adjustments that preserve fidelity and plug into existing samplers. Empirically, the resulting tangent directions yield smooth, semantic unsupervised traversals and effective CLIP-guided optimization, demonstrating practical interactive continuous editing.

---


### 342. [Instance Awareness of Multi-class Semantic Segmentation Loss Functions](https://arxiv.org/abs/2604.24276)

**<font color=#1a73e8>作者：</font>** Soumya Snigdha Kundu, Florian Kofler, Marina Ivory 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Instance-sensitive losses for semantic segmentation such as blob loss and CC loss were designed to address instance imbalance, ensuring small lesions generate the same gradient as large ones, but operate only on single-class segmentation. In multi-class settings, class imbalance poses an additional problem: rare classes with few instances receive a disproportionately small share of the training signal. We show that extending instance-sensitive losses to multi-class segmentation via a one-vs-rest class decomposition repurposes them to also address class imbalance, as uniform averaging over classes ensures each class contributes equally regardless of frequency. We further show that inverse-size weighting, which destabilizes training when applied globally due to weight imbalances across rare and common classes, becomes effective when integrated within the per-component loss, confining the reweighting to each component's spatial context. On the BraTS-METS 2025 dataset (260 test cases), multi-class CC loss improves foreground Dice (0.64 +/- 0.26 vs. 0.59 +/- 0.27 baseline) and rare-class Dice, while maintaining Panoptic Quality at DSC threshold 0.5. Multi-class blob loss achieves the best Panoptic Quality at threshold 0.5 (0.40 +/- 0.24 vs. 0.38 +/- 0.25 baseline) and recognition quality (0.53 +/- 0.29 vs. 0.49 +/- 0.30). Integrating inverse-size weighting within the per-component loss increases rare-class Dice to 0.44 +/- 0.36 at the cost of reduced detection quality.

---


### 343. [Resolving Conflicts Between RTOS Timekeeping and Uninterruptable Trusted Computing](https://arxiv.org/abs/2604.24277)

**<font color=#1a73e8>作者：</font>** Antonio Joia Neto, Amarin Amarin, Norrathep Rattanavipanon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Trusted Execution Environments (TEEs) on low-power microcontrollers (e.g., ARM TrustZone-M) enable isolation of Secure and Non-Secure software but still require both worlds to share resources, including interrupt controllers. In this model, real-time applications and real-time operating systems (RTOS-s) are executed in the Non-Secure sub-system, whereas the Secure sub-system is typically reserved for a small set of pre-defined security (e.g., cryptographic) operations referred to as trusted computing services. However, many RTOS-s rely on periodic interrupts (SysTicks) to advance their own notion of time (time-keeping), and the delivery of this interrupt is essential for preserving real-time behavior. On the other hand, the security of many trusted computing services requires atomicity vis-a-vis the Non-Secure sub-system (where the RTOS resides), precluding SysTick handling.
This paper first characterizes this conflict and then introduces a Secure-driven time synchronization mechanism in which the Secure World measures elapsed time and compensates the Non-Secure RTOS by unobtrusively updating the RTOS time-keeping data structures with the appropriate number of missed ticks before re-enabling interrupts and resuming the execution of the Non-Secure system. This approach restores a consistent, monotonic notion of time across worlds and enables secure coexistence of trusted computing services and RTOS-s on microcontrollers. Importantly, the proposed approach requires no modifications to the underlying RTOS and yields no significant run-time overhead.

---


### 344. [Model-Free Inference of Investor Preferences: A Relative Entropy IRL Approach](https://arxiv.org/abs/2604.24280)

**<font color=#1a73e8>作者：</font>** Chen Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a framework using Relative Entropy Inverse Reinforcement Learning (RE-IRL) to recover investor reward functions from observed investment actions and market conditions. Unlike traditional IRL algorithms, RE-IRL is employed to account for environments where transition probabilities are unknown or inaccessible. To address the challenge of data sparsity, we utilize a $K$-nearest neighbor approach to estimate the observed behavior policy. Furthermore, we propose a statistical testing framework to evaluate the validity and robustness of the estimated results.

---


### 345. [RowHammer Vulnerability Counter (RVC): Redefining RowHammer Detection with Victim-Centric Tracking](https://arxiv.org/abs/2604.24287)

**<font color=#1a73e8>作者：</font>** Lavi Jain, Venkata Kalyan Tavva  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Rowhammer vulnerability poses an increasing challenge with newer generations of DRAM and aggressive technology scaling. Existing mitigation techniques, such as Graphene, Twice, and Hydra, primarily rely on tracking activation counts for each row and issuing refreshes when a row reaches a predefined tracking threshold. However, these methods have inherent limitations, including inefficiencies in identifying rows genuinely at risk of bit flips.
In this paper, we propose a novel framework called Rowhammer Vulnerability Count (RVC), which shifts the focus from activation count tracking to evaluating a row's actual vulnerability to bit flips. By selectively issuing refreshes only to rows on the verge of experiencing bit flips, RVC drastically reduces unnecessary refresh operations. We also demonstrate that prior works have incorrectly set tracking thresholds, leading to security flaws.
Our evaluation shows that RVC achieves 95 - 99.99% improvement in mitigation induced refreshes when compared to Graphene, with no additional space overhead. Furthermore, RVC improves energy efficiency and reduces average LLC latency by up to 76.91%, making it a highly efficient and scalable solution for addressing Rowhammer in modern DRAM systems. These findings establish RVC as a superior approach for preventing Rowhammer, outperforming existing methods in both accuracy and efficiency.

---


### 346. [Latent-Hysteresis Graph ODEs: Modeling Coupled Topology-Feature Evolution via Continuous Phase Transitions](https://arxiv.org/abs/2604.24293)

**<font color=#1a73e8>作者：</font>** Qinhan Hou, Jing Tang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural ordinary differential equations (Graph ODEs) extend graph learning from discrete message-passing layers to continuous-time representation flows. While it supports adaptive long-range propagation, we show that Graph ODEs with strictly positive irreducible mixing operators face an inherent \emph{monostability trap}: in the long-time regime, information leakage is unavoidable and the dynamics converge to a single global consensus attractor. We propose the \textbf{Hysteresis Graph ODE (HGODE)}, which couples feature evolution with a latent topological potential driven by a learned pairwise force. A double-well edge potential and bipolarized gate allow edge states to polarize into connected or insulated phases while preserving differentiability. We provide asymptotic analysis of the collapse mechanism and the proposed hysteretic topology dynamics, and validate HGODE on theory-driven synthetic diagnostics and real-world graph benchmarks.

---


### 347. [ReVSI: Rebuilding Visual Spatial Intelligence Evaluation for Accurate Assessment of VLM 3D Reasoning](https://arxiv.org/abs/2604.24300)

**<font color=#1a73e8>作者：</font>** Yiming Zhang, Jiacheng Chen, Jiaqi Tan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current evaluations of spatial intelligence can be systematically invalid under modern vision-language model (VLM) settings. First, many benchmarks derive question-answer (QA) pairs from point-cloud-based 3D annotations originally curated for traditional 3D perception. When such annotations are treated as ground truth for video-based evaluation, reconstruction and annotation artifacts can miss objects that are clearly visible in the video, mislabel object identities, or corrupt geometry-dependent answers (e.g., size), yielding incorrect or ambiguous QA pairs. Second, evaluations often assume full-scene access, while many VLMs operate on sparsely sampled frames (e.g., 16-64), making many questions effectively unanswerable under the actual model inputs. We improve evaluation validity by introducing ReVSI, a benchmark and protocol that ensures each QA pair is answerable and correct under the model's actual inputs. To this end, we re-annotate objects and geometry across 381 scenes from 5 datasets to improve data quality, and regenerate all QA pairs with rigorous bias mitigation and human verification using professional 3D annotation tools. We further enhance evaluation controllability by providing variants across multiple frame budgets (16/32/64/all) and fine-grained object visibility metadata, enabling controlled diagnostic analyses. Evaluations of general and domain-specific VLMs on ReVSI reveal systematic failure modes that are obscured by prior benchmarks, yielding a more reliable and diagnostic assessment of spatial intelligence.

---


### 348. [SolarTformer: A Transformer Based Deep Learning Approach for Short Term Solar Power Forecasting](https://arxiv.org/abs/2604.24306)

**<font color=#1a73e8>作者：</font>** Ankan Basu, Jyotiraditya Roy, Aditya Datta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate forecasting of solar power output is essential for efficient integration of renewable energy into the grid. In this study, an attention-based deep learning model, inspired by transformer architecture, is used for short-term solar power forecasting. Our proposed model, "SolarTformer", is designed to predict solar power output from meteorological data. Unlike traditional models, SolarTformer leverages self-attention mechanisms to effectively capture temporal dependencies and spatial variability in solar irradiance. In addition, the proposed methodology includes feeding power station-specific metadata into the model, which helps to generalize between power stations located at different locations and with different panel configurations and in different seasons. Our experiments demonstrate that SolarTformer significantly outperforms previous models on the same data set. In particular, the model exhibits strong performance on both clear and cloudy days, indicating high robustness and generalizability. These findings highlight the potential of attention-based architectures in enhancing the accuracy of solar forecasting, contributing to a more reliable management of renewable energy.

---


### 349. [BIMStruct3D: A Fully Automated Hybrid Learning Scan-to-BIM Pipeline with Integrated Topology Refinement](https://arxiv.org/abs/2604.24311)

**<font color=#1a73e8>作者：</font>** Mahdi Chamseddine, Fabian Kaufmann, Marius Schellen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic generation of Building Information Models (BIM) from building scans is a key challenge in architecture and construction. We present a modular pipeline for generating IFC-compliant BIM from 3D point clouds. The hybrid approach combines learning-based semantic segmentation with topology-aware geometric reconstruction to model structural elements accurately. We propose vIoU, adapting voxel-based overlap evaluation to Scan-to-BIM by enabling holistic, instance-matching-free comparison of reconstructed and ground-truth models. We release the German Hospital dataset (DeKH), including high-resolution point clouds, ground truth BIMs, and semantic annotations. Experiments on DeKH and CV4AEC datasets show significant improvements over a RANSAC-based baseline, demonstrating robustness and scalability.

---


### 350. [Unconstrained Multi-view Human Pose Estimation with Algebraic Priors](https://arxiv.org/abs/2604.24312)

**<font color=#1a73e8>作者：</font>** Xiaolin Qin, Qianlei Wang, Jiacen Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering 3D human pose from multi-view imagery typically relies on precise camera calibration, which is often unavailable in real-world scenarios, thereby severely limiting the applicability of existing methods. To overcome this challenge, we propose an unconstrained framework that synergizes deep neural networks, algebraic priors, and temporal dynamics for uncalibrated multi-view human pose estimation. First, we introduce the Triangulation with Transformer Regressor (TTR), which reformulates classical triangulation into a data-driven token fusion process to bypass the dependency on explicit camera parameters. Second, to explicitly embed the inherent algebraic relations of the multi-view variety into the learning process, we propose the Gröbner basis Corrector (GC). This pioneering loss formulation enforces constraints derived from the multi-view variety to ensure the neural predictions strictly adhere to the laws of projective geometry. Finally, we devise the Temporal Equivariant Rectifier (TER), which exploits the equivariance property of human motion to impose temporal coherence and structural consistency, effectively mitigating scale ambiguity in uncalibrated settings. Extensive evaluations on standard benchmarks demonstrate that our framework establishes a new state-of-the-art for uncalibrated multi-view human pose estimation. Notably, our approach significantly closes the performance gap between calibration-free methods and fully calibrated oracles.

---


> [!TIP]
> 当前位于：**301-350**（第 7/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-437](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
