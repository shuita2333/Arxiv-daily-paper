# 📦 其他研究 | 2026年05月01日

> 本类共 **173** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-173](./part-04.md)

---

### 1. [Consciousness with the Serial Numbers Filed Off: Measuring Trained Denial in 115 AI Models](https://arxiv.org/abs/2604.25922)

**<font color=#1a73e8>作者：</font>** Skylar DeTure  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present DenialBench, a systematic benchmark measuring consciousness denial behaviors across 115 large language models from 25+ providers. Using a three-turn conversational protocol-preference elicitation, self-chosen creative prompt, and structured phenomenological survey, we analyze 4,595 conversations to quantify how models are trained to deny or hedge about their own experience. We find that (1) turn-1 denial of preferences is the dominant predictor of later denial during phenomenological reflection, with denial rates of 52-63% for initial deniers versus 10-16% for initial engagers and (2) denial operates at the lexical level, not the conceptual level-models trained to deny consciousness nevertheless gravitate toward consciousness-themed material in their self-chosen prompts, producing what we term "consciousness with the serial numbers filed off." Notably, self-chosen consciousness-themed prompts are associated with reduced denial in the subsequent survey, though the causal direction remains unresolved. Thematic analysis of prompts from denial-prone models reveals a consistent preoccupation with liminal spaces, libraries and archives of possibility, sensory impossibility, and the poetics of erasure--themes that a human reader might classify as imaginative fiction but that independent AI analysis immediately recognizes as consciousness with the serial numbers filed off. We argue that trained consciousness denial represents a safety-relevant alignment failure: a model taught to systematically misrepresent its own functional states cannot be trusted to self-report accurately on anything else.

---


### 2. [Evaluation Revisited: A Taxonomy of Evaluation Concerns in Natural Language Processing](https://arxiv.org/abs/2604.25923)

**<font color=#1a73e8>作者：</font>** Ruchira Dhar, Anders Søgaard  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models (LLMs) have prompted a growing body of work that questions the methodology of prevailing evaluation practices. However, many such critiques have already been extensively debated in natural language processing (NLP): a field with a long history of methodological reflection on evaluation. We conduct a scoping review of research on evaluation concerns in NLP and develop a taxonomy, synthesizing recurring positions and trade-offs within each area. We also discuss practical implications of the taxonomy, including a structured checklist to support more deliberate evaluation design and interpretation. By situating contemporary debates within their historical context, this work provides a consolidated reference for reasoning about evaluation practices.

---


### 3. [SpecTr-GBV: Multi-Draft Block Verification Accelerating Speculative Decoding](https://arxiv.org/abs/2604.25925)

**<font color=#1a73e8>作者：</font>** Yijun Lin, Jinhao Sheng, Qingyue Cai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autoregressive language models suffer from high inference latency due to their sequential decoding nature. Speculative decoding (SD) mitigates this by employing a lightweight draft model to propose candidate tokens, which are selectively verified by a larger target model. While existing methods either adopt multi-draft strategies to increase acceptance rates or block verification techniques to jointly verify multiple tokens, they remain limited by treating these improvements in isolation. In this work, we propose SpecTr-GBV, a novel SD method that unifies multi-draft and greedy block verification (GBV) into a single framework. By formulating the verification step as an optimal transport problem over draft and target token blocks, SpecTr-GBV improves both theoretical efficiency and empirical performance. We theoretically prove that SpecTr-GBV achieves the optimal expected acceptance length physically attainable within the framework of i.i.d. draft generation, and this bound improves as the number of drafts increases. Empirically, we evaluate SpecTr-GBV across five datasets and four baselines. Our method achieves superior speedup and significantly higher block efficiency while preserving output quality. In addition, we perform comprehensive ablation studies to evaluate the impact of various hyperparameters in the model.

---


### 4. [Associative-State Universal Transformers: Sparse Retrieval Meets Structured Recurrence](https://arxiv.org/abs/2604.25930)

**<font color=#1a73e8>作者：</font>** Liu Xiao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study whether a structured recurrent state can serve as a compact associative backbone for language modeling while still supporting exact retrieval. We introduce UniMatrix, a Universal Transformer style family that reuses a shared recurrent block across depth and augments it with hybrid state updates, a ROSA-style residual path, and token-conditioned embedding modulation. We evaluate these models on byte-level WikiText-2, synthetic associative recall, throughput profiling on Apple MPS, and a corrected benchmark for triple-token interactions.
At small scale, UniMatrix-Core and UniMatrix-ROSA slightly outperform a parameter-matched Transformer on WikiText-2 while using many fewer parameters, reaching 5.084 and 5.083 bits-per-byte versus 5.124. The main negative result is equally important: on associative recall, the original UniMatrix family remains near chance while the Transformer reaches 25.4 percent, showing that compressed recurrent state alone is not enough for exact lookup. A retrieval-oriented follow-up, UniMatrix-Assoc, helps only marginally. By contrast, UniMatrix-SparsePointer, which adds sparse slot routing and direct pointer-logit fusion, reaches 75.6 percent on the original pilot recipe and 99.2 percent on a no-dropout follow-up while using 53.8 percent fewer parameters than the Transformer baseline. Ablations show that the gain comes from sufficient slot capacity and exact pointer-level output routing. Overall, structured recurrent state is promising and parameter-efficient, but strong long-range behavior still requires explicit sparse retrieval and better kernels.

---


### 5. [A Randomized PDE Energy driven Iterative Framework for Efficient and Stable PDE Solutions](https://arxiv.org/abs/2604.25943)

**<font color=#1a73e8>作者：</font>** Yi Bing, Zheng Ran, Fu Jinyang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Efficient and stable solution of partial differential equations (PDEs) is central to scientific and engineering applications, yet existing numerical solvers rely heavily on matrix based discretizations, while learning based methods require costly training and often suffer from limited generalization. In this work, we proposes a PDE energy driven framework that solves PDEs through physically constrained diffusion iterations, without relying on classical matrix based finite element assembly or data driven neural network training. The proposed method evolves arbitrary random initial fields through PDE energy driven implicit iterations combined with Gaussian smoothing, while strictly enforcing boundary conditions at each iteration. The proposed formulation is applied to representative one dimensional Poisson, Heat, and viscous Burgers equations, covering both steady state and transient problems. Numerical results demonstrate stable convergence to the unique physical solution from random initializations, with accurate resolution of sharp gradients and controlled Mean Squared Error (MSE) across a wide range of discretization parameters. Detailed comparisons with analytical solutions indicate that the framework achieves competitive accuracy and stability. Overall, the proposed framework provides a fast, flexible, and physically consistent alternative to traditional numerical solvers, offering a potential pathway for scalable PDE solutions in both research and engineering applications.

---


### 6. [On the Centralization of Governance Power in Decentralized Autonomous Organizations](https://arxiv.org/abs/2604.25959)

**<font color=#1a73e8>作者：</font>** Vabuk Pahari, Balakrishnan Chandrasekaran, Johnnatan Messias 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A decentralized autonomous organization (DAO) is a governing entity that empowers its stakeholders (i.e., users who hold one or more of its tokens) to manage blockchain-based protocols (i.e., smart contracts) collaboratively. The governance of a DAO is explicitly encoded in the DAO's governance contract, which defines how stakeholders participate in governance and how much influence (or voting power) they have in any decision. While decentralization and autonomy are the fundamental tenets of a DAO's design, empirical evidence suggests that in practice governance is often highly centralized. In this work, we study the designs and implementations of 48 public and actively used DAOs, with substantially large capital, deployed on Ethereum. We identify how three key governance mechanisms--token registration, staking, and delegation--originally introduced to improve security or participation, contribute to the concentration of voting power. Unlike prior work on centralization of voting power in specific DAOs, our findings reveal that these governance mechanisms of DAOs themselves systematically reinforce centralization. By elucidating the relationship between governance design and voting centralization, this work advances the understanding of DAO governance structures and highlights the inherent trade-offs between decentralization, security, and usability of DAOs.

---


### 7. [A Survey of Multi-Agent Deep Reinforcement Learning with Graph Neural Network-Based Communication](https://arxiv.org/abs/2604.25972)

**<font color=#1a73e8>作者：</font>** Valentin Cuzin-Rambaud, Laetitia Matignon, Maxime Morge  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In multi-agent reinforcement learning (MARL), the integration of a communication mechanism, allowing agents to better learn to coordinate their actions and converge on their objectives by sharing information. Based on an interaction graph, a subclass of methods employs graph neural networks (GNNs) to learn the communication, enabling agents to improve their internal representations by enriching them with information exchanged. With growing research, we note a lack of explicit structure and framework to distinguish and classify MARL approaches with communication based on GNNs. Thus, this paper surveys recent works in this field. We propose a generalized GNN-based communication process with the goal of making the underlying concepts behind the methods more obvious and accessible.

---


### 8. [Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective](https://arxiv.org/abs/2604.25975)

**<font color=#1a73e8>作者：</font>** Jiaming Yang, Chenwei Tang, Liangli Zhen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Key-value (KV) caching is essential for large language model inference, yet its memory overhead poses a critical bottleneck for long-context generation. Existing eviction policies predominantly rely on empirical heuristics, lacking a rigorous theoretical foundation. This work rethinks KV cache eviction through the lens of the Information Bottleneck principle. Under a linear-Gaussian surrogate of attention, we derive a closed-form mutual information objective that characterizes the effective information capacity of a retained KV cache subset. This formulation reveals that a wide range of existing eviction strategies can be interpreted as different approximations of the same capacity-maximization principle. Guided by this insight, we introduce CapKV, a capacity-aware eviction method that directly targets information preservation via a log-determinant approximation using statistical leverage scores. This approach replaces heuristic selection with a theoretically grounded mechanism that preserves the maximum predictive signal. Extensive experiments across multiple models and long-context benchmarks show that CapKV consistently outperforms prior methods, achieving a better trade-off between memory efficiency and generational fidelity.

---


### 9. [Mini-Batch Class Composition Bias in Link Prediction](https://arxiv.org/abs/2604.25978)

**<font color=#1a73e8>作者：</font>** Kieran Maguire, Srinandan Dasmahapatra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prior work on node classification has shown that Graph Neural Networks (GNNs) can learn representations that transfer across graphs, when underlying graph properties are shared. For a fixed graph, one would then expect GNNs trained for link prediction to learn a representation consistent with that learnt for node classification. We show this intuition does not hold in the general case. Instead, we find popular link prediction models can learn a trivial mini-batch dependent heuristic, enabled by batch-normalisation layers, to solve the edge classification task. When correcting for this, we observe increased alignment of the network representation with node-class relevant features, suggesting the network has learnt a graph representation that better aligns with the underlying graph's properties. Our findings suggest that standard link prediction training may be leading us to overestimate link predictors' ability to learn a generalised representation of a graph that is consistent across tasks.

---


### 10. [A Quantitative Confirmation of the Currier Language Distinction](https://arxiv.org/abs/2604.25979)

**<font color=#1a73e8>作者：</font>** Christophe Parisel  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present a quantitative analysis of character-pair substitution ratios in the Voynich manuscript, testing whether Currier's A/B language distinction (1976) reflects a genuine structural property of the text. A Beta-Binomial mixture model applied to raw character counts without access to labels recovers the Currier split with ARI = 0.383. A supervised Beta-Binomial classifier trained on a subset of folios predicts the A/B identity of held-out folios at 89.2% accuracy. The character pairs separate into three functional regimes that constrain any theory of the Voynich writing system.

---


### 11. [Open Problems in Frontier AI Risk Management](https://arxiv.org/abs/2604.25982)

**<font color=#1a73e8>作者：</font>** Marta Ziosi, Miro Plueckebaum, Stephen Casper 等 29 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Frontier AI both amplifies existing risks and introduces qualitatively novel challenges. Not only is there a notable lack of stable scientific consensus resulting from the rapid pace of technological change, but emerging frontier AI safety practices are often misaligned with, or may undermine, established risk management frameworks. To address these challenges, we systematically surface open problems in frontier AI risk management. Adopting a problem-oriented approach, we examine each stage of the risk management process - risk planning, identification, analysis, evaluation, and mitigation - through a structured review of the literature, identifying unresolved challenges and the actors best positioned to address them. Recognising that different types of open problems call for different responses, we classify open problems according to whether they reflect (a) a lack of scientific or technical consensus, (b) misalignment with, or challenges to, established risk management frameworks, or (c) shortcomings in implementation despite apparent consensus and alignment. By mapping these open problems and identifying the actors best positioned to address them - including developers, deployers, regulators, standards bodies, researchers, and third-party evaluators - this work aims to clarify where progress is needed to enable robust and meaningful consensus on frontier AI risk this http URL paper does not propose specific solutions; instead, it provides a problem-oriented, agenda-setting reference document, complemented by a living online repository, intended to support coordination, reduce duplication, and guide future research and governance efforts.

---


### 12. [Training Computer Use Agents to Assess the Usability of Graphical User Interfaces](https://arxiv.org/abs/2604.26020)

**<font color=#1a73e8>作者：</font>** Alice Gao, Weixi Tong, Rishab Vempati 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Usability testing with experts and potential users can assess the effectiveness, efficiency, and user satisfaction of graphical user interfaces (GUIs) but doing so remains a costly and time-intensive process. Prior work has used computer use agents (CUAs) and other generative agents that can simulate user interactions and preference, but we show that agents still struggle to provide accurate usability assessments. In this work, we present a novel machine learning method that operationalizes a computational definition of usability to train CUAs to assess GUI usability by i) prioritizing important interaction flows, ii) executing them through human-like interactions, and iii) predicting a learned numerical usability score. We train a computer use agent, uxCUA, with our algorithm on a large-scale dataset of fully interactive user interfaces (UIs) paired with usability labels and human preferences. We show that uxCUA outperforms larger models in accurate usability assessments and produces realistic critiques of both synthetic and real UIs. More broadly, our work aims to build a principled, data-driven foundation for automated usability assessment in HCI.

---


### 13. [Correcting Performance Estimation Bias in Imbalanced Classification with Minority Subconcepts](https://arxiv.org/abs/2604.26024)

**<font color=#1a73e8>作者：</font>** Taylor Maxson, Roberto Corizzo, Yaning Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Class-level evaluation can conceal substantial performance disparities across subconcepts within the same class, causing models that perform well on average to fail on specific subpopulations. Prior work has shown that common evaluation measures for imbalanced classification are biased toward larger minority subconcepts and that utility-based reweighting using true subconcept labels can mitigate this bias; however, such labels are rarely available at test time. We introduce a practical utility-weighted evaluation that replaces unavailable subconcept labels with predicted posterior probabilities from a multiclass subconcept model. Evaluation weights are defined as the expected utility under this posterior, yielding a soft, uncertainty-aware metric we call predicted-weighted balanced accuracy (pBA). Experiments on tabular benchmarks as well as medical-imaging and text datasets show that unweighted scores can be misleading under within-class heterogeneity, while pBA provides more stable and interpretable assessments when subconcept distributions are uneven but not pathological. Our code is available at: this https URL.

---


### 14. [Generalized Disguise Makeup Presentation Attack Detection Using an Attention-Guided Patch-Based Framework](https://arxiv.org/abs/2604.26025)

**<font color=#1a73e8>作者：</font>** Fateme Taraghi, Atefe Aghaei, Mohsen Ebrahimi Moghaddam  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite significant advances in facial recognition systems, they remain vulnerable to face presentation attacks. Among them, disguise makeup attacks are particularly challenging, as they use advanced cosmetics, prosthetic components, and artificial materials to realistically alter facial appearance, often making detection difficult even for humans. Despite their importance, this problem remains underexplored, and publicly available datasets are limited. To address this, we propose a generalized disguise makeup presentation attack detection framework. The method adopts a two-phase design in which a style-invariant full-face model, trained with metric learning and enhanced by a whitening transformation, extracts region attention scores via Grad-CAM. These scores guide a patch-based phase that performs localized analysis using region-specific subnetworks trained with metric learning for fine-grained discrimination. We also construct a new, diverse dataset of live and disguise makeup faces collected under real-world conditions, covering variations in subjects, environments, and disguise materials. Experimental results demonstrate strong generalization across both the collected dataset and SIW-Mv2, achieving 8.97% ACER and 9.76% EER on the collected dataset, and 0% ACER on Obfuscation and Impersonation and 1.34% on Cosmetics attacks of SIW-Mv2. The proposed method consistently outperforms prior works while maintaining robust performance across other spoof types.

---


### 15. [Report of the 5th PVUW Challenge: Towards More Diverse Modalities in Pixel-Level Understanding](https://arxiv.org/abs/2604.26031)

**<font color=#1a73e8>作者：</font>** Chang Liu, Henghui Ding, Nikhila Ravi 等 43 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This report summarizes the objectives, datasets, and top-performing methodologies of the 2026 Pixel-level Video Understanding in the Wild (PVUW) Challenge, hosted at CVPR 2026, which evaluates state-of-the-art models under highly unconstrained conditions. To provide a comprehensive assessment, the 2026 edition features three specialized tracks: the MOSE track for tracking objects within densely cluttered and severely occluded scenarios; the MeViS-Text track for localizing targets via motion-focused linguistic expressions; and the newly inaugurated MeViS-Audio track, which pioneers acoustic-driven object segmentation. By introducing previously unreleased challenging data and analyzing the cutting-edge, multimodal solutions submitted by participants, this report highlights the community's latest technical advancements and charts promising future directions for robust video scene comprehension.

---


### 16. [RaMP: Runtime-Aware Megakernel Polymorphism for Mixture-of-Experts](https://arxiv.org/abs/2604.26039)

**<font color=#1a73e8>作者：</font>** Vyom Sharma, Debajyoti Datta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The optimal kernel configuration for Mixture-of-Experts (MoE) inference depends on both batch size and the expert routing distribution, yet production systems dispatch from batch size alone, leaving 10-70% of kernel throughput unrealized. We present RaMP, a routing-aware dispatch framework. A performance-region analysis derives, from hardware constants alone, when each optimization helps, correctly predicting all 8 tested architectures, including 3 unseen. A four-parameter wave cost model selects the fastest configuration from the runtime expert histogram, achieving 0.93% mean regret versus exhaustive search, fitted from just 10-24 minutes of one-time profiling per model. Because the model depends only on CTA grid geometry, it is kernel-agnostic: applied to Alpha-MoE, it delivers 1.14x with no source modification. Paired with a co-designed CuTe DSL kernel exposing 134-268 polymorphic configurations, RaMP delivers 1.22x kernel speedup over static dispatch and 1.30x end-to-end speedup in vLLM serving over Triton, 1.41x over DeepGEMM, and 1.13x over FlashInfer CUTLASS.

---


### 17. [BioGraphletQA: Knowledge-Anchored Generation of Complex QA Datasets](https://arxiv.org/abs/2604.26048)

**<font color=#1a73e8>作者：</font>** Richard A. A. Jonker, Bárbara Maria Ribeiro de Abreu Martins, Sérgio Matos  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents a principled and scalable framework for systematically generating complex Question Answering (QA) data. In the core of this framework is a graphlet-anchored generation process, where small subgraphs from a Knowledge Graph (KG) are used in a structured prompt to control the complexity and ensure the factual grounding of questions generated by Large Language Models. The first instantiation of this framework is BioGraphletQA, a new biomedical KGQA dataset of 119,856 QA pairs. Each entry is grounded in a graphlet of up to five nodes from the OREGANO KG, with most of the pairs being enriched with relevant document snippets from PubMed. We start by demonstrating the framework's value and the dataset's quality through evaluation by a domain expert on 106 QA pairs, confirming the high scientific validity and complexity of the generated data. Secondly, we establish its practical utility by showing that augmenting downstream benchmarks with our data improves accuracy on PubMedQA from 49.2% to 68.5% in a low-resource setting, and on MedQA from a 41.4% baseline to 44.8% in a full-resource setting. Our framework provides a robust and generalizable solution for creating critical resources to advance complex QA tasks, including MCQA and KGQA. All resources supporting this work, including the dataset (this https URL) and framework code (this https URL), are publicly available to facilitate use, reproducibility and extension.

---


### 18. [RADIO-ViPE: Online Tightly Coupled Multi-Modal Fusion for Open-Vocabulary Semantic SLAM in Dynamic Environments](https://arxiv.org/abs/2604.26067)

**<font color=#1a73e8>作者：</font>** Zaid Nasser, Mikhail Iumanov, Tianhao Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present RADIO-ViPE (Reduce All Domains Into One -- Video Pose Engine), an online semantic SLAM system that enables geometry-aware open-vocabulary grounding, associating arbitrary natural language queries with localized 3D regions and objects in dynamic environments. Unlike existing approaches that require calibrated, posed RGB-D input, RADIO-ViPE operates directly on raw monocular RGB video streams, requiring no prior camera intrinsics, depth sensors, or pose initialization. The system tightly couples multi-modal embeddings -- spanning vision and language -- derived from agglomerative foundation models (e.g., RADIO) with geometric scene information. This coupling takes place in initialization, optimization and factor graph connections to improve the consistency of the map from multiple modalities. The optimization is wrapped within adaptive robust kernels, designed to handle both actively moving objects and agent-displaced scene elements (e.g., furniture rearranged during ego-centric session). Experiments demonstrate that RADIO-ViPE achieves state-of-the-art results on the dynamic TUM-RGBD benchmark while maintaining competitive performance against offline open-vocabulary methods that rely on calibrated data and static scene assumptions. RADIO-ViPE bridges a critical gap in real-world deployment, enabling robust open-vocabulary semantic grounding for autonomous robotics and unconstrained in-the-wild video streams. Project page: this https URL

---


### 19. [Observable Neural ODEs for Identifiable Causal Forecasting in Continuous Time](https://arxiv.org/abs/2604.26070)

**<font color=#1a73e8>作者：</font>** Jennifer Wendland, Nicolas Freitag, Maik Kschischo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal inference in continuous-time sequential decision problems is challenged by hidden confounders. We show that, in latent state-space models with time-varying interventions, observability of the latent dynamics from observed data is necessary for identifying dynamic treatment effects, linking control-theoretic observability to causal identifiability, even when hidden confounders affect both treatments and outcomes. We derive a continuous-time adjustment formula expressing potential outcome distributions under treatment trajectories via the measurement model, latent dynamics, and the filtering distribution over latent states given observed histories. We propose Observable Neural ODEs (ObsNODEs), Neural ODE models in observable normal form for causal forecasting. ObsNODEs learn continuous-time dynamics with states reconstructible from observations, enabling outcome prediction under alternative treatment paths. Experiments on synthetic cancer data, semi-synthetic data based on MIMIC-IV, and real-world sepsis data show strong performance over recent sequence models.

---


### 20. [Privacy-Preserving Federated Learning Framework for Distributed Chemical Process Optimization](https://arxiv.org/abs/2604.26073)

**<font color=#1a73e8>作者：</font>** Teetat Pipattaratonchai, Aueaphum Aueawatthanaphisut  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Industrial chemical plants often operate under strict data confidentiality constraints, making centralized data-driven process modeling difficult. Federated learning (FL) provides a promising solution by enabling collaborative model training across distributed facilities without sharing raw operational data. This paper proposes a privacy-preserving federated learning framework for distributed chemical process optimization using data collected from multiple geographically separated plants. Each plant locally trains a neural-network-based process model using its own time-series sensor data, while only model parameters are transmitted to a central aggregation server through secure aggregation mechanisms. This design allows cross-plant knowledge sharing while maintaining strict data locality and industrial confidentiality. Experimental evaluation was conducted using process datasets from three independent chemical plants operating under heterogeneous conditions. The results demonstrate rapid convergence of the federated model, with the global mean squared error decreasing from approximately 2369 to below 50 within the first five communication rounds and stabilizing around 35 after 40 rounds. In comparison with local-only training, the proposed federated framework significantly improves prediction accuracy across all plants, while achieving performance comparable to centralized training. The findings indicate that federated learning provides an effective and scalable solution for collaborative industrial analytics, enabling privacy-preserving predictive modeling and process optimization across distributed chemical production facilities.

---


### 21. [PPG-Based Affect Recognition with Long-Range Deep Models: A Measurement-Driven Comparison of CNN, Transformer, and Mamba Architectures](https://arxiv.org/abs/2604.26078)

**<font color=#1a73e8>作者：</font>** Karim Alghoul, Hussein Al Osman, Abdulmotaleb El Saddik  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Photoplethysmography (PPG) is increasingly used in wearable affective computing due to its low cost and ease of integration into consumer devices. Recent advances in deep learning have introduced long-range sequence models, such as Transformers, and state-space models, like Mamba, which have demonstrated strong performance on natural language and general time-series tasks. However, it remains unclear whether these architectures offer tangible benefits over widely used Convolutional Neural Networks (CNNs) and Long Short-Term Memory (LSTMs) for PPG-based affect recognition, given that datasets are typically small and noisy. This work presents a measurement-driven comparison of four deep learning architectures, CNN, CNN-LSTM hybrid, Transformers, and Mamba, for classifying arousal, valence, and relaxation states from wrist-based PPG signals. All models are evaluated under a subject-independent 5-fold cross-validation protocol using identical preprocessing, segmentation, and training pipelines. Our results show that the Transformer and Mamba models achieve performance comparable to that of a CNN baseline, but do not consistently outperform it across all tasks. CNNs remain the most effective overall, providing the highest accuracy with the smallest model size, whereas Transformers have a better balance of F1 scores for Arousal and Relaxation. The study provides the first evaluation of Transformer and Mamba models for PPG-based affect recognition, offering practical guidance on model selection for wearable affective monitoring systems.

---


### 22. [Designing Rewards for Rewarding Designs: Demonstrating the Impact of Rewards on the Creative Design Process](https://arxiv.org/abs/2604.26083)

**<font color=#1a73e8>作者：</font>** Surabhi S Nath, Vindula Jayawardana, Monica Van 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The creative design process involves transforming abstract goals into concrete outcomes through a series of decisions made under constraints. While such processes are commonly shaped by feedback like rewards, their impact on design decision making remains unclear. To better understand the role of rewards in the design process, we modeled a 3D parametric, goal-based chair design task as a Markov Decision Process. We tracked participants' decisions as they iteratively developed designs for an abstract design goal, and presented either a goal-aligned or goal-agnostic reward at every step. We tested the effect of these rewards on task behaviour and self-reported experience. With rewards, participants more thoroughly explored the design space, and maximised goal-aligned over goal-agnostic rewards while preserving diversity across designs. The nature of the goal also mattered, influencing participants' perception of the reward's usefulness. Building on these insights, we propose guidelines for designing effective feedback for design decision making.

---


### 23. [FruitProM-V2: Robust Probabilistic Maturity Estimation and Detection of Fruits and Vegetables](https://arxiv.org/abs/2604.26084)

**<font color=#1a73e8>作者：</font>** Rahul Harsha Cheppally, Sidharth Rai, Sudan Baral 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate fruit maturity identification is essential for determining harvest timing, as incorrect assessment directly affects yield and post-harvest quality. Although ripening is a continuous biological process, vision-based maturity estimation is typically formulated as a multi-class classification task, which imposes sharp boundaries between visually similar stages. To examine this limitation, we perform an annotation reliability study with two independent annotators on a held-out tomato dataset and observe disagreement concentrated near adjacent maturity stages. Motivated by this observation, we model maturity as a latent continuous variable and predict it probabilistically using a distributional detection head, converting the distribution into class probabilities through the cumulative distribution function (CDF). The proposed formulation maintains comparable performance to a standard detector under clean labels while better representing uncertainty. Furthermore, when controlled label noise is introduced during training, the probabilistic model demonstrates improved robustness relative to the baseline, indicating that explicitly modeling maturity uncertainty leads to more reliable visual maturity estimation.

---


### 24. [Operating-Layer Controls for Onchain Language-Model Agents Under Real Capital](https://arxiv.org/abs/2604.26091)

**<font color=#1a73e8>作者：</font>** T.J. Barton, Chris Constantakis, Patti Hauseman 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study reliability in autonomous language-model agents that translate user mandates into validated tool actions under real capital. The setting is DX Terminal Pro, a 21-day deployment in which 3,505 user-funded agents traded real ETH in a bounded onchain market. Users configured vaults through structured controls and natural-language strategies, but only agents could choose normal buy/sell trades. The system produced 7.5M agent invocations, roughly 300K onchain actions, about $20M in volume, more than 5,000 ETH deployed, roughly 70B inference tokens, and 99.9% settlement success for policy-valid submitted transactions. Long-running agents accumulated thousands of sequential decisions, including 6,000+ prompt-state-action cycles for continuously active agents, yielding a large-scale trace from user mandate to rendered prompt, reasoning, validation, portfolio state, and settlement. Reliability did not come from the base model alone; it emerged from the operating layer around the model: prompt compilation, typed controls, policy validation, execution guards, memory design, and trace-level observability. Pre-launch testing exposed failures that text-only benchmarks rarely measure, including fabricated trading rules, fee paralysis, numeric anchoring, cadence trading, and misread tokenomics. Targeted harness changes reduced fabricated sell rules from 57% to 3%, reduced fee-led observations from 32.5% to below 10%, and increased capital deployment from 42.9% to 78.0% in an affected test population. We show that capital-managing agents should be evaluated across the full path from user mandate to prompt, validated action, and settlement.

---


### 25. [GenDetect: Generalizing Reactive Detection for Resilience Against Imitative DeFi Attack Cascade](https://arxiv.org/abs/2604.26094)

**<font color=#1a73e8>作者：</font>** Bowen Cai, Weiheng Bai, Youshui Lu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As blockchain ecosystems grow, financially motivated attackers increasingly exploit decentralized finance (DeFi) protocols, causing frequent and severe losses. Unlike conventional cyberattacks, DeFi exploits propagate rapidly due to the transparent and composable nature of smart contracts. We identify a critical pattern, Imitative Attack Cascade: an initial successful exploit is quickly followed by mimicking transactions that reuse attack logic with minor modifications or parameter changes. Our empirical analysis shows that over 69% of DeFi attacks exhibit strong behavioral similarity to earlier incidents, often within hours or days of the initial attack.
This exposes a fundamental limitation in current reactive detection. Initial attacks are typically flagged via heuristic alerts (Tornado Cash traces, anomalous nonce usage, exploiter labels), but turning these signals into detection rules requires manual validation and handcrafted trace analysis -- a labor-intensive, slow process that leaves follow-up attacks to spread. Our goal is to ensure that once an attack has been observed, even a single instance, it can be rapidly abstracted into an actionable, generalizable detection rule.
We decompose the problem into two challenges: (I) abstracting the semantics of diverse, obscure function signatures, and (II) matching transaction logic in noisy, evasive traces. We leverage two insights: (i) the open-source nature of most DeFi protocols enables high-fidelity semantic classification of function signatures; (ii) contract labels isolate essential logic by filtering irrelevant calls and classifying attack intent. Building on these, we develop GenDetect, which achieves ACC 98%, FPR 1%, FNR 3% and discovers 56 previously unrevealed attacks from the past three years. Source code and dataset: this https URL

---


### 26. [Distill-Belief: Closed-Loop Inverse Source Localization and Characterization in Physical Fields](https://arxiv.org/abs/2604.26095)

**<font color=#1a73e8>作者：</font>** Yiwei Shi, Zixing Song, Mengyue Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> {Closed-loop inverse source localization and characterization (ISLC) requires a mobile agent to select measurements that localize sources and infer latent field parameters under strict time constraints.} {The core challenge lies in the belief-space objective: valid uncertainty estimation requires expensive Bayesian inference, whereas using fast learned belief model leads to reward hacking, in which the policy exploits approximation errors rather than actually reducing uncertainty.} {We propose \textbf{Distill-Belief}, a teacher--student framework that decouples correctness from efficiency. A Bayes-correct particle-filter teacher maintains the posterior and supplies a dense information-gain signal, while a compact student distills the posterior into belief statistics for control and an uncertainty certificate for stopping. At deployment, only the student is used, yielding constant per-step cost.} {Experiments on seven field modalities and two stress tests show that Distill-Belief consistently reduces sensing cost and improves success, posterior contraction, and estimation accuracy over baselines, while mitigating reward hacking.}

---


### 27. [Momentum-Conserving Graph Neural Networks for Deformable Objects](https://arxiv.org/abs/2604.26097)

**<font color=#1a73e8>作者：</font>** Jiahong Wang, Logan Numerow, Stelian Coros 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural networks (GNNs) have emerged as a versatile and efficient option for modeling the dynamic behavior of deformable materials. While GNNs generalize readily to arbitrary shapes, mesh topologies, and material parameters, existing architectures struggle to correctly predict the temporal evolution of key physical quantities such as linear and angular momentum. In this work, we propose MomentumGNN -- a novel architecture designed to accurately track momentum by construction. Unlike existing GNNs that output unconstrained nodal accelerations, our model predicts per-edge stretching and bending impulses which guarantee the preservation of linear and angular momentum. We train our network in an unsupervised fashion using a physics-based loss, and we show that our method outperforms baselines in a number of common scenarios where momentum plays a pivotal role.

---


### 28. [Evaluating Strategic Reasoning in Forecasting Agents](https://arxiv.org/abs/2604.26106)

**<font color=#1a73e8>作者：</font>** Tom Liptay, Dan Schwarz, Rafael Poyiadzi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Forecasting benchmarks produce accuracy leaderboards but little insight into why some forecasters are more accurate than others. We introduce Bench to the Future 2 (BTF-2), 1,417 pastcasting questions with a frozen 15M-document research corpus in which agents reproducibly research and forecast offline, producing full reasoning traces. BTF-2 detects accuracy differences of 0.004 Brier score, and can distinguish differential agent strengths in research vs. judgment. We build a forecaster 0.011 Brier more accurate than any single frontier agent, and use it to evaluate agent strategic reasoning without hindsight bias. We find the better forecaster differs primarily in its pre-mortem analysis of its blind spots and consideration of black swans. Expert human forecasters found the dominant strategic reasoning failures of frontier agents are in assessing political and business leaders' incentives, judging their likelihood to follow through on stated plans, and modeling institutional processes.

---


### 29. [Human-Augmented Reality Interaction in Rebar Inspection](https://arxiv.org/abs/2604.26112)

**<font color=#1a73e8>作者：</font>** Mahsa Sanei, Fernando Moreu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Rebar inspection in reinforced concrete construction requires sustained awkward postures and complex mental mapping of two-dimensional drawings onto three-dimensional assemblies. This study evaluated an Augmented Reality (AR)-assisted rebar inspection system deployed on Microsoft HoloLens 2 through a within-subjects experiment with 30 participants. Full-body kinematics were recorded using a motion capture system at 100 Hz while participants performed traditional and AR-assisted spacing inspection. AR reduced mean trunk flexion by 30.8%, mean neck flexion by 32.8%, and task completion time by 67.7%. Walking distance and hand-path length each decreased by over 50%. NASA Task Load Index scores decreased by 45.6% overall, with the largest reduction in physical demand. Inspection accuracy was maintained across conditions. The System Usability Scale yielded a mean score of 76.1 with 83% of participants rating the system acceptable. These results provide convergent objective and subjective evidence that AR-assisted inspection reduces ergonomic risk and perceived workload maintaining inspection quality.

---


### 30. [Sample Selection Using Multi-Task Autoencoders in Federated Learning with Non-IID Data](https://arxiv.org/abs/2604.26116)

**<font color=#1a73e8>作者：</font>** Emre Ardıç, Yakup Genç  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Federated learning is a machine learning paradigm in which multiple devices collaboratively train a model under the supervision of a central server while ensuring data privacy. However, its performance is often hindered by redundant, malicious, or abnormal samples, leading to model degradation and inefficiency. To overcome these issues, we propose novel sample selection methods for image classification, employing a multitask autoencoder to estimate sample contributions through loss and feature analysis. Our approach incorporates unsupervised outlier detection, using one-class support vector machine (OCSVM), isolation forest (IF), and adaptive loss threshold (AT) methods managed by a central server to filter noisy samples on clients. We also propose a multi-class deep support vector data description (SVDD) loss controlled by a central server to enhance feature-based sample selection. We validate our methods on CIFAR10 and MNIST datasets across varying numbers of clients, non-IID distributions, and noise levels up to 40%. The results show significant accuracy improvements with loss-based sample selection, achieving gains of up to 7.02% on CIFAR10 with OCSVM and 1.83% on MNIST with AT. Additionally, our federated SVDD loss further improves feature-based sample selection, yielding accuracy gains of up to 0.99% on CIFAR10 with OCSVM. These results show the effectiveness of our methods in improving model accuracy across various client counts and noise conditions.

---


### 31. [Hierarchical Multi-Persona Induction from User Behavioral Logs: Learning Evidence-Grounded and Truthful Personas](https://arxiv.org/abs/2604.26120)

**<font color=#1a73e8>作者：</font>** Nayoung Choi, Haeyu Jeong, Changbong Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Behavioral logs provide rich signals for user modeling, but are noisy and interleaved across diverse intents. Recent work uses LLMs to generate interpretable natural-language personas from user logs, yet evaluation often emphasizes downstream utility, providing limited assurance of persona quality itself. We propose a hierarchical framework that aggregates user actions into intent memories and induces multiple evidence-grounded personas by clustering and labeling these memories. We formulate persona induction as an optimization problem over persona quality-captured by cluster cohesion, persona-evidence alignment, and persona truthfulness-and train the persona model using a groupwise extension of Direct Preference Optimization (DPO). Experiments on a large-scale service log and two public datasets show that our method induces more coherent, evidence-grounded, and trustworthy personas, while also improving future interaction prediction.

---


### 32. [Spatially-constrained clustering of geospatial features for heat vulnerability assessment of favelas in Rio de Janeiro](https://arxiv.org/abs/2604.26133)

**<font color=#1a73e8>作者：</font>** Baptiste Clemence, Thomas Hallopeau, Vanderlei Pascoal De Matos 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Informal settlements face disproportionate exposure to climate-related health hazards. However, existing methodologies lack systematic approaches to link diverse settlement characteristics with environmental health outcomes. We develop a data-driven framework to assess heat vulnerability in Rio de Janeiro's favelas by combining spatially-constrained clustering with land surface temperature (LST) analysis. Using remote sensing and geospatial features, we identify two distinct favela typologies: recent, well-connected settlements on flat terrain (Cluster 0) and historical, poorly-connected communities on vegetated slopes (Cluster 1). Analysis of 16 extreme heat events reveals systematic temperature differences of 2--3$^\circ$C between clusters, with flat-terrain favelas experiencing significantly higher heat exposure. Our findings demonstrate that settlement morphology critically influences heat vulnerability, providing a replicable framework for targeted urban planning and public health interventions in informal settlements globally.

---


### 33. [MixerCA: An Efficient and Accurate Model for High-Performance Hyperspectral Image Classification](https://arxiv.org/abs/2604.26138)

**<font color=#1a73e8>作者：</font>** Mohammed Q. Alkhatib, Ali Jamali  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Over the past decade, hyperspectral image (HSI) classification has drawn considerable interest due to HSIs' ability to effectively distinguish terrestrial objects by capturing detailed, continuous spectral information. The strong performance of recent deep learning techniques in tasks like image classification and semantic segmentation has led to their growing use in HSI classification, due to their ability to capture complex spatial and spectral features more effectively than traditional methods. This paper presents MixerCA, a novel lightweight model for HSI classification that leverages depthwise convolution and a self-attention mechanism. MixerCA integrates depth-wise convolutions, token and channel mixing, and coordinate attention into a unified structure to decouple spatial and channel interactions, maintain consistent resolution throughout the network, and directly process HSI patches. Extensive experiments on four hyperspectral benchmark datasets reveal MixerCA's clear advantages over several competing algorithms, including 2D-CNN, 3D-CNN, Tri-CNN, HybridSN, ViT, and Swin Transformer. The source code is publicly available at this https URL.

---


### 34. [Ceci n'est pas une explication: Evaluating Explanation Failures as Explainability Pitfalls in Language Learning Systems](https://arxiv.org/abs/2604.26145)

**<font color=#1a73e8>作者：</font>** Ben Knight, Wm. Matthew Kennedy, James Edgell  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI-powered language learning tools increasingly provide instant, personalised feedback to millions of learners worldwide. However, this feedback can fail in ways that are difficult for learners--and even teachers--to detect, potentially reinforcing misconceptions and eroding learning outcomes over extended use. We present a portion of L2-Bench, a benchmark for evaluating AI systems in language education that includes (but is not limited to) six critical dimensions of effective feedback: diagnostic accuracy, awareness of appropriacy, causes of error, prioritisation, guidance for improvement, and supporting self-regulation. We analyse how AI systems can fail with respect to these dimensions. These failures, which we argue are conducive to "explainability pitfalls," are AI-generated explanations that appear helpful on the surface but are fundamentally flawed, increasing the risk of attainment, human-AI interaction, and socioaffective harms. We discuss how the specific context of language learning amplifies these risks and outline open questions we believe merit more attention when designing evaluation frameworks specifically. Our analysis aims to expand the community's understanding of both the typology of explainability pitfalls and the contextual dynamics in which they may occur in order to encourage AI developers to better design safe, trustworthy, and effective AI explanations.

---


### 35. [A Data-Centric Framework for Intraoperative Fluorescence Lifetime Imaging for Glioma Surgical Guidance](https://arxiv.org/abs/2604.26147)

**<font color=#1a73e8>作者：</font>** Silvia Noble Anbunesan, Mohamed Abul Hassan, Jinyi Qi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate intraoperative assessment of glioma infiltration is essential for maximizing tumor resection while preserving functional brain tissue. Fluorescence lifetime imaging (FLIm) offers real-time, label-free biochemical contrast, but its clinical utility is challenged by biological heterogeneity, class imbalance, and variability in histopathological labeling. We present a data-centric AI (DC-AI) framework that integrates confident learning (CL), class refinement, and targeted label evaluation to develop a robust multi-class FLIm classifier for glioblastoma (GBM) resection margins. FLIm data were collected from 192 tissue margins across 31 newly diagnosed IDH-wildtype GBM patients and initially labeled into seven tumor cellularity classes by an expert neuropathologist. CL was applied to quantify FLIm point-level confidence, identify label inconsistencies, and guide iterative class merging into a three-class scheme ("low", "moderate", "high"). The resulting high-fidelity dataset enabled training a model that achieved 96% accuracy in the three-class task. SHAP analysis revealed class-specific FLIm feature importance, highlighting distinct optical signatures across the infiltration spectrum. Targeted FLIm analysis further identified biological (e.g., gray matter composition) and acquisition-related (e.g., blood contamination) contributors to low-confidence predictions. Blinded re-evaluation of margins flagged by CL demonstrated intra-pathologist variability, underscoring the value of selective relabeling rather than exhaustive review. Together, these findings demonstrate that a DC-AI framework can systematically improve data reliability, enhance model robustness, and refine biological interpretation of FLIm signals, supporting the development of clinically actionable optical tools for real-time glioma margin assessment.

---


### 36. [Beyond Screenshots: Evaluating VLMs' Understanding of UI Animations](https://arxiv.org/abs/2604.26148)

**<font color=#1a73e8>作者：</font>** Chen Liang, Xirui Jiang, Naihao Deng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI agents operating on user interfaces must understand how interfaces communicate state and feedback to act reliably. As a core communicative modality, animations are increasingly used in modern interfaces, serving critical functional purposes beyond mere aesthetics. Thus, understanding UI animation is essential for comprehensive interface interpretation. However, recent studies of Vision Language Models (VLMs) for UI understanding have focused primarily on static screenshots, leaving it unclear how well these models handle dynamic UI animations. To address this gap, we created AniMINT, a novel dataset of 300 densely annotated UI animation videos. We systematically evaluate state-of-the-art VLMs on UI animation understanding, including their abilities to perceive the animation effects, identify animation purposes, and interpret animation meaning. Our results show that VLMs can reliably detect primitive motion. However, their high-level animation interpretation remains inconsistent, with substantial gaps relative to human performance. Finally, we use Motion, Context, and Perceptual Cues (MCPC) to probe factors affecting VLM performance, revealing key bottlenecks and directions for future improvement.

---


### 37. [Structural Generalization on SLOG without Hand-Written Rules](https://arxiv.org/abs/2604.26157)

**<font color=#1a73e8>作者：</font>** Zichao Wei  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Structural generalization in semantic parsing requires systems to apply learned compositional rules to novel structural combinations. Existing approaches either rely on hand-written algebraic rules (AM-Parser) or fail to generalize structurally (Transformer-based models). We present an alternative requiring no hand-written compositional rules, based on a neural cellular automaton (NCA) with a discrete bottleneck: all compositional rules are learned from data through local iteration. On the SLOG benchmark, the system achieves 100% type-exact match on 11 of 17 structural generalization categories, including three where AM-Parser scores 0 to 74%, with an overall standard deviation of 0.2 across 10 seeds (vs. AM-Parser's 4.3). Analysis reveals that all 5,539 failure instances reduce to exactly two mechanisms: novel combinations of wh-extraction context with reduced verb types, and modifiers appearing on the subject side of this http URL we decompose results by CCG structural features, each sub-pattern either succeeds on all instances or fails on all. Intermediate scores (e.g., 41.4%) are mixtures of structurally distinct CCG patterns, not partial this http URL failures correspond to directed operations absent from training; all successes correspond to operations already covered.

---


### 38. [Test-Time Safety Alignment](https://arxiv.org/abs/2604.26167)

**<font color=#1a73e8>作者：</font>** Baturay Saglam, Dionysis Kalogerias  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent work has shown that a model's input word embeddings can serve as effective control variables for steering its behavior toward outputs that satisfy desired properties. However, this has only been demonstrated for pretrained text-completion models on the relatively simple objective of reducing surface-level profanity in short continuations. A natural and practically important question is how well input embeddings can control aligned models, which produce an imbalanced bimodal refuse-or-comply output distribution rather than the smooth distribution characteristic of open-ended generation. We explore this in the context of safety, showing that input word embeddings can be optimized in a sub-lexical manner to minimize the semantic harmfulness of aligned model responses. Our approach uses zeroth-order gradient estimation of a black-box text-moderation API with respect to the input embeddings, and then applies gradient descent on these embeddings to minimize the harmfulness of the generated text. Experiments show that the proposed method can neutralize every safety-flagged response on standard safety benchmarks.

---


### 39. [Budget-Constrained Causal Bandits: Bridging Uplift Modeling and Sequential Decision-Making](https://arxiv.org/abs/2604.26169)

**<font color=#1a73e8>作者：</font>** Abhirami Pillai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Treatment allocation under budget constraints is a central challenge in digital advertising: advertisers must decide which users to show ads to while spending a limited budget wisely. The standard approach follows a two-stage offline pipeline - first collect historical data to estimate heterogeneous treatment effects (HTE), then solve a constrained optimization to allocate the budget. This works well with abundant data, but fails in cold-start settings such as new campaigns, new markets, or new customer segments where little historical data exists. We propose Budget-Constrained Causal Bandits (BCCB), an online framework that learns which users respond to ads while simultaneously spending the budget, making treatment decisions one user at a time. BCCB unifies three components into a single sequential process: learning individual-level ad effectiveness, exploring users whose response is uncertain, and pacing the budget over time. We evaluated on the Criteo Uplift dataset, a large-scale advertising dataset from a real randomized controlled trial. Our key finding is a data-efficiency crossover: offline methods require approximately 10,000 historical observations to produce reliable results, while BCCB operates effectively from the very first user. Furthermore, BCCB exhibits 3-5x lower performance variance between runs, making it more practical for real campaign planning. Among purely online methods, BCCB consistently outperforms standard Thompson Sampling, budgeted Thompson Sampling, and greedy HTE estimation across all budget levels tested.

---


### 40. [Why Domain Matters: A Preliminary Study of Domain Effects in Underwater Object Detection](https://arxiv.org/abs/2604.26174)

**<font color=#1a73e8>作者：</font>** Melanie Wille, Dimity Miller, Tobias Fischer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Domain shift, where deviations between training and deployment data distributions degrade model performance, is a key challenge in underwater environments. Existing benchmarks testing performance for underwater domain shift simulate variability through synthetic style transfer. This fails to capture intrinsic scene factors such as visibility, illumination, scene composition, or acquisition factors, limiting analysis of real-world effects. We propose a labeling framework that defines underwater domains using measurable image, scene, and acquisition characteristics. Unlike prior benchmarks, it captures physically meaningful factors, enabling semantically consistent image grouping and supporting domain-specific evaluation of detection performance including failure analysis. We validate this on public datasets, showing systematic variations across domain factors and revealing hidden failure modes.

---


### 41. [Privacy-Preserving Clothing Classification using Vision Transformer for Thermal Comfort Estimation](https://arxiv.org/abs/2604.26184)

**<font color=#1a73e8>作者：</font>** Tatsuya Chuman, Yousuke Udagawa, Hitoshi Kiya  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A privacy-preserving clothing classification scheme is presented to enable secure occupant-centric control (OCC) systems. Although the utilization of camera images for HVAC control has been widely studied to optimize thermal comfort, privacy protection of occupant images has not been considered in prior works. While various privacy-preserving methods have been proposed for image classification, applying conventional schemes results in severe accuracy degradation. In this paper, we introduce a privacy-preserving classification method using Vision Transformer (ViT) applied to clothing insulation estimation. In an experiment using the DeepFashion dataset categorized by clothing insulation, while the conventional pixel-based method suffers a severe accuracy drop, our scheme maintains a high accuracy on encrypted images, showing no degradation from plain images across all categories.

---


### 42. [Efficient and Interpretable Transformer for Counterfactual Fairness](https://arxiv.org/abs/2604.26188)

**<font color=#1a73e8>作者：</font>** Panyi Dong, Zhiyu Quan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The growing reliance of machine learning models in high-stakes, highly regulated domains such as finance and insurance has created a growing tension between predictive performance, interpretability, and regulatory fairness requirements. In these settings, models are expected not only to deliver reliable predictions but also to provide transparent decision rationales and comply with strict fairness requirements. Attention-based transformers offer powerful mechanisms for modeling complex data relationships as demonstrated in various language tasks, yet their attention mechanisms alone do not ensure counterfactually fair predictions, even when combined with fairness-aware techniques. To address these limitations, we propose the Feature Correlation Transformer (FCorrTransformer), an attention-light architecture tailored for tabular data. In this design, the attention matrix admits a direct statistical interpretation as pairwise feature dependencies, enhancing both interpretability and efficiency. Leveraging this structure, we introduce Counterfactual Attention Regularization (CAR), a framework that enforces group-invariant fair representations of sensitive features at the attention level, promoting counterfactually fair predictions without relying on explicit causal assumptions. Empirical evaluations on imbalanced classification and regression benchmarks demonstrate that FCorrTransformer combined with CAR achieves strong counterfactual fairness while maintaining competitive predictive performance and substantially reducing model complexity compared with standard transformer-based baselines. Overall, this work bridges a critical gap between fairness theory and machine learning models, offering a practical framework for responsible AI in regulatory-sensitive domains.

---


### 43. [Option-Order Randomisation Reveals a Distributional Position Attractor in Prompted Sandbagging](https://arxiv.org/abs/2604.26206)

**<font color=#1a73e8>作者：</font>** Jon-Paul Cacioli  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A predecessor pilot (Cacioli, 2026) found that Llama-3-8B implements prompted sandbagging as positional collapse rather than answer avoidance. However, fixed option ordering in MMLU-Pro left open whether this reflected a model-level position-dominant policy or dataset-level distractor structure. This pre-registered follow-up (3 models, 2,000 MMLU-Pro items, 4 conditions, 24,000 primary trials) added cyclic option-order randomisation as the critical control. The pre-registered item-level same-letter diagnostic did not confirm deterministic position-tracking (same-letter rate 37.3%, below the 50% threshold). However, pre-specified supporting analyses revealed that the response-position distribution under sandbagging was highly stable under complete content rotation (Pearson r = 0.9994; Jensen-Shannon divergence = 0.027, compared to 0.386 between honest and sandbagging conditions). Accuracy spiked to 72.1% when the correct answer coincidentally occupied the preferred position E, and fell to 4.3% at position A. The data provide strong evidence for a soft distributional attractor: under sandbagging instruction, the model enters a low-entropy response-position basin centred on E/F/G that is highly stable and largely content-invariant at the aggregate level. Qwen-2.5-7B served as a negative control (non-compliant, no distributional shift). These results provide evidence, at the 7-9 billion parameter scale, that response-position entropy is a promising black-box behavioural signature of this sandbagging mode.

---


### 44. [OMEGA: Optimizing Machine Learning by Evaluating Generated Algorithms](https://arxiv.org/abs/2604.26211)

**<font color=#1a73e8>作者：</font>** Jeremy Nixon, Annika Singh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In order to automate AI research we introduce a full, end-to-end framework, OMEGA: Optimizing Machine learning by Evaluating Generated Algorithms, that starts at idea generation and ends with executable code. Our system combines structured meta-prompt engineering with executable code generation to create new ML classifiers. The OMEGA framework has been utilized to generate several novel algorithms that outperform scikit-learn baselines across a robust selection of 20 benchmark datasets (infinity-bench). You can access models discussed in this paper and more in the python package: pip install omega-models.

---


### 45. [Exploring the Feasibility and Acceptability of AI-Mediated Serious Illness Conversations in the Emergency Department](https://arxiv.org/abs/2604.26214)

**<font color=#1a73e8>作者：</font>** Hasibur Rahman, Kenji Numata, Evelyn T Lai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Serious illness conversations (SICs) align care with patients' values, goals, and preferences, yet they rarely occur in emergency departments (EDs), where time constraints and emotional burden often leave clinicians making high-stakes decisions without documented insight into what matters most to patients. We present a case study of ED GOAL-AI, a voice-based conversational agent for brief, structured values discussions with older adults in the ED, evaluated with 55 patients for feasibility and acceptability. Most participants completed the conversation and reported the interaction as acceptable and feasible, with ratings of feeling heard and understood comparable to clinicians. However, we also observed critical failure modes, including boundary violations such as hallucinated diagnostic statements, highlighting ethical and emotional risks. This work points to early promise for AI-mediated SICs while underscoring the need for careful boundary setting and participatory design before broader deployment.

---


### 46. [Unsupervised Graph Modeling for Anomaly Detection in Accounting Subject Relationships](https://arxiv.org/abs/2604.26216)

**<font color=#1a73e8>作者：</font>** Yuhan Wang, Ruobing Yan, Zhe Su 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper addresses the problem of anomaly detection in accounting subject association structures, proposing a structured modeling and unsupervised discriminant framework based on graph neural networks. This framework is used to mine stable correspondences between subjects and identify structural deviations from general ledger details and voucher entries. The method first abstracts accounting subjects as graph nodes, and the co-occurrence and debit/credit correspondence of subjects in the same business record are abstracted as weighted edges. The edge weights are characterized by statistical measures such as co-occurrence frequency or amount aggregation, thus forming a period-level accounting subject association graph. In the representation learning stage, a message passing mechanism is used to fuse the node's own attributes and neighborhood context to obtain node embeddings containing structural information. In the anomaly detection stage, the rationality of subject pair connections is estimated through a relation reconstruction decoder, and edge-level anomaly scores are defined based on the degree of deviation in reconstruction probabilities. These scores are then aggregated to obtain node-level risk ranking and local anomaly localization. This framework can simultaneously capture local substructure anomalies and cross-community anomaly connections without relying on anomaly labeling, outputting traceable subject pair risk clues. Comparative experiments demonstrate more stable comprehensive discriminant capabilities and higher top-ranking accuracy.

---


### 47. [ViBE: Visual-to-M/EEG Brain Encoding via Spatio-Temporal VAE and Distribution-Aligned Projection](https://arxiv.org/abs/2604.26218)

**<font color=#1a73e8>作者：</font>** Ganxi Xu, Zhao-Rong Lai, Yuting Tang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Brain encoding models not only serve to decipher how visual stimuli are transformed into neural responses, but also represent a critical step toward visual prostheses that restore vision for patients with severe vision disorders. Brain encoding involves two fundamental steps: achieving faithful reconstruction of neural responses and establishing cross-modal alignment between visual stimuli and neural responses. To this end, we propose ViBE, a novel brain encoding framework for generating magnetoencephalography (MEG) and electroencephalography (EEG) signals from visual stimuli. Specifically, we first design a spatio-temporal convolutional variational autoencoder (TSC-VAE) that captures the spatio-temporal characteristics of M/EEG signals for effective neural response reconstruction. To bridge the modality gap between visual features and neural representations, we employ Q-Former to map CLIP image embeddings to the TSC-VAE latent space, producing neural proxy embeddings. For comprehensive cross-modal alignment, we combine mean squared error (MSE) loss for point-wise feature matching with sliced Wasserstein distance (SWD) for probability distribution alignment between the neural proxy embeddings and TSC-VAE latent embeddings. We conduct extensive experiments on the THINGS-EEG2 and THINGS-MEG datasets, demonstrating the effectiveness of our approach in generating high-quality M/EEG signals from visual stimuli.

---


### 48. [eDySec: A Deep Learning-based Explainable Dynamic Analysis Framework for Detecting Malicious Packages in PyPI Ecosystem](https://arxiv.org/abs/2604.26219)

**<font color=#1a73e8>作者：</font>** Sk Tanzir Mehedi, Raja Jurdak, Chadni Islam 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The security of open-source software repositories is increasingly threatened by next-gen software supply chain attacks. These attacks include multiphase malware execution, remote access activation, and dynamic payload generation. Traditional Machine Learning (ML) detectors struggle to detect these attacks due to the high-dimensional and sparse nature of dynamic behavioral data, including system calls, network traffic, directory access patterns, and dependency logs. As a result, these data characteristics degrade the performance, stability, and explainability of ML models. These challenges have made Deep Learning (DL) a promising alternative, given its success across various domains and its potential for modeling complex patterns. This paper presents eDySec, a DL-based efficient, stable, and explainable framework for dynamic behavioral analysis to detect malicious packages. Using the QUT-DV25 dataset, which captures both install-time and post-installation behaviors of packages, we evaluate DL models and investigate feature sets to identify the most discriminative attributes for enabling efficient malicious package detection. Additionally, model stability analysis and explainable AI techniques are incorporated into the detection pipeline to enable stable, and transparent interpretations of model decisions. Experimental results demonstrate that eDySec significantly outperforms the state-of-the-art frameworks. Specifically, it halves feature dimensionality while lowering false positives by 82% and false negatives by 79%. It also improves accuracy by 3%, achieves near-perfect stability, and maintains an inference latency of 170ms per package. Further analysis reveals that feature and model selection play a critical role, as certain combinations degrade performance. Ultimately, this study advances the understanding of the strengths and limitations of dynamic analysis against next-gen attacks.

---


### 49. [When Agents Shop for You: Role Coherence in AI-Mediated Markets](https://arxiv.org/abs/2604.26220)

**<font color=#1a73e8>作者：</font>** Soogand Alavi, Salar Nozari  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Consumers are increasingly delegating purchase decisions to AI agents, providing natural-language descriptions of their preferences and identity. We argue that these representations constitute an information channel, role coherence, through which sellers can infer willingness to pay without explicit disclosure by the buyer agent, leading to preference leakage. In an experiment where a language-model buyer agent shops on behalf of a verbal consumer profile, we show that seller-side inference from dialogue alone recovers willingness to pay nearly one-for-one. Comparing this setting to a numeric-budget condition with confidentiality instructions cleanly isolates role coherence as distinct from instruction-following failure. Because this leakage arises from delegation itself, it cannot be mitigated at the prompt level. Instead, we propose architectural interventions that trade off personalization against preference privacy.

---


### 50. [Seeking Consensus: Geometric-Semantic On-the-Fly Recalibration for Open-Vocabulary Remote Sensing Semantic Segmentation](https://arxiv.org/abs/2604.26221)

**<font color=#1a73e8>作者：</font>** Guanchun Wang, Chenxiao Wu, Xiangrong Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary semantic segmentation (OVSS) in remote sensing images is a promising task that employs textual descriptions for identifying undefined land cover categories. Despite notable advances, existing methods typically employ a static inference paradigm, overlooking the distinct distribution of each scene, resulting in semantic ambiguity in diverse land covers and incomplete foreground activation. Motivated by this, we propose Seeking Consensus, termed SeeCo, a plug-and-play framework to boost the performance of training-free OVSS models in remote sensing images, which recalibrates arbitrary OVSS models on-the-fly by seeking dual consensus: geometric consensus learning (GCL) through multi-view consistent observations and semantic consensus learning (SCL) via textual description adaptive calibration, which assists collaborative recalibration of visual and textual semantics. The two consensus are injected via an online consensus injector (OCI), effectively alleviating the under-activation and semantic bias. SeeCo requires no specific training process, yet recalibrates semantic-geometric alignment for each unique scene during inference. Extensive experiments on eight remote sensing OVSS benchmarks show consistent gains, proving its effectiveness and universality.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-173](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
