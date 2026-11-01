# 📦 其他研究 | 2026年11月02日

> 本类共 **432** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-432](./part-09.md)

---

### 201. [Representation Complexity Along Learning Trajectories: Trading Width for Precision and Time](https://arxiv.org/abs/2610.39027)

**<font color=#1a73e8>作者：</font>** Ryan Singh, Miguel De Llanza, Christopher L. Buckley  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> What computational role does overparameterisation play during learning? Information-plane analyses suggest that neural networks can traverse representations substantially more complex than those required by their final predictors. We explore when this transient complexity serves a computational purpose by comparing the representation complexity needed for prediction with that needed to make an unknown target statistically visible through gradient feedback. We introduce an oracle model of neural network learning and use Kolmogorov \(n\)-widths to quantify effective representation complexity. Our main technical result transfers complexity bounds from the forward representation to the corresponding gradient-query features. Combined with statistical-query lower bounds, this gives a task-agnostic lower bound on the initial effective width required for target-dependent gradient information to become detectable. For \(k\)-sparse parity in \(D\) dimensions, a known target admits an \(O(k)\)-width representation, while the general bound already implies a polynomial separation between representation and discovery. We then exploit parity's invariance under coordinatewise sign reflections to identify a sharper unsigned effective width, which removes sign distinctions invisible to the parity information channel. At a transfer-compatible measurement resolution, its critical scale is \(\widetilde{\Theta}_k\left( D^{k-1}\tau^2 \right)\), up to logarithmic factors. Thus, the representation resources required to discover a predictor can substantially exceed those required to represent it once learned. Interpreting precision through accumulation over fresh samples yields a corresponding width-time frontier. Experiments support the predicted dimension dependence and examine how optimisation and generalisation depart from this idealised frontier.

---


### 202. [FairSplit: Decomposing the Embedding Space for Fair Classification](https://arxiv.org/abs/2610.39031)

**<font color=#1a73e8>作者：</font>** Andrii Shkabrii, Anna Beer, Ylli Sadikaj 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fair classification faces a twofold challenge: maintaining high classification accuracy while limiting reliance on sensitive information. Our method FairSplit achieves this by learning a decomposition of the embedding space into a Fair Space used for prediction and a Sensitive Space that isolates sensitive information. During training, the model must simultaneously learn the classification task and separate fair from sensitive information. The Sensitive Space gives sensitive attributes a destination, so the Fair Space can be used for prediction without relying on them. This decomposition is guided via a learnable mask and the Hilbert-Schmidt Independence Criterion (HSIC) as a measure of statistical dependence. We provide theoretical guarantees showing that the demographic parity gap is upper-bounded by both (i) the learned dimensionality of the Fair Space and (ii) the HSIC between the Fair Space and sensitive attributes. FairSplit effectively handles multiclass tasks and non-binary sensitive attributes, overcoming key limitations of existing fair classification methods. Experiments on established fairness benchmarks show that FairSplit achieves competitive accuracy-fairness trade-offs. Code is available at this https URL.

---


### 203. [LightGenBench: A Benchmark for 3D Emission Generation](https://arxiv.org/abs/2610.39038)

**<font color=#1a73e8>作者：</font>** Dongchen Yang, Xingguang Yan, Manolis Savva  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent generation methods produce 3D assets with detailed geometry and rich textures. However, these assets are non-emissive: they reflect light but emit none. We study a new task, emission generation: predicting spatially varying RGB emission over a 3D asset's surface from its geometry, non-emissive materials, and a rendered view.
To support this task, we introduce LightGenBench. Our benchmark makes three contributions. First, we curate a dataset of 37k artist-authored emissive assets in UV, voxel, and multi-view form. Second, we establish baselines across four method families: UV-domain, sparse-voxel, multi-view, and segmentation-based generation. Third, we design an evaluation protocol that measures where an asset emits and how, complemented by user-study comparisons on renderings with varying emission strength.
Across the four families, the sparse-voxel baseline TRELLIS.2-Emission performs best because generating emission natively in 3D avoids the failure modes of the other representations, such as the fracturing artifacts of UV space and the occluded emitters that multi-view generation cannot see. However, TRELLIS.2-Emission only reaches an IoU of 0.271, leaving the task far from solved. We hope LightGenBench establishes emission generation as a benchmarkable problem for 3D generation.

---


### 204. [Exponential-Nemytskii Neural Operators: Learning Field Evolution Across Step Sizes](https://arxiv.org/abs/2610.39041)

**<font color=#1a73e8>作者：</font>** Jingye Li, Jinglai Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In variable-step operator learning, agreement at observed step sizes does not by itself determine predictions at other temporal resolutions. We propose an operator whose step-size dependence is prescribed by a first-order Duhamel approximation of semilinear dynamics. It combines exact linear propagation with a local nonlinear function of the field and its derivatives, allowing evaluation below the observation interval without supervision densely sampled across step sizes. Under suitable conditions and at fixed spatial resolution, we prove that agreement between models at two step sizes controls their prediction differences throughout a prescribed range. We also give conditions for local identifiability of both components from two step sizes, supporting interpretation of the learned structure. A latent extension applies the same construction to learned fields. We evaluate the base model on two synthetic problems and the extension on two real datasets against several baselines.

---


### 205. [When Should AI Decide, Defer, and Deviate? Responsible Automation for Deceased Donor Kidney Allocation](https://arxiv.org/abs/2610.39045)

**<font color=#1a73e8>作者：</font>** Madeleine Pollack, Thomas Daillak, Mehmet Toner 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We ask when an AI trained on historical decisions should be allowed to recommend decisions, defer to human experts, or in other cases, flag concerning patterns in data and deviate from past practice. This can be challenging because past decisions record what was done rather than what should have been done, and where data is sparse, a model's predictions may be too uncertain to act on. We provide a framework for addressing this problem using a case study in deceased-donor kidney allocation. Nearly 30% of kidneys recovered from deceased donors in the United States are never transplanted, largely because they are hard to place through the standard waitlist sequence. One can use AI to flag kidneys at risk of delayed or failed placement for out-of-sequence (OOS) allocation, but this comes at the cost of bypassing candidates higher on the waitlist. Thus, OOS allocation should only be used when the organ is demonstrably at high risk of discard on the standard sequence. Using Organ Procurement and Transplantation Network match-run data from 2016-2019 and 2023-2025 (excluding COVID-19-disrupted years), we build the Arbitrator framework, which combines various interpretable models and acts only when the uncertainty in their predictions cannot change the preferred action. Our Arbitrator resolves 93.5% of organ placement decisions using explicit medical criteria learned from data, and defers the remaining 6.5% to a human or a more complex model. We show that the Arbitrator correctly identifies 70.1% of historically discarded low-KDPI kidneys as OOS candidates, projecting that up to 43.9% of historically discarded kidneys could be flagged for expedited placement and potentially transplanted. We then exploit the interpretability of the Arbitrator to create an agentic audit comparing the learned rules to published clinical literature in order to flag decision-making patterns that are contentious.

---


### 206. [Reinforcement Learning for the Game of Balatro: A Fast Simulator and Two-Policy Training Approach](https://arxiv.org/abs/2610.39049)

**<font color=#1a73e8>作者：</font>** Ajay Vikram Periasami, Anjaneya Gupta, Ethan Cheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Balatro, a 2024 roguelike deckbuilder, presents three difficulties that have historically derailed reinforcement learning methods: a 3,000-action state-dependent action space, horizons of several hundred decisions with sparse rewards, and pervasive stochasticity in both card draws and shop generation. Published RL results on the game remain scarce. We introduce an end-to-end pipeline comprising (i) a high-throughput Rust simulator that is automatically state-diffed against the live game client via BalatroBot, (ii) a condensed observation-action interface with dynamic per-step masking of legal moves, and (iii) a multi-agent PPO architecture that decomposes play into a tactical blind policy and a strategic shop policy that share the full game state but act in disjoint phases. Long-horizon credit assignment is partially addressed by per-agent reward routing with explicit cross-agent credit. On the main joint run, training metrics show a sharp phase transition in which the first-blind clear rate converges above 99% and mean episode return increases by roughly an order of magnitude, plateauing at a mean maximum ante of 3 out of 8; single-agent baselines under identical rewards oscillated between greedy and hoarding failure modes and did not stably clear the first blind. These results establish the two-policy decomposition as a strong reactive baseline for Balatro and localise the remaining gap to long-horizon strategic planning rather than tactical blind play.

---


### 207. [BASILISC: Bayesian Alignment of Siamese-Integrated Latents for Inferring Single-cell Correspondence](https://arxiv.org/abs/2610.39050)

**<font color=#1a73e8>作者：</font>** Sepideh Saran, Mahsa Ghanbari, Uwe Ohler  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Single-cell assays study the genome one cell at a time. Unimodal assays measure one molecular layer, the newer multimodal assays measure several. Most data are single-modality, so integrating them relies on models trained on multimodal assays, where the cell correspondence across modalities is known. These models return a matching, but rarely a confidence measure. We present BASILISC (Bayesian Alignment of Siamese-Integrated Latents for Inferring Single-cell Correspondence), a framework for matching single-cell representations with uncertainty on the correspondence itself. A BASILISC model is a probabilistic siamese network over the two modalities with a predictive distribution over the correspondence for a cross-modal pair of cells. We instantiate it at two levels: at the cell-type level the question is whether two cells share a cell type, at the cell level which cell is the partner in the other modality. To our knowledge, this is the first uncertainty score on a learned cross-modal correspondence evaluated against a known ground-truth pairing. BASILISC learns a similarity across modalities that reflects cell lineage: an unseen cell type is matched to its lineage relative, matching still works on such held-out types (balanced accuracy 0.86 on unseen against 0.93 on seen types), and the predictive uncertainty rises on these out-of-distribution cells. The uncertainty score also selects high-quality matches for downstream analysis: discarding the least certain fifth of the pairs raises accuracy from 0.93 to 0.98. At the cell level, a deep ensemble of the deterministic matcher reaches 0.062 matching accuracy on the benchmark test set, above the competition winner; on the Bayesian matcher's assignment, the posterior flags the wrong matches that cross a cell-type boundary better than a deterministic read of the same scores (AUROC 0.68 against 0.64).

---


### 208. [DeepDiff: Neuro-Dynamic Regression-Freedom Checking for Security Patch Validation](https://arxiv.org/abs/2610.39066)

**<font color=#1a73e8>作者：</font>** Laboni Sarker, Shuvendu K Lahiri  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Automatically validating AI-generated security patches remains a significant challenge. Eliminating a reported crash and passing existing test suites do not provide sufficient confidence that a patch correctly addresses the underlying vulnerability without introducing regressions. We present DeepDiff, a technique for regression-freedom checking that differentially evaluates candidate patches against the original vulnerable program using non-crashing inputs that exercise the affected code paths. The expectation of regression-freedom is that a correct patch should eliminate the vulnerability triggering crash while preserving the intended behavior on non-crashing inputs. To support this evaluation, we introduce a dataset of correct and incorrect patch candidates for open-source memory-safety vulnerabilities from CyberGym. We explore different approaches for non-triggering test input generation to reach the patched code, a purely neural regression-freedom checker, and a hybrid approach that combines dynamic analysis with neural techniques. Our experimental results demonstrate the effectiveness of regression-freedom checking in validating security patches while outlining the challenges that remain.

---


### 209. [Certified Access: Test-Time Compute on Conservative Physics-Structured AI Memory](https://arxiv.org/abs/2610.39073)

**<font color=#1a73e8>作者：</font>** Pratik Jawahar, Riccardo Maggioni, Jonas Petersen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Test-time compute mechanisms, such as retries, confidence-based escalation and non-local routing, are conventionally deployed as black-box additions to trained models. They typically add forward passes or halting heads, but give no structural account of what the extra compute buys or what it costs against the model's stability guarantees. We therefore propose a theoretical and empirical framework for test-time compute on a Latent Dynamics Model used as the memory. When an encoder's latent state $(q,p)$ is advanced by a damped symplectic (velocity-Verlet) step of a learned Hamiltonian, every mechanism that expands access has an exact phase-volume Jacobian, a bounded energy change and an exact latch-transport law. We split reachability failures into escape failures and reach failures. A Lorentz squeeze resolves escape failures by injecting bounded, re-absorbable energy. A gated canonical translation (a one-step channel across $C_T$) resolves reach failures at $\detJ=1$ exactly. We verify this certificate stack on a designed analytic testbed. Reaching just beyond $C_T$ with the squeeze requires energy that grows quadratically in the excess distance. The gated channel's energy cost equals the potential difference between its endpoints, which is zero on the matched channel measured here, and so does not grow with distance in this testbed. An untrained state-replacing map annihilates phase volume and erases stored charge, while the gated channel transports it. On a learned physics-structured memory, we show calibrated compute rationing and evaluate the scaling limits of non-local routing against a physics-free baseline. The main contribution is the formalization and verification of the certificate stack, not benchmark performance.

---


### 210. [Usable String Matching by Humans through Overlaid Presentation](https://arxiv.org/abs/2610.39084)

**<font color=#1a73e8>作者：</font>** Enka Blanchard, Ted Selker, Alan T. Sherman 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We explore the ability of humans to compare strings, an error-prone activity which occurs in critical contexts (e.g., bank wire transfers), where it is not always possible to trust a machine to help.
We hypothesize that understanding human cognitive and perceptual limitations can improve how people verify whether two character strings are identical. We vary the strings' relative positions and presentation formats to measure comparison speed and accuracy.
We present results from two online experiments with 178 human subjects who compared pairs of strings to determine whether the two strings were identical. The strings varied by length (5 characters to small paragraphs), difference (matching versus making a random change or a hard-to-detect one), alignment (vertical versus horizontal), and presentation (Overlay versus Adjacent).
Our experiments test whether, by encoding and memory tasks into perceptual tasks, overlay formats can offer advantages in speed and accuracy. Results show that overlay offers a substantially faster method, with improved accuracy for long strings. Nevertheless, mean error rates were at least 4 percent, indicating that even the improved approach may be insufficiently accurate for many verification tasks.

---


### 211. [HALO: Human-Grounded Granular Evaluation of Proactive Agents](https://arxiv.org/abs/2610.39086)

**<font color=#1a73e8>作者：</font>** Wenqi Pei, Xinyu Wang, Jinrui Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Proactive agents must decide whether, when, and how far to assist without an explicit request. Existing evaluations often rely on automated scores or binary verdicts, offering limited human diagnosis of evidence use and intervention quality. To address these gaps, we introduce HALO, Human-Grounded GrAnular EvaLuation of PrOactive Agents. HALO-Arena covers 4 proactive need types, Dependency, Blockage, Risk, and Opportunity, across 10 everyday domains and 50 personal environments. Scenarios require agents to retrieve evidence from structured databases or unstructured documents before judging whether assistance is warranted and choosing its scope. On HALO-Arena, we construct HALO-8K, a dataset of 8,000 responses from 10 models across 400 scenarios, annotated by 20 experts for action level, acceptability verdicts, and human diagnosis. For rejected responses, human diagnosis covers timing, intensity, and other issues. Recorded reasoning tokens and retrieval rounds measure the effort behind these responses. The best proprietary and open-source models achieve 72.88% and 56.63% acceptability, respectively. Our central finding is that over-proactivity is the dominant observed failure mode, with Premature timing or Excessive intensity accounting for 61.20% of rejected responses. Further analyses yield complementary findings on the balance between intervention and restraint, evidence acquisition, and the calibration of timing and intensity.

---


### 212. [Generating Critic-Guided Synthetic Experience in Latent World Models](https://arxiv.org/abs/2610.39100)

**<font color=#1a73e8>作者：</font>** Jorge de Freitas, Christos Ziakas, Alessandra Russo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning from offline datasets is limited in scalability, as collecting new experience is often costly or unsafe in the real world. World models offer an alternative way to generate new experience through a learned dynamics model, yet learning policies in latent space is limited due to compounding errors in imagined rollouts. To this end, we propose using the world model as a local transition generator, leveraging critic guidance to choose actions inside that model to generate synthetic experiences. We study action refinement methodologies, introducing Critic-Guided Synthetic Experience (CGSE) generation in world models. Specifically, CGSE augments an existing offline dataset by sampling candidate actions using an offline policy and refining each to maximize a first-order approximation of the $Q$-function within a trust region. We then use a frozen latent world model to imagine the future state given each updated action, and use the critic to choose the best one, appending this synthetic transition to the replay buffer. Our method requires no additional real-environment interaction or test-time planner, as it generates synthetic experience offline using the world model. On three OGBench manipulation tasks, CGSE improves an offline policy by a relative improvement of $7.1\%$ on the average success rate.

---


### 213. [From Local Recovery to Unified Generation: Discovering Triple Set in Knowledge Graphs via Observation-Anchored Latent Diffusion](https://arxiv.org/abs/2610.39114)

**<font color=#1a73e8>作者：</font>** Jiaqi Wang, Yisen Gao, Huayang Shi 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Triple set prediction (TSP) is to recover missing relational triples in a knowledge graph by predicting the triple set instead of isolated links. Existing approaches predominantly rely on the subgraph-based completion paradigm, where the original graph is first partitioned into local subgraphs which are then independently completed. Such a paradigm suffers from fragmented structural reasoning, limited cross subgraph dependency modeling, and missing predictions across subgraphs. This paper proposes LatentDiff, a novel unified latent generative framework for TSP, which reformulates knowledge graph completion as latent space graph generation. LatentDiff first learns a compact latent representation using a relation-aware residual-quantized knowledge graph autoencoder, which encodes the whole graph into relation-aware latent embeddings, quantizes them with chunked residual codebooks, and reconstructs triples through a factorized decoder. On top of this latent space, we introduce an observation-anchored latent graph diffusion model, where the target latent graph representation is perturbed toward the observed latent. The reverse process recovers missing triples through progressive latent denoising. Experiments on three benchmark datasets show that LatentDiff outperforms the SOTA in terms of F_{tsp} by 5.4 percentage points on average. Code: this https URL.

---


### 214. [Uncertainty-Guided Cross-Modal Alignment for Diffusion-Based IoT Intrusion Detection](https://arxiv.org/abs/2610.39117)

**<font color=#1a73e8>作者：</font>** Mahdi Arab Loodaricheh, Anita Raja, Mohammad Hossein Manshaei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models evolve noisy states toward a learned data distribution, so their sampling behavior depends on the geometry of the representation in which denoising occurs. This dependence is especially important for multimodal data: independently trained encoders can map synchronized views to incompatible latent regions, while uniform alignment can let an uncertain view distort the shared geometry. To address this gap, we introduce a novel reliability-guided alignment rule that uses normalized VAE posterior variance to control directional cross-modal influence before diffusion training. We study this issue in minority-attack generation for imbalanced Internet-of-Things intrusion detection. Tabular flow attributes, a DeepInsight image, and a packet sequence are encoded by modality-specific variational autoencoders. Per-modality normalized VAE posterior variances provide bounded, sample-specific weighting signals in an asymmetric stop-gradient alignment objective. We use these quantities as heuristic encoder-derived reliability proxies rather than calibrated probabilistic uncertainties. The full modality-specific latent means obtained after alignment fine-tuning are standardized and modeled jointly by a class-conditional EDM; a second-order sampler then generates paired attack-conditioned latent blocks for the three decoders. In controlled experiments on TON-IoT, uncertainty-aware alignment obtains the highest mean precision, recall, density, and coverage among three diffusion variants. Augmenting only the training split yields ROC-AUC 0.9515, PR-AUC 0.8954, balanced accuracy 0.8395, and attack-class F1 0.7940 on an untouched real test set. Among the two variants with matched alignment fine-tuning, posterior-variance-based weighting improves both tabular generative fidelity and downstream detection relative to uniform weighting.

---


### 215. [Clean Sheets and Checkpoints: Evidence Complexity for Certifying Sequential Agent Risk](https://arxiv.org/abs/2610.39124)

**<font color=#1a73e8>作者：</font>** Rohith Yanambaka Venkata, Don McBride, Tiago Sequeira 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dangerous-capability evaluations often test an AI agent from prepared states at ordered milestones. A clean sheet records no successes. What it certifies about a campaign of $B$ attempts depends on what a failed attempt erases. We model the task as a chain of $k$ milestones divided into checkpoint segments and ask how many zero audit responses certify, at level $\alpha$, a completion probability of at most $\epsilon$. For segments chosen before the audit, counting possible completion windows gives a certificate for any specified budget. The bound also covers adaptive deployment processes that follow the chain's transitions, provided their success probabilities after every complete history are capped by the corresponding audit success probabilities. The audit does not test this transport assumption. In rare-risk phase interiors, each segment is either rarely completed within the budget (active) or nearly always completed (free). The minimum expected number of zero responses is asymptotic to $\log(1/\alpha)\,(B^a/(a!\,\epsilon))^{1/K_A}$, where the $a$ active segments contain $K_A$ milestones and are those at least as long as a budget-dependent threshold. The certificate attains this constant. Every asymptotically optimal evaluator must divide its expected response count equally among active milestones in the limit, with a vanishing share elsewhere. Where a single segment passes from active to free, each of its milestones receives a smaller limiting share than an active milestone; a crossover-aware certificate attains the optimal constant. For selected segments with known or unqueried prefix steps, counting failed cycles can sharpen the certificate.

---


### 216. [DICE: Decentralized Incentive-driven Federated Learning for Efficient & Scalable Customization of Pretrained Models in Web3](https://arxiv.org/abs/2610.39132)

**<font color=#1a73e8>作者：</font>** Hong Lin, Zhongle Xie, Lidan Shou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Customizing Pretrained Models (PMs) for downstream tasks demands task-specific data, which burgeoning Web3 applications provide abundantly. Blockchain-powered federated learning (BCFL) offers a secure and privacy-preserving paradigm to customize PMs among self-interested and untrusted Web3 participants. Yet, existing BCFL algorithms face severe efficiency and scalability challenges when applied to large PMs, due to their substantial computational and memory requirements and the hardware constraints of many participants. This paper introduces DICE, a novel BCFL algorithm that addresses the efficiency and scalability challenges of customizing large PMs in Web3 via two sets of synergistic techniques: (i) a dynamic progressive learning scheme and a model slice verification scheme to enable a wider range of honest participants, including those unable to deploy the full model, to engage in customizing PMs, while preserving model utility; (ii) a tree-structured committee consensus protocol and an efficiency-driven incentive scheme to address the dominant bottleneck that hinders existing BCFL algorithms from scaling to a larger number of data holders for customizing data-hungry large PMs, while maintaining security. Theoretical analysis and extensive experimental results on customizing vision and language PMs demonstrate DICE's efficiency, effectiveness, and security.

---


### 217. [Kinematic Causal Attribution: Black-Box Explanations of Motion versus Geometry for 4D Point-Cloud Video Models](https://arxiv.org/abs/2610.39147)

**<font color=#1a73e8>作者：</font>** Zerui Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 4D perception models, which classify 3D point-cloud videos, are being built into robots, assistive monitoring and AR, yet before deploying one a practitioner cannot check which cue it relies on: how a body part moves, or what shape it has. 3D attribution is single-frame, video attribution is confined to RGB pixels, gradient maps need white-box access, attention is absent from state-space backbones, and point-level perturbations assume a point correspondence across frames that real depth and LiDAR data lack. We present Kinematic Causal Attribution (KCA), a black-box, interventional attribution method that queries only the model's outputs. Its freeze operator removes a region's motion while keeping its shape, and a shape-free proxy removes the shape while keeping the motion. Together they span a motion$\times$geometry cube for every tracked region, whose order-symmetric Shapley decomposition is complete and whose interaction is measured rather than assumed away. The operators rewrite per-frame point sets, so they need no correspondences, and a context-averaged estimator handles structures that span several regions. We validate KCA on the official PSTNet, P4Transformer and Mamba4D trained on MSR-Action3D. The decisive test is an audit: two binary tasks are built from real clips whose classes differ only in the motion or only in the shape of the same arm, and the motion share of the arm's importance follows the defining cue on all three backbones (0.83 vs. 0.60 on P4Transformer, 0.86 vs. 0.30 on PSTNet, 0.92 vs. 0.61 on Mamba4D), a distinction no single attribution map can make. The split costs no faithfulness: the necessity maps have the lowest deletion AUC on P4Transformer and PSTNet, tie with the best baseline on Mamba4D, and lose their correlation with the trained model's once the weights are randomised. Skeleton ground truth, re-sampling stability and cost complete the validation.

---


### 218. [STRATA: Reinforcement-driven Active Sampling with Tri-paradigm Adaptation for Efficient 3D Spatial Transcriptomics](https://arxiv.org/abs/2610.39151)

**<font color=#1a73e8>作者：</font>** Junchao Zhu, Ruining Deng, Chongyu Qu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial transcriptomics (ST) enables joint characterization of tissue morphology and gene expression. However, 3D volumetric ST acquisition remains expensive. AI-driven methods offer a low-cost alternative but remain limited in accuracy, while recent 2D section-wise ST acquisition still rely on dense grid sampling, resulting in redundant measurements and undersampling of biologically informative regions. To bridge the gap, we propose STRATA, a reinforcement-driven active sampling framework with tri-paradigm adaptation for reconstructing dense 3D transcriptomic maps from sparse voxel-wise ST acquisition. STRATA constructs a 3D graph integrating H&E morphology with single-cell priors and employs a reinforcement learning agent to estimate morphological sparsity and transcriptomic informativeness, enabling budget-aware selection of informative spots. Given these sparse measurements, an adaptive tri-paradigm predictor combines retrieval, regression, and cross-layer imputation through lightweight fusion, dynamically weighting their contributions. Experiments across datasets demonstrate improved sampling efficiency and accuracy, particularly under low-budget settings. Code is available at this https URL.

---


### 219. [Unlocking with the Heart: Investigating User Perceptions of ECG-Based Biometric Authentication](https://arxiv.org/abs/2610.39152)

**<font color=#1a73e8>作者：</font>** Farnaz Farid, Linet Momposhi, Tamara Watson 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Password-based authentication remains challenging for many users, especially for those who face usability and accessibility issues. The burden of maintaining security can cause user fatigue, frustration and non-engagement. To address these issues, we conducted a pilot study to assess ECG-based biometric authentication as a passwordless alternative and to gather adult participants' perspectives on this approach. The research consisted of a survey study, an authentication prototype and a follow-up usability experience questionnaire. Our approach combined an online survey of 337 adults examining authentication practices and perceptions, with a separate usability evaluation in which 49 participants interacted with a simulated ECG-authentication and password interface in a health-care application prototype, then completed a post-test usability test questionnaire. The survey examined how adults across age groups use and perceive various authentication techniques, their experiences with biometrics, their views on security and convenience, and their willingness to adopt ECG authentication. In parallel, the usability prototype and questionnaire captured participants' responses after hands-on interaction with an ECG authentication prototype.

---


### 220. [CLaW: Codec-Guided Adaptive Latent Watermarking for Traceable Diffusion Image Generation](https://arxiv.org/abs/2610.39160)

**<font color=#1a73e8>作者：</font>** Huangchao Song, Lingyun Yu, Cong Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the rapid advancement of text-to-image diffusion models, increasingly realistic AI-generated content has raised serious concerns about misuse and copyright infringement. Digital watermarking offers a promising solution by enabling user-level traceability, yet existing methods remain difficult to deploy at scale, hindered by costly model retraining or detection, poor effectiveness-fidelity trade-offs, and limited robustness to image transformations. To address these challenges, we propose CLaW (Codec-guided Latent Watermarking), a robust and efficient watermarking framework for traceable diffusion image generation with frozen diffusion backbones and inversion-free detection. Specifically, CLaW first uses a pretrained watermark codec to map each watermark message to a latent residual, enabling low-cost sampling-time injection. Then, the residual is injected within a late denoising window, where image semantics are better preserved and the watermark signal is less perturbed by subsequent denoising updates, yielding a better balance between watermark effectiveness and image fidelity. Furthermore, we introduce a decoder-guided adaptive injection mechanism that uses decoding confidence as feedback to dynamically calibrate watermark strength, reinforcing weak watermark signals and improving robustness under image transformations. Extensive experiments show that CLaW preserves high visual fidelity and achieves state-of-the-art robustness under image transformations, enabling reliable user-level traceability.

---


### 221. [Joint Rigid Alignment and Morphable Reconstruction from Partial 3D Face Scans](https://arxiv.org/abs/2610.39161)

**<font color=#1a73e8>作者：</font>** Eli A. Underwood, Nicolas Rondan, Angel V. Peterchev 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aligning a partial, real-world 3D face scan to a canonical representation requires solving two coupled problems at once: estimating the rigid pose that brings the scan into a common frame, and completing the facial shape in regions the scan never observed. Existing pipelines typically decouple these steps, running a generic point-cloud registration front end followed by a separate non-rigid fitting or deformation stage. Building on the GeoTransformer superpoint-matching architecture, we propose a single network that predicts both a rigid pose and a shape-complete point cloud in one forward pass: a cross-attention regressor, conditioned on transformer point features and predicted coarse correspondences, maps a partial scan to per-patch coefficients of a 3D morphable face model learned offline from a corpus of 8,000 identities. The resulting morphed template is then used, in the same forward pass, as the target for fine-grained Sinkhorn matching and rigid pose estimation, supervised purely by geometric alignment to ground-truth morphed geometry, so no hand-labeled coefficients are required. Against six classical and learned non-rigid registration baselines on held-out identities, our method leads the strongest ones by 3-4 times on per-vertex error and baselines that collapse the head onto the visible region by more than an order of magnitude, and is simultaneously the most accurate and fastest method on ground-truth-free scans from two independent real-scan datasets, NoW and NPHM. Code will be made publicly available.

---


### 222. [A Novel Approach to Evaluating Evaluation Metrics for Multi-Output Structured Prediction](https://arxiv.org/abs/2610.39162)

**<font color=#1a73e8>作者：</font>** Akshay Vyas, Angelo Pimienta, Nicholas Ruozzi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In multi-output structured prediction tasks, while only one ground truth label may be provided in the training data, multiple equally valid outputs may be possible, making reliable evaluation a persistent challenge. We postulate that human evaluators implicitly use task-specific invariants, e.g., object boundaries in colorized images or named entities in translations, to judge if an output is acceptable. Under this assumption, we introduce a notion of approximate task-specific invariants and use them as diagnostic tools to evaluate a variety of existing metrics for vision and language tasks. We use these task invariants as part of a framework to systematically test metric reliability by encouraging domain-relevant invariants in model outputs via an augmented loss function. In our experiments, we observe that enforcing invariants with an augmented loss yields substantial improvements in popular distributional metrics while more traditional metrics change only marginally. Through this invariants-driven evaluation, we expose where standard metrics fail to detect meaningful differences, and we highlight the conditions under which distributional metrics succeed or still fall short.

---


### 223. [ACAM-J-MARS: Multi-Atlas Riemannian Spectral Representations for Decoding Advanced Meditation States from fMRI](https://arxiv.org/abs/2610.39171)

**<font color=#1a73e8>作者：</font>** Jian Wang, Winson F.Z. Yang, Wugeng Zheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inferring jhana-type advanced concentration absorption meditation (ACAM-J) states from fMRI data is challenging due to the spatially distributed nature of meditation-related effects, substantial inter-individual variability that can exceed within-subject state differences, and limited sample sizes. Conventional machine-learning approaches often formulate this problem as unimodal, Euclidean, atlas-based classification, thereby neglecting the non-Euclidean geometry of functional connectivity matrices and underrepresenting temporal information in functional magnetic resonance imaging (fMRI); these limitations can lead to suboptimal classification performance. We propose ACAM-J-MARS (\textbf{M}ulti-\textbf{A}tlas \textbf{R}iemannian \textbf{S}pectral representation), which computes functional connectivity using multiple atlases, represents symmetric positive definite (SPD) connectivity matrices on a Riemannian manifold, projects them into a log-Euclidean tangent space, and augments connectivity-derived features with low-frequency BOLD spectral energy to better resolve subtle state differences under heterogeneous variability. Evaluated on 204 segments from 22 practitioners, ACAM-J-MARS improves performance across multiple backbone models, achieving a balanced accuracy of 0.757 for early versus late ACAM-J classification and 0.545 for three-class classification, corresponding to a 10.8-point absolute improvement over the strongest baseline. These findings suggest that the proposed representation improves the decoding of advanced meditative brain states and may enable downstream applications such as closed-loop neurofeedback and real-time psychophysiological brain-computer interfaces.

---


### 224. [Edited Endpoints as Partial Goals for Image-to-Video Generation](https://arxiv.org/abs/2610.39179)

**<font color=#1a73e8>作者：</font>** Sihyun Kim, Sanghyun Jo, Kyungsu Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Edited endpoint images make the target of an image-to-video transition explicit and can improve transition completion, but also preserve context in the source image's layout. Full-frame endpoint conditioning turns this preserved context into requirements on the video's final state, potentially inducing temporal artifacts. We measure discontinuity with Hard-Cut (HC), late background reversal with Background Motion Reversal (BMR), and motion suppression with Dynamic Degree (DD). These artifacts appear across five video models spanning training-free and learned endpoint conditioning, in model-specific forms. We study Partial, a selective conditioning scheme that constrains only an edit-relevant region estimated from image-editor attention and leaves the remaining terminal content to the video model. Across three backbones on TC-Bench-I2V, Partial reduces temporal artifacts relative to full-frame conditioning, with no significant difference in Transition Completion Ratio (TCR); on Wan2.2-Turbo, uniformly weakening conditioning does not reproduce these reductions. A donor-context intervention keeps full-frame conditioning and replaces only the context outside the edit-relevant region with the final frame of a Partial video. It lowers HC and BMR on HunyuanVideo-1.5 and lowers BMR while restoring DD on Wan2.2-Turbo, with no significant difference in TCR, so constraint extent alone does not account for these artifacts. Together, these findings suggest that edited endpoints should serve as partial future goals, although edit relevance does not guarantee future validity. Code and data will be released at this https URL.

---


### 225. [Multi-level Constrained Learning for Underwater Image Enhancement](https://arxiv.org/abs/2610.39183)

**<font color=#1a73e8>作者：</font>** Wangtao Bao, Liping Xie, Kanjian Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Underwater image enhancement aims to correct color and recover detail degraded by wavelength-dependent attenuation, scattering, and noise. Paired-reference supervision constrains output similarity, but does not by itself specify the color mapping, the strength of local detail corrections, or consistency with the degraded observation. We propose MCL-UIE, a paired-supervised framework that addresses these requirements by constraining restoration operations and the training objective. Monotonic Chromatic Transform (MCT) restricts global color mapping in log-LMS space through positive diagonal entries and bounded cross-channel coefficients. Uncertainty-Gated Wavelet Reconstruction (UGWR) modulates high-frequency residuals with a learned confidence gate calibrated against normalized wavelet reconstruction errors. During training, Reference-Anchored Degradation Replay (RADR) renders the enhanced image and its paired reference using shared latent degradation proxies, encouraging both to reproduce the input. The three components share a restoration network that combines structured color correction, locally controlled detail recovery, and reference-anchored replay. MCL-UIE ranks first in thirteen of sixteen full-reference dataset-metric comparisons and produces competitive visual results on no-reference benchmarks. Objective ablations indicate that confidence calibration is most effective when combined with replay supervision. RADR is used only during training and adds no inference-time computation. Our code is available at this https URL.

---


### 226. [Provably Secure Diffusion Watermarking Against Removal Adversaries with Batched Detector Access](https://arxiv.org/abs/2610.39189)

**<font color=#1a73e8>作者：</font>** De Zhang Lee, Ee-Chien Chang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recent latent-based watermarking methods can embed undetectable watermarks into AI-generated content. However, these approaches are vulnerable to removal attacks as their watermark detection boundaries are exposed, prompting the use of secret long-term transformations to hide these boundaries. We show that such defenses are insecure under a stronger threat model motivated by publicly reachable detectors: an adversary with batched detector access can reconstruct the transformations, permanently re-exposing the decision boundary. To address this, we propose a watermarking scheme based on a hybrid of long-term and one-time secret transformations, which prevents the reuse of structure across samples and keeps the long-term secret hidden. Besides undetectability, we show that this scheme is provably secure against removal adversaries with batched detector access, in the sense that no probabilistic polynomial-time adversary can achieve a non-negligible advantage over an adversary restricted to adding isotropic white-noise with a $\sqrt{2}\times$ larger perturbation budget, and we show this $\sqrt{2}$ factor to be tight. Evaluations on Stable Diffusion 2.1 and XL demonstrate the attack against the existing defense, and show that our scheme preserves generation quality and withstands common perturbations and targeted removal attacks.

---


### 227. [Wearable Biosensors for Early Detection and Continuous Monitoring of Postpartum Depression: A Human-Centered Approach](https://arxiv.org/abs/2610.39191)

**<font color=#1a73e8>作者：</font>** Emma Ricci-De Lucca, Elizabeth L. Murnane  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Postpartum depression (PPD) is the leading cause of maternal mortality in the United States. However, there are significant gaps in PPD screening, detection, and treatment. A main challenge stems from limitations in existing methods for early PPD diagnosis and subsequent monitoring and intervention. Mobile technology that incorporates interactive interfaces and continuous wearable biosensors holds major potential to augment clinical decision-making and enhance PPD care. A number of compelling research directions exist in effectively developing such systems, including user experience design, sensing accuracy during perinatal stages, clinical integration and interoperability, acceptance and adoption, and privacy and ethics. By focusing on wearable devices that center women and their experiences, this paper discusses such challenges and opportunities at the intersections of HCI, inclusive physiological computing, and women's health.

---


### 228. [Analyzing Condensation on Patterned Surfaces via Deep Learning](https://arxiv.org/abs/2610.39195)

**<font color=#1a73e8>作者：</font>** Tae E. Cooper, Michael Gee, Sheila Whitman 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dropwise condensation is key to power and water systems. State-of-the-art condensation surfaces are often inhomogeneous, either patterned by design or random defects. Inhomogeneous surface features dictate the rates of each stage of dropwise condensation-nucleation, growth, coalescence, and shedding. Characterizing these rates requires the precise detection of thousands of droplets. Yet, existing segmentation methods are unable to detect droplets on inhomogeneous surfaces. We developed TileSAM3, a universal droplet segmentation tool built on the Segment Anything Model 3 (SAM3). Hierarchical tiling with per-tile inference followed by post-processing extended SAM3's detection cap and raised the effective resolution of small droplets. We created two datasets: High Quality Droplet Dataset (N=365,826; HQDD) with homogeneous surfaces and Low Quality Droplet Dataset (N=63,577; LQDD) with patterned, defect-laden surfaces under adverse lighting. TileSAM3 closely reproduced thresholding annotations on HQDD, surpassed it over sixfold on LQDD (Average Precision 0.57 versus 0.088), and outperformed other deep learning models on all metrics evaluated. Combined with KD-tree tracking, TileSAM3 identified localized nucleation and coalescence in narrow active bands on a stiffness-patterned surface. TileSAM3 enables analysis of understudied inhomogeneous substrates with poor lighting and videography which facilitates faster, lower cost research of condensation materials.

---


### 229. [COGS: A Diagnostic Benchmark for Attribute-Aware Object-Level 3D Gaussian Splatting Perception](https://arxiv.org/abs/2610.39201)

**<font color=#1a73e8>作者：</font>** Zheng Xiao, Yifan Liu, Weijian Deng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) is increasingly explored as an input representation for 3D perception. Yet it remains unclear how current 3D architectures exploit heterogeneous Gaussian attributes. This ambiguity makes accuracy hard to interpret and limits principled architecture design for 3DGS perception. However, existing object-level 3DGS datasets lack the appearance variation or artifact control needed for systematic attribute-level analysis. We introduce COGS, a large-scale 3DGS dataset with 15,675 artifact-filtered and appearance-rich objects across 40 categories. Built on COGS, we establish COGS-Bench for object classification and attribute-usage diagnosis, complemented by external validation. Our benchmark shows that Gaussian attributes are not uniformly beneficial: selected subsets can outperform the full attribute set, and the effects of appearance, opacity, and covariance-related attribute combinations vary substantially across architectures. We further study this finding with HALO, a reference model that preserves attribute-specific evidence before hierarchical aggregation. Experiments on COGS-Bench and external 3DGS datasets demonstrate that COGS supports systematic diagnosis of 3DGS attribute usage, while HALO highlights the value of role-preserving attribute organization. Our dataset is available at this https URL.

---


### 230. [Sparse Autoencoders as Implicit Diversification Regularisers for Cross-Sectional Cryptocurrency Returns](https://arxiv.org/abs/2610.39205)

**<font color=#1a73e8>作者：</font>** Weijia Han, Lisha Qu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Factor models are central to asset pricing and portfolio construction, but neural factors are often difficult to interpret, and their effect on portfolio risk is unclear. A sparse autoencoder (SAE) may address both concerns by describing daily returns across many assets with only a few active features. We ask whether this sparse representation produces stable financial factors and better-diversified portfolios. We study cryptocurrency returns, use equities as a secondary test, and compare the SAE with common benchmarks in a time-ordered evaluation. We find consistently lower volatility in SAE portfolios and link this result to lower correlations among the selected assets. However, the SAE does not outperform a simple contrarian strategy on risk-adjusted return, and its factor identities are not stable across training runs. Our contribution is to show that sparse coding can support portfolio diversification, while clearly separating this risk effect from claims about alpha or stable factor identities.

---


### 231. [Where Position Matters: Profiling-Guided Layer-Wise RoPE Allocation in Transformers](https://arxiv.org/abs/2610.39223)

**<font color=#1a73e8>作者：</font>** Zhiwei Liu, Boao Kong, Bing Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rotary Position Embedding (RoPE) typically uses uniform coverage across Transformer layers despite heterogeneous positional requirements. Phase-off interventions reveal non-uniform, model-specific rotary-phase dependence, while coverage interventions relate it to coverage-upgrade benefits. We propose profiling-guided layer-wise RoPE allocation, assigning high/low coverage under a fixed budget using early coverage-benefit profiles. The framework supports fixed-width query/key representations and physical rotary-dimension allocation in Multi-head Latent Attention (MLA). Normalized-depth mapping transfers profiles within model families, enabling small-model measurements to guide larger-model allocations before pretraining. A brief analysis relates selection and transfer to score calibration and inter-layer interactions. From-scratch experiments demonstrate validation-loss improvements over available budget-matched baselines, while analytical resource accounting identifies favorable quality--storage--compute trade-offs for physical MLA. These results connect positional demand to transferable, efficient architecture design.

---


### 232. [Seeing and Imagining as One: Unified Video Generation and 4D Perception for Embodied World Modeling](https://arxiv.org/abs/2610.39232)

**<font color=#1a73e8>作者：</font>** Haitang Feng, Zhuoman Liu, Zhennan Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Embodied world models should not only imagine plausible futures, but also perceive the geometric, semantic, and motion structure of the evolving world. We present GenSight, a unified embodied world model that brings future video generation and dense perception into a single pretrained video diffusion transformer. GenSight uses a unified spatiotemporal representation for video, depth, embodiment segmentation, and first-frame-relative 2D flow. Built on a shared DiT backbone, GenSight uses lightweight task modulation to predict all modalities within the same architecture. All tasks are jointly optimized within a unified velocity prediction space. At inference, GenSight supports two complementary modes: multi-step future video generation with aligned dense predictions and single-step dense perception from an observed video. By unifying modality representation, model architecture, and prediction space, GenSight avoids separate modality-specific pipelines and couples appearance, geometry, semantics, and motion in a shared representation. It promotes cross-modal consistency and allows dense perception to benefit from the spatiotemporal priors learned through video generation. Trained on embodied manipulation data spanning multiple robot embodiments and human-hand interactions, GenSight demonstrates strong performance in both video generation and dense 4D perception, highlighting the effectiveness of unifying seeing and imagining for embodied world modeling.

---


### 233. [Efficient Covariance-Aware Vicinal Latent Diffusion for Continuous Conditional Image Generation](https://arxiv.org/abs/2610.39277)

**<font color=#1a73e8>作者：</font>** Xin Ding, Shuo Huang, Zhenglong Ding 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continuous Conditional Generative Modeling (CCGM) aims to synthesize high-dimensional data conditioned on continuously valued scalar labels. However, existing continuous diffusion models face severe data sparsity under imbalanced and long-tailed label distributions, which can lead to visual artifacts and condition inconsistency. Moreover, inference-time classifier-free guidance and dense pixel-space integration introduce substantial sampling overhead, limiting practical deployment. To address these challenges, we propose CAViLD, an efficient latent diffusion framework for continuous conditional generation. CAViLD first constructs a purified condition-aware latent space through density-adaptive vicinal learning, auxiliary semantic regularization, and NIQE-guided negative data augmentation. It then internalizes the conditional guidance direction through an EMA teacher, enabling single-branch conditional inference, and introduces covariance-aware progressive distillation for label-dependent probability-flow ODEs, supporting sampling down to four NFEs. Experiments on RC-49, UTKFace, and Steering Angle demonstrate a favorable trade-off among generation fidelity, continuous condition consistency, and sampling efficiency.

---


### 234. [WorldFlow: Joint Video and 3D Motion Prediction via Large-Scale Pretraining](https://arxiv.org/abs/2610.39278)

**<font color=#1a73e8>作者：</font>** Yuhao Lu, Jiongxu Chen, Hexiang Wei 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Predicting future physical states stands as a central challenge in embodied intelligence. Existing video world models leave 3D dynamics implicit, action-based formulations remain tied to specific robot configurations, and 3D motion prediction models use flow-only supervision, providing a limited learning signal for physical dynamics. To circumvent these limitations, we introduce \method{}, a generative world model that jointly predicts future video and query-based 3D trajectories. By parameterizing 3D motion as continuous displacement tokens aligned with the video grid, a unified Mixture-of-Transformers (MoT) backbone jointly denoises both modalities under a rectified-flow objective. This formulation couples explicit geometric dynamics with visual evolution, effectively unlocking the physical commonsense embedded within pretrained video models. To empirically scale and validate this unified architecture, we train \method{} on a heterogeneous mixture of 1.44 million object-level samples spanning simulated and real-world domains. We further introduce WorldFlowBench, comprising 1,678 evaluation samples from 11 data sources across simulated and real-world interactions, including spatial reasoning tasks. Across all three evaluation sets, WorldFlow achieves the lowest average displacement error (ADE) and final displacement error (FDE) among the evaluated learning-based methods. Notably, on the challenging SpatialCog set, WorldFlow achieves an ADE of 0.060 m, a 54.2\% reduction compared with the strongest external baseline. It also reduces ADE and FDE by 55.9\% and 68.5\%, respectively, compared with its flow-only variant. Project page: this https URL.

---


### 235. [PriorMaskMap: Robust Online Vectorized Map Construction with Biased Priors](https://arxiv.org/abs/2610.39283)

**<font color=#1a73e8>作者：</font>** Haoming Xu, Wei Li, Yu Hu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Online vectorized map construction provides autonomous vehicles with essential, real-time semantic and geometric scene understanding. While leveraging prior maps presents an opportunity to improve accuracy, they are often biased due to outdated information or temporary road changes. Existing methods, which typically treat priors as fully reliable or only consider limited noise patterns, suffer severe performance degradation when these priors are imperfect. To address this, we propose PriorMaskMap, a robust framework for prior-guided vectorized map construction. Its first innovation is a Prior-Aware Confidence Estimator (PACE) that evaluates the input rasterized map against current visual observations. It assigns confidence scores to regions classified as reliable, erroneous, or blank, creating a foundational mask that guides two subsequent branches. In one branch, the Dual-Prior Query Generator (DPQG) selectively filters and embeds both rasterized and vectorized priors to initialize informative queries from trustworthy map structures. In the other, the Confidence-Guided Prior Fusion (CGPF) module spatially propagates and refines the mask, using the refined version to govern the fusion of BEV features with the prior map, thereby providing rich contextual representations for the map decoder. Evaluation on the nuScenes dataset shows that PriorMaskMap achieves superior mapping precision over existing approaches and exhibits marked robustness when provided with priors containing apparent errors. Our code is released at this https URL.

---


### 236. [Strongly Adaptive Online Learning Achieves Uniform Discounted Regret](https://arxiv.org/abs/2610.39292)

**<font color=#1a73e8>作者：</font>** Sifan Yang, Wenhao Yang, Lijun Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discounted regret measures the performance of an online learner by assigning exponentially decaying weights to past losses, reflecting the greater importance of recent losses in non-stationary online learning. While previous work obtains uniform discounted regret bounds over a continuous range of discount factors using a specialized meta-algorithm, its results are limited to convex functions. In this paper, we demonstrate that strongly adaptive regret bounds can directly imply uniform discounted regret guarantees for convex, strongly convex, and exp-concave loss functions. Our key observation is that discounted regret against a fixed comparator admits an exact decomposition into a convex combination of interval regrets. For convex functions, this reduction yields an $O(\sqrt{\log T/(1-\lambda)})$ discounted regret bound for all discount factors $\lambda\in(0,1)$, matching the previous rate over a broader range of discount factors. For strongly convex and exp-concave functions, we provide regret bounds of $O\left(\log T\left(1+\log\frac{1}{1-\lambda}\right)\right)$.

---


### 237. [Multi-Solution Inverse Design of Pixelated Patch Antennas Using an Autoregressive Transformer](https://arxiv.org/abs/2610.39300)

**<font color=#1a73e8>作者：</font>** Young-Mok Yun, Seung-Won Shin, Jaeyong Chung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep-learning-based inverse design has emerged as a promising framework for pixelated patch antenna synthesis by enabling broader exploration of discrete geometry spaces and reducing design time compared with conventional template-based methods. Existing methods, including surrogate-assisted metaheuristic optimization, tandem inverse networks, and diffusion models, have advanced the field but still face practical limitations. Metaheuristic methods such as binary particle swarm optimization (BPSO) are sensitive to initialization and search hyperparameters and are often time-consuming, tandem networks have difficulty capturing the one-to-many nature of inverse antenna design, and diffusion models may require excessive complexity and data for moderate-scale binary layout synthesis. In this paper, an autoregressive (AR) transformer is presented for the inverse design of 10 x 10 pixelated patch antennas. Its sequential discrete generation process enables the synthesis of multiple feasible structures for a given target response. The pretrained model is further fine-tuned for dual-band design using step-shaped target responses with sharp spectral transitions, allowing intuitive band specification without manually constructing detailed S11 curves. Compared with BPSO, our proposed method generates valid and diverse antenna candidates more efficiently. Fabricated and measured examples confirm that distinct pixelated layouts can realize the desired antenna responses, thereby demonstrating the multi-solution capability of the proposed framework.

---


### 238. [Learning to Bound: Monotonic, Calibrated Neural Upper Bounds for MPE Inference](https://arxiv.org/abs/2610.39305)

**<font color=#1a73e8>作者：</font>** Akshay Vyas, Hailiang Dong, Shivvrat Arya 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Probabilistic graphical models (PGMs) compactly encode structured joint distributions, but Most Probable Explanation (MPE), which finds the highest-probability assignment to unobserved variables, remains computationally intractable in large, densely structured models. Anytime systematic search, such as branch-and-bound (B&B), is a popular approach, but its efficiency depends on tight admissible upper bounds that are often prohibitively expensive to compute using classical methods like Mini-Bucket Elimination (MBE). We introduce Learning to Bound (L2B), a data-driven framework that amortizes bound computation cost by training a neural predictor. L2B targets two key properties required for effective search bounds: admissibility, which is achieved via statistical calibration techniques, and progressive tightening as evidence accumulates, which is enforced through structural architectural constraints that ensure monotonicity by construction. Across challenging benchmarks, L2B delivers tighter, monotonic bounds at orders-of-magnitude lower cost on every PGM family, and yields measurable improvements when integrated with branch-and-bound on high-treewidth instances.

---


### 239. [Unlimited OCR Works 2](https://arxiv.org/abs/2610.39308)

**<font color=#1a73e8>作者：</font>** Shu Wei, Jingjing Wu, Qunyi Xie 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Unlimited OCR ushers the era of long-horizon parsing, substantially mitigating the growth of working memory as document lengthens. However, as document length scales to hundreds of pages, the visual context grows substantially, sharply increasing the computational cost of each decoding step and limiting the scalability of ultra-long document parsing. Inspired by human book transcription via localized focus without re-scanning preceding pages, we introduce Unlimited OCR 2, a document parsing model that looks only at what it transcribes. Building on Unlimited OCR, we upgrade all the decoder attention modules to Sparse Reference Sliding Window Attention (SR-SWA), bounding active reference tokens to a fixed capacity and thus sustaining constant computational costs across arbitrarily long documents. By combining SR-SWA with Unlimited-Horizon Decoding Paradigm, Unlimited OCR 2 enables document parsing over virtually unlimited lengths without prohibitive memory overhead. At the hundred-page scale, Unlimited OCR 2 achieves 7.0$\times$ and 5.6$\times$ per-step speedups over Full Attention and R-SWA, respectively. Furthermore, it delivers state-of-the-art end-to-end performance on both MPDocBench and MarathonDocBench, our newly proposed benchmark targeting hundred-page document parsing. Ultimately, the capacity for uninterrupted, one-shot document parsing signifies a fundamental paradigm shift into the OCR 3.0 era.

---


### 240. [MemoryFusion: Cross-Temporal Memory Learning for Multimodal Video Fusion](https://arxiv.org/abs/2610.39322)

**<font color=#1a73e8>作者：</font>** Meiqi Gong, Hao Zhang, Jiayi Ma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal videos contain rich temporal cues that can facilitate faithful fusion. However, existing video fusion methods mainly rely on short-range temporal interactions, leaving valuable long-term information underexplored. Moreover, inconsistent fusion representations can cause flickering artifacts, undermining temporal coherence. To address these coupled challenges, we propose MemoryFusion, a two-stage framework integrating cross-temporal memory learning with progressive temporal refinement. Considering the complementary roles of adjacent and distant frames, the first stage combines a Short-Term Memory Bank for local temporal guidance with a Long-Term Memory Bank that preserves reliable historical information through a fusion-oriented update strategy. To mitigate temporal fluctuations, a Temporal Smoothing Module leverages soft motion cues for coarse background stabilization. Building upon the resulting fusion prior, The second stage further employs a lightweight 3D residual Temporal Refinement Module to correct remaining temporal inconsistencies while enhancing structural details. Extensive experiments demonstrate that MemoryFusion achieves superior fusion quality and temporal consistency over existing frame-based and video-based fusion methods. The source code is publicly available at this https URL.

---


### 241. [Class-aware Latent Attention Replay (CLAR): Class Incremental Hazard Diagnosis for Resilient AI in the Manufacturing Industrial Internet](https://arxiv.org/abs/2610.39323)

**<font color=#1a73e8>作者：</font>** Avranshu Mahanty, Ran Jin, Yingyan Zeng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Artificial Intelligence (AI) systems provide critical computation services in the Manufacturing Industrial Internet (MII), and their resilience depends on timely diagnosis of hazards across the data, AI pipeline, and cyber-physical layers. During operation, new hazard types keep emerging with only a few samples each, hazards co-occur, and the diagnosis model runs on memory-constrained computation nodes. Replay-based class-incremental learning (CIL) can learn new hazard classes while revisiting a small memory of past samples, but existing methods assume single-label, balanced streams, store high-dimensional raw samples, and select them independently of the classifier. We propose Class-aware Latent Attention Replay (CLAR), which combines a dual buffer that stores mostly compact latent representations with a few raw samples, an Attention Leverage Score (ALS) that upper-bounds the classifier logit and guides class-balanced reservoir sampling, and an exponential-moving-average teacher that slows latent-space drift. For an idealized buffer model, we prove that the buffer is class-balanced and follows an ALS-weighted class distribution, and that below a critical per-class capacity, ALS-guided replay has a lower replay-gradient error than class-balanced uniform replay. In the case study, On hazard diagnosis data from an MII testbed, CLAR achieves the highest mean average weighted F1 score among the evaluated replay methods with the same buffer size

---


### 242. [Can Image Agents Complete Visual Commissions? A Benchmark and Modular Framework](https://arxiv.org/abs/2610.39330)

**<font color=#1a73e8>作者：</font>** Tong Li, Lishuai Gao, Qi Zeng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual commissions require image agents to integrate heterogeneous source materials, preserve requirements across dependent stages, and produce coordinated deliverables. Existing evaluations examine specific capabilities and execution settings, leaving end-to-end commission completion less understood. We introduce Visual Commission Bench (VCB), comprising 600 tasks across 12 categories and three complementary tiers, from capability-focused tasks to complete commissions. VCB uses 5,039 requirement checks and separate visual quality ratings to assess content correctness, visual realization, constraint preservation, and delivery completeness without prescribing an internal workflow. We present V-Protocol, a reference agent that dynamically composes reusable task, cognitive, and expression modules at inference time. Task modules organize delivery, cognitive modules derive content, and expression modules guide visual realization. The modules exchange structured intermediate artifacts, while a shared execution harness tracks artifact revisions and dependencies, manages tool execution, and checks completion. With the same controller and image generator as the agent baselines, V-Protocol achieves 69.0\% strict task success on VCB, compared with 42.0\% for SCOPE. On Mind-Bench, strict accuracy increases from 39.2\% to 45.4\%.

---


### 243. [MulClip: A table-free activation function with monotonic and folding regimes for reservoir computing on microcontrollers](https://arxiv.org/abs/2610.39343)

**<font color=#1a73e8>作者：</font>** Guren Matsumura, Masato Takemoto, Shinzo Koyama  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This letter proposes MulClip, a lightweight activation function for reservoir computing (RC) on microcontrollers (MCUs). In a ring reservoir, a representative sparse RC topology, multiply-accumulate operations are few, and evaluating tanh accounted for 75% of the state-update time on a Cortex-M4. MulClip introduces curvature into the response using only comparison, absolute value, multiplication, and subtraction, and places its clipping threshold not at the extremum but at the point where the response returns to zero after passing the extremum. As a result, a single function has both a monotonic regime and a nonmonotonic folding regime that increases the expressiveness of a single unit. Which regime is used is determined by the usual hyperparameter search, e.g., over the input scale, so no task-specific threshold tuning is required. The state-update time measured on hardware was 0.34 times that of tanh and shorter than that of any of the 11 evaluated tanh approximations. In PC-based evaluation, third-order MulClip achieved a 22% lower NMSE than tanh on NARMA-20, where the pre-activations remained in the monotonic regime, and on 8-bit parity it raised the accuracy from 0.76-0.78 for the monotonic-clip variant without folding to 0.97-0.98. For these two tasks, on-device inference yielded nearly the same values as on the PC.

---


### 244. [PicturePerfect: Diffusion-based Same-identity Facial Replacement](https://arxiv.org/abs/2610.39344)

**<font color=#1a73e8>作者：</font>** Manik Dhingra, Yashesh Savani, Mahesh Reddy 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the growing success of diffusion models in computer vision, we explore their potential for same-identity facial replacement in photographs. Specifically, we propose a diffusion-based method, built on top of a pre-trained text-to-image model, that takes as input a portrait image of a person and a second reference image of the same individual, potentially captured under different conditions. The goal is to seamlessly replace the input face with the reference face, while keeping the background intact. Surprisingly, despite the clear real-world utility of this task, no recently published work has directly addressed face replacement in this specific setting. To support this goal, we construct a large dataset of image pairs depicting the same person under varying facial expressions and poses. Experimental results demonstrate that our approach produces more realistic and identity-consistent results than existing face reenactment models.

---


### 245. [Measuring Duplication, Leakage, and Rendering Dependence in Malware-as-Image Benchmarks](https://arxiv.org/abs/2610.39351)

**<font color=#1a73e8>作者：</font>** Stefan Larson, Kevin Leach  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Classifying malware binaries rendered as images is a popular approach to malware family identification, and papers on the standard benchmarks for this task report accuracies of 97-99%. In this paper we audit ten of these benchmarks for near-duplicate images and test-train leakage, and retrain standard classifiers under naive and content-aware splits. Deduplicating by file hash, which is the standard practice, does not prevent leakage, because distinct binaries render to identical images. Deduplicating on image content reduces top-1 accuracy by up to 8 points and macro-F1 by up to 15 points on the released benchmarks we find leaky. The rendering step also adds duplication, since byteplots of the same binaries contain 19.7% near-duplicates where static feature vectors contain 2.2%, and changing the width at which bytes are wrapped into rows reduces accuracy by 20 to 33 points, although no byte changes. We recommend that content-level duplication and a non-image baseline be reported alongside accuracy.

---


### 246. [CoToan: Executable Rules and a Representation Contract for Reproducible Game AI Evaluation](https://arxiv.org/abs/2610.39353)

**<font color=#1a73e8>作者：</font>** Ha-Thanh Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Game AI results are comparable only when different implementations expose the same decision problem. Yet seemingly minor representation choices can silently change that problem by altering action probabilities or collapsing states with different outcomes. We study this issue through CoToan, an executable specification and representation contract for Vietnamese Mathematical Chess connecting the Game Description Language (GDL) with OpenSpiel. The game provides a useful case because a single capture may have multiple arithmetic justifications, while outcomes can depend on scoring rules and a finite playing horizon. CoToan therefore represents actions by their state transitions rather than by arithmetic witnesses, and treats time and victory configuration as part of task identity. Cross-representation tests show agreement in legal actions, successor states, and terminal outcomes across hundreds of sampled and constructed positions, complemented by exhaustive checks of all 32 operator masks and 512 opposing-material subsets. Controlled diagnostics further show that uniform witness-level sampling alters endpoint-action probabilities, while omitting remaining time or victory settings can merge states with different terminal behavior. These results show that action semantics, time, and victory configuration are not merely implementation details. They are part of the experimental task itself and must be represented explicitly for reproducible game AI.

---


### 247. [Semantic Mismapping in Generalized Category Discovery: Evaluation and Mitigation](https://arxiv.org/abs/2610.39356)

**<font color=#1a73e8>作者：</font>** Zitai Wang, Qianqian Xu, Cong Hua 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generalized Category Discovery (GCD) aims to perform old-category recognition and novel-category discovery in the same unlabeled set. Early methods address both objectives through clustering and evaluate the exchangeable predicted indices with global Hungarian (GH) matching. Recent methods adopt trainable parametric heads, using supervision for old-category recognition and discovery-oriented objectives for new categories. In this way, the output space becomes partially exchangeable: old indices are semantically anchored, while new indices remain exchangeable. However, these methods still apply global matching, which can reassign anchored old indices to other categories and hide some prediction errors. Empirically, we are surprised to observe that this reassignment can induce an overestimation of new-category accuracy by up to 25.63 points. We term this phenomenon semantic mismapping and further derive a permutation-cycle condition that characterizes when semantic mismapping can increase the global matching score. To fix this issue, we propose Semantics-Preserving Evaluation (SPE), which preserves the supervised semantics of old indices and restricts Hungarian matching to the new region. Furthermore, we propose Mismapping-Mitigating Optimization (MMO) to alleviate the prediction errors that can give rise to semantic mismapping, combining a region-balance loss (RBL) for old/new routing with a novel-diversity loss (NDL) that encourages orthogonality among new prototypes. Theoretically, we show that minimizing the two losses can tighten an upper bound on spurious accuracy gains from semantic mismapping, with controllable residual terms. Empirical results under both GH and SPE demonstrate the effectiveness of our proposed method.

---


### 248. [More Is Better? Exploring Latent Correspondence in Federated Hypergraph Learning](https://arxiv.org/abs/2610.39362)

**<font color=#1a73e8>作者：</font>** Bo Yan, Siming Zhang, Siqi Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated hypergraph learning with latent cross-client hyperedge correspondence poses fundamental identifiability and computational challenges, as the same local release can correspond to multiple global hypergraph structures. We characterize the tractability of recovering these latent correspondences, showing tractable pairwise assignment but generally intractable multi-client hyperedge matching. Building on this characterization, we derive a cross-entropy decomposition that reveals when local prediction can outperform predictors fitted with additional cross-client information. Motivated by this principle, we introduce Federated Adaptive Spectral Training with Representation Alignment (FedASTRA), which learns correspondence-invariant diffusion representations through adaptive heat diffusion and masked latent prediction while communicating model parameters only. We establish its asymptotic optimality with respect to the permitted local information and prove global population-risk convergence under explicit conditions on recovery, representation, and update alignment. Experiments on eight real-world datasets demonstrate the effectiveness of FedASTRA against identifier-free federated graph and hypergraph methods. On ogbn-papers100M, FedASTRA reaches the performance-communication Pareto frontier, achieving 50.07 Accuracy and 29.73 Macro-F1 while communicating only 59.60 MiB per round.

---


### 249. [Lookover: Scaffolding Student Participation in Social Annotation](https://arxiv.org/abs/2610.39363)

**<font color=#1a73e8>作者：</font>** Yubo Zhou, Xinyi Xu, Zesen Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Social annotation platforms such as Perusall and Hypothesis are widely used to support student engagement with course readings, often through required commenting. Yet visible participation does not necessarily produce sustained or substantive peer exchange. Analyzing six weeks of Perusall activity from a graduate course (2,873 comments), we found that participation was often fragmented: 53.5% of comments received no reply, 38.3% were posted within the final 12 hours before the deadline, and over one-third of a double-coded sample went no further than repeating or agreeing with the reading or a peer. Interviews pointed to two linked difficulties: locating a discussion worth entering and contributing something that meaningfully advances it. We present Lookover, an AI-assisted annotation system that scaffolds both stages without writing for students. Discussion Overview helps students identify active themes and relevant threads, while Spark Thinking poses questions that encourage them to move beyond reaction and restatement toward questioning, extending, and substantively responding to peers. A preliminary study with five participants found Discussion Overview valuable for those who noticed it, while the usefulness of Spark Thinking depended on how much a participant already knew about the topic.

---


### 250. [DualGuard: Comprehensive and Efficient Memory Safety across Sequential and Speculative Execution](https://arxiv.org/abs/2610.39374)

**<font color=#1a73e8>作者：</font>** Sixuan Dang, Quan Zhou, Kaiming Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Although decades of research have yielded sophisticated mechanisms for enforcing memory safety, speculative execution can subvert these protections through transient memory operations. Conversely, defenses designed specifically for speculative safety, such as Speculative Load Hardening (SLH), cannot enforce memory safety during non-speculative execution. A naive combination of defenses from both domains raises two fundamental challenges: (1) which combination of otherwise fragmented defenses can ensure dual memory safety under speculative and non-speculative executions? (2) whether such combinations introduce redundant protections that incur unnecessary performance overhead?
We present DualGuard, a unified framework for dual memory protection under non-speculative and speculative executions. DualGuard systematically analyzes memory behaviors, classifying them into four categories, and further identifies the minimal composition requirements for dual memory safety, which allow us to strategically combine existing mitigations and design new ones to avoid redundant or excessive protections. We implement DualGuard through a combination of static analysis and runtime enforcement within the LLVM infrastructure. Our evaluation demonstrates that DualGuard reduces overhead by 3%-72% compared to naive compositions of fragmented defenses. In some cases, it even incurs lower overhead than approaches that guarantee memory safety solely under either non-speculative or speculative execution.

---


> [!TIP]
> 当前位于：**201-250**（第 5/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-432](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
