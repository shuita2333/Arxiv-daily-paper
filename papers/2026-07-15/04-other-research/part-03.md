# 📦 其他研究 | 2026年07月15日

> 本类共 **420** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-420](./part-09.md)

---

### 101. [DynaFilter: Cloud-driven Dynamic Filtering for Satellite Edge Intelligence](https://arxiv.org/abs/2607.10098)

**<font color=#1a73e8>作者：</font>** Ziyang Zhang, Jie Liu, Luca Mottola  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern satellite edge systems, including those performing remote sensing tasks such object detection and tracking, are characterized by severely limited bandwidth and intermittent connections, making continuous data transmission to the cloud impractical. Existing edge-cloud systems, however, either require heavy pre-processing before analysis, for instance, full decompression of imagery data, or transmit all compressed data regardless of relevance. To address these challenges, we design DynaFilter, a dynamic filtering technique that enables satellite edge devices to perform selective region-of-interest (RoI) inference directly in the compressed-domain, without full decompression. Our key insight is that low-level compression syntax, specifically DC coefficients/AC energy in JPEG images and motion vectors in video streams, exhibits strong correlations with high-level semantic queries. By establishing a precise mapping between cloud query semantics and multimodal compressed-domain features, DynaFilter enables the edge to identify and transmit only relevant data associated to RoIs. Extensive evaluations show that DynaFilter reduces the total volume of pixel data for decoding and subsequent inference by 1.6x-7.1x for images, and achieves 92.0% bandwidth savings for video streams compared to state-of-the-art baselines. Furthermore, it decreases energy consumption by 43.1-88.6% on target devices and achieves a 1.6x-3.0x speedup in inference latency.

---


### 102. [Learning behavior accounts for background-related advantage in AI-assisted education](https://arxiv.org/abs/2607.10101)

**<font color=#1a73e8>作者：</font>** Jingwei Yi, Yueqi Xie, Jiyan He 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI has been found, and will likely be found increasingly, useful in education. However, existing AI-for-education studies provide inconsistent evidence on its average effects. More broadly, research on prior educational technologies shows that average effects often mask substantial heterogeneity across student populations. Motivated by this evidence, this study examines heterogeneity in students' learning behavior with AI, which students benefit from AI assistance, and how learner profiles and learning behavior shape these patterns. To this end, we recruited 318 university students to participate in structured learning experiments lasting up to 125 minutes. Our findings indicate that students' learning behavior is strongly associated with learning outcomes, with behaviors characterized by proactive and critical engagement, rather than limited engagement, associated with significantly better performance. These behavioral differences are related to learner profiles, with students from higher-ranking universities and those with greater prior knowledge tending to benefit more, consistent with their greater likelihood of adopting proactive interaction strategies. Accounting for learning behavior substantially weakens or eliminates the associations between learner profiles and learning outcomes, suggesting that how students use AI is a key pathway through which background differences are linked to learning gains. Overall, this work provides a deeper understanding of AI assistance in education by showing how differences in learner profiles and learning behavior shape who benefits from AI-supported learning. These insights can help educators and students better navigate and integrate AI into educational practices.

---


### 103. [Dynamic Agent Skills: A Lifecycle Survey and Taxonomy of Evolving Skill Libraries](https://arxiv.org/abs/2607.10113)

**<font color=#1a73e8>作者：</font>** Yubo Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents increasingly store reusable procedures outside the model. These reusable procedures are often called \emph{skills}: they may be code functions, natural-language instructions, this http URL packages, workflow graphs, or learned adapters that a future agent can retrieve and invoke. This taxonomy-driven survey asks how such skill libraries change over time. Across a $124$-paper $2023$--$2026$ audit set, we synthesize dynamic skill systems as \emph{lifecycle-managed, verified, evolving artifact stores}: agents collect evidence from interaction, propose skill updates, verify and admit candidates, organize them for retrieval and composition, repair or prune stale entries, and govern sharing through provenance and rollback. We organize the literature around three survey tools. First, a $\text{six}$-sense taxonomy distinguishes the structurally different artifacts called ``skills'' in current papers. Second, an $\text{eight}$-stage lifecycle architecture identifies the recurring design decisions behind evidence acquisition, proposal, verification/admission, storage, retrieval/composition, maintenance, distillation/portability, and governance. Third, a lightweight skill-record schema and $\text{ten}$-operator vocabulary provide common terms for comparing library updates without elevating them into a separate method contribution. Using this structure, we synthesize evidence-graded patterns with explicit caveats: admission and repair are repeatedly important, verifier quality materially affects skill-aware RL, flat retrieval can degrade as libraries grow, and current benchmarks still under-report library trajectories, usage--utility gaps, and safety surfaces. We close with concrete reporting standards and open problems for evaluating dynamic skills as changing libraries rather than static prompt or tool collections.

---


### 104. [Cost of Reasoning in non-English Languages: A Case Study on Japanese](https://arxiv.org/abs/2607.10114)

**<font color=#1a73e8>作者：</font>** Yuu Jinnai  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning Language Models (RLMs) achieve their strongest performance when they reason in English, the language for which reasoning-oriented training data is most abundant. However, reasoning trace is a clue for model interpretability and safety, and useful in practice for both the model users and for model developers. Thus, it is desirable to be able to develop a model that reasons in a language of the user's choice, while still maintaining strong reasoning performance. To this end, we study the feasibility of training a model that reasons in Japanese. We develop a Japanese-reasoning variant of Qwen-3-Swallow-8B, which is a Japanese LLM continually pretrained from Qwen-3-8B, with GRPO and evaluate it across coding, math, and science benchmarks. The study shows that reasoning-language control is feasible by training a Japanese continually pretrained model with GRPO. However, its performance is at best on par with strong English-reasoning baselines on several benchmarks. We also evaluate the trained model on Japanese cultural benchmarks and observe that the model's performance is worse than the baseline models, suggesting that the reasoning in Japanese does not immediately improve performance on culturally relevant tasks for free.

---


### 105. [When Data Imbalance Helps: Robust Generalization Through Shortcut Saturation](https://arxiv.org/abs/2607.10116)

**<font color=#1a73e8>作者：</font>** Cheng-Ting Chou, Duc Binh Hoang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study robust generalization under spurious correlations: tasks where a shortcut feature is correlated with the true label in training but anti-correlated in an adversarial held-out split. Varying the spurious ratio $r$ (the fraction of training examples where shortcut = true label) and model capacity, we find a counterintuitive result: data imbalance promotes generalization in sufficiently capable models. On a synthetic task where the true label is sum parity of an integer sequence and the shortcut is the parity of the maximum-valued element, a 2-layer, 2-head transformer generalized (reached $100\%$ adversarial accuracy) in 0% of seeds at $r{=}0.50$ but 77% of seeds at $r{=}0.90$. The effect is absent in 1-layer models, where imbalance instead traps the model on the shortcut. Through mechanistic analysis -- gradient conflict dynamics, circuit evolution, and QK/OV circuit ablations -- we characterize a mechanistic pathway consistent with imbalance promoting generalization.

---


### 106. [WeaveEarth: Structured Evidence Construction and Reasoning for Training-Free UHR Remote Sensing Understanding](https://arxiv.org/abs/2607.10120)

**<font color=#1a73e8>作者：</font>** Xianzhi Ma, Shujun Wang, Xiaohan Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ultra-High-Resolution (UHR) remote sensing image understanding requires Vision-Language Models (VLMs) to capture both the global scene layout and sparse yet task-critical local details under limited computational budgets. Existing methods mainly follow two paradigms. One is passive perception, which relies on resolution expansion or token compression and may therefore discard fine-grained details. The other is active perception, which depends on multi-round zooming and search, but suffers from high latency, contextual fragmentation, and error accumulation. We argue that a more effective path toward UHR understanding lies not in accessing more, but in organizing better. To this end, we propose WeaveEarth, a training-free framework that reformulates UHR understanding as a problem of structured evidence construction and reasoning under global context constraints. Specifically, WeaveEarth first employs Global-Aware Evidence Construction to select a compact, low-redundancy, and spatially complementary Minimal Support Evidence Set. It then introduces Structured Evidence Reasoning, which weaves local evidence, spatial metadata, and relative topology into a unified reasoning interface, thereby enhancing the VLM's ability to perform global-local joint reasoning. Extensive experiments show that WeaveEarth consistently outperforms strong baselines and existing UHR methods across multiple UHR remote sensing benchmarks and multiple frozen VLM backbones. Code is available at this https URL.

---


### 107. [Energy-guided Recursive Model](https://arxiv.org/abs/2607.10128)

**<font color=#1a73e8>作者：</font>** Yifei Zhao, Ying Tang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recursive reasoning models address structured problems by repeatedly updating latent states of small neural networks. However, their test-time scaling lacks a principled inference mechanism: increasing depth or stochastic breadth generates more trajectories without a clear criterion for selection, and existing methods predominantly rely on additional q-heads or heuristic voting. Here, we develop the Energy-guided Recursive Model (ERM), which introduces an intrinsic selection principle based on explicit Hopfield energies. ERM leverages Hopfield-type memories of valid local or global structures to define the selector over candidate trajectories. The resulting energy seamlessly integrates with energy-based techniques such as parallel tempering to enhance sampling efficiency and ranking. With $D=64$ recurrent steps and $K=128$ candidates, ERM reaches optimal solutions on Sudoku ($98.97\%$), Pencil Puzzle Bench (PPBench, $88.04\%$) and Maze ($99.30\%$), improving upon recent Probabilistic Tiny Recursive Model and Equilibrium Reasoners. These results suggest that incorporating explicit energy functions into recursive reasoning offers a principled path toward more effective inference.

---


### 108. [SALT-GNN: Handling Dense Neighborhoods in Anti-Money Laundering Graphs via Statistics-Aware Attention](https://arxiv.org/abs/2607.10131)

**<font color=#1a73e8>作者：</font>** Lidia Losavio, Francesco Sovrano, Dario Fenoglio 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Money laundering threatens financial stability and exposes institutions to penalties, motivating automated detection. Because laundering schemes often emerge through relational patterns, graph neural networks (GNNs) are increasingly used for anti-money laundering (AML). Yet AML GNNs are typically evaluated with aggregate metrics such as overall F1 score, which hide an operational issue: high-activity recipient accounts concentrate many incoming transactions, making suspicious signals harder to isolate and costlier to investigate. We introduce a recipient-degree stratified evaluation that reports standard AML metrics across recipient-context density. Across three datasets (HI-Small, HI-Medium, and AMLSim-32k-5%), it reveals consistent degradation in dense recipient contexts, which we trace to three GNN characteristics: two known limitations that AML amplifies, i.e., (1) multiset non-discriminability and (2) cardinality blindness, and (3) an attention-specific effect: in dense neighborhoods, normalized attention attenuates weak but pattern-relevant multi-hop signals. Guided by this diagnosis, we propose SALT-GNN, a lightweight statistics-aware architecture that fuses degree-aware statistical aggregation with attention at each message-passing layer, so distributional and cardinality information shapes the node states used by subsequent attention steps. Ablations support fusion placement as a key factor in dense-context performance. On HI-Small and HI-Medium, SALT-GNN uses up to 77% fewer parameters than task-specific graph-transformer baselines while improving dense-context F1 score by 3-6 points; on AMLSim-32k-5%, it improves highest-degree F1 score by 16-20 points. The gains hold for both Transformer- and GAT-style attention, indicating that the benefit comes from where statistical and attentional evidence is fused rather than from a specific attention operator.

---


### 109. [FlowPainter: Inpainting Optical Flow via Confidence-Guided Completion](https://arxiv.org/abs/2607.10140)

**<font color=#1a73e8>作者：</font>** Yuang Meng, Chenyang Wu, Xianshun Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing optical flow methods broadly follow two paradigms: iterative optimization and diffusion-based estimation. Iterative methods, exemplified by RAFT, achieve high accuracy through recurrent refinement, but remain challenged by large displacements and complex motion. Diffusion-based methods introduce generative modeling and show promise in such ambiguous regions. However, existing diffusion models usually denoise the entire dense flow field from Gaussian noise, including simple regions where reliable motion can already be estimated by a lightweight network. This increases the denoising burden and may cause slow convergence and unstable training. To address this issue, we introduce FlowPainter, a diffusion-based optical flow framework that reformulates dense-flow generation as confidence-guided soft inpainting. FlowPainter employs a lightweight confidence-aware network to predict a rough flow and a pixel-wise confidence mask, distinguishing reliable simple regions from uncertain hard regions. The resulting simple-flow prior is used for confidence-based initialization and further injected into iterative denoising through confidence-gated residual guidance. With dynamically decaying guidance strength, FlowPainter stabilizes early denoising while preserving the flexibility of the diffusion model for late-stage detail refinement. Extensive experiments on public benchmarks, including Sintel, KITTI, and Spring, show that FlowPainter achieves strong accuracy under comparable training settings and converges more efficiently than existing diffusion-based optical flow methods, with notable gains on challenging benchmark splits. Our approach offers a practical way to integrate reliable discriminative priors with diffusion-based refinement for optical flow estimation. Our code is publicly available at this https URL.

---


### 110. [IdeaTrail: Full-Process Agent Trajectories for Scientific Ideation](https://arxiv.org/abs/2607.10144)

**<font color=#1a73e8>作者：</font>** Hengquan Guo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific research is a complex, multi-stage workflow rather than a single act of text generation. The ideation process typically emerges through literature search, paper reading, tool use, claim checking, cross-paper synthesis, brainstorming, rejection of weak directions, and iterative writing. Existing resources capture individual components of this process, but datasets that jointly record tool use, evidence acquisition, intermediate artifact evolution, and idea- or proposal-level endpoints remain limited. This report introduces \method, a multi-turn process-trajectory dataset for scientific ideation and proposal generation. Each instance records a research process from evidence gathering to either idea selection or proposal construction. Rather than freely fabricating trajectories, \method starts from human-selected high-quality research papers and proposal artifacts and uses a Generator--Advisor synthesis loop. The Generator produces the visible trajectory through actions, observations, and artifact edits, while the Advisor has access to the full generation context and checks grounding, causal order, naturalness, and leakage from hidden targets. This reverse-to-forward procedure produces multi-turn research data that remains aligned with real scientific artifacts while approximating the uncertainty, evidence use, and staged convergence of research practice. \method provides both a dataset and a general recipe for synthesizing process-supervision data for scientific research agents.

---


### 111. [REVA-PO: Stabilizing Reinforcement Learning for Chest X-ray Report Generation](https://arxiv.org/abs/2607.10147)

**<font color=#1a73e8>作者：</font>** Li Guo, Anas M. Tahir, Z. Jane Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated chest X-ray report generation has recently benefited from reinforcement learning (RL) and large language models. However, RL training often suffers from instability or limited exploration due to fixed Kullback-Leibler (KL) regularization and a static reference policy that accumulates KL pressure over time. We propose Response-Weighted and Validation-Anchored Policy Optimization (REVA-PO), a RL framework that stabilizes long-term training via Response-Weighted Regularization (RER) and Validation-Anchored Policy Reset (VAPR). RER dynamically adjusts per-response KL weights based on advantage and reference-policy entropy, relaxing constraints for high-quality responses while tightening them for low-quality ones. Complementarily, VAPR periodically synchronizes the reference and current policies to the best validation checkpoint, resetting accumulated regularization pressure to expand the viable exploration space. To ensure a robust starting point, we employ a three-stage pipeline consisting of warm-up training, classifier-guided supervised fine-tuning, and RL. Extensive evaluations on MIMIC-CXR and IU-Xray demonstrate that REVA-PO sets new state-of-the-art benchmarks in both linguistic quality and clinical accuracy. Notably, BLEU-4 improves by 5.1% on MIMIC-CXR and 3.6% on IU-Xray, while CheXpert F1 and RadGraph F1 scores increase by 4.5% and 12.8%, respectively, over prior leading methods. The code is publicly available at this https URL.

---


### 112. [EmoStyle: Affective Conditioning of Style-Specialist Experts for Emotional Image Generation](https://arxiv.org/abs/2607.10165)

**<font color=#1a73e8>作者：</font>** Dexiang Hong, Yijie Guo, Weidong Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Emotion-aware artistic image generation requires an image to match the input prompt, follow the specified artistic style, and convey the target emotion. In this challenge, the main difficulty is that the visual and affective attributes available in the training data are not explicitly provided at test time. Without these attributes, the generator has to decide not only what to depict, but also how the target emotion should be expressed through color, lighting, brushwork, composition, line, and layout. This creates a control gap between the available test prompt and the fine-grained conditions needed for emotion-aware artistic generation. To bridge this gap, we propose EmoStyle, a Z-Image-based framework that converts the input prompt into a structured generation state. An LLM reasoner first predicts affective cues (valence-arousal, dominant emotion, and therapeutic-effect labels) and an aspect-ratio decision. Instead of using these predictions only as additional prompt text, we encode the affective fields into an affective condition vector and inject it into the denoising blocks through AdaLN-style modulation. This allows the inferred control variables to directly guide the generation of intermediate features. Since emotional expression is also style-dependent, we further train a dedicated LoRA adapter for each artistic style bucket and select the corresponding expert during inference, enabling the same affective cues to be rendered with bucket-specific priors for color, texture, brushwork, and composition. Finally, a lightweight VLM-guided candidate selection step ranks the generated images based on prompt alignment, style consistency, emotional expression, and visual quality. In Track 1 of the AffectiveArt Challenge 2026, our USTC\_PI\_LAB\_TEAM submission achieved first place.

---


### 113. [RideGym: A Standardized Interface for Real-World Large-Scale Ride-Sharing System](https://arxiv.org/abs/2607.10173)

**<font color=#1a73e8>作者：</font>** Zijian Zhao, Yulong Hu, Sen Li  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Ride-sharing has become an essential component of modern urban transportation and has attracted significant attention across computer science, transportation, and management science. While the field spans a broad range of problems, such as driver relocation, dynamic pricing, and vehicle charging or fueling dispatch, the core challenge remains order assignment and trip bundling, which directly affect urban traffic efficiency and carbon emissions. Despite its importance, existing simulation platforms are typically tailored to specific operational studies or tightly coupled to a particular dispatch algorithm, and rarely expose a standardized, learning-friendly interface. As a result, most researchers still build customized environments from scratch, raising serious concerns about reproducibility and fair comparison, and incurring substantial redundant effort. To address this gap, we present RideGym, the first open-source, standardized Gym-style interface tailored to MARL-based order dispatch in real-world ride-sharing systems. By fully decoupling the environment from the dispatch algorithm, RideGym enables diverse learning-based and model-based methods to be developed and compared under identical, fully specified conditions. It supports efficient, large-scale city-level simulations on real road networks, and offers flexible configurations for vehicle attributes, order specifications, and automatic shortest-path routing. We validate RideGym by reproducing several baselines, and demonstrate its high efficiency, with a one-hour simulation involving thousands of vehicles and tens of thousands of orders completed within one minute across all methods. Moreover, we reveal that the choice of exploration noise can significantly affect both the performance and the relative ranking of MARL solutions, an aspect often overlooked in prior work.

---


### 114. [BiLoG-Net: A Bi-Context Location-Guided Network for Breast Mass Segmentation and Malignancy Classification in Mammography](https://arxiv.org/abs/2607.10188)

**<font color=#1a73e8>作者：</font>** Abu Fatema Mohammad Abdun Noor, Md Imam Ahasan, Md Samiul Ahasan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Breast cancer remains the most commonly diagnosed malignancy among women worldwide, yet accurate detection and characterization of breast masses in mammography remain challenging due to subtle intensity variations, heterogeneous tissue densities, and indistinct lesion boundaries that complicate radiological interpretation. To address these limitations, we propose BiLoG-Net, a deep learning framework that jointly performs breast mass segmentation and malignancy classification through bi-context location-aware feature modeling and segmentation-guided attention mechanisms. Our architecture integrates a novel encoder-decoder paradigm with Fire-based feature extraction, lightweight global and local feature enhancement modules, and adaptive location-aware gating to simultaneously capture long-range contextual dependencies and fine-grained boundary-sensitive details. Unlike conventional multi-stage pipelines, our tightly coupled multi-task design enables mutual reinforcement between pixel-level localization and image-level diagnosis, reducing error propagation while producing spatially grounded malignancy predictions. Evaluated on CBIS-DDSM and INBreast benchmarks, BiLoG-Net achieves state-of-the-art performance with Dice scores of 94.20% and 93.10%, classification accuracies of 95.20% and 93.60%, and AUC values of 97.10% and 96.00%, respectively, substantially outperforming existing CNN and transformer-based baselines. By combining precise boundary delineation with reliable malignancy assessment in a single end-to-end model, this work holds strong potential for clinical computer-aided detection systems, helping radiologists prioritize suspicious cases and improve screening efficiency in busy clinical settings.

---


### 115. [PhysMRV: Physical Memory Retrieval and Verification for Physics Plausibility Reasoning](https://arxiv.org/abs/2607.10190)

**<font color=#1a73e8>作者：</font>** Wenyuan Wang, Lianyu Hu, Hao Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Video-language models (VLMs) have achieved remarkable performance on video understanding and visual question answering, yet they remain unreliable in reasoning about physical plausibility, where understanding object interactions, causal dynamics, and fundamental physical principles is essential. This limitation is particularly evident on challenging physical reasoning benchmarks, revealing a persistent gap in physical commonsense reasoning. To address this challenge, we propose PhysMRV, a training-free physical memory and verification framework for physical plausibility reasoning. Unlike retrieval-augmented VLMs that retrieve semantically similar videos as additional context, PhysMRV transforms training videos into a Hierarchical Memory Bank of structured physical knowledge comprising three complementary levels: scene descriptions capturing visual context, physical-event graphs modeling object interactions and causal structure, and physics-rule summaries distilling reusable physical principles and cues. During inference, PhysMRV retrieves physically relevant memories and leverages their structured physical evidence to guide a frozen VLM in verifying physical plausibility, requiring neither fine-tuning nor parameter updates. We evaluate PhysMRV on three challenging physical reasoning benchmarks, ImplausiBench, IntPhys2, and GRASP Level 2, across multiple state-of-the-art VLMs. Experimental results demonstrate consistent improvements over direct prompting across diverse VLMs and evaluation benchmarks, showing that structured physical memories provide an effective and scalable means of enhancing physical plausibility reasoning without additional training.

---


### 116. [Instruction Set and Language for Hypergraphs](https://arxiv.org/abs/2607.10194)

**<font color=#1a73e8>作者：</font>** Mario Pascual-Gonzalez, Ezequiel Lopez-Rubio  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present IsalHG, a method for representing the structure of any finite, connected hypergraph of bounded hyperedge arity as a string over a compact instruction alphabet $\Sigma_{\mathrm{HG}}$. The encoding is executed by a small virtual machine comprising a sparse hypergraph, a circular doubly-linked list (CDLL) of node references, and $k$ traversal pointers, where $k$ bounds the hyperedge arity. Instructions either move a pointer through the CDLL or insert a hyperedge, optionally together with new nodes, into the hypergraph. Every string over $\Sigma_{\mathrm{HG}}$ decodes to a valid hypergraph; the alphabet is closed. A greedy \emph{HypergraphToString} (h2s) algorithm encodes any connected hypergraph into a string; a backtracking variant seeded at nodes of lexicographically maximal structural tuple produces a \emph{canonical string} $w^{*}$, which we conjecture to be a complete isomorphism invariant. Canonical-string equality then decides hypergraph isomorphism natively, without the standard reduction to the Levi incidence graph followed by a graph-isomorphism engine. We verify the round-trip property $s2h(h2s(H)) \cong H$ on 150 connected random uniform hypergraphs and on named combinatorial designs, and we benchmark the canonical algorithm against the three practically available exact baselines -- nauty, Traces, and bliss operating on the 2-coloured Levi graph -- across a $(n, c)$ grid with ten seeds per cell. All four methods agree on every one of 600 isomorphism verdicts, consistent with the completeness conjecture. On wall-clock time the Levi baselines dominate every tested cell by three to five orders of magnitude (geometric-mean ratio $311\times$ to $117{,}672\times$), which we report as measured. We contribute the representation framework, a conjecture of canonical completeness, and the first native-versus-Levi benchmark for hypergraph isomorphism.

---


### 117. [Generative Augmentation of Raman Spectra for Glioma Classification](https://arxiv.org/abs/2607.10196)

**<font color=#1a73e8>作者：</font>** Andrei Iuşan, Iulian Vasile, Daria Voiculescu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Access to sufficiently large biomedical datasets remains a major obstacle for machine learning in Raman spectroscopy-based diagnostics. In particular, for glioma analysis, datasets are typically small and heterogeneous, affected by acquisition-specific variability. This work investigates the utility of deep generative augmentation in such a small-cohort setting. We analyze glioma biopsy spectra acquired from 58 tumor samples and consider both binary IDH-status classification and 6-class methylation subtype classification problems. To address the limited size and imbalance of the dataset, we develop a conditional variational autoencoder ($\beta$-CVAE) capable of generating class-conditioned synthetic Raman spectra. The generated data are evaluated in Train-on-Synthetic, Test-on-Real (TS/TR) and Train-on-Synthetic+Real, Test-on-Real (TSR/TR) settings under a strict patient-isolated cross-validation protocol. Models trained exclusively on synthetic data underperform models trained on real spectra, indicating a substantial domain gap between synthetic and real distributions. However, augmenting the real training data with synthetic spectra consistently improves classification performance across multiple models. These findings indicate that, even with a limited number of independent patient samples, generative models can capture sufficient structure to provide useful regularization for downstream classifiers. We also investigate a reconstruction-based inference strategy, termed Classification by Reconstruction (CbR), in which class prediction is based on reconstruction error under different class conditions. Overall, the results support the use of deep generative augmentation as a practical strategy for improving machine learning robustness in Raman spectroscopy applications characterized by limited biomedical datasets.

---


### 118. [Equal Accuracy, Unequal Evidence: Search APIs as Decision Surfaces for Tool-Using Agents](https://arxiv.org/abs/2607.10198)

**<font color=#1a73e8>作者：</font>** Sriram Selvam, Anneswa Ghosh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Search APIs are the fundamental retrieval layer for many agents and are often their most frequently used tool. Traditional search APIs provide URLs, titles, and snippets that preview website contents. Because full-page retrieval is token-intensive, agent retrieval architectures increasingly use progressive disclosure: the agent first sees snippets and then chooses whether to fetch full pages. In such systems, search API performance is often evaluated primarily by answer accuracy. We argue that a commercial search API is better understood as a decision surface: the ranked snippets, URLs, and metadata that determine whether an agent answers immediately, searches again, or spends tokens opening pages. We test this claim with one frozen GPT-5.4 agent, two tools (search_web and fetch_page), and 100 questions from SEALQA-HARD, varying only the search provider (Brave, Tavily, Firecrawl). A Kimi-K2.6 oracle labels every content element visible to the agent (URL, title, snippet, and fetched page, when fetched), producing 6,869 valid per-URL judgments. We use an audited correct-answer label, semantic match, which preserves exact matches while accepting harmless formatting and naming variants. Under this measure, the providers remain close (25, 25, 26 / 100), but their evidence economies differ sharply: Brave offers gold-answer-rich snippets, Tavily concentrates gold-supporting URLs at rank 1, and Firecrawl is associated with broader exploration under this fixed agent policy. We also introduce a surface contradiction-to-gold URL ratio, which varies from 0.92 to 2.59. Provider choice is therefore a retrieval-budget and policy decision, not merely a recall decision.

---


### 119. [The Differential Neural Tangent Kernel and Its Positivity](https://arxiv.org/abs/2607.10200)

**<font color=#1a73e8>作者：</font>** Bangti Jin, Longjun Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Neural Tangent Kernel (NTK) is one powerful tool for analyzing the training dynamics of neural networks in the over-parameterized regime. Recently, the theoretical framework has been extended to physics-informed neural networks (PINNs) for solving linear PDEs, one highly popular class of neural PDE solvers. In the analysis, the positivity of the associated NTK plays a fundamental role. However, establishing the positivity of the NTK for PINNs is highly challenging, due to the presence of multiple differential operators. In this work, we propose a new theoretical framework, called Differential Neural Tangent Kernel (DNTK), for analyzing PINNs through the lens of the NTK, and establish the positivity of the infinite width DNTK for both shallow and deep neural networks for a wide class of activation functions, including RePU and smooth but non-polynomial activations, for all linear differential operators. These theoretical results lay the foundation for the analysis of gradient type algorithms for training PINNs.

---


### 120. [Two Confounds in Cross-Model Value Comparison: Response Determinism and the Access Harness](https://arxiv.org/abs/2607.10202)

**<font color=#1a73e8>作者：</font>** Hong-In Won, Jinseok Jang, Hyoseop Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cross-model comparisons read divergence in value dispositions as evidence that language models hold individuated values. Under single-draw measurement this conflates two quantities: a difference in central tendency (a genuine value difference) and a difference in response determinism (how sharply a model commits to a forced choice). We introduce a separation protocol -- no-rule value dilemmas with counterbalanced, repeated forced-choice measurement and a determinism index -- and a determinism-corrected decomposition that splits an apparent cross-model distance into a direction-flip component (genuine disagreement) and a same-side-more-extreme component we label determinism. Across nine models, determinism varies substantially (0.66-0.95 among engaging models); whether it is a per-model trait or tracks provider and scale is a question our method makes measurable but our sample leaves open. Correcting for determinism shrinks apparent individuation, while a few cross-family disagreements survive a strict test. We then isolate a second confound: the access harness serving each model. Re-collecting the same models through raw provider APIs, we find the deployment client shifts a model's value profile substantially and client-specifically: one subscription CLI moves a profile by 0.31, flips four of eighteen items, and inflates the flagship's apparent softness (0.34 via CLI vs 0.66 via raw API), whereas another provider's client is clean, confounding provider family with access client. The harness is a value-shaping layer: a base model that refuses one-in-ten forced choices is made compliant by an agent system prompt, established causally in a white-box control. An audit ranking models by single-draw value distance thus ranks a determinism-inflated quantity, confounded further by the client used. We contribute the decomposition and identify the deployment harness as a distinct value confound.

---


### 121. [Exploratory Analysis of Deep Learning Models for Forecasting Meteorological Parameters in the Agricultural Sector](https://arxiv.org/abs/2607.10208)

**<font color=#1a73e8>作者：</font>** Piotr Sikora, Sotirios Kontogiannis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate meteorological forecasting is essential for agricultural planning, irrigation management, and environmental decision support. This study conducts a comparative evaluation of recurrent and hybrid deep learning architectures for multivariate forecasting of reference evapotranspiration ($ET_0$), vapour pressure deficit (VPD), wind speed, and the sine and cosine components of wind direction. The analysis utilizes 134,376 hourly observations from Ioannina, Greece, spanning January 2011 to April 2026, sourced from ERA5 via the OpenMeteo Historical Weather API. Single and multi-layer GRU and LSTM networks are compared with hybrid 1D-CNN-GRU and 1D-CNN-LSTM models for two forecasting tasks: a 24-hour next-day forecast and a 168-hour week-ahead forecast. Performance is evaluated using normalized root mean squared error, the coefficient of determination, and a composite Weighted Quotient Score (WQS). The most effective purely recurrent models are a 64-unit LSTM for the 24-hour horizon, with a WQS of 0.816755, and a 1024-unit GRU for the 168-hour horizon, with a WQS of 0.779465. The hybrid CNN-GRU models achieved the highest overall scores of 0.827535 and 0.782863 for the 24-hour and 168-hour horizons, but with additionally more number of units respectively to LSTM models, while the CNN-LSTM models yield nearly identical results with substantially fewer parameters. Compared to the corresponding recurrent baselines, the hybrid models improve WQS by 1.22--1.63\% at 24 hours and by 0.44--0.45\% at 168 hours, indicating that convolutional feature extraction is more beneficial for short-term forecasting.

---


### 122. [Toward Stronger Code Watermarking: A Grammar-Driven Approach to Optimizing the Trade-off Between Quality and Detectability](https://arxiv.org/abs/2607.10210)

**<font color=#1a73e8>作者：</font>** Licheng Yu, Aiwei Liu, Songze Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With the rapid development of Large Language Models (LLMs), text watermarking has emerged as a crucial technique for identifying machine-generated content. However, directly applying existing logits-based watermarking methods to code generation remains challenging, since the low-entropy nature of code exacerbates the trade-off between code quality and watermark detectability. In this paper, we propose a novel code watermarking approach called Grammar-Driven Watermark (GDW) for LLMs. GDW preserves syntactic validity through a grammar-guided three-level masking mechanism and injects watermark signals via structural role-aware modulation, assigning a stronger bias to content-bearing tokens while applying a more conservative bias to syntax-critical tokens. Aligning with the generation process, we further design a role-aware weighted detection statistic to improve detectability. Experiments across multiple programming languages, models, and decoding strategies show that GDW establishes a stronger quality-detectability trade-off frontier than existing methods, while maintaining robustness against variable-renaming attacks.

---


### 123. [KGCQual: An Interpretable Framework for Evaluating the Knowledge Graph Construction Quality from Text](https://arxiv.org/abs/2607.10212)

**<font color=#1a73e8>作者：</font>** Nipun Misra, Vikranth Udandarao, Aanchal Gupta 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge Graphs (KGs) are increasingly constructed through automated extraction pipelines; however, such systems often introduce spurious or incomplete triples, which degrade downstream performance. Existing evaluation practices rely heavily on task-specific metrics or small-scale manual verification, offering limited insight into the structural and semantic fidelity of extracted graphs. We propose a novel, interpretable metric for intrinsic KG quality assessment that measures how closely an automatically extracted graph approximates an "ideal" graph capturing the key noun phrases, predicate relations, and basic linguistic phenomena such as negation expressed in the source text. Our framework integrates two complementary components: (1) an entity-level assessment that evaluates completeness, resolution quality, and connectivity, and (2) a relation-level assessment that judges predicate preservation and multiplicity using lexical similarity, dependency-parse alignment, and light-weight negation handling to ensure semantic faithfulness. We evaluate our metric across multiple state-of-the-art triple extraction systems and datasets, including WebNLG, TinyButMighty, and BenchIE, demonstrating that it reliably identifies omissions, redundancy, and structural deviations that existing metrics overlook. Our work offers a scalable, model-agnostic, and interpretable framework for comparing automated KG construction methods and provides a foundation for standardised evaluation. We further validate the metric through an ablation study isolating noun and verb components, and a downstream evaluation showing that KGCQual scores correlate significantly with link prediction performance on the same extracted KGs. The code repository is available at this https URL.

---


### 124. [ScratNet: A Swin-Based Multi-Scale Dilated Network with Precision Refinement for Semiconductor Scratch Segmentation](https://arxiv.org/abs/2607.10214)

**<font color=#1a73e8>作者：</font>** Sachin Ranjan, Hoon Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surface scratch defects in semiconductor manufacturing pose significant challenges due to their irregular shapes, low contrast, and varying scales. Traditional inspection methods often struggle to detect such defects reliably, especially in complex imaging scenarios. While deep learning approaches based on Convolutional Neural Networks (CNNs) have improved accuracy, they often fail to capture fine-grained edge details. To address these limitations, we propose ScratNet, a novel end-to-end scratch segmentation framework that integrates a modified Swin Transformer backbone with a tailored decoder. The decoder incorporates a Multi-Scale Dilated Aggregation (MDA) module to capture both local and global context, a Stem Integration Module (SIM) to restore spatial detail, and a Precision Refinement (PR) branch that enhances boundary sharpness using anisotropic convolutions. Through this stage-adaptive feature aggregation and boundary-aware refinement, ScratNet achieves superior accuracy on thin and irregular defects. Extensive experiments demonstrate that ScratNet consistently outperforms existing methods, providing a scalable and robust solution for automated scratch inspection in high-precision manufacturing.

---


### 125. [When Are Sparse Feature Interventions Actually Localized? Matched Evaluation for SAE-Based Safety Control](https://arxiv.org/abs/2607.10226)

**<font color=#1a73e8>作者：</font>** Daming Luo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We evaluate when sparse autoencoder (SAE) features act as localized control handles for safety-relevant behavior. This question is difficult because apparent success can arise from weak interventions, mismatched baselines, model robustness, or degenerate outputs that automated safety judges mark as unsafe without representing meaningful harmful compliance. We introduce a matched coherence-gated evaluation protocol for runtime safety interventions: methods are compared at matched target-effect points, and the primary target metric counts harmful compliance only when an output is both judge-unsafe and coherent. Applying this protocol to three prompt splits on Gemma-2-9B-it with a Gemma Scope layer-20 residual SAE, we find that SAE feature ablation has a narrow useful regime. SAE top800 reaches a low-to-mid target effect with lower total perturbation and competitive utility, but SAE top1600 loses utility relative to a matched dense refusal-direction baseline, and SAE top3200 primarily induces coherence collapse. Human audit confirms that coherence gating removes unsafe-only artifacts, and feature diagnostics show that the useful regime is driven by a stable head of refusal-aligned features whose activation separation decays rapidly with rank. These results argue that SAE-based safety interventions should be evaluated as regime-dependent control mechanisms rather than assumed to be uniformly localized.

---


### 126. [PhenoEmbed: Self-Supervised Multispectral UAV Time-Series Embeddings for Individual Tree Crown Phenology](https://arxiv.org/abs/2607.10231)

**<font color=#1a73e8>作者：</font>** Taimur Khan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tree crowns are a challenging target for resilient AI because they are not static objects: their spectral response, internal texture, translucency, and apparent boundaries change substantially across the growing season. We develop PhenoEmbed, a self-supervised crown-centric temporal embedding model trained with contrastive and masked reconstruction objectives on HeideBench, an 18-date UAV multispectral time-series benchmark for forest crown phenology in D{ö}lauer Heide. The model treats seasonal crown dynamics as phenological appearance change driven by leaf emergence, canopy closure, senescence, and leaf-off conditions. Segmented tree crown polygons are retained as object anchors to extract aligned crown-centered crops through time, allowing one 256-dimensional vector summarizing seasonal crown appearance to be learned per tree. On 5,885 crop-safe crowns, the exported embeddings show structured low-dimensional organization, with the first two principal components explaining 25.1\% of variance and nearest-neighbor retrieval producing a median top-1 cosine similarity of 0.946. Compared with handcrafted temporal features and a learned mean-pooling baseline, PhenoEmbed yields substantially more compact nearest-neighbor structure, while ablations show that the contrastive loss, masked reconstruction loss, and explicit seasonal time features each affect the structure of the learned embedding space. These results support PhenoEmbed as a reusable forest crown representation learner and motivate future downstream tests of whether such features improve tree-level models under seasonal change.

---


### 127. [CoSAG: Compact Semantic Anchor Gaussians via Training-Free Rate-Distortion Coding](https://arxiv.org/abs/2607.10237)

**<font color=#1a73e8>作者：</font>** Yuang Jia, Jinlong Wang, Junhong Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary 3D scene understanding is commonly achieved by embedding 2D vision-language features such as CLIP into a 3D Gaussian Splatting scene, turning it into a text-queryable semantic field. However, attaching a high-dimensional feature to each of millions of Gaussians inflates a single scene to gigabytes, which makes storage and deployment the real bottleneck of these fields. Existing compact methods each learn and ship a per-scene codec, an autoencoder, a quantized codebook, or a distilled feature field, entangling field construction with field storage and never compressing the per-Gaussian assignment that holds the bulk of the cost. We argue that construction and storage should be decoupled, and that storage is a rate-distortion problem over the per-Gaussian binding to a small anchor table, a structure no prior open-vocabulary method compresses. We present CoSAG, which constructs the field without any per-scene training through a closed-form transmittance-weighted lift, spatially grounded semantic anchors, and multi-view denoising, and stores it with a spatially predictive entropy coder that ships no decoder. Because the anchors are spatially grounded, the binding is predictable and therefore highly compressible. The transmittance-weighted lift and multi-view denoising yield a clean, view-consistent assignment, so the entropy coder spends almost no rate on correcting noise and instead codes only the residual against its spatial prediction. CoSAG reaches sub-megabyte storage while matching or exceeding the state of the art across the 2D-rendered, 3D-selection, and dense-LSeg protocols, reducing field size by 37 to 76x relative to LangSplatV2 at higher accuracy.

---


### 128. [Benchmarking Dynamic Affective Reasoning: A Viewer-Centric Video Emotion Dataset](https://arxiv.org/abs/2607.10238)

**<font color=#1a73e8>作者：</font>** Zhiyan Zhang, Peipei Song, Jinpeng Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video emotion analysis is typically framed as a static classification problem, treating each clip as an independent labeled unit. However, such a formulation overlooks a key psychological fact: emotions change as a result of cumulative reactions to consecutive causal events. To bridge this gap, we introduce Dynamic Affective Reasoning, the first large-scale benchmark for viewer-centric affect transitions and causal reasoning over consecutive video events. DAR contains 15,087 videos and 36,908 event-aligned affective segments annotated with 27 emotion categories. Unlike existing video-based emotion datasets, DAR presents a new viewer-centric perspective on fine-grained emotional expressions and transitions, and provides dense, temporally grounded, and causally explicit reasoning chains. Based on DAR, we formally define three challenging tasks: affective segmentation, fine-grained emotion classification, and affective reasoning. Complementing this benchmark, we propose DAR-R1, a two-stage framework that combines supervised fine-tuning with Group Relative Policy Optimization. Experiments across 10+ MLLMs show that DAR-R1 sets a new state-of-the-art for dynamic affective reasoning, in terms of both emotional localization and affective reasoning. Project page: this https URL.

---


### 129. [DSSMs: State Space Models with Explicit Memory via Delay Differential Equations](https://arxiv.org/abs/2607.10244)

**<font color=#1a73e8>作者：</font>** Yixiao Qian, Song Chen, Jiaxu Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> State Space Models (SSMs) have emerged as a powerful paradigm for efficient long-sequence modeling, offering parallel training and fast linear-time recurrent inference. However, like other recurrent architectures, SSMs must compress an unbounded history into a fixed-size state, which limits context retention and makes precise retrieval over long-range context inherently difficult. To overcome this limitation, we propose Delay State Space Models (DSSMs), a delay differential equation (DDE)-inspired extension of diagonal SSMs that augments discrete SSM recurrences with explicit delayed-state feedback. Making explicit delayed feedback practical requires new stability parameterization, history management, and FFT-training tools. We address these challenges with a practical discretization and parameterization grounded in a simple delay-independent stability condition. To bypass direct time-domain kernel construction, we derive the DSSM transfer function and compute kernels in the frequency domain, using a kernel contour shift to suppress aliasing and recover accurate FFT training. Empirically, DSSMs substantially improve targeted delayed-retrieval tasks while outperforming S4D on most standard sequence metrics and remaining close on the others.

---


### 130. [Which Languages Transfer Best to Warlpiri? A Similarity-Based Study for Low-Resource ASR](https://arxiv.org/abs/2607.10256)

**<font color=#1a73e8>作者：</font>** Pravina Mylvaganam, Eliathamby Ambikairajah, Ting Dang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper investigates how language similarity can improve cross-lingual transfer for automatic speech recognition (ASR) in extremely low-resource settings. Warlpiri, an Australian Aboriginal language, has very limited transcribed speech data, making transfer learning essential. We propose a framework combining acoustic similarity from pre-trained speech models with linguistic similarity based on typology, phoneme inventories, grammatical, and syntactic features to rank high-resource source languages and evaluate their effectiveness for ASR transfer to Warlpiri. Experiments with Whisper show that acoustically and typologically similar languages outperform monolingual and multilingual baselines. Assamese and Hindi achieve substantial reductions in word and character error rates. Correlation analysis further indicates that acoustic similarity is the strongest predictor of fine-tuning performance, while phoneme inventory and typological similarity better explain zero-shot transfer.

---


### 131. [Data-Driven Telecom Marketing Optimization: A Machine Learning-Based Churn Prediction and Customer Segmentation Framework](https://arxiv.org/abs/2607.10260)

**<font color=#1a73e8>作者：</font>** Nada Ali, Lina Ahmed, Tahani Abdalla Attia Gasmalla  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Customer churn is a major challenge for telecommunication companies, directly eroding revenue and long term customer relationships. Traditional retention programs rely on generic, not personalized incentives and lack the precision to identify high risk customers before they leave. This paper presents a data driven marketing optimization framework integrating machine learning based churn prediction, customer segmentation combining churn risk with customer value, and tailored, segment specific marketing and Return on Investment ROI strategies. Using the IBM Telco Customer Churn dataset with 7043 customers and 21 features, three gradient boosting ensembles, XGBoost, LightGBM, and CatBoost, were trained and tuned via randomized search with stratified 5 fold cross validation, class weighting, and F1 score driven decision threshold optimization to counter a class imbalance of 73.4% versus 26.6%. CatBoost was selected as the deployment model, achieving 77.68% accuracy, an F1 score of 0.6366, a PR AUC of 0.6553, and a ROC AUC of 0.8403 on the held out test set. Customers were partitioned with K Means clustering, validated via the Elbow method and visualized with Principal Component Analysis, into High, Medium, and Low Value segments, cross tabulated against churn risk labels to define four actionable clusters. Segment specific retention, upsell, and engagement strategies were designed for each cluster, and a theoretical ROI and CLV framework quantifies the financial impact of the proposed interventions. The pipeline was operationalized in an interactive Streamlit web application allowing marketing teams to upload data, filter by segment, visualize churn drivers via SHAP, and download automated segment reports. Results confirm that combining predictive churn modeling with value aware segmentation yields more actionable and profitable marketing decisions than churn prediction alone.

---


### 132. [Sharper Analysis of Single-Loop Methods for Bilevel Optimization](https://arxiv.org/abs/2607.10263)

**<font color=#1a73e8>作者：</font>** Yubo Zhou, Jun Shu, Luo Luo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bilevel optimization underpins many machine learning applications, including hyperparameter optimization, meta-learning, neural architecture search, and reinforcement learning. While hypergradient-based methods have advanced significantly, a gap persists between theoretical guarantees and practical single-loop implementations required for efficiency. We bridge this gap by establishing sharper convergence results for single-loop approximate implicit differentiation (AID) and iterative differentiation (ITD) methods, leveraging our proposed analytical framework, decoupled norm analysis (DNA). For AID, we improve the convergence rate from $\mathcal{O}(\kappa^6/K)$ to $\mathcal{O}(\kappa^5/K)$, where $\kappa$ is the condition number of the inner-level problem. For ITD, we prove that the asymptotic error is $\mathcal{O}(\kappa^2)$, exactly matching the known lower bound and improving upon the previous $\mathcal{O}(\kappa^3)$ guarantee. Numerical experiments on synthetic and real tasks corroborate our theoretical findings.

---


### 133. [Language Re-generation: An investigation into information locality effects on reconstruction](https://arxiv.org/abs/2607.10268)

**<font color=#1a73e8>作者：</font>** Amirhossein Mohammadi, Laurence E. Frank, Albert Gatt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Information locality, the tendency for syntactically related words to appear close together, shapes both human language processing and language model learning. While prior work has examined whether language models can acquire impossible languages, it remains unclear whether they can recover natural language from such input and what this reveals about their inductive biases. We address this by complementing learnability-based approaches with a reconstruction framework: fine-tuning GPT-2 models pre-trained on impossible languages to reconstruct natural English from three perturbation types. Our findings show that the recovered structures exhibit shorter dependency lengths than the original text, mirroring the locality preference observed in unconstrained language model generation and providing a quantitative signature of an architectural bias that learnability experiments alone do not reveal. Recovery difficulty increases with the degree of locality disruption. Structural recovery (dependency Triple F1) dissociates from surface recovery (Exact Match), while fluency dissociates from faithful reconstruction under global shuffling. Sentence length further modulates performance: longer sentences facilitate recovery when local structure is preserved but lead to complete collapse under global shuffling. Finally, recovery difficulty tracks learnability difficulty across perturbation types, suggesting that information locality is the shared constraint governing both.

---


### 134. [Geometry-aware Gaussian Prior and Axial Attention for Cervical Cytology Image Classification](https://arxiv.org/abs/2607.10278)

**<font color=#1a73e8>作者：</font>** Yating Li, Cheng Ye, Nenan Lyu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate cervical cytology image classification is a key component of automated cervical cancer screening, where reliable recognition of normal, precancerous, and cancer-associated cellular patterns from Pap smear images can improve screening efficiency and diagnostic consistency. However, this task remains challenging because cervical cells exhibit complex morphology, subtle intra-class variations, and strong inter-class similarities. Existing convolution-based models capture local texture well but have limited ability to model long-range relationships, whereas attention-based models provide broader context but often lack explicit structural guidance. To address these limitations, we propose a geometry-aware classification framework for cervical cancer screening-oriented cytology image analysis, incorporating semantic abstraction and structural priors learned from pre-trained vision-language features. The method uses Gaussian expert modules to generate axis-wise priors from global semantic information, capturing structural regularities such as nuclear alignment and cellular spatial organization. These priors are embedded into an axial self-attention module to modulate similarity computation along horizontal and vertical directions, improving long-range dependency modeling and structure-sensitive feature interaction. Experiments on the Mendeley liquid-based cytology and SIPaKMeD datasets show that the proposed method achieves 99.48% accuracy on the former and 96.08% on the latter, with balanced gains in recall, precision, and overall classification performance. Visual analysis further shows that the learned priors highlight diagnostically relevant cellular regions, demonstrating the potential of the proposed framework as a screening-oriented decision-support tool for cervical cytology.

---


### 135. [Interpreting learning dynamics of autoencoders: Transient scaling and emerging concepts of the Ising model](https://arxiv.org/abs/2607.10285)

**<font color=#1a73e8>作者：</font>** Max Weinmann, Miriam Klopotek  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study how unsupervised autoencoders trained on microscopic spin configurations from the Ising model learn macroscopic, theory-relevant variables underlying the data-generating process. Without embedding domain knowledge, we mimic a typical discovery setting: We quantify learning across multiple spatial (coarse-graining) scales and reveal two distinct dynamical regimes controlled by main hyperparameters (model depth, width, and learning rate) -- a magnetization-dominated regime and an energy-dominated regime characterized by trade-offs in their representation quality. The first regime is a transitory state exhibiting dynamical scaling and fluctuations that follow an ordering-to-scale; the second gradually shifts resolution towards smaller scales relevant for the energy representation. Deep models trained at moderate and fast rates become arrested before reaching these regimes. With a novel analysis of recursive-dynamic trajectories, we demonstrate that prediction errors induce flow fields that produce a common trajectory topology across all representation spaces. A dynamical viewpoint of learning is established in which intrinsic properties expose the effects of forced changes in representation during training. We utilize the intuition that learning operates as a process driven far from equilibrium by fluctuations from the training data and optimizer to provide an interpretive basis grounded in both the physical world and the machine models that represent it.

---


### 136. [Structured Evidence Selection for Weakly Supervised Video Anomaly Detection](https://arxiv.org/abs/2607.10298)

**<font color=#1a73e8>作者：</font>** Chenglizhao Chen, Tianxiang Nan, Wen Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Weakly supervised video anomaly detection relies solely on video-level labels for training, making it difficult to accurately localize anomalous events in complex scenes. In real-world videos, anomalous behaviors exhibit large variations in appearance and temporal duration, while scene appearance and action dynamics are often tightly entangled. Consequently, existing models tend to rely on scene-related statistical cues rather than true behavioral deviations, resulting in unstable detection performance. To address this challenge, we propose a Structured Evidence Selection framework (SESAD) that reformulates anomaly detection as a structured reasoning process over clip-level visual evidence. Instead of directly mapping aggregated features to anomaly scores, SESAD reorganizes clip representations into semantically structured candidate evidence and performs context-conditioned selection under scene and action constraints. This mechanism adaptively emphasizes anomaly-relevant semantics while suppressing scene interference, thereby alleviating semantic entanglement under weak supervision. Furthermore, we introduce a lightweight geometric discrimination module that constructs a dual-prototype structure in the embedding space, enabling anomaly decisions through relative geometric relations. Extensive experiments on UBnormal, ShanghaiTech, and UCF-Crime show that SESAD achieves 67.92, 97.99, and 88.46 AUC, respectively, while maintaining high computational efficiency and overall consistently stable anomaly discrimination.

---


### 137. [ChartSync: A Benchmark for Visuo-Logical Cascading Chart Editing](https://arxiv.org/abs/2607.10301)

**<font color=#1a73e8>作者：</font>** Jiakang Yu, Yixuan Chai, Tianci Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative image editing models struggle with structured statistical charts when data modifications require geometric synchronization. We formalize this task as Visuo-Logical Cascading Editing (VLCE). However, existing methods remain confined to localized text substitutions and struggle with dependency-aware cascading updates. To systematically evaluate this capability, we introduce ChartSync, an expert-validated benchmark constructed via a programmatic rendering pipeline that guarantees deterministic visuo-logical coupling for the ground truth. ChartSync comprises 870 triplets across 9 chart categories and 4 task types, including 235 geometry-coupled VLCE instances that specifically test cascading text-to-geometry synchronization. We further evaluate these instances via a two-tier framework combining objective visual metrics with a vision-language model judge paradigm to assess low-level fidelity alongside multimodal comprehension and reasoning. Evaluating 14 image editing models and one code-mediated pipeline reveals a nuanced capability gap: most open-source models suffer severe drops in geometric synchronization, while only two frontier proprietary models show emerging VLCE capability, with their residual errors mainly involving semantic isolation and background corruption. Our detailed error analysis deconstructs these failure paradigms to identify core meta-abilities for guiding future multimodal architectures. The ChartSync dataset and code are publicly released at this https URL.

---


### 138. [Generalize LMMs to Versatile Visual Modalities via Fabricated Modality Synthesis](https://arxiv.org/abs/2607.10308)

**<font color=#1a73e8>作者：</font>** Shihao Yuan, Yuanze Li, Ruyi Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the advancements of Large Multimodal Models (LMMs) in RGB vision, their ability to generalize to unseen visual modalities remains a largely unexplored challenge. We argue that different visual modalities are merely distinct samplings of the same physical world. Therefore, effective generalization requires models to possess both modality-agnostic perception of scene semantics and the adaptability to modality-specific characteristics. To achieve this, we propose a training framework, VVM-Tuning, to equip LMMs with these capabilities through modality synthesis and modality contexts. Specifically, we synthesize diverse appearance-varied images from RGB scenes, training the model to disentangle invariant semantics from varying visual appearances, and align these appearances with language for visual concepts decoupled from modalities. We then introduce modality contexts in the prompt and use instruction tuning to assist the model in mapping these appearance variations back to modality-related attributes, enabling zero-shot adaptation to unseen modalities during inference. To facilitate research in this direction, we introduce VVM-Bench, a comprehensive benchmark featuring 6 real and synthetic modalities to evaluate semantic perception and modality understanding. Experiments demonstrate that, via our training on synthetic modalities, 5 tested models exhibit consistent improvements on both real-world and novel synthetic modalities without in-modality training. Source code and data will be publicly available at this https URL.

---


### 139. [Measure the Sim-to-Real Gap: Designing an Affordable Real-World Benchmark Platform for Reinforcement Learning in AIoT Systems](https://arxiv.org/abs/2607.10309)

**<font color=#1a73e8>作者：</font>** Rongping Zhou, Omid Tavallaie, Shuaijun Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) is commonly employed to enhance the performance of autonomous systems, including the Autonomous Internet of Things (AIoT). However, the trial-and-error nature of RL, when conducted in real-world environments, is costly and hazardous in some scenarios. Consequently, the majority of RL research is conducted in simulation. This reliance introduces challenges related to the Sim-to-Real transferability. Evaluating the Sim-to-Real algorithmic robustness and the Sim-to-Real gap is a critical prerequisite for research aimed at improving RL performance in the real world. Therefore, industries such as robotics have developed concurrent simulation and physical platforms to facilitate this research. However, a universal Sim-to-Real benchmark platform for AIoT does not currently exist. To address these concerns, we developed a real-world AIoT platform for studying RL in AIoT. On this platform, an agent deployed on an edge device plays video games on a separate host computer via a hardware-emulated keyboard, guided by vision input. This platform uses commercially available components costing less than USD 400, together with two computers. Because the system's objective is game score maximization, it inherently mitigates safety risks associated with real-world RL deployments. Experimental results show the simulation-trained agent suffers a 1160% performance degradation relative to the human-level performance after real-world deployment, indicating a significant Sim-to-Real gap. Direct real-world training using the deep Q-network (DQN) algorithm achieves approximately 38% of human-level performance after 10 million training steps, demonstrating the feasibility of RL under real-world conditions. These results suggest that the proposed Sim-to-Real benchmark platform provides a substantial foundation for qualitative and quantitative evaluations of RL in real-world AIoT systems.

---


### 140. [Polarization Detection: A Hybrid Approach with AfroXLMR-Social and DeBERTa for Low- and High-Resource Settings](https://arxiv.org/abs/2607.10312)

**<font color=#1a73e8>作者：</font>** Muhammad Abdullahi Said  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid proliferation of online polarization threatens social cohesion, necessitating robust automated detection systems that operate effectively across diverse linguistic contexts. This paper presents our system description for the POLAR Shared Task 2026, focusing on the detection and characterization of polarized discourse in English and Hausa. We propose a hybrid modeling strategy: for English binary detection, we leverage the monolingual strength of \textbf{DeBERTa}, while for Hausa and all fine-grained subtasks (Types and Manifestations), we utilize \textbf{AfroXLMR-Social}. This domain-adapted multilingual model proved critical for capturing the nuances of polarization in social media text. To further address computational constraints and data scarcity, we implement Low-Rank Adaptation (LoRA) and textual data augmentation via \texttt{nlpaug}. We report competitive results across all three subtasks, demonstrating that model selection tailored to specific subtask requirements yields the best balance of performance.

---


### 141. [Understanding Implicit Trust Errors in Core Carrier Networks through Multi-Agent Flaw Discovery and Analysis](https://arxiv.org/abs/2607.10315)

**<font color=#1a73e8>作者：</font>** Ziyu Lin, Ziting Wang, Xinfeng Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cellular core networks (CNs) are critical infrastructure, yet their internal security model has historically relied on physical isolation: interfaces between core components often operate within an assumed trust zone. As CNs transition to cloud-native deployments, this assumption weakens, expanding the attack surface and enabling external adversaries to reach previously internal interfaces. From a root-cause analysis of security flaws reported in GitHub issues for opensource CN implementations, we found a recurring pattern of blind trust among CN components. Components may omit syntactic validation, fail to enforce semantic invariants, or allocate resources without checking availability. Once internal interfaces become reachable, these weaknesses can lead to severe impacts such as denial of service and session hijacking. We call these vulnerabilities implicit trust errors (iTrue). To detect iTrues and understand their security impacts, we designed iFinder, an LLM-driven multi-agent system that summarizes known flaws, distills them into detection patterns, and applies them to discover new iTrues in CN implementations. To suppress hallucinations produced by large language models (LLMs), we built an innovative strategy that crosschecks both 3GPP specifications and CN code to capture existing protection missed by the agents. Further, we developed a technique that uses LLMs to generate proof-of-concept (PoC) exploits for potential iTrues and iteratively refine the PoCs by automatically executing them against CN implementations and analyzing results. Running iFinder on seven prominent open-source CN implementations, we discovered 84 previously unknown vulnerabilities. Among them, 83 have already been confirmed and 81 have been assigned CVEs. Importantly, a session-hijacking flaw has been confirmed on real-world commercial 5G core networks.

---


### 142. [Neutralizing Structural Inequality in the Nigerian FinTech Sector](https://arxiv.org/abs/2607.10317)

**<font color=#1a73e8>作者：</font>** Muhammad Abdullahi Said  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Algorithmic decision systems in financial services often rely on data proxies that inadvertently encode structural inequalities. This paper introduces a hierarchical human-AI triage model for Point of Sale fraud detection in the Nigerian FinTech sector. Adopting a We Are All Equal worldview, we address the challenge of discrimination laundering, wherein the system misinterprets infrastructure related aleatoric noise such as rural network timeouts as fraudulent intent. We implement a three-tier routing policy utilizing a calibrated ensemble model as a primary filter. The policy routes transactions characterized by epistemic uncertainty such as cold start new accounts to specialist analysts while reserving high stakes cases for a senior supervisor. To manage finite human capacity, we utilize a dynamic shadow price to ration human attention and implement a random audit mechanism to prevent human skill atrophy. Our experimental results demonstrate a statistically significant 1.88\% complementarity gap and a 24.79\% percentage point gain in fraud recall over an autonomous baseline. Crucially, the model reduces the regional performance gap from 19.43 to 2.88 percentage points, neutralizing structural bias. Hierarchical collaboration provides a robust mechanism for substantive equality of opportunity, ensuring that rural accounts are not excluded from the digital economy due to environmental brute luck.

---


### 143. [Intervenability as a Design Requirement for Autonomy and Oversight within Human-Centered AI](https://arxiv.org/abs/2607.10322)

**<font color=#1a73e8>作者：</font>** Thomas Herrmann  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Based on the literature and several practical examples of possible AI applica-tions, we outline the concept of intervenability. This new phenomenon is not covered by emergency shutdowns, workarounds, or the reconfiguration of automated systems. Intervenability instantiates the principles of control-lability, autonomy, oversight, and keeping humans in the loop in the context of AI. We provide a taxonomy that encompasses a range of possibilities for intervening activities and differentiates them regarding the mental effort of the users. This taxonomy extends the scope of interventions from real-time control of automated processes to AI-based discrete case-related decision-making. This is in accordance with human-centered AI, which seeks to combine human strengths with the usage of AI. We demonstrate how inter-venability can potentially contribute to the ongoing development of human capabilities on the one hand and to further technical improvement by recon-figuration of AI on the other. Exploring and collaboratively reflecting on the effects of interventions as an integral part of organizational practices is key to enabling this continuous improvement on both sides. Intervenability also provides further momentum for the design of an AI that can help realize in-terventions on its own and advance a smooth transition from intervention to reconfiguration of the AI.

---


### 144. [Comparing Socio-technical Design Principles with Guidelines for Human-centered AI](https://arxiv.org/abs/2607.10331)

**<font color=#1a73e8>作者：</font>** Thomas Herrmann  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human-centered AI (HCAI) refers to guidelines or principles that aim on ethi-cally oriented design of systems. We compare HCAI- guidelines with princi-ples of socio-technical systems that emerged in the context of conventional in-formation technology. The comparison leads to a revision of socio-technical heuristics by including aspects of AI-usage. The comparison reveals that con-tinuous evolution is a basic characteristic of socio-technical systems, and that human oversight or interventions and the subsequent appropriation of AI-systems lead to continuous adaptation and re-design of the systems, if autono-my is collaboratively exercised. From a socio-technical point of view, the cru-cial requirement of transparency has not only to be fulfilled with technical fea-tures, but also by contributions of the whole system including human actors. It will be promising for using AI, if not only technical features, but organization-al and social practices are socio-technically designed in a way that compen-sates shortcomings of AI.

---


### 145. [ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory](https://arxiv.org/abs/2607.10350)

**<font color=#1a73e8>作者：</font>** Jiayi Tian, Shiao Liu, Yuting Xu 等 27 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent VLM and VLA systems have improved robotic perception and action prediction, yet long-horizon embodied agents still require a general runtime layer for reasoning, memory, tool use, verification, and cross-embodiment execution. We present ABot-AgentOS, a general robotic Agent Operating System that sits above low-level controllers and provides a deliberative agent layer for scene-conditioned planning, context-isolated skill execution, multi-stage verification, multi-modal memory, and edge-cloud collaboration. To evaluate such systems, we introduce EmbodiedWorldBench, an executable benchmark with 16 indoor, outdoor, and hybrid scenes, four difficulty levels, and over 200 tasks involving navigation, object search, NPC dialogue, dynamic events, and trace-grounded scoring. ABot-AgentOS further introduces Universal Multi-modal Graph Memory, a persistent source-grounded substrate that converts dialogue, visual observations, spatial context, temporal relations, and task traces into typed nodes and edges. A failure-driven self-evolution loop converts diagnosed memory failures into gated runtime evo-assets that are promoted only to later evaluation splits, preventing current-split ground-truth leakage while enabling continual improvement. On an initial EmbodiedWorldBench subset, ABot-AgentOS improves over a single-controller baseline in both task success and goal completion. Across memory benchmarks, ABot-AgentOS Static achieves 87.5 on LoCoMo, 59.9 on OpenEQA EM-EQA, 88.6 on Mem-Gallery, and 76.5 Acc@All on NExT-QA; self-evolution further improves LoCoMo to 88.7, OpenEQA to 60.4, and Mem-Gallery to 89.0. These results suggest that a general Agent OS layer can improve long-horizon embodied execution while providing persistent, auditable memory for continual interaction.

---


### 146. [GRC-ProbNet: Uncertainty-aware Feature Extraction for Cardiovascular Disease Classification](https://arxiv.org/abs/2607.10357)

**<font color=#1a73e8>作者：</font>** Yash Shah, Omar Todd, Philipp Seeböck 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The automatic detection and classification of cardiovascular disease (CVD) from computed tomography (CT) images plays an important role in clinical practice. Recently, a hybrid pipeline (GRC-Net) for CVD classification was proposed, which leverages a deep-learning-based segmentation and registration method to extract radiomic and geometric features. However, GRC-Net relies on a deterministic segmentation mask, without considering the inherent ambiguity associated with cardiac anatomy. In this paper, we propose GRC-ProbNet, which takes advantage of a deep ensemble to produce multiple segmentation masks for a given input. From these masks, we extract multiple uncertainty features. We analyze these uncertainty features for both their correlation with segmentation error and their propagation effects on downstream CVD classification performance. Our experiments on the publicly available MM-WHS and ASOCA datasets show that the uncertainty measure that best reflects segmentation quality is not necessarily the one that provides the strongest signal for downstream CVD classification. Overall, our results demonstrate that GRC-ProbNet utilizing uncertainty features substantially improves CVD classification AUROC (92.92\) compared to the baseline GRC-Net model (91.25%). Our code is publicly available: this https URL.

---


### 147. [A Hyperbolic Neural Closure for M1 Radiation Transfer](https://arxiv.org/abs/2607.10364)

**<font color=#1a73e8>作者：</font>** Bongseok Kim, Jiahao Zhang, Johannes Krotz 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In radiation transfer simulations, an M1 method achieves substantial computational savings by replacing the full angular transport equation with a low-order moment system. Because this reduced system is not closed, a closure model is required to represent the unknown higher-order moments using lower-order moments. While machine learning (ML)-based closures can improve accuracy beyond classical analytic closures, unconstrained learned closures may produce non-real characteristic speeds and consequently cause numerical solver breakdown. To guarantee real eigenvalues of the Jacobian associated with ML closures, we propose a hyperbolic neural closure for the M1 radiative transfer system. Rather than directly predicting closure terms, we parameterize the Jacobian through two neural networks: (i) a symmetric matrix network and (ii) a strictly convex entropy network whose Hessian defines a positive definite symmetrizer. These components are combined to yield a Jacobian that is similar to a symmetric matrix, thereby ensuring real eigenvalues. The closure is then reconstructed by numerical integration of the learned Jacobian field along a prescribed integration path. Numerical experiments show that the proposed closure not only achieves higher closure accuracy than classical analytic closures, but also improves solution accuracy and remains stable in discontinuous Galerkin simulations for radiative transfer problems.

---


### 148. [Gradient-Skipping Relevance Propagation for Efficient Explainability of Vision Transformers](https://arxiv.org/abs/2607.10365)

**<font color=#1a73e8>作者：</font>** Christopher Buratti, Michele Marchetti, Federica Parlapiano 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers (ViTs) are difficult to interpret because current methods of relevance propagation and attention flow do not fully consider some key architectural features, such as the uneven importance of attention heads and residual connections. Prior approaches typically assume uniform importance across attention heads; furthermore, they model skip connections as identity paths, leading to inaccurate relevance attribution. To address these issues, we introduce GradSkip, a novel relevance propagation method for ViTs based on adaptive head weighting and skip-aware propagation. GradSkip models the different importance of the attention heads and dynamically distributes relevance between the attention and residual paths. Experiments on ImageNet1K and BloodMNIST demonstrate a state-of-the-art faithfulness of GradSkip while requiring over 14 times fewer GFLOPs than the best-performing existing approaches. Additional evaluations using transformer-based segmentation confirm improved localization and alignment with ground-truth regions.

---


### 149. [Co4ICF: Co-evolving Physics-Informed Surrogate and RL-based Pulse Optimizer for Inertial Confinement Fusion](https://arxiv.org/abs/2607.10366)

**<font color=#1a73e8>作者：</font>** Jiatong Zhao, Tengyue Zhang, Yuhan Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Offline-trained surrogates for Inertial Confinement Fusion (ICF) suffer a well-known failure mode that iterative optimizers drive inputs into out-of-distribution (OOD) regions where predictions become unreliable. Here we present Co4ICF, a co-evolving framework that couples a physics-informed surrogate with a PPO-based pulse optimizer. The surrogate is iteratively fine-tuned on policy-induced trajectories, correcting extrapolation errors as the optimizer shifts the input distribution; the optimizer queries this evolving surrogate as a fast environment. In the 1D MULTI environment, Co4ICF achieves 146.1% normalized yield based on current laser design baseline; as a post-hoc cross-fidelity check, the optimized pulse further attains 246.9% normalized yield when directly evaluated in 2D-MULTI without any 2D training or fine-tuning. Budget-matched ablations support that the gains are not explained solely by additional simulation data and are consistent with the co-evolving mechanism playing a key role. We release a large-scale MULTI-IFE simulation dataset to support future benchmarking.

---


### 150. [Neural Motion Blending Across Arbitrary Character Topologies](https://arxiv.org/abs/2607.10370)

**<font color=#1a73e8>作者：</font>** Luca Cazzola, Giulia Martinelli, Nicola Conci  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Motion blending in character animation enables the synthesis of new motions by interpolating between existing examples. Current methods are typically restricted to fixed skeleton topologies, requiring identical or near-identical skeletal structures across characters. We present a novel framework for motion blending across heterogeneous skeletons. The proposed architecture combines a semantic encoder, which extracts per-frame latent representations of the motion state, with a diffusion-based decoder, which reconstructs character-specific motion conditioned on this latent code. At inference, blended motions are obtained by interpolating the latent representations of two input motions. We train and evaluate the method on the Truebones Zoo dataset using motions defined on both same and distinct skeleton topologies, demonstrating the ability to achieve smooth and plausible blending in a variety of scenarios.

---


> [!TIP]
> 当前位于：**101-150**（第 3/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-420](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
