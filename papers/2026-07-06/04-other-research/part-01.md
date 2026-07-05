# 📦 其他研究 | 2026年07月06日

> 本类共 **266** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-266](./part-06.md)

---

### 1. [SPARCLE: SPeaker-aware Aligned Representations via Contrastive Language Embeddings](https://arxiv.org/abs/2607.01238)

**<font color=#1a73e8>作者：</font>** Priyam Mazumdar, Yurii Halychanskyi, Steven Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in speech synthesis have shifted from phoneme representations to direct grapheme modeling. While phonemes address the one-to-many mapping between text and acoustics, they rely on grapheme-to-phoneme (G2P) systems that fail to capture speaker-specific acoustic variation. Prior work demonstrates that grapheme-based models outperform phoneme-based systems at scale, but not in low-resource settings.
In this paper, we propose SPARCLE, a speaker-aware grapheme representation model that enriches characters with their precise acoustic realizations. SPARCLE is trained with a contrastive objective to align graphemes with corresponding Wav2Vec2 acoustic representations while conditioned on speaker identity. The resulting model serves as a replacement to G2P systems for downstream text-to-speech (TTS) tasks. We demonstrate that SPARCLE improves generation quality, reducing word error rates by half in extreme low-resource settings compared to standard grapheme-based models.

---


### 2. [Mapping Text to Multiplex Graph: Prompt Compression as Lévy Walk-Guided Graph Pruning](https://arxiv.org/abs/2607.01241)

**<font color=#1a73e8>作者：</font>** Yaxin Gao, Yao Lu, Jinhong Deng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing prompt compression methods treat text as flat token sequences, failing to capture the distributed nature of important information, which is often spread across multiple locations and connected through both local syntactic dependencies and global semantic relations. Such relational structure is naturally represented as a graph, where tokens or sentences become nodes and their dependencies become edges. To this end, we propose RAGP, which formulates prompt compression as Redundancy-Aware Graph Pruning on a multiplex graph that jointly models fine-grained attention-based dependencies and coarse-grained semantic relations. To efficiently identify non-redundant nodes in this heterogeneous structure (dense local subgraphs and sparse global connections), we employ Levy walks whose heavy-tailed step distribution naturally balances local exploitation with global exploration. Experiments on LongBench show that RAGP achieves an average score of 49.3 under a 4x compression ratio, outperforming existing LLM-based compression methods, such as LongLLMLingua, which attains 48.8 at a 3x compression ratio. Besides, RAGP also surpasses state-of-the-art vision-based text compression paradigms on multiple tasks. The code is available at this https URL.

---


### 3. [Office Comprehension Benchmark](https://arxiv.org/abs/2607.01245)

**<font color=#1a73e8>作者：</font>** Firoz Shaik, Mateus Picanço Lima Gomes, Tanvir Aumi 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Office Comprehension Bench (OCB), the first public benchmark to jointly evaluate LLM systems on Word, Excel, and PowerPoint comprehension over native file formats (.docx, .xlsx, .pptx) and their variants. OCB consists of two tracks. File Fidelity Q&A tests structural and visual perception of office artifacts - tables, charts, embedded images, formulas, and app-specific elements such as headers, speaker notes, and named ranges. Domain Q&A tests expert-level reasoning grounded in real-world industry documents across 12 professional domains, with queries requiring multi-step analysis and synthesis across documents. Each reference answer is decomposed into atomic, binary-gradable claims, and an ensemble of LLM judges scores responses against each claim independently. Even the strongest frontier system in its default reasoning mode reaches only about 59.3% on Domain Q&A; increasing thinking depth within a tier does not move performance materially, while moving to a higher product tier yields modest gains. We release the dataset, evaluation tooling, judge prompt, and a public leaderboard.

---


### 4. [Embedding Inference Attack](https://arxiv.org/abs/2607.01276)

**<font color=#1a73e8>作者：</font>** Cedric Fitiavana Raelijohn, Sébastien Gambs, Jean-Francois Rajotte  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Embedding models are essential components of modern Information Retrieval (IR) systems, yet they are typically hidden behind APIs. Recent works have shown that dense IR system can lead to security vulnerabilities such as embedding inversion attacks. However, such attacks usually require that the attacker knows the embedding model for the attack to be applicable. In this paper, we study IR systems under a black-box setting in which the adversary observes only the unordered set of retrieved documents, without ranking or similarity scores. We demonstrate that in such contexts, tailored queries allow an adversary to identify which embedding model is in use from a set of known model candidate, which we coin as an embedding inference attack (EIA). We also show that certain queries remain discriminative even when the system includes a reranker as a potential defense mechanism. We further validate our method on a real Retrieval-Augmented Generation (RAG) system, in which the tailored queries bypass the LLM's tendency to reject inputs it does not recognize as well-formed questions. Finally, we propose and evaluate other mitigation strategies such as similarity thresholds.

---


### 5. [Multilayer Q-Matrix-Embedded Neural Network for Cognitive Diagnosis (M-QCDNet): Structure-Aware Deep Learning Architecture for Psychometric Interpretability](https://arxiv.org/abs/2607.01278)

**<font color=#1a73e8>作者：</font>** Yiyao Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The research proposes a multilayer Q-matrix-embedded neural network for cognitive diagnosis (M-QCDNet), which integrates the structural interpretability of cognitive diagnostic models (CDMs) with the deep learning neural network (NN). M-QCDNet structures the item-skill relationship using the Q-matrix as a structural prior, ensuring latent mastery profiles remain interpretable and consistent with cognitive theory, followed by the proposed loss function with an L2 penalty to penalize skills not aligned with the Q-matrix and to balance predictive performance and structural alignment. Corresponding evaluation matrices, the interpretable alignment-based metrics that quantify the degree to which predicted skill activations correspond to item-level skills, were further developed. M-QCDNet offers practical benefits for classroom practice, enabling early detection of learning difficulties and supporting mastery-based interventions. By embedding diagnostic validity into model design, M-QCDNet bridges psychometric transparency and neural flexibility, advancing interpretable, fair, and actionable AI for cognitive diagnostics.

---


### 6. [I\textsuperscript{2}RiMA: Spectral Riemannian Representation with Temporal Attention for Mental Stress Detection based on EEG Signals](https://arxiv.org/abs/2607.01279)

**<font color=#1a73e8>作者：</font>** Cheng He, Kunyu Peng, Shangen Han 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cross-subject EEG stress detection remains challenging because discriminative stress-related patterns are both subject-dependent and frequency-specific. Conventional Riemannian methods model spatial covariance mainly in the time domain, overlooking neural oscillations that are critical for high-level cognitive state decoding, while standard temporal tokenization often fragments inter-slice temporal coherence. To address these limitations, we propose \method{}, an Intra-Inter Riemannian Manifold Attention Network for EEG-based stress detection. \method{} constructs spatial covariance matrices independently at each frequency point and maps them to the SPD tangent space, preserving channel-wise geometry together with frequency-specific discriminative cues. It further introduces frequency cluster aggregation to select informative spectral components and reduce redundancy by forming compact, data-driven frequency clusters aligned with EEG rhythms. Finally, an intra-inter slice attention module adaptively integrates local slice-level spectral dynamics and global temporal context across EEG sequences. Experiments on three datasets show that \method{} consistently outperforms five state-of-the-art baselines, achieving up to 82.78\% balanced accuracy while remaining efficient with only 1.60M parameters and 31.95M FLOPs.

---


### 7. [Fixed-Set Robustness in Programming by Example: Example Corruption and Semantic Partition Recovery](https://arxiv.org/abs/2607.01280)

**<font color=#1a73e8>作者：</font>** Yuan Si, Jialu Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Programming-by-example systems infer programs from a small set of input-output examples. Robust PBE work usually models wrong examples as samples from a stochastic noise process and then minimizes an expected or empirical loss. This paper studies a different failure mode: an adversary who sees the synthesizer and chooses the examples whose corruption most damages the returned program. We formalize fixed-set worst-case corruption for finite PBE version spaces, implement exact-within-bounded-pool and heuristic corruption searches for a string-transformation DSL, and introduce version-space partition aggregation (VPA), a defense that synthesizes on disjoint example groups and votes by semantic signatures. The central claim is deliberately bounded and partly negative: low-margin PBE tasks have an adversarial robustness dimension that random-typo and noisy-PBE evaluations miss, while semantic partition aggregation helps only when the clean semantics keep a partition vote margin, which often fails on realistic tasks. Evidence from curated/generated DSL tasks, accepted public SyGuS PBE_SLIA slices, SYNTRA Playgol v2, and noisy-PBE objective baselines supports that boundary. One curated edit flips all 8 spike tasks while 200-trial typo, DSL-pool, and distance-matched random controls succeed on 10.3%, 11.0%, and 16.7%; generated margin-1 rows flip under budget 1 yet VPA recovers them; on public SyGuS the vote margin is near one, so an adaptive attacker drives VPA accuracy to zero; accepted public SyGuS slices move across exact-within-pool budget boundaries; and Playgol shows positive paired-bootstrap gaps against typo and same-pool random controls on the 141 accepted rows. A small exact-output prompt harness over 20 controlled margin-1 tasks shows the same qualitative clean-to-attacked pattern across local and API models, while it is treated as a scope check, not a broad LLM benchmark.

---


### 8. [Domain Knowledge Based Temporal-Spatial Graph Convolution Network for ECG Recognition](https://arxiv.org/abs/2607.01282)

**<font color=#1a73e8>作者：</font>** Wenting Ma, Zhipeng Zhang, Xiaohang Yuan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In light of strides in Arti cial Intelligence (AI) and its wide spread application, challenges persist in the interpretability of AI models, particularly within specialized domains like healthcare, such as electro cardiograph (ECG) recognition. Rather than relying solely on end-to-end convolutional neural networks, this paper introduces a novel approach using a domain knowledge-based graph convolution network for ECG recognition. Key landmarks points of PRQST, vital to ECG interpreta tion, are incorporated as domain knowledge. The double-stream directed graph is employed to model both intra and inter ECG cycles. Speci cally, spatial directed graphs capture the positional relationships among key points, while temporal directed graphs delineate temporal dependencies between adjacent cycles in extended ECG sequences. Experimental re sults on the First Chinese ECG Intelligent Competition dataset, which speci cally classify ECG into nine categories, prove the e cacy of the proposed model. The overall average F1 score is 88.1%, the average F1 score of rare categories is 76.3%, both outperform the state-of-the-art models. The introduction of domain knowledge did enhance the detec tion performance, especially for rare categories.

---


### 9. [Scaling Laws for Grid-Based Approximate Nearest Neighbor Search in High Dimensions](https://arxiv.org/abs/2607.01283)

**<font color=#1a73e8>作者：</font>** Matthew J Liu, Wei Hang Zheng, Vidhan Purohit 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Grid-based approaches to approximate nearest neighbor (ANN) search have been absent from modern scaling analyses. We present a systematic characterization of a multiprobe grid algorithm with respect to dataset size $N$ and dimensionality $d$. Our experiments reveal a previously unreported $d$-scaling crossover on the GloVe embedding family, in which multiprobe grid search maintains an approximately constant dimensional scaling exponent while other graph-, tree-, and partitioning-based methods exhibit degrading throughput. The advantage comes with near-linear query scaling in $N$, but also with lower indexing cost than competing ANN methods. Our results suggest that grid-based methods such as multiprobe grid may be competitive in rebuild-heavy or high-dimensional settings where indexing cost and dimensional robustness dictate performance. More broadly, recent work has formalized self-attention as an ANN operation. Thus, the $N$- and $d$-scaling properties of ANN algorithms may guide cost analysis of efficient transformer architectures. Code is available at: this https URL.

---


### 10. [IonSense-QKG: A Quantum-Readiness Metadata Framework for Lithium-Ion Battery Dataset Discovery](https://arxiv.org/abs/2607.01286)

**<font color=#1a73e8>作者：</font>** Sakthi Prabhu Gunasekar, Prasanna Kumar Rangarajan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Public lithium-ion battery datasets are increasingly used for state-of-health estimation, remaining-useful-life prediction, anomaly detection, electrochemical diagnostics, second-life analytics, and battery safety research. However, these datasets vary substantially in chemistry, modality, scale, label quality, sequence structure, access status, and preprocessing complexity. These differences directly affect whether a dataset is feasible for near-term hybrid quantum-classical machine-learning workflows.
This paper presents IonSense-QKG, a quantum-readiness metadata framework for lithium-ion battery dataset discovery. Starting from the EV-Battery-IonSense index, the proposed framework enriches public battery dataset records with quantum-relevant metadata, including task type, sensing modality, chemistry, label availability, sequence type, preprocessing requirements, candidate quantum encodings, estimated qubit range, and NISQ feasibility. A transparent Quantum Readiness Score is introduced to rank datasets as candidate resources for future hybrid quantum-classical battery benchmarks. The score is intended as a dataset-selection heuristic, not as evidence of quantum advantage.
The framework demonstrates query-based discovery over enriched metadata to identify datasets suitable for compact quantum feature maps, quantum time-series workflows, limited-label anomaly detection, and future battery-health benchmarking. The released artifact includes metadata tables, scoring scripts, robustness checks, link-checking utilities, and SQL-style query examples. IonSense-QKG positions dataset selection as a data-management problem and provides a reproducible foundation for data-centric quantum battery analytics.

---


### 11. [AnchorSplat: Fast and Structure Consistent Detail Synthesis for Gaussian Splatting](https://arxiv.org/abs/2607.01290)

**<font color=#1a73e8>作者：</font>** Dexu Zhu, Jiangnan Shao, Xiaofeng Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) has emerged as a powerful representation for high-fidelity rendering. However, existing assets often suffer from quality bottlenecks such as missing details and texture noise. Prior attempts to enhance these assets via 2D image processing introduce multi-view inconsistencies and high computational costs. In this paper, we propose a novel 3D-native refinement paradigm named AnchorSplat. AnchorSplat is an end-to-end deep network operating directly on 3D structures, avoiding the expensive optimization overhead of traditional 3D-2D-3D pipelines. Crucially, AnchorSplat is a strictly source-free solution requiring no original multi-view images. Central to the proposed method is the Point Anchor Mechanism, which enforces geometric consistency via local offset constraints, mitigating ill-posed mapping and gradient confounding. Furthermore, AnchorSplat replaces iterative densification with a single-pass multiplication mechanism. To facilitate research, we construct 3DGS-SR, the first large-scale benchmark for this task. Experiments demonstrate state-of-the-art results on the 3DGS-SR dataset, with throughput up to $10^5$ times faster than optimization methods. Notably, AnchorSplat exhibits robust zero-shot generalization across diverse data distributions, including generative model outputs and real-world scans.

---


### 12. [CPG-PAD: Concept-Informed Prompts Guided Presentation Attack Detection](https://arxiv.org/abs/2607.01303)

**<font color=#1a73e8>作者：</font>** Haoyuan Zhang, Xiangyu Zhu, Li Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Presentation Attack Detection (PAD) serves as a crucial safeguard for face recognition systems against presentation attacks such as printed photos, replayed videos, and 3D masks. Despite significant progress, existing PAD models still struggle to generalize across unseen domains due to variations in sensors, lighting, and attack materials. Recent Vision-Language Models (VLMs) have shown strong generalization ability, yet their applications in PAD remain limited because learned prompts, typically optimized under class-label supervision, fail to explicitly align with fine-grained attack-relevant visual semantics. As a result, the learned representations often overfit domain-specific artifacts instead of capturing transferable attack cues. To address this, we propose Concept-Informed Prompts Guided Presentation Attack Detection (CPG-PAD), a framework that introduces model-level concept guidance into the prompt learning process. Specifically, we design a Visual Concept-driven Enhancement (VCE) module that employs eXplainable AI (XAI) techniques to automatically discover PAD-relevant visual concepts and generate concept-associated heatmaps providing localized fine-grained guidance. Guided by these heatmaps, a Prompt-based Concept Injection (PCI) mechanism integrates these concepts into the prompt space through a Visual-Prompt Decoder (VPD) and a concept-mapping loss, enabling prompts to align with the model's internal concept space. This design enables CPG-PAD to capture generalizable and domain-invariant attack cues while effectively suppressing dataset-specific biases. Extensive experiments across nine benchmark datasets demonstrate that CPG-PAD consistently achieves state-of-the-art cross-domain performance under multi-source, limited-source, and single-source settings.

---


### 13. [Generative AI and Federated Learning for Intrusion Detection Systems: A Survey](https://arxiv.org/abs/2607.01305)

**<font color=#1a73e8>作者：</font>** Jiefei Liu, Abu Saleh Md Tayeen, Pratyay Kumar 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Intrusion Detection Systems (IDSs) are essential for monitoring network traffic and identifying malicious activities in modern cyber-physical, Internet of Things (IoT), enterprise, and distributed network environments. However, developing reliable IDS models remains challenging because attack behaviors evolve over time, realistic datasets are difficult to obtain, traffic records may be incomplete, attack classes are often imbalanced, and privacy constraints limit centralized data collection. Recent advances in generative artificial intelligence (AI) and Federated Learning (FL) provide new opportunities to address these limitations. Generative models can support anomaly detection, synthetic traffic generation, data augmentation, data imputation, adversarial traffic generation, and IDS alert explanation. FL enables distributed IDS training without directly sharing local network traffic, making it suitable for privacy-sensitive and geographically distributed environments. This survey provides a structured review of generative AI and FL techniques for IDS. We first summarize representative IDS research directions, including adversarial machine learning, anomaly-based detection, IoT-oriented IDS, explainable IDS, and benchmark datasets. We then categorize generative AI applications in IDS according to model families and task objectives, covering autoencoder-based models, Generative Adversarial Networks (GANs), diffusion models, and Large Language Models (LLMs). Finally, we review emerging studies that integrate generative AI with FL-based IDS and discuss open challenges, including synthetic data quality, realistic traffic generation, dual-use adversarial risks, non-IID client distributions, communication-efficient model sharing, federated IDS benchmarking, and domain-specific LLMs for network security.

---


### 14. [PACE: A Neuro-Symbolic Framework for Plausible and Actionable Counterfactual Explanations](https://arxiv.org/abs/2607.01306)

**<font color=#1a73e8>作者：</font>** Pavel Iakovets, Liyanapathiranage Sudeepika Wajirakumari Samarathunga, Martin Thomas Horsch 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Counterfactual explanations explain machine learning predictions by identifying minimal input changes that would alter a model's decision. Although many existing methods successfully generate prediction-changing alternatives, they often produce unrealistic or infeasible recommendations due to a lack of explicit mechanisms for incorporating domain knowledge and intervention constraints. Neuro-symbolic AI offers a promising direction by combining data-driven predictive models with symbolic reasoning capable of representing human-understandable rules and feasible actions. This paper presents PACE, a modular neuro-symbolic framework for generating feasibility-aware counterfactual explanations. The framework separates prediction and reasoning into two components: a neural predictive model for classification and a symbolic reasoning layer that enforces domain-specific constraints during counterfactual generation. By explicitly modeling feasible interventions, the framework produces explanations consistent with domain knowledge while remaining interpretable and actionable. The approach is model-agnostic and adaptable to domains requiring realistic decision support. A case study is conducted on the Adult Income dataset, combining a multilayer perceptron classifier with Answer Set Programming (ASP) rules encoding feasible modifications to education, occupation, and working hours while preserving immutable attributes. Results highlight the trade-off between counterfactual validity and plausibility and show that symbolic constraints yield explanations that better satisfy domain-specific feasibility requirements, illustrating the potential of neuro-symbolic methods for transparent, feasibility-aware counterfactual explanation in explainable AI.

---


### 15. [A Novel Machine Learning Approach for Central Nervous System Tumor Classification from DNA Methylation](https://arxiv.org/abs/2607.01307)

**<font color=#1a73e8>作者：</font>** Paulo R. Ferreira Jr., Lucas Coutinho Freitas, Laís dos Santos Gonçalves 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> NA methylation profiling has become a powerful approach for central nervous system (CNS) tumor classification, yet important challenges remain regarding cross-cohort transferability, methodological correctness, and robust multiclass evaluation. In this work, we propose a novel and methodologically rigorous machine-learning approach for methylation-based CNS tumor classification that combines Sparse Random Projection for dimensionality reduction with multinomial logistic regression for classification. We evaluate the proposed approach in the same general experimental setting established by a widely used reference classifier. On the 2,801-sample reference cohort, our method achieves a mean accuracy of 96\% under stratified 3-fold cross-validation. On the independent 1,104-sample clinical evaluation cohort, it reaches 86\% accuracy at the 91-class level and 93\% when predictions are evaluated at the methylation class family level. These results improve upon the corresponding state-of-the-art reference figures of 82\% class-level concordance and 88\% family-level concordance, yielding absolute gains of approximately 4 and 5 percentage points, respectively. This improvement is clinically relevant: in a diagnostic setting, a 5-point increase in correct tumor classification can directly affect cancer subtype assignment and, in turn, influence treatment selection and downstream clinical decision-making. Our results show that the proposed model, grounded in stronger methodological practice in machine learning, consistently outperforms the previous state of the art across evaluation settings and can materially improve the reliability of CNS tumor classification.

---


### 16. [Cache Merging as a Convergent Replicated State for Multi-Agent Latent Reasoning](https://arxiv.org/abs/2607.01308)

**<font color=#1a73e8>作者：</font>** Carlos Baquero, Luís Brito  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent latent reasoning composes agents' KV-caches into one context for a final agent. Prior work (Agent Primitives) does this by concatenating caches along the sequence axis with RoPE re-encoding, which we call BagMerge. BagMerge is non-commutative, and the best input ordering is unpredictable, shifting with the regime, the latent-step budget, and the model scale. We make this exchange a convergent replicated state. First, CanonicalMerge fixes the layout by content: ordering caches by mean K-norm at a middle layer renders the merged cache byte-identical under any input permutation, verified algorithmically (arity N<=5) and bit-for-bit on real Qwen3-1.7B and 4B state. Second, we separate the replicated state from decode-time layout: the state is a set of content-addressed latent fragments whose merge is set union, a state-based CvRDT (commutative, associative, idempotent, absorbing), and CanonicalMerge is its deterministic render. Because the render is byte-equivalent, every N=2 accuracy number carries over unchanged and re-delivered duplicates are absorbed rather than re-concatenated. On a partitioned-reasoning benchmark, CanonicalMerge matches the best BagMerge ordering in every regime-by-budget-by-ordering cell without knowing which order is best, trading a small, statistically insignificant accuracy margin for an unconditional structural guarantee. The behaviour transfers to real multi-document QA (HotpotQA), while the closest training-free output-fusion baseline (PackLLM) loses by 45 points at matched budget, placing cache-level merging in a regime distinct from output-level fusion. Finally, at k>2 the approach transports and colocates latent traces but does not by itself compose them, which we characterize to motivate future work.

---


### 17. [From Approximation to Emergence: A Theory of Deep Learning](https://arxiv.org/abs/2607.01311)

**<font color=#1a73e8>作者：</font>** Zhilin Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning has outgrown any single mathematical explanation. From Approximation to Emergence develops a unified, proof-oriented account of modern deep learning theory, tracing a path from the classical foundations of approximation, optimization, and generalization to the contemporary mechanisms of overparameterization, robustness, generative modeling, transformers, in-context learning, scaling laws, interpretability, alignment, and emergence. Rather than presenting isolated results, the book organizes a broad literature into a coherent research narrative: each theory is examined through the object it controls, the assumptions that make it valid, and the phenomena it leaves unexplained. Written for researchers, graduate students, and mathematically trained practitioners, this monograph offers a rigorous map of deep learning theory as it stands today: powerful, incomplete, and increasingly centered on the question of how learned mechanisms arise from scale, data, architecture, and training.

---


### 18. [KathaTrace: Diagnosing Semantic Trajectory Collapse in Generated Visual Narratives](https://arxiv.org/abs/2607.01312)

**<font color=#1a73e8>作者：</font>** Jamuna S. Murthy, Amin Karimi Monsefi, Rajiv Ramnath  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual narratives are central to storyboards, comics, children's media, and film previsualization, where viewers understand stories from images alone. Recent generators such as StoryDiffusion produce coherent sequences, but visual coherence does not guarantee that source-story transition meaning remains recoverable. Existing benchmarks assess visual quality, content faithfulness, and scene coherence, but miss a critical failure mode: storyboards where scenes appear visually coherent while the semantic link between scenes disappears. We introduce KathaTrace, a generator-agnostic protocol for diagnosing semantic trajectory collapse, defined as the loss of transition meaning needed to understand how one scene follows another. KathaTrace evaluates transitions under three evidence conditions: text-only, image-only, and text-plus-image, and filters ambiguous items. We contribute KathaBench-25K, with 5,000 narratives from classical collections including Aesop, Panchatantra, and Kathasaritasagara, 20,000 transitions, and 28,712 recoverability questions. We define Semantic Trajectory Gap, or STG, as text-only minus image-only recoverability, measuring transition meaning lost during visualization. Human validation yields Fleiss' kappa = 0.845. Experiments across state-of-the-art generators show substantial STG of 23.5 +/- 1.3. Semantic Compass, an actionability probe, uses KathaTrace signals for post-generation repair and improves storyboard selection.

---


### 19. [An alternative approach towards attacks against fully-split PLWE instances](https://arxiv.org/abs/2607.01340)

**<font color=#1a73e8>作者：</font>** Iván Blanco-Chacón, Rodrigo Martín Sánchez-Ledesma, Raúl Durán Díaz  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In the present work we address some key questions regarding the generalization of root-based attacks presented in a recent work by the authors. In particular, we analyze potential root-based attacks extensions via the construction of explicit isomorphisms from vulnerable instances, and provide a formal proof that this approach will not yield any new vulnerabilities under a fully-split setting. To do so, we first construct an explicit isomorphism between fully-split polynomial rings and polynomial rings where previous attacks apply and show that the application of such an isomorphism will always distort the samples in a way that the resulting samples cannot be used to distinguish. Then, we prove that any isomorphism between fully-split polynomial rings must be of the form of the constructed isomorphism.

---


### 20. [TurnNat: Automatic Evaluation of Turn-Taking Naturalness in Dyadic Spoken Dialogue](https://arxiv.org/abs/2607.01345)

**<font color=#1a73e8>作者：</font>** Hao Zhang, Thomas Thebaud, Georgi Tinchev 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Turn-taking naturalness is central to full-duplex spoken dialogue systems, yet its automatic evaluation remains limited. Existing evaluations often rely on human judgments or behavior-specific timing metrics, making it difficult to compare heterogeneous timing failures within a unified framework. We propose TurnNat, a likelihood-based framework for automatic turn-taking naturalness evaluation in two-channel spoken dialogue. A causal turn-taking prediction model trained on natural conversations estimates future two-speaker voice-activity states, and the negative log-likelihood (NLL) of the observed future activity measures timing atypicality. TurnNat pools frame-level NLLs over turn-taking boundary units (TBUs) extracted from utterance onsets and offsets, and aggregates mean and tail TBU scores into a dialogue-level naturalness score. We further construct a controlled perturbation benchmark of paired natural and perturbed dialogue clips, validated by human naturalness judgments. Experiments on this benchmark show that TurnNat successfully identifies unnatural turn-taking perturbations across heterogeneous timing failures.

---


### 21. [Spatial-Temporal Expert Learning for Video-based Person Re-identification](https://arxiv.org/abs/2607.01353)

**<font color=#1a73e8>作者：</font>** Xiaofei Hui, Pengfei Wang, Evan Ling 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video-based person re-identification (Re-ID) aims to retrieve the same identity in the query video clips from the gallery video clips. To solve this problem, exploiting fine-grained features is of great importance, especially when discriminating identities that are similar in appearance. In this paper, we propose to enhance the ability to explore fine-grained information with a novel input-aware extendable expert module. Instead of updating the network parameters with every sample in the dataset, we aim to train the experts within specific subsets that only contain similar samples and promote their ability to exploit fine-grained information within these similar samples. To achieve this goal, we incorporate two mechanisms in this module: input-aware expert selection mechanism and spatial-temporal selection mechanism. The first mechanism dynamically activates a set of experts on subsets of similar samples, pushing the experts to exploit subtle differences between these similar samples, while the second one further increases their sensitivity to the fine-grained differences in spatial and temporal aspects and allows the experts to dynamically utilize them for different input samples. In addition, to facilitate the expert module, we design an extendable scheme that allows the module to flexibly add new experts when necessary. As a result, our method achieves outstanding performance on two large-scale datasets.

---


### 22. [Chameleon: Recovering Cyber-Physical Systems from Memory Corruption Attacks via ML Surrogates](https://arxiv.org/abs/2607.01356)

**<font color=#1a73e8>作者：</font>** Mohsen Salehi, Karthik Pattabiraman  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cyber-physical systems (CPSs) are increasingly deployed in every aspect of our lives and can be compromised through memory corruption vulnerabilities, allowing attackers to hijack the control flow and take over the system. Existing techniques mostly focus on detecting such attacks but respond by terminating or halting execution upon attack detection, which is not acceptable in CPSs used in safety-critical tasks, as interrupted tasks can have catastrophic consequences. Other techniques replace compromised CPS components with simplified defaults that degrade system behavior, or reboot the system upon attack detection.
We propose Chameleon, a novel framework for automatically recovering CPSs from memory corruption attacks using machine learning (ML)-based surrogates trained at compartment granularity that nearly replicate their original compartments' behavior but do not have the same memory corruption vulnerabilities. Upon attack detection, Chameleon replaces the compromised compartment with its trained surrogate. We implemented Chameleon using the LLVM compiler and evaluated its efficiency and effectiveness on seven different robotic vehicles (RVs), including simulated and real ones. We found that Chameleon can generate surrogates that closely approximate the original compartments (with an average R$^2$=0.96), successfully recover the system despite real-world memory corruption attacks unlike prior approaches, and complete their tasks while incurring low performance and memory overhead.

---


### 23. [Mitigating Confirmation Bias through Hand-Drawing Videos](https://arxiv.org/abs/2607.01359)

**<font color=#1a73e8>作者：</font>** Chenyu Lin, Cindy Xiong, Icy Zhang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Understanding data visualizations is essential for informed decision-making, yet interpretation is often shaped and even distorted by prior beliefs. We investigate whether an embodied pedagogical approach, in which viewers observe the dynamic hand-drawing of a visualization, can mitigate confirmation bias and improve interpretation accuracy. We conducted a study comparing static bar charts to videos in which charts are constructed through hand-drawing, across contexts that either align with or challenge participants' prior beliefs. The results indicate that hand-drawn videos helped participants accurately interpret data, even when the data conflicted with their prior beliefs. This approach also reduced belief-consistent errors and increased belief-overriding responses. These findings suggest that exposing the construction process of a visualization supports more accurate reasoning and mitigates the influence of confirmation bias. Consequently, this work introduces a promising design space for bias-mitigating data interfaces.

---


### 24. [Multi-modal Rail Crossing Safety Analysis](https://arxiv.org/abs/2607.01365)

**<font color=#1a73e8>作者：</font>** Paimon Goulart, Chansong Lim, Nícolas Roque dos Santos 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Given one or more images of a railway crossing, can we leverage visual cues that allow us to robustly estimate how safe it is? Can we improve our ability to do so by introducing structured data (such as official accident reports) about the accident history of that crossing into our models? In this work, we explore how to best answer those questions towards building an AI system that can ingest multi-modal data for railway crossings and provide safety assessment and scores that align with expert opinion and with safety scoring used by the Federal Railroad Administration (FRA). To that end, we propose a proof-of-concept pipeline that delivers on that goal, while at the same time exploring and tackling a number of critical research challenges that pertain to different parts of the pipeline, from data preparation to different learning paradigms that can allow us to realize such a system. Indicatively, our proposed system identifies HIGH-RISK and LOW-RISK crossings with a macro F1 score of 0.757 and estimates FRA-based safety scores with an RMSE of 0.078 and correlation of 0.492 using a routed fine-tuned compact VLM pipeline, while producing qualitative results that align with domain-expert assessment.

---


### 25. [Simulation Based Reward Function Validation for Multi-Agent On Orbit Inspection](https://arxiv.org/abs/2607.01367)

**<font color=#1a73e8>作者：</font>** Patrick Quinn, Bala Prenith Reddy Gopu, George M. Nehma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> A proposed method for the control of groups of inspection spacecraft is Multi-Agent Reinforcement Learning (MARL). While MARL has already been employed for this purpose in previous work, the reward functions used focus on reaching a finite set of predetermined inspection points around the target. In this work, we study and develop a generalized reward function for the MARL inspection task informed by the analysis of 3D reconstructions of inspected objects in orbit. Because the reward function is generalized such that any number of images at arbitrary locations may evaluated, we also allow trained agents to have complete control over when images are collected. With this approach, we gather insights into best practices for not only the specific MARL inspection task, but also gain key takeaways informative to the broader inspection task outside of a MARL context.

---


### 26. [MapDreamer: Aerial Imagery Conditioned Latent Diffusion for Lane-Level Map Generation](https://arxiv.org/abs/2607.01370)

**<font color=#1a73e8>作者：</font>** Julian Brandes, Philipp Crocoll, Wolfram Burgard  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High definition map generation is essential for autonomous driving, yet remains a labor-intensive process at scale. We present MapDreamer, a generative diffusion model that synthesizes lane-level vector maps with explicit topology directly from a single aerial image. MapDreamer learns a compact latent representation of lane centerlines and their topological relations using a variational autoencoder and predicts graphs with a transformer-based latent diffusion model. To align generated maps with the observed scene, we condition each denoising step on dense aerial features injected through cross-attention. To handle the varying number of lanes across scenes, we propose a lane cardinality module paired with background ghost lane latents, a learned buffer that prevents slot collapse during diffusion. Furthermore, we introduce a sliding-window global graph aggregation strategy that stitches local tiles into city-scale maps while preserving connectivity through encoded lane boundaries. Experiments on UrbanLaneGraph derived from Argoverse 2 show improved geometric and topological fidelity over non-generative baselines.

---


### 27. [MIBE: Multi-subject Interaction Benchmark and Evaluator for Personalized Image Generation](https://arxiv.org/abs/2607.01383)

**<font color=#1a73e8>作者：</font>** Zhihan Chen, Yuhuan Zhao, Yijie Zhu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-subject personalized image generation requires the precise rendering of all requested reference identities and their specified interactions based on a guiding prompt. However, state-of-the-art models still struggle with this process, frequently omitting subjects, failing to preserve reference appearances, or misattributing interactions. Furthermore, existing metrics designed primarily for single-subject fidelity cannot reliably capture these errors, suffering severe degradation in ranking separability and failing to align with human preference as the subject count increases. To address this gap, we introduce Multi-subject Interaction Benchmark and Evaluator (MIBE), a unified framework comprising a Multi-subject Interaction Benchmark (MIB) and a Multi-subject Interaction Evaluator (MIE). MIB systematically covers diverse relation types and scene complexities through a decoupled data regime. This consists of a 60K-pair VLM-labeled Silver Set for scalable metric training and a 4K-pair double-blind Human Evaluation Gold Set covering a diverse range of state-of-the-art generators, with the Silver Set reaching 95.1% cross-VLM preference agreement. To demonstrate the utility of this benchmark, we present MIE, a lightweight, reference-conditioned evaluator trained exclusively on the Silver Set with a dual-head ranking and diagnosis objective. MIE exhibits strong cross-generator generalization on the Gold Set, achieving 0.922 overall pairwise accuracy against human preference, including 0.982 on seen generators and 0.884 on unseen generators. By outperforming a broad spectrum of baseline metrics, including CLIP and DINO variants, MIE demonstrates that diagnostic supervision can preserve ranking separability and human alignment where traditional evaluators collapse.

---


### 28. [RusFinChain: A Russian Benchmark for Verifiable Chain-of-Thought Reasoning in Finance with Fuzzy-Aligned Evaluation](https://arxiv.org/abs/2607.01388)

**<font color=#1a73e8>作者：</font>** M. K. Arabov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-step symbolic reasoning is essential for robust financial analysis, yet most benchmarks neglect intermediate reasoning steps. FINCHAIN introduced verifiable Chain-of-Thought (CoT) evaluation but is limited to English. FINESSE-Bench includes a Russian block but relies on multiple-choice questions without step-level supervision. We present RusFinChain, the first Russian-language symbolic benchmark for verifiable CoT reasoning in finance. It spans 17 domains, 172 topics, and comprises 5,280 parameterized examples from executable Python templates, ensuring contamination-free evaluation. Each example includes a gold-standard reasoning chain with intermediate numeric values for automatic verification. We also introduce enhanced metrics: Fuzzy Numeric Alignment and Soft-Attention Alignment. We evaluate 8 open-weight LLMs on a stratified sample, generating 8,100 responses. Results reveal a substantial reasoning gap: models achieve Hard F1 of ~0.65 for step alignment, but only ~29% of final answers are correct. Our fuzzy and soft metrics show stronger correlation with final-answer correctness (Spearman rho approx 0.48) than the original ChainEval (rho approx 0.38-0.46), demonstrating superior diagnostic power. We release dataset, code, and evaluation framework to foster verifiable financial AI for the Russian-speaking community.

---


### 29. [How Should Transformers Encode Numeric Values in Electronic Health Records?](https://arxiv.org/abs/2607.01391)

**<font color=#1a73e8>作者：</font>** Maria Elkjær Montgomery, Christian Igel, Mikkel Odgaard 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How do we encode numeric values in transformer-based sequence processing, particularly in electronic health record (EHR) data? We systematically compare discrete, continuous, and hybrid value encoding strategies using synthetic arithmetic tasks embedded within real-world EHR data, as well as real-world clinical prediction tasks. Our study reveals trade-offs between numeric precision, optimisation stability, and architectural flexibility. We find that approaches that explicitly model value-concept interactions perform best on precision-sensitive arithmetic tasks when architectural constraints permit. Hybrid token-based approaches that retain numeric values but apply binning prior to projection provide a more robust and broadly applicable alternative, with the optimal number of bins following a simple empirically derived power-law in dataset size. Across tasks, models consistently exhibit reliable "good enough" numeric computation rather than exact arithmetic, while clinical gains from incorporating laboratory values are task-dependent. This suggests that robustness and deployability often outweigh maximal numeric precision in practice, motivating hybrid token-based approaches as a practical default.

---


### 30. [Rethinking Generic Object Tracking Toward Human-Level Perceptual Intelligence](https://arxiv.org/abs/2607.01395)

**<font color=#1a73e8>作者：</font>** Shih-Fang Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> At the heart of human visual perception lies the ability to maintain a continuous and coherent understanding of the external world. By integrating observations with accumulated experience, the human visual system can continuously adapt to variations in both the target and its surrounding environment, while preserving robust visual continuity as scene dynamics evolve. Human vision can therefore integrate prior knowledge, spatial geometry, and semantic context to understand complex scenes and their changes. As a core problem in computer vision, visual object tracking aims to bring machine perception closer to human visual perception. These capabilities are central to the task of Generic Object Tracking (GOT). In this task, a visual tracker is initialized only with the bounding box of an arbitrarily specified target in the first frame, and must continuously localize the target in subsequent dynamic visual streams. However, future events, observations, and real-world variations are inherently unpredictable; therefore, the model's generalization and online adaptation capabilities remain bottlenecks. Tracking reliability can deteriorate when the target undergoes severe deformation, is affected by complex distractors, encounters significant environmental changes, or belongs to a category unseen during training. This dissertation aims to narrow the gap between machine visual tracking systems and human visual perception by proposing a series of methods that systematically enhance the target discrimination, robust adaptation, and geometric reasoning capabilities of tracking models.

---


### 31. [Computer Vision for Wildlife Monitoring: Detecting Brown Howler Monkeys using YOLO](https://arxiv.org/abs/2607.01396)

**<font color=#1a73e8>作者：</font>** Gabriel Ferri Schneider, Guido Luis Glufke Mainardi, Paulo Ricardo Knob 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Urban expansion threatens global biodiversity, especially affecting arboreal species due to the fragmentation of forest habitats. The movement of arboreal species across disjointed forest patches increases mortality risk and, thus, compromises their conservation. In this context, the installation of canopy bridges can be a viable strategy; yet continuous monitoring of their use by arboreal species is essential for ensuring their effectiveness, typically carried out with the aid of camera traps. However, this method often produces false-positive images that demand time from conservationists for review. In this context, computer vision algorithms can optimize the task of detecting target species using the canopy bridges. In this study, we explored the automatic detection of brown howler monkeys (Alouatta guariba) in videos obtained by camera traps. Given the need for a large number of annotated images of the target animals to train the algorithms, we tested the incorporation of auxiliary data to improve detection models, fine-tuning the YOLOv10 framework using varying proportions of them. The improvement of these automatic detection techniques contributes to conservation efforts, by providing automatic tools to monitor solutions that minimize the impact of human interference in animals habitats.

---


### 32. [NeuroBridge: Bridging Multi-Task MRI Knowledge for Neurodegenerative Disease Diagnosis](https://arxiv.org/abs/2607.01401)

**<font color=#1a73e8>作者：</font>** Mengyu Li, Guoyao Shen, Chad W. Farris 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> INTRODUCTION: Accurate MRI-based identification of Alzheimer's disease (AD), mild cognitive impairment (MCI), and related dementias remains challenging because disease-related structural changes are often subtle and heterogeneous. We developed NeuroBridge, a clinically guided multi-task MRI framework for neurodegenerative disease diagnosis. METHODS: NeuroBridge integrates large-scale self-supervised MRI pretraining with hippocampal segmentation, hippocampal atrophy classification, and reconstruction objectives, followed by gated fusion fine-tuning. Performance was evaluated across ADNI and OASIS cohorts, including cross-cohort transfer, probability-based analysis, and opportunistic screening. RESULTS: NeuroBridge achieved the highest performance across evaluated classification tasks, reaching 88.17% accuracy for AD versus cognitively normal controls in ADNI and 82.78% in OASIS. The largest gains occurred in MCI-related and mixed-diagnosis settings. The framework demonstrated strong cross-cohort generalization, systematic associations between predicted-class probability and accuracy, and the feasibility of probability-based opportunistic screening. DISCUSSION: Clinically guided multi-task representation learning improves neurodegenerative MRI diagnosis beyond conventional single-task approaches. NeuroBridge provides a robust and scalable framework for dementia assessment and MRI-based opportunistic screening.

---


### 33. [Spin-Weighted Spherical Harmonics Enable Complete and Scalable $\mathrm{E}(3)$-Equivariant Networks](https://arxiv.org/abs/2607.01408)

**<font color=#1a73e8>作者：</font>** Chenxing Liang, Yuchao Lin, Andrii Kryvenko 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> $\mathrm{E}(3)$-equivariant networks are promising for 3D atomistic system modeling, yet their scalability is limited by the $O(L^6)$ complexity of the Clebsch-Gordan Tensor Product (CGTP). The recently proposed Gaunt Tensor Product (GTP) reduces the complexity but is unable to capture the antisymmetric paths, resulting in incomplete expressivity. In this work, we present SpinGTP, an approach to overcome the GTP incompleteness by generalizing from scalar functions to Spin-Weighted Spherical Harmonics (SWSH). By relying on the algebraic properties of SWSH, SpinGTP recovers the missing antisymmetric interactions while maintaining the asymptotic efficiency of GTP. It also allows for a more expressive equivariant basis that naturally accounts for the parity-odd components of tensor products. We evaluate SpinGTP across diverse benchmarks, including Tetris, 3BPA, SPICE-MACE-OFF, and OC20. Our results show that SpinGTP achieves accuracies comparable to full CGTP. Notably, by explicitly capturing antisymmetric paths, SpinGTP exhibits superior performance in tasks involving chiral materials and non-centrosymmetric geometries. This work provides a complete, scalable, and mathematically rigorous path toward high-order equivariance in large-scale 3D atomistic system simulations.

---


### 34. [The Rollout Infrastructure Tax in Coding-Agent Reinforcement Learning](https://arxiv.org/abs/2607.01415)

**<font color=#1a73e8>作者：</font>** Daniel Thi Graviet, Lovre Pesut, Ivan Dagelic 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Coding-agent reinforcement learning treats execution infrastructure as a background implementation detail, despite relying on large numbers of interactive software rollouts. This is a missed opportunity: measuring infrastructure overhead can reveal practical efficiency gains for RL post-training, where small per-rollout savings compound at scale. We present a comparative study of four execution substrates: single containers, hosted sandboxes, Kubernetes-orchestrated containers, and cloud virtual machines. We find up to $110\times$ variation in cold-start latency and a $1.8\times$ spread in projected worker-hours for one million 150-step trajectories. Our results suggest that future coding-agent RL systems should optimize execution substrates as part of the training system itself, not merely as deployment plumbing.

---


### 35. [Beyond Heatmaps: Unsupervised Concept-Graph Reasoning for Interpretable Visual Explanation](https://arxiv.org/abs/2607.01416)

**<font color=#1a73e8>作者：</font>** Md Mohasin Hossain, Anar Amirli, Robert Leist 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Concept Bottleneck Models (CBMs) provide an intrinsically interpretable alternative to post-hoc explanations. However, existing CBMs often rely on predefined concept vocabularies or supervised annotations, lack explicit concept grounding, and summarize each concept with a single image-level score -- discarding spatial recurrence and inter-concept dependencies. We propose a Graph-based Concept Bottleneck Model (G-CBM), an intrinsically interpretable framework that performs unsupervised concept discovery via Non-negative Matrix Factorization (NMF) and represents the discovered concepts as nodes in a per-image concept-graph representation. G-CBM matches region-level features to these concept nodes -- providing concept grounding and capturing concept recurrence across the image -- and applies a \emph{tunable concept filtering threshold} $\tau$ to suppress weak region-level features. A Graph Attention Network (GAT) then performs concept-level reasoning by modeling nonlinear dependencies across nodes. Across ImageNet, HAM10000, PH2, and Derm7pt, G-CBM achieves an average relative AUC improvement of 3.7\% over a ResNet-50 baseline. Concept filtering frequently improves predictive performance while inducing selective concept use, achieving peak AUC of $0.96$ on PH2 with only 2 of 10 concepts and 0.92 on HAM10000 with 3.8 of 9 concepts. On dermoscopy benchmarks, G-CBM is competitive with supervised approaches requiring external annotations. Deletion/insertion analyses with random ablation controls show that the learned concept ranking faithfully reflects model predictions.

---


### 36. [Conditional Inference Trees and Forests for Feature Selection](https://arxiv.org/abs/2607.01417)

**<font color=#1a73e8>作者：</font>** Robert Milletich, Justin Downes, Steve Goley 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conditional inference trees (CIT) and conditional inference forests (CIF) reduce split-selection bias by testing features before choosing split thresholds, but repeated permutation tests and threshold searches can make these methods computationally expensive. We study CIT and CIF as top-$k$ feature-ranking methods for downstream prediction using real-data benchmarks, runtime ablations, and synthetic feature-recovery experiments. At a fixed node, if the features and permutation budget do not depend on the node responses, Bonferroni-corrected $+1$ Monte Carlo permutation $p$-values control nodewise rejection under the complete permutation null. CIF ranks 4th among 17 classification methods on 22 datasets and 3rd among 18 regression methods on 8 datasets. With Bonferroni correction held fixed, the CIF runtime ablations indicate that adaptive stopping and the number of thresholds searched have the largest measured effect on runtime: turning off adaptive stopping and using exact threshold search increase fitting time by 4.0--8.4$\times$ and 1.9--10.8$\times$, respectively, while downstream score changes are at most 0.011. Sparse high-$p$ simulations indicate that forest feature sampling can leave informative features out of many split decisions. Overall, the results support CIF as a top-$k$ feature-ranking method in the evaluated downstream prediction benchmarks.

---


### 37. [Agent4cs: A Multi-agent System for Code Summarization in Large Hierarchical Codebases](https://arxiv.org/abs/2607.01425)

**<font color=#1a73e8>作者：</font>** Yongjian Tang, Ezgi Sarikayak, Doruk Tuncel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Understanding large, complex codebases, especially those with obfuscated structures and incomplete documentation, remains a significant challenge. Existing code summarization solutions often rely on a single language model or coding assistant like Claude Code, and treat source code as flat text, underutilizing the rich interdependencies and hierarchical information within a repository. To address these shortcomings, we propose Agent4cs - a multi-agent framework that summarizes large codebases in a bottom-up fashion, where a summarization agent focuses on producing robust summaries; a keyword-extraction agent proactively identifies critical information from subfolders; and a quality-assurance agent iteratively refines the outputs for readability, coherence, and completeness. Evaluated on 7 frontier models, Agent4cs improves semantic consistency across all folder levels by average 8% compared to two structured prompting baselines with code segments. Furthermore, extensive evaluation on real-world datasets demonstrates up to 38% gains in normalized keyword coverage rate over the same baselines.

---


### 38. [When Should Service Agents Reconsider? Difficulty-Routed Control in Customer-Service Operations](https://arxiv.org/abs/2607.01426)

**<font color=#1a73e8>作者：</font>** Qian Chen, Chengyuan Liu, Xin Yu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous customer-service agents are shifting from conversational interfaces toward operational execution roles: they retrieve firm records, apply service policies, and execute backend writes such as refunds, cancellations, exchanges, order modifications, and reservation changes. This shift creates a service-control problem: firms must keep routine service fast and low-friction while preventing operational errors on requests where customer instructions, policy constraints, firm records, and backend writes interact. We propose a difficulty-routed service-control architecture that asks when service agents should reconsider before acting. A lightweight router keeps routine sessions on a low-cost baseline path and routes operationally coupled sessions to an escalated workflow. The escalated path uses conflict-aware communication and write-triggered reconsideration to concentrate deliberation and safeguards before consequential backend writes, rather than applying additional control uniformly across all service sessions. We evaluate the architecture on human-verified retail and airline tasks from $\tau^{2}$-bench. In retail, the method improves reliability consistently on service requests with operational conflict. Routing evidence shows that stronger control is directed toward conflicted requests rather than broadly applied to routine ones. Dialogue and tool-use profiles suggest that gains do not come from indiscriminate interaction expansion or broader tool chains; instead, added turns and tool calls support evidence gathering, write separation, and pre-write reconsideration. Case-level evidence shows that the escalated workflow preserves fallback plans, binds retrieved records to the correct action, sequences writes, and decomposes multi-entity requests. Airline results extend the same service-control logic to reservation operations.

---


### 39. [Sign in the Air to Unlock: An Interface for authentication in Virtual and Augmented Reality Powered by Point-Voxel Cross-Attention Network](https://arxiv.org/abs/2607.01435)

**<font color=#1a73e8>作者：</font>** Neda Abdolrahimi, Thiru Siddharth, Frank Sicongchen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Significant advancement of immersive technologies such as Virtual and Augmented Reality (VR/AR) and their integration into diverse aspects of modern life need authentication interfaces that are secure, intuitive, and compatible with embodied interaction. Traditional methods such as passwords, PINs, and device-based logins, break immersion and rely on external hardware. Recent 3D-specific behavioral approaches, such as hand-gesture, eye-tracking, and electroencephalography (EEG)-based methods, offer promising alternatives but often require specialized sensors or constrain natural movement, limiting usability in dynamic environments. We present Sign in the Air to Unlock, an in-air signature interface that enables users to authenticate by signing naturally in 3D space which is a familiar, personal, and reproducible gesture. To realize this interface, we design a point-voxel Cross-Attention Network (PV-Net) that jointly models local motion dynamics and global spatial structure from 3D trajectories. The model is evaluated on two datasets: the public DeepAirSig dataset (1,800 signatures from 40 users) and ImmAirsig, a new dataset collected using Meta Quest 2 in immersive VR (880 samples from 22 users). PV-Net achieves an Equal Error Rate of 2.5% on DeepAirSig and 76% classification accuracy on ImmAirSig. These findings highlight the potential of 3D behavioral interfaces for seamless, user-centric authentication that merges security with natural interaction in immersive environments.

---


### 40. [How Much Future Helps? A Controlled Study of Future-Privileged Supervision for Causal Egocentric Gaze Estimation](https://arxiv.org/abs/2607.01437)

**<font color=#1a73e8>作者：</font>** Jia Li, Wenjie Zhao, Fnu Atisri 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Egocentric gaze estimation is commonly studied using models that process the full video with access to future frames, while real-world applications require strictly causal, online prediction. This discrepancy raises key questions: Does future context inherently provide valuable signals for gaze estimation? If so, how much future look-ahead optimally supervises a causal model during training? To investigate, we propose a controlled framework featuring a future-aware branch that accesses a tunable look-ahead horizon during training but is discarded at inference. This design isolates the impact of future context while keeping the inference architecture fixed and strictly causal. Across EGTEA Gaze+ and Ego4D, we find that future-privileged supervision consistently improves causal gaze prediction, confirming its utility. However, performance gains do not increase monotonically with longer look-ahead, but rather peak within a bounded temporal regime. Specifically, optimal performance corresponds to roughly 1.7--3.3 seconds of future context ($H{\in}[5, 10]$) on EGTEA Gaze+ and 2.7 seconds ($H{=}10$) on Ego4D. Our results demonstrate that lightweight causal models can effectively absorb future-aware signals, providing practical guidance for real-time egocentric gaze modeling.

---


### 41. [On the Utility and Factual Reliability of Pruned Mixture-of-Experts Models in the Biomedical Domain](https://arxiv.org/abs/2607.01444)

**<font color=#1a73e8>作者：</font>** Atsuki Yamaguchi, Szymon Palucha, Léo Bijar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models offer inference speedups via selective activation but impose substantial memory requirements because the whole network must remain loaded. Structured expert pruning is a practical approach for reducing deployment costs in resource-constrained settings. However, prior studies primarily evaluate benchmark utility, leaving the effect of pruning on factual reliability underexplored, particularly in high-stakes domains such as biomedicine. In this paper, we investigate how domain-specific expert pruning affects both utility and reliability. We assess four MoE models, six pruning methods, and multiple pruning ratios across generation and classification tasks under in-domain (biomedical) and cross-domain settings. Results reveal that moderate pruning preserves in-domain utility without immediate reliability decline, although hallucination risks increase at extreme pruning ratios. When shifting to the general domain, both utility and reliability degrade rapidly. These findings indicate that safe compression depends heavily on the task and domain. Evaluating pruned MoE models solely on utility is inadequate for high-stakes deployment without reliability assessment.

---


### 42. [Hamm-Grams: An Algorithm for Mining Regular Expressions of Bytes](https://arxiv.org/abs/2607.01445)

**<font color=#1a73e8>作者：</font>** Derek Everett, Edward Raff, James Holt  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Malware poses a critical and ever-evolving threat, and robust and effective systems for detecting and classifying malware are of essential importance. $n$-grams features are among the common static features used in effective machine learning systems for malware, but these features are inherently brittle. We propose an algorithm for constructing more robust features, hamm-grams, which are a special class of regular expressions having a fixed length and single-character wildcards. We devise an efficient algorithm for finding common hamm-grams using a new locality-sensitive hash designed to produce collisions among pairs of small Hamming distance and a clustering within hash buckets to place wildcards. We then demonstrate the advantages of these features in malware classification and detection tasks.

---


### 43. [Geometry-Aware R-Structured Kolmogorov-Arnold Networks](https://arxiv.org/abs/2607.01449)

**<font color=#1a73e8>作者：</font>** Sergei Kucherenko, Nilay Shah  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a novel hybrid neural architecture, the Geometry-aware R-Structured Kolmogorov-Arnold Network (GRS-KAN), which integrates this http URL's R-functions into the Kolmogorov-Arnold Network (KAN) framework. The proposed approach combines two complementary modeling mechanisms: smooth nonlinear structure is learned by KAN branches, while known geometric or logical constraints are encoded analytically using differentiable R-functions. This enables explicit representation of discontinuities, feasible regions, and implicit geometric boundaries within a trainable neural architecture.
The framework implements differentiable logical operations through R-conjunctions and R-disjunctions, allowing complex geometric supports to be represented analytically and incorporated directly into regression models. Several GRS-KAN variants are introduced, including additive, multiplicative, and agnostic branch-weighted architectures.
The method is demonstrated on regression problems involving discontinuities with circular and rectangular supports. Numerical experiments show that explicit geometric encoding substantially improves predictive accuracy and boundary localization compared with standard KANs. In the considered benchmarks, geometry-aware GRS-KAN models reduce test RMSE by up to 67% while simultaneously improving interpretability through explicit analytical representation of the learned geometric structure. The agnostic variant further demonstrates the ability to automatically determine whether geometric priors are beneficial for a given learning task.

---


### 44. [Token Geometry](https://arxiv.org/abs/2607.01455)

**<font color=#1a73e8>作者：</font>** Kathan Shah  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models learn continuous programs over discrete symbols, with the embedding table and LM-head acting as the read/write interface between them. We show that this interface has gradient geometry distinct from dense hidden weights which can be exploited to improve the Pareto frontier across supervised finetuning, RL, and pretraining, while only utilizing kilobytes of optimizer state. We introduce Ember, a lightweight optimizer for embedding and LM-head matrices that utilizes O(V + D) VRAM, instead of Adam's O(2VD), and forgoes the need to shard both token table optimizer states. We provide empirical evidence that Ember scales effectively across batch size and parameter count. We show that the optimization trajectory of tokens can be well described by a simple 1D ray, counter to the popular belief that neural net parameters navigate a heavily nonconvex landscape. We provide a principled view on the surprisingly narrow space of optimizers that suffice for Transformer training. Finally, we open-source our distributed Ember implementation that merges cleanly with existing ZeRO/FSDP setups to support further research at this https URL

---


### 45. [Comparing Architectures for Supervised Political Scaling](https://arxiv.org/abs/2607.01464)

**<font color=#1a73e8>作者：</font>** Anna Golub, Sebastian Padó  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text scaling, the task of positioning political actors on an ideological scale, is a fundamental task in political analysis. To ease the need for manual analysis, various NLP methods have been proposed for this task, including classification- and regression-based approaches, showing successes as well as limitations. The goal of our paper is to consolidate the state of the art in this area. We ask two questions: (a) Can the performance of scaling methods be improved by predicting scales not individually but jointly? (b) Is there a middle ground between classification and regression?

---


### 46. [World Feedback for Clinical Agents: Diagnosing RL in FHIR Environments](https://arxiv.org/abs/2607.01470)

**<font color=#1a73e8>作者：</font>** Ananya Mantravadi, Harshit Rajgarhia, Prasanna Desikan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical protocol-execution tasks -- checking a lab value, applying a threshold, placing a correctly structured FHIR order -- are natural candidates for RL from world feedback: once clinical SMEs encode decision logic into a verifier, that verifier grades unlimited rollouts without per-episode annotation. But applying RL requires a sound feedback channel and sufficient base capability. We audit MedAgentBench v1/v2, find a 41.7\% silent-finish ceiling that makes inaction the RL dominant strategy, and construct \textbf{MedAgentBench-v3 (MAB-v3)} (508 tasks, 8.9\% ceiling). Training Qwen3-8B exposes two structural barriers: a \emph{capability ceiling} (10/20 task types have 0\% base performance, zero gradient) and a \emph{format-knowledge barrier} (3/20 types require exact clinical codes undiscoverable by exploration). Pure RL reaches 18.2\% pass@1 vs.\ 34.1\% for rule-based SFT; the 15.9~pp gap is attributable entirely to these barriers. A decision/format-knowledge/lookup taxonomy predicts RL learnability and prescribes the fix: SFT to inject codes, RL to learn conditionals.

---


### 47. [Class-Grouped Normalized Momentum and Faster Hyperparameter Exploration to Tackle Class Imbalance in Federated Learning](https://arxiv.org/abs/2607.01474)

**<font color=#1a73e8>作者：</font>** Haemin Park, Diego Klabjan, Martin W. Braun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Class imbalance poses a critical challenge in federated learning (FL), where underrepresented classes suffer from poor predictive performance yet cannot be addressed by standard centralized techniques due to privacy and heterogeneity constraints. We propose FedCGNM (Federated Class-Grouped Normalized Momentum), a client-side optimizer in FL that partitions classes into a small number of groups based on minimum within-group variance, maintains a momentum per group, normalizes each group momentum to unit length, and uses the summation of the normalized group momentums as an update direction. This design both equalizes gradient magnitude across majority and minority groups and mitigates the noise inherent in rare-class gradients. We further provide a theoretical convergence analysis explicitly accounting for time-varying resampling-rates. Additionally, to efficiently optimize these rates in small-client regimes, we introduce FedHOO, an X-armed-bandit (XAB) based algorithm that exploits federated parallelism that evaluates many combinations of two candidate rates per client at linear cost. Empirical evaluation on four public long-tailed benchmarks and a proprietary chip-defect dataset demonstrates that FedCGNM consistently outperforms baselines, with FedHOO yielding further gains in small-scale federations.

---


### 48. [How to Allocate Your Tokens? Scaling Laws with Training Steps and Batch Size](https://arxiv.org/abs/2607.01487)

**<font color=#1a73e8>作者：</font>** Fabian Schaipp  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a scaling law that takes into account model size and training data while explicitly splitting the latter into training steps and batch size (called three-term law). Fitting the proposed law on a large set of training runs, we find that it correctly recovers the scaling of the optimal batch size. Moreover, because it makes use of training runs with suboptimal batch size, our proposed law can be robustly fit with a significantly smaller amount of training runs. We further show that the three-term law can be used to derive scaling laws for suboptimal batch sizes, and that it matches previous empirical findings related to the critical batch size.

---


### 49. [Don't Let Gains FADE: Breaking Down Policy Gradient Weights in RL](https://arxiv.org/abs/2607.01490)

**<font color=#1a73e8>作者：</font>** Juliette Decugis, Sean O'Brien, Francis Bach 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning post-training dramatically improves LLM reasoning, but suffers from training instability and diversity collapse. Advantage functions offer an appealing fix: they reshape the training objective, reweight which rollouts drive learning, and are trivial to implement. Yet a proliferation of methods makes it unclear which advantage to use and when. We cut through the confusion with a unifying framework that decomposes any advantage into its positive and negative gradient mass along two orthogonal axes. On the sign axis, imbalanced updates collapse either entropy or weight geometry. On the difficulty axis, hard-problem focus sharpens signal but costs sample size. Both trade-offs shift during training: exploration favors balance and hard focus; exploitation favors suppression and medium focus. This motivates FADE (Focal Advantage with Dynamic Entropy), a self-adapting advantage that reads training dynamics to schedule the gradient weight automatically. FADE reaches peak pass@1 20k steps earlier than the best static baseline at the 7B scale and 2k steps earlier at the 32B , while achieving the best accuracy-diversity trade-off across all pass@k on LiveCodeBench and AIME.

---


### 50. [Unveiling the Non-Monotonic Effect of Privacy on Generalization under Byzantine Robustness](https://arxiv.org/abs/2607.01492)

**<font color=#1a73e8>作者：</font>** Thomas Boudou, Batiste Le Bars, Nirupam Gupta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work has established a fundamental trilemma between Byzantine robustness, local differential privacy (LDP), and optimization error in distributed learning. We show that this trilemma does not universally extend to generalization error, but instead depends critically on the privacy regime. Specifically, in the high-noise regime (strong privacy), we prove that increasing privacy reduces the generalization error, i.e., there is no tension between robustness and privacy. In the low-noise regime (weaker privacy), however, the tension between robustness and privacy reappears and increasing privacy indeed degrades generalization. Our theory explains this surprising non-monotonic behavior of the generalization error via matching lower and upper bounds on the algorithmic stability of Byzantine-robust distributed learning under LDP constraints. We corroborate and further analyze these theoretical findings with empirical evaluations.

---


> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-266](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
