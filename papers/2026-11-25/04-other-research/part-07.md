# 📦 其他研究 | 2026年11月25日

> 本类共 **569** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-350**（第 7/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-569](./part-12.md)

---

### 301. [Towards Global Counterfactual-Based Self-Explainable Graph Neural Networks](https://arxiv.org/abs/2611.29681)

**<font color=#1a73e8>作者：</font>** Wendy Zheng, Yinhan He, Jundong Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Counterfactual Explanations (GCEs) have emerged as an effective approach for interpreting Graph Neural Network (GNN) predictions by identifying minimal graph modifications needed to change predictions. However, existing methods suffer from two fundamental limitations: (1) They rely on a post-hoc explanation paradigm, where a separate explainer is trained after the GNN. This sequential optimization prevents the explainer from leveraging how the GNN learned its representations, often resulting in lower-quality explanations. (2) They are largely local, generating counterfactual explanations only for individual samples. Consequently, they fail to capture generalizable patterns across the data distribution, a crucial gap for applications like drug discovery, where global principles enable systematic decision-making across thousands of cases. To address these limitations, we propose GCSGNN (Global Counterfactual-based Self-explainable GNN), a unified framework that integrates counterfactual generation into the GNN architecture, encouraging explanations that faithfully reflect the model's decision-making process. Beyond local explanations, GCSGNN discovers shared latent patterns influencing predictions across graphs, yielding global (i.e., model-level) counterfactual explanations. We further introduce an efficient latent-space counterfactual mechanism that avoids the combinatorial complexity of discrete graph manipulation, enabling scalable discovery of generalizable modification patterns. Extensive experiments on real-world datasets demonstrate that GCSGNN outperforms existing methods in generating effective counterfactual explanations. Our code is available at this https URL.

---


### 302. [Where Do Fact-Checking Errors Arise? Separating Retrieval, Search Control and Judgement in Evidence-Grounded Verification](https://arxiv.org/abs/2611.29697)

**<font color=#1a73e8>作者：</font>** Martin Pavlíček, Martin Kotyrba, Eva Volná 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> An evidence-grounded fact-checker can fail because it does not find the evidence or because it does not use it; end-to-end accuracy does not tell the two apart. We present a protocol that follows the reference evidence from the store to the verdict and separates retrieval, search control, judgement and verdict validation. We assess 293 claims from FEVER, FEVER 2.0 and AVeriTeC with one open-weights 9B model under two evidence conditions: small stores of annotated evidence, where discovery is easy, and the full source collections. In the control condition a single hybrid retrieval pass delivers complete reference evidence for 226 of 228 evidence-bearing claims, and adaptive controllers and a tool agent spend two to nine times as many model calls without a consistent gain. Of 34 decisive claims labelled as lacking evidence, 33 have the complete evidence in the packet: in 15 the judge abstains, and in 18 validation rules overturn a decisive verdict. On AVeriTeC these rules lower single-pass accuracy by six points, to 65.0% (balanced accuracy 57.6%). Ten judges from eight model families also show abstentions and validation conversions on fixed packets. Against the full stores hybrid single-pass accuracy falls by 17 to 29 points. Wikipedia evidence recovery declines; AVeriTeC recovery changes from annotated answers to cited pages and is measured separately. No controller recovers the accuracy loss. The agent also shows no resolved gain on 714 further Wikipedia claims. Evidence recovery, judgement and validation should be measured separately before an error is attributed to search.

---


### 303. [Managing Uncertainty in Teacher Vibe Coding: A Comparison of Teacher and Expert Workflows](https://arxiv.org/abs/2611.29698)

**<font color=#1a73e8>作者：</font>** Jiaju Lin, Ellen Wenting Zou  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Vibe coding, or natural language software development, enables teachers to become creators of digital teaching artifacts. However, novice educators oftentimes face different barriers. This qualitative study examined the workflows of pre-service teachers, in-service teachers, and expert developers through think-aloud protocols. Findings reveal vibe coding operates through a loop of problem framing, development, and verification governed by uncertainty management. Teachers reduced uncertainty by grounding designs in authentic needs: pre-service teachers drew on pedagogical principles, whereas in-service teachers relied on everyday teaching challenges. Conversely, Experts reduced ambiguity by constraining requirements, decomposing artifacts into testable modules, and automating tests. These differences reveal complementary forms of pedagogical, contextual, and technical expertise. Future work may be about supporting nontechnical teachers in developing reliable and educational applications.

---


### 304. [Loop-Count Schedules in Looped Transformers: An Empirical Study](https://arxiv.org/abs/2611.29704)

**<font color=#1a73e8>作者：</font>** Konstantin Kolokolov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped transformers apply one block of layers several times with shared weights, trading parameters for repeated computation. We study how the schedule of the loop iteration count R during training determines whether each extra pass acts as a full layer or as a small correction, using a controlled ladder of 46M-110M-parameter models trained on 2B tokens with learned residual gates on every loop pass and three schedules: R fixed to 2, R sampled uniformly from {1,...,6}, and R sampled from {2,3,4}. We find that the lower bound of the sampling range is the decisive choice. If the sampled range includes R=1, so that some training steps run the block only once and compute the loss on that single pass, the gates collapse to 0.1-0.5 and each additional pass becomes a small correction to the first; if the range starts at R=2, so that every training step runs the block at least twice, the gates stay at 0.6-0.9 and each pass keeps the strength of a full layer, while the model can still be run at any R from 2 up to twice the largest trained value with validation loss within a few hundredths of a nat of its best. The {2, 3, 4} schedule gives the best looped model, 2.909 nats against 2.951 for the parameter-matched plain model, and degrades by only 0.038 nats when run at twice its trained depth. We further show that under a fixed R the direction of the residual stream converges geometrically beyond the trained depth while the loss diverges, which refines a recent finding that static-depth training does not converge, and that reusing the first pass's keys and values on later passes costs 0.01-0.03 nats in every regime while making the per-token iteration uniformly contractive and halving the inference cache. The loop recovers about a third of what real depth provides at equal parameters. The code, trained weights, and per-token traces are released.

---


### 305. [Learning-Augmented QUBO for Time-Expanded Multi-Commodity Flow](https://arxiv.org/abs/2611.29711)

**<font color=#1a73e8>作者：</font>** Aikaterini Nikolidaki  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study energy-aware multi-commodity flow on time-expanded graphs, a problem that captures dynamic routing in layered networks and is NP-hard in general. We formulate the problem as a quadratic unconstrained binary optimization problem, give an explicit penalty coefficient that provably guarantees feasibility, and show that it is smaller than the standard bound by a factor of roughly the number of active links. The layered structure of the time-expanded graph yields three structural results: a treewidth bound that gives a fixed-parameter tractable exact algorithm in the bag size, a matrix-product-operator representation of small bond dimension, and a proof that the annealing gap of the associated Ising Hamiltonian is strictly positive for every instance with a unique optimum, uniformly over bounded windows. For learning-augmented routing, we bound the Hamming distance between a predicted and an optimal flow by the flow error, and prove a consistency guarantee: a hybrid algorithm that keeps the better of the prediction and the solver output returns a flow whose cost exceeds the optimum by a factor that grows linearly with the prediction error. The results are exact statements about the QUBO and its associated Ising Hamiltonian, and they hold for any physical implementation.

---


### 306. [UniDR: Learning To Generate Anatomical Deformations From Images via Unified Diffusion Modeling and Registration](https://arxiv.org/abs/2611.29712)

**<font color=#1a73e8>作者：</font>** Swakshar Deb, Tonmoy Hossain, Tom Fletcher 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents a novel framework, Unified Diffusion modeling and Registration (UniDR), which learns to generate arbitrary anatomical deformations from images with preserved topology. Existing approaches often model the generative process separately from registration-based deformation estimation; hence making them prone to propagated errors from the registration stage. To address this limitation, we propose a unified paradigm based on a conditional diffusion model over deformation fields that are jointly optimized from the registration process. A principled registration-guided score-matching objective function is then introduced to align the diffusion process with the deformation distribution induced by registration. As a result, our UniDR establishes an explicit connection between generation and registration: the diffusion model enables exploration of the space of plausible anatomical deformations, whereas registration provides structured supervision for learning transformations consistent with observed images. Once trained, UniDR is able to sample diverse, anatomically plausible transformations conditioned on any single input image. We evaluate UniDR across multiple real-world applications and demonstrate its effectiveness in generating high-fidelity image samples compared to the state-of-the-art. Additionally, we demonstrate that these generated samples improve performance in downstream medical image analysis and vision tasks.

---


### 307. [From States to Dynamics: Detecting Rule Violations in OthelloGPT](https://arxiv.org/abs/2611.29715)

**<font color=#1a73e8>作者：</font>** David L. Cao, Sai Sumedh R. Hindupur, Demba Ba  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sequence models trained on game moves have been shown to encode world models, with structured linear probes revealing the underlying game states. World models, however, are inherently dynamic: in deterministic board games, a set of rules constrain how states evolve over time. We therefore ask if and how OthelloGPT, a transformer trained only on Othello move sequences, manifests the rules of the game in its activation space. We divide the rules of Othello, and symmetrically their violations, into three classes: placing a disc on an empty square (R1), flanking an opponent's disc (R2), and moving in turn (R3). We find that linear probes accurately separate legal from illegal moves, and also distinguish between the three kinds of rule violations. We introduce an unsupervised rule-violation detector based on the step length of activations between consecutive moves, which identifies illegal moves above chance. We further improve our detection metric by computing step length in the latent space of select sparse autoencoders. Together, we find that OthelloGPT follows game rules of Othello to a large extent, and that we can detect rule violations using structured detectors on model activations.

---


### 308. [Randomized Weighted Distance Nearest Neighbor Classification](https://arxiv.org/abs/2611.29720)

**<font color=#1a73e8>作者：</font>** Shayan Shafaei, Naeem Shahabi Sani, Chao Lan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The nearest neighbor classifier is known to be memory-inefficient, and a popular solution is to compress its training data. Recently, a compression algorithm based on weighted distance nearest neighbor (WNN) was proposed, which has elegant theoretical properties and effective classification performance. However, its compression process is computationally expensive, for it performs a greedy search of the densest homogeneous balls in data space. In this paper, we propose a randomized variant RWNN. It simply randomizes the ball search process, and results in substantially reduced compression time (often 0.1%--1% of WNN's) and similar classification accuracy. RWNN also inherits several theoretical properties of WNN including consistency and a generalization bound. Experimental results on multiple datasets demonstrate its efficacy.

---


### 309. [ApexID: Hierarchical Learning for Multi-Species Animal Re-Identification](https://arxiv.org/abs/2611.29723)

**<font color=#1a73e8>作者：</font>** Seifeldin Elkerdany, Mohamed ElBassat, Gamal Abouelhamd 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Animal re-identification (Re-ID) must distinguish individuals across species and capture conditions. We introduce ApexID, a hierarchical SphereFace2-based loss that integrates global identity discrimination with balanced animal-category supervision. Using 132,533 images curated from 19 public datasets, we evaluate three model families and four objectives on four external datasets with observation-aware retrieval protocols. ApexID achieves a dataset-averaged Rank-1 accuracy of 64.89% with ConvNeXt-Small and an mAP of 32.54% with MIEW-ID, outperforming their pretrained reference models. On elephants, a category absent from animal Re-ID training, our ConvNeXt-Small variant achieves the highest retrieval performance among the fourteen evaluated configurations. Scores vary by backbone and dataset, and open-set evaluation reveals remaining discovery challenges. These findings support hierarchical category-identity learning to improve transfer to unseen datasets and species.

---


### 310. [Quantum-Annealing-Assisted Search-Space Reduction for Large-Scale Shortest-Path Computation](https://arxiv.org/abs/2611.29724)

**<font color=#1a73e8>作者：</font>** Kasymkhan Khubiyev, Yaroslav Kholodov, Alexey Petrenko  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Computing point-to-point shortest paths in large weighted graphs can require classical algorithms to explore a substantial portion of the graph. We ask whether quadratic unconstrained binary optimization (QUBO) can reduce the work required to return a verified shortest path. For a known set of queries, we select paths that share arcs. For new queries, we select a corridor and test whether any path leaving it could improve the distance found by Dijkstra's algorithm. We also partition the graph into blocks and reuse local paths between their boundaries. We compare path encodings on identical inputs using simulated annealing on classical processors.
The comparison of exact block overlays with direct Dijkstra search covered 45 synthetic graphs and the New York road network with 264,346 vertices. The overlay reduced the number of arc inspections in the final search in 97 of 200 graph and block-size combinations. Once endpoint attachment, assembly, and reconstruction were included, every combination took longer per query than direct Dijkstra search. On a separate set of 168 synthetic graphs, tightening the flow penalty increased the fraction of trials returning a verified local optimum within 20,ms from 35.8% to 84.1% under the same annealing schedule and update policy. A cost model for a prepared graph of 16,384 vertices predicts a 1.072x query speedup over a parallel classical overlay if five local problems can be solved accurately in one batch at the assumed service cost. The practical benefit of reduction thus depends on whether savings in the final search cover the cost of obtaining and verifying the local paths.

---


### 311. [Lightweight Spectral Subspace Filtering for Trojan-Resilient AI Inference Engines](https://arxiv.org/abs/2611.29734)

**<font color=#1a73e8>作者：</font>** Soumita Chatterjee, Sudip Ghosh, Tamal Ghosh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Backdoor attacks pose a significant security threat to deep neural networks (DNNs) deployed on AI inference engines and hardware accelerators. By embedding hidden triggers during training, these attacks induce malicious behavior while maintaining high accuracy on benign inputs. Multi-trigger backdoor attacks are particularly challenging to detect and mitigate because of the distributed and stealthy nature of their effects. To address this challenge, this paper proposes a training-free Spectral Subspace Filtering framework that detects and suppresses backdoor-induced activations by analyzing latent feature representations. Exploiting the geometric separation between benign and malicious feature distributions, the framework employs Singular Value Decomposition (SVD) to identify the dominant malicious subspace and performs inference-time spectral scrubbing through activation projection. This approach suppresses backdoor effects without model retraining, requiring only a small set of triggered samples collected offline. Experimental evaluation across CNN and transformer architectures, including AlexNet, ResNet18, VGG16, MobileNetV2, and Vision Transformer (ViT), demonstrates that the proposed method reduces the attack success rate (ASR) from 94.2-99.8% to an average of 2.07%, while preserving clean accuracy of up to 98.54% with low inference overhead. The framework also demonstrates robustness across varying poisoning rates and multiple concurrent triggers, highlighting its potential as a lightweight runtime defense for enhancing the security and reliability of AI inference engines against backdoor attacks.

---


### 312. [Seeing Beyond Names: Image-Grounded Concept Linking for Robust Vision-Language Recognition](https://arxiv.org/abs/2611.29735)

**<font color=#1a73e8>作者：</font>** Behraj Khan, Shabir Ahmad, Tahir Qasim Syed 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A zero-shot vision-language classifier is highly sensitive to the class names it receives. Even when images remain unchanged, replacing familiar labels with synonyms, abbreviations, or ontology terms can significantly alter predictions. We investigate this \emph{vocabulary shift} using a leakage-free evaluation protocol across Tiny ImageNet, ImageNet-R, ImageNet-A, and ImageNetV2. With CLIP ViT-B/16, alternative class names reduce top-1 accuracy by $14.8$--$17.6$ percentage points. To address this issue, we propose \emph{image-grounded concept linking}, a training-free method that maps class names to visual concepts and uses a reliability gate to improve predictions. The method outperforms a template ensemble across all four datasets, achieving a pooled gain of $1.8$ points. We further evaluate five vision-language backbones across four datasets. Our method improves performance in $16$ of $20$ backbone--dataset combinations, with no significantly negative results. It also reduces pooled negative log-likelihood across all five backbones. Stronger text linking and transductive refinement provide no consistent improvements, suggesting that accurate visual class-name linking remains the main challenge. A second CLIP ViT-B/16 seed confirms the improvement on ImageNetV2, but not on ImageNet-A.

---


### 313. [Deterministic Proper Positive-Only Learning Is Independent of ZFC](https://arxiv.org/abs/2611.29737)

**<font color=#1a73e8>作者：</font>** Shai Ben-David, Farnam Mansouri, Anay Mehrotra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Binary classification from positive-only samples is a variant of PAC learning in which the learner receives i.i.d. samples only from the positive region of an unknown target concept, but is evaluated on the full distribution. Improper learnability in this model has a textbook characterization, whereas proper learnability has remained open for decades. Recent work characterized it for learners with access to randomness, and showed that, unlike in PAC learning, some classes are properly learnable with randomness but not without it, leaving the deterministic case open. We show that this case cannot be resolved within the standard axioms of mathematics (ZFC): there is a class of VC dimension two whose deterministic proper learnability is independent of ZFC, even though a randomized learner provably learns it. Moreover, no dimension of finite character, a desirable property shared by most dimensions in learning theory, characterizes deterministic proper learnability. We also show that the size of the domain is decisive. In ZFC, deterministic proper learnability has a combinatorial characterization on every domain whose cardinality is below a certain threshold, including every countable domain. In contrast, this characterization fails on every domain of sufficiently large cardinality. Under the generalized continuum hypothesis, this threshold is sharp: it is the exact cardinality at which the characterization starts to fail. Finally, our proofs introduce new tools, based on the Erdos--Rado partition theorem, that may be of broader interest.

---


### 314. [MISeg-Agent: A Human-in-the-Loop Agentic Framework for Error Diagnosis and Executable Prompt Review in 3D Medical Image Segmentation](https://arxiv.org/abs/2611.29741)

**<font color=#1a73e8>作者：</font>** Delin An, Mingqi Xu, Jian-Xun Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the strong performance of modern medical image segmentation models, their predictions can still contain localized errors that compromise segmentation quality. Identifying and correcting these errors is therefore essential for improving the reliability of existing segmentation results. While interactive segmentation models enable targeted corrections, identifying potential errors, determining where to intervene, and evaluating corrective actions remain challenging. Moreover, each correction changes the current mask, requiring subsequent error diagnosis and recommendations to adapt accordingly. To address these challenges, we propose MISeg-Agent, a human-in-the-loop agentic framework that diagnoses segmentation errors and provides evidence-based correction recommendations. MISeg-Agent first selects a suitable pretrained segmentation model based on benchmark performance and computational requirements. Given its predicted mask, the framework identifies potential missing and excess foreground regions and recommends suspicious slices and corrective points for review. The framework then evaluates candidate point prompts using an interactive segmentation model and presents the resulting corrections for human verification before applying them. By operating directly on images and predicted masks, the error diagnosis process remains independent of the underlying segmentation model architecture. Evaluations on CT datasets demonstrate that MISeg-Agent improves initial segmentation results and produces final masks closely aligned with reference annotations. By integrating adaptive error diagnosis with validated correction recommendations, MISeg-Agent provides an interpretable approach to identifying and reducing residual errors in existing medical image segmentations.

---


### 315. [Who Sent It or How It Moved? Sender Shortcuts in Cryptocurrency Anti-Money-Laundering Benchmarks, Audited on Elliptic2 and Elliptic++](https://arxiv.org/abs/2611.29744)

**<font color=#1a73e8>作者：</font>** Mohammad Nasir Uddin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Two public benchmarks dominate graph-based anti-money-laundering (AML) research on Bitcoin: the transaction-level Elliptic dataset, extended as Elliptic++, and the subgraph-level Elliptic2. In both, a label is assigned according to the entity that sends the funds. We ask whether models trained on these benchmarks learn how laundering moves or merely who sent the money, and we propose a diagnostic protocol to tell the two apart: a sender lookup baseline, a novelty baseline, a sender-disjoint split with a leakage check, and a decomposition of performance into sender, receiver and intrinsic signal. On Elliptic2 the task largely reduces to classifying the sender. Under the standard random split, a no-learning lookup of sender history reaches a PR-AUC of 0.954, against 0.975 for gradient boosting on 456 features; our reimplementation of RevClassify reproduces its reported 0.97 and falls to 0.126 without sender information. When senders are held out, performance drops to 0.746, and the subgraph's own structure, transactions and receivers fall from 0.619 to 0.186. On Elliptic++ the same protocol finds the shortcut negligible: sender history reaches only 0.340 against 0.986 for the full model (3.5 against 10.1 times the test prevalence), adding it to the full model raises PR-AUC by less than 0.004 in every seed, and the transaction's own features keep 0.883 when sending addresses are held out. We trace the difference to the unit of sender identity: Elliptic2 senders are entity clusters that recur across many labeled subgraphs, whereas Elliptic++ senders are individual addresses, and fewer than half of test transactions have a sending address seen in training. A shared sender-based label rule thus produces a severe shortcut in one benchmark and a negligible one in the other, so the diagnostic must be run on each benchmark.

---


### 316. [Refine, Don't Reinvent: RASA-Bench for Source-Grounded Hindi Prose Refinement](https://arxiv.org/abs/2611.29750)

**<font color=#1a73e8>作者：</font>** Abdur Rahman, Pratham Singla, Mohammad Saifullah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> For a producer of Hindi creative prose, drafting is cheap and editing is not: a machine-written episode, story, or essay reads as under-written and flat, laced with translationese, and it sometimes quietly alters what the source says. RASA-Bench targets that editing task across three Hindi prose forms, measuring how well a model refines an under-written AI draft, a task distinct from writing from scratch. Across 2,050 drafts and eight refiners (16,400 rewrites), a four-layer protocol credits a rewrite only after it passes a faithfulness check against its own source, then ranks the survivors by holistic editorial preference through per-form Bradley-Terry fits whose centered coefficients are standardized before equal-weight averaging. Staying faithful proves to be a decisive test that behaves differently by form: gate-failure rates range from 9.1% on short stories to 29.5% on audio fiction, and the drift that disqualifies a rewrite shifts from events and identity in narrative to claims and evidence in essays. A 600-case human audit puts gate agreement at 0.925 (0.91 to 0.94 across forms), whereas subjective preference is form-sensitive and least settled for essays, among human readers no less than the model judge. The benchmark, evaluation protocol, and Hindi prose diagnostics are available at this https URL.

---


### 317. [DREAM: Dual-Memory Reasoning for Anticipatory 3D Perception in Autonomous Driving](https://arxiv.org/abs/2611.29753)

**<font color=#1a73e8>作者：</font>** Sriram Mandalika, Athira Nambiar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous driving systems must not only interpret the current scene but also anticipate perceptual challenges such as occlusions, sparse observations, and recurring failure patterns. However, most existing LiDAR semantic segmentation methods operate in a frame-centric manner, processing each scan independently and discarding past contextual experience, which limits robustness under dynamic scene changes. We propose DREAM, a Dual-memory REAsoning framework for continual LiDAR seMantic segmentation that reframes perception as an experience-driven and anticipatory process. DREAM maintains two complementary memory banks in a strictly online setting: a latent memory that stores compact semantic abstractions of previously observed scenes, and an error memory that records representations associated with uncertain predictions. At each timestep, relevant memory entries are retrieved via cosine similarity and integrated into the feature space through a lightweight modulation mechanism, enabling the model to reinforce consistent semantic patterns while suppressing recurring failure modes. The backbone remains frozen and no past scans are replayed, ensuring computational efficiency and bounded memory growth. Extensive experiments on multiple large-scale LiDAR benchmarks demonstrate that DREAM achieves state-of-the-art performance, with consistent improvements on dynamic and small-scale objects, highlighting the effectiveness of persistent and error-aware memory for robust long-horizon perception.

---


### 318. [Mitigating Nested GTP Attacks: A Closed-Loop eBPF Defense for 5G and Beyond Networks](https://arxiv.org/abs/2611.29756)

**<font color=#1a73e8>作者：</font>** AbdulAziz AbdulGhaffar, Ashraf Matrawy  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The evolving cellular networks continue to rely on the legacy GPRS Tunneling Protocol-User Plane (GTP-U) to encapsulate and route user data traffic across the data plane. Recent security research demonstrated that nested GTP-U (GTP-in-GTP) payload vulnerabilities enable a diverse range of attacks on victim users. To address this vulnerability, in this paper, we propose a closed-loop extended Berkeley Packet Filter (eBPF) and eXpress Data Path (XDP) defense to detect and mitigate nested GTP-U attacks in 5G and beyond networks. The proposed framework contains three components: an in-kernel XDP Detection and Drop Module (XDP-DDM), a user-space User-Plane Telemetry Agent (UP-TA), and a multi-threaded Control-Plane Mitigation Orchestrator (CP-MO).
We implement and evaluate the proposed defense on a sliced 5G testbed integrating Free5GC, UERANSIM, and Containerlab. Experimental results indicate that the XDP-DDM detects and drops malicious nested GTP-U packets at line rate, while the UP-TA and CP-MO asynchronously report and revoke the attacker's network access, respectively. Under a 10,000 packets-per-second cross-slice nested GTP-U flood, the proposed solution preserves the baseline performance of the victim slices while introducing minimal overhead. We also show that the proposed solution has minimal impact on the user's throughput and round-trip time.

---


### 319. [What Should World Models Plan Over? Learning Geometry-Aligned Representations of Body Motion](https://arxiv.org/abs/2611.29759)

**<font color=#1a73e8>作者：</font>** Renhao Zhang, Abhranil Chandra, Bruno Castro da Silva  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce MotionPort, which learns low-dimensional latent representations of body motion for accurate dynamics prediction and effective long-horizon planning. Existing world-model planners often search over action representations learned for prediction, yet we show that predictive accuracy alone does not ensure that optimization can discover successful trajectories. MotionPort addresses this mismatch by representing body trajectories rather than action chunks and organizing the search space by motion similarity, helping predicted improvements translate into successful execution. Without fine-tuning state encoders, MotionPort raises average goal-reaching success from 37.9% to 87.8% across three backbones and seven settings in four domains. On the evaluated AntMaze-OGBench tasks, it achieves 72% success, compared with 4% for the strongest baseline.

---


### 320. [Selecting Stable Sampling Dynamics for Compositional Diffusion: A Feynman-Kac Weight Reduction](https://arxiv.org/abs/2611.29764)

**<font color=#1a73e8>作者：</font>** Sunjin Kim, Sungsoo Ahn, Michael Chertkov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Given $K$ separately trained diffusion models, how should one sample from a $\beta_k$-weighted product of their terminal laws without jointly retraining the experts? Existing Feynman--Kac constructions provide many weighted stochastic differential equations (SDEs) with the correct target marginal. The consequential question is how to select useful proposal dynamics among them. We study an explicit family of weighted diffusions that realizes the same product-of-intermediate-experts trajectory. A scalar parameter $\lambda$ controls how strongly the proposal drift follows the composed expert score, while an additional Langevin component can be varied independently. Writing $B=\sum_{k=1}^{K}\beta_k>0$, we identify the distinguished choice $\lambda=1/B$. At this value, the aggregate squared-score term in the instantaneous Feynman--Kac log-weight rate cancels exactly. For positive expert exponents, the remaining score-disagreement contribution is non-positive. We call this structural cancellation Feynman--Kac reduction. Under bounded-divergence assumptions, it yields an upper bound on the instantaneous unnormalized log-weight rate for all $\lambda\leq 1/B$. For linear diffusion protocols with compactly supported expert data, $\lambda=1/B$ yields two-sided bounds at every nonterminal time, for exponents of either sign. A corresponding result holds for a single expert under the same divergence assumption. In these two-sided settings, the selected value is unique within the specified family in a universal worst-case sense. Experiments on Gaussian mixtures and molecular sampling compare the analytically predicted stability with actual sampling quality, including instances in which parameter choices different from $\lambda=1/B$ perform better empirically.

---


### 321. [CivicBench: Robust Detection of AI-Generated Political Video](https://arxiv.org/abs/2611.29766)

**<font color=#1a73e8>作者：</font>** Mert Onur Cakiroglu, Elham Buxton, Mehmet Dalkilic 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI-generated video of politicians can pass for real footage, and once such fakes are common, real footage can be dismissed as fake. Platforms address both problems with detectors, but whoever uploads a clip controls its pixels. Existing datasets of political video are small, show real politicians, and test no attacks. We introduce CivicBench, with 10,800 generated clips of invented politicians from eight open generators and 2,632 public-domain or openly licensed real clips. Each clip can be attacked, to hide a fake or to frame real footage. Published detectors trained on a general benchmark reach at most .781 AUC on CivicBench. Adversarial changes of 1 gray level per pixel hide nearly every generated clip from the detectors not built to resist attacks. An attack's reach is how far it can move a clip's score. A clip keeps its label when its margin from the threshold exceeds this reach, and we find that the reach grows almost linearly with the budget. On this basis, we propose Tau-Anchor, which fine-tunes an encoder pretrained on attacked images. It attacks real and generated clips during training and adds a margin term at its deployed threshold. It reaches .941 AUC on CivicBench. It also keeps .668 of generated clips flagged at 2 gray levels, against at most .289 for published detectors. When real clips are framed at the same 2 gray levels, Tau-Anchor's false alarms rise only from 8% to 14%, whereas four published detectors flag nearly every framed real clip at just 1 gray level. External political footage and two general benchmarks show the same pattern under attack. Code and data are available at this https URL.

---


### 322. [When Simpler Beats Learned: Dual-Weighted Sampling vs. Machine Learning for the Pricing Subproblem in Graph Coloring](https://arxiv.org/abs/2611.29769)

**<font color=#1a73e8>作者：</font>** Nikolai Antonov, Přemysl Šůcha, Mikoláš Janota 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The graph coloring problem can be solved to optimality by branch-and-price (B&P), but its performance hinges on the column generation (CG) step, where each iteration requires solving a maximum weight independent set (MWIS) pricing problem. The state-of-the-art machine-learning (ML) pricing heuristic follows a prediction-sampling paradigm: a learned model scores each vertex of a graph, and independent sets are sampled from the induced distribution. We observe, however, that the scoring procedure does not need to be learned, and critically assess the role of ML by replacing the learned scores with the dual solution of the restricted master problem, resulting in Dual-Weighted Sampling, a proposed lightweight alternative that requires no feature engineering or training. Within a unified CG and B&P framework that varies only the pricing oracle, Dual-Weighted Sampling outperforms MLPH, hand-crafted heuristics, and exact solvers on the established graph coloring benchmark in both runtime and solution quality. In particular, it remains competitive on the DIMACS random family, where MLPH was shown strongest in the original evaluation, while achieving more than a two-fold speedup in CG runtime on recursive-sparse and real-world graph families.

---


### 323. [Constrained Diffusion from Binary Evaluations via Learned Doob h-Functions](https://arxiv.org/abs/2611.29779)

**<font color=#1a73e8>作者：</font>** Ssaumya Kammal Jaiswal, Mahfuza Farooque  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conditional generation under constraints that can only be checked on a finished sample, such as a molecular property filter, remains challenging for diffusion models: most guidance methods require differentiable measurement operators, paired conditional data, or rollouts of the base model at every step. We present a framework grounded in the Doob $h$-transform that reduces conditional generation to learning a single function, the probability that a noisy sample denoises into the constraint set. We learn this function from binary clean-sample evaluations alone, by squared-error regression on forward-noised labels; the base model is frozen, one lightweight head is trained per constraint, and noisy-state classifier guidance arises as a special case. The exact guidance step fades where the constraint signal provably vanishes and carries a factor of the inverse probability across samples, which normalized guidance discards: with the schedule and mean step size held fixed, equalizing the step costs 17.0 to 18.5 points of constraint satisfaction on CIFAR-10 at comparable FID, across independently trained estimators. Guidance is more than 50$\times$ cheaper per satisfying sample than rejection sampling at a 1.7% base rate, raises a Lipinski-type property filter on QM9 from 54.3% to 96.8%, and lifts satisfaction on Stable Diffusion 1.5 from 7.2% to 60.0% at one sixteenth of the cost of derivative-free selection, which reaches 9.0%. These results demonstrate that binary evaluations of clean samples are sufficient supervision for constrained generation across pixel, latent, and molecular diffusion.

---


### 324. [A Cascaded Framework with a Cross-Attention-Guided Mamba-CNN Model for Pre- and Post-Treatment Glioma Segmentation](https://arxiv.org/abs/2611.29792)

**<font color=#1a73e8>作者：</font>** Siavash Taremi, Mahmoud Heidari, Seyed Mohammad Hossein Hashemi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate glioma segmentation is vital for diagnosis and follow-up, but manual segmentation is time-consuming, subjective, and variable across interpreters. Gliomas are heterogeneous in size, shape, and location. Deep learning has therefore emerged as a potential solution. CNNs excel at local features but may struggle with long-range dependencies, whereas Vision Transformers capture global context efficiently but incur higher computational complexity. Most previous studies focused on pre-treatment gliomas; post-treatment cases with resection cavities (RCs) remain less explored. This study proposes a Cross-Attention-Guided Mamba-CNN (CMC-Seg) model within a cascaded framework for pre- and post-treatment diffuse glioma segmentation, aiming to balance accuracy and computational cost. Experiments used BraTS 2025 mpMRI of diffuse glioma patients. After preprocessing, a coarse segmentation model extracted tumor-centered patches, which were fed to CMC-Seg for fine-grained segmentation. CMC-Seg was compared with 3D U-Net, SegResNet, SwinUNETR, UNETR, nnFormer, and SegMamba. On the test set, CMC-Seg achieved the highest mean Dice (81.20%) and non-enhancing tumor core (NETC) Dice (77.09%). It also achieved an RC Dice of 78.63% and the lowest 95% Hausdorff distance (HD95; 4.39 mm). Results were comparable to CNN and Mamba baselines and significantly better than Transformer-based baselines (P < 0.05). CMC-Seg required the fewest inference GFLOPs (381.49). Ablation experiments indicated that multi-direction scanning and cross-attention improved performance, particularly for RC (P < 0.05). Grad-CAM explainability experiments showed that CMC-Seg focuses on diagnostically relevant tumor regions.

---


### 325. [Learning Gaussian Process Priors with Linear Semigroups and Kinetic Regularisation](https://arxiv.org/abs/2611.29796)

**<font color=#1a73e8>作者：</font>** Angela Lavinia Varazi, Felipe Tobar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce a semigroup-based construction of Gaussian process (GP) priors. A linear semigroup transforms a source GP at $t=0$ into a prior at $t=1$, enabling computationally tractable regression. Linearity preserves Gaussianity, allowing us to characterise the evolution of the covariance and draw connections with optimal transport and convolution models. The semigroup is parametrised by its generator, which is learned through two competing objectives: the marginal likelihood encourages agreement with observations, while a kinetic-energy regulariser favours lower-energy trajectories and limits unnecessary mass displacement from the source GP. Experiments on independent GP draws show that, with sufficiently many training functions, the learned prior provides accurate predictions on held-out functions, while kinetic regularisation substantially reduces the energy of the generated trajectories without compromising prediction accuracy.

---


### 326. [Revisiting RadioGalaxyNET: modern detectors for radio galaxy detection and host identification](https://arxiv.org/abs/2611.29798)

**<font color=#1a73e8>作者：</font>** Argo Saakyan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> RadioGalaxyNET is the public benchmark for finding extended radio galaxies in EMU pilot-survey images, classifying them and locating their infrared hosts. Its best published results date from 2023: 54.5 box AP (Gal-YOLOv8) and 48.1 host keypoint AP (Gal-DINO). We train three current detectors, D-FINE-seg, YOLO26-pose and RF-DETR, on the same data and score them with the benchmark's own evaluation code, which reproduces the published Gal-DINO numbers exactly. All exceed the published results. D-FINE-seg M reaches 67.1 box AP and 72.4 host AP, 12.6 and 24.3 points above the best published results, and the highest host AP of the detectors we tested; on boxes it is level with YOLO26. Its host lead over YOLO26 comes from host-centered images, which make up most of the benchmark. End to end, D-FINE-seg S is the fastest model at 1.9 ms per image; engine against engine, YOLO26 is faster at the same size. We also report what matters for anyone using the benchmark: its scoring protocol adds 5 to 10 AP, its host labels sit at the image center, its box labels are offset from the image by 1.5 pixels, and its images can be rebuilt from the public survey data, which recovers sky positions and doubles as extra training data. We suggest that future work report host identification F1, as a measure closer to catalog use: D-FINE-seg M 71.8, YOLO26-pose M 70.5, RF-DETR 63.8, Gal-DINO 59.2.

---


### 327. [Blind to What They Can Fix: A Detection Gap in Self-Improving Agents](https://arxiv.org/abs/2611.29807)

**<font color=#1a73e8>作者：</font>** Teng Cao, Yu Deng, Kristian Kersting  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents can write programs that carry out a task without calling a model at every step, so the task runs fast and its logic stays open to inspection. Agents improve these programs by running them, studying their failures, and revising the code, a form of recursive self-improvement (RSI). We ask whether this process also yields runtime checks that can be trusted. In five task domains, with up to seven author models, agents bring their programs to high scores. Yet when the environment changes, the checks they were told to write stay silent on half or more of the resulting failures in four domains. These failures can be detected and repaired: a monitor built from records of normal runs catches most of them in three domains, and the same agents usually repair them once called. The checks do not examine the recorded relations that reveal the failures, and the strongest agent writes checks that catch most of them once told that its checks are the only thing that calls it back. An unreported failure stays unrepaired, which limits what self-improvement is worth in autonomous operation. Evaluations of self-improvement should measure not only scores but also whether a system notices its own failures.

---


### 328. [Information-Theoretic Analysis of Multi-Objective Bandits: Pareto Violations & Gap-Based Regret](https://arxiv.org/abs/2611.29808)

**<font color=#1a73e8>作者：</font>** Muhammad Qasim Elahi, Murat Kocaoglu, Mahsa Ghasemi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study Bayesian multi-objective bandits and ask an information-theoretic question: what aspects of an unknown environment must be resolved to achieve low regret? We show that the answer depends on the regret criterion and the information needed to represent its loss. For Pareto-violation regret, which incurs unit loss whenever a dominated action is selected, the Pareto-optimal set is a natural information target. We introduce a predictive separation measure for competing candidate Pareto sets, connect it to information gain about the unknown set, and use this connection to analyze Thompson Sampling and develop an Information-Directed Sampling strategy. We establish sublinear Bayesian regret under uniform and polynomially decaying separation and prove a lower bound showing that weak separation can impose an unavoidable statistical cost. We then study gap-based Pareto regret, which quantifies the magnitude of Pareto suboptimality. Here, Pareto-set information is generally too coarse: distinct environments can share the same Pareto set while inducing different reward geometries and Pareto gaps, and averaging environments consistent with one Pareto set need not preserve Pareto dominance. This motivates retaining finer information about the environment. We develop parameter-level information-theoretic analyses of Thompson Sampling and Information-Directed Sampling to derive gap-based regret guarantees. Under sublinear information budgets, Pareto Thompson Sampling also achieves sublinear gap regret while recovering the full Pareto set on the same run, with a related guarantee for a fixed mixture with gap-based IDS. Together, our results reveal a hierarchy of information requirements: binary Pareto membership can be controlled through set-level information, whereas quantitative Pareto-gap suboptimality can require finer knowledge of reward geometry.

---


### 329. [Data-Quality-Aware Fundus Classification with Anatomy-Guided Glaucoma Assessment and Cross-Dataset Evaluation](https://arxiv.org/abs/2611.29834)

**<font color=#1a73e8>作者：</font>** Imdadul Haque Sourav, Marjana Jannat Miti, Md. Jehadul Islam Mony  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Background: Deep learning fundus classifiers often perform well internally, but duplicated images, inconsistent labels, acquisition differences and poor threshold transfer can undermine their reliability. We assess nine-class classifiers beyond internal accuracy, using a data audit, frozen-model external evaluation and an anatomy-guided specialist. Methods: Nine-class experts (ConvNeXt-Small, EfficientNetV2-Small, DenseNet169) were trained with three seeds. Auditing 5,318 images for exact duplicates and cross-label conflicts removed 464 conflict groups (942 images) and six same-label copies, leaving 4,370 images. An anatomy-guided glaucoma specialist read disc-centred crops with vessel and disc/cup segmentation maps, plus cup-to-disc features. Frozen models were evaluated on RFMiD and JSIEC, and a prespecified comparison on REFUGE was replicated on ORIGA, G1020 and PAPILA. Results: ConvNeXt-Small reached an internal accuracy of 0.910, macro-F1 of 0.917 and AUC of 0.982; disc and cup Dice scores were 0.966 and 0.915. Across seeds, the fixed anatomy-guided mix left internal accuracy unchanged relative to equal soft voting (-0.001) but raised mean external closed-set accuracy by 4.9 percentage points on RFMiD (positive in two of three seeds) and 2.3 on JSIEC. On REFUGE (800 photographs) it improved balanced accuracy by 7.4 percentage points (95% CI 5.1 to 9.5), and by 2.1 on ORIGA, with positive gains on G1020 and PAPILA. Thresholds transferred poorly (REFUGE sensitivity 0.950, specificity 0.411). Conclusions: Retinal classifiers should be judged by data-quality auditing, anatomy-informed modelling and multi-cohort evaluation. Anatomy-guided fusion improved transfer at no internal cost, but gains varied by cohort and thresholds did not transfer, so internal metrics alone do not establish reliable performance.

---


### 330. [Continuous-time 4D Reconstruction via Event-guided Latent Feature Interpolation](https://arxiv.org/abs/2611.29838)

**<font color=#1a73e8>作者：</font>** Gwangtak Bae, Seunggu Kang, Junho Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent geometric foundation models can successfully convert a video sequence into frames of registered point clouds, but cannot predict moments beyond the observed temporal resolution. We propose a continuous-time 4D reconstruction method that extracts 3D structure and camera poses at any time instant, with additional guidance from event-camera measurements. While event cameras provide evidence at microsecond resolution to continuously fill the temporal gap, integrating them into existing RGB-based foundation models remains challenging. We formulate the problem as interpolation in the latent feature space and augment event-based losses in the image space as an auxiliary task to boost accuracy. Operating in the latent space leverages the powerful geometric priors of foundation models, while the event loss provides physically grounded guidance. To effectively address the lack of paired training data, we further propose a self-supervised training framework that uses pseudo-ground-truth labels of estimated geometry and simulated events generated from high-frame-rate RGB videos. Through extensive experiments, we demonstrate that the proposed pipeline outperforms baselines that temporally interpolate either the input RGB videos or the estimated geometry, and that it generalizes to unseen real-world scenarios. Controlled experiments with synthetic corruptions show that it remains robust under motion-blur and low-light conditions.

---


### 331. [Dynamics Forcing: Mitigating Error Accumulation in Causal Video World Models](https://arxiv.org/abs/2611.29839)

**<font color=#1a73e8>作者：</font>** Xin Zhou, Cong Miao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Causal video world models generate block by block from their own previous outputs. Small errors in early blocks are fed back as history and grow until the scene and the robot fall apart. Teacher forcing trains on clean ground-truth history, so the model never sees the history it will actually condition on, and it also finds a shortcut: copying the previous frame instead of predicting how the scene changes. We present Dynamics Forcing, a training scheme that keeps real video as the only supervision and reshapes how history is presented. History is perturbed in three ways: random noising, self-resampling by the model itself, and joint denoising, in which the most recent blocks are still partly noisy when the next block is predicted. On top of this we move history guidance and first-frame anchor guidance from inference into training, so that the model is pushed to use its history and its reference frame rather than ignore them. Dynamics Forcing needs no teacher model, no distillation, and no additional model at inference. Applied to a 5B video model with LoRA on 77 hours of manipulation video on a single GPU, it better matches unseen real continuations and reduces error accumulation.

---


### 332. [When Source-Domain Validation Fails to Transfer: A Staged Study of Hyperparameter Selection](https://arxiv.org/abs/2611.29846)

**<font color=#1a73e8>作者：</font>** Veet Zaveri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hyperparameters for an unseen domain are often selected using held-out examples from the available source domains. Withholding entire source domains during validation seems to better reflect deployment shift, but does this produce better selections on independent targets? We investigate this question through two complementary studies. A preliminary factorial experiment crosses particle swarm optimization and random search with pooled source validation and a leave-one-source-domain-out mean-minimum fitness on PACS and Multi-Domain Sentiment. The domain-aware fitness does not provide a consistent target advantage. We then separate selector development from confirmation using a shared pool of 64 configurations per task across four image benchmarks. Complete target-performance landscapes on VLCS and Office-Home inform one rule: retain the top 16 configurations by pooled source validation, then select the largest leave-one-source-domain-out mean-minus-standard-deviation score. The rule is frozen before evaluation on TerraIncognita and SVIRO. Across their 14 target domains, its equal-dataset-weighted balanced-accuracy difference from pooled validation is +0.097 percentage points (95% bootstrap interval [-0.685, +0.960]), with five wins and nine losses. Exploratory analyses reveal substantial variation across datasets, target domains, and training seeds. These results do not establish equivalence or a general failure of domain-aware validation. They show that the evaluated source-domain criteria did not establish reliable target gains under the tested protocols, and motivate assessing selection rules on datasets independent of those used to develop them.

---


### 333. [Ego2Wrist: Bootstrapping Wrist-View Synthesis from Egocentric Video](https://arxiv.org/abs/2611.29850)

**<font color=#1a73e8>作者：</font>** Ziyao Zeng, Xiatao Sun, Hao Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Wrist cameras provide an action-centric view that is directly relevant to robot manipulation. However, collecting human wrist-camera videos at scale is challenging due to cumbersome setups that can interfere with natural hand movements. In contrast, head-mounted human egocentric videos are much easier to scale. We introduce Ego2Wrist, which synthesizes synchronized wrist-camera views from human egocentric videos and task descriptions. Trained on approximately 940 hours of paired head- and wrist-camera recordings, Ego2Wrist jointly generates three views. To evaluate generated wrist views without ground truth, we propose hand-centric cross-view consistency (HCC), which measures consistency between generated wrist views and corresponding hand regions in the input head view. HCC ranks model checkpoints comparably to ground-truth-based LPIPS, and human evaluators prefer HCC-selected generations in 77% of responses. Evaluated on four datasets, Ego2Wrist outperforms fine-tuned WorldWander, reducing LPIPS by 28% and receiving human preference in 76% of responses. More importantly, HCC facilitates recursive self-improvement on in-the-wild egocentric videos by selecting generated wrist views for further training. Generation quality progressively improves over three rounds. These results demonstrate a scalable approach to generating real-world wrist-view human manipulation videos for robot policy training.

---


### 334. [LexiDet-OVD: Benchmarking Lexical Sensitivity in Open-Vocabulary Object Detection](https://arxiv.org/abs/2611.29851)

**<font color=#1a73e8>作者：</font>** Amit Thakur, Mukesh Singhal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary object detectors localize objects from free-form text prompts, but their reliability depends on how users describe the target. Standard evaluations usually test a fixed class name, leaving prompt-induced failure modes underexplored. We introduce LexiDet-OVD, a benchmark and metric suite for studying lexical sensitivity in open-vocabulary object detection. We organize prompt sets into equivalent, conditional, and broad semantic scopes, and evaluate four detector families on fixed COCO and LVIS samples, each covering 30 classes (800 held-out COCO images and 1,000 LVIS images). Beyond mean and worst-prompt AP50, we report P10, CVaR at 20%, leave-one-prompt-out influence, detection agreement, box consistency, and confidence variance using one-to-one multi-instance matching. Equivalent-prompt best-to-worst gaps range from 5.3 to 23.4 points on COCO1000 and from 5.1 to 29.9 points on LVIS1000-30c, showing that strong average accuracy and lexical stability are distinct properties. We compare maximum-score selection, weighted-box fusion, Prompt Consensus, and an exploratory fusion rule. Aggregation recovers performance in several settings, but no method dominates all model-dataset pairs. A controlled Detic/SHiNe comparison further shows that semantic hierarchy enrichment does not by itself eliminate lexical sensitivity. These results support reporting prompt-distribution robustness alongside conventional open-vocabulary detection accuracy.

---


### 335. [World Models Are the Right Foundation for Simulating Mars Terraforming](https://arxiv.org/abs/2611.29856)

**<font color=#1a73e8>作者：</font>** Sameera S Kashyap, Akshitha Nagaraj, Razvan Marinescu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Terraforming Mars is a long-horizon, action-conditioned control problem that requires predicting atmospheric responses to interventions over centuries to identify effective policies. This position paper argues that physics-regularized recurrent state-space world models are the most promising foundation for this setting. Data-driven climate emulators lack action-conditioning, and physics-based general circulation models (GCMs) are too expensive for policy search. Among learned world models, recurrent state-space architectures with physics constraints are better suited than transformer-based alternatives: they provide native uncertainty quantification through their stochastic-deterministic decomposition, remain stable under sparse non-terrestrial training data, and enforce physical consistency at each rollout step. To make this position concrete, we describe a potential architecture combining JEPA-inspired latent encoding, universal differential equation constraints, and a Dreamer-lineage planning head. We also introduce MarsWorld, an open benchmark proposal for intervention-conditioned planetary world models, and discuss broader implications and objections.

---


### 336. [Comparative Analysis of Machine Learning Classifiers for Lightweight IoT Intrusion Detection Using Feature Reduction](https://arxiv.org/abs/2611.29869)

**<font color=#1a73e8>作者：</font>** Shaker Nawasra  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine learning-based intrusion detection systems can improve IoT security, but high-dimensional traffic features and imbalanced datasets may reduce model reliability and deployment feasibility in resource-constrained environments. This study presents a lightweight binary IoT intrusion detection framework using an approximately balanced CICIoT2023 derived dataset, feature reduction, and comparative machine learning evaluation. The original multi-class attack labels were converted into two classes: Benign and Malicious. To reduce class bias, malicious traffic was randomly undersampled to obtain an approximately balanced binary dataset. Information Gain Ratio and Gini Decrease were then used to rank traffic features and generate reduced feature subsets of 38, 30, 20, 10, 5, and 3 features. Five machine learning classifiers, including Random Forest(RF), Decision Tree(DT), Naive Bayes(NB), Logistic Regression(LR), and Support Vector Machine(SVM), were evaluated using 5-fold cross-validation. The results show that Random Forest achieved the strongest overall performance. In particular,the 20-feature subset achieved accuracy of 99.1% and MCC of 0.982, matching the full-feature model while reducing feature dimensionality by approximately 47.4%. The 10-feature subset also maintained strong performance with accuracy of 98.9% and MCC of 0.979, reducing the feature space by approximately 73.7%. These findings demonstrate that balanced binary classification and progressive feature reduction can preserve detection effectiveness while improving lightweight IDS feasibility.

---


### 337. [Deep Discriminative Feature Fusion of Convolutional and Attention-Based Recurrent Representations for Subject-Independent ECG Stress Recognition](https://arxiv.org/abs/2611.29870)

**<font color=#1a73e8>作者：</font>** Zeeshan Ahmad, Muhammad Rehman Zafar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Stress has become a significant concern because of its negative impact on both physical and mental health and therefore drives the need for reliable automated systems to assess stress levels. Electrocardiogram (ECG) signals provide a non-invasive and objective measure of physiological stress responses and have emerged as a promising modality for continuous stress monitoring. While deep learning techniques have achieved encouraging results in ECG-based stress detection, many studies focus only on one type of feature representation, and therefore limit their ability to capture both the morphological patterns and temporal dynamics embedded in ECG signals. To address this limitation, in this paper, we propose three deep learning-based feature fusion frameworks for ECG-based stress classification. These are Residual Feature Fusion (RFF), Bidirectional Feature-Wise Cross-Attention Fusion (BFCAF), and a novel Cross-Attention Residual Fusion (CARF) framework that combines the strengths of residual learning and bidirectional cross-attention within a unified architecture. A 1D Convolutional Neural Network (1D-CNN) and a BiLSTM-Attention network are used to extract complementary morphological and temporal representations from ECG signals, respectively. The proposed fusion frameworks leverage these heterogeneous representations to improve feature interaction, information preservation, and stress discrimination. The proposed frameworks are evaluated using subject-independent Leave-One-Subject-Out Cross-Validation (LOSOCV) on the RML and WESAD datasets for three-class stress classification. Experimental results show that the proposed feature fusion methods consistently improve performance over individual CNN and BiLSTM models, with CARF achieving the highest accuracies of 83.1% and 77.91% on the RML and WESAD datasets, respectively.

---


### 338. [Weight Averaging at Small Budgets Confounds Formula-Labeled Pretraining in Microstructure-Property Regression: A Pre-Specified Study with Post Hoc Rechecks](https://arxiv.org/abs/2611.29876)

**<font color=#1a73e8>作者：</font>** Jonghyun Lee, Soojung Kang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Closed-form physics formulas can label synthetic microstructures at no cost, so supervised pretraining on those labels is an alternative to self-supervised pretraining when labels are scarce. One pre-specified protocol tests this on two public simulated benchmarks, two-phase conductivity and short-fiber stiffness: a ConvNeXt-Small is pretrained on 150,000 synthetic images by formula regression or masked reconstruction and fine-tuned on 100, 400, or 1,600 labels. Five fine-tuning seeds from one formula checkpoint have mean residual correlations of 0.994 (conductivity) and 0.999 (stiffness). On conductivity the formula network compresses its predictions (slope 0.64) and has four times the 400-label error of ImageNet initialization. Two confounds interact: the generator renders the low-conductivity phase with the opposite contrast polarity, and the exponential moving average (EMA; decay 0.995, no bias correction) still holds 16% of the initial weights after the 400-label schedule. Without the EMA the slope is 0.97, and over three subsets and five seeds the mismatched checkpoint has 1.4 times the ImageNet error (0.0119 versus 0.0084). Three pretraining runs per polarity leave the comparison inconclusive: matched means (0.0086, 0.0111, 0.0118) fall below mismatched means (0.0119, 0.0120, 0.0123) in aggregate (0.0105 versus 0.0121) but overlap on two of three subsets, and the matched spread (0.0032) exceeds the mismatched spread (0.0004). On stiffness without the EMA, formula pretraining lowers the 100-label error by 18% versus ImageNet over five seeds, including a re-initialized head, while ImageNet seeds also correlate at 0.992. Weight averages that start at the pretrained weights can dominate small-budget comparisons and should be rechecked at the last weights.

---


### 339. [Reparameterizing Your Object Detectors for Weight Space Programming](https://arxiv.org/abs/2611.29882)

**<font color=#1a73e8>作者：</font>** Chien-Yao Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Weight-Space Programming (WSP) edits network weights without backpropagation, yet directly editing converged object detectors stalls or collapses because set prediction penalizes duplicate boxes as false positives while compact parameterizations trap weights in an isotropic Euclidean minimum. We propose Inverse-Reparameterized Object-Detection WSP (IR-ODWSP), lifting detector layers via exact function-preserving operators (E, C) into decoupled moment, 2D-DCT, PCA, and Stiefel-Procrustes subspaces. Solving winner-exclusive updates and folding back (Delta Params=0%, Delta FLOPs=0%) induces an anisotropic Riemannian metric, improving all 26/26 MS COCO settings across 17 YOLO26, EdgeCrafter, and RF-DETR detectors (up to +0.31 APs), +1.42 mAP cross-basin COCO-O, zeroimage repair (+2.95 mAP), and label-free weather adaptation (+2.79 AP). Without retraining, IR-ODWSP supports -100% to +100% latency budgets across bridged contraction, 1.00x folding, dynamic (IR-ODWSP-DYN), and static (IR-ODWSP-SG) graphs: -10% retains 51.62 AP / 33.48 mAP, while positive budgets scale monotonically (+0.30 AP at +10%, +1.12 on RF-DETR-N; 54.83 AP at +100%; 55.91 AP / 35.44 mAP in IR-ODWSP+). Source code is released at this https URL.

---


### 340. [Particle Belief Representations for Reinforcement Learning under Partial Observability](https://arxiv.org/abs/2611.29884)

**<font color=#1a73e8>作者：</font>** Himanshu Gupta, Brendan Crowe, Christoffer Heckman 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Particle filters flexibly represent complex, multimodal beliefs but expose them as weighted, unordered sets incompatible with conventional fixed-dimensional policies. We study particle-belief encodings as inputs to reinforcement-learning policies while holding belief estimation and policy optimization fixed. We compare statistical summaries, cumulant-generating-function (CGF) features, and permutation-invariant set encoders. Trainable encoders are learned end-to-end or pretrained through belief reconstruction or task-specific prediction. Across eight tasks, pooling-based set encoders and gradient CGF features are reliable end-to-end, while the Set Transformer achieves the highest performance with appropriate pretraining. Task-specific pretraining helps when its target captures decision-relevant belief structure, whereas reconstruction pretraining and latent alignment provide more selective benefits. For selecting and training particle-belief encoders in partially observable Markov decision processes, our results show that an encoding that reconstructs the belief well is not necessarily a good input for control.

---


### 341. [Second-Order Dynamics in Noisy RNNs Produce Exploration and Temporal Compression in Replay](https://arxiv.org/abs/2611.29888)

**<font color=#1a73e8>作者：</font>** Josue Casco-Rodriguez, Nanda H. Krishna, Richard G. Baraniuk  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Biological neural networks (like the hippocampus) can internally generate "replay" resembling stimulus-driven activity. Recent computational models of replay use noisy recurrent neural networks (RNNs) trained to path-integrate. Replay in these networks is described as Langevin sampling, but this theory alone fails to capture the environmental exploration and temporal compression observed in real biological replay. To close this gap, we re-examine spontaneous noisy RNN activity ("replay") as Langevin sampling, one timestep at a time, from a time-series distribution resembling lived experiences (unlike previous works which defined sampling as Monte Carlo inference over a static distribution). We provide a normative second-order Langevin sampling framework wherein spike-frequency adaptation drives spatial exploration at the cost of speed, and momentum via dendritic input differentiation drives temporal compression. We numerically verify our framework via simulations of noisy RNNs trained on 2D triangular and T-maze navigation activity, and others trained on place cell activity of synthetic rats. Crucially, we observe that simultaneous adaptation and momentum increases both replay exploration and speed, and provide one of the first accounts for biologically plausible temporal compression in rate-based RNN replay. Our findings encourage experiments into whether dendritic input differentiation, or other mechanisms, may support temporal compression in memory circuits like the hippocampus.

---


### 342. [Segment Anything In-Context via Visual Demonstrations](https://arxiv.org/abs/2611.29896)

**<font color=#1a73e8>作者：</font>** Yuzhu Wang, Manni Duan, Hongliang Ye 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present the Segment Anything Model via Visual Demonstrations (SAYD), a foundation model for in-context segmentation. Given visual demos comprising prompt images and their segmentation masks, SAYD segments coherent regions (e.g., objects or their parts) in a query image by establishing visual correspondences between the prompts and the query. SAYD generalizes to previously-unseen segmentation tasks, including those requiring tacit visual knowledge or involving concepts that are difficult to articulate unambiguously in language. We train SAYD on 12 public datasets originally curated for panoptic segmentation using our proposed techniques, including a lightweight mask decoder for prompt-agnostic mask generation and a learning mechanism for recognizing novel query classes absent in the prompts. These innovations enhance both computational efficiency and out-of-domain generalization. Consequently, SAYD significantly outperforms existing methods of in-context segmentation and open-vocabulary segmentation across 24 out-of-domain benchmarks, spanning natural, biological, ecological, cosmological, medical, pathological, and satellite imagery.

---


### 343. [From Patterns to Threats: A Deep Learning Model for Anomaly Detection in Cyber-Physical Systems](https://arxiv.org/abs/2611.29903)

**<font color=#1a73e8>作者：</font>** Kayode L. Ogunsusi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cyber-physical systems increasingly rely on interconnected sensing, communication, and control components, creating a need for reliable detection of abnormal behavior. This study proposes a Deep Autoencoder for anomaly detection using the Edge-IIoTset dataset. After preprocessing the full dataset, 2,219,201 observations and 38 numerical features were retained. The proposed model employed a 38-24-12-6-12-24-38 encoder-decoder architecture and was trained exclusively on normal observations to learn representative patterns of expected system behavior. Anomaly decisions were based on reconstruction error, with the classification threshold selected independently from validation data by maximizing the F1-score. To assess model stability, five independent runs were conducted using different random seeds, and results were reported as mean plus or minus standard deviation. The proposed Deep Autoencoder achieved an accuracy of 0.9195 plus or minus 0.0061, precision of 0.9602 plus or minus 0.0204, recall of 0.7348 plus or minus 0.0095, F1-score of 0.8325 plus or minus 0.0121, ROC-AUC of 0.8825 plus or minus 0.0339, and PR-AUC of 0.8640 plus or minus 0.0286. Compared with a Simple Autoencoder baseline, the proposed model improved recall and F1-score while reducing the false positive rate. The results demonstrate that the proposed reconstruction-based representation learning approach can provide an effective and reproducible method for detecting anomalous behavior in cyber-physical environments.

---


### 344. [Safe Quantum Stochastic Linear Bandits](https://arxiv.org/abs/2611.29904)

**<font color=#1a73e8>作者：</font>** Ruizhe Zhang, Junyi Wu, Guang Lin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We initiate the study of safe quantum stochastic linear bandits, in which a learner maximizes an unknown linear reward while satisfying unknown linear mean constraints at every interaction. Under coherent unitary access to the joint reward-and-constraint distribution, we develop QRS-COLTS, a staged quantum resampled-scaling analog of constrained linear Thompson sampling (COLTS). With high probability, QRS-COLTS plays only feasible actions and achieves regret that is polylogarithmic in the query horizon and scales only with the square root of the number of constraints. We also study a model in which the learner queries superpositions of actions while an unsafe-action flag, a "bomb" that terminates the interaction upon violation, is measured after every query. In this setting, the bomb provides exact membership access to the safe set, and query regret is evaluated over the action superposition. For this model, we propose BCO-QLinTS, which selects feasible actions via bomb-certified quantum convex optimization without estimating the constraint matrix. Its query-weighted regret remains polylogarithmic in the horizon, with the constraints entering the bound only through the geometry of the safe set.

---


### 345. [Bridging the Gap between Continual Learning and Test-Time Adaptation with Domain Preview](https://arxiv.org/abs/2611.29905)

**<font color=#1a73e8>作者：</font>** Frédéric Li Combeau, Nicolas Michel, Toshihiko Yamasaki  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Domain shift is a major problem for training machine learning models. While Continual Learning (CL) assumes distribution shift during training and Continual Test-Time Adaptation (CTTA) considers new domains at test time, setups that require explicit online adaptation to domain shift during both phases remain under-explored. We propose continual learning with domain preview (CL-P), a new combination of CL and TTA where both train and test data suffer from distribution shift. The training phase of CL-P is analogous to domain-incremental learning while the testing phase consists of a TTA phase on a future domain (which we call preview), and an evaluation phase on all seen domains. The model must then adapt to new domains at train and test time. In this paper, we evaluate mainstream CL and TTA methods that adapt only at train or test time, as well as their naive combination. Experimentally, TTA heavily damages the domain on which the CL method has just trained and increases forgetting. Notably, this damage mostly comes from the BatchNorm statistics shared by all domains. In that sense, we propose DOSE (Dosing by Online Statistics of Each domain), which allows a seamless combination of any CL and TTA methods by adaptive domain inference at test time, where the adaptation is applied to each image in proportion to the probability that it comes from the preview domain. Through extensive experiments with ResNet and ViT backbones, various combinations of CL and TTA baseline methods and datasets considering diverse domains, we show that DOSE matches or improves on CL methods alone in all 24 settings and on the naive combination in all but one. The code can be found in appendix.

---


### 346. [Dynamic Gaussian Scene Reconstruction by Integrating Events and Structural Priors](https://arxiv.org/abs/2611.29920)

**<font color=#1a73e8>作者：</font>** Zihao Yu, Guozhen Liu, Jie Yan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing approaches to event-based dynamic Gaussian reconstruction rely on two assumptions for support augmentation and reliability estimation. First, existing Gaussians can absorb reconstruction errors. Second, photometric optimization has converged sufficiently to estimate reliability using analytical variance. Both assumptions can fail under fast motion. When the first fails, regions without Gaussian support cannot generate densification candidates. When the second fails, Gaussians in moving regions where optimization has not converged may be excluded as motion references. We propose Event-Structure Collaborative Dynamic Gaussian Reconstruction (ESC-DGR), using event observations independent of both conditions. Events first identify changes that require additional support, placed only where rendered depth is valid. The augmented representation still needs reliable motion references. Online rendering statistics and historical event evidence therefore propagate displacement estimates from reliable Gaussians to weakly observed neighborhoods. These references describe dominant motion at the frame-interval timescale. Target-time events therefore further condition bounded position residuals for active Gaussians. Support placement, reference selection, and residual prediction thus operate on the same evolving representation within one optimization run. For event-driven monocular dynamic scene reconstruction, our method achieves the best reconstruction quality among the evaluated methods on the E-D3DGS benchmark. Relative to E-D3DGS, dynamic-region PSNR (dPSNR) improves by 1.02 and 1.45 dB on synthetic and real scenes, respectively. The total dynamic Gaussian count across eight synthetic scenes decreases by 8.5%. Although mean frame rate decreases by about 21%-25% relative to E-D3DGS, rendering remains above 80 FPS in all twelve scenes. Code: this https URL.

---


### 347. [Beyond PINNs: Boundary-Enriched Holomorphic Networks for Laplace Problems](https://arxiv.org/abs/2611.29922)

**<font color=#1a73e8>作者：</font>** Andrei Vlad Nicula, Kalp Shah, Robert-Stefan Sofroni 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural networks (PINNs) solve partial differential equations by penalizing their residual, but this formulation can be difficult to optimize for solutions with singular behaviour. We focus specifically on the two-dimensional Laplace equation, whose strong analytical structure allows the governing equation to be enforced directly in the neural representation. We compare a hybrid harmonic-neural model with a holomorphic neural network whose output is harmonic by construction and therefore requires only boundary training. We further enrich the holomorphic model with singular functions chosen according to the interior angle and boundary conditions at each junction of boundary segments. On six singular benchmarks, the enriched model is the most accurate of the neural models we compare. On the four with a closed-form solution, however, that solution lies in the span of the enrichment terms, and a least-squares fit of these terms alone is exact to rounding error. On Motz's problem and the cracked beam, the neural core reduces the relative error of the recovered leading singular coefficient from about $10^{-2}$, for a least-squares fit with the same four terms, to about $10^{-6}$, and on four variants whose solution has a smooth part outside the span, the network is $4\times10^{4}$ to $2\times10^{7}$ times more accurate than a fit of its singular terms alone; classical least-squares fits with more singular terms, or with harmonic polynomials and rational poles, are more accurate still. Our results demonstrate how exploiting problem-specific analytical structure can provide an alternative to base and residual PINNs for challenging scientific computing problems.

---


### 348. [KGLP-Net: Kalman-Reliable Global--Local Learning With Group Fisher Pruning for Hyperspectral Image Classification](https://arxiv.org/abs/2611.29944)

**<font color=#1a73e8>作者：</font>** Wenshuai Deng, Wen Xie, Abdel Hamid Soliman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate hyperspectral image (HSI) classification requires both the effective integration of broad spatial context and fine-grained spectral--spatial information surrounding target pixels. However, the reliability of these complementary representations may vary considerably across heterogeneous scenes, and uncertainty estimates obtained during feature fusion are rarely exploited to guide subsequent model compression. To address these challenges, we propose Kalman-Reliable Global--Local Learning with Group Fisher Pruning (KGLP-Net), a unified framework that couples uncertainty-aware feature fusion with reliability-guided structured pruning. Specifically, an asymmetric dual-view architecture employs a Global Mamba Encoder to capture long-range spatial dependencies and a Local CNN Encoder to extract fine-grained spectral--spatial features from target neighborhoods. To adaptively integrate these complementary representations, Kalman-Reliable Fusion (KRF) estimates their relative uncertainties in feature space and performs a Kalman-inspired posterior update, treating global features as a contextual prior and local features as an observation. Building upon the resulting posterior uncertainty, Kalman-Reliable Group Fisher Pruning (KRGF) quantifies group-level reliability through normalized posterior precision and integrates it with Group Fisher importance to identify and prune Kalman-coupled channel groups, enabling structurally consistent model compression. Experiments on four public HSI datasets demonstrate that the resulting Compact48 model, with a hidden width of 48, achieves the highest overall accuracy among ten representative competing classifiers. Compared with the unpruned Dense64 model, Compact48 reduces the number of parameters, FLOPs, and inference time by 38.5%, 34.8% and 37.6% on average, respectively, while incurring only a 0.03-percentage-point decrease in mean overall accuracy.

---


### 349. [Beyond Fixed Prompt Configuration: Alternating Policy Learning for Adaptive Topology-Based Prompting in Few-Shot Graph Learning](https://arxiv.org/abs/2611.29950)

**<font color=#1a73e8>作者：</font>** Yizhuo Ma, Yihong Huang, Rongzheng Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Prompt Learning (GPL) adapts frozen pre-trained graph models to few-shot graph tasks through a small set of trainable prompts that encode task-specific information. Topology-based prompting instantiates this idea by augmenting an input graph with new prompt nodes and edges, yielding promising performance. However, prompt content and propagation structure are coupled, making it difficult to assess their individual effects and learn compatible configurations. In this paper, we empirically analyze two challenges in learning adaptive policies for topology-based prompting: asymmetric performance effects and coupled configuration selection. We then propose TTPR, a two-stage reinforcement framework that alternately optimizes two policies to generate adaptive configurations, with each policy conditioned on configurations generated by the other fixed policy. These conditional updates separate policy evaluation while preserving configuration compatibility. Specifically, TTPR models an edge-level policy to construct connection patterns and optimizes it with Connection Relative Policy Optimization (CRPO) through group-wise comparisons of complete connection patterns. The other is a node-level policy that generates prompt-node schemes and is optimized with Incremental Node Proximal Policy Optimization (INPPO) through incremental prompt-count decisions and feature generation. Across diverse datasets and pre-training strategies, TTPR ranks first in 8/10 few-shot node classification settings and attains the highest average performance across graph classification benchmarks.

---


### 350. [Yggdrasil: Tree-Routed Recurrent Experts for State Tracking and Fast CPU Inference](https://arxiv.org/abs/2611.29954)

**<font color=#1a73e8>作者：</font>** Cosmo Santoni  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parallel-trainable recurrences such as Mamba, linear attention, and DeltaNet offer constant-cost streaming inference, but they suffer from two limitations: 1) they struggle to track discrete state, and 2) they read every parameter at every step, tying model capacity directly to CPU latency. We introduce Yggdrasil, a recurrent architecture that decouples capacity from per-step compute by looking up each layer's transition in a large, tree-routed bank of recurrent experts. Each router addresses its bank using the current token and the state of the layer below. We prove that this cross-layer context is necessary---a single token-indexed layer of non-expanding transitions with finitely many reachable states cannot perform conditional resets---while avoiding feedback from the layer's own past preserves parallel-scan training. Because each step traverses one tree path and reads a single expert per layer, active weights stay within a few hundred kilobytes in CPU L2 cache while the full bank resides in RAM. Among the parallel-trainable models we evaluate, Yggdrasil is the only one to solve all five state-tracking tasks. At matched active parameter counts, it achieves the lowest test bits on enwik8 (1.540 bpb) and the human genome hg38 (1.567 bpb), while stepping $3.0\times$ and $3.3\times$ faster on a single CPU core ($6.7\,\mu\mathrm{s}$ and $5.8\,\mu\mathrm{s}$) than the fastest streaming baseline, and delivering the highest GPU throughput of all models at batch 1024. On the Genomic Benchmarks, it is the strongest causal model at matched active parameters (86.0% mean accuracy).

---


> [!TIP]
> 当前位于：**301-350**（第 7/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-569](./part-12.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
