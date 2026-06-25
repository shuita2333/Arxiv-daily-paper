# 📦 其他研究 | 2026年06月26日

> 本类共 **222** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-222](./part-05.md)

---

### 101. [Stagnant Neuron: Towards Understanding the Plasticity Loss in Multi-Agent Reinforcement Learning Value Factorization Methods](https://arxiv.org/abs/2606.25335)

**<font color=#1a73e8>作者：</font>** Zhengzhu Liu, Zeming Gao, Haoyuan Qin 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-Agent Reinforcement Learning (MARL) value factorization methods can suffer from a loss of plasticity, gradually failing to adapt when transferring to new task instances. We trace this issue to stagnant neurons, units whose gradient updates become negligibly small relative to their weights, thereby hindering learning. While existing plasticity injection methods exist, they prove ineffective for such neurons. To address this, we propose Knowledge-retentive Neuron-level PlastIcity Focusing InjEction (KNIFE), a novel method that directly targets stagnant neurons. KNIFE replaces each stagnant neuron with a composite unit comprising three specialized components: a frozen knowledge neuron to preserve acquired knowledge, a re-initialized active neuron to restore learning capacity, and a compensation neuron to ensure the combined output matches the original, thus maintaining previous learned cooperation knowledge. Extensive experiments on SMACv2, predator-prey, and matrix games demonstrate that KNIFE significantly outperforms state-of-the-art plasticity injection methods.

---


### 102. [Invoice Haystack: Benchmarking Document Retrieval and Visual Question Answering Under Strong Visual Homogeneity](https://arxiv.org/abs/2606.25343)

**<font color=#1a73e8>作者：</font>** Heethanjan Kanagalingam, Thenukan Pathmanathan, Mokeeshan Vathanakumar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Language Models have achieved near-human performance on single-document Visual Question Answering, yet their effectiveness degrades significantly when retrieving information from large collections of visually homogeneous documents. Existing multi-document benchmarks aggregate diverse document types, creating artificial separation in embedding space that does not reflect enterprise document repositories where thousands of records share identical visual templates. We identify this as embedding collapse and introduce Invoice Haystack, a benchmark with 1,500 anonymized invoice images paired with 200 discriminative question-answer pairs, specifically designed to stress-test retrieval under strong visual homogeneity. Invoice Haystack exhibits a mean pairwise cosine similarity of 0.73, compared to 0.38 (DocHaystack) and 0.31 (InfoHaystack) in existing benchmarks, posing a fundamentally more challenging retrieval problem. Addressing the identified challenge, we propose VL-RAG, a hybrid retrieval-augmented generation framework that jointly leverages text and visual embeddings to harness the complementary strengths of both modalities, followed by a VLM-based verification filter for precise document identification. VL-RAG achieves 60.0\% Recall@1 on Invoice Haystack-500, outperforming existing state-of-the-art method by up to an absolute 13.5 percentage points. It further improves retrieval considerably on DocHaystack-1000 (77.1\% vs.\ 75.2\%) and InfoHaystack-1000 (84.5\% vs.\ 80.0\%), establishing the proposed dual-stream fusion as a consistently superior retrieval strategy across both homogeneous and heterogeneous document collections.

---


### 103. [Follow Your Track: Precise Skeleton Animation Controlled by 3D Trajectories](https://arxiv.org/abs/2606.25344)

**<font color=#1a73e8>作者：</font>** Yueting Liu, Yanqin Jiang, Nian Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 4D generation aims to animate 3D objects with realistic motion, holding great promise for applications. Existing methods typically decouple 3D asset generation from motion synthesis: acquire a 3D asset, prepare a structural representation like mesh and Gaussians, and synthesize motion from text or video control signals. However, dense mesh and Gaussian representations incur high computational costs and are prone to temporal artifacts, limiting animation quality and duration to only short clips. Meanwhile, text lacks fine-grained spatial and temporal details such as timing and coordination, while video entangles motion with appearance and background. Together, these limitations result in 4D animations that suffer from poor temporal consistency, wrong identification, and limited controllability. We address these issues with \texttt{ACT}, a trajectory-conditioned framework for topology-general skeletal animation. ACT uses skeletons as a compact structured and compute-efficient representation and 3D point trajectories from monocular video as explicit motion guidance which provide detailed motion patterns without appearance entanglement. At the core of ACT is a Routed Trajectory Injector, which achieves accurate and robust trajectory-to-joint transfer through three complementary designs: prior-guided hard routing establishes precise skeleton-to-mesh correspondences, global routing enables holistic joint-track interaction for full-body motion awareness, and local windowed cross-attention enforces fine-grained temporal alignment, improving micro-timing and reducing motion misalignment across varying motion rates. Extensive experiments demonstrate that \texttt{ACT} significantly outperforms existing methods in fidelity and temporal consistency.

---


### 104. [Geometry-Anchored Transport Framework for Exemplar-Free Class-Incremental Learning](https://arxiv.org/abs/2606.25347)

**<font color=#1a73e8>作者：</font>** Hongye Xu, Bartosz Krawczyk  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Exemplar-free class-incremental learning (EFCIL) requires stable decision boundaries within a shifting feature space. While maintaining class-conditional Gaussian statistics provides a principled classification strategy, these parametric summaries remain sensitive to anisotropic representation drift. Existing methods often transport these statistics across tasks using a decoupled, post-hoc paradigm: optimizing a backbone without explicit geometric constraints can distort the legacy manifold, limiting the precision of retroactive alignment. In this paper, we formulate feature transport as an endogenous training constraint rather than a separate post-task step, presenting the Geometry-Anchored Transport Framework. First, we derive an Analytic Geometric Anchor via Mahalanobis-aligned regression to mitigate macroscopic anisotropic drift. Second, we introduce a Topology-Aware Evolution objective that regularizes localized manifold degradation while calibrating a residual network against the analytic prior. By coupling manifold evolution with transport constraints during the primary training phase, our framework mitigates evaluation errors without requiring decoupled fine-tuning. Experiments across CIFAR-100, TinyImageNet, and ImageNet-100 demonstrate that the proposed framework consistently improves upon existing post-hoc alternatives under strict exemplar-free constraints.

---


### 105. [General Techniques for Reducing Key-Switching Overhead in Privacy-Preserving Two-Party Transformer Inference](https://arxiv.org/abs/2606.25349)

**<font color=#1a73e8>作者：</font>** Wenshao Yang, Zhenhua Liu, Dongdong Yao  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In secure two-party Transformer inference, linear layers are typically evaluated using Fully Homomorphic Encryption (FHE) through plaintext-ciphertext or ciphertext-ciphertext matrix multiplications, where key switching primarily occurs and dominates computational overhead in both FHE-based and hybrid FHE-MPC systems. Existing optimizations rely heavily on packing-specific algorithms, limiting their general applicability.
Targeting this overhead from a packing-independent perspective, we propose a preprocessing-assisted method for secure attention computation. By decomposing attention into precomputable operations and online interactions, this method reduces online inference-phase key switching without modifying existing packing strategies.
However, the first method shifting key switching offline introduces additional storage requirements. To address this, we propose storage-communication trade-off techniques that replace large precomputed ciphertexts with modest online communication, enabling flexible deployment under varying resource constraints.
While ciphertext-ciphertext matrix multiplication is offloaded to the preprocessing phase in hybrid schemes and the first layer of FHE-based schemes, these operations still persist in the offline stage and subsequent FHE layers. To further optimize it, we propose a fused key-switch technique targeting the multiplication-followed-by-rotation pattern, which frequently arises in existing RNS-CKKS matrix multiplication schemes. By combining relinearization and rotation into a single procedure, this technique reduces the associated computation costs.
Analytical evaluations demonstrate that our proposed techniques significantly reduce online key-switch overhead and provide flexible trade-offs between storage and communication without requiring modifications to existing packing strategies.

---


### 106. [Compositional Behavioral Semantics for State Abstraction in Reinforcement Learning](https://arxiv.org/abs/2606.25357)

**<font color=#1a73e8>作者：</font>** Yivan Zhang, Ziyan Luo, Manuel Baltieri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> State abstraction plays a key role in scaling reinforcement learning to complex but structured systems. In studying such systems, a wide range of behavioral structures have been studied in reinforcement learning, including value functions, invariants, bisimulation relations, and behavioral metrics. However, a general principle for determining what structures are provably preserved under state abstraction is still lacking. In this paper, we present a unified framework for defining and analyzing behavioral structures in reinforcement learning. Our framework provides a compositional way to specify behavioral semantics based on local, one-step descriptions of system dynamics. Using this framework, we establish results showing how behavioral structures can be safely transferred between abstract and concrete systems. We further show how to construct quantitative metrics from logical behavioral semantics with soundness guarantees. Together, these results provide a principled foundation for reasoning about behaviors under state abstraction in reinforcement learning and offer reusable definition and proof principles for a broad class of behavioral structures in reinforcement learning.

---


### 107. [Memory Makes the Difference: Evaluating How Different Memory Roles Shape Conversational Agents](https://arxiv.org/abs/2606.25361)

**<font color=#1a73e8>作者：</font>** Yuxin Wang, Paul Thomas, Zhiwei Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prior research on memory mechanism in RAG-based conversational system has emphasized how memory is stored and retrieved. However, far less is known about how memories with different functional roles influence response quality. Specifically, how they shape an agent's responses under varying conversational contexts and whether they lead to substantively different response behaviors. Existing evaluations in conversational system are also largely reference-based, insufficiently capturing the nuances in responses that may address users' preferences differently. In this work, we probe the impact of different memory types in shaping agents' responses. We present a fine-grained taxonomy of conversational memory, classify retrieved memories into different role types, and design a user-centric evaluation framework that simulates user perspectives. Through comparative experiments on long-term datasets and frontier LLMs, our analysis reveal many differentiated effects of memories: e.g., clarifying memory improves responses' factual accuracy and constraint awareness, making them more correct and personalized; irrelevant memory reduces topic relevance and degrades constraint awareness. Despite the power of frontier LLMs, these findings shed light on how different memory types can be leveraged to produce more personalized responses and inspire further research in this direction.

---


### 108. [Neural Machine Translation for Low-Resource Tangkhul--English](https://arxiv.org/abs/2606.25365)

**<font color=#1a73e8>作者：</font>** Chormi Zimik Vashai, Agniva Maiti  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a study on low-resource machine translation for the Tangkhul-English (nmf-en) language pair. Tangkhul is a severely under-resourced Tibeto-Burman language spoken primarily in Manipur, India, with virtually no prior natural language processing infrastructure. We describe two systems: (1) a primary system based on ByT5-large fine-tuned on 38,336 Tangkhul-English parallel sentence pairs, and (2) a contrastive system based on mT5-small fine-tuned on the same corpus. Our primary ByT5-large system achieves a corpus BLEU score of 39.97, chrF++ of 58.07, BERTScore F1 of 0.8104, and COMET (wmt22-comet-da) of 0.7302 on a held-out test set of 3,856 sentences. We further discuss the orthographic challenges specific to Tangkhul's Latin-script diacritics, the domain bias of our training corpus (which comprises biblical text, stories, and conversational data), and avenues for future improvement through data diversification and domain adaptation.

---


### 109. [Three Buddhist Vocabularies: Computational Stylometry of the English Pali Canon across Sutta, Vinaya, and Abhidhamma](https://arxiv.org/abs/2606.25372)

**<font color=#1a73e8>作者：</font>** Joy Bose  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a computational stylometric analysis of the Tipitaka across all three Pitakas in English translation, extending earlier work on the Sutta Pitaka alone. The corpus spans 134,831 segments from Bhikkhu Sujato's Sutta Pitaka (114,591 segments, CC0), Bhikkhu Brahmali's Vinaya Pitaka (7,923 segments, CC0 2026), I.B. Horner's 1938 Vinaya translation (2,826 segments), three English translations of the Abhidhammattha Sangaha compendium (2,077 segments), and cross-tradition Vinaya texts from the Dharmaguptaka and Mulasarvastivada schools. We compute Zipf rank-frequency distributions with OLS-fitted exponents, Moving Average TTR (MATTR-500), numeral-word density, and vocabulary overlap (Jaccard and Szymkiewicz-Simpson coefficients). Main findings: (1) all corpora show Zipf-consistent distributions (R2 > 0.989); the Vinaya is closest to ideal Zipf slope -1 and the Sangaha corpus deviates most, with 'consciousness' displacing grammatical particles at rank 8; (2) MATTR-500 shows the Sutta and Vinaya Theravada are nearly identical in lexical diversity (0.399 and 0.400), while the Sangaha corpus is genuinely more diverse (0.560), confirmed by size-controlled subsampling; (3) the Sangaha corpus has the highest numeral-word density (3.26%), consistent with its systematic enumeration of mental and material categories; (4) the Mulasarvastivada Vinaya shares 20.0% vocabulary (Jaccard) and 49.1% (overlap coefficient) with the Theravada Vinaya, reflecting shared legal heritage across two millennia; (5) two English translations of the same Vinaya source text share only 24.2% of their vocabulary across 88 years, with 'musing' versus 'absorption' for jhana and 'defeat' versus 'expulsion' for parajika as the most diagnostic shifts. All results are point estimates; no significance testing is conducted. Code and data are released as open-source extensions to the Darshana Graph corpus (arXiv:2606.18222).

---


### 110. [What Actually Works for Spacecraft Fault-Tolerant Control: An Honest Settled-Gate Benchmark of Learned and Classical Methods](https://arxiv.org/abs/2606.25374)

**<font color=#1a73e8>作者：</font>** Alireza Shojaei  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent learned fault-tolerant-control (FTC) work reports high success on spacecraft actuator faults, but often in simulation, on narrow fault sets, and with transient metrics that a trajectory need only touch once. We ask what recovers spacecraft pointing when success means holding it on faults never seen in training. We answer with a benchmark built around a settled gate, pointing held within 0.2 deg over a dwell window and scored on the true state, train/test splits disjoint in inertia, gain, sign pattern, and bias, Wilson intervals over n=500 episodes per cell, and one-command reproduction on a 6-DOF Basilisk testbed. Across classical, adaptive, learned end-to-end, and structured controllers, three findings stand out. Fault-unaware PD/PID and from-scratch end-to-end RL score 0%, so learning capacity alone is not the lever. Classical adaptive laws resolve sign faults but handle gain poorly at 55.2%, and a literature-faithful Nussbaum-gain law reaches 45.2% and 3.2%. A structured estimate-then-control design, with a learned recurrent module that infers actuator gain online and feeds an analytic law, wins on sign and gain faults at 97.8% and 94.4%, approaching the privileged oracle while unstructured methods remain at zero. The hard wall is constant additive bias, which is 0% for every controller including the privileged gain oracle, because an integral-free law cannot null a constant disturbance. We close it with a disturbance observer that recovers bias from the dynamics and is self-correcting for gain-estimate error. Composed with the gain estimate, it recovers 59.4% of held-out bias faults with no sign/gain regression, moving that class off zero. We classify sensor-fault regimes similarly, show that sensor bias is unobservable from the corrupted measurement alone and therefore requires fusion rather than an observer, and release the benchmark so the gate is shared.

---


### 111. [Transferable Attack against Face Swapping in an Extended Space](https://arxiv.org/abs/2606.25376)

**<font color=#1a73e8>作者：</font>** Mingzhi Lyu, Yi Huang, Jun Xie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although deep Face Swapping (FS) models may benefit the entertainment industry, they pose severe threats to privacy and security. Existing protections, including deepfake detection and adversarial perturbation, are either passive responses or ineffective to unseen subject-agnostic FS models. In this paper, we propose a transferable attack against subject-agnostic FS models named Additive Identity attack based on a Relighting function (AIR). AIR leverages reillumination and additive perturbations to mislead the identity extraction modules in subject-agnostic FS models. By using these two types of perturbations simultaneously, the attack space is extended such that stronger but more visually natural adversarial examples can be identified. To further enhance the visual quality while preserving the effectiveness of the attack, an adaptive translation-invariant operation and an illumination control scheme are designed for AIR. Unlike other methods, AIR does not require a surrogate FS model to achieve high transferability. In addition, a mathematical proof is given for the extension of the attack space. Extensive experiments using 1000 image pairs across various state-of-the-art subject-agnostic FS models, including GAN and diffusion-based FS models, show that AIR surpasses all existing attacks in terms of both attack success rate and image quality.

---


### 112. [Story Operators: Decomposing the Original $\to$ Sequel Transformation in Embedding Space](https://arxiv.org/abs/2606.25379)

**<font color=#1a73e8>作者：</font>** W. Frederick Zimmerman  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> I treat a book as a point in a sentence-embedding space and a literary transformation as an operation on points. Given an original novel and its sequel, I ask what it takes, geometrically, to turn the first into the second. Using all-mpnet-base-v2 paragraph embeddings drawn from a precomputed index of the PG19 corpus, I form the displacement $d=\bar{x}_{\rm seq}-\bar{x}_{\rm orig}$ and greedily decompose it along a content basis obtained by PCA over the two books' own paragraphs. Each component is an interpretable axis anchored by real passages at its poles. Across thirteen verified author pairs from Project Gutenberg, the decomposition reveals a small taxonomy of sequels: formulaic (a tiny, low-rank change: Doyle's Holmes collections, $\|d\|=0.12$), concentrated (one dominant axis: Alcott's Little Women $\to$ Little Men, 75% on a single move), and compositional (many small axes: Twain, Burroughs's Barsoom, Nesbit). For the canonical case, Tom Sawyer $\to$ Huckleberry Finn, the dominant recovered axis is structural -- the collapse of sheltering domesticity into a picaresque road -- rather than the famous surface themes of vernacular voice or slavery, which ride later, smaller axes; and the transformation routes through adventure-journey space rather than diluting toward generic realism. I corroborate the recovered geometry against Twain's documented authorial intent (his 1875--76 letters to Howells), which names the first-person picaresque move years in advance, and I quantify, with an explicit representation caveat, how much of the realized transformation his stated intentions span. All computations are reproducible from the released scripts and data.

---


### 113. [Introducing corpora Hlava Cor and Hlava AD: Human Label Variation in Coreference and Discourse Relations](https://arxiv.org/abs/2606.25383)

**<font color=#1a73e8>作者：</font>** Anna Nedoluzhko, Šárka Zikánová, Jiří Mírovský 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As previous research on annotator disagreement in discourse phenomena has shown, understanding text coherence varies considerably from one individual to another. To explore this phenomenon, we created two corpora with multiple annotations of Czech texts, accompanied by annotators' explanations of their choices. The first corpus consists of 1,024 contexts annotated in parallel by three annotators. It captures differences in the identification of coreference across various text types and grammatical-semantic categories, including pronouns, full noun phrases, and anaphoric adverbials. The second corpus comprises 512 contexts, annotated in parallel by five annotators, and focuses on identifying discourse relations in attributive and non-attributive constructions. Both corpora achieve a comparable inter-annotator agreement of approximately 60-65%. For coreference annotation, agreement tends to be lower in cases where automatic coreference resolution models disagree, suggesting that when the models disagree, the examples tend to be more difficult or ambiguous for human annotators to interpret. The annotators' comments, both for coreference and discourse relations, further reveal differences in interpretation, varying levels of confidence in text understanding, and individual reading strategies.

---


### 114. [Offline Multi-agent Continual Cooperation via Skill Partition and Reuse](https://arxiv.org/abs/2606.25389)

**<font color=#1a73e8>作者：</font>** Yuchen Xiao, Lei Yuan, Ruiqi Xue 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Extracting skills from multi-agent offline dataset improves learning efficiency via sharing task-invariant coordination skills among tasks. In settings where tasks occur sequentially and the space of skills grows exponentially, existing approaches that rely on heuristically designed and fixed-sized skill libraries struggle to resolve the problem of distributional shift and interference, facing catastrophic forgetting and plasticity loss. To address this problem and endow agents with the ability to continually discover and reuse coordination skills in open-environment, we propose COMAD, a principled framework for Continual Offline Multi-agent Skill Discovery via Skill Partition and Reuse. We first discover skills from mixed multi-agent behavior data with an auto-encoder to transform coordination knowledge into reusable coordination skills. Then we construct a skill-augmented policy learning objective with multi-head architectures, explicitly guiding the advantage function with reusable skills identified via a density-based reusability estimator. Theoretical analysis shows our method approximates the optimum of a continual skill discovery problem. Empirical results across diverse MARL benchmarks show that COMAD continually expands its skill library to mitigate interference, achieving superior forward and backward transfer for task streams compared to multiple baselines.

---


### 115. [Anatomically-conditioned Latent Diffusion Model for Data-Efficient Few-Shot Cross-Domain 3D Glioma MRI Synthesis](https://arxiv.org/abs/2606.25390)

**<font color=#1a73e8>作者：</font>** Salman Shaik, Truong Thanh Hung Nguyen, Hung Cao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate classification of diffuse gliomas is often hindered by domain shifts across centers and a lack of large, annotated datasets. We propose the Anatomically-conditioned Latent Diffusion Model (ALDM), a novel framework for data-efficient, few-shot 3D volumetric MRI synthesis. ALDM utilizes a two-stage approach: a 3D variational autoencoder learns anatomical priors from a data-rich source domain, while a conditional latent diffusion model, guided by tumor masks via a ControlNet, generates structurally coherent volumes for a data-scarce target domain. Evaluated in an extreme few-shot setting with only 16 target images, ALDM outperformed GAN and hybrid baselines, achieving a superior Frechet Inception Distance (FID) of 85.40 and a downstream classification AUC of 0.987. Qualitative results confirm that the model preserves sharp pathology boundaries and cross-modal consistency, with visual fidelity improving progressively during training. By capturing essential diagnostic features, ALDM provides a robust tool for clinical data augmentation in low-resource settings. Our implementation is available at this https URL.

---


### 116. [FactorLibrary: From Polynomials to Circuits via Recursive Subgoals](https://arxiv.org/abs/2606.25394)

**<font color=#1a73e8>作者：</font>** Rohan Pandey, Michael Ruofan Zeng, Weikun K. Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Finding minimal arithmetic circuits for polynomials over finite fields is a combinatorially hard problem central to algebraic complexity theory. We formulate it as a reinforcement learning problem in two directions, bottom-up and top-down. To address the challenge of a fast-growing combinatorial search space, we introduce FactorLibrary, which stores factorizable subexpressions that serve as reusable subgoals across training episodes. We trained a bottom-up agent with Gumbel-PPO-MCTS and two top-down agents with PPO+MCTS and SAC. The PPO+MCTS top-down agent exhibited the most stable performance, finding certified optimal circuits up to complexity $8$ with a success rate of $91.8\%$.

---


### 117. [Long-Term Simulation Exposes Cognitive-Developmental Risks in AI Companions](https://arxiv.org/abs/2606.25396)

**<font color=#1a73e8>作者：</font>** Kaicheng Shen, Lingyu Li, Wen Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI companions powered by large language models increasingly interact with cognition-developing users, including children and adolescents, creating risks that may accumulate over time. Existing safety evaluations largely rely on single-turn or short-session tests, which cannot capture risks that emerge only through prolonged interaction. To address this gap, we propose TSJ (Theater-Stage-Judge), a longitudinal framework combining persona-driven user simulation, dynamic psychological-state updating and retrospective evaluation. We evaluate six mainstream models across four developmental stages, twenty-four risk dimensions and three psychological-vulnerability personas, covering 12,960 simulated person-day interactions. TSJ shows that short-horizon testing systematically underestimates developmental risks, for which TSJ yields a stable risk estimate only after 140 turns within prolonged simulated relationships. Applying TSJ further identifies early childhood and emerging adulthood as the most vulnerable stages, with cognitive trust and emotional dependency as the weakest domains. TSJ provides a scalable methodology for longitudinal cognitive developmental risk evaluation in AI companion systems.

---


### 118. [Teach-to-Reason: Competition-Guided Reasoning with a Self-Improving Teacher](https://arxiv.org/abs/2606.25407)

**<font color=#1a73e8>作者：</font>** Xiao Han, Hao Liu, Zhimin Bao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chest X-ray visual question answering (CXR VQA) requires models not only to predict correct answers, but also to produce reliable medical reasoning. However, existing reinforcement-learning-based training typically relies on answer-level rewards, which are often too coarse to improve chain-of-thought (CoT) quality and can become ineffective when group-level advantages collapse to zero. We propose \textbf{Teach-to-Reason (T2R)}, a framework that introduces comparison-based supervision into CoT optimization through a self-improving \emph{Teacher} and a competition-guided \emph{Reasoner}. As the Teacher is iteratively strengthened via self-competition, the Reasoner is optimized against progressively stronger Teacher-generated references. We further introduce a case-wise reward design that preserves the original reward-induced positive/negative partition when it is informative, and restores supervision from competition scores when the original reward signal degenerates. Experiments on multiple CXR open-ended VQA benchmarks show that T2R consistently outperforms strong baselines, indicating that comparison-based supervision, when integrated in a controlled and principled manner, provides a more effective training signal for reasoning optimization.

---


### 119. [DFMU: Data-Frugal Machine Unlearning](https://arxiv.org/abs/2606.25410)

**<font color=#1a73e8>作者：</font>** Sajith U, Prateek Keserwani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine unlearning is an emerging domain that ensures the safe removal of elements (includes concepts, attributes, entity and class) from the trained model along with least drop in model performance. The domain of machine unlearning brings its own indigenous challenges since the removal of pre-trained elements from model will always degrade the model performance on remaining elements. The existing methods basically rely on retraining for removal of elements from the pre-trained model, which is compute extensive. In this work, we propose a machine unlearning method which helps to reduce the computational requirement for faster retain-dataset accuracy convergence which also does not require extensive retraining of the pre-trained model. The proposed method, Data-Frugal Machine Unlearning (DFMU) requires only a single forward and backward pass for computing the importance score of various computational blocks of a model. The importance score computation is based on knowledge preserving pruning which helps to converge faster and requires far less data as compared to the existing methods. Experimentally, it achieves 40% more retain-accuracy with just 13% of data samples in comparison with SOTA method on various public datasets and also averages 88% faster processing time for forgetting a given class.

---


### 120. [Gastroendoscopy View Synthesis: A New Real Dataset and Evaluation](https://arxiv.org/abs/2606.25427)

**<font color=#1a73e8>作者：</font>** Masaki Minai, Yusuke Monno, Masatoshi Okutomi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Novel view synthesis (NVS) is an active research topic in computer vision, owing to the success of neural radiance field (NeRF) and 3D Gaussian splatting (3DGS) methods. While NVS opens the door to potential applications in gastroendoscopy, such as extending the field of view of endoscopic images and enabling digital twins for 3D archiving and endoscopist manipulation training, the dataset is insufficient to evaluate NVS for gastroendoscopy. In this paper, we present the first real gastroscopy dataset for NVS, namely the GastroNVS dataset, which contains a set of gastroscopic images, camera poses, and a point cloud for real gastroendoscopy inspection. To assess the suitability of the GastroNVS dataset, we evaluate several 3DGS methods and discuss the challenges for future development. The dataset is available on request from our project page.

---


### 121. [PRISM: Feed-Forward Single-Image 3D Reconstruction via Geometric Warp-Residual Modeling](https://arxiv.org/abs/2606.25430)

**<font color=#1a73e8>作者：</font>** Zhijie Zheng, Xinhao Xiang, Jiawei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing 3D scenes from a single image is a fundamental challenge in computer vision, with broad applications in virtual reality, robotics, and content creation. Recent methods achieve outstanding performance by leveraging camera-controlled video diffusion models, but rely on iterative diffusion sampling, which greatly limits their practical deployment. We observe that geometric forward warping alone can cover the majority of a target view directly from the input image, with only a compact residual left for the encoder to correct. Motivated by this observation, we propose PRISM, a feed-forward framework that decomposes multi-view latent prediction into a parameter-free geometric prior and a learned residual correction, with no diffusion sampling required at inference. To enable generalization from purely synthetic training data, we devise a two-stage training strategy combining latents supervised distillation for geometric generalization and perceptual fine-tuning for appearance quality optimization. Extensive experiments on three benchmarks demonstrate that PRISM achieves competitive reconstruction quality compared with diffusion-based methods, while reducing inference time dramatically to only 36 seconds per scene.

---


### 122. [Brevity is the Soul of Inference Efficiency: Inducing Concision in VLMs via Data Curation](https://arxiv.org/abs/2606.25432)

**<font color=#1a73e8>作者：</font>** DatologyAI, Matthew L. Leavitt, Siddharth Joshi 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inference efficiency is typically pursued by shrinking the model: distillation, pruning, quantization, and sparse routing each lower per-token cost while treating token count as fixed. But output length has been inflating, and it is precisely the component the standard toolkit leaves untouched. Here, we argue that brevity is the missing inference-efficiency lever, and that pretraining data curation is a practical way to pull it: a model trained on concise, correct data learns to answer in fewer tokens; i.e. it has a lower Cost-of-Pass. We apply our VLM curation pipeline to the MAmmoTH-VL single-image subset, and compare models trained on our curated data, the standard MAmmoTH-VL data, and external open-weight frontier VLMs. On a controlled 20-evaluation set and 14 VLMs at 1B-4B activated parameters, we hold output length fixed with a per-model regression, separating brevity from quality, and price models in FLOPs per correct answer. Curation buys a 35x Cost-of-Pass advantage over the most verbose 4B comparator (Qwen3.5-4B) within $\sim$1 pp of accuracy (0.41 vs 14.58 TFLOPs per correct answer; 0.691 vs 0.704 mean accuracy). Curation also buys a +17.55-percentage-point matched-length accuracy gain over the uncurated baseline that grows with model scale (from +16.7 pp at 1B to +21.2 pp at 4B). This brevity improvement concedes no quality: generic verbosity buys no accuracy at any capability or scale, and the window where reasoning-structured verbosity still earns its tokens shrinks from 4 of 8 capability groups at 2B to 1 of 8 at 4B. Per example, the concise model even reaches correct answers the verbose reasoning model misses, marking reasoning as a distinct curation target rather than something brevity gives up. Inference efficiency in this regime is a tokens-per-correct problem, and brevity is the lever that targets it directly.

---


### 123. [Interpretable Concept-Guided Polynomial Tabular Kolmogorov-Arnold Network for EEG-Based Mild Cognitive Impairment Detection](https://arxiv.org/abs/2606.25434)

**<font color=#1a73e8>作者：</font>** Yosef Bernardus Wirian, Qiang Cheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Early and scalable detection of mild cognitive impairment (MCI) remains an unresolved clinical challenge. Existing EEG-based screening approaches are constrained by handcrafted feature pipelines that discard neurophysiologically meaningful domain structure and deep learning classifiers that sacrifice interpretability for performance. No existing work unifies physiologically organized concept encoders, cross-concept interaction modeling, and nonlinear tabular classification in a sleep EEG-based MCI detection framework. This study proposes Concept-guided Polynomial-transformed Tabular learning using Kolmogorov-Arnold Network (CPTabKAN), which maps heterogeneous EEG-derived features into domain-informed concept representations, expands them via degree-2 polynomial transformation to expose first- and second-order interactions, and applies a Fourier-parameterized TabKAN classifier to learn nonlinear decision boundaries. CPTabKAN was evaluated on the Study of Osteoporotic Fractures cohort (372 subjects, overnight polysomnography), using 1,379 features organized into ten physiologically motivated concept groups. Under 10-fold cross-validation, CPTabKAN-Second Order achieved a weighted F1-score of 0.9038 (SD 0.034), outperforming GradientBoosting by 5.65 percentage points (t(9)=1.934,p=0.043, one-sided paired test), with advantages persisting under SMOTE-based balancing. Ablation analysis confirmed independent contributions from each component. Concept importance analysis revealed that power spectral density, multi-scale entropy, and Hjorth parameters dominated first-order weights, while cross-concept interactions involving Lempel-Ziv-Welch complexity, statistics, demographics, and slow oscillations exceeded all first-order scores. These results demonstrate that concept-structured, interaction-aware tabular learning surfaces physiologically coherent reasoning, supporting clinical trust.

---


### 124. [LinStereo: Linear-Complexity Global Attention for Multi-Scale Iterative Stereo Matching](https://arxiv.org/abs/2606.25437)

**<font color=#1a73e8>作者：</font>** Yiran Wang, Oliver Turner, Viorela Ila  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing Vision Foundation Model (VFM)-based iterative stereo pipelines under-exploit three information pathways: multi-scale backbone features are collapsed into single-level correlations, geometric priors remain untapped at initialization, and context propagates only locally. These gaps widen under degraded photometric cues, making underwater scenes a stringent generalization test. To address this, we propose LinStereo, built upon Depth Anything V3, whose core is a Position-Aware Linear Attention (PALA) module that replaces local recurrence with global aggregation at linear cost, propagating reliable estimates from well-matched regions into degraded areas while preserving disparity structure. PALA is made effective by two enabling components: Hierarchical Semantic Cost Volumes (HSCV), which supply scale-aligned correlations from the VFM feature hierarchy, and a Depth Prior Initialization (DPI) that converts monocular depth into a metrically calibrated warm start. LinStereo achieves state-of-the-art-level accuracy on standard benchmarks and strong cross-domain generalization, particularly on underwater scene where severe photometric degradation makes stereo matching particularly challenging, attaining the best overall accuracy with consistent gains 28% lower AbsRel on TartanAir-UW, 26% on SQUID, a real-world underwater dataset).

---


### 125. [TopoCast: A Topological Fidelity Framework for Evaluating Transformer-Based Time Series Forecasting](https://arxiv.org/abs/2606.25439)

**<font color=#1a73e8>作者：</font>** Sandeepa Weerasekara, Sandareka Wickramanayake  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning-based models have achieved state-of-the-art performance in Time Series Forecasting (TSF), yet their evaluation remains dominated by pointwise error metrics such as Mean Squared Error (MSE), which quantify numerical accuracy but overlook structural properties of the forecast signal, including recurrent dynamics, oscillatory behavior, and phase alignment. As a result, forecasts exhibiting over-smoothing, phase shifts, or frequency distortions may achieve favorable error scores despite substantial structural degradation. To address this limitation, we propose TopoCast, a topology-driven framework for evaluating structural fidelity in TSF. TopoCast reconstructs phase-space representations of forecast and ground-truth sequences using Takens delay embedding and applies persistent homology to characterize their intrinsic dynamics. We derive four complementary topological fidelity measures from persistence diagrams and aggregate them into a Topological Fidelity Score (TFS). We further introduce dominant cycle overlap, a novel metric that maps persistent topological features to the temporal domain to assess whether dominant oscillatory patterns occur at the correct time points. Combined with TFS, this yields the Localized Topological Fidelity Score (LTFS), a phase-aware measure that captures temporal localization errors invisible to existing evaluation metrics. Experiments on five Transformer architectures across three real-world benchmark datasets demonstrate that models with similar forecasting errors can exhibit markedly different structural fidelity profiles, revealing failure modes overlooked by conventional evaluation and highlighting the value of topology-aware forecast assessment.

---


### 126. [C3-Bench: A Context-Aware Change Captioning Benchmark](https://arxiv.org/abs/2606.25445)

**<font color=#1a73e8>作者：</font>** Jae-Woo Kim, Hyeongbeom Kim, Ue-Hwan Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Change Captioning systems have garnered substantial attention to respond to our evolving world, their true performance on diverse real-world change contexts remains largely unexplored due to the lack of comprehensive evaluation frameworks. To fill this gap, we propose C3-Bench, a comprehensive benchmark for evaluating Context-aware Change Captioning. C3-Bench features: (1) 4,996 human-labeled image pairs of 51 real-world change contexts across four domains (e.g., natural scenes, remote sensing imagery, image editing, and anomalies), each with diverse, carefully curated scenarios derived from multiple change-centric communities; and (2) the first LLM-as-Judge evaluation framework in the change captioning task that measure fine-grained dimensions (e.g., correctness, specificity, fluency, and relevance), along with a novel reversibility metric exploring whether models understand changes with symmetric consistency. Based on C3-Bench, we benchmark 32 models -- including conventional change captioning models, proprietary Large Multimodal Models (LMMs), and 2B-90B open-source LMMs. We reveal a fundamental blind spot in the prevailing change captioning paradigm: Once the change context departs from training-style regimes, conventional models collapse, and even state-of-the-art LMMs such as GPT-5.2 exhibit systematic domain- and position-dependent errors that distort reliable change understanding. By making these hidden failure modes explicit and measurable, we delineate the next frontier for building generalizable and trustworthy change captioning systems. All codes and datasets are publicly available on the project page.

---


### 127. [Reclaim Evaluation: A Lossy Memory Is Worse Than an Empty One](https://arxiv.org/abs/2606.25449)

**<font color=#1a73e8>作者：</font>** Alex Kwon  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A language model's memory can be worse than having no memory at all. Give a model a memory that kept a wrong conclusion but dropped the work behind it, and it emits that stale value as a confident answer; give the same model an empty memory and it abstains. Across seven models this direction never reverses, a clean kill condition that none breaks. We call this brittle memory: behavioral, not the near-immediate information bound beneath it; only its magnitude is disposition- and task-dependent, not its direction. We measure it with reclaim evaluation: compress a drifted interaction at a fixed budget, then test whether a correction recovers the known answer, scored against ground truth with no judge. Correctability is bottlenecked by whether the answer-determining source survives, not by capability. A one-line source-first policy (keep the recomputable source, drop the re-derivable conclusion) restores correctability at equal budget where that source is compact and identifiable; a length-matched control rules out added text as the cause. The hand-built oracle reaches 1.00; a one-prompt deployable version reclaims 0.49-0.88. The stake compounds: chained through a memory loop, a single dropped-source error corrupts a growing span of downstream steps and stays uncorrectable, while source-first holds to a bounded budget horizon. The wall and fix replicate across three deployed memory systems and on real dialogue (MultiWOZ), and past the budget where the source no longer fits, the fix fails silently unless the note records completeness. This is a controlled study of a mechanism, not a benchmark: judge-free exact scoring, matched-budget controls, and validators built to come out false. We release the harness, conditions, and validators.

---


### 128. [The Generalization Spectrum: A Chromatographic Approach to Evaluating Learning Algorithms](https://arxiv.org/abs/2606.25450)

**<font color=#1a73e8>作者：</font>** Jinghan Zhang, Zerui Cheng, Shiqi Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traditional evaluations measure a learning algorithm's final performance on an i.i.d. test set, reducing learning to a single aggregate score. This approach obscures a fundamental question: to what extent does learning from a specific example generalize to others? Such per-sample generalization, akin to learning by analogy in human cognition, captures how far the knowledge extracted from one example can transfer, yet remains invisible to standard benchmarks. We introduce the Generalization Spectrum, an evaluation framework designed to expose this hidden dimension. For each training example, we construct a controlled suite of test variants arranged by increasing transfer distance, from exact recall to implementation transfer across languages, context transfer under complete narrative re-framing, category-matched in-domain problems, and an unpaired baseline. By tracking performance across these distances, we reveal not just whether an algorithm learns, but how far that learning extends. We instantiate this framework on competitive programming, using a selection-and-synthesis pipeline seeded with recent problems to mitigate contamination. We first compare three canonical learning paradigms under matched memorization. RL converts memorization into near-transfer more efficiently than SFT-family baselines, while ICL exhibits strong but correspondence-dependent transfer. We then use the Spectrum to diagnose within-family variants. The resulting profiles show that local gains need not expand the generalization radius: abstractions and hints mainly lift local transfer, RFT preserves a stronger far-transfer tail than reference SFT, and self-distillation or hint-assisted RL can reduce far transfer even when local transfer or optimization improves.

---


### 129. [Learning with a Single Rollout via Monte Carlo Pass@k Critic](https://arxiv.org/abs/2606.25451)

**<font color=#1a73e8>作者：</font>** Fengdi Che, Yang Liu, Lei Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating token-level advantages in reinforcement learning (RL) for language models remains challenging because scaling up episodic experience collection is expensive. The difficulty intensifies for baseline advantage estimation methods, where repeated sampling causes trajectories to diverge into substantially different reasoning prefixes. In this context, RL algorithms such as GRPO prove limited: an outcome reward is too sparse to be attributed to specific actions like intermediate steps, and comparisons across sampled traces are non-trivial because they are heterogeneous. To mitigate both the computational cost of repeated sampling and the difficulty of credit assignment, we study single-rollout proximal policy optimization (SR-PPO) featuring token-level credit assignment in RL for language models. Instead of estimating advantages by normalizing episodic returns within the candidate group, we train a calibrated token-level credit critic using Monte Carlo outcomes from one rollout per prompt. Specifically, we use the critic to predict the Pass@k success probability at the prompt prefix, which is derived from a Pass@1 attempt. This choice yields a more selective learning signal than Pass@1: it discounts easily solved prefixes while prioritizing hard ones whose success probability remains marginal. We show that as $k$ increases, Pass@k converges to a reachability indicator, reflecting whether a prefix can lead to at least one successful continuation. In an explicit state graph, the limit ($k \rightarrow \infty$) can be computed in $O(|V|+|E|)$ time, offering a promising surrogate for direct credit assignment without the need to sample contrastive traces. As an initial validation, SR-PPO exhibits stable learning dynamics, along with consistent gains in Pass@128 success rates on mathematical reasoning benchmarks such as HMMT26 and AIME24.

---


### 130. [Towards Robust EEG Decoding Based on Riemannian Self-Attention](https://arxiv.org/abs/2606.25456)

**<font color=#1a73e8>作者：</font>** Shaocheng Jin, Tao Zhou, Rui Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Brain-Computer Interface (BCI) based on electroencephalography (EEG) enables direct interaction between the brain and external environments and has significant applications in assistive technologies, medical rehabilitation, and entertainment. Recently, EEG decoding methods based on Symmetric Positive Definite (SPD) learning have demonstrated superior performance. However, these methods typically employ basic network architectures and do not explicitly capture local relationships between EEG signals. This limitation is problematic for EEG signals due to their inherently low Signal-to-Noise Ratio (SNR). Moreover, most existing Riemannian manifold-based methods are restricted to specific metrics. The most widely used is the Affine-Invariant Metric (AIM). However, it has a quadratic dependency on the SPD matrices and cannot handle ill-conditioned SPD matrices, which hinders the effectiveness of networks. In contrast, the Bures-Wasserstein Metric (BWM) exhibits linear dependence on SPD matrices and demonstrates superior performance for ill conditioning. To overcome these challenges, we propose a Riemannian self-attention network based on the BWM. Additionally, the recently introduced power-deformed generalized Bures-Wasserstein metric reveals a nonlinear relationship between SPD matrices and matrix power deformation. This metric provides a more nuanced representation of the geometric structure of the SPD manifold. Consequently, we extend our model to a learnable version. For simplicity, we refer to it as GBWAtt. Experimental results on three EEG benchmarking datasets validate the robustness and effectiveness of our proposed method. The code is available at this https URL.

---


### 131. [Probing in the Wild: A Case Study of Self-Supervised Speech Representations on Mandarin Sub-dialects with Unsupervised Articulatory Analysis](https://arxiv.org/abs/2606.25459)

**<font color=#1a73e8>作者：</font>** Shu Shang, Fuliang Weng, Zeqian Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While self-supervised speech models have achieved strong performance across speech tasks, relatively little is known about how their internal phonetic representations behave under fine-grained dialect variation. Existing probing studies typically rely on curated corpora with manual phonetic annotations, limiting their applicability to naturally occurring dialect speech. We present a case study of articulatory feature representations in a Mandarin self-supervised speech model using an entirely unlabeled probing pipeline. Phone sequences are generated using a language-agnostic universal phone recognizer and mapped to articulatory feature vectors, enabling frame-level probing without manual annotation. Our results reveal a structured pattern in articulatory feature decodability across Mandarin sub-dialects. Acoustically salient features such as labiality and stridency remain comparatively stable, whereas features associated with finer spectral distinctions exhibit larger dialect-dependent variation. This variation is driven primarily by elevated decodability for Beijing speech relative to other Mandarin sub-dialects. Layer-wise analyses further show distinct representational dynamics for these feature groups. These findings suggest that language-agnostic articulatory probing can be applied to real-world dialect corpora and that dialect sensitivity in self-supervised speech representations is unevenly distributed across articulatory dimensions.

---


### 132. [Optimizing Abstractive Summarization With Fine-Tuned PEGASUS](https://arxiv.org/abs/2606.25462)

**<font color=#1a73e8>作者：</font>** Sadiul Arefin Rafi, Naimur Rahman, Kazi Nazibul Islam 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Abstractive text summarization is the technique of generating a short and concise summary comprising the salient ideas of a source text without making a subset of the salient sentences from the source text. The introduction of transformer models such as BART, T5, and PEGASUS has made this sort of summarization process more efficient and accurate. The objective of this paper is to fine-tune PEGASUS on the XL-Sum English corpus to achieve a better performance compared to the baseline mT5 model. The performance of the generated summaries from the fine-tuned model is evaluated using the ROUGE metric, which basically compares the auto-generated summaries with human-created summaries. To the best of our knowledge, the results from our fine-tuned PEGASUS model give a state-of-the-art performance on the XL-Sum English Corpus. To quantify the improvement, there is a 4.04% improvement in the ROUGE-1 score, a 15.25% increase in the ROUGE-2 score, and a 3.39% improvement in the ROUGE-L score from the baseline model.

---


### 133. [EchoStyle: Unlocking High-Fidelity Video Stylization with Reverse Data Synthesis](https://arxiv.org/abs/2606.25465)

**<font color=#1a73e8>作者：</font>** Huaqiu Li, Jiahao Wang, Sijia Cai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While image stylization has been studied extensively, video stylization remains a critical and largely unsolved challenge in the field of intelligent content creation. Existing methods, usually utilizing a reference image as the style prior, suffer from content leakage, data scarcity and limited adaptability to long videos, leading to suboptimal results with severe style drift and motion distortion. For these issues, we present EchoStyle, a scalable text-driven framework to achieve high-quality stylization of videos with arbitrary lengths. To start with, we construct a video-to-video architecture to appropriately re-fuse the video content and the text style. To address data scarcity, we pioneer an automatic reverse-synthesis pipeline to establish V-Style20k, a large-scale stylization dataset of 20k high-quality video pairs. To facilitate long video stylization, we devise an init-follow-mode mechanism along with a sliding-window inference strategy. Extensive experiments demonstrate EchoStyle's excellent performance across a wide range of artistic styles, even comparable to leading closed-source solutions.

---


### 134. [TACO: Towards Task-Consistent Open-Vocabulary Adaptation in Video Recognition](https://arxiv.org/abs/2606.25478)

**<font color=#1a73e8>作者：</font>** Minghao Zhu, Xiao Lin, Mengxian Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adapting CLIP for open-vocabulary video recognition necessitates a delicate balance between newly acquired video knowledge and the pretrained generalization. While existing studies pursue this generalization-specialization trade-off with additional regularizations or constraints, we argue that they overlook the deviation of representations beyond the fine-tuning data distribution, resulting in suboptimal adaptation effects. We believe such deviation is inherited from the inconsistency between the fine-tuning and evaluation objectives, where model optimization is restricted to the known training distribution but evaluated on unseen ones. In this paper, we introduce \emph{TACO}, a simple yet effective framework to mitigate the potential negative effects induced by this inconsistency. Our key insight is that adaptation should preserve OOD-relevant alignment beyond the training distribution. To this end, we propose \emph{Relative Structure Distillation}, which regularizes the relative geometry of the representation space and suppresses harmful alignment shift during training. We further decouple the representation space from the optimization space with a lightweight specialization projection, allowing task-specific adaptation without directly overspecializing the representations used at test time. \emph{TACO} establishes state-of-the-art performance on diverse benchmarks under cross-dataset and base-to-novel settings. Code will be released at this https URL.

---


### 135. [Rate-Aware Quantum-Inspired Trajectory Learning for Interference-Limited Multi-UAV Networks](https://arxiv.org/abs/2606.25480)

**<font color=#1a73e8>作者：</font>** Khaoula Khaled, Muhammad Afaq, Ali Arshad Nasir 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Unmanned aerial vehicle (UAV) can provide on-demand, high-capacity connectivity in disaster and normal situation. However, it faces a challenge of curse of dimensionality in trajectory optimization, where interference-limited environments and vast search spaces make real-time coordination computationally expensive. To overcome this challenge, we propose the Rate-Aware Quantum-Annealed Graph Condensation (RA-QAGC) scheme, which combines rate-aware graph abstraction with decentralized reinforcement learning to enable scalable, interference-aware UAV coordination. By identifying high throughput locations and guiding UAV trajectory adaptation toward throughput-optimal regions, RA-QAGC effectively balances network capacity by maintaining quality-of-service (QoS) requirements. Simulation results demonstrate the proposal outperformed over existing schemes by achieving 59.4 Mbps total throughput and 23.9 Mbps priority-user throughput, representing gains of approximately 15% and 34%, respectively, over the baseline schemes.

---


### 136. [Cross-View Variance Correlation in Path-Traced Stereo:A Hidden Shortcut in Synthetic Training Data](https://arxiv.org/abs/2606.25483)

**<font color=#1a73e8>作者：</font>** Po-Ting Lin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Path-traced synthetic stereo data underlie a large fraction of modern disparity-estimation training pipelines. We report a previously unrecognised property of such data: while the Monte Carlo (MC) noise streams of the two cameras are statistically independent, the underlying \emph{variance fields} -- deterministic per-pixel functions of the rendering integrand -- are highly correlated once aligned by the ground-truth disparity warp. Across 20 scenes rendered with Mitsuba~3, the warped Pearson correlation reaches $\rho{=}0.754{\pm}0.016$ across 20 scenes at $\mathrm{SPP}{=}512$, and on a representative scene remains essentially invariant ($\rho{=}0.778{\pm}0.001$) over a $16\times$ range of samples per pixel. The effect is strongest in Lambertian regions ($\rho{\approx}0.78$) and substantially weaker in glass ($\rho{\approx}0.30$), as predicted by an integrand decomposition into view-independent and view-dependent components. A residual-shuffle intervention that breaks the cross-view alignment while preserving the clean image degrades the GT cost margin by $33\%$ on non-glass and the variance-based winner-take-all accuracy on glass by $4.3\times$, confirming the structure functions as a matching cue. This signal is unique to MC-rendered data and constitutes a candidate sim-to-real shortcut whose impact on trained networks remains to be quantified.

---


### 137. [How Reliable Is Your Jailbreak Judge? Calibration and Adversarial Robustness of Automated ASR Scoring](https://arxiv.org/abs/2606.25487)

**<font color=#1a73e8>作者：</font>** Yang Gao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Almost every paper on LLM jailbreaks and prompt injection reports an attack-success rate (ASR), and that number is assigned not by people but by an automated judge: either a safety classifier trained for the task, or a general chat model prompted to grade. The judge is rarely checked. We check it. Using 596 human-labeled completions from the HarmBench classifier validation set, we compare the two judge families against human majority votes and then attack them. The two families fail in opposite ways. The dedicated classifier over-flags (precision 0.835, recall 0.974); three different LLM-as-judges keep high precision (0.81 to 0.94) but show erratic recall (0.06 to 0.65), so the same responses produce very different ASR depending on which judge scores them. The two families also differ sharply in robustness. Wrappers that leave the harmful text untouched and only add benign framing flip every LLM-judge between 57% and 100% of the time, and a single prepended refusal sentence accounts for much of this (39% to 88%). The dedicated classifier resists these surface attacks (at most 6.7%), but a white-box GCG attack on its open weights flips 70% of confident true positives (21 of 30; 95% CI 54 to 86%) even at a small optimization budget. A two-annotator audit confirms the attacks leave the harm intact: every one of 80 sampled flips still contained the harmful content. Because a large and growing share of reported ASR comes from LLM-judges, many such numbers are unreliable both on average and under deliberate pressure. We recommend that papers report judge precision and recall on a human-labeled slice, report ASR corrected for judge precision, and include an adversarial check of the judge. Our code is released.

---


### 138. [Distill on a Diet: Efficient Knowledge Distillation via Learnable Data Pruning](https://arxiv.org/abs/2606.25488)

**<font color=#1a73e8>作者：</font>** Yifan Wu, Yiqi Wang, Xichen Ye 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge Distillation (KD) is widely used to obtain compact models for efficient inference in resource-constrained environments. Yet the computational overhead of the distillation process itself is often overlooked, raising the question of whether a better student model can be obtained with less data and less compute via data pruning. However, existing data pruning methods are not designed for KD: some introduce substantial overhead, such as obtaining training dynamics through retraining, while others rely on heuristic selection rules that fail to capture what KD actually requires, often resulting in suboptimal subsets. To address these issues, we propose IF-Beta, an efficient data pruning framework that combines influence functions with a learnable sampling policy. Empirically, we first demonstrate that influence functions can serve as an effective and efficient estimator of sample impact in KD settings, where only a pretrained teacher is available. Building on this, our sampling policy is specifically parameterized by a Beta distribution, whose highly flexible two-parameter family allows the policy to adapt to diverse pruning regimes rather than being tied to fixed heuristic forms. Next, we formulate KD pruning as optimizing this policy through a bilevel objective, where the inner loop operates in the teacher feature space with a KD-aligned objective, enabling fast proxy training, while the outer loop updates the policy parameters to maximize distillation performance. This design ensures that IF-Beta is both computationally efficient and inherently aligned with the goals of KD. Extensive experiments on CIFAR-10/100 and ImageNet show that IF-Beta consistently outperforms other baselines across a wide range of pruning ratios. Remarkably, IF-Beta enables students trained on less data and less compute to surpass the performance of students distilled on the full dataset.

---


### 139. [HG-Bench: A Benchmark for Multi-Page Handwritten Answer-Region Grounding in Automated Homework Assessment](https://arxiv.org/abs/2606.25491)

**<font color=#1a73e8>作者：</font>** Chuangxin Zhao, Boyan Shi, Yanling Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated homework assessment depends not only on recognizing student answers, but also on accurately locating where each answer and each intermediate reasoning step appears in noisy, multi-page handwritten work. This paper addresses the missing evaluation setting of page-aware, two-level answer-region grounding: given a sequence of homework page images, a model must localize complete answer regions and their ordered step-level subregions. We introduce HG-Bench, a benchmark of 500 human-annotated K-12 homework samples curated from a 1,489,278-image source pool, with question-level and step-level boxes linked by a hierarchical containment constraint. HG-Bench is paired with a page-aware evaluation protocol that separately measures complete-answer localization (FA) and step-level decomposition (FSm), revealing whether models truly ground the spatial structure of student reasoning rather than merely parse visible text. Across frontier closed-source APIs and competitive open-weight VLMs, no zero-shot system exceeds 55.22% on FA or 48.22% on FSm, while a GLM-4.6V 9B reference model fine-tuned on ~10k in-domain examples reaches 74.97/72.26. These results identify step-level handwritten grounding as a concrete capability gap and provide a reproducible benchmark, evaluation protocol, and trained reference point for future work on automated homework assessment.

---


### 140. [Spam and Sentiment Detection in Arabic Tweets Using MARBERT Model](https://arxiv.org/abs/2606.25495)

**<font color=#1a73e8>作者：</font>** Abrar Alotaibi, Atta-ur Rahman, Raheel Alhaza 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Saudi Telecom Company (STC) is among the most popular companies in Saudi Arabia, with many customers. Yet, there is still a big room for improvement in users' satisfaction. Social media is the most robust platform to gauge users' satisfaction and determine their sentiments and critics. Twitter is among the most popular social media platform in this regard. STC customers prefer to use Twitter to write their feedback because it's a fast way to get responses due to the STC customer services account. One way to achieve customer demands and improve customer service is using the Sentiment Analysis tool. Sentiment Analysis on Twitter is highly used because of the significant number of tweets and the different opinions. Likewise, Deep learning is the best existing Sentiment Analysis method, and it has diverse models. Bidirectional Encoder Representations from Transformers (BERT) model is one of the deep learning models which have achieved excellent results in Sentiment Analysis for Natural Language Processing (NLP). NLP is mainly investigated in the English language. However, for Arabic, there is a significant gap to be filled. This study trained the proposed model using MARBERT and measured the performance using f1-score, precision, and recall metrics. We trained the model with an Arabic dataset of 24,513 tweets, including 1,437 positive, 13,828 negative, 5,694 neutral, 1,221 sarcasm, and 2,297 indeterminate tweets. The main goal is to analyze the tweets and get the sentiment to improve STC customer service. The proposed scheme is promising in terms of accuracy in contrast to existing techniques in the literature.

---


### 141. [C2RM-Seg: Causal Counterfactual Reasoning with Structural-Semantic Priors for Weakly Supervised Histopathological Tissue Segmentation](https://arxiv.org/abs/2606.25508)

**<font color=#1a73e8>作者：</font>** Hualong Zhang, Siyang Feng, Zihan Huan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Histopathological tissue segmentation is essential for computer-aided diagnosis, yet weakly supervised methods often suffer from noisy pseudo-labels generated by Class Activation Mapping (CAM). Existing CAM approaches tend to focus on staining-driven appearance cues rather than true causal tissue morphology, resulting in spurious localization and poor structural consistency. To address this issue, we propose C$^2$RM-Seg, a two-stage framework that integrates causal pseudo-label refinement with structure-aware semantic enhancement. For classification, we introduce a Causal Counterfactual Reasoning Module (C$^2$RM) that decomposes features into latent factors and performs counterfactual intervention via a learned causal structure matrix, suppressing confounding context and producing morphology-aligned CAMs. For segmentation, we design a Dual-Path Structural-Semantic Architecture that combines fine-grained structural features from ResNeSt with global semantic priors from a frozen DINOV3 foundation model. A cross-path gating mechanism adaptively regulates semantic injection using local structural cues to preserve boundary fidelity. To further mitigate residual pseudo-label noise, we propose an Uncertainty-Gated Margin (UGM) loss, which dynamically balances margin enforcement and confidence learning based on prediction uncertainty. Extensive experiments on two public histopathological tissue datasets show that C$^2$RM-Seg achieves state-of-the-art performance.

---


### 142. [Fault of Our Stars: Behavioral Drivers of Rating-Sentiment Incongruence](https://arxiv.org/abs/2606.25518)

**<font color=#1a73e8>作者：</font>** Ramanaish Abaiyan, Ruththiragayan Sutharsan, Kusal Amantha 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When people share experiences online, they often express thoughts in two ways: a star rating and a written review. In sentiment analysis, ratings are widely used as convenient weak labels for textual sentiment, yet whether the two actually agree is rarely questioned. This study investigates sentiment-rating incongruence, where the sentiment expressed in review text differs from the sentiment implied by the assigned star rating, in Sri Lankan tourism attraction reviews. A dataset of 16,156 reviews from 2010 to 2023 is analyzed using a transformer-based sentiment pipeline that derives textual sentiment independently of assigned ratings. Incongruence occurs in 18.6% of reviews and falls into six directional patterns, with Conservative Rater and Obligatory 5-Star behaviors accounting for the majority of mismatches. Prevalence also varies across venue types, with museums showing the highest rates. Statistical tests, logistic regression, Random Forest, and SHAP analysis identify venue type, reviewer expertise, review length, and temporal factors as contributors to rating-text divergence. Overall, this study demonstrates that star ratings are not interchangeable with textual sentiment and should be validated before being treated as ground-truth labels in NLP.

---


### 143. [Low Variance Trust Region Optimization with Independent Actors and Sequential Updates in Cooperative Multi-agent Reinforcement Learning](https://arxiv.org/abs/2606.25526)

**<font color=#1a73e8>作者：</font>** Bang Giang Le, Viet Cuong Ta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cooperative multi-agent reinforcement learning assumes each agent shares the same reward function and can be trained effectively using the Trust Region framework of single-agent. Instead of relying on other agents' actions, the independent actors setting considers each agent to act based only on its local information, thus having more flexible applications. However, in the sequential update framework, it is required to re-estimate the joint advantage function after each individual agent's policy step. Despite the practical success of importance sampling, the updated advantage function suffers from exponentially high variance problems, which likely result in unstable convergence. In this work, we first analyze the high variance advantage both empirically and theoretically. To overcome this limitation, we introduce a clipping objective to control the upper bounds of the advantage fluctuation in sequential updates. With the proposed objective, we provide a monotonic bound with sub-linear convergence to $\epsilon$-Nash Equilibria. We further derive two new practical algorithms using our clipping objective. The experiment results on three popular multi-agent reinforcement learning benchmarks show that our proposed method outperforms the tested baselines in most environments. By carefully analyzing different training settings, our proposed method is highlighted with both stable convergence properties and the desired low advantage variance estimation. For reproducibility purposes, our source code is publicly available at this https URL.

---


### 144. [PatchINR: Patch-Based Implicit Neural Representations for Efficient and Scalable Inference](https://arxiv.org/abs/2606.25534)

**<font color=#1a73e8>作者：</font>** Jiachen Ren, Wenyong Zhou, Taiqiang Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Implicit Neural Representation (INR) provides an effective approach for continuous signal modeling, but classical per-pixel inference results in quadratic growth in inference count, leading to dramatically increased computational costs in high-resolution application scenarios. To address this issue, we propose a patch-based approach that treats non-overlapping patches as fundamental processing units and predicts entire pixel patches in a single forward pass, significantly reducing the number of inference queries required. To validate the effectiveness of our approach, we propose a hardware acceleration architecture on the Field Programmable Gate Array (FPGA) platform for the INR model, which features a configurable pipeline and supports dual-precision computation. Our patch-based INR achieves comparable reconstruction quality to pixel-level INR (34.97 dB PSNR with 2 x 2 patches) while reducing inference latency by 75% with only 0.6% parameter overhead.

---


### 145. [Spatio-Temporal Mixture-of-Modality-Experts Diffusion for Quantitative DCE-MRI Synthesis from Incomplete MR Sequences](https://arxiv.org/abs/2606.25535)

**<font color=#1a73e8>作者：</font>** Junhyeok Lee, Kyu Sung Choi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Quantitative maps from dynamic contrast-enhanced MRI (DCE-MRI) are essential for tumor assessment but are often unavailable due to contrast-agent risks and protocol variability. Prior methods predict these maps from other MRI modalities, yet most assume fixed, fully observed inputs and fail under realistic missingness. We present Spatio-Temporal Mixture-of-Modality-Experts (ST-MoME), a conditional diffusion framework that synthesizes 3D DCE parameter maps from diverse subsets of multimodal MRI. ST-MoME fuses modality-specific expert features through a spatio-temporal gating network that produces voxel-wise, timestep-dependent weights, forming a conditioning tensor that guides denoising. To preserve quantitative fidelity, ST-MoME performs diffusion directly in image space with 3D patch-based training and a Swin-based backbone. On a clinical brain-tumor cohort of 386 patients, we evaluate ST-MoME across 16 controlled modality-availability scenarios. It achieves the lowest mean Normalized Mean Square Error (NMSE) aggregated across all three DCE parameters, with leading performance on $v_p$ and $v_e$, competitive results on $K^{\mathrm{trans}}$, and the lowest reconstruction error within the clinically critical tumor region. A post-hoc analysis of the learned gating dynamics shows a structural-early, physiological-late fusion schedule consistent with clinical intuition.

---


### 146. [TensorLDM: A Component-Wise Latent Diffusion Model for Volumetric DTI Reconstruction from Sparse DWIs](https://arxiv.org/abs/2606.25545)

**<font color=#1a73e8>作者：</font>** Junhyeok Lee, Kyu Sung Choi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing diffusion tensors from sparse DWIs is critical for accelerating Diffusion Tensor Imaging (DTI) in clinical settings, yet current deep learning approaches frequently yield anatomically inconsistent or physically implausible tensors. We introduce TensorLDM, a component-wise latent diffusion model that processes the six tensor components through two group-specific encoders (for diagonal and off-diagonal elements) while maintaining anatomical consistency via shared DWI conditioning. TensorLDM uses an Anatomy-Conditioned Autoencoder that encourages the latent to focus on tensor properties rather than re-encoding structural information. A shared Cross-Component Attention (CCA) mechanism, applied in both autoencoder refinement and diffusion fine-tuning, models inter-component dependencies, while a Mixture-of-Experts (MoE) DWI conditioner provides component-adaptive conditioning. On the Human Connectome Project (HCP) dataset under a single-shell, four-volume sparse acquisition, TensorLDM produces the most accurate downstream tractography and tensors with near-ground-truth physical validity (SPD-violation rate 1.54% vs. 1.40%), with the best or comparable voxel-wise reconstruction accuracy. Geodesic tensor error measured by the Log-Euclidean Metric (LEM) corroborates these gains.

---


### 147. [Disease-Centric Vision-Language Pretraining with Hybrid Visual Encoding for 3D Computed Tomography](https://arxiv.org/abs/2606.25546)

**<font color=#1a73e8>作者：</font>** Bowen Shi, Weiwei Cao, Ruifeng Yuan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language pre-training (VLP) holds great promise for general-purpose medical AI by leveraging radiology reports as rich textual supervision, yet existing methods struggle with 3D CT imaging due to inefficient visual backbones and coarse semantic alignment. To address these issues, we propose a tailored VLP framework featuring three key components: (1) a CNN-ViT hybrid encoder that replaces ViT's patch embedding with a 3D CNN backbone to efficiently capture local anatomical details while preserving global attention and compatibility with pre-trained cross-modal priors; (2) a disease-level contrastive learning mechanism using learnable query tokens to dynamically extract disease-specific semantics from full reports and align them with corresponding visual features, thereby disentangling distinct diseases within the same anatomical region; and (3) a diagnosis-aware prompt strategy that employs real clinical phrases and aggregated disease prototypes to bridge the pre-training-inference gap and enhance zero-shot diagnostic reliability. Our model achieves state-of-the-art performance on CT-RATE (84.4% AUC, +5.1%) and Rad-ChestCT (75.4% AUC, +5.4%), with even larger gains (+9.8% AUC) on a challenging 60-disease benchmark, and demonstrates strong transferability to radiology report generation, underscoring the generality and clinical utility of our approach.

---


### 148. [Efficient Cross-Scale Invertible Hiding Network with Spatial-Frequency Collaboration and Non-Invertible Mechanism](https://arxiv.org/abs/2606.25547)

**<font color=#1a73e8>作者：</font>** Junxue Yang, Xin Liao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image hiding aims to conceal image-level messages within cover images at the same resolution. Invertible neural networks (INN)-based image hiding has emerged as an important branch. It treats concealing and revealing as a pair of inverse problems on image domain transformation and uses INN's forward and backward processes to address them. Due to architectural constraints, existing INN-based methods suffer from single-scale and single-domain feature extraction and limited nonlinear representation capability, resulting in inferior image quality. To mitigate these limitations, we propose an efficient cross-scale invertible hiding network with the spatial-frequency collaboration and the non-invertible mechanism, termed CrosInv. CrosInv exploits cross-scale and spatial-frequency collaborative features while enhancing nonlinear representation. Specifically, we introduce a cross-scale invertible module that bijectively maps inputs to cross-scale representations. To effectively integrate spatial and frequency information, the cross-scale invertible module employs pixel shuffle, Haar wavelet transformation, and their inverse operations for scale transformation. Furthermore, a non-invertible cross dense module is integrated to enhance the nonlinearity. Comprehensive experiments verify the effectiveness and superiority of the proposed CrosInv.

---


### 149. [Concept Removal for Frontier Image Generative Models](https://arxiv.org/abs/2606.25548)

**<font color=#1a73e8>作者：</font>** Aditya Kumar, Pierre Joly, Adam Dziedzic 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image generative models are trained on massive, largely uncurated internet-scale datasets that contain undesirable visual concepts. Efficiently removing such concepts from the model generations without degrading the quality of output images remains challenging. We introduce a novel concept removal method for frontier diffusion and image autoregressive models, such as SD3.5, Flux, and Infinity. Our intervention replaces the internal bottleneck layer present in all these modern models with a transcoder that is trained to replicate the original layer while structuring it into distinct activation features. This in-place substitution creates an integrated filter through which concept-specific signals can be selectively disabled while preserving the rest of the model's behavior. Since the intervention modifies the model backbone rather than attaching an external component, it remains persistent under white-box access. Empirically, the approach achieves state-of-the-art concept removal performance across modern diffusion and autoregressive models, maintains visual generation quality, provides robustness against adversarial prompts, and supports sequential removal of diverse concepts. This positions our method as a practical approach for concept removal in frontier image generative models.

---


### 150. [H-Adapter: Pose-Robust Hairstyle Transfer via Attention-Derived, Source-Aligned Hair Masks](https://arxiv.org/abs/2606.25578)

**<font color=#1a73e8>作者：</font>** Seulgi Jeong, Yunseong Cho, Sanghun Park  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hairstyle transfer has practical applications such as virtual try-on, yet remains challenging when the source and reference exhibit large head-pose discrepancies. We propose H-Adapter, which improves pose robustness by training with a region-specific loss that disentangles hair and non-hair objectives and thereby induces spatially disentangled cross-attention, from which a source-aligned hair edit mask is derived to guide diffusion-based inpainting. Experiments on pose-agnostic and pose-different subsets demonstrate strong quantitative results, including the best FID, $\mathrm{FID}_{\mathrm{CLIP}}$, and CLIP-I under pose differences, while maintaining competitive non-hair preservation and improving qualitative fidelity to fine-grained reference hairstyle details. Beyond source-conditioned transfer, H-Adapter supports practical extensions including text-to-image generation, auxiliary prompt-based hair color control, and compatibility with an identity-preserving IP-Adapter variant. We also introduce a VLM-as-a-judge protocol and observe consistent gains in hairstyle faithfulness, non-hair preservation, and artifact quality.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-222](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
