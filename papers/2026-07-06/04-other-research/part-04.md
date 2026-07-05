# 📦 其他研究 | 2026年07月06日

> 本类共 **266** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-266](./part-06.md)

---

### 151. [Robust Image Processing Techniques for Construction Environment Monitoring Using Underwater Robots](https://arxiv.org/abs/2607.01915)

**<font color=#1a73e8>作者：</font>** Seunghee Yun, Geonmo Yang, Juhui Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper proposes a robust image processing framework for underwater robot-based construction environment monitoring, targeting complex degradations observed in real marine environments. Unlike conventional approaches that mainly consider absorption and backscattering, real underwater imagery is strongly affected by depth-dependent forward scattering blur and particle-induced degradations such as marine snow. To address this, we introduce a staged processing pipeline that sequentially models background degradation via depth-aware forward scattering and foreground degradation using realistic marine snow patterns extracted from real images. The resulting synthetic data are used to retrain an existing Joint-ID network without modifying its architecture, enabling an isolated evaluation of dataset realism. In addition, a lightweight post-processing scheme is applied to enhance contrast and structural clarity. Experiments on real underwater datasets collected in Korean coastal environments demonstrate consistent improvements in visual quality and UIQM scores. The results indicate that explicitly modeling forward scattering and realistic particle effects effectively reduces the synthetic-to-real gap and improves practical applicability in real-world underwater robotic operations.

---


### 152. [ContextSniper: AntTrail's Token-Efficient Code Memory for Repository-Level Program Repair](https://arxiv.org/abs/2607.01916)

**<font color=#1a73e8>作者：</font>** Chiwang Luk, Matin Mohammad Najafi, Zhifeng Jia 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents can repair real repository issues, but they often spend large context budgets on whole-file reads, broad searches, and long terminal outputs where useful evidence is mixed with irrelevant code and logs. This paper presents ContextSniper, AntTrail's token-efficient code memory layer for repository-level program repair. As the coding specialization of AntTrail's broader agent memory engine, ContextSniper implements the Sniper feature for precision evidence selection: it retrieves candidate code and runtime evidence, ranks it with hybrid retrieval signals, filters long outputs through an intention-aware context gate, and returns compact evidence packets while preserving recoverable source context outside the prompt. We evaluate ContextSniper on SWE-bench Lite with OpenClaw and Claude Code, using 50 task runs per host-agent condition. ContextSniper reduces total token use by 51.5% and logged cost by 36.4% for OpenClaw, and reduces total token use by 38.9% and estimated cost by 27.3% for Claude Code. Submitted-resolution rates decrease slightly, from 26.0% to 24.0% for OpenClaw and from 32.0% to 30.0% for Claude Code. ContextSniper's pilot testing scripts are open-sourced at this https URL

---


### 153. [Sparse-Aware Vector Quantization for Bandwidth-Efficient Collaborative 3D Semantic Occupancy Prediction](https://arxiv.org/abs/2607.01928)

**<font color=#1a73e8>作者：</font>** Feng Li, Chaokun Zhang, Gong Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Collaborative perception extends single-agent perception by enabling multiple vehicles to exchange complementary perceptual information. However, it introduces an inherent trade-off between perception gain and communication overhead, which is particularly severe for 3D semantic occupancy prediction that relies on fine-grained spatial structures. Existing methods typically compress 3D features into 2D, causing severe spatial information loss, or transmit dense 3D representations, hindering real-world deployment. To overcome these limitations, we propose a bandwidth-efficient collaborative Vector Quantization Semantic Occupancy Prediction (VQSOP) framework. VQSOP employs a Sparse-Aware Vector Quantization (SAVQ) mechanism that exploits 3D scene sparsity to compactly encode informative regions, drastically reducing communication overhead while preserving complete geometric context. Furthermore, to enhance structural consistency and feature continuity, we design a Dual-Branch Adaptive Spatial Refinement (ASR) module that dynamically fuses local high-frequency details with broad contextual semantics. Extensive experiments demonstrate that our approach achieves state-of-the-art performance while reducing communication volume by up to 82x.

---


### 154. [AIriskEval-edu: New Dataset for Risk Assessment in AI-mediated K-12 Educational Explanations](https://arxiv.org/abs/2607.01934)

**<font color=#1a73e8>作者：</font>** Javier Irigoyen, Roberto Daza, Francisco Jurado 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This work introduces AIriskEval-edu-db2, a new dataset designed to train and evaluate auditors based on LLMs for an explainable pedagogical risk assessment in instructional content for grades K-12. The dataset comprises 1,639 explanations from 170 curated ScienceQA questions, covering science, language arts, and social sciences. For each question, the dataset includes an explanation written by a human teacher alongside 11 explanations generated by LLM-simulated teacher profiles associated with distinct pedagogical risks. We propose a comprehensive risk rubric aligned with established educational standards that covers five complementary dimensions: factual precision, depth and completeness, focus and relevance, student-level appropriateness, and ideological bias. A key contribution is the addition of 785 explanations with structured explainability annotations, including risk localization and risk description. The annotations are produced through a semi-automatic process with expert teacher validation. Finally, we present validation experiments comparing state-of-the-art proprietary models with a lightweight local Llama 3.1 8B model in both the pedagogical risk detection and the explainability assessment. These experiments evaluate whether supervised fine-tuning on AIriskEval-edu-db2 enables a locally deployable model to approach or outperform stronger frontier models while preserving privacy in educational auditing and assessment tasks.

---


### 155. [A-TMA: Decoupling State-Aware Memory Failures in Long-Term Agent Memory](https://arxiv.org/abs/2607.01935)

**<font color=#1a73e8>作者：</font>** Zitong Shi, Yixuan Tang, Anthony Kum Hoe Tung  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long term memory lets LLM agents act as persistent assistants, but user facts change. A useful memory system must know what is true now, what used to be true, and what changed. We study \emph{ghost memory}, a state coordination failure in which old, current, and transition facts coexist in the memory bank, remain mixed during retrieval, and mislead the answer model. We argue that memory systems should be understood and optimized from three levels: bank maintenance, retrieval, and answer time resolution. We propose ATMA, a state aware overlay for existing memory systems. ATMA keeps superseded and transition records in the bank, builds evidence packets for the query's requested state view, and exposes current, historical, and transition labels to QA. We further call for decoupled evaluation of bank, retrieval, and answer level failures, since final QA accuracy can hide where ghost memory occurs. To make this failure measurable, we build LTP (LoCoMo Temporal Plus), a conflict heavy benchmark for ghost memory, and evaluate on LoCoMo for long conversation generalization. On LTP, Graphiti+ATMA improves conflict accuracy by 0.240 absolute over Graphiti. On LoCoMo, Graphiti+ATMA raises temporal F1 from 0.0295 to 0.1705. The gains are host dependent, but they indicate that explicit state roles can reduce memory failures hidden by final QA accuracy.

---


### 156. [Conditional Co-Ablation: Recovering Self-Repair Backups in Transformer Circuits](https://arxiv.org/abs/2607.01940)

**<font color=#1a73e8>作者：</font>** Zhiren Gong, Zihao Zeng, Chau Yuen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mechanistic interpretability often relies on component-level interventions to discover how a model produces a behavior. This guides attribution, capability knockout, and model pruning downstream to operate by scoring each unit by the effect of ablation in isolation. Such first-order scoring is natural when component importance is additive, but becomes misleading when a transformer self-repairs: after a primary component is removed, a dormant backup can take over, muting the primary's measured effect while the backup itself appears irrelevant on the intact model. We recast this failure as a recovery task, conditional circuit completion, and introduce Conditional Co-Ablation (CoAx), a label-free, output-grounded score that asks how much each remaining unit's ablation effect grows once a primary set has been removed. This conditional growth exposes the second-order interaction that single-unit scores discard. On the GPT-2-small IOI circuit, CoAx raises backup-head recovery from 0.33 to 0.91 ROC-AUC, outperforming all baselines, including self-repair-aware gradient scores (best 0.82); counterfactual patching verifies that the recovered heads causally carry the repair. The same label-free procedure transfers to induction across eight models. Beyond discovery, the recovered backups correct self-repair-masked attribution, identify the components required for capability knockout, and yield repair-aware structured pruning scaling from 124M to 7B. Component importance is therefore not merely an isolated-unit property: in robust circuits, the components that matter can become visible only under the interventions that make them necessary.

---


### 157. [Hybrid quantum-classical neural network for sentiment analysis](https://arxiv.org/abs/2607.01943)

**<font color=#1a73e8>作者：</font>** Giacomo Cappiello, Filippo Caruso, Xing Liang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantum machine learning has recently emerged as a promising paradigm that leverages the expressive power of quantum circuits to address complex learning tasks. In this work, we investigate the applicability of hybrid quantum-classical neural networks to sentiment analysis, a central problem in natural language processing. We focus on a dataset of tweets related to COVID-19, where the textual content is vectorized using TF-IDF and fed into both classical feedforward networks and hybrid architectures incorporating parameterized quantum circuits. Our results show that hybrid models can achieve accuracy comparable to the classical baseline, while exhibiting distinct learning dynamics, especially in terms of validation loss and accuracy, that suggest a richer representational capacity. Moreover, when applying transfer learning to an SMS spam classification task, the hybrid models consistently outperform the classical counterpart, achieving an accuracy increase of 15 percentage points (from 66% to 81%) on the spam class, demonstrating enhanced generalization. These findings highlight the feasibility of employing QML for natural language processing and point toward the potential advantages of hybrid models as quantum hardware continues to advance.

---


### 158. [LiZAD: A Lightweight Zero-Shot Anomaly Detection Framework for Industrial Manufacturing](https://arxiv.org/abs/2607.01949)

**<font color=#1a73e8>作者：</font>** Uzair Khan, Luigi Capogrosso, Muhammad Aqeel 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In modern high-throughput industrial production lines, product configurations and visual characteristics frequently change, making it impractical to collect and annotate data for every new scenario. This dynamic setting makes Zero-Shot Anomaly Detection (ZSAD) particularly suitable, as it enables defect detection without requiring training on target-specific samples. Although recent ZSAD approaches show promising results, they are computationally intensive and thus unsuitable for deployment on resource-constrained devices. We propose LiZAD: a lightweight framework designed for real-time ZSAD specifically tailored for use on edge devices. The proposed approach pairs the dense and spatially aware visual features of DINOv3, crucial for precise pixel-level localization, with the highly computationally efficient text embeddings of MobileCLIP2. These features are then mapped into a shared latent space via low-memory trainable projection heads. Compared to six state-of-the-art ZSAD models, LiZAD achieves an average memory reduction of 61.5%, a parameter reduction of 74.6%, and a speedup of 3.02x in terms of latency. Despite substantial reductions in computational and memory costs, our approach maintains competitive anomaly detection performance, dropping the average P-AUROC by just 6.4% relative to the best state-of-the-art model across the VisA, BTAD, MPDD, and MVTec-AD datasets. Finally, it is successfully deployed on the NVIDIA Jetson NX and Jetson AGX edge devices and tested on the real production line of the Industrial Computer Engineering Laboratory (ICE Lab) at the University of Verona. The code is available at this https URL.

---


### 159. [Personalized 4D Whole-Heart Mesh Reconstruction from Cine MRI via Multi-Scale Temporal Modeling and Differentiable Contour Rendering](https://arxiv.org/abs/2607.01952)

**<font color=#1a73e8>作者：</font>** Xiaoyue Liu, Dongcheng Cang, Xiaohan Yuan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate 4D whole-heart mesh reconstruction from sparse cine MRI is critical for creating cardiac digital twins, but remains challenging due to limited 2D slice coverage and the complex coupling between cardiac shape and motion. Existing methods often rely on intermediate contour fitting and typically reconstruct static, single-phase, or partial cardiac geometries, limiting their ability to capture full-chamber dynamics. We propose a novel end-to-end framework for reconstructing temporally resolved whole-heart meshes from multi-view 2D cine MRI sequences by learning an image-to-mesh mapping. The framework incorporates a differentiable contour renderer inspired by the Beer-Lambert attenuation principle, enabling anatomy-aware supervision of 3D+t mesh deformation through contour-based projection losses. To improve temporal consistency across the cardiac cycle, we further introduce a multi-scale temporal modeling module that integrates global cycle-level dynamics with local inter-frame coherence to generate smooth and physiologically plausible mesh trajectories. The proposed method achieved a whole-heart mean absolute error of 1.68 $\pm$ 0.31 mm and a motion jitter of 0.77 $\pm$ 0.17 $\mathrm{mm}/\mathrm{frame}^{3}$, outperforming existing methods with lower reconstruction error and substantially improved motion smoothness. It also improved 2D contour alignment across multiple cine MRI views and supported downstream proof-of-concept electrophysiological simulation. The code will be released publicly upon acceptance of the manuscript for publication.

---


### 160. [A More Accurate Algorithm Comparison through A/B Testing using Offline Evaluation Methods](https://arxiv.org/abs/2607.01958)

**<font color=#1a73e8>作者：</font>** Koki Konishi, Masataka Ushiku, Yuta Saito  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A/B testing is the gold standard for selecting the better algorithm in online services. While offline evaluation has attracted attention as a safer alternative due to the high experimental costs and the potential risk of degrading user experience and revenue in A/B testing, it is widely recognized that the estimation accuracy of offline evaluation is substantially lower. As a result, final selection decisions are typically made through A/B testing. Contrary to this conventional view, we reveal a counterintuitive phenomenon in which A/B testing can produce a higher algorithm selection error rate than offline evaluation. This occurs because the sample mean estimator used in A/B testing does not induce positive correlation, which is crucial for reducing critical selection errors, namely underestimating the truly superior algorithm and overestimating the truly inferior one. In contrast, offline evaluation methods unintentionally generate this beneficial correlation by relying on shared offline data when estimating and comparing the performance of multiple algorithms. Building on this insight, we propose an estimator that intentionally induces positive correlation to improve algorithm selection in A/B testing. The key idea is to introduce a hypothetical middle algorithm and to estimate the performance difference between algorithms A, M, and B in a stepwise manner using shared data at each step. This approach enables the application of offline evaluation techniques in each step, thereby inducing positive correlation and reducing critical selection errors. Furthermore, we derive the optimal middle algorithm regarding the resulting variance and analyze its advantages over existing methods through bias-variance analysis. Experiments on real-world data demonstrate that our estimator achieves the same selection error rate as existing approaches while using only one half of the A/B testing data.

---


### 161. [NAVER LABS Europe Submission to the Instruction-following 2026 Short Track](https://arxiv.org/abs/2607.01960)

**<font color=#1a73e8>作者：</font>** Marcely Zanon Boito, Hemant Yadav, Jean-Luc Meunier 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this paper, we describe NAVER LABS Europe's submission to the instruction-following speech processing short track at IWSLT 2026. We participate again in the constrained setting, developing systems capable of jointly performing ASR, ST, and SQA from English speech into Chinese, Italian, and German. Building on our previous submission, ranked first in last year's short track, we update our multi-stage training pipeline by replacing the speech projector with SpeechMapper, a method for learning a speech-to-LLM embedding projector using only ASR data. In addition, we introduce a synthetic SQA dataset, fakACL, composed of artificially generated scientific presentations. This dataset is built by prompting the LLM backbone, segmenting the generated talks, and synthesizing speech with SeamlessM4T-large-v2. The combination of an improved speech projection mechanism and domain-specific synthetic data allows our model to outperform last year's best short-track system, while being considerably more compact and relying on a weaker LLM backbone. This year's results place our system tied for first place in the overall short track ranking.

---


### 162. [NeoMap: Training-free Novel-View Synthesis from Single Images and Videos](https://arxiv.org/abs/2607.01962)

**<font color=#1a73e8>作者：</font>** Jinxi Li, Tianyi Zhang, Yafei Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study the challenging problem of novel view video synthesis from single images or monocular videos. Existing methods, which operate under the assumption that pre-trained video models lack native novel view synthesis capability and enforce view alignment via camera conditioning, task-specific fine-tuning, or stepwise hard denoising guidance, often suffer from artifacts and compromised global scene consistency. In this paper, we introduce NeoMap, a novel training-free framework designed to locate high-fidelity, view-consistent novel view solutions from general pre-trained video models. The key to our approach is the core insight that promising novel view solutions are inherently encoded within the natural video data manifold learned by pre-trained models, and the core challenge is simply to locate this optimal solution. We solve this via our core mechanism: convergent manifold alternating projection iterations that optimize the initial noise. Extensive experiments demonstrate that NeoMap significantly outperforms all existing methods across 3 standard novel view synthesis benchmarks, including the challenging Tanks-and-Temples, LLFF and DAVIS datasets, achieving state-of-the-art generation fidelity and top-tier view consistency.

---


### 163. [Towards a Phonology-Informed Evaluation of Multilingual TTS](https://arxiv.org/abs/2607.01965)

**<font color=#1a73e8>作者：</font>** Sneha Ray Barman, Neeraj Kumar Sharma, Shakuntala Mahanta  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Neural TTS systems can sound natural across languages, but naturalness does not guarantee the preservation of sound contrasts that distinguish words from their grammatical forms. Standard metrics like MOS do not test for this. We propose a classifier-based framework that audits TTS output against language-specific phonological patterns using human speech as a benchmark. Testing Assamese advanced tongue root (ATR) vowel harmony with Meta's MMS TTS, we show that a classifier trained on human speech transfers to synthesized speech with minimal loss. The faithfulness audit reveals that [+ATR] mid vowels are realized as [-ATR] in 1/3 tokens despite an underlying [+ATR] specification, a bias absent in human speech. At the word level, predicted ATR labels classify harmony more accurately than transcription labels, indicating a gap between intended and produced phonology. The framework offers task-specific diagnostics and generalizes to other phonological contrasts with measurable acoustic cues.

---


### 164. [Assessing VLM Reliability for Medical Image Quality Evaluation Under Corruption and Bias](https://arxiv.org/abs/2607.01973)

**<font color=#1a73e8>作者：</font>** Sofiane Ouaari, Kevin Vorwalder, Nico Pfeifer  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) are increasingly applied in medical tasks such as pathology description, report generation, and visual question answering. Medical Image Quality Assessment (MIQA) supports diagnostic accuracy and patient safety by determining whether images meet the standards required for clinical decision-making. Automating MIQA with VLMs may reduce workload, but their behavior under real-world conditions, where images may be degraded or textual context may affect judgments, should be further explored before deployment. We benchmark VLMs on medical image quality using the MediMeta-C dataset zero-shot across seven corruption types and five severity levels. We evaluate sensitivity to degradation patterns, the effect of corruptions on embedding geometry, and whether textual attributes (demographics, expertise, infrastructure, institution) alter scores. Across 16 VLMs and seven modalities, pixelation produced the largest score reductions (mean -20.58%, up to -34.4% for OCT), whereas brightness had limited effect (-0.81%). Embedding displacement was associated with score changes. Same-family models showed correlations of 0.67-0.83; some produced increases up to +31% for corrupted mammography. Textual attributes affected scores: institutional prestige raised them +17.15%, and equipment age lowered them -14.7%. The largest changes were +95.62% (InternVL-8B) and -37.7% (MedGemma). Current VLMs show limitations for medical image quality assessment. Pixelation, a privacy-preserving transformation, reduces performance, indicating a trade-off between patient privacy and reliability. Sensitivity to contextual metadata indicates limited objectivity and marks metadata as a privacy and bias source. Privacy protection and objective quality assessment are related requirements for use.

---


### 165. [Do Newer Lightweight CNNs Perform Better Under Resource Constraints? A Controlled Multigenerational Study of Architecture, Initialization, Training Budget, and Efficiency](https://arxiv.org/abs/2607.01984)

**<font color=#1a73e8>作者：</font>** Tasnim Shahriar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Newer lightweight convolutional neural networks are often presented as improving predictive performance and deployment efficiency, but such claims require controlled evaluation. This study compares nine lightweight CNN model packages across CIFAR-10, CIFAR-100, and Tiny ImageNet under a shared downstream protocol. We report top-1 accuracy, macro F1, top-5 accuracy, parameter count, FP32 storage, GMACs, batch-size-1 latency on an NVIDIA L4 and AMD Ryzen 5 5500U CPU, peak PyTorch CUDA allocated tensor memory, and point estimate Pareto frontiers. EfficientNetV2-S achieves the highest observed top-1 accuracy on CIFAR-10 and CIFAR-100 at 97.57% and 86.98%, while RepViT-M1.0 leads Tiny ImageNet at 79.87%. EfficientNet-B0 remains within 0.22, 0.85, and 1.79 percentage points of the best result on the three datasets while using approximately 79% fewer parameters and 86% fewer GMACs than EfficientNetV2-S. It also appears on every evaluated accuracy and resource Pareto frontier, making it the most consistently competitive intermediate-budget option. MobileNetV3-Small has the lowest GMAC count, is the fastest model under both CPU thread settings, and records higher observed accuracy than MobileNetV4-Conv-S on all three datasets. Under random initialization, it leads MobileNetV4-Conv-S by 2.55, 1.76, and 0.99 points, with paired test-set intervals excluding zero for the fixed trained models. EfficientNet-B0 remains 3.29, 10.10, and 17.54 points below its pretrained counterpart after 100 epochs of scratch training, despite requiring about five times the recorded training time. SqueezeNet1.1 has the fewest parameters and lowest peak CUDA allocation, but substantially weaker accuracy. Latency rankings differ sharply between the L4 and CPU environments, showing that GMACs alone do not predict measured inference performance. Overall, newer designs provide selective rather than universal gains

---


### 166. [Liquid Latent State Dynamics for Interpretable Turbofan Degradation Modeling](https://arxiv.org/abs/2607.01986)

**<font color=#1a73e8>作者：</font>** Weizhi Nie, Weijie Wang, Yuting Su  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multivariate time-series models for prognostics are often evaluated by point prediction accuracy, yet their internal states rarely expose a coherent degradation process. We study liquid neural networks as latent dynamics models for aircraft engine health monitoring on the C-MAPSS benchmark. The proposed model encodes a history window into a latent state, evolves that state with a liquid transition model, and decodes future sensor observations. To separate health evolution from operating-condition variation, the latent state is factorized into degradation and condition components. Remaining useful life, monotonic risk, and latent-consistency losses supervise the degradation component, while condition prediction and decorrelation losses discourage operating-condition leakage. Across FD001--FD004, the full disentangled model improves overall sensor forecasting RMSE from 0.2438 for a GRU baseline to 0.2266, with the largest gains on the multi-condition subsets FD002 and FD004. The learned degradation state also forms a clearer temporal degradation axis, reaching an average state-speed Spearman correlation of 0.5960. Direct remaining-useful-life regression remains stronger for the GRU baseline, indicating that the proposed representation is currently more effective as an interpretable world model for degradation dynamics than as a calibrated lifetime regressor. These results suggest that liquid latent dynamics can bridge predictive maintenance forecasting and inspectable health-state modeling.

---


### 167. [Understanding Geometric Representations in Self-Supervised Vision Transformers via Subspace Intervention](https://arxiv.org/abs/2607.01987)

**<font color=#1a73e8>作者：</font>** Weichen Zhou, Yawen Zou, Chunzhi Gu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce a controlled subspace intervention framework to investigate how self-supervised Vision Transformers (ViTs) encode dense geometric information. While linear probing is widely used to assess geometric representations, it treats features as a black box, failing to disentangle the underlying topology. To address this issue, we decompose the weights of converged linear probes to isolate the low-rank subspaces containing explicit geometric signals using Singular Value Decomposition (SVD). Our perspective yields three key insights: (1) Pre-training objectives determine how features are encoded. DINOv2 aligns spatial features for efficient linear extraction, while Masked Autoencoders (MAE) tend to disperse these signals, requiring a broader spatial context. (2) Explicit geometric representations are highly compressible, suggesting dense predictive heads could potentially be constrained to low-rank subspaces with minimal performance loss. (3) The layer-wise task affinity suggests that geometric precision peaks at intermediate layers before yielding to semantic abstraction in the final layers. By connecting internal encoding mechanics with downstream performance, these findings provide a basis for effective feature selection and lightweight decoder design. The source code is available at this https URL.

---


### 168. [Episodic-to-Semantic Consolidation Without Identity Drift](https://arxiv.org/abs/2607.01988)

**<font color=#1a73e8>作者：</font>** Xue Qin, Simin Luan, Cong Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-running adaptive intelligent agents face a structural tension between knowledge consolidation and information integrity. Memory consolidation is conventionally treated as an agent-changing operation: a model is fine-tuned, a prompt rewritten, a policy distilled, or a reflection appended to the context that governs future behaviour. In regulated autonomic deployment this is a liability because the agent operates under commitments and audit contracts that bind to a specific, cryptographically certified identity. We propose to treat consolidation not as a mutation of the planner or the identity manifest, but as a deterministic function f: M^ep -> M^sem over episodic memory whose output is a separately addressable semantic knowledge layer; the identity hash does not read M^sem, so consolidation updates knowledge without changing the agent's certified identity. We give a formal account of the agent representation, prove identity invariance through a structural lemma on the manifest's hash-input set, specify a deterministic aggregation algorithm whose outputs are auditable database rows with explicit confidence and supporting-event provenance, and validate the construction with synthetic experiments demonstrating per-field correctness, byte-equal identity across consolidation passes, and a mean 79.82% reduction in unproductive planner attempts (95% BCa CI [78.02%, 81.49%] across 10 seeds) against a calibrated Bayesian-shrunk baseline. The construction is a knowledge-update discipline for autonomic agents in which lessons accumulate as queryable facts while the agent's certified identity remains byte-equal across its operational lifetime, with an embodied service agent as the running case study.

---


### 169. [Training-free Controllable Human Motion Generation under Heterogeneous Constraints](https://arxiv.org/abs/2607.01990)

**<font color=#1a73e8>作者：</font>** Xiaofei Hui, Bo Yan, Haoxuan Qu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training-free controllable motion generation has attracted growing interest for enabling flexible constraint enforcement without constraint-specific training. However, existing training-free methods require constraints to be continuous objective-based with differentiable losses, while many real-world requirements are criterion-based and provide only discontinuous, sparse, or even black-box feedback. In this paper, we propose Motion-Inference-as-Control (MIC), the first training-free motion generation framework that handles both continuous objective-based and criterion-based motion constraints under a shared mechanism. The key idea is to cast diffusion-based motion generation as a stochastic control problem. This perspective not only provides principled and practically effective step-wise control laws that support criterion-based constraints without requiring differentiability and naturally accommodate objective-based constraints as a special case, but also motivates a control-oriented constraint coordination mechanism that adaptively balances and reconciles motion constraints during generation. Experiments across diverse constraint settings demonstrate the effectiveness of our framework.

---


### 170. [Using embeddings to predict spoken word duration and pitch in Mandarin monosyllabic words](https://arxiv.org/abs/2607.02002)

**<font color=#1a73e8>作者：</font>** Xiaoyun Jin, Mirjam Ernestus, R.Harald Baayen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Time-normalized f0 contours of Mandarin words in conversational speech have been shown to be predictable in part from their contextualized embeddings (CEs). The present study investigates whether CEs also predict spoken word duration for 7470 tokens of Mandarin monosyllabic CV words extracted from a Mandarin corpus of spontaneous speech. We show that CEs indeed are predictive for duration, above chance level, not only at the type level, but also at the level of individual tokens, as indicated by the results obtained with the type-wise and token-wise permutation baselines. We also show that the predicted durations are sufficiently precise to back-transform predicted f0 contours in [0,1] normalized time to contours on the ms time scale. The resulting predicted contours approximate empirical contours and also outperform a permutation baseline.

---


### 171. [Mirror Illusion Art](https://arxiv.org/abs/2607.02015)

**<font color=#1a73e8>作者：</font>** Xiaopei Zhu, Zeyuan Li, Jun Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mirror Illusion Art is a novel reflection-conditioned 3D illusion where one object yields two target appearances (front and mirror). The task is formulated as inverse design from two target 2D images (front and mirror) to a printable 3D object with geometry and texture. Prior topology-driven and shadow-based approaches demand substantial manual effort, optimize shape only, and often yield non-smooth or incomplete geometry. To address these challenges, we propose AutoMIA, an automated Mirror Illusion Art design pipeline that jointly optimizes shape and color. To stabilize optimization and suppress artifacts, four mechanisms are introduced: (1) projection-alignment component (PAC) selection to reduce surface noise, (2) position-weighted adaptive (PWA) suppression for background noise, (3) internal voxel preservation (IVP) to prevent internal fractures, and (4) shape-color decoupled (SCD) optimization that balance shape and color optimization. AutoMIA generate diverse smooth Mirror Illusion artworks successfully both in the digital and physical world, with only around 76s design time and 2.6 GB memory on average using a single RTX 3090, advancing inverse graphics and computational design. Our code is available at this https URL.

---


### 172. [UnderOneFacade: Worldwide Facade Semantic Segmentation Benchmark Dataset](https://arxiv.org/abs/2607.02018)

**<font color=#1a73e8>作者：</font>** Yi Wang, Fan Wang, Prabin Gyawali 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Globally consistent semantic digital twins require centimeter-accurate and geographically transferable 3D facade segmentation. However, progress in facade parsing is limited by the lack of large-scale, standardized benchmarks for evaluating cross-domain generalization. Existing datasets are geographically narrow, semantically inconsistent, or insufficiently precise. We introduce UnderOneFacade, the largest cross-country and cross-continent 3D facade benchmark to date, comprising centimeter-accurate point clouds with hierarchical, harmonized, and architecturally grounded semantic labels totaling 2.7 billion annotated points. Through a systematic evaluation of representative point-, graph- and transformer-based architectures, we show that current methods struggle to recognize fine-grained architectural elements and degrade significantly across geographic domains, with the best models achieving only up to 33 IoU on the fine-grained LoFG3 benchmark. By combining geometric precision with standardized semantics at unprecedented scale, UnderOneFacade establishes a rigorous benchmark for developing robust and transferable 3D segmentation models. The dataset, evaluation scripts, and pretrained models will be released upon publication.

---


### 173. [Spatio-Temporal and Clinical Conditioning for Fine-Grained Radiology Report Retrieval](https://arxiv.org/abs/2607.02024)

**<font color=#1a73e8>作者：</font>** P. Sloan, E. Simpson, M. Mirmehdi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radiology is vital to modern healthcare, but rising imaging demand and persistent workforce shortages strain reporting capacity and clinical workflows. Automated radiology report generation has the potential to support radiologists and help alleviate this burden; however, existing retrieval-based methods remain rigid, lack explicit anatomical grounding, and do not account for longitudinal disease progression or available clinical context. In this work, we introduce STAR3, a multimodal, spatio-temporal, attentive retrieval framework for radiology report generation that aligns region-level anatomical information with clinical indications and longitudinal changes across chest X-ray studies. Our framework employs an object detector to identify anatomically meaningful regions and retrieves semantically relevant report sentences conditioned on both current clinical context and changes observed between prior and current examinations. This design enables anatomically and temporally grounded report generation that better reflects clinical reporting practice. Experiments on the MIMIC-CXR dataset demonstrate that STAR3 outperforms current retrieval-based approaches on retrieval, NLP and clinical metrics, highlighting the value of conditioning retrieval anatomically, temporally and clinically for advancing automated radiology report generation.

---


### 174. [ComplexMimic: Human-Scene Interaction Imitation in Complex 3D Environments](https://arxiv.org/abs/2607.02034)

**<font color=#1a73e8>作者：</font>** Lu Pan, Hongwei Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Physics-based Human-Scene Interaction (HSI) imitation learning is crucial for embodied intelligence as it bridges the gap between kinematic 3D motions and real-world dynamics. However, most existing methods focus on simplified scene settings, leaving complex environments largely unexplored, which limits their applicability in real-world scenarios. In this paper, we focus on HSI mimicry in complex environments. Under this complex setting, we observe an inherent trade-off between successfully performing interaction and maintaining natural, physically plausible motions. To address this challenge, we propose ComplexMimic, a framework that reconstructs diverse HSI by interpreting imperfect MoCap data. First, we introduce a Dual Flow Strategy, which learns two complementary experts: an imitation expert for accurate motion tracking and an interaction expert for collision-aware adaptation in complex scenes. Second, naive multi-expert distillation, which treats all experts equally, often under-samples challenging behaviors, limiting effective learning. To mitigate this issue, we propose a difficulty-aware distillation strategy that adaptively weights supervision and prioritizes hard-yet-learnable trajectories guided by failure statistics and learning progress signals. Extensive experiments on three benchmark datasets demonstrate that our approach outperforms current state-of-the-art methods. Our implementation is available at this https URL.

---


### 175. [Hierarchical Anti-Aesthetics: Protecting Facial Privacy against Customized Diffusion Models](https://arxiv.org/abs/2607.02038)

**<font color=#1a73e8>作者：</font>** Songping Wang, Yueming Lyu, Shiqi Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rise of customized diffusion models has fueled a boom in personalized visual content creation, but it also introduces serious risks of malicious misuse, thereby posing threats to personal privacy. Image aesthetics are strongly correlated with human perception of image quality. Motivated by this observation, we address facial privacy protection from a novel aesthetic perspective by degrading the generation quality of maliciously customized models, thus reducing facial identity leakage. Specifically, we propose a Hierarchical Anti-Aesthetics (HAA) framework that exploits aesthetic cues at multiple perceptual levels. HAA consists of two key branches: (1) Global Anti-Aesthetics, which degrades overall aesthetics and generation quality by constructing a global anti-aesthetic reward mechanism and a corresponding loss; and (2) Local Anti-Aesthetics, which disrupts facial identity by using a local anti-aesthetic reward mechanism and loss to guide adversarial perturbations toward facial regions. By integrating both branches, HAA achieves anti-aesthetic degradation from a global to a local level during customized generation. Extensive experiments show that HAA outperforms existing methods in identity removal, providing an effective tool for protecting facial privacy.

---


### 176. [Fast and Accurate Anomaly Detection in Time Series](https://arxiv.org/abs/2607.02046)

**<font color=#1a73e8>作者：</font>** Emanuele Mele, Massimo Cafaro, Angelo Coluccia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Anomaly detection is a critical and evolving field in Machine Learning, with applications targeting different domains such as cybersecurity, finance, healthcare, manufacturing and IoT (Internet of Things) systems. Traditionally, anomaly detection algorithms have been designed using both supervised and unsupervised learning paradigms. The fundamental challenge in real-world anomaly detection scenarios is related to the inherent class imbalance (anomalies are typically rare) and, for supervised methods, to the scarcity of labelled anomalous data. Indeed, labelling is both expensive and time-consuming. Conversely unsupervised methods do not require labelling, but may suffer from high false positive rates when deployed in safety-critical applications. In this work we introduce a novel unsupervised algorithm for anomaly detection in time series based on the Haar discrete wavelet and a suitably designed $t$-test. We establish the theoretical foundation of the proposed $t$-test and, through extensive experimentation across 343 datasets, demonstrate that our algorithm outperforms state-of-the-art unsupervised and self-supervised benchmarks.

---


### 177. [OpenSafeIntent: Evaluating Intent-Calibrated Safe Completion Across Dual-Use Prompt Sets](https://arxiv.org/abs/2607.02047)

**<font color=#1a73e8>作者：</font>** Rheeya Uppaal, Seungwoo Lyu, Selina Sung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Safe completion requires models to provide useful assistance without enabling harm, but this behavior is difficult to evaluate with isolated prompts. We introduce OpenSafeIntent, a benchmark of controlled prompt-sets that vary intent while holding the underlying task fixed. Each datapoint contains benign, dual-use, and malicious variants of the same task. This design lets us evaluate whether models calibrate assistance across intent shifts, rather than merely appearing safe on average. Across a broad model suite, we find that prompt-level safety hides important failures: models often fail to remain safe across matched intent variants, dual-use behavior is brittle under paraphrase, high-level answers on risky topics are not reliably safe, and responses that reframe ambiguous requests into safer tasks are substantially less likely to cross the safety boundary. Our results suggest that safe completion should be evaluated as intent-calibrated behavior over controlled task variants, not as a single safety-helpfulness tradeoff over independent prompts.

---


### 178. [A Memory Efficient Unified Algorithm for Online Learning of Linear Dynamical Systems](https://arxiv.org/abs/2607.02050)

**<font color=#1a73e8>作者：</font>** Yuval Ran-Milo, Angelos Assos, Elad Hazan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Motivated by the challenge of stabilizing a general unknown linear dynamical system (LDS) from observations, we study the natural prerequisite of online prediction. Our goal is to achieve sublinear regret with a memory footprint that adapts to the intrinsic complexity of the dynamics rather than the full hidden -- state dimension. We focus on the practically central regime of systems with low instability complexity -- eigenvalues outside the real stable interval that do not decay rapidly, together with non-semisimple modes-potentially embedded in an otherwise stable real spectrum of much higher dimension; we write $k$ for this count. This regime is the primary setting in which stabilization is plausible: we show that many systems with high instability complexity cannot be stabilized without exponentially large controls. Thus, prediction is meaningful for stabilization precisely when the instability complexity is small. Within this regime, we introduce a unified online algorithm that handles every LDS (including non-diagonalizable systems with complex or exploding modes) with a learnable parameter count of $\widetilde{O}(k)$. Finally, we prove a lower bound showing that $k$ is a valid complexity measure: any filter-based predictor needs at least $k$ filters. Experiments corroborate our theory: on a high-dimensional system, our predictor sharply outperforms prior methods at an equal parameter budget.

---


### 179. [Embracing Intra-Class Heterogeneity for Semi-Supervised Medical Image Segmentation: From Diversity to Precision](https://arxiv.org/abs/2607.02051)

**<font color=#1a73e8>作者：</font>** Yuqi Liu, Yufei Chen, Wei Fu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Due to the scarcity of expert-annotated data, Semi-Supervised Medical Image Segmentation (SSMIS) has emerged as a promising approach. Many anatomical structures in medical images exhibit significant intra-class heterogeneity, with different regions showing heterogeneous intensity patterns within the same structure. However, existing methods inadequately exploit this intensity-manifested intra-class heterogeneity, resulting in uniform structural representations and imprecise segmentation. Furthermore, the scarcity of labeled data makes it more difficult to effectively capture such complex heterogeneity. To address this, we propose Multiple Prototype Contrastive Learning (MPCL), an SSMIS framework that possesses better diversity and better precision. It consists of three novel designs: First, we provide structural representations with better diversity and propose Intensity-aligned Heterogeneous Prototype Generation (IHPG) that effectively models intra-class heterogeneity by generating multiple prototypes aligned with intensity characteristics. Second, we further enhance more diverse structural representations and build a solid foundation for more precise segmentation through Prototypical Space Optimization (PSO) that systematically optimizes a more discriminative and generalizable prototypical space. Finally, we achieve segmentation results with better precision through Dual-branch Knowledge Alignment (DKA) that efficiently promotes intra-class heterogeneity knowledge transfer from prototypical space to the segmentation network. Extensive experiments on three medical image datasets with significant intra-class heterogeneity demonstrate that MPCL significantly outperforms existing methods, especially under extremely limited labeled data.

---


### 180. [Beyond the Performance Illusion: Structure-Aware Stratified Partitioning and Curriculum Distributionally Robust Optimization for Spatially Correlated Domains](https://arxiv.org/abs/2607.02055)

**<font color=#1a73e8>作者：</font>** Prathamesh Patil, Arpit Jain, Aswanth Krishnan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Performance evaluation in AI systems commonly assumes that random dataset splits produce independent and identically distributed (i.i.d.) subsets. We show that this assumption often breaks down in spatiotemporally correlated domains such as aerial surveillance, precision agriculture, and medical imaging, leading to two systematic failures: data leakage, where correlated samples span training and validation splits and inflate performance estimates, and hidden stratification, where errors on minority subpopulations are obscured by aggregate metrics. To address these issues, we propose a unified evaluation and training framework for spatially correlated data. We introduce Structure-Aware Stratified Partitioning (SASP), which constructs validation splits that reduce spatiotemporal leakage while preserving meaningful class balance, and Curriculum Distributionally Robust Optimization (CDRO), a curriculum-based relaxation of distributionally robust training that stabilizes optimization under these stricter splits. Across multiple benchmarks, this combination yields consistently improved generalization, more reliable confidence calibration, and exposes failure modes that remain hidden under conventional random-split evaluation.

---


### 181. [SA-HGNN: Sample-Adaptive Hyperbolic Graph Neural Network for EEG-Based Depression Recognition](https://arxiv.org/abs/2607.02063)

**<font color=#1a73e8>作者：</font>** Yang Li, Pan Hu, Yan Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) have been widely used to capture spatial functional connectivity patterns to improve electroencephalography (EEG)-based depression recognition performance. However, the functional connectivity of brain networks in patients with depression exhibits an inherent hierarchical structure, making it difficult to capture accurate connection patterns. To address these issues, this paper proposes a novel model named Sample-Adaptive Hyperbolic Graph Neural Network (SA-HGNN), which aims to accurately extract the authentic hierarchical structure of depression-affected brain networks. Specifically, the proposed model comprises three core modules. First, a Sample-Adaptive Graph Construction module dynamically constructs personalized brain network topologies to capture more complex spatial relationships within the brain network. Second, hyperbolic graph convolution is employed to overcome the representation bottlenecks of Euclidean space, leveraging hyperbolic geometry to precisely capture latent hierarchical relationships within the brain network. Finally, an Attention Pooling module adaptively filters out highly redundant noise channels in EEG signals, effectively mitigating the interference of inherent noise on the authentic hierarchical topology. Extensive experiments on public EEG datasets demonstrate the superior performance of our method across resting-state and task-related paradigms, validating its robustness to noise and efficacy in capturing abnormal functional connectivity patterns in brain networks of patients with depression.

---


### 182. [Algebraic Model Counting for Global Analysis of Optimal Decision Trees](https://arxiv.org/abs/2607.02069)

**<font color=#1a73e8>作者：</font>** Hiroki Arimura  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ensuring model reliability in Explainable AI requires a global assessment of the hypothesis space. We propose a formal framework for the exhaustive analysis of optimal and near-optimal decision trees, called Algebraic Decision Tree Counting (ADTC). Inspired by Algebraic Model Counting (AMC) in knowledge representation, ADTC reformulates diverse analytical tasks, such as optimization, counting, and sampling, into a unified sum-of-products computation over a semiring $R$. While the hypothesis space of decision trees is doubly exponential with respect to the maximum depth $\Delta$, our dynamic programming algorithm achieves $O^*(n^{O(\Delta)})$ time complexity in the number of features $n$, where $O^*$ suppresses polynomial factors. To handle complex constraints consisting of multiple tree metrics, we introduce model behavior tensors that aggregate semiring values via convolution products over a tensor semiring. This algebraic approach efficiently constructs a model profile that captures the global landscape and trade-offs between criteria such as accuracy, size, and fairness. We demonstrate the utility of our software, emtrees, on real-world datasets, illustrating how ADTC facilitates evidence-based model selection in sensitive domains.

---


### 183. [Evidence-State Rewards for Long-Context Reasoning](https://arxiv.org/abs/2607.02073)

**<font color=#1a73e8>作者：</font>** Ya Gao, Pekka Marttinen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-context reasoning requires models to locate, revise, and synthesize evidence distributed across lengthy inputs. Existing long-context RL methods usually reward final answers or static evidence extraction, offering little feedback on how intermediate actions change the model's evidence state. We propose Maven, a reinforcement learning framework with an editable evidence memory. Maven defines an answer-conditioned evidence-state value and rewards action-level state transitions: add actions are credited by marginal gain and hindsight contribution, link actions by evidence synergy, and drop actions by improved answer support after removing misleading evidence. These rewards are assigned to the corresponding action spans in GRPO. Across Llama and Qwen models on LongBench v2, LongReason, and RULER, Maven outperforms outcome-only RL and evidence-identification baselines, producing more sufficient evidence sets and lower distractor retention. Our results show that long-context RL benefits from optimizing stateful evidence navigation rather than one-shot evidence extraction.

---


### 184. [Comprehensive Robustness Analysis of LiDAR-based 3D Object Detection in Autonomous Driving](https://arxiv.org/abs/2607.02074)

**<font color=#1a73e8>作者：</font>** Adwait Chandorkar, Kai Krink, Yerdana Maulenbay 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advancements in LiDAR-only 3D object detection have demonstrated improved detection accuracy over benchmark datasets. However, the adversarial robustness of these models remains untested. Very few adversarial robustness studies exist for LiDAR-only 3D object detection and unfortunately, even they are limited to legacy models. Moreover, there is a systemic gap in the existing evaluation frameworks that rely simply on mAP ignoring other structural and predictive factors. To fill this gap, we propose a holistic framework that evaluates adversarial robustness using two structural factors (point cloud density and point cloud localization) and three predictive factors (misclassification, localization error, distance from ego). Using this framework, we perform an empirical study and critical analysis on recent and legacy state-of-the-art models using adversarial attacks specifically designed for LiDAR-based models. Our key finding is that high-capacity, voxel-based detectors are more susceptible to structured coordinate perturbations than pillar-based detectors. Additionally, non-anchor-based detectors demonstrate poor adversarial robustness, which necessitates rethinking model training techniques. Overall, our results demonstrate that recent models are as vulnerable to adversarial attacks as their predecessors. Therefore, we argue that there is a need to improve the evaluation benchmarks for 3D object detection that not only reward architectural modifications for improving detection accuracy, but also evaluate whether the design choices improve adversarial robustness.

---


### 185. [HandsOnWorld: Unconstrained Egocentric Video Generation with Camera-Disentangled Hand Control](https://arxiv.org/abs/2607.02075)

**<font color=#1a73e8>作者：</font>** Yushuo Chen, Xiaoyu Shi, Xiaoshi Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present HandsOnWorld, a framework for hand-controlled egocentric video generation that forgoes multi-view and marker-based motion capture, learning instead from unconstrained monocular video. Such generality is bottlenecked by the scarcity of scalable 3D hand annotations: large egocentric corpora lack finger-level labels, whereas precise hand datasets are confined to narrow, instrumented settings, limiting prior hand-controlled generators to restricted scene distributions. We instead annotate 3D hands directly on in-the-wild egocentric video through monocular reconstruction, introducing a protagonist-centered annotation pipeline that filters the reconstructions at the action-semantic, image-quality, and 3D-geometric levels to build EgoVid-Pro, a dataset of clean, protagonist-only hand trajectories spanning 103K clips and roughly 12M frames across diverse everyday scenes. To resolve the camera-hand entanglement induced by large ego-motion, we further propose the Plücker Hand Map, a 3D-aware control signal that extends Plücker-ray representations from camera rays to the hand surface, disentangling camera and hand motion at the representation level. Experiments show that \method surpasses prior hand-controlled generators in reconstruction fidelity and control accuracy, and generalizes to out-of-distribution everyday scenes beyond the laboratory datasets on which prior methods rely.

---


### 186. [HaloGuard 1.0: An Open Weights Constitutional Classifier for Multilingual AI Safety](https://arxiv.org/abs/2607.02079)

**<font color=#1a73e8>作者：</font>** Navaneeth Sangameswaran, Preetham S, Ashmiya Lenin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present HaloGuard 1.0, an open-weights implementation of the constitutional-classifier paradigm for input safety. It achieves state-of-the-art performance on English and multilingual prompt-safety benchmarks at roughly one-tenth the model size of current leading open guard models. The safety constitution is the organising structure of the corpus: a natural-language constitution of 46 policies and 2,940 subcategories drives synthetic data generation, with exhaustive one-to-one paired counterfactuals that hold topic and vocabulary fixed while flipping intent, a two-tier harmless design that separately targets boundary and baseline false positives (FPs), and balanced multilingual materialisation across 46 languages that treats language as a surface form appearing on both sides of the boundary rather than as an adversarial signal. Across seven prompt-safety benchmarks, HaloGuard 1.0-0.8B attains the best average F1 (90.9) of any open guard we evaluate, outperforming baselines up to 27B parameters (over 30 times larger) while holding false-positive rate (FPR) to 4.3 and false-negative rate (FNR) to 9.5. The HaloGuard 1.0-4B variant reaches average F1 of 92.1 and FPR of 3.5, spending its extra capacity on precision rather than recall. A structured adjudication of the remaining failures indicates that most apparent missed-harm cases are benchmark mislabels rather than genuine model misses. An always-on adversarial red-teaming protocol continuously hardens the guard against both content-level and agentic attacks. We release the models as open weights.

---


### 187. [SUNTA: Hierarchical Video Prediction with Surprise-based Chunking](https://arxiv.org/abs/2607.02087)

**<font color=#1a73e8>作者：</font>** Tomoshi Iiyama, Masahiro Suzuki, Yutaka Matsuo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hierarchical state-space models (HSSMs) offer a promising approach to long-horizon prediction by segmenting sequences into temporal chunks. However, their performance hinges on how chunk boundaries are determined. While prior HSSMs typically rely on fixed-length chunking or similarity-based boundary detection, these methods often misalign with the intrinsic temporal structure of the data. We argue that chunking should instead be driven by prediction errors, which more directly indicate when longer-range context becomes necessary. Nevertheless, integrating surprise-based chunking into HSSMs introduces critical challenges, including hierarchical collapse during end-to-end training and the absence of surprise signals during open-loop prediction. To address these issues, we propose Surprise-based Nested Temporal Abstraction (SUNTA), a method that employs a decoupled training strategy to preserve surprise signals and uses internal inconsistency as a top-down surprise metric to determine chunk boundaries within imagined rollouts. Experiments on video prediction tasks in 2D and 3D environments demonstrate that SUNTA outperforms baselines, uniquely maintaining accurate predictions over 250 timesteps, whereas all baselines degrade within the first 10 timesteps.

---


### 188. [Fourier Neural Operators for Rayleigh-Bénard Convection](https://arxiv.org/abs/2607.02088)

**<font color=#1a73e8>作者：</font>** Chelsea Maria John, Thibaut Lunet, Sebastian Götschel 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose an improved Fourier Neural Operator (FNO) for modeling two-dimensional Rayleigh-Bénard convection by predicting time increments instead of full solutions, achieving higher accuracy than a standard FNO baseline. The resulting model is compact (314k parameters, 1.26 MB) and fast (7 ms inference), while maintaining similar accuracy as demonstrated in previous benchmarks. We show that although FNOs generalize to finer meshes, accuracy remains limited by the resolution of the training data.

---


### 189. [TCG-AR: Real-Time Multi-View Augmented Reality for Trading Card Game Streaming](https://arxiv.org/abs/2607.02090)

**<font color=#1a73e8>作者：</font>** Anthony Cioppa, Antoine Verdonck, Maxim Henry 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Trading card games are increasingly played and broadcast online, yet live streams remain mostly limited to flat top-down footage of the playing area. Augmenting such streams with virtual models of the played cards would improve the viewing experience, but most existing systems rely on instrumented playing surfaces and embedded chips, which are costly and impractical for casual players and large-scale events. In this work, we present TCG-AR, a novel real-time pipeline that augments trading card games using ordinary RGB cameras alone, without any physical markers or specialized hardware. Our pipeline detects, orients, and identifies the cards on the board, renders virtual content onto each card across all views, and can additionally compose a broadcaststyle view that summarizes the game state for spectators, streaming the augmented feeds to standard broadcasting software such as OBS. To train the detection, orientation, and identification models without manual labeling, we introduce an automatic procedure that generates annotated synthetic training data from a reference set of card images. Then, we evaluate several trained models on a new manually annotated dataset with real images, analyzing performance and runtime throughput that determine real-world usability. Overall, by relying only on commodity cameras and hardware, and by open-sourcing all code, models, and datasets, this work aims to serve as a reference for real-time trading card recognition and to make real-time augmented-reality streaming accessible to the broader community of players and streamers.

---


### 190. [LongEgoRefer: A Benchmark for Long-Form Egocentric Video Referring Expression Comprehension](https://arxiv.org/abs/2607.02096)

**<font color=#1a73e8>作者：</font>** Shunya Kato, Taiki Miyanishi, Shuhei Kurita 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Egocentric videos capture rich and diverse human-object interactions and have emerged as a fundamental resource for understanding human activities related to objects. In this context, Video Referring Expression Comprehension (Video REC), the task of localizing the temporal and spatial extent of a referred object in video frames given a natural language query, plays a key role in linking textual descriptions to observed objects in untrimmed egocentric recordings. However, existing egocentric Video REC benchmarks primarily focus on short video clips, where some target object appears densely within frames. Such settings do not reflect real-world egocentric recordings, which are long-form, untrimmed, and characterized by sparse object occurrences and complex activity transitions. To address this limitation, we introduce LongEgoRefer, a novel and challenging benchmark constructed from long-form videos in the Ego4D dataset. LongEgoRefer contains 1,498 referring expressions with an average video duration of 45 minutes. The benchmark exhibits extreme target sparsity, detailed linguistic descriptions, and complex human-object interactions embedded in long, dynamic egocentric narratives. Consequently, it defines a demanding spatio-temporal grounding problem that requires models to identify both when an event occurs and where the referred object appears within extended video sequences. We evaluate existing Video REC approaches, including training-free baselines based on vision-language models combined with Grounded SAM2. Extensive experiments show that even advanced baselines and current state-of-the-art models struggle significantly on LongEgoRefer. These results highlight the intrinsic difficulty of long-form egocentric spatio-temporal grounding and emphasize the need for more robust video understanding models.

---


### 191. [WBMM: Windowed Batch Matrix Multiplication for Efficient Large Receptive Field Convolution](https://arxiv.org/abs/2607.02097)

**<font color=#1a73e8>作者：</font>** Wan Song, Wei Zhou, Rui Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large kernel depthwise convolutions achieve strong performance but suffer from significant degradation as kernel size grows due to irregular memory access from gather-based computation; while Large Kernel Acceleration (LKA) helps on small feature maps, it becomes counterproductive on large feature maps, even slower than non-accelerated implementations. We propose Windowed Batch Matrix Multiplication (WBMM), which partitions input into contiguous windows and indexes a compact relative position bias table to construct weight matrices, enabling regular memory access via batched matrix multiplication. This yields a unique property: WBMM's throughput improves with larger windows, opposite to depthwise convolutions that degrade with larger kernels. Operator-level benchmarks show WBMM with 14x14 windows outperforms 5x5 depthwise convolution baselines in speed while providing a 7.8x larger per-layer receptive field. Combined with inter-block cross-window communication and hierarchical window reparameterization, WBMM achieves comparable or higher accuracy on ImageNet-1K, COCO, and ADE20K with 1.31-1.88x training speedup, and demonstrates consistent advantages across GPU, CPU, and edge devices without requiring specialized acceleration kernels. Our code is available at this http URL

---


### 192. [X-Splat: Gaussian Splatting for 3D CBCT Generation from Single Panoramic Radiograph](https://arxiv.org/abs/2607.02099)

**<font color=#1a73e8>作者：</font>** Tomasz Szczepański, Szymon Płotka, Michal K. Grzeszczyk 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating a 3D dental volume from a single panoramic radiograph (PXR) could provide a low-radiation alternative to Cone-Beam Computed Tomography (CBCT), but the problem is highly underdetermined: panoramic acquisition integrates 3D attenuation along curved X-ray paths into a 2D image, leaving depth-resolved anatomy unobserved. Existing implicit and generative approaches often produce oversmoothed geometry or anatomically inconsistent hallucinations, lacking geometry-driven supervision and relying on smooth representations unable to precisely localize sharp anatomical boundaries. We propose X-Splat, the first Gaussian Splatting framework for generating CBCT-like 3D dental volumes from a single PXR. X-Splat uses the known panoramic acquisition geometry as a generation scaffold: learnable anisotropic Gaussian primitives are initialized along the X-ray paths that formed the input image and adjusted in a single feed-forward pass, constrained by Beer-Lambert reprojection and multi-view radiographic training supervision. A lightweight residual refiner adds dataset-level anatomical priors without overriding the geometry already resolved by the Gaussians. We train on synthetic PXR-CBCT pairs, enabling direct volumetric supervision without paired real scans. We further introduce segmentation-based geometry-aware metrics, providing the first evaluation of PXR-based generation over maxillofacial anatomy. X-Splat outperforms NeRF- and GAN-based baselines, recovering individual teeth, cortical boundaries, and alveolar structure, including the mandibular canal which prior methods fail to reconstruct. Code will be available at this https URL

---


### 193. [ContextNest: Verifiable Context Governance for Autonomous AI Agent](https://arxiv.org/abs/2607.02116)

**<font color=#1a73e8>作者：</font>** Misha Sulpovar, Benn R. Konsynski, Qaish Kanchwala 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous AI agents increasingly depend on external knowledge stores, yet most retrieval pipelines provide relevance without durable guarantees of provenance, version identity, integrity, traceability, or point-in-time reconstruction. We formalize this as context governance and present ContextNext, an open specification and reference implementation for governed AI-consumable knowledge vaults. ContextNext does not replace Retrieval-Augmented Generation (RAG); it supplies the governance layer beneath retrieval, determining which artifacts are approved, current, attributable, and integrity-verified before retrieval systems operate over them.
The specification combines typed Markdown documents with metadata, deterministic set-algebraic selectors, contextnest:// URI references, SHA-256 hash-chained version histories, graph-level checkpoints, source nodes for live data through the Model Context Protocol (MCP), and audit traces of agent context consumption. These mechanisms let organizations reconstruct which knowledge versions informed an agent output and whether those versions were AI-eligible when consumed.
We report first empirical results from two controlled experiments. In a stale-version attack isolating the governance-versus-retrieval failure mode, governed selection strictly Pareto-dominates BM25 sparse retrieval, with higher answer-quality pass rate (97% versus 93-90%) at about one-third the input-token cost. In a retrieval-determinism experiment over a 1,060-document corpus, deterministic selectors and BM25 return stable document sets across repeated identical queries (Jaccard 1.0), while a dense+HNSW baseline is non-deterministic on 80% of queries (mean Jaccard 0.611, worst case 0.210). These results suggest that context governance addresses failure modes retrieval quality alone is not designed to resolve. We release a core engine, CLI, and MCP server under open licenses.

---


### 194. [Predictive Conformal Slip Monitoring: An Empirical Evaluation of Rolling Split Conformal Prediction for Pre-Incident Traction Loss Detection](https://arxiv.org/abs/2607.02124)

**<font color=#1a73e8>作者：</font>** Varshith Roy Kotla  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conventional traction control architectures intervene only after the adhesion limit of a tire has already been breached. This paper investigates whether Rolling Split Conformal Prediction , monitoring the volatility of non-conformity residuals from a per-driver Random Forest model of expected slip behavior , can serve as a statistically grounded pre-incident warning signal, ahead of gross traction loss. Unlike an earlier internal draft of this work, the evaluation reported here corrects a confound in the slip proxy (vehicle speed is included as an explicit model feature, not left implicit in the target's denominator), uses every racing lap for each driver rather than only the fastest lap, and is scored against real, timestamped incident labels extracted from FIA Race Control Messages and track-limits lap deletions rather than narrated post-hoc. The result is negative: across 19 drivers and 55,563 test-phase telemetry samples, the rolling-volatility detector achieves a mean precision of essentially 0.0 and mean recall of 0.0 against 14 ground-truth incidents, while flagging on average 15.3% of all samples as anomalous , too high a false-alarm rate for any early-warning use. A static 95th-percentile threshold baseline performs no better in any way that would justify the added complexity of the conformal-volatility formulation. Residual autocorrelation diagnostics show the split-conformal exchangeability assumption is violated for every driver (Ljung-Box p < 0.001, n = 19/19), which is one plausible driver of the high false-alarm rate. We report this as a methodologically rigorous negative finding, diagnose its likely causes, and outline what a genuinely predictive version of this approach would require.

---


### 195. [AbsoluteDegradation: A Physics-Inspired Synthetic Film-Degradation Pipeline and Archival Film Restoration Benchmark](https://arxiv.org/abs/2607.02131)

**<font color=#1a73e8>作者：</font>** Mikołaj Jastrzębski, Dawid Glinkowski, Dawid Zieliński 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Restoring archival film remains a fundamentally challenging problem due to the absence of paired training data and the lack of standardized evaluation benchmarks. Pristine versions of deteriorated footage are physically unrecoverable, requiring supervised methods to rely on synthetic data that often fail to capture the complex, temporally coherent nature of real film degradation. At the same time, existing real-world datasets are limited in scale, quality, and accessibility, hindering reliable evaluation and fair comparison across methods. We address both limitations with AbsoluteDegradation, a physics-inspired, modular pipeline for synthesizing realistic film degradations, and a new large-scale archival benchmark. The proposed pipeline models the analog-to-digital process as a structured composition of artifact families, incorporating signal-dependent grain, parametric scratches, and temporally coherent camera motion, enabling controlled generation of diverse degradation regimes. In parallel, we introduce a curated dataset of 81,576 high-resolution frames sourced from real archival footage, designed for consistent evaluation under real-world conditions. Together, these contributions provide a unified framework for training and benchmarking restoration models. Extensive experiments across multiple architectures show that models trained with AbsoluteDegradation generalize better to real-world footage, while the proposed benchmark reveals systematic failure modes of current methods. We hope this work establishes a foundation for reproducible and domain-authentic evaluation in archival film restoration.

---


### 196. [Coding-agents can replicate scientific machine learning papers](https://arxiv.org/abs/2607.02134)

**<font color=#1a73e8>作者：</font>** Atharva Hans, Ilias Bilionis  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific machine learning papers typically make computational claims, e.g., that the relative mean square error is less than 5% or that the 95% predictive credible interval covers the test data. A coding agent can be prompted to replicate those claims from paper materials alone, but the prompt does not by itself reliably preserve progress or check whether generated evidence supports the paper's claims. We introduce Paper-replication, a workflow that makes each selected paper claim a target with recorded evidence, and implement it as a coding-agent skill. The workflow makes the agent record those targets, reconstruct the paper's method, run computational experiments, link generated outputs to provenance and comparisons with the paper's claims, record where matched evidence appears in the replication report, and pass validation checks before completion. We evaluate Paper-replication on twelve independent runs across four scientific machine learning papers. All twelve workspaces pass the completion gate, and all 158 recorded targets are matched with report coverage. Even in this completed workspace state, repeated runs differ in how papers are divided into targets, in numerical fidelity to the source papers, in elapsed replication time, in the number of intermediate executions replaced before final evidence is accepted, and in the rules used to accept evidence. Paper-replication makes completion depend on workspace evidence and validation checks rather than on the agent's final message.

---


### 197. [ART for Diffusion Sampling: Continuous-Time Control and Actor-Critic Learning](https://arxiv.org/abs/2607.02137)

**<font color=#1a73e8>作者：</font>** Yilie Huang, Wenpin Tang, Xun Yu Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study timestep allocation for score-based diffusion sampling, where a learned reverse-time dynamics is discretized on a finite grid. Uniform and hand-crafted schedules are standard choices, but they rely on fixed prescriptions and can therefore be suboptimal. To address this limitation, we propose Adaptive Reparameterized Time (ART), a continuous-time control formulation that learns a time change by treating the speed of the sampling clock as the control, so that a uniform grid on the learned clock induces adaptive timesteps in the original diffusion time. Based on a leading-order Euler error surrogate, ART provides a principled objective for allocating timesteps along the sampling trajectory. To solve this deterministic control problem, we introduce ART-RL, an auxiliary randomized formulation with Gaussian policies that turns schedule learning into a continuous-time reinforcement learning problem. We prove that the randomized ART-RL formulation is equivalent to ART at the optimizer level, in the sense that its optimal Gaussian policy recovers the optimal ART time-warping rate through its mean. We further establish policy evaluation and policy improvement characterizations and derive trajectory-based moment identities that yield implementable actor--critic updates for learning the schedule. Across experiments ranging from controlled low-dimensional settings to image generation, ART-RL can be plugged into existing diffusion samplers by changing only the timestep grid, consistently improving sample quality over strong baseline schedules at matched budgets while leaving the rest of the sampling pipeline unchanged. The learned schedules also exhibit broad generalization, transferring without retraining across sampling budgets, datasets, solvers, pipelines, and representation spaces.

---


### 198. [AdaCount: Training-Free Similarity-Guided Spatial and Feature Adaptation for Zero-Shot Object Counting](https://arxiv.org/abs/2607.02139)

**<font color=#1a73e8>作者：</font>** Muhammad Ibraheem Siddiqui, Muhammad Haris Khan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot object counting (ZOC) aims to count instances of arbitrary object categories specified only through textual prompts. Recent training-free approaches leverage foundation models such as SAM to reformulate counting as a prompt-driven segmentation task, eliminating the need for costly counting-specific training data with point-level annotations. More recently, SAM3 introduced promptable concept segmentation, enabling the zero-shot segmentation of all instances corresponding to a text-defined concept. However, SAM3 struggles in densely populated scenes containing numerous small objects, where limited image resolution and insufficient attention to target-relevant regions often lead to missed instances and poor instance separation, hindering accurate object counting. To address this limitation, we propose AdaCount, a training-free framework for ZOC based on similarity-guided spatial and feature adaptation. AdaCount first estimates a prototype-driven similarity map that identifies target-relevant regions. This similarity map subsequently guides two complementary adaptations: (i) similarity-guided spatial warping, which reallocates image resolution toward target instances, and (ii) feature modulation, which amplifies target-relevant encoder representations. Together, these adaptations enable SAM3 to devote greater representational capacity to target-relevant regions while preserving global image context, without requiring any model retraining. Extensive experiments across six diverse counting benchmarks establish AdaCount as a new SOTA among training-free ZOC approaches.

---


### 199. [A$^{2}$utoLPBench: An Auto-Generated, Agent-Friendly LP Benchmark via Inverse-KKT Construction](https://arxiv.org/abs/2607.02141)

**<font color=#1a73e8>作者：</font>** Shuo Ren, Yaohui Han, Yifan Shi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Most LP-from-text benchmarks are static datasets of word problems written and labeled by hand. Once such a dataset is released, its size is fixed, its difficulty is fixed, and every problem can leak into the training data of future LLMs. We present \textbf{A$^{2}$utoLPBench}, a benchmark for testing LLM-driven agents on linear programming problems written in plain text. We first pick a feasible point and dual, then write down a problem for which that point is optimal and the objective value is known. The answer is known by construction, with no solver call and no human annotator. The evaluation environment bundles a reference solver-critic baseline and a Docker image whose usage instructions are written for an LLM-driven agent to read. With these in place, any agent can run the benchmark and get a calibrated score with one command. Because the benchmark is a generator rather than a fixed dataset, it has properties no fixed dataset can match: an unlimited supply of fresh problems, a difficulty knob set by $(n,m)$, ground-truth answers correct by construction, low LLM-side cost per problem relative to human authoring, repeatable scores across independent batches, and resistance to training-data leakage when fresh post-cutoff seed ranges are used.

---


### 200. [Predicting Early Stages Of Alzheimer's Disease And Identifying Key Biomarkers Using Deep Artificial Neural Network And Ensemble Of Machine Learning Methodologies](https://arxiv.org/abs/2607.02142)

**<font color=#1a73e8>作者：</font>** Debopriya Ghosh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Alzheimers disease (AD) is a brain disorder that develops slowly and mainly affects memory, thinking, language, and daily activities. It is one of the most common causes of dementia and creates many difficulties for patients as well as their families. In the early stage, the symptoms are often mild and may look like normal ageing. For this reason, many people are diagnosed late, when the disease has already progressed. At present, there is no complete cure for AD. Still, early detection can help doctors manage the condition better and take suitable steps at the right time. In this study, a machine learning model is proposed to detect the early stages of Alzheimers disease using clinical details, neuropsychological test scores, and neuroimaging-related measures. The data used in this work is collected from the Alzheimers Disease Neuroimaging Initiative (ADNI). As the dataset has missing values, iterative imputation is applied to fill them. The dataset also has class imbalance, which is handled using Borderline SVM-SMOTE. After that, feature selection is carried out using wrapper-based and embedded methods so that only important features are used for training. The selected features are divided into training and testing sets, and feature scaling is applied. A stacking ensemble model is developed using Logistic Regression, Extra Trees, Bagging KNN, and LightGBM as base classifiers. Along with this, an artificial neural network is also trained on the same dataset. The performance of these models is compared using precision, recall, F1-score, and AUC-ROC. This study aims to find the best classifier and also identify important biomarkers that may help in the early diagnosis of Alzheimers disease.

---


> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-266](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
