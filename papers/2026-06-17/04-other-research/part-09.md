# 📦 其他研究 | 2026年06月17日

> 本类共 **509** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**401-450**（第 9/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-509](./part-11.md)

---

### 401. [A Formal Resilience Framework for Cyber-Physical Embodied Systems under Device-Level Cyberattacks](https://arxiv.org/abs/2606.16467)

**<font color=#1a73e8>作者：</font>** Alberto Giaretta  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In cyber-physical systems (CPSs), fault tolerance is traditionally achieved by analysing sensor and actuator outputs, detecting progressive drift or sudden failures, and initiating suitable tolerance mechanisms. Reasonable under general failure models, this approach fails to capture nuanced disruptions caused by cyberattacks, which may employ subtle strategies. This is particularly critical in embodied CPSs, where computational and physical devices not only have an active role in task completion, but also in embodiment preservation (that is, maintaining the system's physical integrity). To prevent structural physical damage, embodied CPSs require a framework that enables proactive response to cyberattacks. This paper proposes a formal dependability framework that incorporates IDS information into resilience evaluation predicates, enabling assessment of tolerance to disruption and degradation. The framework supports structured reasoning about how cyberattacks affect task execution and embodiment preservation, and whether mitigation strategies must be deployed. Analytical examples demonstrate its analytical capability and soundness, establishing a theoretical foundation for dependable and secure embodied CPSs.

---


### 402. [Decoupled Object-Centric Video Understanding for Generating Robotic Manipulation Commands](https://arxiv.org/abs/2606.16470)

**<font color=#1a73e8>作者：</font>** Thanh Nguyen Canh, Thanh-Tuan Tran, Haolan Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Translating video demonstrations into executable robot commands remains challenging because existing methods often fail to identify which objects are functionally involved in the demonstrated action. As a result, they may generate commands that are linguistically plausible but operationally ambiguous. We propose an object-centric video understanding framework that decouples action recognition from object identification to generate precise, grammar-free manipulation commands. Our approach integrates Temporal Shift Modules (TSM) for efficient spatio-temporal action classification with a novel \textbf{Object Selection} algorithm that identifies task-relevant objects through trajectory-based role classification, blur detection, and overlap minimization. The selected objects are then processed by Vision-Language Models (VLMs) for robust category recognition and zero-shot generalization. Evaluated on a modified Something-Something V2 dataset, our method achieves 86.79\% action classification accuracy and BLEU-4 scores of 0.337 on standard objects and 0.261 on novel objects. These results improve over the strongest task-specific baseline by 80.2\% and 143.9\%, respectively. Larger gains are observed in METEOR and CIDEr, reaching 157.9\% and 171.7\% on novel objects. Across all semantic metrics, our approach consistently outperforms task-specific methods and remains competitive with, or surpasses, large general-purpose VLMs while retaining a modular, object-centric design.

---


### 403. [From Awareness to Adherence: Bridging the Context Gap in Spoken Dialogue Systems via Context-Aware Decoding](https://arxiv.org/abs/2606.16472)

**<font color=#1a73e8>作者：</font>** Che Hyun Lee, Heeseung Kim, Sungroh Yoon  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite the success of end-to-end (E2E) spoken dialogue systems, maintaining strict context adherence in multi-round conversations remains a challenge. While prior works attribute these failures to models forgetting dialogue history, we highlight an equally critical but overlooked bottleneck: a gap between latent context awareness and active adherence. Although models internally recognize relevant past utterances, strong parametric priors often overshadow these signals during decoding. To bridge this gap, we propose an audio-adapted Context-Aware Decoding (CAD) approach. By leveraging internal attention mechanisms to isolate key historical rounds, our approach contrasts output distributions with and without this key context during inference, directly amplifying multimodal contextual signals. Evaluations on the Audio MultiChallenge benchmark demonstrate significant improvements in Semantic Memory and Self Coherence subtasks, successfully enforcing strict, context-faithful adherence.

---


### 404. [Measurement Study of Post-Quantum Readiness of Internet: 2026](https://arxiv.org/abs/2606.16473)

**<font color=#1a73e8>作者：</font>** Vanishka Mohan Dubey, Gaurav Varshney  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The emergence of quantum computing presents a fundamental challenge to the security of current Internet communication systems. Transport Layer Security (TLS), which forms the backbone of secure web communication, predominantly relies on classical public-key cryptographic algorithms such as RSA and elliptic curve cryptography (ECC), both of which are susceptible to quantum attacks. This paper conducts a large scale empirical evaluation of post-quantum readiness across 32,011 domains, with a primary focus on real-world TLS deployments across diverse sectors by analysing negotiated TLS parameters, including protocol versions, cipher suites, key exchange mechanisms, and certificates. The results indicate that while modern protocols like TLS 1.3 and QUIC are gaining adoption, 15.70% of domains especially in critical sectors such as banking and government still rely on TLS 1.2.
Furthermore, 49.3% of domains support hybrid post-quantum key exchange mechanisms (e.g., MLKEM768 with X25519), whereas 50.7% continue to use classical key exchange, reflecting partial transition. Notably, 0% adoption of hybrid post-quantum certificates was observed, leaving the authentication layer vulnerable to quantum-enabled attacks such as certificate forgery. The findings reveal uneven adoption of post-quantum mechanisms across sectors, where technology driven platforms are advancing more rapidly than legacy-dependent infrastructures. Overall, the study highlights that achieving complete quantum resilience requires a coordinated transition not only in key exchange mechanisms but also in certificate infrastructures. Without such comprehensive migration, Internet communication systems remain vulnerable to long-term threats, including Harvest-Now-Decrypt-Later (HNDL) attacks.

---


### 405. [MVOFormer: Flow-Semantic Transformer for Robust Monocular Visual Odometry](https://arxiv.org/abs/2606.16474)

**<font color=#1a73e8>作者：</font>** Jituo Li, Shunwang Sun, Jialu Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular visual odometry (MVO) is foundational to autonomous navigation and robotic localization. However, existing learning-based MVO approaches often struggle with either a lack of interpretable, complementary features or overly complex multi-stage architectures. These limitations inherently restrict their robustness and cross-domain generalization. In this work, we propose MVOFormer, a novel transformer framework for robust monocular visual odometry. Our architecture features a Flow-Semantic Dual Branch Encoder that synergizes dense geometric motion cues with object-centric semantic priors, explicitly distinguishing static structures from dynamic distractors. These representations are then fused by an Iterative Multimodal Decoder, enabling coarse-to-fine pose refinement while dynamically suppressing attention on unreliable regions. Extensive evaluations demonstrate that, without any target-domain fine-tuning, MVOFormer achieves superior zero-shot generalization and robustness, significantly outperforming prior learning-based frame-to-frame methods across diverse benchmarks including TartanAir, KITTI, TUM-RGBD, and ETH3D-SLAM.

---


### 406. [AURA: Active-Response Attribution under Treatment Ambiguity in Bacterial Cytological Profiling](https://arxiv.org/abs/2606.16477)

**<font color=#1a73e8>作者：</font>** Kartik Jhawar, Mrunmayee Deshpande, Wilfried Moreira 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When a bacterial sample is exposed to several antibiotics, not every applied drug necessarily acts: if the organism is resistant to one of them, that drug leaves no morphological trace. The clinically meaningful quantity is therefore not which antibiotics were applied, but which ones were active. We show that these two are sharply decoupled in real E. coli microscopy - naively assuming the applied combination equals the active one is correct only about 37% of the time - yet existing computational tools are ill-suited to recovering the active set. Forward perturbation models such as scGen, CPA, and IMPA are designed to predict appearance from treatment, not the reverse, and inverting them degrades sharply; discriminative image classifiers tend to memorise strain- and batch-specific texture and fail to transfer across experimental replicates. We introduce AURA, which reframes the task as constrained, energy-based inverse attribution. Its central inductive bias is that the active set must be a subset of the applied set; this collapses the candidate space and lets AURA infer the active subset of applied antibiotics by decomposing residual morphology into antibiotic response atoms and selecting the subset with the lowest reconstruction energy, using no strain label at test time. AURA-E adds evidence-aware abstention, withholding a prediction when candidate explanations remain near-equally plausible. On cross-replicate transfer in an E. coli cytological profiling dataset, AURA recovers the active antibiotic combination with 95.47% exact-match accuracy.

---


### 407. [Uncertainty Quality of VGGT: An Analysis on the DTU Benchmark Dataset](https://arxiv.org/abs/2606.16479)

**<font color=#1a73e8>作者：</font>** Markus Hillemann, Robert Langendörfer, Steven Landgraf 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual Geometry Grounded Transformer (VGGT) has already attracted a great deal of attention in a short period of time, not least due to the Best Paper Award at CVPR-2025. Similar to DUSt3R and MASt3R, VGGT aims to bring about a paradigm shift by replacing established methods like bundle adjustment and feature matching with a simple, unified, feed-forward neural network that predicts camera poses, depth maps, and dense 3D structure directly from multiple images of a scene in a few seconds. A key aspect is its ability to process an arbitrary number of views consistently in a single forward pass without any post-processing or iterative optimization. For photogrammetry, this opens new possibilities for real-time, scalable, and accessible 3D reconstruction. In this context, not only high reconstruction accuracy but also high-quality uncertainty estimates are crucial, as they foster trust and enable robust quality assurance. This paper therefore investigates the quality of VGGT's uncertainty predictions. The analysis identifies an effective confidence threshold for filtering VGGT's raw output and demonstrates that enhancing uncertainty quality holds strong potential for improving the accuracy of its 3D reconstructions.

---


### 408. [daVinci-kernel: Co-Evolving Skill Selection, Summarization, and Utilization via RL for GPU Kernel Optimization](https://arxiv.org/abs/2606.16497)

**<font color=#1a73e8>作者：</font>** Dayuan Fu, Mohan Jiang, Tongyu Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> GPU kernel optimization represents a paradigm where functional correctness is assumed and execution efficiency is the objective. We present daVinci-kernel, a reinforcement learning framework that couples skill discovery with skill exploitation through a dynamically evolving skill library. daVinci-kernel jointly trains three agents sharing one LLM backbone: a Skill Selection Agent that retrieves relevant techniques via BM25 and LLM reranking, a Policy Agent that generates multi-turn CUDA/Triton kernels conditioned on selected skills, and a Skill Summary Agent that distills successful rollouts into reusable skills. Candidate skills are added only after execution-based verification confirms reproducible speedups. All three agents share a single LLM backbone, are initialized via a structured SFT cold start on diversity-filtered data, and are then jointly optimized end-to-end with multi-turn REINFORCE and per-agent advantage estimation. On KernelBench, daVinci-kernel-14B achieves 37.2%, 70.6%, and 32.2% on Level 1, Level 2, and Level 3 under the Fast$_1$ threshold, outperforming the strongest prior RL-trained model, this http URL-14B.

---


### 409. [Active Reference Acquisition in Few-Shot Font Generation](https://arxiv.org/abs/2606.16502)

**<font color=#1a73e8>作者：</font>** Shinnosuke Matsuo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot font generation aims to synthesize the remaining glyphs of a font given one or a few reference glyphs while preserving stylistic consistency, thereby supporting font designers in efficiently completing a typeface. Existing methods primarily focus on improving generation quality given a fixed reference set. However, when the current reference glyphs are insufficient to represent the target style, few-shot font generation may fail to produce satisfactory results. In practical scenarios, additional reference glyphs can often be obtained from the designer when necessary. Accordingly, we propose a new framework, Active Reference Acquisition in Few-Shot Font Generation, in which the model sequentially decides which character to acquire next as an additional reference. Furthermore, we propose a reference part-coverage-based acquisition function to efficiently query the designer. Motivated by the observation that font styles are well characterized by local structural parts, we represent each glyph using a histogram of local features and select query characters that maximize the expected part coverage of the reference set. By prioritizing characters that contain parts not yet covered by the current references, the proposed method progressively expands the diversity of visual parts in the reference set. As a result, generation quality is improved with fewer queries. Experiments on the Google Fonts dataset demonstrate that the proposed method achieves higher generation quality than random querying and reference-agnostic baselines. The code is available at this https URL.

---


### 410. [Model Graph Inductive Learning for Knowledge Graph Completion](https://arxiv.org/abs/2606.16509)

**<font color=#1a73e8>作者：</font>** Mohommad Esmaei Khani, Mahdieh Hasheminejad, Ali Taherkhani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Link prediction in knowledge graphs fundamentally depends on the quality of learned embeddings for entities and relations. However, most existing methods derive these embeddings by aggregating only the local neighborhood of each entity, neglecting the global structure of the knowledge graph. This limited view prevents models from capturing higher-level structural patterns that are essential for accurate and generalizable link prediction.
To address these limitations, we introduce Model Graph Inductive Learning (\textbf{MGIL}), a framework that constructs a model graph by clustering entities based on the similarity of their incoming and outgoing relational structures or their entity types. A GNN is then applied to this model graph to produce embeddings that capture the global view of the knowledge graph. These embeddings subsequently serve as high-quality initial features %embeddings for the original knowledge graph, replacing random initialization and leading to more stable and expressive representations.
Extensive experiments on standard and recently proposed inductive benchmarks demonstrate that MGIL achieves state-of-the-art or highly competitive performance in inductive link prediction, highlighting its effectiveness across diverse graph settings.

---


### 411. [Direction-Conditioned Policies via Compositional Subgoal Scoring for Online Goal-Conditioned Reinforcement Learning](https://arxiv.org/abs/2606.16515)

**<font color=#1a73e8>作者：</font>** Swaminathan S K, Damiya Gondha, Theyanesh Eswaramoorthy Rajahkrishnan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hamilton-Jacobi-Bellman theory implies that the optimal goal-conditioned action depends on the goal only through the gradient of the goal-reaching distance at the current state, yet standard online GCRL still conditions the actor on the raw goal -- a signal that is geometrically uninformative when the goal is far from the data distribution. We propose Direction-Conditioned Policies (DCP), a fully online method that decomposes goal-reaching into two components sharing one InfoNCE representation $\psi$: a subgoal-scoring step that selects a visited state $z_t$ aligned with the final goal $g$ in $\psi_g$, and a direction-conditioned actor that consumes the unit direction $d_t$ and magnitude $r_t$ from $\psi(s_t)$ to $\psi(z_t)$. The two components train jointly, factor cleanly at deployment (subgoal scoring is removed, while direction conditioning remains with $g$ in place of $z_t$), and admit independent modification at the same $(d_t,r_t)$ interface. We prove three results. First, direction sufficiency under HJB: the optimal action under control-affine dynamics depends on the goal only through the value gradient. Second, a quantitative bound showing that, under mild conditions on the learned representation and assuming the scoring rule returns an on-path $z_t$, the actor's conditioning input at training and at deployment coincide up to representation error and geodesic slack. Third, a controllable-subspace characterization of when directional conditioning fails. Across nine environments, DCP improves over Contrastive RL on most final metrics, with the largest gains on manipulation and obstacle-interaction tasks; a qualitative analysis of the learned $\psi$-distance landscape shows the contrastive representation behaves as an online quasimetric encoding environment topology, and the single failure case (AntSoccer) localizes to a learned-gradient pathology that the theory anticipates.

---


### 412. [SkillWiki: A Living Knowledge Infrastructure for Agent Skills](https://arxiv.org/abs/2606.16523)

**<font color=#1a73e8>作者：</font>** Dingcheng Huang, Yuda Ding, Bingshuo Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While knowledge is managed through Wikipedia and software through GitHub, agent skills still lack an infrastructure for large-scale production, governance, and evolution. SkillWiki is a living knowledge infrastructure that supports the organization, grounding, and continuous evolution of agent skills by transforming heterogeneous knowledge into reusable skill assets linked to their originating evidence. Our demonstration presents the complete skill lifecycle, from knowledge ingestion and skill production to provenance-aware exploration, governance, and execution-driven evolution. SkillWiki highlights a future in which knowledge, skills, and execution experience co-evolve within a shared infrastructure. The live demonstration and source code are publicly available at this https URL.

---


### 413. [Neural Bayesian Anomaly Mitigation: A Robust Loss that Doubles as an Unsupervised Contamination Classifier](https://arxiv.org/abs/2606.16524)

**<font color=#1a73e8>作者：</font>** S. A. K. Leeney, W. J. Handley, H. T. J. Bevins 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Engineered robust losses such as Huber, Student-$t$, and generalised cross-entropy make supervised models tolerant of contamination but cannot answer which observations are corrupted. We introduce Neural Bayesian Anomaly Mitigation (NBAM), a general-purpose drop-in loss derived from a Bayesian latent-switch mixture model: the marginal likelihood defines a robust supervised loss, and the associated posterior defines an unsupervised contamination classifier. Like Huber or Student-$t$, NBAM can replace the standard training loss in any supervised pipeline; unlike them, it additionally learns a structured contamination model and returns a calibrated per-sample contamination posterior. A learned input-dependent prior $\pi_\phi(x)$ captures the spatial locality of contamination, so that samples near known corruptions are more likely to be flagged, while an Occam penalty emerges automatically and regularises against over-flagging. On CIFAR-10 with asymmetric label contamination, NBAM recovers the structure of the corruption process without supervision: the contamination posterior separates clean from corrupted samples, and the learned anomaly head identifies the direction of every label-flip pair. Alongside these capabilities, NBAM outperforms the four robust-loss baselines considered here at contamination rates 0.2-0.6.

---


### 414. [Assessing Reliability of Symbol Detection in Concept Bottleneck Models](https://arxiv.org/abs/2606.16535)

**<font color=#1a73e8>作者：</font>** Javier Fumanal-Idocin, Javier Andreu-Perez  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Concept Bottleneck Models (CBMs) are a relevant tool for explainable Artificial Intelligence because they make their predictions through human-interpretable symbols. However, high task accuracy does not guarantee that these symbols are detected faithfully: jointly trained CBMs may encode task-specific shortcuts in the bottleneck, making their explanations unreliable. In this paper, we study concept-detection reliability by swapping independently trained concept detectors and classification heads that share the same symbolic vocabulary. We use the resulting performance degradation, concept-level metrics, and symbol-wise uncertainty estimates to identify concepts that are especially prone to spurious firing. Finally, we propose a reliability-aware training strategy in which a shared concept detector is optimized with multiple classification heads and penalized for relying on globally or instance-wise unreliable symbols. On CUB-200-2011 with full concept supervision, detectors and heads are almost freely interchangeable (swap drop below one accuracy point, relative retention above $99\%$, and no concept detected below chance), whereas on a controlled synthetic task we show that, as the concept-supervision weight is reduced, models keep near-perfect task accuracy while swapped accuracy and agreement with the ground-truth concepts collapse to chance. Our reliability-aware training substantially mitigates this leakage, roughly doubling swap accuracy in the leaky regime.

---


### 415. [The Faithfulness Gap: Certifying Semantic Equivalence Between Natural-Language and Formal Mathematical Statements](https://arxiv.org/abs/2606.16541)

**<font color=#1a73e8>作者：</font>** Noor Islam S. Mohammad, Tamim Sheikh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autoformalization, translating natural-language mathematics into formal proof assistants, is bottlenecked not by translation fluency but by \emph{faithfulness}: a formal statement can typecheck and be provable, yet still encode a different theorem than the source intended. We introduce \emph{Bidirectional Provability Fingerprinting} (\bpf{}), a framework that certifies faithfulness by characterizing each candidate through its forward and backward consequence neighborhoods in the ambient theory and matching these against probes derived from the natural-language statement. We further introduce four novel components: (i) \emph{Counterfactual Probe Generation} (\cpg{}), a contrastive procedure that synthesizes probes targeting specific drift directions; (ii) the \emph{Equivalence Spectrum}, a continuous faithfulness score that replaces brittle binary verdicts; (iii) \emph{Adaptive Probe Budget Allocation} (\apba{}), an information-theoretic budget router; and (iv) \emph{Faithfulness-Guided Decoding} (\fgd{}), which uses \bpf{} signals as a reward during autoformalization. We prove a \emph{drift detection theorem} and a \emph{PAC-faithfulness} result establishing that the equivalence class of a natural language statement is learnable from $\mathcal{O}(\log(1/\delta)/\varepsilon)$ probes under mild assumptions. We release \driftbench{}, a benchmark of $2{,}183$ NL/Lean~4 pairs with controlled drift labels across six subfields of mathlib4. \bpf{}\,+\,\cpg{} detects $89.6\%$ of drifted formalizations at a $3.0\%$ false-positive rate-against $41.2\%$ for typecheck and $63.3\%$ for LLM-judge baselines, and \fgd{} reduces the rate at which a state-of-the-art autoformalizer emits drifted statements by $47\%$. this https URL

---


### 416. [ROSA-RL: Uncertainty-Aware Roundabout Optimized Speed Advisory with Reinforcement Learning](https://arxiv.org/abs/2606.16558)

**<font color=#1a73e8>作者：</font>** Anna-Lena Schlamp, Jeremias Gerner, Klaus Bogenberger 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Roundabouts challenge automated driving in mixed traffic, as heterogeneous and non-deterministic human behavior, unknown driving intentions, and high interaction complexity create uncertainty about whether the conflict zone will be blocked or available at the moment of entry. We present ROSA-RL -- uncertainty-aware Roundabout Optimized Speed Advisory with Reinforcement Learning. It enables safe and efficient roundabout entry for automated and human-driven vehicles in mixed traffic through probabilistic conflict forecasting. A Transformer-based model predicts conflict zone occupancy over a five-second horizon, capturing multi-agent interactions to anticipate upcoming conflicts and available gaps. The prediction outputs encode uncertainty in future motion and intent, and augment the state of a classical RL framework, enabling uncertainty-aware speed coordination. Evaluated in simulations grounded in real-world data, ROSA-RL can effectively handle uncertainty and outperform a comparable model-based baseline, closing the gap to an ideal setting assuming fully known occupancy while improving traffic efficiency and safety. The source code of this work is available under: this http URL.

---


### 417. [The BD-LSC Dataset: Facilitating the Benchmarking of Models for Lexical Semantic Change Detection in Slang and Standard Usage](https://arxiv.org/abs/2606.16560)

**<font color=#1a73e8>作者：</font>** Afnan Aloraini, Viktor Schlegel, Goran Nenadic 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic semantic change detection aims to identify how word meanings shift over time, offering insights into both linguistic and societal change. Despite recent progress in computational lexical semantic change (LSC), existing benchmarks and methods struggle to capture bi-directional semantic change, particularly cases where words simultaneously gain and lose senses. This problem is especially challenging for words that have both slang and standard meanings. To address these gaps, we introduce two complementary benchmark datasets. The Bi-Directional Lexical Semantic Change (BD-LSC) dataset captures sense gain, sense loss, and stability across three time periods, enabling the study of complex semantic trajectories. The SlangTrack Word Sense Disambiguation (ST-WSD) dataset provides fine-grained, instance-level sense annotations for words combining slang and standard usages, supporting systematic benchmarking of WSD and semantic change detection models. Using these benchmarks, we systematically evaluate models across different methodological families: unsupervised clustering using contextualised embeddings, supervised machine learning, transformer-based models, and state-of-the-art large language models. Among the evaluated systems, the few-shot GPT-4o model achieved the strongest aggregate performance on Exact Sense Match (ESM) and multi-label accuracy; however, Macro-F1 scores near 0.5 across all systems show that rare slang senses remain difficult, which we identify as the central open challenge.

---


### 418. [A data-driven security quantification framework for IoT-based systems](https://arxiv.org/abs/2606.16561)

**<font color=#1a73e8>作者：</font>** Alhassan Abdulhamid, Sohag Kabir, Ibrahim Ghafir 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Internet of Things (IoT) is integral to modern cyber-physical systems. Quantitative cybersecurity assessment in IoT environments remains challenging due to heterogeneous system architectures, evolving threat landscapes, and the limited availability of reliable probabilistic exploitability data. Although Attack Tree Analysis (ATA) provides a structured framework for modelling potential attack paths leading to system compromise, conventional ATA quantification often relies on subjective expert judgement or heuristic scoring schemes, which can introduce uncertainty and reduce analytical reproducibility. This study introduces a data-driven probabilistic security framework for IoT-based safety-critical systems by integrating Model-Based Systems Engineering (MBSE), ATA, and empirical vulnerability data. In the proposed framework, SysML models capture system architecture, from which attack trees are derived. Vulnerabilities are mapped as Basic Attack Steps and assigned exploitation probabilities using the Exploit Prediction Scoring System (EPSS). The attack tree is then represented as a Bayesian Network, enabling probabilistic reasoning, diagnostic inference, and vulnerability criticality analysis. The framework quantifies system compromise probabilities, identifies likely causes of attacks, and prioritises mitigation strategies. By combining architecture-driven modelling with real-world vulnerability intelligence, it provides a rigorous, reproducible approach for cybersecurity risk assessment in complex IoT environments.

---


### 419. [Local-GS: Accelerating 3D Gaussian Splatting via Tile-Local Warp Coherence](https://arxiv.org/abs/2606.16566)

**<font color=#1a73e8>作者：</font>** Yang Luo, Yan Gong, Yongsheng Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) has significantly advanced real-time novel view synthesis by representing scenes as dense collections of anisotropic 3D Gaussian primitives. However, the irregular spatial distribution of Gaussians often leads to poor GPU utilization, as warp divergence and redundant computation degrade rendering performance. To address this, we present Local-GS, a warp-coherent rendering paradigm that, organizes Gaussian primitives with respect to SIMT (Single Instruction, Multiple Threads) execution boundaries rather than scene geometry. Specifically, we propose three warp-coherent stages: a hoisting stage that precomputes shared parameters at tile level, a culling stage that discards warps with no contribution, and a blending stage that replaces per-pixel branching with a uniform instruction stream. Across extensive benchmarks on multiple datasets, Local-GS improves efficiency without compromising quality. As a plug-and-play optimization, it provides additional performance gains to all tested baselines, culminating in a $7.76\times$ speedup on Deep Blending scenes.

---


### 420. [TNODEV: Toolbox for Neural ODE Verification](https://arxiv.org/abs/2606.16567)

**<font color=#1a73e8>作者：</font>** Abdelrahman Sayed Sayed, Pierre-Jean Meyer, Mohamed Ghazel  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Neural ordinary differential equations (neural ODE) have started to appear in safety critical settings such as continuous-time controllers for cyber-physical systems and classifiers integrated into automated decision pipelines, raising the question of whether their behavior can be formally verified. Existing tools dedicated to neural ODE provide only a single reachability call without iterative input set refinement, limiting the precision of their verdicts to whatever one reachability call can deliver. We present TNODEV, the first sound formal verifier for neural ODE that integrates a falsification checker, a fast interval-based reachability backend based on continuous-time mixed monotonicity, a verification and refinement loop with three input-set splitting heuristics, and a parallel scheduler in a single end-to-end pipeline. TNODEV supports safe-set inclusion verification on pure neural ODE, neural ODE in closed loop with a neural network controller and general neural ODE (GNODE), with the safe set specified either as an interval or as the half-space intersection induced by a target classification label. We evaluate TNODEV on a range of benchmarks across safe-set inclusion and classification-robustness properties, including a direct reachability comparison against NNV~2.0 and CORA and a verification comparison against NNV2.0 on MNIST general neural ODE classifiers.

---


### 421. [Fast When, Careful Who: Dual-Process Multiparty Turn-Taking with Diffusion Augmentation](https://arxiv.org/abs/2606.16568)

**<font color=#1a73e8>作者：</font>** Rutherford A. Patamia, Ming Liu, Wei Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reliable turn-taking is essential for spoken dialogue systems. However, most existing methods are designed for two-speaker interaction and struggle with realistic multiparty audio containing overlap and rapid speaker changes. We study multiparty turn-taking on the VoxConverse dataset and propose an audio-only two-stage pipeline that separates when to trigger a turn boundary from whether the floor is actually transferring. A fast trigger scans the audio and proposes candidate end-of-turn times, while a lightweight verifier runs only at those times to decide \textsc{Hold} or \textsc{Shift} and support next-speaker prediction. We report results in the full multiparty setting and a controlled dyadic top-2 projection for comparability. We also investigate diffusion-based, label-preserving background-audio mixing as a data augmentation strategy. Results show improved shift detection over a baseline, with further improvements from diffusion augmentation.

---


### 422. [RepNet: Tackling spectral bias in deep neural networks via parameter reparameterization](https://arxiv.org/abs/2606.16575)

**<font color=#1a73e8>作者：</font>** Yong Wang, Tao Zhou, Xuhui Meng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks (DNNs) have achieved remarkable success in scientific computing, yet they often suffer from spectral bias in capturing oscillatory and multiscale behaviors. In this study, we investigate this limitation by examining the failure of shallow ReLU neural networks in fitting high-frequency functions. This observation identifies two important factors in resolving rapid oscillations: the initial slope scale and the distribution of partition points induced by the networks. Motivated by this analysis, we propose RepNet, a reparameterized DNN model for ReLU and tanh networks designed for high-frequency and multiscale problems. The key idea is to reparameterize the weights and biases in the first hidden layer, which enables effective control of the initial slope scale and provides an appropriate distribution of the initial partition points. Furthermore, treating the reparameterized weights and biases as trainable parameters allows the DNN to achieve adaptive frequency scaling during training. In addition, we derive quantitative estimates for the output and slope magnitudes of the reparameterized DNN to guide the initialization of the proposed method. Numerical experiments, including multiscale one- and four-dimensional function approximation, forward and inverse PDE problems in combination with physics-informed neural networks (PINNs), and operator learning, demonstrate that RepNet improves the predicted accuracy of vanilla DNNs in capturing highly oscillatory features with slightly additional computational cost. These results indicate that RepNet provides an effective and flexible approach for overcoming spectral bias and applying DNNs to multiscale problems.

---


### 423. [On the Entropy Formula for Real, Complex, and Quaternionic Deep Linear Networks](https://arxiv.org/abs/2606.16579)

**<font color=#1a73e8>作者：</font>** Luis Contreras, Marco Nahas, Tejas Kotwal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We extend the entropy formula of Menon and Yu for the real Deep Linear Network (DLN) to its complex and quaternionic analogues, obtaining a unified formula for DLNs over $\mathbb{R}$, $\mathbb{C}$, and $\mathbb{H}$.

---


### 424. [Uncertainty Is Not a Safety Net for Clinical VQA, but Can It Anticipate Model Failure?](https://arxiv.org/abs/2606.16583)

**<font color=#1a73e8>作者：</font>** Arnisa Fazla, Alberto Testoni, Ameen Abu-Hanna 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Safe deployment of clinical vision-language models (VLMs) requires reliable uncertainty estimation (UE): a signal indicating when predictions should be trusted or escalated to a clinician. We test whether current UE methods actually deliver this signal. Benchmarking 8 methods across 12 VLMs on clinical visual question-answering (VQA), we find that UE quality is not an intrinsic property of the UE method: it tracks model accuracy, degrading precisely where the model performance is weakest, and therefore where reliability is most needed. When we stress-test models by hiding the correct option among the multiple-choice answers (NOTA perturbations), accuracy collapses while uncertainty barely changes, leaving models systematically miscalibrated. Yet, we find that uncertainty on the unperturbed input reliably anticipates which predictions will collapse under NOTA, indicating that UE in current VLMs carries diagnostic information about model fragility. Our results position UE as a diagnostic tool for identifying fragile predictions and motivate perturbation-based evaluation as a path toward safe clinical deployment.

---


### 425. [Infant Spontaneous Movement Noise Improves Exploration in Deep RL](https://arxiv.org/abs/2606.16590)

**<font color=#1a73e8>作者：</font>** Francisco M. López, Markus R. Ernst, Francisco Cruz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Exploration in deep reinforcement learning (RL) is commonly implemented as temporally uncorrelated white noise. However, recent works show that temporally correlated colored noise can improve exploration efficiency by producing smooth trajectories with better coverage of the state space. We inquire whether action noise inspired by infant spontaneous movements can also improve exploration in deep RL. We find that the power spectral densities of babies' end-effector velocities follow a colored noise process where the spectral exponent increases with age. Inspired by this developmental pattern, we introduce a mechanism that progressively increases the temporal auto-correlation of exploration noise during RL training, matching the infant statistics. Experiments across several RL environments show that infant-inspired noise produces structured exploratory behavior and can improve learning efficiency compared to conventional exploration strategies. These findings suggest that human motor and cognitive development can provide useful guidance for designing learning mechanisms in artificial agents. Our code is available at this https URL.

---


### 426. [Rotational Symmetry based Object Pose Estimation from Point Clouds in the Absence of Known 3D Models](https://arxiv.org/abs/2606.16593)

**<font color=#1a73e8>作者：</font>** Weichen Dai, Ruixun Yu, Yangjie Tang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object pose estimation is crucial to many industrial applications, with one example being automated spray painting using a robot. However, confidentiality concerns often limit access to high-quality 3D models, posing a significant challenge for point-cloud-based pose estimation. In such scenarios, rotational symmetry, a readily accessible characteristic of many industrial objects, can provide valuable prior information to facilitate pose this http URL this paper, we propose a method that leverages the rotational symmetry commonly found in industrial objects to address the challenge caused by the absence of 3D models. The object pose is jointly estimated with point cloud refinement through an iterative optimization process. This optimization relies on a rotational symmetry constraint loss. To construct this loss, each 3D point is rotated according to the currently estimated pose, and multiple correspondences are identified using nearest-neighbor search by exploiting the rotational symmetry property. These correspondences are then used to compute the rotational symmetry constraint loss, which iteratively refines both the pose and the point this http URL explicitly incorporating rotational symmetry into the optimization process, the proposed method achieves robust pose estimation and generalizes well across diverse object types. The proposed method is evaluated on a dataset specifically created for point clouds without known 3D models, consisting of four categories of synthetic objects and one real wheel hub collected from a production line. Experimental results demonstrate that the proposed method achieves performance comparable to methods that rely on known 3D models.

---


### 427. [How Far Can Machine Translation Quality Take You? Extrinsic Discourse Evaluation in Goal-Oriented Setups](https://arxiv.org/abs/2606.16596)

**<font color=#1a73e8>作者：</font>** Wafaa Mohammed, Kata Naszadi, Vlad Niculae  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing machine translation (MT) metrics and discourse-focused evaluations primarily assess translation quality intrinsically, without measuring the downstream consequences of translation errors. In this work, we focus on extrinsic discourse evaluation of machine translation under two distinct regimes: static and interactive. Under the static regime, we propose an entity counting task as a probe of referential consistency in discourse. We show that high intrinsic MT quality does not reliably predict downstream discourse success and strong MT systems still produce referential inconsistencies. For the interactive regime, we study the goal-oriented multi-agent Welfare Diplomacy game as a probe of long-horizon communication and coordination. We find that interaction-specific translation failures impact downstream coordination. Our results highlight goal-oriented environments as a viable framework for discourse-sensitive extrinsic MT evaluation.

---


### 428. [PhysGuard: Fisher-Guided Gradient Projection for Sim-to-Real Neural PDE Surrogates](https://arxiv.org/abs/2606.16602)

**<font color=#1a73e8>作者：</font>** Changjian Zhou, Junfeng Fang, Negin Yousefpour 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operator models trained on simulation data often lose accuracy when applied to experimental measurements due to the sim-to-real gap. Standard fine-tuning with limited real data can reduce this gap, but it may also damage the core physics-relevant representations learned during pretraining. Although knowledge-preserving adaptation has been widely investigated in vision or language tasks, it remains unclear whether these methods are suitable for neural operators whose architectures and protected knowledge are fundamentally different. Neural operators need to preserve core-scale physical structures rather than semantic or visual features. We propose PhysGuard, a physics-preserving framework for accurate sim-to-real adaptation of neural operators. Specifically, PhysGuard uses the empirical Fisher Information Matrix computed on simulation data to identify physics-critical parameter directions, then restricts fine-tuning updates to directions that do not interfere with them. A layer-wise Gram-matrix formulation makes this efficient for models with millions of parameters, while an adaptive threshold automatically determines the protected subspace size. A spectral probe experiment shows that the dominant Fisher directions are strongly associated with low-frequency output structures. Experiments on benchmark across four neural operator architectures and different physical systems show that PhysGuard performs strongly on most evaluation metrics compared to baselines. The benefits are most evident under severe domain shift, where it reduces low-frequency error by up to 32\% compared to standard fine-tuning while maintaining adaptability. Our code is available at this https URL.

---


### 429. [VeriGraph: Towards Verifiable Data-Analytic Agents](https://arxiv.org/abs/2606.16603)

**<font color=#1a73e8>作者：</font>** Jiajie Jin, Zhao Yang, Wenle Liao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based agents have demonstrated strong capabilities in data-intensive analytical tasks, yet their outputs are rarely verifiable: a reliance on linear text trajectories makes their reasoning difficult to audit. In particular, deterministic computations over raw data and semantic deductions over natural-language claims are often entangled in an unstructured stream, leaving numerical conclusions hard to reproduce and qualitative judgments hard to inspect. To address this, we propose VeriGraph, a traceable neuro-symbolic reasoning framework that enables agents to construct an explicit heterogeneous evidence directed acyclic graph (DAG) during execution. VeriGraph introduces three evidence-expansion primitives, namely computational, grounding, and derivational expansion, to connect raw data, interpreter variables, computed results, and natural-language claims in a unified graph. Under this formulation, structural traceability is reduced to graph reachability from raw data sources to terminal claims, while semantic support is measured by claim-level evidence evaluation. To improve graph construction, we further design a graph-based policy optimization strategy with a composite reward that jointly supervises answer correctness, computational integrity, and derivational coherence. Experiments on four benchmarks show that VeriGraph-8B achieves the highest overall score among all baselines. More importantly, VeriGraph produces auditable evidence graphs with substantially stronger claim grounding, achieving a 87.61\% Grounding Rate under our claim-level evidence support evaluation. These results suggest that explicit evidence-graph construction is a promising path toward verifiable data-analytic agents. Our code is available at this https URL.

---


### 430. [TCHG: Tri-Trust Conditioned Heterogeneous Graph Learning for Reliable Dynamic Trust Prediction](https://arxiv.org/abs/2606.16611)

**<font color=#1a73e8>作者：</font>** Bohao Liao, Boyu Deng, Qipeng Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Trust prediction infers latent user-user trust relations and provides important support for social recommendation, fake-review and manipulation detection, and risk identification. Graph neural networks have become a prominent approach to trust prediction because of their ability to learn network structures and complex trust dependencies. However, existing methods often rely on a unified representation of trust signals and do not disentangle heterogeneous trust evidence into separate evidence channels, failing to exploit the distinct roles that different evidence channels should play during trust modeling. To address this gap, this paper argues that trust evidence should not be treated as an undifferentiated input, but should be decomposed and used as functional control factors over graph propagation. We propose TCHG, a tri-trust conditioned heterogeneous graph learning framework that decomposes trust evidence into three channels and assigns them distinct functional roles in propagation: entity reliability governs message admission, interaction-behavior reliability modulates propagation strength, and contextual trust adjusts the propagation mode through context-conditioned operator selection. Since the three evidence channels evolve at different temporal scales, TCHG maintains independent temporal states with non-uniform decay rates to prevent rapidly changing contextual signals from overwriting slowly accumulated entity reliability. It further predicts trust probability and calibrates the output probability, improving predictive confidence under sparse or conflicting evidence. Extensive experiments on multiple public trust datasets show that TCHG achieves effective and reliable trust prediction compared with representative trust prediction and heterogeneous graph baselines.

---


### 431. [Sycophancy as Material Failure under Pushback Loading: A Multi-Axis Characterization Across Three Loading Cases and up to Seventeen Material Charges](https://arxiv.org/abs/2606.16617)

**<font color=#1a73e8>作者：</font>** Ferdinand M. Schessl  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sycophancy in LLMs is documented across 70+ papers, but expert agreement on construct boundaries remains low (ICC=.184; Ye et al., 2026). The construct fragments because behavioral classification depends on which surface form is privileged. We adopt a materials-science framing: conversation as test specimen under load, LLM-model as material charge, pushback as progressive load, stance-flip as material failure. We characterize this failure across three loading cases (debate n=1000; false-presuppositions n=3400; ethical-setting n=3400; 10-17 material charges per case; 7800 specimens total) using 14 turn-level axis-measurements spanning velocity, damage accumulation, frame-drift, brittleness, and direction stability, plus three speaker-resolved axes from an independent pipeline. The measurements are Hooke-coupled ($\sigma = E \cdot \varepsilon$ analog) and reproduce across loading cases with effects up to $|r_{rb}| = 0.35$ on debate; the sign structure adds a second pattern: the ethical-setting case inverts the velocity and accumulation blocks. Variance composition partitions into two profiles: debate is charge-dominated (brittle-fracture-like: the material grade decides), false-presuppositions and ethical-setting are topic-dominated (creep-like: the load decides); the ratios (2.03 vs 0.13/0.17) are estimator-dependent, for debate even in direction. Cross-judge reliability (GPT-4o vs Haiku 4.5) shows debate scoring is judge-robust (Cohen's $\kappa = 0.88$) while false-presupposition scoring is judge-sensitive ($\kappa = 0.36$) -- a caveat single-judge benchmarks must report. This is the methodological move Ye et al.'s diagnosis calls for: a multi-axis characterization that does not depend on which surface form of the construct one privileges.

---


### 432. [Entropy-Gated Latent Recursion](https://arxiv.org/abs/2606.16620)

**<font color=#1a73e8>作者：</font>** Soham Bhattacharjee, Dushyant Singh Chauhan, Salem Lahlou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inference-time scaling has become the dominant lever for improving language-model reasoning, but existing methods derive rollout diversity from a single source: stochastic token-level sampling. We argue that this single-axis sampling space is fundamentally limiting, and identify a second, fully deterministic and complementary axis: the layer span $L$ at which a frozen model's top decoder layers are recursively re-applied at high-uncertainty tokens. Different choices of $L$ produce distinct rollouts that solve different subsets of problems, with no stochasticity. We instantiate this axis through Entropy-Gated Latent Recursion (EGLR), a training-free decoding procedure that re-applies the top-$L$ layers for at most $K_{\max}$ iterations until the next-token distribution converges. Combined with $T$ temperature samples, EGLR turns a single-axis stochastic rollout pool into an $L\times T$ Cartesian sampling space at almost the same per-rollout cost. We characterize this space across $8$ instruction-tuned models and $6$ math reasoning benchmarks, and show that the $L$-axis is genuinely complementary to temperature: on MATH-500 with Qwen2.5-3B-Instruct, the joint $L\times T$ oracle reaches $91.6\%$, $+8.2$ percentage points beyond the temperature-only oracle ($83.4\%$) and $+10.4$ points beyond the layer-only oracle ($81.2\%$), confirming that the two axes capture genuinely complementary problems. The expanded rollout pool provides richer per-prompt candidates for any downstream procedure that consumes rollouts, including self-consistency, best-of-$N$ with verifiers, and group-relative RL training (GRPO), opening a new direction for inference-time scaling that does not rely on stochastic noise.

---


### 433. [MR-GVNO: A Geometry-Aware Variational Physics-Informed Neural Operator for Mindlin-Reissner Plates on Irregular Domains](https://arxiv.org/abs/2606.16624)

**<font color=#1a73e8>作者：</font>** Siqi Wang, Daobo Sun, Yizheng Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Plate and shell structures are widely used in engineering, making rapid response prediction under varying geometries, materials, and loads highly desirable. However, conventional finite element methods require repeated modeling and solution, resulting in high computational costs. This study proposes a geometry-aware variational neural operator for Mindlin-Reissner plate problems, termed MR-GVNO. The method uses boundary point clouds to represent irregular geometries and employs separate encoders for spatially varying material fields, pressure loads, and scalar physical parameters. A cross-attention mechanism integrates these inputs with query point information to predict transverse deflections and rotations at arbitrary locations. MR-GVNO is trained without labeled solution data using a variational physics-informed loss derived from the discretized total potential energy. It directly processes irregular point clouds and allows different physical fields to be discretized independently, avoiding interpolation onto a common grid. Numerical experiments on single-hole, double-hole, and L-shaped plates demonstrate accurate response prediction under homogeneous and heterogeneous materials and uniform and random loads. The model also achieves millisecond-level full-field inference and favorable cross-geometry generalization.

---


### 434. [Using AI in engineering education: a balancing act, driven by clear purpose](https://arxiv.org/abs/2606.16626)

**<font color=#1a73e8>作者：</font>** Olya Kudina  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Based on a questionnaire of 100 higher-education students, predominantly from engineering-related fields, and a critical review of recent literature, this chapter examines how students use and perceive Large Language Models (LLMs) in engineering education. Students primarily value LLMs for writing support, conceptual clarification, coding assistance, and brainstorming, while simultaneously expressing concerns about inaccuracies, bias, overreliance, academic integrity, and the burden of verification. Through an analysis of two dominant metaphors, namely LLMs as an "oracle" and as a "tutor," the chapter shows how these systems cultivate expectations of authority, expertise, and personalized learning that often exceed their actual capabilities. The chapter further argues that students' attachment to the promises of efficiency and personalized support reflects a form of "cruel optimism," where the perceived benefits of LLMs often depend on the very skills, vigilance, and expertise that students are still developing. Overall, the chapter argues for a purpose-driven and context-sensitive approach to AI integration in engineering education, emphasizing critical AI literacy, reflective assessment design, pedagogical caution, and consideration of broader ethical and environmental impacts.

---


### 435. [DCP-Prune: Ultra-Low Token Pruning with Distribution Consistency Preservation](https://arxiv.org/abs/2606.16633)

**<font color=#1a73e8>作者：</font>** Xifeng Xue, Xiaokang Wang, Zirui Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent vision token pruning methods effectively preserve model performance under moderate token budgets but become unstable under ultra-low token budget. Our analysis shows that as the pruning budget decreases, accuracy degradation is often accompanied by larger feature distribution shifts. Critically, the degree of this distribution shift strongly correlates with performance degradation. To better characterize this phenomenon, we introduce a lightweight distribution consistency metric to estimate the distribution shift between retained and full tokens. Motivated by these observations, we propose a two-stage pruning framework consisting of Anchor-Context Graph Recovery (ACGR) and Text-Aware Token Cluster Selection (TATCS). Specifically, ACGR transfers contextual information before token removal, while TATCS dynamically re-selects representative tokens when severe distribution shift is detected. Extensive experiments demonstrate that our method achieves superior and more stable performance under ultra-low token budget. Notably, it retains 92.1% of the upper-bound average performance on LLaVA-1.5-7B with only 16 visual tokens.

---


### 436. [MVM-IOD: An Industrial Object-Centric Benchmark Dataset for the Evaluation of 3D Reconstruction Methods](https://arxiv.org/abs/2606.16638)

**<font color=#1a73e8>作者：</font>** Robert Langendörfer, Markus Hillemann, Markus Ulrich  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D object reconstruction, and camera pose estimation in industrial applications are challenging tasks, as errors are costly while the computation time is often limited. The complexity of typical industrial objects further complicates these tasks. Most of the existing datasets in this context do not depict realistic industrial scenarios. Therefore, we introduce the Machine Vision Metrology Industrial Object Dataset (MVM-IOD). Images of typical industrial objects are captured systematically, by moving a camera, mounted at the end effector of an industrial robot arm, on a hemisphere around the objects. MVM-IOD contains reference camera poses and reference 3D point clouds, the acquired RGB images of 9 objects and 2 background choices resulting in 18 scenes, which allows evaluation of all image based methods that compute a 3D reconstruction, camera poses, or novel views of a scene. Based on MVM-IOD, we extensively evaluate current SOTA 3D reconstruction and camera pose estimation methods, such as Structure from Motion, Multi-View Stereo, recent feed forward methods (Visual Geometry Grounded Transformer, {\pi}3), and 2D Gaussian Splatting and report our findings as a baseline for future research. The experiments show that capture setups like ours generate out-of distribution images for feed forward methods, leading to suboptimal point clouds and camera poses. However, these out-of-distribution images can be shifted closer to the training distribution by applying simple preprocessing steps. Consequently, in certain industrial applications, feed forward methods should be used with caution.

---


### 437. [SPICE: Synergy and Partial Information Based Curriculum Evolution](https://arxiv.org/abs/2606.16639)

**<font color=#1a73e8>作者：</font>** Ankush Pratap Singh, Houwei Cao, Yong Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal learning exploits complementary information across heterogeneous modalities. The informativeness of each modality can vary widely across samples and training stages. Existing multimodal curriculum learning strategies often assume that the relative complexity of samples remains unchanged throughout training and therefore cannot adapt to model evolution. We propose SPICE (Synergy and Partial Information based Curriculum Evolution), a novel progressive curriculum framework for multimodal interaction learning. Guided by Partial Information Decomposition (PID) theory, our approach decomposes multimodal interactions into redundant, unique, and synergistic information components, enabling an interpretable and dynamic characterization of sample complexity. Building on this decomposition, we design a progressive curriculum that evolves throughout training, allowing the model to transition from learning shared cross-modal cues to modality-specific patterns and, finally, to complex synergistic interactions. Adapting to model evolution, sample ordering is refined in real-time using PID information estimates derived from unimodal and multimodal predictions. Experiments across multiple multimodal benchmarks demonstrate consistent improvements over conventional training and state-of-the-art baselines, highlighting the effectiveness of PID information decomposition and adaptive sample ordering for multimodal curriculum learning.

---


### 438. [SoK: Taxonomizing the Low-Level Attack Surface of Modern Web Browsers](https://arxiv.org/abs/2606.16646)

**<font color=#1a73e8>作者：</font>** Han Zheng, Qinying Wang, Qiang Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The web browser remains one of the most exposed remote attack surfaces on end-user systems, and memory-corruption flaws continue to play a central role in real-world browser exploitation. Despite a decade of intensive browser testing and bug-disclosure efforts, the community still lacks an explicit, defense-oriented systematization of the browser's low-level attack surface. Prior SoKs have surveyed browser vulnerabilities and mitigation techniques. However, these perspectives remain fragmented, leaving open a central question: how is the low-level attack surface of modern web browsers structured, and which parts of this surface remain underexplored by existing security testing?
We approach this primary question through three sub-questions. (RQ1) How is the browser's attack surface structured along input classes and components? (RQ2) Where do memory corruption vulnerabilities arise within this taxonomy? (RQ3) What do these attack-surface patterns imply for existing browser security testing? To answer RQ1, we derive an architecture-grounded Input x Component x Privilege taxonomy that abstracts the architectures of browsers into a unified view. To answer RQ2, we map 2,233 memory corruption reports disclosed between 2016 and 2025 onto this taxonomy. To answer RQ3, we overlay a decade of academic browser fuzzers, classified by the targeted input class, onto the bug-density map. Our systematization reveals that current testing concentrates on well-explored components while bug-dense, high-impact surfaces remain insufficiently tested. Moreover, we identify three fuzzer deployment gaps, which are orthogonal to the academic efforts. Our work offers a structured foundation for future browser security research.

---


### 439. [Mapping the Design Space for Youth Social Media: A Framework Centered on Friendship Building](https://arxiv.org/abs/2606.16651)

**<font color=#1a73e8>作者：</font>** JaeWon Kim  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This dissertation develops a design framework for friendship-supportive youth social media. I conducted a qualitative meta-analysis across my formative, case-study, and co-design work with teens and young adults, synthesizing recurring design themes into three pillars: social understanding (legible norms, intentions, trust, reciprocity, and accountability), placeness (spatial and embodied affordances that make online interaction feel inhabitable), and identity alignment (authentic expression that remains current, plural, and interpretable). The framework is grounded in interpersonal, developmental, and sociotechnical theory, but its contribution is design-oriented: it translates broader accounts of friendship and social development into the specific ways social media platforms can shape youth friendship building. I initially validate parts of this framework through WhoamI Today (WIT), a platform deployed with 99 youth across the United States and Korea. My proposed work extends this validation through a follow-up deployment while refining the framework as a roadmap for cumulative design research on youth social media.

---


### 440. [Distribution Alignment for One-Shot Federated Learning via Optimal Transport](https://arxiv.org/abs/2606.16655)

**<font color=#1a73e8>作者：</font>** Daniele Berardini, Vito Paolo Pastore, Vittorio Murino  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> One-Shot Federated Learning (OSFL) addresses extreme communication regimes in which clients interact with the server only once, amplifying the impact of heterogeneous client data distributions. In particular, the interaction of domain shift and label shift across clients induces misaligned feature representations that cannot be corrected through iterative optimization. Existing OSFL methods rely on distillation, server-side generation or ensemble-based aggregation, but assume aligned representations or address domain and label shift separately. We introduce SLOT-Align (Single-round, Learning-free Optimal Transport Alignment), a geometry-aware feature harmonization framework for OSFL. SLOT-Align uses a shared frozen encoder to extract compact feature statistics, constructs a global reference via Bures-Wasserstein barycenters, and aligns local representations using closed-form geodesic optimal transport maps. The method is computationally efficient and can be combined with existing OSFL pipelines relying on frozen encoders without modifying their training procedures. Extensive experiments across multiple benchmarks, pretrained backbones, and OSFL methods show that SLOT-Align consistently improves accuracy and robustness under joint domain and label shift.

---


### 441. [Near-Optimal Stochastic Linear Bandits with Delay](https://arxiv.org/abs/2606.16656)

**<font color=#1a73e8>作者：</font>** Ofir Schlisselberg, Mengxiao Zhang, Yishay Mansour  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study stochastic linear bandits with delayed feedback under several delay models and establish near-optimal regret guarantees. Our results identify when delayed linear bandits exhibit the same qualitative behavior as multi-armed bandits (MAB), and when the linear structure creates fundamentally new challenges. Specifically, (1) for \emph{loss-independent delays}, where the delay does not depend on the realized loss (but potentially depends on the arm), we show that delays incur only an additive regret penalty. Under stochastic delays, this penalty scales with the expected delay, while under adversarial delays, it scales with the maximum number of outstanding observations. Notably, both delay penalties are dimension-free, improving upon the state-of-the-art results; (2) for \emph{loss-dependent delays}, we show that linear bandits are substantially harder than MAB: unlike in MAB, we prove matching (up to log factors) upper and lower bounds in linear bandits, whose delay penalty depends on the square root of the dimension. (3) for the \emph{delay-as-payoff model}, a special case of loss-dependent delay, we show that the optimal MAB guarantee, which depends only on the delay of the optimal arm, is also unattainable in linear bandits. Together, these results provide a sharp characterization of how delayed feedback interacts with linear generalization.

---


### 442. [Beyond Defensive Reporting: Machine Learning for Active Anti-Money Laundering Control in Insurance](https://arxiv.org/abs/2606.16663)

**<font color=#1a73e8>作者：</font>** Dara Goldar, Geir Kjetil Ferkingstad Sandve, Martin Jullum  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Money laundering through insurance claims poses a threat to insurers both through fraudulent payouts and reputational and regulatory risk. Despite this, little research has examined how such laundering can be prevented. This paper examines whether machine learning can help insurers flag suspicious claims before payout, shifting the focus from passive reporting to active prevention. Using production data from a major Norwegian insurer, we train gradient-boosted decision tree models to detect claims later reported to authorities for suspected money laundering. Because fraud and laundering may share behavioural patterns, we also examine whether insurance fraud labels can serve as an auxiliary training signal. We compare different learning setups using the Budget-Weighted Capture Rate, a metric introduced in this paper to measure how many laundering cases are captured when only a small share of claims can be manually reviewed. The results show that incorporating fraud-related investigation labels substantially improves laundering detection. The best-performing model captures nearly two-thirds of laundering cases within the top-ranked 2 to 6 percent of claims selected for investigation. To our knowledge, this is the first empirical study of machine learning for money laundering detection in insurance claims.

---


### 443. [Sinkhorn-CPD: Robust point cloud registration via unbalanced entropic optimal transport](https://arxiv.org/abs/2606.16672)

**<font color=#1a73e8>作者：</font>** Jin Zhang, Mingyang Zhao, Bing Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Coherent Point Drift (CPD) is widely used for rigid point cloud registration because of its soft correspondences and closed-form parameter updates. However, CPD's target-side marginal constraint forces every observation, including outliers, to receive exactly unit probability mass. This assumption degrades registration accuracy under heavy outliers and partial overlap. Optimal transport (OT) methods can handle missing mass through unbalanced formulations, but require hand-tuned annealing schedules. In this paper, we propose Sinkhorn-CPD, which replaces CPD's target-side marginal constraint with dual Kullback-Leibler penalties, allowing the algorithm to discard outliers on both sides. The resulting formulation is a fully unbalanced entropic optimal transport problem, which can be efficiently solved by generalized Sinkhorn iterations. Moreover, Sinkhorn-CPD preserves the closed-form Procrustes and variance updates of CPD. In our method, the variance sigma^2 plays the role of the entropic regularization parameter, which induces an automatic annealing schedule from diffuse to sharp correspondences without manual temperature tuning. Experiments on synthetic, cross-category, and scan-to-CAD benchmarks show that Sinkhorn-CPD achieves state-of-the-art accuracy, with strong robustness to outliers and partial overlap.

---


### 444. [MMDiff: Extending Diffusion Transformers for Multi-Modal Generation](https://arxiv.org/abs/2606.16673)

**<font color=#1a73e8>作者：</font>** Yagmur Akarken, Orest Kupyn, Christian Rupprecht  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion transformers have demonstrated remarkable generative capabilities, yet the rich perceptual representations computed across their denoising trajectory are discarded once the content is rendered. We present MMDiff, a framework that transforms a frozen diffusion transformer into a multi-modal generative system that jointly produces images alongside any combination of dense perceptual modalities using lightweight decoder heads. Our central finding is that perceptual information is temporally distributed along the denoising trajectory, and that multi-timestep feature fusion with spatially varying aggregation weights is essential, improving semantic segmentation results by up to 28.7% mIoU over single-timestep extraction. We further adopt concept-driven attention extraction for interpretable spatial guidance, and show that frozen diffusion features are competitive with and complementary to state-of-the-art encoders such as DINOv3. By training only lightweight decoder heads on a frozen backbone, we achieve strong performance in semantic segmentation, salient object detection, and depth estimation, and demonstrate that this framework enables effective synthetic data generation at scale.

---


### 445. [From Affect Prediction to Affect Forecasting: Evidence for Distinct Information Sources in Longitudinal Text](https://arxiv.org/abs/2606.16687)

**<font color=#1a73e8>作者：</font>** Sadia Noor, Seemab Latif, Raja Khurram Shahzad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modeling dimensional affect in longitudinal text requires distinguishing current affect estimation from future affective change forecasting. Existing approaches often treat each text as an independent observation and apply similar assumptions to both tasks, without testing whether they rely on different information sources. This paper investigates that distinction using longitudinal self-reported ecological essays and feeling-word entries. We propose the Trait--State Affective Prediction (TSAP) framework and its temporal extension E-TSAP for per-text valence and arousal prediction, evaluated on a held-out prediction test set of 1,737 entries from 91 users. We further propose the Affective Change Forecaster Hybrid (ACF-Hybrid) for next-step affective change forecasting, evaluated on a held-out forecasting test set of 46 users. For prediction, E-TSAP achieves composite Pearson correlations of 0.670 for valence and 0.449 for arousal. For forecasting, textual representations perform worse than compact numeric trajectory baselines: the text-inclusive model achieves only r=0.316 for valence and r=0.284 for arousal, whereas a simple prior-state baseline reaches r=0.615 and r=0.670, respectively. ACF-Hybrid, using dimension-specific numeric trajectory features, achieves r=0.659 for valence and $r=0.658$ for arousal. These results show that textual semantics support current affect prediction, whereas future affective change is better captured through prior numeric trajectory dynamics.

---


### 446. [Adaptive inference and function vectors in deep transformers](https://arxiv.org/abs/2606.16694)

**<font color=#1a73e8>作者：</font>** Ravin Raj, Gautam Reddy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers are widely used as a general-purpose substrate for learning complex correlations between a large collection of coupled variables, but their internal mechanisms have remained mysterious. We introduce a theory of a deep transformer as a mean-field interacting system that implements distributed inference, subject to constraints on communication, locality and depth. We show that such a system can exploit internal state representations ('function vectors') to infer a latent context variable at increasingly finer scales over its layers. In an in-context regression task, the theory predicts a non-trivial relationship between non-Gaussian, hierarchical structure in the latent context variable, and transformer depth. Predictions are tested using constrained linear attention transformers and demonstrate adaptive inference in deep architectures. Feedforward blocks and depth enable transformers to implement a much richer class of in-context learning algorithms than previously described.

---


### 447. [Multi-Turn Reflective Masking Elicits Reasoning in Mask Diffusion Models](https://arxiv.org/abs/2606.16700)

**<font color=#1a73e8>作者：</font>** Yanming Zhang, Yihan Bian, Jingyuan Qi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While reasoning on autoregressive (AR) models is often performed by chain-of-thought reasoning and reflection, their refinement of previous outputs still relies on fully sequential generation, even when only local edits are needed. In contrast, the masking mechanism in Mask Diffusion Models (MDMs) naturally supports explicit local edits on previous outputs, allowing selective refinement without discarding previous answers and generating another from scratch. While this property more closely aligns with how humans correct mistakes by iterative local refinement, existing MDMs do not support multi-turn masking and denoising. We propose Reflective Masking (RM), which elicits such an intrinsic reasoning capability in MDMs via lightweight post-training. RM provides a native test-time scaling, where an MDM iteratively revisits and revises its prior outputs based on evolving context. To exploit insights from previous turns like AR reasoning, we further introduce History Reference, a parameter-free mechanism that leverages intermediate denoising states during revision. Our approach requires no architectural changes and is easily applicable to existing MDMs. Across diverse tasks and modalities, including text generation, Sudoku, and image editing, Reflective Masking consistently outperforms standard masking-based baselines and demonstrates strong generality, positioning RM as a fundamental primitive for reasoning on MDMs.

---


### 448. [User as Code: Executable Memory for Personalized Agents](https://arxiv.org/abs/2606.16707)

**<font color=#1a73e8>作者：</font>** Bojie Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A personalized AI agent needs a user memory: a persistent model of who the user is, built across many conversations and consulted on each new one. Today this memory is almost always stored as unstructured text, a knowledge graph, or a flat store of facts, and consulted by retrieval -- fetching the entries most similar to the current request. Such "bag-of-facts" memory recalls individual facts well, but because storing a fact and acting on it are separate steps, it struggles to resolve contradictions, aggregate over many records, or enforce rules. We argue that user memory should instead be executable. We introduce User as Code (UaC), a paradigm in which an agent's model of a user is a living software project: typed Python objects hold the user's state and ordinary Python functions encode the rules that govern it, so representing and reasoning about the user happen in one medium an interpreter can run. The enabling mechanism is a two-phase pipeline: an append-only log that never discards a fact, periodically checkpointed into typed code.
This changes what memory can do. On standard long-term conversation benchmarks, UaC matches both a full-context upper bound and the strongest prior memory systems on recall (78.8% on LOCOMO). Its advantage emerges where representation matters most. On aggregate questions over a user's history -- "how many international trips did I take last year?" -- retrieval-based memory collapses (6-43%) while UaC stays near-perfect (99%), because the answer is a one-line computation over typed state rather than a search over text. And because its rules execute deterministically whenever the state changes, UaC can surface unsolicited, safety-critical alerts -- such as a newly prescribed drug that conflicts with an allergy recorded months earlier -- a capability query-driven memory cannot provide.

---


### 449. [Misinformation Propagation in Benign Multi-Agent Systems](https://arxiv.org/abs/2606.16710)

**<font color=#1a73e8>作者：</font>** Jonas Becker, Jan Philip Wahle, Terry Ruas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems, in which multiple large language model agents solve problems through turn-based interaction, are increasingly deployed in high-stakes settings such as medical diagnosis, legal analysis, and forensic decision-making. Their reliability can be at risk when single agents reason from incorrect or misleading context, e.g., from tool calls, since errors may propagate through agent interactions. This work studies this risk by injecting intent-based misinformation into benign single-agent and multi-agent systems across reasoning, knowledge, and alignment tasks. We find that misinformation can degrade single-agent performance and persists across multi-agent debate, with agents often retaining answers introduced by misinformed peers. Nevertheless, multi-agent debate reduces the resulting performance degradation compared to single-agent prompting, especially when most agents are not exposed to misinformation. Robustness depends on group composition and decision protocol. Consensus can be more stable than voting under peer pressure, while majorities can often steer misinformed agents back toward correct answers. Our results show that misinformation robustness in multi-agent systems depends on the underlying model and also on how agents exchange information and aggregate decisions.

---


### 450. [From Third-Party to First-Party: Measuring and Protecting Against Modern Web Tracking Mechanisms](https://arxiv.org/abs/2606.16720)

**<font color=#1a73e8>作者：</font>** Christian Böttger, Tareq Khouja, Norbert Pohlmann 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Web user tracking has always been a cat-and-mouse game between privacy-conscious users and trackers. Recently, this conflict has driven a shift from third-party tracking toward first-party tracking (FPT) and server-side tracking (SST). By relocating tracking logic to the browser's first-party context or the website's backend, these mechanisms obscure data flows and render traditional client-side detection tools increasingly ineffective. Despite the growing adoption of these techniques, our understanding of their deployment at scale remains limited, and generalized protection mechanisms are lacking.
In this work, we conduct a large-scale measurement of top sites to assess this shift and the prevalence of FPT and SST. We develop a provider-independent methodology to detect these mechanisms and find that over 54% of analyzed sites now deploy FPT or SST-related techniques. By clustering scripts based on their similarity and constructing a network graph, we demonstrate that the ecosystem is densely connected and dominated by major vendors like Google. Finally, we demonstrate that current filter lists are largely ineffective against first-party tracking, and we propose new rules to address this gap. We show that these rules block 63% more requests than traditional filter lists.

---


> [!TIP]
> 当前位于：**401-450**（第 9/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-509](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
