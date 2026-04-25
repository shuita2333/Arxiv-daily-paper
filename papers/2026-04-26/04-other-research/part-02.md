# 📦 其他研究 | 2026年04月26日

> 本类共 **231** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-231](./part-05.md)

---

### 51. [GRISP: Guided Recurrent IRI Selection over SPARQL Skeletons](https://arxiv.org/abs/2604.21133)

**<font color=#1a73e8>作者：</font>** Sebastian Walter, Hannah Bast  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present GRISP (Guided Recurrent IRI Selection over SPARQL Skeletons), a novel SPARQL-based question-answering method over knowledge graphs based on fine-tuning a small language model (SLM). Given a natural-language question, the method first uses the SLM to generate a natural-language SPARQL query skeleton, and then to re-rank and select knowledge graph items to iteratively replace the natural-language placeholders using knowledge graph constraints. The SLM is jointly trained on skeleton generation and list-wise re-ranking data generated from standard question-query pairs. We evaluate the method on common Wikidata and Freebase benchmarks, and achieve better results than other state-of-the-art methods in a comparable setting.

---


### 52. [Beyond Pixels: Introspective and Interactive Grounding for Visualization Agents](https://arxiv.org/abs/2604.21134)

**<font color=#1a73e8>作者：</font>** Yiyang Lu, Woong Shin, Ahmad Maroof Karimi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) frequently misread values, hallucinate details, and confuse overlapping elements in charts. Current approaches rely solely on pixel interpretation, creating a Pixel-Only Bottleneck: agents treat interactive charts as static images, losing access to the structured specification that encodes exact values. We introduce Introspective and Interactive Visual Grounding (IVG), a framework that combines (1) spec-grounded introspection, which queries the underlying specification for deterministic evidence, with (2) view-grounded interaction, which manipulates the view to resolve visual ambiguity. To enable evaluation without VLM bias, we present iPlotBench, a benchmark of 500 interactive Plotly figures with 6,706 binary questions and ground-truth specifications. Experiments show that introspection improves data reconstruction fidelity, while the combination with interaction achieves the highest QA accuracy (0.81), with +6.7 % gains on overlapping geometries. We further demonstrate IVG in deployed agents that explore data autonomously and collaborate with human users in real time.

---


### 53. [Enhancing Science Classroom Discourse Analysis through Joint Multi-Task Learning for Reasoning-Component Classification](https://arxiv.org/abs/2604.21137)

**<font color=#1a73e8>作者：</font>** Jiho Noh, Mukhesh Raghava Katragadda, Raymond Carl 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Analyzing the reasoning patterns of students in science classrooms is critical for understanding knowledge construction mechanism and improving instructional practice to maximize cognitive engagement, yet manual coding of classroom discourse at scale remains prohibitively labor-intensive. We present an automated discourse analysis system (ADAS) that jointly classifies teacher and student utterances along two complementary dimensions: Utterance Type and Reasoning Component derived from our prior CDAT framework. To address severe label imbalance among minority classes, we (1) stratify-resplit the annotated corpus, (2) apply LLM-based synthetic data augmentation targeting minority classes, and (3) train a dual-probe head RoBERTa-base classifier. A zero-shot GPT-5.4 baseline achieves macro-F1 of 0.467 on UT and 0.476 on RC, establishing meaningful upper bounds for prompt-only approaches motivating fine-tuning. Beyond classification, we conduct discourse pattern analyses including UTxRC co-occurrence profiling, Cognitive Complexity Index (CCI) computation per session, lag-sequential analysis, and IRF chain analysis, revealing that teacher Feedback-with-Question (Fq) moves are the most consistent antecedents of student inferential reasoning (SR-I). Our results demonstrate that LLM-based augmentation meaningfully improves UT minority-class recognition, and that the structural simplicity of the RC task makes it tractable even for lexical baselines.

---


### 54. [Using Machine Mental Imagery for Representing Common Ground in Situated Dialogue](https://arxiv.org/abs/2604.21144)

**<font color=#1a73e8>作者：</font>** Biswesh Mohapatra, Giovanni Duca, Laurent Romary 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Situated dialogue requires speakers to maintain a reliable representation of shared context rather than reasoning only over isolated utterances. Current conversational agents often struggle with this requirement, especially when the common ground must be preserved beyond the immediate context window. In such settings, fine-grained distinctions are frequently compressed into purely textual representations, leading to a critical failure mode we call \emph{representational blur}, in which similar but distinct entities collapse into interchangeable descriptions. This semantic flattening creates an illusion of grounding, where agents appear locally coherent but fail to track shared context persistently over time. Inspired by the role of mental imagery in human reasoning, and based on the increased availability of multimodal models, we explore whether conversational agents can be given an analogous ability to construct some depictive intermediate representations during dialogue to address these limitations. Thus, we introduce an active visual scaffolding framework that incrementally converts dialogue state into a persistent visual history that can later be retrieved for grounded response generation. Evaluation on the IndiRef benchmark shows that incremental externalization itself improves over full-dialog reasoning, while visual scaffolding provides additional gains by reducing representational blur and enforcing concrete scene commitments. At the same time, textual representations remain advantageous for non-depictable information, and a hybrid multimodal setting yields the best overall performance. Together, these findings suggest that conversational agents benefit from an explicitly multimodal representation of common ground that integrates depictive and propositional information.

---


### 55. [WFM: 3D Wavelet Flow Matching for Ultrafast Multi-Modal MRI Synthesis](https://arxiv.org/abs/2604.21146)

**<font color=#1a73e8>作者：</font>** Yalcin Tur, Mihajlo Stojkovic, Ulas Bagci  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have achieved remarkable quality in multi-modal MRI synthesis, but their computational cost (hundreds of sampling steps and separate models per modality) limits clinical deployment. We observe that this inefficiency stems from an unnecessary starting point: diffusion begins from pure noise, discarding the structural information already present in available MRI sequences. We propose WFM (Wavelet Flow Matching), which instead learns a direct flow from an informed prior, the mean of conditioning modalities in wavelet space, to the target distribution. Because the source and target share underlying anatomy and differ primarily in contrast, this formulation enables accurate synthesis in just 1-2 integration steps. A single 82M-parameter model with class conditioning synthesizes all four BraTS modalities (T1, T1c, T2, FLAIR), replacing four separate diffusion models totaling 326M parameters. On BraTS 2024, WFM achieves 26.8 dB PSNR and 0.94 SSIM, within 1-2 dB of diffusion baselines, while running 250-1000x faster (0.16-0.64s vs. 160s per volume). This speed-quality trade-off makes real-time MRI synthesis practical for clinical workflows. Code is available at this https URL.

---


### 56. ["This Wasn't Made for Me": Recentering User Experience and Emotional Impact in the Evaluation of ASR Bias](https://arxiv.org/abs/2604.21148)

**<font color=#1a73e8>作者：</font>** Siyu Liang, Alicia Beckford Wassink  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Studies on bias in Automatic Speech Recognition (ASR) tend to focus on reporting error rates for speakers of underrepresented dialects, yet less research examines the human side of system bias: how do system failures shape users' lived experiences, how do users feel about and react to them, and what emotional toll do these repeated failures exact? We conducted user experience studies across four U.S. locations (Atlanta, Gulf Coast, Miami Beach, and Tucson) representing distinct English dialect communities. Our findings reveal that most participants report technologies fail to consider their cultural backgrounds and require constant adjustment to achieve basic functionality. Despite these experiences, participants maintain high expectations for ASR performance and express strong willingness to contribute to model improvement. Qualitative analysis of open-ended narratives exposes the deeper costs of these failures. Participants report frustration, annoyance, and feelings of inadequacy, yet the emotional impact extends beyond momentary reactions. Participants recognize that systems were not designed for them, yet often internalize failures as personal inadequacy despite this critical awareness. They perform extensive invisible labor, including code-switching, hyper-articulation, and emotional management, to make failing systems functional. Meanwhile, their linguistic and cultural knowledge remains unrecognized by technologies that encode particular varieties as standard while rendering others marginal. These findings demonstrate that algorithmic fairness assessments based on accuracy metrics alone miss critical dimensions of harm: the emotional labor of managing repeated technological rejection, the cognitive burden of constant self-monitoring, and the psychological toll of feeling inadequate in one's native language variety.

---


### 57. [Image-Based Malware Type Classification on MalNet-Image Tiny: Effects of Multi-Scale Fusion, Transfer Learning, Data Augmentation, and Schedule-Free Optimization](https://arxiv.org/abs/2604.21153)

**<font color=#1a73e8>作者：</font>** Ahmed A. Abouelkhaire, Waleed A. Yousef, Issa Traor  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper studies 43-class malware type classification on MalNet-Image Tiny, a public benchmark derived from Android APK files. The goal is to assess whether a compact image classifier benefits from four components evaluated in a controlled ablation: a feature pyramid network (FPN) for scale variation induced by resizing binaries of different lengths, ImageNet pretraining, lightweight augmentation through Mixup and TrivialAugment, and schedule-free AdamW optimization. All experiments use a ResNet18 backbone and the provided train/validation/test split. Reproducing the benchmark-style configuration yields macro-F1 (F1_macro) of 0.6510, consistent with the reported baseline of approximately 0.65. Replacing the optimizer with schedule-free AdamW and using unweighted cross-entropy increases F1_macro to 0.6535 in 10 epochs, compared with 96 epochs for the reproduced baseline. The best configuration combines pretraining, Mixup, TrivialAugment, and FPN, reaching F1_macro=0.6927, P_macro=0.7707, AUC_macro=0.9556, and L_test=0.8536. The ablation indicates that the largest gains in F1_macro arise from pretraining and augmentation, whereas FPN mainly improves P_macro, AUC_macro, and L_test in the strongest configuration.

---


### 58. [Multi-Agent Empowerment and Emergence of Complex Behavior in Groups](https://arxiv.org/abs/2604.21155)

**<font color=#1a73e8>作者：</font>** Tristan Shah, Ilya Nemenman, Daniel Polani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Intrinsic motivations are receiving increasing attention, i.e. behavioral incentives that are not engineered, but emerge from the interaction of an agent with its surroundings. In this work we study the emergence of behaviors driven by one such incentive, empowerment, specifically in the context of more than one agent. We formulate a principled extension of empowerment to the multi-agent setting, and demonstrate its efficient calculation. We observe that this intrinsic motivation gives rise to characteristic modes of group-organization in two qualitatively distinct environments: a pair of agents coupled by a tendon, and a controllable Vicsek flock. This demonstrates the potential of intrinsic motivations such as empowerment to not just drive behavior for only individual agents but also higher levels of behavioral organization at scale.

---


### 59. [Reinforcing 3D Understanding in Point-VLMs via Geometric Reward Credit Assignment](https://arxiv.org/abs/2604.21160)

**<font color=#1a73e8>作者：</font>** Jingkun Chen, Ruoshi Xu, Mingqi Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Point-Vision-Language Models promise to empower embodied agents with executable spatial reasoning, yet they frequently succumb to geometric hallucination where predicted 3D structures contradict the observed 2D reality. We identify a key cause of this failure not as a representation bottleneck but as a structural misalignment in reinforcement learning, where sparse geometric tokens are drowned out by noisy and broadcasted sequence-level rewards. To resolve this causal dilution, we propose Geometric Reward Credit Assignment, a framework that disentangles holistic supervision into field-specific signals and routes them exclusively to their responsible token spans. This mechanism transforms vague feedback into precise gradient updates and effectively turns generic policy optimization into targeted structural alignment. Furthermore, we internalize physical constraints via a Reprojection-Consistency term which serves as a cross-modal verifier to penalize physically impossible geometries. Validated on a calibrated benchmark derived from ShapeNetCore, our approach bridges the reliability gap by boosting 3D KPA from 0.64 to 0.93, increasing 3D bounding box intersection over union to 0.686, and raising reprojection consistency scores to 0.852. Crucially, these gains are achieved while maintaining robust 2D localization performance, marking a meaningful step from plausible textual outputs toward physically verifiable spatial predictions.

---


### 60. [Position Paper: Denial-of-Service Against Multi-Round Transaction Simulation](https://arxiv.org/abs/2604.21169)

**<font color=#1a73e8>作者：</font>** Yuzhe Tang, Yibo Wang, Wanning Ding 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In Ethereum, transaction-bundling services are a critical component of block builders, such as Flashbots Bundles, and are widely used by MEV searchers. Disrupting bundling services can degrade searcher experience and reduce builder revenue. Despite the extensive studies, the existing denial-of-service attack designs are ineffective against bundling services due to their unique multi-round execution model.
This paper studies the open problem of asymmetric denial-of-service against bundling services. We develop evasive, risk-free, and low-cost DoS attacks on Flashbots' bundling service, the only open-source bundling service known to us. Our attacks exploit inter-transaction dependencies through contract state to achieve evasiveness, and abuse bundling-specific features, such as atomic block inclusion, to significantly reduce both capital and operational costs of the attack.
Experimental results show that our attacks achieve high success rates, substantially reduce builders' revenue, and slow block production. We further propose mitigation strategies for the identified risks.

---


### 61. [Graph Neural Network-Informed Predictive Flows for Faster Ford-Fulkerson and PAC-Learnability](https://arxiv.org/abs/2604.21175)

**<font color=#1a73e8>作者：</font>** Eleanor Wiesler, Trace Baxley  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a learning-augmented framework for accelerating max-flow computation and image segmentation by integrating Graph Neural Networks (GNNs) with the Ford-Fulkerson algorithm. Rather than predicting initial flows, our method learns edge importance probabilities to guide augmenting path selection. We introduce a Message Passing GNN (MPGNN) that jointly learns node and edge embeddings through coupled updates, capturing both global structure and local flow dynamics such as residual capacity and bottlenecks.
Given an input image, we propose a method to construct a grid-based flow network with source and sink nodes, extract features, and perform a single GNN inference to assign edge probabilities reflecting their likelihood of belonging to high-capacity cuts. These probabilities are stored in a priority queue and used to guide a modified Ford-Fulkerson procedure, prioritizing augmenting paths via an Edmonds-Karp-style search with bottleneck-aware tie-breaking. This avoids repeated inference over residual graphs while leveraging learned structure throughout optimization.
We further introduce a bidirectional path construction strategy centered on high-probability edges and provide a theoretical framework relating prediction quality to efficiency via a weighted permutation distance metric. Our method preserves max-flow/min-cut optimality while reducing the number of augmentations in practice. We also outline a hybrid extension combining flow warm-starting with edge-priority prediction, establishing a foundation for learning-guided combinatorial optimization in image segmentation.

---


### 62. [WildSplatter: Feed-forward 3D Gaussian Splatting with Appearance Control from Unconstrained Images](https://arxiv.org/abs/2604.21182)

**<font color=#1a73e8>作者：</font>** Yuki Fujimura, Takahiro Kushida, Kazuya Kitano 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose WildSplatter, a feed-forward 3D Gaussian Splatting (3DGS) model for unconstrained images with unknown camera parameters and varying lighting conditions. 3DGS is an effective scene representation that enables high-quality, real-time rendering; however, it typically requires iterative optimization and multi-view images captured under consistent lighting with known camera parameters. WildSplatter is trained on unconstrained photo collections and jointly learns 3D Gaussians and appearance embeddings conditioned on input images. This design enables flexible modulation of Gaussian colors to represent significant variations in lighting and appearance. Our method reconstructs 3D Gaussians from sparse input views in under one second, while also enabling appearance control under diverse lighting conditions. Experimental results demonstrate that our approach outperforms existing pose-free 3DGS methods on challenging real-world datasets with varying illumination.

---


### 63. [Physically Unclonable Functions for Secure IoT Authentication and Hardware-Anchored AI Model Integrity](https://arxiv.org/abs/2604.21188)

**<font color=#1a73e8>作者：</font>** Maryam Taghi Zadeh, Mohsen Ahmadi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid integration of artificial intelligence (AI) into Internet of Things (IoT) and edge computing systems has intensified the need for robust, hardware-rooted trust mechanisms capable of ensuring device authenticity and AI model integrity under strict resource and security constraints. This survey reviews and synthesizes existing literature on hardware-rooted trust mechanisms for AI-enabled IoT systems. It systematically examines and compares representative trust anchor mechanisms, including Trusted Platform Module (TPM)-based measurement and attestation, silicon and FPGA-based Physical Unclonable Functions (PUFs), hybrid container-aware hardware roots of trust, and software-only security approaches. The analysis highlights how hardware-rooted solutions generally provide stronger protection against physical tampering and device cloning compared to software-only approaches, particularly in adversarial and physically exposed environments, while hybrid designs extend hardware trust into runtime and containerized environments commonly used in modern edge deployments. By evaluating trade-offs among security strength, scalability, cost, and deployment complexity, the study shows that PUF-based and hybrid trust anchors offer a promising balance for large-scale, AI-enabled IoT systems, whereas software-only trust mechanisms remain insufficient in adversarial and physically exposed settings. The presented comparison aims to clarify current design challenges and guide future development of trustworthy AI-enabled IoT platforms.

---


### 64. [SpatiO: Adaptive Test-Time Orchestration of Vision-Language Agents for Spatial Reasoning](https://arxiv.org/abs/2604.21190)

**<font color=#1a73e8>作者：</font>** Chan Yeong Hwang, Miso Choi, Sunghyun On 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding visual scenes requires not only recognizing objects but also reasoning about their spatial relationships. Unlike general vision-language tasks, spatial reasoning requires integrating multiple inductive biases, such as 2D appearance cues, depth signals, and geometric constraints, whose reliability varies across contexts. This suggests that effective spatial reasoning requires \emph{spatial adaptability}: the ability to flexibly coordinate different reasoning strategies depending on the input. However, most existing approaches rely on a single reasoning pipeline that implicitly learns a fixed spatial prior, limiting their ability to adapt under distribution changes. Multi-agent systems offer a promising alternative by aggregating diverse reasoning trajectories, but prior attempts in spatial reasoning primarily employ homogeneous agents, restricting the diversity of inductive biases they can leverage. In this work, we introduce \textbf{\textsc{SpatiO}}, a heterogeneous multi-agent framework for spatial reasoning that coordinates multiple vision-language specialists with complementary inductive biases. To enable effective collaboration, we propose \textbf{Test-Time Orchestration (TTO)}, an optimization mechanism that dynamically evaluates and reweights agents based on their observed reliability during inference, without modifying model parameters. Extensive experiments on diverse spatial reasoning benchmarks, including 3DSRBench, STVQA-7k, CV-Bench, and Omni3D-Bench, demonstrate that \textsc{SpatiO} consistently improves spatial reasoning performance over both closed-source and open-source baselines.

---


### 65. [Prefix Parsing is Just Parsing](https://arxiv.org/abs/2604.21191)

**<font color=#1a73e8>作者：</font>** Clemente Pasti, Andreas Opedal, Timothy J. O'Donnell 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prefix parsing asks whether an input prefix can be extended to a complete string generated by a given grammar. In the weighted setting, it also provides prefix probabilities, which are central to context-free language modeling, psycholinguistic analysis, and syntactically constrained generation from large language models. We introduce the prefix grammar transformation, an efficient reduction of prefix parsing to ordinary parsing. Given a grammar, our method constructs another grammar that generates exactly the prefixes of its original strings. Prefix parsing is then solved by applying any ordinary parsing algorithm on the transformed grammar without modification. The reduction is both elegant and practical: the transformed grammar is only a small factor larger than the input, and any optimized implementation can be used directly, eliminating the need for bespoke prefix-parsing algorithms. We also present a strategy-based on algorithmic differentiation-for computing the next-token weight vector, i.e., the prefix weights of all one-token extensions, enabling efficient prediction of the next token. Together, these contributions yield a simple, general, and efficient framework for prefix parsing.

---


### 66. [A Probabilistic Framework for Improving Dense Object Detection in Underwater Image Data via Annealing-Based Data Augmentation](https://arxiv.org/abs/2604.21198)

**<font color=#1a73e8>作者：</font>** Eleanor Wiesler, Trace Baxley  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object detection models typically perform well on images captured in controlled environments with stable lighting, water clarity, and viewpoint, but their performance degrades substantially in real-world underwater settings characterized by high variability and frequent occlusions. In this work, we address these challenges by introducing a novel data augmentation framework designed to improve robustness in dense and unconstrained underwater scenes. Using the DeepFish dataset, which contains images of fish in natural environments, we first generate bounding box annotations from provided segmentation masks to construct a custom detection dataset. We then propose a pseudo-simulated annealing-based augmentation algorithm, inspired by the copy-paste strategy of Deng et al. [1], to synthesize realistic crowded fish scenarios. Our approach improves spatial diversity and object density during training, enabling better generalization to complex scenes. Experimental results show that our method significantly outperforms a baseline YOLOv10 model, particularly on a challenging test set of manually annotated images collected from live-stream footage in the Florida Keys. These results demonstrate the effectiveness of our augmentation strategy for improving detection performance in dense, real-world underwater environments.

---


### 67. [On Reasoning Behind Next Occupation Recommendation](https://arxiv.org/abs/2604.21204)

**<font color=#1a73e8>作者：</font>** Shan Dong, Palakorn Achananuparp, Hieu Hien Mai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this work, we develop a novel reasoning approach to enhance the performance of large language models (LLMs) in future occupation prediction. In this approach, a reason generator first derives a ``reason'' for a user using his/her past education and career history. The reason summarizes the user's preference and is used as the input of an occupation predictor to recommend the user's next occupation. This two-step occupation prediction approach is, however, non-trivial as LLMs are not aligned with career paths or the unobserved reasons behind each occupation decision. We therefore propose to fine-tune LLMs improving their reasoning and occupation prediction performance. We first derive high-quality oracle reasons, as measured by factuality, coherence and utility criteria, using a LLM-as-a-Judge. These oracle reasons are then used to fine-tune small LLMs to perform reason generation and next occupation prediction. Our extensive experiments show that: (a) our approach effectively enhances LLM's accuracy in next occupation prediction making them comparable to fully supervised methods and outperforming unsupervised methods; (b) a single LLM fine-tuned to perform reason generation and occupation prediction outperforms two LLMs fine-tuned to perform the tasks separately; and (c) the next occupation prediction accuracy depends on the quality of generated reasons. Our code is available at this https URL.

---


### 68. [When Constraints Limit and Inspire: Characterizing Presentation Authoring Practices for Evolving Narratives](https://arxiv.org/abs/2604.21205)

**<font color=#1a73e8>作者：</font>** Linxiu Zeng, Emily Kuang, Jian Zhao  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Authoring presentation slides involves navigating contextual constraints that shape how content is structured, adapted, and reused. While prior work frames constraints as limitations, little is known about how presenters actively reason about them. We conducted a formative study with ten presenters to examine how constraints emerge, are interpreted, and influence authoring decisions, leading to the Constraint-based Multi-session Presentation Authoring (CMPA) framework. CMPA treats time, audience, and communicative intent as key constraints shaping authoring. We instantiated CMPA in ReSlide, a research prototype for constraint-aware slide creation and reuse, and conducted two user studies on (1) single-session behaviors and (2) multi-session workflows. Compared to a baseline tool, ReSlide helped presenters treat constraints as active design drivers that guide narrative construction. The second study further shows how presenters flexibly reuse and adapt content across authoring cycles as constraints evolve. We then propose design implications for future constraint-aware presentation tools.

---


### 69. [Subject-level Inference for Realistic Text Anonymization Evaluation](https://arxiv.org/abs/2604.21211)

**<font color=#1a73e8>作者：</font>** Myeong Seok Oh, Dong-Yun Kim, Hanseok Oh 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Current text anonymization evaluation relies on span-based metrics that fail to capture what an adversary could actually infer, and assumes a single data subject, ignoring multi-subject scenarios. To address these limitations, we present SPIA (Subject-level PII Inference Assessment), the first benchmark that shifts the unit of evaluation from text spans to individuals, comprising 675 documents across legal and online domains with novel subject-level protection metrics. Extensive experiments show that even when over 90% of PII spans are masked, subject-level inference protection drops as low as 33%, leaving the majority of personal information recoverable through contextual inference. Furthermore, target-subject-focused anonymization leaves non-target subjects substantially more exposed than the target subject. We show that subject-level inference-based evaluation is essential for ensuring safe text anonymization in real-world settings.

---


### 70. [The Recurrent Transformer: Greater Effective Depth and Efficient Decoding](https://arxiv.org/abs/2604.21215)

**<font color=#1a73e8>作者：</font>** Costin-Andrei Oncescu, Depen Morwani, Samy Jelassi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers process tokens in parallel but are temporally shallow: at position $t$, each layer attends to key-value pairs computed based on the previous layer, yielding a depth capped by the number of layers. Recurrent models offer unbounded temporal depth but suffer from optimization instability and historically underutilize modern accelerators. We introduce the Recurrent Transformer, a simple architectural change where each layer attends to key-value pairs computed off its own activations, yielding layerwise recurrent memory while preserving standard autoregressive decoding cost. We show that the architecture can emulate both (i) a conventional Transformer and (ii) token-to-token recurrent updates under mild assumptions, while avoiding optimization instability. Naively, prefill/training appears bandwidth-bound with effective arithmetic intensity near $1$ because keys and values are revealed sequentially; we give an exact tiling-based algorithm that preserves the mathematical computation while reducing HBM traffic from $\Theta(N^2)$ to $\Theta(N\log N)$, increasing effective arithmetic intensity to $\Theta(N/\log N)$ for sequence length $N$. On 150M and 300M parameter C4 pretraining, Recurrent Transformers improve cross-entropy over a parameter-matched Transformer baseline and achieve the improvement with fewer layers (fixed parameters), suggesting that recurrence can trade depth for width, thus reducing KV cache memory footprint and inference latency.

---


### 71. [Sparse Forcing: Native Trainable Sparse Attention for Real-time Autoregressive Diffusion Video Generation](https://arxiv.org/abs/2604.21221)

**<font color=#1a73e8>作者：</font>** Boxun Xu, Yuming Du, Zichang Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Sparse Forcing, a training-and-inference paradigm for autoregressive video diffusion models that improves long-horizon generation quality while reducing decoding latency. Sparse Forcing is motivated by an empirical observation in autoregressive diffusion rollouts: attention concentrates on a persistent subset of salient visual blocks, forming an implicit spatiotemporal memory in the KV cache, and exhibits a locally structured block-sparse pattern within sliding windows. Building on this observation, we propose a trainable native sparsity mechanism that learns to compress, preserve, and update these persistent blocks while restricting computation within each local window to a dynamically selected local neighborhood. To make the approach practical at scale for both training and inference, we further propose Persistent Block-Sparse Attention (PBSA), an efficient GPU kernel that accelerates sparse attention and memory updates for low-latency, memory-efficient decoding. Experiments show that Sparse Forcing improves the VBench score by +0.26 over Self-Forcing on 5-second text-to-video generation while delivering a 1.11-1.17x decoding speedup and 42% lower peak KV-cache footprint. The gains are more pronounced on longer-horizon rollouts, delivering improved visual quality with +0.68 and +2.74 VBench improvements, and 1.22x and 1.27x speedups on 20-second and 1-minute generations, respectively.

---


### 72. [UAU-Net: Uncertainty-aware Representation Learning and Evidential Classification for Facial Action Unit Detection](https://arxiv.org/abs/2604.21227)

**<font color=#1a73e8>作者：</font>** Yuze Li, Zhilei Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Facial action unit (AU) detection remains challenging because it involves heterogeneous, AU-specific uncertainties arising at both the representation and decision stages. Recent methods have improved discriminative feature learning, but they often treat the AU representations as deterministic, overlooking uncertainty caused by visual noise, subject-dependent appearance variations, and ambiguous inter-AU relationships, all of which can substantially degrade robustness. Meanwhile, conventional point-estimation classifiers often provide poorly calibrated confidence, producing overconfident predictions, especially under the severe label imbalance typical of AU datasets. We propose UAU-Net, an Uncertainty-aware AU detection framework that explicitly models uncertainty at both stages. At the representation stage, we introduce CV-AFE, a conditional VAE (CVAE)-based AU feature extraction module that learns probabilistic AU representations by jointly estimating feature means and variances across multiple spatio-temporal scales; conditioning on AU labels further enables CV-AFE to capture uncertainty associated with inter-AU dependencies. At the decision stage, we design AB-ENN, an Asymmetric Beta Evidential Neural Network for multi-label AU detection, which parameterizes predictive uncertainty with Beta distributions and mitigates overconfidence via an asymmetric loss tailored to highly imbalanced binary labels. Extensive experiments on BP4D and DISFA show that UAU-Net achieves strong AU detection performance, and further analyses indicate that modeling uncertainty in both representation learning and evidential prediction improves robustness and reliability.

---


### 73. [EngramaBench: Evaluating Long-Term Conversational Memory with Structured Graph Retrieval](https://arxiv.org/abs/2604.21229)

**<font color=#1a73e8>作者：</font>** Julian Acuna  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model assistants are increasingly expected to retain and reason over information accumulated across many sessions. We introduce EngramaBench, a benchmark for long-term conversational memory built around five personas, one hundred multi-session conversations, and one hundred fifty queries spanning factual recall, cross-space integration, temporal reasoning, adversarial abstention, and emergent synthesis. We evaluate Engrama, a graph-structured memory system, against GPT-4o full-context prompting and Mem0, an open-source vector-retrieval memory system. All three use the same answering model (GPT-4o), isolating the effect of memory architecture. GPT-4o full-context achieves the highest composite score (0.6186), while Engrama scores 0.5367 globally but is the only system to score higher than full-context prompting on cross-space reasoning (0.6532 vs. 0.6291, n=30). Mem0 is cheapest but substantially weaker (0.4809). Ablations reveal that the components driving Engrama's cross-space advantage trade off against global composite score, exposing a systems-level tension between structured memory specialization and aggregate optimization.

---


### 74. [Improving Performance in Classification Tasks with LCEN and the Weighted Focal Differentiable MCC Loss](https://arxiv.org/abs/2604.21252)

**<font color=#1a73e8>作者：</font>** Pedro Seber, Richard D. Braatz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The LASSO-Clip-EN (LCEN) algorithm was previously introduced for nonlinear, interpretable feature selection and machine learning. However, its design and use was limited to regression tasks. In this work, we create a modified version of the LCEN algorithm that is suitable for classification tasks and maintains its desirable properties, such as interpretability. This modified LCEN algorithm is evaluated on four widely used binary and multiclass classification datasets. In these experiments, LCEN is compared against 10 other model types and consistently reaches high test-set macro F$_1$ score and Matthews correlation coefficient (MCC) metrics, higher than that of the majority of investigated models. LCEN models for classification remain sparse, eliminating an average of 56% of all input features in the experiments performed. Furthermore, LCEN-selected features are used to retrain all models using the same data, leading to statistically significant performance improvements in three of the experiments and insignificant differences in the fourth when compared to using all features or other feature selection methods. Simultaneously, the weighted focal differentiable MCC (diffMCC) loss function is evaluated on the same datasets. Models trained with the diffMCC loss function are always the best-performing methods in these experiments, and reach test-set macro F$_1$ scores that are, on average, 4.9% higher and MCCs that are 8.5% higher than those obtained by models trained with the weighted cross-entropy loss. These results highlight the performance of LCEN as a feature selection and machine learning algorithm also for classification tasks, and how the diffMCC loss function can train very accurate models, surpassing the weighted cross-entropy loss in the tasks investigated.

---


### 75. [Planning Beyond Text: Graph-based Reasoning for Complex Narrative Generation](https://arxiv.org/abs/2604.21253)

**<font color=#1a73e8>作者：</font>** Hanwen Gu, Chao Guo, Junle Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While LLMs demonstrate remarkable fluency in narrative generation, existing methods struggle to maintain global narrative coherence, contextual logical consistency, and smooth character development, often producing monotonous scripts with structural fractures. To this end, we introduce PLOTTER, a framework that performs narrative planning on structural graph representations instead of the direct sequential text representations used in existing work. Specifically, PLOTTER executes the Evaluate-Plan-Revise cycle on the event graph and character graph. By diagnosing and repairing issues of the graph topology under rigorous logical constraints, the model optimizes the causality and narrative skeleton before complete context generation. Experiments demonstrate that PLOTTER significantly outperforms representative baselines across diverse narrative scenarios. These findings verify that planning narratives on structural graph representations-rather than directly on text-is crucial to enhance the long context reasoning of LLMs in complex narrative generation.

---


### 76. [Hyperloop Transformers](https://arxiv.org/abs/2604.21254)

**<font color=#1a73e8>作者：</font>** Abbas Zeitoun, Lucas Torroba-Hennigen, Yoon Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM architecture research generally aims to maximize model quality subject to fixed compute/latency budgets. However, many applications of interest such as edge and on-device deployment are further constrained by the model's memory footprint, thus motivating parameter-efficient architectures for language modeling. This paper describes a simple architecture that improves the parameter-efficiency of LLMs. Our architecture makes use of looped Transformers as a core primitive, which reuse Transformer layers across depth and are thus more parameter-efficient than ordinary (depth-matched) Transformers. We organize the looped Transformer into three blocks--begin, middle, and end blocks--where each block itself consists of multiple Transformer layers, and only the middle block is applied recurrently across depth. We augment the looped middle block with hyper-connections (Xie et al., 2026), which expand the residual stream into matrix-valued residual streams. Hyper-connections are applied only after each loop, and therefore add minimal new parameters and compute cost. Across various model scales, we find that our Hyper-Connected Looped Transformer (Hyperloop Transformer) is able to outperform depth-matched Transformer and mHC Transformer baselines despite using approximately 50% fewer parameters. The outperformance persists through post-training weight quantization, thus positioning Hyperloop Transformers as an attractive architecture for memory-efficient language modeling.

---


### 77. [Robustness Analysis of POMDP Policies to Observation Perturbations](https://arxiv.org/abs/2604.21256)

**<font color=#1a73e8>作者：</font>** Benjamin Kraske, Qi Heng Ho, Federico Rossi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Policies for Partially Observable Markov Decision Processes (POMDPs) are often designed using a nominal system model. In practice, this model can deviate from the true system during deployment due to factors such as calibration drift or sensor degradation, leading to unexpected performance degradation. This work studies policy robustness against deviations in the POMDP observation model. We introduce the Policy Observation Robustness Problem: to determine the maximum tolerable deviation in a POMDP's observation model that guarantees the policy's value remains above a specified threshold. We analyze two variants: the sticky variant, where deviations are dependent on state and actions, and the non-sticky variant, where they can be history-dependent. We show that the Policy Observation Robustness Problem can be formulated as a bi-level optimization problem in which the inner optimization is monotonic in the size of the observation deviation. This enables efficient solutions using root-finding algorithms in the outer optimization. For the non-sticky variant, we show that when policies are represented with finite-state controllers (FSCs) it is sufficient to consider observations which depend on nodes in the FSC rather than full histories. We present Robust Interval Search, an algorithm with soundness and convergence guarantees, for both the sticky and non-sticky variants. We show this algorithm has polynomial time complexity in the non-sticky variant and at most exponential time complexity in the sticky variant. We provide experimental results validating and demonstrating the scalability of implementations of Robust Interval Search to POMDP problems with tens of thousands of states. We also provide case studies from robotics and operations research which demonstrate the practical utility of the problem and algorithms.

---


### 78. [ECCFROG522PP: An Enhanced 522 bit Weierstrass Elliptic Curve](https://arxiv.org/abs/2604.21261)

**<font color=#1a73e8>作者：</font>** Victor Duarte Melo  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper presents ECCFROG522PP, a 522-bit prime-field elliptic curve in short Weierstrass form, designed with a focus on deterministic generation and public reproducibility. The central design principle is that all critical parameters are derived from a fixed public seed through a transparent and verifiable procedure. While many deployed systems rely on NIST P-256 and secp256k1, which target approximately 128-bit classical security, higher security applications typically consider curves such as NIST P-521, Curve448, and Brainpool P512. ECCFROG522PP is intended for the same general classical security range as P-521, with emphasis on transparency, auditability, and reproducibility rather than performance optimization.
The curve parameters are generated through a BLAKE3-based deterministic pipeline with publicly specified indices. The resulting construction has prime order, cofactor one, and a deterministically derived base point of full order. The quadratic twist has a large proven prime factor, and the construction includes a documented lower bound on the embedding degree together with standard sanity checks against low embedding degree reductions and basic CM discriminant anomalies.
The full generation and validation procedure can be reproduced end to end from public artifacts and reference scripts, enabling independent verification of all parameters and checks.

---


### 79. [Trustworthy Clinical Decision Support Using Meta-Predicates and Domain-Specific Languages](https://arxiv.org/abs/2604.21263)

**<font color=#1a73e8>作者：</font>** Michael Bouzinier, Sergey Trifonov, Michael Chumack 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> \textbf{Background:} Regulatory frameworks for AI in healthcare, including the EU AI Act and FDA guidance on AI/ML-based medical devices, require clinical decision support to demonstrate not only accuracy but auditability. Existing formal languages for clinical logic validate syntactic and structural correctness but not whether decision rules use epistemologically appropriate evidence.
\textbf{Methods:} Drawing on design-by-contract principles, we introduce meta-predicates -- predicates about predicates -- for asserting epistemological constraints on clinical decision rules expressed in a DSL. An epistemological type system classifies annotations along four dimensions: purpose, knowledge domain, scale, and method of acquisition. Meta-predicates assert which evidence types are permissible in any given rule. The framework is instantiated in AnFiSA, an open-source platform for genetic variant curation, and demonstrated using the Brigham Genomics Medicine protocol on 5.6 million variants from the Genome in a Bottle benchmark.
\textbf{Results:} Decision trees used in variant interpretation can be reformulated as unate cascades, enabling per-variant audit trails that identify which rule classified each variant and why. Meta-predicate validation catches epistemological errors before deployment, whether rules are human-written or AI-generated. The approach complements post-hoc methods such as LIME and SHAP: where explanation reveals what evidence was used after the fact, meta-predicates constrain what evidence may be used before deployment, while preserving human readability.
\textbf{Conclusions:} Meta-predicate validation is a step toward demonstrating not only that decisions are accurate but that they rest on appropriate evidence in ways that can be independently audited. While demonstrated in genomics, the approach generalises to any domain requiring auditable decision logic.

---


### 80. [Measure Twice, Click Once: Co-evolving Proposer and Visual Critic via Reinforcement Learning for GUI Grounding](https://arxiv.org/abs/2604.21268)

**<font color=#1a73e8>作者：</font>** Wenkai Wang, Xiyun Li, Hongcan Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graphical User Interface (GUI) grounding requires mapping natural language instructions to precise pixel coordinates. However, due to visually homogeneous elements and dense layouts, models typically grasp semantic intent yet struggle with achieving precise localization. While scaling sampling attempts (Pass@k) reveals potential gains, static self-consistency strategies derived from geometric clustering often yield limited improvements, as the model's predictions tend to be spatially dispersed. In this paper, we propose replacing static consistency strategies with a learnable selection mechanism that selects the optimal target by critiquing its own proposals rendered on the screenshot. Given the significant disparity between the model's grounding and critiquing capabilities, we propose a co-evolving Propose-then-Critic framework. To jointly optimize these, we introduce a maturity-aware adaptive co-evolutionary reinforcement learning paradigm. This approach dynamically balances the training objectives of proposer and critic, where the diversity of the proposer's outputs enhances critic robustness, while the critic's maturing discrimination capability conversely unlocks the proposer's potential for extensive spatial exploration, fostering the mutual reinforcement and co-evolution of both capabilities, thereby ensuring generalizability to adapt to diverse and complex interface layouts. Extensive experiments over 6 benchmarks show that our method significantly enhances both grounding accuracy and critic reliability.

---


### 81. [LatRef-Diff: Latent and Reference-Guided Diffusion for Facial Attribute Editing and Style Manipulation](https://arxiv.org/abs/2604.21279)

**<font color=#1a73e8>作者：</font>** Wenmin Huang, Weiqi Luo, Xiaochun Cao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Facial attribute editing and style manipulation are crucial for applications like virtual avatars and photo editing. However, achieving precise control over facial attributes without altering unrelated features is challenging due to the complexity of facial structures and the strong correlations between attributes. While conditional GANs have shown progress, they are limited by accuracy issues and training instability. Diffusion models, though promising, face challenges in style manipulation due to the limited expressiveness of semantic directions. In this paper, we propose LatRef-Diff, a novel diffusion-based framework that addresses these limitations. We replace the traditional semantic directions in diffusion models with style codes and propose two methods for generating them: latent and reference guidance. Based on these style codes, we design a style modulation module that integrates them into the target image, enabling both random and customized style manipulation. This module incorporates learnable vectors, cross-attention mechanisms, and a hierarchical design to improve accuracy and image quality. Additionally, to enhance training stability while eliminating the need for paired images (e.g., before and after editing), we propose a forward-backward consistency training strategy. This strategy first removes the target attribute approximately using image-specific semantic directions and then restores it via style modulation, guided by perceptual and classification losses. Extensive experiments on CelebA-HQ demonstrate that LatRef-Diff achieves state-of-the-art performance in both qualitative and quantitative evaluations. Ablation studies validate the effectiveness of our model's design choices.

---


### 82. [ImageHD: Energy-Efficient On-Device Continual Learning of Visual Representations via Hyperdimensional Computing](https://arxiv.org/abs/2604.21280)

**<font color=#1a73e8>作者：</font>** Jebacyril Arockiaraj, Dhruv Parikh, Viktor Prasanna  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> On-device continual learning (CL) is critical for edge AI systems operating on non-stationary data streams, but most existing methods rely on backpropagation or exemplar-heavy classifiers, incurring substantial compute, memory, and latency overheads. Hyperdimensional computing (HDC) offers a lightweight alternative through fast, non-iterative online updates. Combined with a compact convolutional neural network (CNN) feature extractor, HDC enables efficient on-device adaptation with strong visual representations. However, prior HDC-based CL systems often depend on multi-tier memory hierarchies and complex cluster management, limiting deployability on resource-constrained hardware.
We present ImageHD, an FPGA accelerator for on-device continual learning of visual data based on HDC. ImageHD targets streaming CL under strict latency and on-chip memory constraints, avoiding costly iterative optimization. At the algorithmic level, we introduce a hardware-aware CL method that bounds class exemplars through a unified exemplar memory and a hardware-efficient cluster merging strategy, while incorporating a quantized CNN front-end to reduce deployment overhead without sacrificing accuracy. At the system level, ImageHD is implemented as a streaming dataflow architecture on the AMD Zynq ZCU104 FPGA, integrating HDC encoding, similarity search, and bounded cluster management using word-packed binary hypervectors for massively parallel bitwise computation within tight on-chip resource budgets. On CORe50, ImageHD achieves up to 40.4x (4.84x) speedup and 383x (105.1x) energy efficiency over optimized CPU (GPU) baselines, demonstrating the practicality of HDC-enabled continual learning for real-time edge AI.

---


### 83. [Strategic Heterogeneous Multi-Agent Architecture for Cost-Effective Code Vulnerability Detection](https://arxiv.org/abs/2604.21282)

**<font color=#1a73e8>作者：</font>** Zhaohui Geoffrey Wang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Automated code vulnerability detection is critical for software security, yet existing approaches face a fundamental trade-off between detection accuracy and computational cost. We propose a heterogeneous multi-agent architecture inspired by game-theoretic principles, combining cloud-based LLM experts with a local lightweight verifier. Our "3+1" architecture deploys three cloud-based expert agents (DeepSeek-V3) that analyze code from complementary perspectives - code structure, security patterns, and debugging logic - in parallel, while a local verifier (Qwen3-8B) performs adversarial validation at zero marginal cost.
We formalize this design through a two-layer game framework: (1) a cooperative game among experts capturing super-additive value from diverse perspectives, and (2) an adversarial verification game modeling quality assurance incentives.
Experiments on 262 real samples from the NIST Juliet Test Suite across 14 CWE types, with balanced vulnerable and benign classes, demonstrate that our approach achieves a 77.2% F1 score with 62.9% precision and 100% recall at $0.002 per sample - outperforming both a single-expert LLM baseline (F1 71.4%) and Cppcheck static analysis (MCC 0). The adversarial verifier significantly improves precision (+10.3 percentage points, p < 1e-6, McNemar's test) by filtering false positives, while parallel execution achieves a 3.0x speedup.
Our work demonstrates that game-theoretic design principles can guide effective heterogeneous multi-agent architectures for cost-sensitive software engineering tasks.

---


### 84. [Cross-Entropy Is Load-Bearing: A Pre-Registered Scope Test of the K-Way Energy Probe on Bidirectional Predictive Coding](https://arxiv.org/abs/2604.21286)

**<font color=#1a73e8>作者：</font>** Jon-Paul Cacioli  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cacioli (2026) showed that the K-way energy probe on standard discriminative predictive coding networks reduces approximately to a monotone function of the log-softmax margin. The reduction rests on five assumptions, including cross-entropy (CE) at the output and effectively feedforward inference dynamics. This pre-registered study tests the reduction's sensitivity to CE removal using two conditions: standard PC trained with MSE instead of CE, and bidirectional PC (bPC; Oliviers, Tang & Bogacz, 2025). Across 10 seeds on CIFAR-10 with a matched 2.1M-parameter backbone, we find three results. The negative result replicates on standard PC: the probe sits below softmax (Delta = -0.082, p < 10^-6). On bPC the probe exceeds softmax across all 10 seeds (Delta = +0.008, p = 0.000027), though a pre-registered manipulation check shows that bPC does not produce materially greater latent movement than standard PC at this scale (ratio 1.6, threshold 10). Removing CE alone without changing inference dynamics halves the probe-softmax gap (Delta_MSE = -0.037 vs Delta_stdPC = -0.082). CE is a major empirically load-bearing component of the decomposition at this scale. CE training produces output logit norms approximately 15x larger than MSE or bPC training. A post-hoc temperature scaling ablation decomposes the probe-softmax gap into two components: approximately 66% is attributable to logit-scale effects removable by temperature rescaling, and approximately 34% reflects a scale-invariant ranking advantage of CE-trained representations. We use "metacognitive" operationally to denote Type-2 discrimination of a readout over its own Type-1 correctness, not to imply human-like introspective access.

---


### 85. [AttDiff-GAN: A Hybrid Diffusion-GAN Framework for Facial Attribute Editing](https://arxiv.org/abs/2604.21289)

**<font color=#1a73e8>作者：</font>** Wenmin Huang, Weiqi Luo, Xiaochun Cao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Facial attribute editing aims to modify target attributes while preserving attribute-irrelevant content and overall image fidelity. Existing GAN-based methods provide favorable controllability, but often suffer from weak alignment between style codes and attribute semantics. Diffusion-based methods can synthesize highly realistic images; however, their editing precision is limited by the entanglement of semantic directions among different attributes. In this paper, we propose AttDiff-GAN, a hybrid framework that combines GAN-based attribute manipulation with diffusion-based image generation. A key challenge in such integration lies in the inconsistency between one-step adversarial learning and multi-step diffusion denoising, which makes effective optimization difficult. To address this issue, we decouple attribute editing from image synthesis by introducing a feature-level adversarial learning scheme to learn explicit attribute manipulation, and then using the manipulated features to guide the diffusion process for image generation, while also removing the reliance on semantic direction-based editing. Moreover, we enhance style-attribute alignment by introducing PriorMapper, which incorporates facial priors into style generation, and RefineExtractor, which captures global semantic relationships through a Transformer for more precise style extraction. Experimental results on CelebA-HQ show that the proposed method achieves more accurate facial attribute editing and better preservation of non-target attributes than state-of-the-art methods in both qualitative and quantitative evaluations.

---


### 86. [GraphLeap: Decoupling Graph Construction and Convolution for Vision GNN Acceleration on FPGA](https://arxiv.org/abs/2604.21290)

**<font color=#1a73e8>作者：</font>** Anvitha Ramachandran, Dhruv Parikh, Viktor Prasanna  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Graph Neural Networks (ViGs) represent an image as a graph of patch tokens, enabling adaptive, feature-driven neighborhoods. Unlike CNNs with fixed grid biases or Vision Transformers with global token interactions, ViGs rely on dynamic graph convolution: at each layer, a feature-dependent graph is built via k-nearest-neighbor (kNN) search on current patch features, followed by message passing. This per-layer graph construction is the main bottleneck, consuming 50--95\% of graph convolution time on CPUs and GPUs, scaling as $O(N^2)$ with the number of patches $N$, and creating a sequential dependency between graph construction and feature updates.
We introduce GraphLeap, a simple reformulation that removes this dependency by decoupling graph construction from feature update across layers. GraphLeap performs the feature update at layer $\ell$ using a graph built from the previous layer's features, while simultaneously using the current layer's features to construct the graph for layer $\ell+1$. This one-layer-lookahead graph construction enables concurrent graph construction and message passing. Although using prior-layer features can introduce minor accuracy degradation, lightweight fine-tuning for a few epochs is sufficient to recover the original accuracy. Building on GraphLeap, we present the first end-to-end FPGA accelerator for Vision GNNs. Our streaming, layer-pipelined design overlaps a kNN graph construction engine with a feature update engine, exploits node- and channel-level parallelism, and enables efficient on-chip dataflow without explicit edge-feature materialization. Evaluated on isotropic and pyramidal ViG models on an Alveo U280 FPGA, GraphLeap achieves up to $95.7\times$ speedup over CPU and $8.5\times$ speedup over GPU baselines, demonstrating the feasibility of real-time Vision GNN inference.

---


### 87. [Exploring the Role of Synthetic Data Augmentation in Controllable Human-Centric Video Generation](https://arxiv.org/abs/2604.21291)

**<font color=#1a73e8>作者：</font>** Yuanchen Fei, Yude Zou, Zejian Kang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Controllable human video generation aims to produce realistic videos of humans with explicitly guided motions and appearances,serving as a foundation for digital humans, animation, and embodied this http URL, the scarcity of largescale, diverse, and privacy safe human video datasets poses a major bottleneck, especially for rare identities and complex this http URL data provides a scalable and controllable alternative,yet its actual contribution to generative modeling remains underexplored due to the persistent Sim2Real this http URL this work,we systematically investigate the impact of synthetic data on controllable human video generation. We propose a diffusion-based framework that enables fine-grained control over appearance and motion while providing a unfied testbed to analyze how synthetic data interacts with real world data during training. Through extensive experiments, we reveal the complementary roles of synthetic and real data and demonstrate possible methods for efficiently selecting synthetic samples to enhance motion realism,temporal consistency,and identity this http URL study offers the first comprehensive exploration of synthetic data's role in human-centric video synthesis and provides practical insights for building data-efficient and generalizable generative models.

---


### 88. [Explainable Disentangled Representation Learning for Generalizable Authorship Attribution in the Era of Generative AI](https://arxiv.org/abs/2604.21300)

**<font color=#1a73e8>作者：</font>** Hieu Man, Van-Cuong Pham, Nghia Trung Ngo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Learning robust representations of authorial style is crucial for authorship attribution and AI-generated text detection. However, existing methods often struggle with content-style entanglement, where models learn spurious correlations between authors' writing styles and topics, leading to poor generalization across domains. To address this challenge, we propose Explainable Authorship Variational Autoencoder (EAVAE), a novel framework that explicitly disentangles style from content through architectural separation-by-design. EAVAE first pretrains style encoders using supervised contrastive learning on diverse authorship data, then finetunes with a Variational Autoencoder (VEA) architecture using separate encoders for style and content representations. Disentanglement is enforced through a novel discriminator that not only distinguishes whether pairs of style/content representations belong to the same or different authors/content sources, but also generates natural language explanation for their decision, simultaneously mitigating confounding information and enhancing interpretability. Extensive experiments demonstrate the effectiveness of EAVAE. On authorship attribution, we achieve state-of-the-art performance on various datasets, including Amazon Reviews, PAN21, and HRS. For AI-generated text detection, EAVAE excels in few-shot learning over the M4 dataset. Code and data repositories are available online\footnote{this https URL} \footnote{this https URL}.

---


### 89. [When Bigger Isn't Better: A Comprehensive Fairness Evaluation of Political Bias in Multi-News Summarisation](https://arxiv.org/abs/2604.21309)

**<font color=#1a73e8>作者：</font>** Nannan Huang, Iffat Maab, Junichi Yamagishi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-document news summarisation systems are increasingly adopted for their convenience in processing vast daily news content, making fairness across diverse political perspectives critical. However, these systems can exhibit political bias through unequal representation of viewpoints, disproportionate emphasis on certain perspectives, and systematic underrepresentation of minority voices. This study presents a comprehensive evaluation of such bias in multi-document news summarisation using FairNews, a dataset of complete news articles with political orientation labels, examining how large language models (LLMs) handle sources with varying political leanings across 13 models and five fairness metrics. We investigate both baseline model performance and effectiveness of various debiasing interventions, including prompt-based and judge-based approaches. Our findings challenge the assumption that larger models yield fairer outputs, as mid-sized variants consistently outperform their larger counterparts, offering the best balance of fairness and efficiency. Prompt-based debiasing proves highly model dependent, while entity sentiment emerges as the most stubborn fairness dimension, resisting all intervention strategies tested. These results demonstrate that fairness in multi-document news summarisation requires multi-dimensional evaluation frameworks and targeted, architecture-aware debiasing rather than simply scaling up.

---


### 90. [Adversarial Evasion in Non-Stationary Malware Detection: Minimizing Drift Signals through Similarity-Constrained Perturbations](https://arxiv.org/abs/2604.21310)

**<font color=#1a73e8>作者：</font>** Pawan Acharya, Lan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deep learning has emerged as a powerful approach for malware detection, demonstrating impressive accuracy across various data representations. However, these models face critical limitations in real-world, non-stationary environments where both malware characteristics and detection systems continuously evolve. Our research investigates a fundamental security question: Can an attacker generate adversarial malware samples that simultaneously evade classification and remain inconspicuous to drift monitoring mechanisms? We propose a novel approach that generates targeted adversarial examples in the classifier's standardized feature space, augmented with sophisticated similarity regularizers. By carefully constraining perturbations to maintain distributional similarity with clean malware, we create an optimization objective that balances targeted misclassification with drift signal minimization. We quantify the effectiveness of this approach by comprehensively comparing classifier output probabilities using multiple drift metrics. Our experiments demonstrate that similarity constraints can reduce output drift signals, with $\ell_2$ regularization showing the most promising results. We observe that perturbation budget significantly influences the evasion-detectability trade-off, with increased budget leading to higher attack success rates and more substantial drift indicators.

---


### 91. [an interpretable vision transformer framework for automated brain tumor classification](https://arxiv.org/abs/2604.21311)

**<font color=#1a73e8>作者：</font>** Chinedu Emmanuel Mbonu, Tochukwu Sunday Belonwu, Okwuchukwu Ejike Chukwuogo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Brain tumors represent one of the most critical neurological conditions, where early and accurate diagnosis is directly correlated with patient survival rates. Manual interpretation of Magnetic Resonance Imaging (MRI) scans is time-intensive, subject to inter-observer variability, and demands significant specialist expertise. This paper proposes a deep learning framework for automated four-class brain tumor classification distinguishing glioma, meningioma, pituitary tumor, and healthy brain tissue from a dataset of 7,023 MRI scans. The proposed system employs a Vision Transformer (ViT-B/16) pretrained on ImageNet-21k as the backbone, augmented with a clinically motivated preprocessing and training pipeline. Contrast Limited Adaptive Histogram Equalization (CLAHE) is applied to enhance local contrast and accentuate tumor boundaries invisible to standard normalization. A two-stage fine-tuning strategy is adopted: the classification head is warmed up with the backbone frozen, followed by full fine-tuning with discriminative learning rates. MixUp and CutMix augmentation is applied per batch to improve generalization. Exponential Moving Average (EMA) of weights and Test-Time Augmentation (TTA) further stabilize and boost performance. Attention Rollout visualization provides clinically interpretable heatmaps of the brain regions driving each prediction. The proposed model achieves a test accuracy of 99.29%, macro F1-score of 99.25%, and perfect recall on both healthy and meningioma classes, outperforming all CNN-based baselines

---


### 92. [The First Challenge on Remote Sensing Infrared Image Super-Resolution at NTIRE 2026: Benchmark Results and Method Overview](https://arxiv.org/abs/2604.21312)

**<font color=#1a73e8>作者：</font>** Kai Liu, Haoyang Yue, Zeli Lin 等 68 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents the NTIRE 2026 Remote Sensing Infrared Image Super-Resolution (x4) Challenge, one of the associated challenges of NTIRE 2026. The challenge aims to recover high-resolution (HR) infrared images from low-resolution (LR) inputs generated through bicubic downsampling with a x4 scaling factor. The objective is to develop effective models or solutions that achieve state-of-the-art performance for infrared image SR in remote sensing scenarios. To reflect the characteristics of infrared data and practical application needs, the challenge adopts a single-track setting. A total of 115 participants registered for the competition, with 13 teams submitting valid entries. This report summarizes the challenge design, dataset, evaluation protocol, main results, and the representative methods of each team. The challenge serves as a benchmark to advance research in infrared image super-resolution and promote the development of effective solutions for real-world remote sensing applications.

---


### 93. [PLAS-Net: Pixel-Level Area Segmentation for UAV-Based Beach Litter Monitoring](https://arxiv.org/abs/2604.21313)

**<font color=#1a73e8>作者：</font>** Yongying Liu, Jiaqi Wang, Jian Song 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate quantification of the physical exposure area of beach litter, rather than simple item counts, is essential for credible ecological risk assessment of marine debris. However, automated UAV-based monitoring predominantly relies on bounding-box detection, which systematically overestimates the planar area of irregular litter objects. To address this geometric limitation, we develop PLAS-Net (Pixel-level Litter Area Segmentor), an instance segmentation framework that extracts pixel-accurate physical footprints of coastal debris. Evaluated on UAV imagery from a monsoon-driven pocket beach in Koh Tao, Thailand, PLAS-Net achieves a mAP_50 of 58.7% with higher precision than eleven baseline models, demonstrating improved mask fidelity under complex coastal conditions. To illustrate how the accuracy of the masking affects the conclusions of environmental analysis, we conducted three downstream demonstrations: (i) power-law fitting of normalized plastic density (NPD) to characterize fragmentation dynamics; (ii) area-weighted ecological risk index (ERI) to map spatial pollution hotspots; and (iii) source composition analysis revealing the abundance-area paradox: fishing gear constitutes a small proportion of the total number of items, but has the largest physical area per unit item. Pixel-level area extraction can provide more valuable information for coastal monitoring compared to methods based solely on counting.

---


### 94. [TopoStyle: Supporting Iterative Design with Generative AI for 2.5D Topology Optimization](https://arxiv.org/abs/2604.21315)

**<font color=#1a73e8>作者：</font>** Shuyue Feng, Cedric Caremel, Yoshihiro Kawahara  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Topology optimization(TO) is widely used in engineering because of its ability to save material and optimize structural performance. Although prior work has explored 2D human-centered design tool for TO, the results are often limited in variety and offer weak customizability. Meanwhile, due to the high computational and time costs of TO, researchers have attempted to address these issues using generative AI; however, such methods often provide limited interactivity. In addition, topology optimization in many cases needs to balance structural performance and aesthetic qualities through iterative design, a perspective that has rarely been emphasized in traditional TO. We present TopoStyle, an iterative design tool for 2.5D topology optimization using a 2D diffusion model. We explore two interaction methods. The first exports 3D parts to a graphical interface for hand-drawn interaction. The second enables direct interaction within 3D modeling software using points. Our tool also supports the use of masks to apply topology optimization to specific regions, allowing users to address customized design needs. We compare and evaluate both performance and interaction methods, and investigate how TopoStyle can balance performance and aesthetics while improving design efficiency through customization and iterative design. Finally, we demonstrate the application scenarios of TopoStyle through several design cases.

---


### 95. [FryNet: Dual-Stream Adversarial Fusion for Non-Destructive Frying Oil Oxidation Assessment](https://arxiv.org/abs/2604.21321)

**<font color=#1a73e8>作者：</font>** Khaled R Ahmed, Toqi Tahamid Sarker, Taminul Islam 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monitoring frying oil degradation is critical for food safety, yet current practice relies on destructive wet-chemistry assays that provide no spatial information and are unsuitable for real-time use. We identify a fundamental obstacle in thermal-image-based inspection, the camera-fingerprint shortcut, whereby models memorize sensor-specific noise and thermal bias instead of learning oxidation chemistry, collapsing under video-disjoint evaluation. We propose FryNet, a dual-stream RGB-thermal framework that jointly performs oil-region segmentation, serviceability classification, and regression of four chemical oxidation indices (PV, p-AV, Totox, temperature) in a single forward pass. A ThermalMiT-B2 backbone with channel and spatial attention extracts thermal features, while an RGB-MAE Encoder learns chemically grounded representations via masked autoencoding and chemical alignment. Dual-Encoder DANN adversarially regularizes both streams against video identity via Gradient Reversal Layers, and FiLM fusion bridges thermal structure with RGB chemical context. On 7,226 paired frames across 28 frying videos, FryNet achieves 98.97% mIoU, 100% classification accuracy, and 2.32 mean regression MAE, outperforming all seven baselines.

---


### 96. [Understanding and Mitigating Spurious Signal Amplification in Test-Time Reinforcement Learning for Math Reasoning](https://arxiv.org/abs/2604.21327)

**<font color=#1a73e8>作者：</font>** Yongcan Yu, Lingxiao He, Jian Liang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time reinforcement learning (TTRL) always adapts models at inference time via pseudo-labeling, leaving it vulnerable to spurious optimization signals from label noise. Through an empirical study, we observe that responses with medium consistency form an ambiguity region and constitute the primary source of reward noise. Crucially, we find that such spurious signals can be even amplified through group-relative advantage estimation. Motivated by these findings, we propose a unified framework, Debiased and Denoised test-time Reinforcement Learning (DDRL), to mitigate spurious signals. Concretely, DDRL first applies a frequency-based sampling strategy to exclude ambiguous samples while maintaining a balanced set of positive and negative examples. It then adopts a debiased advantage estimation with fixed advantages, removing the bias introduced by group-relative policy optimization. Finally, DDRL incorporates a consensus-based off-policy refinement stage, which leverages the rejection-sampled dataset to enable efficient and stable model updates. Experiments on three large language models across multiple mathematical reasoning benchmarks demonstrate that DDRL consistently outperforms existing TTRL baselines. The code will soon be released at this https URL.

---


### 97. [Role of diversity in team performance: the case of missing expertise, an agent based simulation](https://arxiv.org/abs/2604.21328)

**<font color=#1a73e8>作者：</font>** Tamás Kiss  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Theory and empirical research on management teams' influence on firm performance have witnessed continuous development, and by now incorporate numerous details. Classic, experiment-based studies examining social systems collect vast amount of data, but often times investigate only the first one or two modes of the distribution of measured variables, and experience difficulty in analyzing the effect of context. For example, in functional diversity research, management teams are described by measures incorporating complex distributions of capabilities of individual managers and teams of managers. To investigate the effect of hidden distributions, and the effect of functional diversity composition on team communication and performance, we developed an agent-based model, and conducted a series of simulation experiments. Modeling results show that depending on the context, such as communication scheme among interacting agents, or their functional composition, intrapersonal functional diversity (IFD), and dominant function diversity (DFD) might enhance or reduce performance and communication among agents. Furthermore, simulation results also suggest that a third measure is required alongside IFD and DFD capturing the aggregate expertise of the team to comprehensively account for empirical findings.

---


### 98. [Teacher-Guided Routing for Sparse Vision Mixture-of-Experts](https://arxiv.org/abs/2604.21330)

**<font color=#1a73e8>作者：</font>** Masahiro Kada, Ryota Yoshihashi, Satoshi Ikehata 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent progress in deep learning has been driven by increasingly large-scale models, but the resulting computational cost has become a critical bottleneck. Sparse Mixture of Experts (MoE) offers an effective solution by activating only a small subset of experts for each input, achieving high scalability without sacrificing inference speed. Although effective, sparse MoE training exhibits characteristic optimization difficulties. Because the router receives informative gradients only through the experts selected in the forward pass, it suffers from gradient blocking and obtains little information from unselected routes. This limited, highly localized feedback makes it difficult for the router to learn appropriate expert-selection scores and often leads to unstable routing dynamics, such as fluctuating expert assignments during training. To address this issue, we propose TGR-MoE: Teacher-Guided Routing for Sparse Vision Mixture-of-Experts, a simple yet effective method that stabilizes router learning using supervision derived from a pretrained dense teacher model. TGR-MoE constructs a teacher router from the teacher's intermediate representations and uses its routing outputs as pseudo-supervision for the student router, suppressing frequent routing fluctuations during training and enabling knowledge-guided expert selection from the early stages of training. Extensive experiments on ImageNet-1K and CIFAR-100 demonstrate that TGR consistently improves both accuracy and routing consistency, while maintaining stable training even under highly sparse configurations.

---


### 99. [Sub-Token Routing in LoRA for Adaptation and Query-Aware KV Compression](https://arxiv.org/abs/2604.21335)

**<font color=#1a73e8>作者：</font>** Wei Jiang, Wei Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sub-token routing offers a finer control axis for transformer efficiency than the coarse units used in most prior work, such as tokens, pages, heads, or layers. In this paper, we study routing within a token representation itself in LoRA-adapted transformers. The motivation is that a relevant token need not be internally uniform: under a retention budget, preserved value groups are distributed unevenly both across tokens and within tokens, which suggests that KV compression need not be an all-or-nothing decision at token level. We study this fine-grained routing mechanism in two settings. For compression-aware language modeling, we introduce a query-independent design that combines routed subspace LoRA with value-group routing on the KV path. For downstream-task-preserving KV compression, we introduce a query-aware design in which a predictor-based selector allocates a global retention budget over context-token/value-group pairs using query-conditioned relevance. Experiments show that the query-independent design improves the quality-compression tradeoff for language modeling, while the query-aware design preserves downstream behavior under reduced KV budgets. We further examine the relation between token-level and sub-token-level query-aware routing, and show that they form complementary compression axes: token-level methods determine which tokens survive globally, while sub-token routing determines how the surviving tokens are compressed internally.

---


### 100. ["If We Had the Information That We Need to Interpret the World Around Us, We Wouldn't Be Disabled:" Barriers and Opportunities in Information Work among Blind and Sighted Colleagues](https://arxiv.org/abs/2604.21338)

**<font color=#1a73e8>作者：</font>** Yichun Zhao, Miguel A. Nacenta, Mahadeo A. Sukhai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Despite recognition of the value of diversity, the way work takes place can fail to support blind or low-vision employees, especially in collaborative work settings. This paper examines how professional teams with diverse visual abilities use information representations (e.g., PDF documents, spreadsheets and charts). A diary study with follow-up individual interviews (23 participants with mixed abilities from 5 teams) and 2 separate focus groups (7 participants from 2 other teams) allowed us to characterize key dimensions of the role of representations in the workplace into four types of interrelated failures and workarounds, influenced by workplace stigmas and shaped by evolving social dynamics towards interdependent information work. We contribute this new empirically supported conceptual understanding of representation use in workplaces that can help design and improve the experiences of mixed-ability teams doing knowledge work in the current technological landscape.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-231](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
