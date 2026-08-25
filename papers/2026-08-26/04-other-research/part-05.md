# 📦 其他研究 | 2026年08月26日

> 本类共 **361** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-361](./part-08.md)

---

### 201. [From Symmetry to Invariance: Learning Galois Equivalent Representations in Finite Fields](https://arxiv.org/abs/2608.22513)

**<font color=#1a73e8>作者：</font>** Zheng Zhang, Na Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural networks can learn algebraic operations from finite examples, but it remains unclear whether this ability transfers across mathematically equivalent representations of the same operation. We study this question through multiplication in finite fields under changes of basis. The Galois action organizes basis representations into orbits, and bases in the same orbit induce the same coordinate multiplication map. This structure allows us to separate learning multiplication from transferring it to basis representations that are not used for training. We examine several ways of providing or recovering the relevant orbit structure, including invariant labels, basis matrices, orbit recognition, and algebraic decomposition. Our main approach trains a model to predict the Galois action between basis representations. Repeated applications of the learned transformation are then used to construct a canonical representative for each orbit, which supports multiplication on held-out bases through exact canonical matching. This provides a concrete mechanism for converting a learned algebraic symmetry into an invariant representation that can be used for transfer.

---


### 202. [TRACE: Temporal Retrieval with Anchored and Convergent Evidence for Long-Horizon Video Understanding](https://arxiv.org/abs/2608.22516)

**<font color=#1a73e8>作者：</font>** Pengyiang Liu, Junbo Niu, Xiaoyang Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A long-video answer is evidence-supported only when the frames decoded from the video cover every event the answer depends on. Existing evaluations score final-answer correctness or predicted evidence intervals, but the frames a method decodes before answering are rarely audited, so correct answers can still rest on incomplete observation. We introduce VES-Bench, a 600-question benchmark of Temporal Ordering and Event Counting items over 348 public long videos. Each item carries a jointly necessary set of evidence intervals, letting us audit at three strictness levels whether a method's decoded frames cover every one of them. We also propose TRACE, a training-free agent that grounds answers in raw visual clips, builds an evidence bundle round by round, and stops only when the answer stabilises as the bundle grows and a final pass over the same clips returns the same answer. Under a same-backbone audit, TRACE answers 50.7% of questions correctly with at least two decoded frames inside every evidence interval, at 98.7 frames per question: over 10 points above uniform decoding at 128 frames (40.2%), and within 2.6 points of uniform decoding at 256 frames at 0.39x its frame cost, while reaching the highest answer accuracy in the audit (63.5%). TRACE also stays competitive on Video-MME (86.1), LVBench (75.6), and LongVideoBench (75.1).

---


### 203. [VISTA: Test-Time Compositional Alignment for Visual Autoregressive Generation](https://arxiv.org/abs/2608.22521)

**<font color=#1a73e8>作者：</font>** Hossein Shahabadi, Niki Sepasian, Mahdieh Soleymani Baghshah  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual autoregressive (VAR) models have emerged as a fast, high-quality alternative to diffusion for text-to-image generation, but like diffusion models they exhibit persistent compositional failures, producing images that violate the attribute bindings and spatial relations specified in the prompt. While a rich line of test-time alignment methods has developed for diffusion, no comparable approach exists for next-scale VAR generation, whose stateful, discrete, multi-resolution sampling process makes existing techniques inapplicable. We close this gap with \textbf{VISTA} (\textbf{Vi}sual Autoregressive \textbf{S}emantic \textbf{T}est-time \textbf{A}lignment), the first gradient-based test-time alignment framework for next-scale autoregressive image generation. Built on Infinity, VISTA intervenes directly in the generation process, optimizing intermediate representations through the frozen transformer to steer visual predictions toward compositional constraints, without modifying model parameters or requiring additional training. VISTA introduces the mechanisms needed to make such optimization stable across scales, together with an extensible objective space that any differentiable constraint on cross-attention can plug into. Across two benchmarks and two model scales, VISTA improves every targeted compositional category, raising the mean targeted score by nearly 20\% on a 2B backbone and almost 6\% on an 8B backbone, with the largest gains on spatial relations. Image quality is preserved: an independent preference model VISTA never optimizes scores its outputs nearly 20\% higher. Notably, the 2B model with VISTA surpasses a backbone four times its size, indicating that a substantial part of the compositional gap between model scales is recoverable at test time.

---


### 204. [On SSI-based Private Decentralized Bidding](https://arxiv.org/abs/2608.22525)

**<font color=#1a73e8>作者：</font>** Andreea Elena Drăgnoiu, Nicoleta Dumitru, Ruxandra F. Olimid  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Private bidding is a process in which participants submit sealed bids, ensuring that their content remains hidden from other bidders during the bidding window. This is essential in competitive environments to ensure a fair and independent evaluation of all proposals. While (public) blockchain enables decentralized bidding and its transparency offers advantages such as public verifiability, without a Trusted Third Party (TTP), current methods struggle to verify whether a bidder is eligible. We propose a framework that leverages Self-Sovereign Identity (SSI) to address these issues by certifying the bid's eligibility and authenticity using the now-established SSI framework. To allow participants to prove they meet the requirements while keeping their bids secret, our model uses Verifiable Credentials (VCs) and cryptographic primitives such as Zero-Knowledge Proofs (ZKPs).

---


### 205. [RS$^3$-Prune: Read-Sparse, Store-Sparse Token Pruning for Video Object Segmentation](https://arxiv.org/abs/2608.22526)

**<font color=#1a73e8>作者：</font>** Avilasha Mandal, Sarvesh Shashikumar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce RS$^3$-Prune, a training-free token-pruning recipe that instantiates as a small set of inference time hooks atop existing video object segmentation (VOS) networks. Modern VOS models have converged on a common, expensive design: an image encoder produces a dense token grid for every frame, and a memory bank accumulates these tokens across all previously processed frames to condition future predictions. As a video grows longer, the resulting token budget governs both per-frame latency and peak GPU memory. Hence these models break on use cases such as --- long-form video or real-time deployment on memory-bounded accelerators. In this work we argue that the right axis along which to compress memory-bank VOS is the token budget itself. RS$^3$-Prune operates in two precise locations within an arbitrary memory-bank VOS pipeline: at the boundary between the image encoder and the memory-attention readout, where we restrict the queries that participate in the cross-frame attention to only a small, geometrically informed subset; and at the boundary between the memory encoder and the memory bank, where we restrict which tokens are ever permitted to enter the bank to those that lie within the object's spatial extent. Over various established benchmarks, RS$^3$-Prune delivers up to $38.8\%$ FPS speedup and reduces $13.1\%$ peak memory usage, while preserving a competitive $\mathcal{J}$&$\mathcal{F}$ compared to the unmodified VOS networks.

---


### 206. [SymmAdapt: Symmetrical Flow Matching for Source-Free Domain Adaptation in Medical Image Segmentation](https://arxiv.org/abs/2608.22532)

**<font color=#1a73e8>作者：</font>** Tal Grossman, Noa Cahan, Hayit Greenspan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Domain shift across imaging modalities and acquisition sites remains a significant barrier to the clinical deployment of segmentation models. Source-free unsupervised domain adaptation (SFUDA) addresses this by adapting a pretrained model to an unlabeled target domain without requiring access to sensitive source data. We introduce a novel SFUDA framework built on Symmetrical Flow Matching, a unified generative model that segments an input image and synthesizes a source-like image from a mask within the same learned flow. By initializing inference from a domain-agnostic Gaussian origin, the model preserves structural consistency across domains and grounds predictions in learned anatomy rather than shifted texture statistics. Our pipeline leverages this symmetry to generate reliable pseudo-labels and corresponding source-like synthetic images from unlabeled target data, creating a generative replay buffer that anchors source knowledge during a generative self-training stage that fine-tunes on a joint set of real target and synthetic source-like images. We evaluate on abdominal multi-organ and cardiac segmentation, covering cross-modality MRI<->CT shifts, and multi-site prostate segmentation. Our approach outperforms SFUDA baselines and is competitive with conventional UDA methods.

---


### 207. [STAGE: Stateful Translation to Agentic Graph Execution with Policy-Scoped Context and Deterministic Control](https://arxiv.org/abs/2608.22538)

**<font color=#1a73e8>作者：</font>** Mengxi Luo, Changjia Chen, An Cao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Policy-governed agents must interpret case evidence while following an authorized procedure. We present \textsc{Stage}, an executable-graph framework that confines model judgment to policy-scoped nodes while placing procedural control in deterministic code. At each node, the model receives task-relevant policy context and returns a typed result, while the coordinator enforces the reviewed execution contract. We evaluate \textsc{Stage} on SOP-Bench Referral Abuse, two $\tau^2$-bench domains, and Smart Dispute, a proprietary banking benchmark. Compared with monolithic full-policy execution, \textsc{Stage} generally improves task success and repeated-run reliability across workflows of varying procedural complexity. The largest gains occur on the deeper Telecom and Smart Dispute workflows, where $\mathrm{Pass}^3$ increases by 7.5--55.0 and 57.2--65.7 percentage points, respectively, depending on the model. These results show that combining policy-scoped context with deterministic procedural control can improve the reliability of policy execution.

---


### 208. [Scaling Curriculum Learning For Autonomous Driving](https://arxiv.org/abs/2608.22549)

**<font color=#1a73e8>作者：</font>** Cevahir Koprulu, David Paz, Feng Tao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Batched simulators for autonomous driving have recently enabled training reinforcement learning (RL) agents at scale, encompassing thousands of traffic scenarios and billions of interactions within a matter of days. Although such high-throughput feeds RL algorithms faster than ever, their sample-efficiency has not kept pace: As the standard training scheme, domain randomization uniformly samples scenarios, thereby consuming a vast number of interactions on cases that contribute little to learning. Curriculum learning offers a remedy by adaptively prioritizing scenarios that matter most to policy improvement. We present CL4AD, the first integration of curriculum learning into batched autonomous driving simulators by framing scenario selection as an unsupervised environment design problem. We introduce utility functions that shape curricula based on success rates and the realism of the agent's behavior, in addition to existing regret-estimation functions. Large-scale experiments in GPUDRIVE demonstrate that curriculum learning achieves a 99% success rate a billion steps earlier than domain randomization, reducing wall-clock time by 77%, and outperforms heuristic curricula with static and dynamic attributes, with only one exception at the largest scale. An ablation under limited compute shows that curriculum learning improves sample efficiency by 67%. We also investigate how utility functions behave at scale, and how prioritized scenarios evolve during training. We release an implementation of CLForAD in GPUDRIVE.

---


### 209. [Neighbor-embedded Graph Neural Network-based Crowd Delivery Traffic Management in Smart City](https://arxiv.org/abs/2608.22555)

**<font color=#1a73e8>作者：</font>** Kishu Gupta, Deepika Saxena, Ashutosh Kumar Singh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The significant upsurge in vehicle traffic presents a considerable challenge in the pursuit of smart mobilization and transportation (SMT) worldwide. Current approaches primarily focus on vehicular traffic management through congestion prediction but fall short in addressing essential objectives such as traffic reduction and appropriate vehicle selection to alleviate congestion in smart cities ($SmCt$). To address these concerns, this work introduces a novel \textit{Neighbor-Embedded Graph Neural Network-based Crowd Delivery Traffic Management} (NeCDM) Model, comprising two key components: the Traffic Congestion Prediction Unit (TCPu) and the Traffic Observation and Management Unit (TOMu). The TCPu utilizes Graph Neural Network (GNN) optimization to accurately predict traffic flow levels at various delivery stations within $SmCt$ ecosystems. Additionally, the TOMu facilitates the intelligent selection of the most suitable delivery vehicles for fulfilling crowd delivery requests ($CDR$). This work emphasizes the potential of crowd delivery as a feasible solution for achieving SMT goals while adhering to smart city parameters ($\mathcal{SCP}$s), such as reduced carbon emissions, shorter travel times, and minimized travel distances. The proposed model achieves notable improvements in computational efficiency, including reductions of up to 4.03\% in L1 loss ($£$), 16.66\% in L2 loss ($£_{rmse}$), and 7.64\% in computation time.

---


### 210. [Syntax Element Encryption for H.265/HEVC Using Chaotic Map-Based Coefficient Scrambling Scheme](https://arxiv.org/abs/2608.22573)

**<font color=#1a73e8>作者：</font>** Liang-Wei Li, Chung-Nan Lee, Kishu Gupta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In today's digital landscape, high-efficiency video coding (H.265/HEVC) has emerged as the most widely used video coding standard, employing selective encryption schemes to protect the privacy of video content while maintaining efficient compression performance. However, existing coefficient scrambling methods impose a significant computational load, leading to increased bit rate overhead due to encryption, longer execution times, and insufficient safety measures. To address these issues, a new coefficient scrambling scheme based on \textit{chaotic maps} is proposed. This approach leverages the pseudorandomness, ergodicity, and sensitivity to initial conditions inherent in chaotic maps to generate highly unpredictable coefficient distributions, thereby strengthening security while preserving low complexity. Unlike conventional scrambling, chaotic maps ensure minimal correlation between encrypted coefficients, enhancing resistance against statistical and differential attacks. Additionally, the scrambling conditions are specifically designed to minimize the impact on the bit rate overhead. Furthermore, when combined with syntax element encryption (SEC), which includes motion vector difference (MVD), quantized transform coefficients (QTC), and luma intraprediction mode (Luma IPM), this method effectively distorts video content. The proposed scheme operates synchronously with slices, ensuring that the decryption of video content remains intact even if some slices are lost. Additionally, a random sequence generated by AES-CTR is incorporated with the H.265 encoded stream to protect against chosen-plaintext attacks.

---


### 211. [CausalCache: Conditional High-Fidelity Restoration for Long-Horizon GUI Agents](https://arxiv.org/abs/2608.22577)

**<font color=#1a73e8>作者：</font>** Jiaxuan Luo, Zhanfeng Liao, Jiayao Teng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon GUI agents can retain a complete interaction trace cheaply as textual action records, but expose only a few past events to the policy in high-fidelity pixels. We formulate this as conditional fidelity restoration: each event persists in summary-only form and is linked to an archived screenshot, while an active visual-context budget $B$ limits how many events may be promoted to summary-plus-image form. Recent-$B$ spends every slot on the latest events. CausalCache instead reallocates the same $B$ promotions over the complete trace, evicting a recent image only when a distant event has higher conditional marginal utility. Its history-gated key/value (HGKV) adapter modifies only restored history-image tokens and is exactly bypassed with no history image. Matched-budget replacement groups and per-arm-anchored difference-in-differences supervision make uniform history amplification worth zero; a budget-aware selector then chooses which summarized events to restore. On desktop, the frozen policy shows no reliable preference for a task-relevant archived screenshot over the recent frame it would displace; HGKV learns exactly that selectivity inside a pre-specified drift envelope. On OSWorld-Verified, restoring history to high fidelity is worth about $13$ success points over summary-only memory, while same-budget allocations remain indistinguishable. Zero-shot on a cross-application mobile benchmark, CausalCache significantly improves overall success over the same-budget recent allocation ($+3.7$ points on the full roster), and the gain concentrates where it should: $+8.6$ points on the memory-critical split fixed by benchmark metadata at construction, no detectable effect on matched controls, and a significant split-by-method interaction.

---


### 212. [Clinical Graph-JEPA: Predictive Patient-State Knowledge Graphs for Cognitive Decision Support](https://arxiv.org/abs/2608.22583)

**<font color=#1a73e8>作者：</font>** Kushagra Yadav, Nalin Prabhath, Amit Lamba 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clinical records contain rich evidence about patient state, but converting that evidence into reliable, structured knowledge graphs remains difficult because extraction errors, ontology mismatch, missing relations, and temporal ambiguity can propagate into downstream systems. We propose a clinical knowledge graph construction and refinement framework that combines multi-agent relation proposal, ontology-aware normalization, deterministic evidence scoring, and JEPA-based latent refinement. Rather than treating a clinical knowledge graph as a static extraction artifact, we treat it as a predictive patient-state representation. For each admission, the system constructs an evidence-scored graph from structured MIMIC-IV records and inferred clinical cross-links, then learns to recover held-out clinical relations from the observed graph context. We evaluate the refiner with leakage-free leave-one-out edge recovery (MRR and Hits@k) and held-out batch-mask evaluation (AUC and MRR). To isolate the contribution of discharge-note context, we compare a note-embedding-free configuration with a note-augmented configuration that injects real discharge-note representations only into note-grounded entities. Under the same cohort and evaluation protocol, entity-grounded note injection improves overall leave-one-out MRR by 31% relative improvement.

---


### 213. [Weakly supervised concept Bottleneck Learning for Robust Two stage Object centric visual reasoning](https://arxiv.org/abs/2608.22584)

**<font color=#1a73e8>作者：</font>** Sparsh Tiwari, Gesina Schwalbe, Bettina Finzel  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Two-stage neuro-symbolic architectures provide an elegant paradigm for visual problem solving by cleanly separating connectionist perception of predefined symbols from possibly later defined relational reasoning thereon. However, anchoring high-level predicates into visual frames typically necessitates annotations that are expensive to acquire. In this work, we introduce the Dynamic Orthogonal Concept Bottleneck (D-OCB), an object-centric slot- VAE framework designed to extract human-aligned symbolic predicates under extremely weak supervision. D-OCB eliminates the arduous manual tuning of loss-balancing coef- ficients by dynamically learning optimal hyperparameter allocations during training. To infuse prior knowledge on independence of concept categories, in addition to standard re- construction self-supervision we penalize correlation across concept subspaces. Crucially, to combat the instability of very low supervision regimes, D-OCB incorporates a dynamic di- mensionality allocation mechanism; this adaptive formulation allows well-represented con- cepts to yield latent dimensions to underperforming concepts that are lagging behind, effectively preventing representation collapse and significantly improving overall concept accuracy. Through an extensive empirical evaluation, we demonstrate that our framework achieves high concept alignment and downstream visual reasoning accuracy using minimal label budgets, matching or outperforming end-to-end paradigms.

---


### 214. [GCA: Global Centroid Alignment in Federated Learning](https://arxiv.org/abs/2608.22593)

**<font color=#1a73e8>作者：</font>** Jong-Ik Park, Harry Jiang, Logan Blakely 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autoencoder (AE)-based federated learning (FL) is attractive for anomaly detection when clients have limited local data. However, conventional FL exchanges AE parameters or gradients, incurring substantial communication overhead and potentially exposing input training data information, since AEs are explicitly optimized to reconstruct their inputs. We introduce \emph{Global Centroid Alignment (GCA)}, a latent-code-mediated FL protocol that coordinates clients without transmitting AE parameters or gradients. In each round, (1) clients first train their local AEs using a \emph{reconstruction} update and upload a small subset of encoder latent codes to the FL server. (2) The server pools these codes, fits a clustering model, and broadcasts only \emph{global latent centroids and their support counts}. (3) Each client then updates its encoder by aligning its local latent codes with the \emph{nearest} centroid using \emph{inverse-count} weighting to emphasize globally underrepresented patterns. Steps (1)--(3) repeat over communication rounds. Because GCA exchanges only sampled latent codes and centroid statistics, its communication cost depends on latent dimensionality and the numbers of uploaded codes and returned centroids rather than on AE model size. Across five tabular and two vision benchmarks, GCA yields higher reconstruction error under a server-side client data extraction attack in all 21 comparisons and clearly lower cosine similarity in 20 of 21 comparisons with FedAvg, FedProx, and FedNova, showing its ability to protect training data. It even improves test accuracy over FedAvg by up to $5.76\%$. GCA achieves extraction defense comparable to DP-FedAvg, remains effective when DP-FedAvg does not reduce target resemblance, and lowers per-round communication by up to $99.15\%$.

---


### 215. [Adversarial Agents on Topology Optimization: Understanding the Fragility and Robustness of Deep Learning-based and Physics-Based Design Models under Adversarial Perturbation](https://arxiv.org/abs/2608.22606)

**<font color=#1a73e8>作者：</font>** Hoang Anh Nguyen, Yuan Hong, Hongyi Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Topology optimization, using both physic-based approaches and deep learning surrogates, serves as a cornerstone for generative design agents in cyber-manufacturing systems. While deep learning surrogates have gained widespread adoption due to their speed in online design generation, this work demonstrates their vulnerability under input perturbations. In this work, we present a mechanics-grounded reliability evaluation framework that formulates an adversarial agent targeting the generative design models. We investigate a strictly non-intrusive threat model where bounded perturbations are introduced exclusively to the initial-density channel, while physical boundary conditions, compliance-gradient channels, network architectures, and solver routines remain intact. Evaluating surrogate models across U-Net, convolutional, and generative architectures with varying physics-gradient conditioning depths demonstrates that bounded initialization noise can cause catastrophic mechanical failure, increasing compliance by multiple orders of magnitude through severed load paths and disconnected supports. Furthermore, we discover that incorporating richer physics-gradient conditioning in the deep learning surrogates does not guarantee monotonic robustness across surrogate families. Finally, physics-in-the-loop recovery demonstrates that initializing the classical SIMP optimizer with perturbed topologies mitigates design performance degradation, having a high probability of restoring compliance to near-baseline levels across tested instances. These findings demonstrate that learned surrogates should serve as physics-verified initializers instead of replacing physics-based solvers entirely in a resilient cyber-manufacturing system. Moreover, the proposed adversarial agent provides a foundation for future training generative design agents robust against noise and targeted perturbations.

---


### 216. [Mitigating Explanation Leakage in Financial Fraud Detection Systems](https://arxiv.org/abs/2608.22607)

**<font color=#1a73e8>作者：</font>** Muhammad Waleed Gul, Elaheh Homayounvala  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Financial fraud detection relies heavily on centralized machine learning models. This creates serious data privacy risks. Federated Learning (FL) decentralizes data processing, but financial regulations still require models to be transparent. This means using Explainable AI (XAI) tools such as TreeSHAP. Recent cybersecurity research shows a problem with this approach. Sharing high-fidelity SHAP explanations exposes the federated network to Membership Inference Attacks (MIAs). This dissertation proposes and evaluates DP-FedSHAP. It is a new architecture that applies client-level differential privacy only to post-hoc TreeSHAP vectors. It is compared against a Weight-Level DP baseline, which perturbs the trained model directly instead. Using the highly imbalanced IEEE-CIS Fraud Detection dataset, this study measures the trade-off between explanation fidelity, privacy preservation, and the model's Area Under the Precision-Recall Curve (AUPRC).

---


### 217. [AI-based worker guidance in assembly and disassembly operations using multimodal ego/exo-centric data capture and structured task knowledge](https://arxiv.org/abs/2608.22617)

**<font color=#1a73e8>作者：</font>** Vivek Chavan, Jörg Krüger  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Assembly and disassembly processes rely on expert knowledge that is difficult to document, reuse, and transfer. This paper presents a data-centric approach for extracting structured task knowledge from expert demonstrations using egocentric and exocentric recordings. Temporal and multimodal information from video and narration is jointly encoded to derive structured task representations that enable procedural documentation and context-aware worker guidance. The approach is evaluated on a real-world disassembly case study, demonstrating that video-based representations capture procedural structure and execution context beyond static image-based methods. The results highlight the potential of egocentric video understanding for repair, training, and circular manufacturing applications. Project website: this https URL

---


### 218. [Q-Learning with Stable Infinite-Dimensional Linear Function Approximation](https://arxiv.org/abs/2608.22636)

**<font color=#1a73e8>作者：</font>** Shengbo Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Q-learning with linear function approximation can be unstable because an arbitrary approximation architecture need not preserve the Bellman contraction. We develop a stable infinite-dimensional linear function approximation framework for Q-learning from a single Markovian behavior-policy trajectory. The learning variable is a coefficient field $\theta\in C(\mathbb L)$ on a compact latent metric space $(\mathbb L,\rho)$. The framework uses a reconstruction operator that maps $\theta$ to a continuous Q-function and a compression operator that maps Bellman updates back to latent coordinates. Nonexpansiveness of both operators induces a contractive latent Bellman map on $C(\mathbb L)$, with a unique fixed point $\theta^*$ whose reconstruction approximates the optimal Q-function up to representation error. We propose two stochastic approximation (SA) algorithms and establish their sup-norm convergence bounds with a leading term of order $\widetilde O(n^{-1/2})$. The infinite-dimensional formulation provides a powerful abstraction for identifying the structures that govern statistical difficulty. Smoothness of the compression map in $\rho$ is inherited by $\theta^*$ and the SA iterates, allowing uniform estimation errors to be controlled through covering numbers of $(\mathbb L,\rho)$ rather than the dimension of $C(\mathbb L)$. Remarkably, the SA algorithms we propose are agnostic to the choice of $\rho$, and thus can automatically adapt to both the smoothness and the geometry. We further illustrate the framework through Q-measure-learning with linear density approximation and output-layer neural weight training under a frozen pretrained network.

---


### 219. [Mol-JEPA: A multimodal Joint Embedding Predictive Architecture for Molecules](https://arxiv.org/abs/2608.22642)

**<font color=#1a73e8>作者：</font>** Florian Rottach, Sebastian Schieferdecker, William Rudman 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite recent advances in molecular foundation models, several limitations remain, such as chemically invalid augmentations, modality collapse, and incomplete representation of biochemical environments. To address these challenges, we present \textbf{Mol-JEPA}, a scalable framework for learning molecular world models. Rather than relying on suboptimal molecular perturbations, our model uses modality masking to exploit information from molecular structures, cellular phenotypes, binding affinities, ADMET profiles, quantum chemistry simulations and other drug discovery data. Across various benchmarks, we show that the representations learned by Mol-JEPA deliver strong performance, demonstrating the value of incorporating biochemical context through latent space prediction.

---


### 220. [Obscura-PQ: Post-Quantum Privacy-Preserving Protocol for the Algorand Blockchain Using Lattice-Based Linkable Ring Signatures](https://arxiv.org/abs/2608.22645)

**<font color=#1a73e8>作者：</font>** Navid Azimi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Public blockchains expose the complete transaction graph, and the privacy protocols deployed to obscure it rely almost exclusively on elliptic-curve cryptography, whose discrete-logarithm foundations fall to Shor's algorithm. Because ledgers are immutable, every anonymity set published today under classical assumptions can be retroactively deanonymized by a future quantum adversary. Transitioning to post-quantum alternatives remains challenging, as strict smart-contract resource limits prohibit native on-chain verification of computationally intensive post-quantum proofs. To address these challenges, we present \emph{Obscura-PQ}, a decentralized, non-custodial post-quantum privacy protocol that verifies natively on the Algorand blockchain. Its core is a setup-free lattice linkable ring signature over the cyclotomic ring $\mathcal{R}_q = \mathbb{Z}_q[X]/(X^{512}+1)$. A deposit is a Ring-SIS binding commitment to a short secret; a withdrawal proves knowledge of a ring opening via an AOS/Borromean-style challenge chain over two response-sharing linear relations with rejection-sampled short responses, while publishing a deterministic Ring-LWE serial number for double-spend detection. We reduce double-spend soundness and linkability to Ring-SIS, theft resistance to Ring-SIS for honestly generated deposits, and anonymity to Ring-LWE and an explicit decisional linking assumption in the classical random-oracle model. To overcome strict on-chain opcode and storage limits, Obscura-PQ evaluates verification relations entirely in the NTT domain. We split forward NTTs across opcode-pooled execution phases and stream oversized proofs through refundable box storage, enabling $O(1)$ membership and double-spend checks. We provide a complete Algorand testnet implementation, demonstrating native on-chain verification of a post-quantum privacy protocol under strict smart-contract limits.

---


### 221. [Iteration Without Elaboration: A Simple ReAct Architecture Suffices for Text-to-SQL Generation](https://arxiv.org/abs/2608.22651)

**<font color=#1a73e8>作者：</font>** Jian Lu, Haiwei Yu, Raymond M Xiong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern text-to-SQL systems have become increasingly elaborate, relying on schema-linking modules, retrieval-augmented prompting, candidate generation, and multi-stage refinement pipelines. While effective, these additions introduce substantial latency and engineering overhead. To this end, we present \textbf{ReAct-SQL}, a simple yet effective zero-shot ReAct-style framework built solely on iterative reasoning and a constrained action space defined by a typed Domain-Specific Language (DSL) of 15 relational operations, rather than free-form SQL generation. The model incrementally issues DSL calls, observes compiled-SQL execution feedback, and revises its reasoning through interaction. On corrected BIRD mini-dev and EHR-SQL, ReAct-SQL achieves \textbf{84.5\%} and \textbf{73.9\%} accuracy, respectively, matching substantially more elaborate baselines while running up to $8\times$ faster. Incremental ablations further show that iteration primarily improves grounding, while the DSL improves compositional reliability.

---


### 222. [Multiple View Neural Regression of a Facial Shape Model](https://arxiv.org/abs/2608.22655)

**<font color=#1a73e8>作者：</font>** Xiang Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Creating re-topologized 3D facial meshes is essential for high-quality facial animation but remains labor-intensive and time-consuming. This dissertation explores more efficient approaches for capturing production-ready facial meshes through: (1) the development of VarIS, a custom light sphere for capturing high-resolution stereo geometry and reflectance maps; (2) analysis of camera parameters affecting automatic 2D and 3D landmarking; (3) synthetic-data methods for training neural face regression; and (4) techniques for improving neural multi-view face-shape regression.
While VarIS enables photorealistic face capture, its operational and processing costs motivate a more scalable approach. A deep learning framework is therefore proposed to directly predict re-topologized facial meshes from synthetic multiview images generated with Visage Craft, an in-house physically based rendering system using an Appearance 3D Morphable Model (A3DMM). The system produces standardized meshes ready for rigging and animation with minimal human supervision. Results show that incorporating accurate camera intrinsics and extrinsics improves landmark accuracy and geometric consistency, while 3D landmark regularization further improves reconstruction quality.

---


### 223. [Hyperbolic Hierarchical Clustering for Visual Representation Learning](https://arxiv.org/abs/2608.22665)

**<font color=#1a73e8>作者：</font>** Jianan Wei, Guikun Chen, Zhiyuan Weng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We investigate the token mixer in vision backbones by revisiting clustering, one of the most classic approaches in machine learning. An effective token mixer is a fundamental component of modern vision backbones like vision Transformers, facilitating information exchange between image patches. Mainstream token mixers, which rely on convolution, attention, MLP, or their hybrids, primarily focus on navigating the trade-off between accuracy and computational cost. However, a significant drawback of these methods is their black-box nature; their encoding process is opaque and lacks interpretability. Diverging from these opaque designs, we introduce ClusterMixer, a transparent token mixer that is grounded in a clustering paradigm and interpretable by design. ClusterMixer explicitly formulates the token mixing process through a hierarchical clustering mechanism. To model the natural, tree-like relationships inherent in visual data, the clustering is performed in hyperbolic space, which is well-suited for embedding hierarchies with low distortion. Building on this innovation, we present HCFormer, a new backbone architecture that integrates ClusterMixer with a series of meticulously designed clustering strategies to ensure robust performance across tasks. Extensive experiments demonstrate that HCFormer consistently outperforms its counterparts across diverse tasks, including image classification, object detection, instance segmentation, and semantic segmentation. Considering its transparency and efficacy, we hope HCFormer can facilitate a paradigm shift toward interpretable backbones.

---


### 224. [A-CPES: A Reference Framework for Agentic AI in Cyber-Physical Energy Systems](https://arxiv.org/abs/2608.22672)

**<font color=#1a73e8>作者：</font>** Xiaoyu Zhang, Qiuye Sun, Jiachen Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Energy system operation contains a loop of work that automation has never taken over: posing the optimization problem the current cycle should solve, disposing of infeasibility, sequencing a solution into interlocked switching orders, assembling evidence no single model holds, negotiating adjustable capacity with many parties, and settling experience into practice. Licensed dispatchers carry all of it in person, and the rising share of variable renewable generation is making that loop turn faster than their number can grow. Agentic AI supplies the abilities it requires, but enters as the outer loop of control: it calls SCED and the other decision models rather than being called by them. We propose A-CPES, three nested rings, an authorization and accountability frame around an agentic control outer loop around a six-layer CPES core. We argue the loop is indivisible, tune where and how tightly it may close, state eight structural failure modes as falsifiable predictions, and specify six governance modules that rebuild the authorization frame until it covers the loop, before the loop starts turning.

---


### 225. [Robustness Analysis of Agentic AI to Inconsistent and Incomplete Tool Responses](https://arxiv.org/abs/2608.22676)

**<font color=#1a73e8>作者：</font>** Jiachen Xu, Torben Bach Pedersen, Zhongming Yao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Robustness to a bad tool return means answering it in the way that return calls for, which depends on how the tool went wrong. A tool that has failed and a tool that returns a well-formed falsehood are different problems with different remedies. We ask whether the two already differ at the moment the return arrives. This is a qualitative pilot study: we score single decision points rather than running agents to completion. We inject controlled faults into a retail customer-service domain and read two channels off the model's log-probabilities: the likelihood of the returned content under the tool schema alone and under the whole trajectory, and its distribution over the legal actions, read for both shape and where the mass sits. An incomplete return is legible in every case, being improbable under the schema alone in a range no other condition enters, and it moves the mass toward the tools that re-read state wherever there is room to move. An inconsistent return leaves the schema channel untouched and registers in the likelihood comparison on the field whose true value the context already carries verbatim, not on the one whose contradiction runs through the domain policy. The action distribution gives each condition a distinct signature, but orders them by how far the return bears on the next action rather than by fault family. Recognition is therefore asymmetric: each condition is legible in some channel, and no channel is legible on all of them.

---


### 226. [Contextrast++: Robust Multi-Scale Contextual Contrastive Learning for Semantic Segmentation](https://arxiv.org/abs/2608.22679)

**<font color=#1a73e8>作者：</font>** Changki Sung, Hyungtae Lim, Wanhee Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic segmentation has rapidly advanced with deep learning; however, challenges remain in effectively capturing local and global contexts as well as addressing the long-tailed distribution problem. To tackle these issues, we present Contextrast++, a robust contrastive learning method for semantic segmentation that improves multi-scale feature integration and mitigates class imbalance issues. Our method consists of two key components: 1) contextual contrastive learning (CCL) and 2) boundary-aware negative (BANE) sampling. CCL includes three subcomponents: adaptive fusion module, pixel-to-anchor (PA) loss, and anchor-to-anchor (AA) loss. The adaptive fusion module dynamically balances local and global feature integration, resulting in a more context-aware representation. While the PA loss leverages the fused multi-scale features to improve feature representation learning, the AA loss focuses on addressing the long-tailed distribution problem by utilizing a memory bank that stores a fixed number of class-balanced representative anchors. Meanwhile, BANE sampling enhances segmentation precision by selecting hard negatives from misclassified boundary regions, which refines fine-grained details during contrastive learning. As verified in extensive experiments using public datasets, we demonstrate that Contextrast++ substantially improves semantic segmentation performance over existing contrastive learning-based state-of-the-art approaches, while introducing no additional computational overhead during inference.

---


### 227. [Maximum-distance nonnegative matrix factorization for unmixing highly mixed grain-size distribution data: A generalization of AnalySize](https://arxiv.org/abs/2608.22681)

**<font color=#1a73e8>作者：</font>** Qianqian Qi, Zhongming Chen, Peter G. M. van der Heijden  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Nonnegative matrix factorization (NMF) decomposes a nonnegative matrix into the product of two nonnegative matrices. This property makes NMF well suited for unmixing grain-size distribution data, which are inherently nonnegative and have row sums equal to one. Previous studies have shown that AnalySize, an NMF-based method, performs well on poorly mixed grain-size distribution data but struggles when the data is highly mixed, where no observed samples are close to the true end members. To overcome this limitation, we introduce a maximum-distance NMF that encourages the estimated end members to be as distinct as possible and develop a hierarchical alternating least squares algorithm for optimization. The proposed formulation can be regarded as a generalization of AnalySize, where AnalySize minimizes the distance among end members while the proposed method maximizes it. Experimental results demonstrate that the method effectively decomposes highly mixed grain-size distribution data.

---


### 228. [The Colossus with Feet of Clay: Debunking Encrypted Traffic Classifiers under PQC Evolution](https://arxiv.org/abs/2608.22683)

**<font color=#1a73e8>作者：</font>** Bingzhen Li, Lingjia Meng, Runhan Song 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Encrypted traffic classifiers often achieve high accuracy under matched training and testing conditions, implicitly assuming that deployment traffic follows the training distribution. TLS migration toward post-quantum cryptography (PQC) challenges this assumption because hybrid key establishment can reshape observable traffic without changing application labels. We frame this change as PQC-induced protocol drift and study its effects through closed-world HTTPS website fingerprinting using the deployed TLS~1.3 Hybrid-PQC group \texttt{\detokenize{X25519MLKEM768}}. We build a controlled, PQC-aware benchmark pairing Traditional (Non-PQC) and Hybrid-PQC traffic, then evaluate five representative classifiers and side-channel representations under matched-domain, cross-domain, and deployment-ratio settings. Collectively, the experiments show that PQC evolution does not remove learnable website information. Instead, it changes how that information appears in traffic, causing classifiers and feature combinations that perform well in-domain to lose reliability across cryptographic domains. By exposing the fragility of matched-domain evaluation, we offer strategic guidance, identify cross-domain robustness as a research priority, and recommend protocol-aware practices for dependable real-world encrypted traffic classification. The code is available at this http URL.

---


### 229. [MorphoCLIP: Text-Supervised Contrastive Learning for Perturbation Matching in Cell Painting Images](https://arxiv.org/abs/2608.22690)

**<font color=#1a73e8>作者：</font>** Sukhrobbek Ilyosbekov, Shubham Gajjar, Rongfei Jin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cell Painting microscopy captures how cells change after a chemical or genetic perturbation. Connecting these images to the perturbations that produced them could make large imaging screens easier to search and interpret, but the task remains difficult because biological effects are subtle and technical variation is substantial. We introduce MorphoCLIP, a contrastive model that links Cell Painting profiles with text descriptions of compounds, CRISPR knockouts, and ORF overexpressions. The model keeps its vision and language backbones frozen and trains only a compact cross-channel module and projection layers, so it can be trained on a single consumer GPU. On held-out CPJUMP1 data, MorphoCLIP searches in both directions: from a cell image to its perturbation description and from a description to matching cell images. In both cases, a correct match appears among the top ten results much more often than expected by chance. Adding a replicate-alignment loss makes profiles from repeated experiments more consistent, although this improvement does not yet translate into reliable gene-compound matching. Gene-aware labels and plate correction also show no consistent retrieval benefit. These findings suggest that text supervision can help organize chemical and genetic Cell Painting data. Matching compounds with genetic perturbations, however, remains an open problem.

---


### 230. [Hybrid Generative-Discriminative Object Placement](https://arxiv.org/abs/2608.22692)

**<font color=#1a73e8>作者：</font>** Siyuan Zhou, Li Niu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As an important operation of image composition, object placement aims to predict the plausible placement (location, scale) for the inserted foreground object. Previous object placement methods can be divided into generative methods and discriminative methods, both of which cannot balance efficiency and effectiveness well. In this work, we propose a semi-generative method in the middle ground between them. In particular, we assign uniformly distributed anchors on the background. Then, we fuse foreground and background features to predict the rationality score for each anchor and predict plausible placement sets for positive anchors. Extensive experiments on the OPA dataset show that our method can strike a good balance between efficiency and effectiveness.

---


### 231. [TEE-X: TEE-aware Acceleration Framework for Large Vision Models at the Edge](https://arxiv.org/abs/2608.22716)

**<font color=#1a73e8>作者：</font>** Kurt M Wilson, Mohaiminul Al Nahian, Abeer Matar A. Almalky 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Despite their remarkable success, machine learning models, particularly in vision applications, are alarmingly vulnerable to a range of security threats. One key factor in the attack landscape is the distinction between white-box and black-box threat models, as the latter poses challenges that limit attack effectiveness when access to model information is limited. As a result, using Trusted Execution Environments (TEEs) enhances security for machine learning applications by protecting model confidentiality and execution integrity, effectively shifting the execution environment from the white-box to the black-box side of the threat model spectrum. While adopting TEEs for large vision models, e.g., Vision Transformers (ViTs), is crucial for enhancing security and privacy, significant challenges related to memory constraints and increased computational latency must be addressed, especially in time-sensitive edge applications where safety and privacy are paramount. The objective of this work is to enable large vision models to be fully hosted within TEEs, achieving GPU-level inference latency for time-sensitive edge vision applications while maintaining performance. To this end, we propose TEE-X, a TEE-aware acceleration framework that introduces a sensitivity-aware modularization technique and enables vectorization in TEE inference. This design is validated on OP-TEE for Arm TrustZone, configured to optimize performance on the NVIDIA Jetson AGX Xavier for efficient edge vision applications using ViT models. The findings reveal that TEE-X delivers an effective TEE-aware acceleration framework that achieves minimal accuracy-latency trade-offs while ensuring fast and secure edge inference for vision models.

---


### 232. [EGAMA-RC: Risk-Calibrated Evidence-Gated Adaptive Malware Analysis for Robust and Interpretable Memory-Forensic Triage](https://arxiv.org/abs/2608.22721)

**<font color=#1a73e8>作者：</font>** Isaac Kofi Nti  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine-learning malware detectors often achieve high clean-data accuracy, but operational triage also requires evidence about uncertainty, novelty, robustness, interpretability, latency, and review cost. This paper presents EGAMA-RC, a risk-calibrated evidence-gated framework for memory-forensic malware triage. Building on SHAP-guided feature refinement, EGAMA-RC combines dataset-specific refinement, model-pool evaluation, adversarial and open-family testing, novelty scoring, explanation-conditioned evidence, and runtime-aware routing. Low-risk samples are accepted automatically, while uncertain, high-risk, or potentially novel cases are routed to review, escalation, or novelty-aware handling. Across three malware datasets and a frozen multi-seed protocol, the selected hybrid gate accepts 93.12% of pooled samples with 99.86% accepted accuracy and a 0.136% false-accept rate. Novelty calibration reduces over-restrictive review behavior while preserving a low unsafe-accept profile. XGBoost provides lightweight fast-path inference with p50/p95 latency of 0.0054/0.0059 ms per sample. The results show that dependable malware analysis requires risk-calibrated routing, novelty awareness, and controlled analyst review, not classification accuracy alone.

---


### 233. [LoViF 2026 The First Challenge on Unified Removal of Raindrops and Reflections: Methods and Results](https://arxiv.org/abs/2608.22723)

**<font color=#1a73e8>作者：</font>** Zewei He, Xi Tong, Yu Chen 等 52 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This workshop paper comprehensively reviews the First Challenge on Unified Removal of Raindrops and Reflections. The challenge aims to address a frequently encountered practical problem in the field of autonomous driving, i.e., raindrop-reflection composite degradation on rainy days. This competition attracted 149 registered participants and received 12 valid final submissions with corresponding fact sheets, significantly contributing to the progress of unified removal of raindrops and reflections. All the methods are developed and evaluated on our real-shot RainDrop and ReFlection (RDRF) dataset. A detailed analysis of the submitted methods and corresponding results is provided in this report, which highlights effective approaches and provides interesting insights for future research.

---


### 234. [SEAM: Shot Entity-Attribute Memory for Consistent Short-Drama Generation at Scale](https://arxiv.org/abs/2608.22725)

**<font color=#1a73e8>作者：</font>** Jiaqi Liu, Maolin Ran, Xiaoyang Lu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Short-drama generation has grown into a large, industrialized pipeline, and as it scales from isolated shots to the episode level, visual continuity has become a critical bottleneck. Current agent frameworks generate each shot in isolation, so context drifts across shots and props, character posture, and blocking turn inconsistent. Once assembled, these small discrepancies amplify into severe visual breaks. We present SEAM (Shot Entity-Attribute Memory), a training-free, model-agnostic memory graph that repairs continuity entirely at the prompt-text layer by extracting a multi-dimensional state for every shot, retrieving only causally prior context over the resulting graph, filtering it selectively, and injecting the surviving constraints by natural-language prompt rewriting. We further release SEAM-Bench, a double-blind continuity storyboarding benchmark, on which SEAM raises cross-episode continuity recall from 0.700 to 0.946, generalizes across six mainstream text models, and yields consistent, though not yet significant, gains at the generated-image layer. Deployed as a mandatory stage in CreativeFitting's SEAM-Agent production pipeline over 201 shots, SEAM reaches a 96.5% director-acceptance rate with zero unsafe injections; a conservative counterfactual attributes at least 21.9 percentage points of that rate to its cross-episode memory.

---


### 235. [Spiking Neural Networks for Continuous Control: Neuromorphic Reinforcement Learning in Conventional Computing](https://arxiv.org/abs/2608.22729)

**<font color=#1a73e8>作者：</font>** Jessica Hunter, Md Maruf Hossain Shuvo, Krishna Roy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) algorithms have made strides over the past decade applying them to a wide range of problems and control tasks. However, the deployment of RL on neuromorphic hardware for continuous control tasks remains under-validated. Namely it is unclear whether replacing a conventional actor network with a spiking neural network (SNN) affects the performance of an agent before any hardware-specific benefits manifest. We provide a systematic validation of a minimal, neuromorphically viable spiking actor variant of Soft Actor-Critic (SAC) on conventional hardware, establishing a baseline for future neuromorphic RL research. In this paper, we propose the Spiking Actor Network Soft Actor Critic (SANSAC) to address the use of RL frameworks in continuous environments, designed as a framework that can be implemented on neuromorphic hardware. We compare a traditional Soft Actor Critic (SAC) network to SANSAC in a traditional computer. We demonstrate the near equivalent performance of SANSAC and SAC, while addressing the impact of hidden dimensions. Our results demonstrate the viability of SNN based algorithms in complex continuous environments, as well as competitive performance to traditional neural networks in traditional computers, providing a basis to continue exploring the use of SNNs in continuous RL frameworks.

---


### 236. [Seeing the Unseen: Semantic-in-Gaussian for Sparse-View 3D Generalization](https://arxiv.org/abs/2608.22740)

**<font color=#1a73e8>作者：</font>** Zeyang Bai, Yunpeng Wang, Yunbiao Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generalizable 3D Gaussian Splatting (G-3DGS) has emerged as a promising approach for novel view synthesis undersparse-view settings. However, existing frameworks remain restricted by pixel-aligned Gaussian estimation, whichstruggles in partially observed or occluded regions and often leads to incomplete surfaces or structural collapse. Toaddress these challenges, we propose SeeU (Seeing the Unseen), a novel G-3DGS framework. We frame its core design asSemantic-in-Gaussian: semantic-conditioned refinement in Gaussian space. Specifically, we introduce a Cross-viewEntropy-Aware (CEA) module that aggregates multi-view semantic and geometric cues into compact embeddings. Theseembeddings guide the Conditional Gaussian Transformer, which applies residual updates to coarse Gaussians, helpingrecover under-constrained regions of partially observed structures while preserving surface consistency. Comprehensiveexperiments on multiple benchmarks demonstrate that SeeU consistently improves rendering quality and structuralcompleteness while retaining efficient feed-forward inference. Especially under challenging extrapolation settings,SeeU achieves an average improvement of 2.44 dB in PSNR compared to recent SOTA G-3DGS methods.

---


### 237. [MOSH-WM: Mask-Grounded Soft-Hamiltonian Dynamics for Object-Centric World Models](https://arxiv.org/abs/2608.22750)

**<font color=#1a73e8>作者：</font>** Zhekai Wang, Haoxiang Huang, Xiang Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Object-centric world models forecast future videos by evolving a set of entity slots, but the variables receiving dynamics supervision are often unconstrained visual features. We introduce \method{}, a mask-grounded soft-Hamiltonian world model that makes its position-like state explicitly depend on slot-owned image support. A frozen video-slot encoder produces slots and masks; spatial moments of mask-owned support form a canonical state $Q$, temporal differences form $P$, and a learned energy supplies a soft directional bias to a bounded learned increment. Decoder-relevant appearance and identity are stored separately in a causal visual context. A gated composer and bounded residual then combine this context with the propagated phase state to reconstruct decoder-compatible slots. On OBJ3D, given six observed frames and evaluated over the following 30 frames, \method{} reduces LPIPS by 25.0\% and spatial MSE by 33.7\% relative to the strongest object-centric baseline. On CLEVRER, given six observed frames and evaluated over the following ten frames, the corresponding reductions are 14.5\% and 18.7\%. Horizon-resolved visual and object-state measurements show that the complete model accumulates error more slowly throughout the 30-frame closed-loop rollout. Project page:this https URL.

---


### 238. [A Study of Bluetooth Access Control Based on NFT Soft Pairing](https://arxiv.org/abs/2608.22754)

**<font color=#1a73e8>作者：</font>** Zhiming Liang, Bin Chen, Ruijun Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper proposes a Non-Fungible Token (NFT) soft pairing framework for Bluetooth service access control. Unlike conventional Bluetooth systems where pairing implicitly grants persistent service access, the proposed approach decouples native Bluetooth pairing from authorization without modifying the underlying protocol stack. The framework introduces a three-layer architecture consisting of a Bluetooth layer for connectivity, a blockchain layer for trusted execution and on-chain state verification, and an application layer where NFT soft pairing defines the authorization logic. In this design, Non-Fungible Bluetooth Tokens (NFBTs) represent user-side access credentials, while Non-Fungible Device Tokens (NFDTs) represent device identities. Their bidirectional on-chain binding forms a revocable and verifiable NFT soft pairing relationship. During access, users prove ownership of valid NFBTs through challenge-response signatures, and devices verify the corresponding on-chain state before granting service access. A prototype implemented with MetaMask and Ethereum demonstrates secure authentication, dynamic revocation, acceptable latency, and gas-efficient credential issuance based on ERC1155.

---


### 239. [LpWM: A Case for Sparse Representations in World Models](https://arxiv.org/abs/2608.22764)

**<font color=#1a73e8>作者：</font>** Yilun Kuang, Yash Dagade, Quentin Le Lidec 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Joint-embedding predictive architectures (JEPAs) learn latent dynamics for planning and avoid representation collapse by matching features to maximum-entropy distributions such as isotropic Gaussians, yielding dense representations. However, it is unclear whether dense representations are the most favorable geometry for modeling dynamics. In this work, we ask whether a different geometry, sparse representations, can make action-conditioned latent dynamics easier to model, and what dynamical structure emerges from such representations. We first show that nonlinear Lipschitz dynamics can be approximated arbitrarily well by action-conditioned linear dynamics in a sufficiently high-dimensional one-hot latent space, with rollout error vanishing as the dimension grows. This motivates distributed sparse representations as a practical relaxation of one-hot sparsity. We introduce LpWorldModel (LpWM), a JEPA model regularized with Rectified Distribution Matching Regularization (RDMReg) to match encoder features to a Rectified Generalized Gaussian distribution, yielding non-negative sparse codes. Empirically, sparsity lowers the predictor complexity required for successful planning: on PushT, sparse LpWM outperforms dense LeWM by up to 57% in planning success at intermediate predictor capacities. This advantage also extends beyond Gaussian distribution matching, with LpWM outperforming dense VICReg representations across multiple predictor families. We further find that the learned sparse representations are mode-factored, with support encoding discrete dynamical regimes and feature magnitudes capturing continuous within-regime state. Together, these results suggest that sparse representations can reduce the predictor complexity required for control while revealing interpretable structure.

---


### 240. [Learning to Control Coupled-Dynamics Environments with Joint Markov Decision Processes](https://arxiv.org/abs/2608.22765)

**<font color=#1a73e8>作者：</font>** Ege C. Kaya, Aliasghar Pourghani, Mahsa Ghasemi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Coupled-dynamics environments expose the one-step outcomes that would follow from several possible counterfactual actions under a common realization of exogenous randomness. The ordinary Markov decision process formalism allows one to reason about the marginal law of each action but discards dependence across these counterfactual outcomes. The Joint Markov decision process (JMDP) formalism preserves that dependence. Prior work established the formalism and solved the fixed-policy joint moment evaluation problem in JMDPs. This paper develops optimal-control methods. We define a nonparametric distributional Bellman optimality operator for JMDPs, and prove that when the induced marginal MDP has a unique optimal policy, its iterates converge in Wasserstein distance to the optimal joint return law. For the first two moments, we establish convergence under a weaker condition that permits several mean-optimal actions as long as their tie resolutions share a second-moment fixed point. We also derive sampled targets for neural approximation.

---


### 241. [SPOC-SQL: Stage-wise Preference Optimization for Controllable Text-to-SQL](https://arxiv.org/abs/2608.22772)

**<font color=#1a73e8>作者：</font>** Yingnan Chen, Chun Ding, Tianshi Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text-to-SQL aims to translate natural language questions into executable SQL queries over relational databases, requiring multi-stage structured reasoning over database schemas and query constraints. However, existing methods treat this task as single-step generation, where models optimize entire SQL sequences without targeted feedback at key decision points and lack support for interacting with and controlling the intermediate generation process. To address this issue, we propose SPOC-SQL, which decomposes Text-to-SQL into four sequential subtasks following standard SQL execution logic and designs stage-specific optimization strategies for the model to learn key decisions. Specifically, we propose the implementation of fine-grained preference optimisation at key decision points across SQL stages, with the objective of enhancing structured decision-making during query construction. Furthermore, a structured decomposition strategy is designed, facilitating stage-wise intervention and correction through explicit intermediate representations. This results in more controllable and reliable SQL generation. Experiments demonstrate that incorporating stage-wise human knowledge consistently improves performance, validating the effectiveness of stage perception controllable generation.

---


### 242. [LagrangeGS: Non-Conservative Lagrangian System on Dynamic 3D Gaussian Splatting](https://arxiv.org/abs/2608.22773)

**<font color=#1a73e8>作者：</font>** Shogo Sato, Takuhiro Kaneko, Shoichiro Takeda 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic 3D Gaussian Splatting (3DGS) achieves photorealistic reconstruction of time-varying scenes, and recent physics-aware extensions improve extrapolation by explicitly predicting velocity fields. However, these extensions merely fit vector fields to visual deformations without satisfying Lagrangian mechanics, leading to three major issues: (i) physically inconsistent trajectories, (ii) lack of time-reversibility, and (iii) geometric collapse during long-term extrapolation. In this paper, we propose LagrangeGS, which formulates dynamic 3DGS as a non-conservative Lagrangian system. While this Lagrangian formulation fundamentally solves (i), a direct application of general LNNs to dynamic 3DGS requires a large velocity-Hessian inversion for millions of Gaussian particles. To overcome this computational bottleneck, we approximate the velocity-Hessian as an identity matrix, decoupling particle dynamics for computational tractability. For (ii), we restrict the non-conservative forces to be explicitly time independent, enabling consistent backward integration. Finally, to address (iii), we introduce local rigid alignment that regularizes particle trajectories. Extensive evaluations on dynamic scene benchmarks demonstrate that LagrangeGS enables stable long-term extrapolation, consistent time reversal, and counterfactual physics-based editing without retraining.

---


### 243. [Neural Operator based Multi-Field Reconstruction of Inner Solar Boundary State](https://arxiv.org/abs/2608.22782)

**<font color=#1a73e8>作者：</font>** Vignesh Kumar Pandian Sathia, Reza Mansouri, Dustin J. Kempton 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Solar wind is a continuous flow of charged particles emanating from the solar surface and governed by complex, interacting magnetohydrodynamic processes. Accurate specification of inner-boundary conditions is essential for heliospheric modeling and solar-wind prediction. In many practical applications, only a subset of interacting multi-field variables is directly available, but for a comprehensive view of solar wind prediction and downstream magnetohydrodynamic simulations, a more complete boundary state is required. In this work, we study the problem of learning the multi-field multi-scale solar magnetohydrodynamic state at 30 solar radii ($R_\odot$) using operator learning. Specifically, given the radial velocity and radial magnetic field, we aim to reconstruct the non-radial velocity and magnetic field components, radial and non-radial current density, thermodynamic density, and pressure components. This mapping is highly nonlinear, spatially coupled, and multi-scale, making it a challenging task for data-driven scientific machine learning.
To address this problem, we employ a Local Neural Operator (LocalNO) that learns mappings between input and output function spaces while retaining locality and resolution-awareness. Unlike conventional regression models and autoencoder models, neural operators are better suited for learning structured field-to-field transformations arising from physical systems. The resulting predictions along with inputs are intended to serve as boundary condition variables for future inner-heliospheric modeling pipelines.

---


### 244. [ReCoG: Reciprocal Co-Evolution for Multimodal Graph Learning](https://arxiv.org/abs/2608.22786)

**<font color=#1a73e8>作者：</font>** Rui Xue, Tianfu Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal graph learning requires jointly training over graph structure and heterogeneous node attributes, yet existing methods largely decouple these processes: prior multimodal graph neural networks (GNNs) focus on aligning modalities in a shared embedding space while operating on fixed or weakly adapted graph structures, and graph structure learning approaches infer topology from unimodal node representations without accounting for multimodal interactions. This separation fundamentally limits the ability of GNNs to capture semantically meaningful relationships in multimodal settings, where observed edges are often noisy, incomplete, or misaligned with underlying semantics. We propose ReCoG (Reciprocal Co-Evolution for Multimodal Graph Learning), a new learning paradigm that tightly couples graph structure learning and multimodal representation learning through end-to-end reciprocal interaction. Concretely, ReCoG integrates (i) a multimodal graph refiner that infers and corrects edges using cross-modal semantic evidence, and (ii) a coupled cross-modal message passing mechanism that performs joint intra- and inter-modality propagation over the refined graph. This unified design yields greater expressiveness than decoupled or two-stage formulations and allows dynamic interaction between topology and representation learning. Across diverse benchmarks for node classification and link prediction, ReCoG consistently outperforms strong multimodal graph structure learning baselines, including graph foundation models. Our results demonstrate that reciprocal co-evolution of structure and semantics is important for effective multimodal graph learning, challenging the prevailing separation between topology and representation learning.

---


### 245. [GuidedFlow: An Attention-Guided Framework for Anomaly Detection in Additive Manufacturing](https://arxiv.org/abs/2608.22789)

**<font color=#1a73e8>作者：</font>** Sosmita Paul, Krishna Roy  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Additive Manufacturing (AM) plays a vital role in the ongoing industrial revolution. However, quality control remains crucial and challenging due to printing defects or potential cyber-physical intrusions. Image or video-based anomaly detection is a key effort towards addressing these challenges. Various approaches have been explored in this domain, including reconstruction-based, embedding-based, and flow-based methods. Though normalizing flow-based methods address some of the core challenges of unforeseen defects and generalization while maintaining detection performance, existing approaches struggle with tiny/stringing defects common in 3D printing. In a small-data setting, this poses a limitation in generalization. To address these limitations, we propose \textbf{GuidedFlow}, a novel attention-guided normalizing flow model for anomaly detection and localization. GuidedFlow employs a pre-trained ResNet model, fine-tuned on the domain dataset. An attention-guided spatial and temporal flow framework models the dynamics across multiple scales and frames. A Spatio-Temporal Attention Network (SAN) enables the flow model to prioritize relevant contextual cues from input frames. We evaluate GuidedFlow on our AM3D-AD dataset, consisting of benign and anomalous real 3D printed object images and videos. We also conduct a comparative study using the MVTec-AD industrial image anomaly detection dataset. Experimental results demonstrate that GuidedFlow outperforms most of the state-of-the-art models with enhanced detection accuracy and AUROC.

---


### 246. [VersaDB: A High-Performance AI Storage Database for Unifying Mutimodal Datasets](https://arxiv.org/abs/2608.22795)

**<font color=#1a73e8>作者：</font>** Cong Wang, Zelin Liu, Yang Luo Ran Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The AI field has been rapidly developing, leading to the emergence of a large number of AI training datasets of various types. These datasets contain different modalities, including text, images, audio, etc., and may come in various data storage formats. With the advancement of AI hardware, AI computation units like GPUs, TPUs, and NPUs can greatly accelerate the training speed of AI models, which in turn increases the demand for faster data processing. When using existing AI processing frameworks to handle datasets with different modalities and storage formats, processing speeds may be suboptimal due to issues such as data layout and the way users handle the data. Therefore, using a unified database to store multiple data formats can better manage and optimize data access. In this paper, we introduce VersaDB, a database designed specifically for AI datasets with various modalities. We implemented a page-based storage system, separating structured and unstructured data. Additionally, we generated B+ tree-based index files to accelerate data access. VersaDB supports automatic sharding and maintains a hierarchical metadata management system, with corresponding metadata maintained at the page, shard, and global levels, forming the foundation for the efficient operation of the database. We also focused on ease of use by providing APIs for directly converting datasets into VersaDB, as well as APIs for converting popular AI data storage formats (e.g., CSV, TFRecord, .bin) into this http URL experiments show that using VersaDB can achieve up to 5.35x acceleration and maintain consistent performance across different parallelism levels.

---


### 247. [Contrastive Representation-Guided Genetic Minority Oversampling for Imbalanced Time-Series Classification](https://arxiv.org/abs/2608.22804)

**<font color=#1a73e8>作者：</font>** Wenbin Pei, Yunrong Hao, Zhen Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world time-series classification tasks often exhibit class imbalance, which can be extremely severe in some applications. To avoid training biased classifiers on imbalanced data, sampling is one of the most popular data pre-processing techniques because of its classifier-agnostic nature. However, due to the complex temporal dependencies in original time-series data and the scarcity of minority-class samples, existing sampling methods, including interpolation-based oversampling methods and deep learning-based generative models, usually suffer from limited generalization and poor diversity when generating new time-series samples. This paper proposes a Frequency-domain representation-guided Multi-tree Genetic Programming-based oversampling approach (FreMGP) to imbalanced time-series classification, where each individual represents a set of synthetic samples for the minority class. A frequency-domain class-discriminative representation module based on contrastive learning is also developed, guiding the evolutionary search toward high-quality synthetic time-series samples. Experiments on imbalanced time-series datasets demonstrate that FreMGP outperforms existing oversampling methods and consistently improves the performance of different classifiers, including both general machine learning and deep learning models.

---


### 248. [Change Detection in Probability Flow ODE: Online Testing in Diffusion Latent Spaces](https://arxiv.org/abs/2608.22807)

**<font color=#1a73e8>作者：</font>** Artem Kraevskiy, Artem Prokhorov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A rapidly growing range of sequential data tasks, such as identifying trend reversals in financial markets, auto-segmenting video and audio recordings, detecting changes in movement direction from motion sensors cannot be fully addressed without detection of distributional shifts in time-ordered data. We consider a sequential change-point detection problem where the conditional density switches at an unknown time, yet neither the pre- nor post-change distribution admits a closed-form. Classical likelihood-ratio statistics are inapplicable in this settings.
A conditional diffusion model, trained on pre-change-point data with a frozen context encoder, defines a deterministic bijection via the probability flow ODE. Pre-change observations are mapped onto standard Gaussian latent variables. Post-change observations, processed through the same frozen map, deviate from this reference. We employ the Maximum Mean Discrepancy as the test statistic, derive closed-form expressions for its components under the Gaussian null, and establish its asymptotic distribution as a degenerate U-statistic. Afterwards we apply an online detection procedure of Shiryaev--Roberts to the resulting statistic with exact threshold calibration.
The method detects arbitrary distributional shifts, including covariance rotations and higher-order structural breaks, without parametric assumptions on either regime.

---


### 249. [SAGE: Stability-Aware Graph-Based Ensemble Feature Selection for Explainable Postpartum Depression Risk Prediction](https://arxiv.org/abs/2608.22809)

**<font color=#1a73e8>作者：</font>** Md. Rokon Islam Emon, Syed Shariar Alam Shuvo, Shahriar Siddique Ayon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Postpartum depression (PPD) poses a major burden on maternal and child health, especially in low- and middle-income countries where prevalence exceeds 19%. Despite advancements in machine learning for PPD prediction, current approaches are limited by opaque global explanations that lack clinical usefulness at the patient level, unstable feature selection, and poor generalization under class imbalance. We propose SAGE, a Stability-Aware Graph-Based Ensemble feature selection system that incorporates both local explainable AI and a genetically optimized artificial neural network (GA-ANN). Using a primary cohort of 766 postpartum women, SAGE combines information-theoretic relevance, PCA-based structure, and graph-based interactions with bootstrap stability weighting to identify robust and non-redundant predictors. The GA-ANN architecture, optimized using a genetic algorithm and enhanced with GAN based oversampling, achieved strong performance with 87.96% accuracy, 86.32% F1 score, and 0.88 AUC using only 16 features, outperforming baseline and other feature selection methods. Psychological and socioeconomic factors such as EPDS score, PHQ-9 score, feelings about motherhood, and abuse history are the main predictors, while demographic factors have less influence. The LIME-based explanations allow instance-based insight into selected features from the graph, enabling personalized risk assessment. The findings make SAGE a scalable, interpretable, and clinical tool for early identification of PPD in health-care limited resources.

---


### 250. [Direct, Parallel, or Sequential? A Comparative Study of Training-Free Multi-Subject Image-to-Video Generation](https://arxiv.org/abs/2608.22819)

**<font color=#1a73e8>作者：</font>** Yanliang Qi, Kexi Chen, Muchao Ye 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-conditioned image-to-video (I2V) generation has advanced rapidly, yet generating videos with multiple subjects remains challenging. A model must simultaneously preserve the appearance of each subject, assign distinct motions, and maintain coherent spatial and temporal interactions. This paper presents a systematic study of three representative paradigms for training-free multi-subject I2V generation: direct, parallel, and sequential generation. Direct generation applies a pretrained I2V model to the complete reference image and prompt, requiring all subjects and motions to be synthesized jointly. Parallel and sequential generation instead decompose the reference image and prompt into subject-specific visual and textual conditions. Parallel generation synthesizes each subject independently and subsequently composes the resulting videos, reducing the complexity of each generation step at the cost of weaker inter-subject context. Sequential generation first synthesizes a background video and then progressively introduces individual subjects. This preserves accumulated scene context but introduces sensitivity to subject ordering and error propagation. We empirically evaluate the three paradigms across diverse multi-subject scenes, comparing appearance preservation, motion fidelity, temporal consistency, and inter-subject coherence, while also characterizing their distinct failure modes. Our findings reveal the strengths and limitations of each paradigm and offer practical insights for designing controllable multi-subject video generation systems.

---


> [!TIP]
> 当前位于：**201-250**（第 5/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-361](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
