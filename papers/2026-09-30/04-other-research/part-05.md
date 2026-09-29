# 📦 其他研究 | 2026年09月30日

> 本类共 **908** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/19 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-908](./part-19.md)

---

### 201. [What Should Federated LoRA Share? FedSAIL via Input-aware Subspace Alignment](https://arxiv.org/abs/2609.32485)

**<font color=#1a73e8>作者：</font>** Junye Du, Shuaida He, Long Feng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated low-rank adaptation (LoRA) requires identifying an update structure that is shared across heterogeneous clients. Prior work reports strong similarity among trained LoRA projection matrices across clients; however, such agreement may be largely induced by common initialization and collapses toward random overlap under independent initialization. More crucially, relying solely on parameter similarity inherently ignores the influence of local input regime. To uncover a more robust shared structure, we introduce an input-aware action matrix that weights the adapter update by the second-moment statistics of local layer inputs. Empirically, while parameter similarity vanishes, the leading right singular directions of this action matrix remain strongly aligned across clients. This shared geometry preserves task-conditioned differences and naturally varies across network depths. Motivated by these findings, we propose Federated Subspace-Guided Action-Informed Learning (FedSAIL). Instead of averaging weights, FedSAIL estimates a shared action subspace to regularize local training while preserving client-specific coefficients. Across several benchmarks, our approach consistently improves predictive performance over competing federated LoRA methods while reducing communication cost significantly.

---


### 202. [Neural Dynamics as the Composition of Quantized Units](https://arxiv.org/abs/2609.32487)

**<font color=#1a73e8>作者：</font>** Jacopo Minniti, Aravinth Kulanthaivelu, Richard Sproat  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning is commonly interpreted at two levels: the macroscopic, through aggregate trends in loss summarized by scaling laws, and the microscopic, through neurons, features, and circuits. A central challenge is understanding how these levels connect, so that we can explain how elementary computations compose and collectively shape macroscopic behavior. To this end, we study an intermediate abstraction in which training is described as the ordered acquisition of quanta: reusable computations acquired suddenly and binary-activated across examples to reduce loss. By approximating population-gradient updates, we derive quanta's acquisition dynamics. This yields an acquisition priority governed by demand, how frequently a computation is required across examples, and conditional complexity, how difficult that computation is to acquire given those already available. In a Boolean compositional task, we derive predictions for acquisition order and show how staggered discrete acquisitions can produce smooth aggregate loss and, under certain geometries of quanta composition, give rise to scaling laws. We then train a Transformer to map numerals to English number names and recover candidate quanta from its checkpoint trajectory. From these units, we construct a model that preserves much of the Transformer's behavior while exposing interpretable latent computations and acquisition dynamics consistent with the theory. Separately, the quanta structure can serve as training targets to improve transformer generalization. Together, these results suggest the quanta abstraction can provide useful computational atoms for studying a variety of macroscopic phenomena.

---


### 203. [Locally Sound, Globally Insufficient: The Local-Global Gap in Multi-Hop Reasoning](https://arxiv.org/abs/2609.32496)

**<font color=#1a73e8>作者：</font>** Bohao Chu, Hendrik Damm, Qianli Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reliable multi-hop reasoning requires more than locally supported steps: a trace can be sound at every reasoning step yet still fail to answer the question as a whole. We call this failure regime the local-global gap (LGG), in which the trace is locally sound yet globally insufficient. Local soundness requires each step to be supported by the available evidence and preceding steps, whereas global sufficiency requires the reasoning trace to align with the question and establish the submitted answer. In a human-adjudicated diagnostic of 2,598 responses across three multi-hop QA benchmarks and three models, we find that the LGG occurs in every benchmark-model combination and accounts for nearly half of globally insufficient responses overall. However, conventional faithfulness verifiers that check claims against the evidence largely miss these failures: at thresholds retaining at least 95% of reliable traces, recall for LGG cases is substantially lower than that for locally unsound traces. To address these failures, we formalize three dependencies for reliable reasoning: evidence-to-step support, question-to-trace alignment, and trace-to-answer closure. Instead of post-hoc diagnosis, we introduce E-Closure to supervise these dependencies during training, combining generation supervision on supported original and counterfactual responses with bidirectional switching constraints. Averaged over three benchmarks and three backbones, existing fine-tuning baselines improve accuracy and local soundness over the base models, but at the cost of global sufficiency. E-Closure improves both: among all fine-tuned methods, it achieves the highest average accuracy (92.8%) and trace reliability (89.0%) while yielding the lowest LGG rate (6.2%).

---


### 204. [Rondo: Unsupervised Discovery of Recurring Temporal Structure](https://arxiv.org/abs/2609.32500)

**<font color=#1a73e8>作者：</font>** Yingtian Shi, Ankith Chandra, Thomas Plötz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many real-world time series data exhibit structural properties at multiple scales, from short, recurring units to complex sequences composed of these units. Unsupervised discovery of both these components and structure enables the design of intelligent systems that help interpret temporal data, thereby limiting the amount of costly human annotations required. Existing modeling approaches typically overlook the hierarchical structure inherent to many time series, treating recurring patterns at different temporal scales as independent structures. Moreover, most assume access to the complete data sequence and treat discovery as a static process, limiting their ability to evolve as new observations arrive. We introduce Rondo, an unsupervised approach for modeling recurring hierarchical structure in continuous temporal streams. By explicitly constructing vocabularies of reusable units and their recurring compositions, Rondo captures structure shared across complex temporal patterns while refining and expanding its discoveries as the stream evolves. Evaluations on temporal sequences spanning diverse domains and data modalities show that Rondo outperforms existing unsupervised recurrence-discovery baselines, with particularly pronounced advantages in limited-data and continual-stream settings. These capabilities provide a stronger foundation for recurring-pattern discovery, scalable behavior understanding, and adaptive intelligent systems operating on long, unlabeled temporal streams.

---


### 205. [TreeRef-BFN: Equivariance-Free De Novo Molecule Generation based on 2D Topology and Internal 3D Geometry](https://arxiv.org/abs/2609.32502)

**<font color=#1a73e8>作者：</font>** Ruiqing Sun, Sen Yang, Dawei Feng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> De novo 3D molecular generation jointly models molecular size, topology, and geometry. Most methods pre-sample molecular size and generate Cartesian coordinates, limiting variable-size conditional tasks such as fragment completion and scaffold decoration while often relying on equivariant architectures. Internal-coordinate methods avoid rigid-body redundancy but typically require a known molecular graph or autoregressive construction, which may accumulate errors. We propose TreeRef, a tree-based molecular representation that assigns molecular topology and topology-dependent local 3D geometry to a naturally variable-size tree. RingRef nodes encode ring closures while preserving the tree structure, while Null nodes allow molecular size to emerge directly from node occupancy. Based on TreeRef, we develop TreeRef-BFN, a Bayesian Flow Network with a standard Transformer backbone that globally couples these locally defined variables and jointly generates discrete molecular variables and continuous local geometry. A single pretrained TreeRef-BFN supports unconditional generation and variable-size structure-conditioned 3D generation through masking alone, without retraining. Empirical studies demonstrate strong chemical validity, molecular stability, and diversity, accurate local geometric distributions, fast sampling, and competitive property-conditioned generation, establishing TreeRef-BFN as an efficient and flexible framework for 3D molecular generation.

---


### 206. [Fisher Simplicity in Kolmogorov-Arnold Networks and Multilayer Perceptrons](https://arxiv.org/abs/2609.32503)

**<font color=#1a73e8>作者：</font>** Ami Tavory, Meir Feder  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Kolmogorov-Arnold Networks (KANs) are motivated in part by interpretability: their learned edge functions can be inspected, pruned, and reduced to symbolic structure. In a fixed-basis KAN, this makes a small or zero basis coefficient look like a certificate of simplicity, much as a dead rectified linear unit (ReLU) marks unused computation in a multilayer perceptron (MLP). Fisher nullity gives a precise statistical notion: a parameter direction is Fisher-simple exactly when perturbing it is invisible under the task distribution. We study when these architectural and Fisher notions agree.
For a dead ReLU unit, they agree: the closed activation region makes the associated score directions vanish. For a fixed-basis KAN, they do not. In the single-layer Gaussian case, the coefficient Fisher matrix is a basis Gram matrix under the input distribution and is independent of the fitted coefficients. In a multilayer KAN, Fisher simplicity is graph-path based: the data must reach a basis atom and its perturbation must propagate through the downstream network. We encode these two conditions in an effective edge measure and, under local dictionary independence and effective-measure nondegeneracy, show that zero effective exposure exactly identifies Fisher-null directions within an edge. Controlled diagnostics confirm that zero coefficients can preserve rank while effective path disconnections remove the predicted directions. Coefficient magnitude alone is therefore not a Fisher-based pruning criterion for KANs.

---


### 207. [GeoCR: Learning a Generalist Cloud Removal Prior from Heterogeneous Observations](https://arxiv.org/abs/2609.32510)

**<font color=#1a73e8>作者：</font>** Jeonghyeok Do, Munchurl Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cloud removal methods are typically specialized to individual datasets and input configurations, limiting reuse across sensors, spectral bands, and observation settings. We introduce GeoCR, a generalist model that unifies RGB-only-based CR and multispectral-based CR from single- or multi-temporal cloudy observations, with optional SAR guidance, within a single network. To accommodate different spectral and sensing domains, compact input and output stems extend a pretrained RGB autoencoder while keeping its encoder and decoder trunks frozen. This shared latent interface enables a single flow transformer to jointly model clean RGB and non-RGB latents, conditioned on separate cloudy-observation streams and optional SAR tokens. Through joint pretraining on the training splits of ten datasets comprising 883,331 cloud-free target images, GeoCR learns a shared cloud removal prior across these heterogeneous configurations. The same pretrained checkpoint supports direct inference without dataset-specific fine-tuning and efficient adaptation through low-rank adaptation (LoRA). We evaluate GeoCR against general image restoration and cloud removal methods on test splits of the contributing datasets under full-band and RGB-only settings. GeoCR achieves the best FID and DISTS on full-band SEN12MS-CR and Sen2_MTC_New and RGB-only CUHK-CR2, outperforming existing models and demonstrating the effectiveness of a reusable generative model across diverse settings.

---


### 208. [What Do Latent Predictive Vehicle Representations Retain? Measuring State, Geometry, and Local Response](https://arxiv.org/abs/2609.32512)

**<font color=#1a73e8>作者：</font>** Enzo Nicolás Spotorno, Josafat Leal Filho, Antônio Augusto Fröhlich  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Models of vehicle dynamics learned from logged states and commands complement physics-based models, and latent world models, which predict in a learned representation, are used to plan and train controllers in other domains. Vehicle controllers are usually specified in physical terms: costs, limits, and references depend on position, yaw angle, speed, and yaw rate, and the optimizer compares or differentiates predicted outcomes across nearby commands. A latent model placed in such a controller must therefore let these quantities be recovered and must change its predictions with commands as the vehicle does, and prediction error on its own latent targets measures neither. We contribute a measurement protocol for action-conditioned latent predictors with a physical readout that separately tests retention, physical-neighborhood organization, forecasting, and local response to command perturbations, using an untrained-encoder reference and three matched response paths that locate errors in the representation or the predictor. In a case study of a temporal joint-embedding predictive model trained on signals logged in IPG CarMaker, the representations retain the measured planar outputs, though an untrained encoder of the same architecture retains them slightly better; future-command input improves one-second forecasts with retention nearly unchanged; and responses to small command pulses diverge from the simulator already in latent coordinates, raising regret when choosing among nearby commands in all comparisons. Updating the predictor on responses corrects them locally at a cost in forecast accuracy. Measuring retention, forecasting, and local response separately is thus what qualifies a predictive latent as a candidate model for control, and the protocol provides the basis for its closed-loop evaluation.

---


### 209. [Cross-Domain Few-Shot Writer Adaptation for Real-World Handwritten Mathematical Expression Recognition](https://arxiv.org/abs/2609.32513)

**<font color=#1a73e8>作者：</font>** Paulo Grane Gabriel Silva, Lorenz Bernard Marqueses, Joel Ilao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Handwritten mathematical expression recognition (HMER) refers to the task of recognizing and converting handwritten mathematics into a parsable markup language, usually LaTeX. No current state-of-the-art-competitive system adjusts to the way a specific person writes, and the domain gap between training images (usually digital or perfectly binarized) and images physically taken with a camera used in inference has received fairly little attention for this specific problem. We characterize this domain gap through fragmentation and stroke-width analyses of the images as well as introduce a writer-adaptive fine-tuning pipeline to MFH-CoMER in an attempt to address it. We further introduce sample author-specific datasets, consisting of five handwriting category subsets from two authors, and evaluate using a McNemar's test and permutation tests adapted to limited data. Results suggest an increase in expression recognition rate and a decrease in CER for digital handwriting but more varied results for physical handwriting, with the model struggling for handwriting articles that the base model can already evaluate well. Nonetheless, adapted models were found to have improved results for four out of five subsets. Statistical testing results suggest a consistency in improvement for two of the tested author-specific subsets. Our results point towards the potential feasibility of writer adaptation for the HMER task.

---


### 210. [LocalProp: Neuro-Localized Memory-Efficient Backpropagation](https://arxiv.org/abs/2609.32517)

**<font color=#1a73e8>作者：</font>** Diana-Nicoleta Grigore, Iuliana Georgescu, Radu Tudor Ionescu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The current deep learning training paradigm employs end-to-end backpropagation, regardless of the training stage, i.e. pre-training or fine-tuning. However, backpropagating through the entire model is neither biologically plausible nor memory efficient, since learning inside the brain is highly localized. Therefore, we propose LocalProp, a training procedure that locally updates the weights of a model. Our neuro-localized weight updates follow the "pre-training then fine-tuning" paradigm, where the pre-training is based on I-JEPA. After locally updating the weights, a pruning operation is performed, followed by a short final fine-tuning phase. Pruning helps by sending the learning signal from higher blocks to lower blocks. We perform experiments on several datasets, including large-scale benchmarks such as ImageNet, and empirically show that LocalProp reaches good performance at a fraction of GPU peak memory. By varying the number of jointly optimized blocks, we identify gradient-propagation span as a practical control over the accuracy-memory trade-off.

---


### 211. [Does Transolver really need a Transformer?](https://arxiv.org/abs/2609.32525)

**<font color=#1a73e8>作者：</font>** Shizheng Wen, Siddhartha Mishra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The widely used Transolver family of neural operators is based on physics-attention, which softly assigns the points of an unstructured mesh to a small number of slices, applies self-attention among the resulting tokens, and broadcasts the result back to the points. We provide a comprehensive empirical and theoretical analysis to elucidate the mechanisms which are responsible for model performance. To this end, we perform careful ablations on a challenging suite of nine 3D fluid dynamics benchmarks to find that replacing token attention with a constant linear map does not affect the accuracy. Thus, Transolver does not need a Transformer at all. However, removing the global mixing (slicing/deslicing) or doing it only once leads to performance collapse. We leverage the theory of averaging neural operators to explain and corroborate our findings by showing that just slicing/deslicing, in conjunction with pointwise MLPs, already suffices for universal approximation of continuous operators and attention is redundant in this context. Finally, we provide a novel FlashAttention-style efficient implementation of the key slicing/deslicing module of Transolver. This flashslice kernel streams slice and deslice over the points without materializing the heavy slice-weight tensor, while reproducing the best available implementation to floating point error. At the same time, it leads to very significant memory and compute savings, particularly at large slice counts.

---


### 212. [AmbiModBench: Benchmarking Gene Perturbation Prediction Beyond Shared Responses](https://arxiv.org/abs/2609.32527)

**<font color=#1a73e8>作者：</font>** Sikai Huang, Zhiwen Yang, Kai Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Predicting cellular responses to genetic perturbations helps prioritize experiments in single-cell genomics, where exhaustive measurement is infeasible. While computational models increasingly predict these responses, three evaluation deficiencies obscure what their scores demonstrate. First, absolute metrics cannot separate target-specific predictions from a shared background response. Second, common metrics remain high under gene shuffling, so gene-level accuracy is never verified. Third, a score at one training size says nothing about coverage, which depends on representation-space proximity and response-constraining power. We propose AmbiModBench, a specificity-aware, gene-resolved and coverage-aware benchmark. It pairs every score with a training-mean reference fitted on the same split, screens each readout by gene-coordinate permutation, and links embedding distance to response variation. Across K562, RPE1 and Norman, strong absolute scores largely reflect shared background rather than target-specific learning. Widely used readouts track response magnitude distributions rather than the affected genes. Detectable gain follows representation-space coverage rather than training-set size. Nonetheless, on RPE1 the protocol yields a reproducible target-specific gain across five additional splits and three gene selections, which absolute scores alone cannot distinguish from shared background.

---


### 213. [SetOPD: From Few Visual Exemplars to Multimodal Candidate Sets for Remote-Sensing Open-Prompt Detection](https://arxiv.org/abs/2609.32529)

**<font color=#1a73e8>作者：</font>** Jinlong Hu, Yi Zhang, Zhiqi Xia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-prompt detectors allow users to specify targets with text, visual exemplars, or both. We argue that existing designs underuse the visual modality in two ways. First, multiple exemplars are commonly compressed into a single class-level embedding. This textualizes visual prompting: the resulting vector plays the role of another class name, is often aligned to or injected into the text pathway, and may be suboptimal when only a few heterogeneous exemplars are available. Second, existing methods interact primarily in prompt or representation space, before modality-specific detection states are formed. We address both issues from a set perspective: \setopd preserves modality-specific decoding states from a shared prompt-conditioned initialization and performs explicit multimodal collaboration at the candidate-state level. For the first issue, we introduce \br prompting, which reads every boxed exemplar in its full scene context and decomposes the pooled support evidence into a Base anchor and a learned Residual correction; the resulting prompt has fixed capacity regardless of the number of examples and drives its own visual detection pathway. For the second, we recast text--visual collaboration from representation-level fusion into a candidate-set modeling problem. Paired-Query Arbitration (\pqa) then performs explicit cross-modal state arbitration only after modality-specific candidate states have been formed. The two readers share query initialization so their candidates are paired by index; a learned gate arbitrates within each pair, followed by a permutation-equivariant module that reasons over the fused set.

---


### 214. [Activation Flow: Manufacturing Activations for Steering](https://arxiv.org/abs/2609.32530)

**<font color=#1a73e8>作者：</font>** Hong Kiat Tan, Linh Le, David Williams-King  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Difference-in-means steering requires activations recorded while a model shows the desired behavior, which a sandbagging model withholds by deliberately underperforming. We introduce Activation Flow (ActFlow), which manufactures these activations from $k$ correct labels without fine-tuning. ActFlow sets target logits that rank each labeled item's correct answer first, and moves the logits toward them by adding one vector $x$ to all $k$ residual streams at one layer. ActFlow is a family of ordinary differential equations for $x$, one for each rule that maps the required logit change to the velocity of $x$. The smallest-norm rule lands exactly on the targets, while the others keep only the top singular directions of the Jacobian. We test ActFlow on three instruction-tuned models, each locked by a sandbagging prompt and by a password-locked LoRA. At $k=40$, ActFlow keeping five singular directions raises the mean held-out ARC-Easy accuracy over the six locked models from $0.05$ to $0.85$, against $0.88$ for fine-tuning and $0.92$ for the honest models. Furthermore, it scores higher than the smallest-norm rule in 16 of the 18 combinations of locked model and $k$, and its steering direction is nearly orthogonal to the honest difference-in-means direction. It also unlocks two LoRA locks where the honest direction fails.

---


### 215. [What Does a ProcGen Generalization Gap Measure? Action Rules, Convergence, and the Missing Random Floor](https://arxiv.org/abs/2609.32532)

**<font color=#1a73e8>作者：</font>** Abhisek Keshari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A generalization gap in reinforcement learning (return on training levels minus return on held-out levels) is usually reported without a reference point. We argue that the missing reference is a measured random floor: the return of a uniform-random policy on the same levels under the same harness. On ProcGen, the floor changes what several standard numbers mean. On identical checkpoints and levels across eight environments, switching between sampled and greedy (argmax) test-time actions moves held-out return in both directions, and greedy evaluation takes three environments to or below the floor: in miner, the sampled policy scores 4.9x the floor on held-out levels while its argmax scores below it. Raw policy entropy places seven of eight environments short of convergence, but 35-65% of that entropy is spread across actions with identical effects; after merging them, one to three remain short, and against the floor only heist has learned nothing that transfers. An audit of twelve prior ProcGen codebases finds that all eleven with held-out evaluation sample test-time actions for their policy-gradient agents, nine by default rather than explicit choice, and six report running in-loop averages rather than evaluating a fixed checkpoint. Applied to our own case study, the same checks grade down a statistically significant encoder effect and rule out a within-encoder train-vs-test CKA statistic. We recommend that every reported gap state its action rule, use a matched and seeded protocol, and report the random floor on both level sets.

---


### 216. [DepthBench: Measuring How Residual Connections Enable More Computational Depth](https://arxiv.org/abs/2609.32534)

**<font color=#1a73e8>作者：</font>** Keyu Wang, Yangyi Huang, Jiale Kang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Depth is a natural way to increase the computational capacity in Transformers, yet the contribution of deeper layers can diminish as depth grows larger. Recent approaches enhance normalization (\text{e.g.}, LayerNorm Scaling) or residual connections (\text{e.g.}, mHC, AttnRes) to enable better information flow and depth utilization. However, it remains unclear whether they truly translate increased architectural depth into effective computational depth, and whether their reported gains stem from better access to information across depth, or unaccounted-for confounding factors. In this paper, we introduce \textbf{DepthBench}, a controlled benchmark for studying computational depth across various architectures. We systematically vary the width--depth aspect ratio ($d_{\text{model}}/n_{\text{layer}}$) from shallow--wide to deep--narrow shapes, while keeping the model size and pre-training recipe fixed. Across 10 representative architectures, we find that the benefit of allocating more capacity to depth is strongly architecture-dependent. Standard Pre-LN and most of its norm- and scaling-based variants provide little benefit and can even degrade performance as models become deeper and narrower, whereas HC and Full AttnRes improve consistently even at extreme deep shapes. These gains extend beyond pre-training loss and consistently translate into improved domain-specific performance and effective computation. Controlled layer-level analyses further show that the gains of HC and Full AttnRes are associated with more effective utilization of additional layers, revealing distinct mechanisms of computational depth across architectures. Overall, our results identify residual connection design as a key determinant of whether depth can serve as a meaningful scaling axis by enabling additional architectural depth to translate into effective computation.

---


### 217. [RIPE-MambaSpike: Resolution-Independent Spiking-State-Space Interfaces for Parameter-Efficient Event-Based Vision](https://arxiv.org/abs/2609.32537)

**<font color=#1a73e8>作者：</font>** Md Muhiminul Islam, Shoaib Ahmed Dipu, Sayeed Shafayet Chowdhury  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spiking-Mamba hybrids reach strong accuracy on event-based vision, but existing designs often require tens of millions of parameters. Much of that cost comes from how the spiking front-end is connected to the state-space backbone rather than from the hybrid architecture itself. In a representative model, a single resolution-dependent projection accounts for 33.55M of 36.25M parameters. To that end, we introduce RIPE-MambaSpike (Resolution-Independent, Parameter-Efficient), which replaces that projection with a hierarchical multi-resolution bridge of fixed channel width. Its deployed footprint is 0.870M parameters, constant at fixed time steps and widths across a 43x range of input areas. Reparameterized spiking stages, temporal decoupled modulation, and a dynamic convex-hull-bounded dual-stream membrane-potential attention preserve accuracy under this compact design. Result-wise, RIPE-MambaSpike is pareto-optimal on CIFAR10-DVS, N-Caltech101, and DailyDVS-200. Notably, on the 200-class DailyDVS-200, a scaled 8.04M configuration achieves 45.7% top-1 accuracy, the best reported spiking result on that benchmark, and outperforms prior spiking methods with 3.0-15.1x fewer parameters than dense ANNs. Overall, our findings demonstrate that competitive event-based recognition does not require resolution-dependent parameter growth. Code is available at this https URL.

---


### 218. [Interpretable Physics Informed WiFi Indoor Localization: Learning an Effective Access Point Geometry and Using It to Prune](https://arxiv.org/abs/2609.32539)

**<font color=#1a73e8>作者：</font>** Arshia Eftekhari zadeh, Rezvan Nasiri, Hadi Moradi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep learning models can achieve high accuracy for indoor localization, but their black-box nature limits interpretability and the reuse of learned information. We propose a hierarchical deep learning framework for WiFi fingerprint-based indoor localization that jointly predicts user location and learns an effective geometry of the surrounding access points (APs). Physics-informed decoders infer this geometry directly from RSSI measurements and labelled user positions, without requiring the true AP coordinates during training. The learned geometry is then used to rank and prune APs.
On the UJIIndoorLoc dataset, the proposed chained model achieves a mean 3D localization error of 7.07 m, reducing error by 26% to 36% compared with baseline models. Previously published methods evaluated on the same official split report errors 10.6% to 31.0% higher. Pruning 35% or 50% of the APs causes only a small loss in localization accuracy. The inferred geometry also enables Fisher-information-based AP ranking even when fingerprint databases do not contain surveyed AP coordinates. Experiments on the Tampere/TUT and UTSIndoorLoc datasets show that geometry-guided AP selection performs comparably to selectors built directly from labelled data. These results show that physics-informed interpretability can improve indoor localization while also supporting effective feature selection.

---


### 219. [Feature Space Guidance for Breast Cancer Classification in DCE-MRI](https://arxiv.org/abs/2609.32555)

**<font color=#1a73e8>作者：</font>** Benjamin Hamm, Yannick Kirchhoff, Maximilian Rokuss 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic contrast enhanced breast MRI (DCE-MRI) is a powerful clinical tool for breast cancer detection, providing high resolution anatomical detail together with rich temporal contrast information. However, high dimensional 4D inputs, small lesions, and heterogeneous acquisition protocols across clinical sites hinder robust automated classification of healthy, benign, and malignant cases. To address these challenges, we propose a framework that dynamically analyzes latent representations to adapt to protocol-specific characteristics. Spatial variability is mitigated by reducing confounding background uptake and compensating for misalignment caused by deformable soft tissue. Additionally, relationships in the latent space across phases are leveraged to select the most informative temporal features, improving robustness to protocol-specific temporal variability. Finally, task specific discriminative features are promoted through large scale supervised lesion segmentation pretraining, which substantially enhances downstream finetuning. Evaluated under leave-one-center-out validation on the ODELIA dataset and the held-out AMBL cohort, the proposed framework substantially outperforms finetuned radiology foundation models and prior methods, improving mean AUROC by nearly 8 points and balanced accuracy by 4 points over the strongest baseline. Additionally, our method achieved first place in the MICCAI ODELIA Breast MRI Challenge 2025, further demonstrating its effectiveness for robust breast cancer classification. We publicly release our codebase under this https URL.

---


### 220. [Language as an Independent Information Layer: A Conceptual Model of Communication, Cognition and Decision-Making](https://arxiv.org/abs/2609.32556)

**<font color=#1a73e8>作者：</font>** Anastasiia Alifanova, Elena Benderskaya  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Based on an analysis of the role of language in thought and communication, this article proposes a new concept for designing corporate knowledge bases. The concept integrates the probabilistic vector space of a corporate vocabulary, reflect-ing industry specifics, subject focus, terminology, and culture, with traditional ontological modeling. This combination enables the efficient extraction of knowledge from accumulated corporate documents while strictly accounting for specific business processes. Consequently, this concept bridges statistical and semantic (cause-and-effect) methodologies. Furthermore, analyzing the projec-tions of probabilistic spaces and causal relationships can help identify bottlenecks in business logic. As a dynamic system, language functions as a separate, inde-pendent layer within the overall information architecture. Introducing a dynamic component into the probabilistic space of word distribution allows it to be mod-eled as a multidimensional solution space for various problem formulations. In this context, input data defining the problem conditions serve as control parame-ters for dynamic transformations.

---


### 221. [CFCH: Coarse-Fine Collaborative Hierarchical Learning for Anterior Segment Disease Analysis](https://arxiv.org/abs/2609.32559)

**<font color=#1a73e8>作者：</font>** Peng Wang, Haohan Zou, Yanlin Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate classification of anterior segment diseases is crucial for ophthalmic screening and diagnosis. However, slit-lamp image analysis remains challenging due to substantial variability in imaging conditions and the intrinsic anatomical-disease hierarchy of ocular pathologies. Existing methods typically formulate this task as a flat multi-class classification problem, ignoring the structured dependency between anatomical regions (e.g., cornea, conjunctiva, and lens) and disease this http URL address these limitations, we propose CFCH, a Coarse-Fine Collaborative Hierarchical learning framework that explicitly models anatomical context and disease semantics through a dual-branch architecture. To enable effective cross-granularity collaboration, CFCH introduces semantic and cross-granularity attention consistency constraints, encouraging aligned yet complementary feature learning across branches. In addition, we construct AS-9K, a large-scale anterior segment dataset with 8975 images covering 12 common disease categories. To the best of our knowledge, AS-9K is the largest publicly available dataset for anterior segment image classification. Extensive experiments on two anterior segment datasets demonstrate that CFCH outperforms state-of-the-art methods. Qualitative visualizations further show more focused and lesion-relevant activation responses, validating the effectiveness of the proposed framework. Code will be available at this https URL.

---


### 222. [How to Reduce Whisper Hallucination](https://arxiv.org/abs/2609.32560)

**<font color=#1a73e8>作者：</font>** Husein Zolkepli  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Whisper is still what runs in production: one permissively licensed checkpoint, 99 languages, no per-language tuning. But it writes sentences nobody said. On 42 clips of pure room tone, whisper-large-v3 emits words on 61.9% of them and emits something on 100%. The usual response is to distil a student from Whisper pseudo-labels, filtering the hallucinations out of the corpus first, which deletes the evidence while leaving the behaviour in place: the student is fitted to the subset where the teacher was right, and inherits a failure mode absent from its own training data. The second response, adding non-speech audio so the model learns to stay quiet, already ships and works, but teaches suppression without discrimination. The checkpoint best on every non-speech arm here is also the one that recovers the fewest genuinely spoken phrases and deletes 58% of repeated speech. The teacher has to be fixed, with both halves of the signal. Our benchmark scores both at once: 11,852 clips over eight arms, 6,267 synthetic positives, 8,296 clips of real audio that made a production model fail, and FLEURS in 58 languages. We collect 40,891 hallucination phrases in 100 languages, choose a text-to-speech system by measurement, and synthesise those phrases as positives, so the model meets the same text both as something to suppress and as something to transcribe. Across 33 matched pairs of fine-tunes differing only by those positives, adding them lowers word emission on real voice-free audio in 31 pairs and raises phrase recovery in 32; among the 30 pairs that hold English accuracy it is 30 out of 30. The best checkpoint takes hallucination on silence from 61.9% to 2.4% and words over real voice-free audio from 99.9% to 47.8%, while raising phrase recovery from 69.8% to 82.7%. The benchmark, lexicon and synthetic corpus are released at this https URL

---


### 223. [Compositional Objectives: Learning Structure in Structure](https://arxiv.org/abs/2609.32566)

**<font color=#1a73e8>作者：</font>** Pranavchandra Vivekananda, Sumukh Bettadapura, Ajan Subramanian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Intelligence is defined in many ways. One of these definitions defines intelligence as the pursuit of learnable novelty. However, learnable novelty can be meaningless without the ability to compose the learned structures to take action and achieve goals. Learnable novelty builds on epiplexity, which is a way to measure learnable structure in data through a bounded observer. In this paper, we investigate a closed-form spectral approximation to compute epiplexity. We use a fixed-trace constraint and find that the epiplexity objective prefers a more uniform distribution of spectral mass rather than concentrating it in a small number of directions. However, a representation may spread information across many directions without organizing that information into features useful for a particular task. To address this gap, we propose a compositional objective whose observer measures the relationships between the parts and interactions of an image. We compare it with the original spectral objective given only the masked parts. In our ImageNet training runs, the spectral objective with masked parts produces an almost maximally spread representation while achieving the strongest frozen-feature classification performance on most evaluations, more than doubling the linear-probe accuracy of the whole-image baseline. Across multiple image benchmarks, changing what the observer sees matters more than adding relation and interaction tokens. At the same time, our prediction-oriented compositional objective produces substantially better held-out observer prediction but relatively weaker classification, revealing that spectral diversity, predictability, and downstream utility are distinct properties. These results suggest that the usefulness of spectral spreading depends not only on how much structure is preserved, but on which relationships the observer makes available to the objective.

---


### 224. [CUE-Mem: Benchmarking Long-Term User Memory via Implicit Cues in Multimodal Conversations](https://arxiv.org/abs/2609.32574)

**<font color=#1a73e8>作者：</font>** Yulin Hu, Yanyan Zhao, Zimo Long 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term memory is essential for multimodal agents that interact with users across sustained conversations. However, user memories are not always explicitly stated: they may also be implied by recurring background objects in images, ambient sounds in audio, or other peripheral multimodal cues. Existing benchmarks largely focus on text-only memory or explicit multimodal evidence, leaving implicit multimodal cues underexplored. We introduce CUE-Mem, a text-image-audio benchmark for evaluating long-term user memory from implicit cues. CUE-Mem contains 2,674 questions across explicit and implicit evidence settings and covers four tasks: Entity Recall, Long Pattern, Personalized Recommendation, and Answer Refusal. Across textualized memory systems, implicit performance remains far below oracle evidence, locating the main bottleneck in preserving and retrieving subtle cues rather than question answerability. Increasing caption detail recovers more of this evidence, but brings uneven gains and rapidly growing token costs, motivating native multimodal access. Yet native access does not uniformly resolve the bottleneck: evidence use depends strongly on the backbone, while multimodal indexing introduces substantial retrieval noise. CUE-Mem provides a testbed for memory systems that selectively retain, retrieve, and use subtle multimodal evidence.

---


### 225. [Retrieved but Not Delivered: Multimodal Memory Delivery for Long-Term Agents](https://arxiv.org/abs/2609.32590)

**<font color=#1a73e8>作者：</font>** Yuhang Jiang, Qingwei Liao, Kaize Yin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Work on memory for multimodal agents optimizes what is written, updated and retrieved. Between retrieval and the answer, however, is a stage that multimodal memory evaluations do not isolate: what of the retrieved memory reaches the model, and in what form. We call it delivery, and a controlled decomposition on MemLens locates the remaining room there. With the retrieved evidence set exactly fixed, delivering the original pixels instead of withholding them raises accuracy by 13.87 points on an 8B backbone, whereas making retrieval perfect on those same messages improves it by 2.31. Delivery is the larger term on all three MemLens backbones and grows with backbone strength; retrieval grows too, without closing the gap. We propose DeliverMem, an instantiation of delivery as three decisions: keep the original modality, give each item a readable identity, and state when it was seen, with a retrieval-side adapter for the one property delivery cannot supply. Each is measured against a delivery-matched control that alters only its own variable. DeliverMem leads the strongest published memory agent on MemLens at all four context lengths, and beats DMV-Bench's own strongest method at every setting on both backbones. On MemLens it does this on a tenth to a seventieth of the input. Each decision helps only where the question lacks what it supplies, and is null elsewhere. A single fixed configuration nonetheless leads both benchmarks, without training any component or modifying the stored records. Project page: this https URL

---


### 226. [SPACE: Sparse Predictive Attractor via Counterfactual Eviction for Streaming Video Memory](https://arxiv.org/abs/2609.32592)

**<font color=#1a73e8>作者：</font>** Hongjin Niu, Weizhan Zhang, Shuo Bao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fixed-capacity streaming video memory requires repeated eviction decisions whose effects accumulate over time. Yet existing policies are evaluated primarily in terms of retained information or downstream accuracy, leaving how repeated updates alter the futures supported by memory largely unexamined. We define a memory's predictive state as the future representations supported by its retained history and formulate eviction as counterfactual control over transitions in this space. We introduce SPACE (Sparse Predictive Attractor via Counterfactual Eviction), which uses a frozen multi-horizon JEPA to predict the future representations induced by alternative eviction actions. Counterfactual utility identifies future-useful alternatives, while slow predictive-basin geometry determines when to correct avoidable drift and when to adapt to sustained predictive change, without online parameter updates. We further introduce MABS-Bench, which evaluates future-task sufficiency, within-regime predictive stability, transition responsiveness, and perturbation recovery under matched causal streams and memory budgets. Across multiple video datasets, SPACE yields consistent improvements in dataset-native task performance while reducing predictive-state drift.

---


### 227. [Age of Learning: Temporal Persistence of Prediction Errors as a Learning Signal](https://arxiv.org/abs/2609.32593)

**<font color=#1a73e8>作者：</font>** Chenyang Wang, Stefan Forsström, Roger Olsson 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Current machine learning algorithms primarily rely on instantaneous signals such as loss, margin, and prediction confidence to characterize model behavior. These signals indicate how difficult a prediction is at the current optimization step, but they do not capture how long the model has remained incorrect. We study this temporal dimension of learning and introduce Age of Learning (AoL), a learning-state variable that measures the persistence of prediction errors over time. AoL increases while an error remains unresolved and resets when a correct prediction is achieved, thereby distinguishing persistent under-learning from transient mistakes. We develop AoL-based training strategies for both offline and streaming settings. In offline learning, sample-level AoL is accumulated over training and aggregated into class-level states that guide adaptive reweighting and resampling. In streaming learning, where full historical access is unavailable, we maintain lightweight class-level AoL states using current and buffered observations. Across long-tailed classification settings, AoL improves or matches standard training baselines, with larger benefits when learning difficulty persists over time. Multi-seed streaming experiments further show reproducible gains under temporally stable imbalance. Analysis of class frequency, loss, and margin shows that AoL is related to conventional difficulty measures but captures additional information about error duration. These results suggest that temporal persistence provides a useful complementary signal for characterizing and controlling learning dynamics in imbalanced and non-stationary environments.

---


### 228. [MA-FPPO: Multi-Agent Flow-Pretrained Policy Optimization](https://arxiv.org/abs/2609.32594)

**<font color=#1a73e8>作者：</font>** Guowei Zou, Haonan Chen, Haitao Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent flow policies learn cooperative behavior from fixed offline datasets, but often struggle to complete tasks in situations not covered by the offline data. In these situations, agents must both adapt to changes in the environment and coordinate with one another, yet action patterns learned offline are often insufficient for effective adaptation and coordination. To address this problem, we propose Multi-Agent Flow-Pretrained Policy Optimization (MA-FPPO), which uses online fine-tuning to improve the cooperative behavior of models pretrained with flow matching through new interactions with the environment. Building on the behavior learned during pretraining, we construct policies with explicit action likelihoods for discrete and continuous action spaces. We then update the pretrained model using shared team advantages to further improve coordination based on team performance. Our method achieves, on average, relative gains of 52.8% over the strongest listed offline baselines across 30 settings and 29.8% over purely online learning across 38 comparisons with matched online budgets and evaluation protocols.

---


### 229. [GAUGE: Group-Wise View-Inconsistency Rectification for Feed-Forward 4D Tracking](https://arxiv.org/abs/2609.32596)

**<font color=#1a73e8>作者：</font>** Zhuoqian Feng, Weixing Chen, Ziliang Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward models regress dense 3D point trajectories directly from monocular video, yet the residual after global alignment is substantial and lacks a structural explanation. Measured on dynamic query points across models and datasets, the error concentrates along the view direction, while the scale correction each motion group requires differs. The predicted displacement direction nevertheless supports reliable grouping, with a median angle far below the 90° random baseline. The systematic part of the residual is therefore a family of radial degrees of freedom per motion group, along directions 2D observations cannot constrain. We call it group-wise view inconsistency. We present GAUGE (Group-wise Adaptive Unsupervised Gauge Estimation), a training-free and model-agnostic post-hoc module. It recovers motion groups from direction consistency and spatial connectivity, then estimates a per-frame radial scale and group-level translation from 1% to 5% metric anchors, four degrees of freedom per group and frame. On dynamic query points of eight trackers, including D4RT, 4RC and SM4RT, our correction lowers endpoint error by 15.1% to 62.6% over the uncorrected predictions, while spending the same anchors on gradient fine-tuning improves the same models by only -1.1% to 15.2%. Code is publicly available at this https URL.

---


### 230. [When the Environment Becomes the Interface: Multisensory Environmental Interfaces for Human-AI Interaction in Autonomous Vehicles](https://arxiv.org/abs/2609.32604)

**<font color=#1a73e8>作者：</font>** Keqi Chen, Runjia Tan, Xinyi Fu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As AI increasingly assumes operational control, human-computer interaction is shifting from operating systems through explicit interfaces to inhabiting intelligent environments. This raises a fundamental question: when users no longer directly manipulate a system, what mediates their relationship with intelligent technologies? We introduce environmental interfaces: designed environmental conditions that shape human-AI relationships through ambient, holistic, and evaluative pathways rather than explicit functional interaction. Using autonomous vehicle cabins as a revealing context, we conducted a within-subject experiment with 24 participants (216 observations), manipulating lighting and scent in a simulated autonomous driving environment. Three findings emerged. First, perceived atmosphere accounted for 66.5% of the variance in overall journey experience, showing that environmental conditions can function as an interface rather than merely a supporting design element. Second, multisensory processing followed a hierarchical architecture: individual sensory appraisals were initially independent, while cross-modal integration emerged during higher-order environmental evaluation. Third, olfactory stimuli influenced affective responses and experience evaluation more strongly than visual stimuli, challenging the visual dominance of automotive interaction design. Environmental quality and sensory congruency also predicted trust in the autonomous system, suggesting that passengers may use environmental cues as proxy signals when direct assessment of AI competence is difficult. These findings establish environmental interfaces as a distinct interaction modality and point to a broader transition from designing interfaces for operating intelligent systems to designing environments for inhabiting them.

---


### 231. [Levy-Driven Correspondence Estimation for Registration](https://arxiv.org/abs/2609.32612)

**<font color=#1a73e8>作者：</font>** Qianliang Wu, Jiaqi Yang, Wankou Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Finding reliable point correspondences is difficult when point clouds have low overlap or undergo non-rigid deformation. Iterative refinement can correct uncertain matches, but costly network evaluations limit the number of updates. We present LevyMatch, a Lévy-driven method that uses random jumps to refine a soft matching matrix. At each step, a network uses the current matching state and geometric information to predict a target matching matrix. A Brownian reference bridge gives an explicit formula for the update toward this target. A Gamma random clock sets the time step for each update. The updated matches provide new geometric feedback for the next target prediction. We further propose a fixed front-loaded Gamma policy that assigns more expected clock time to early updates and less to later ones, without retraining or extra network evaluations. Reordering the same sampled Gamma increments shows that placing larger increments early gives higher accuracy than placing them late. On 4DMatch and 4DLoMatch, our method improves both non-rigid feature matching recall (NFMR) and inlier ratio (IR) over the compared methods. The front-loaded policy achieves 93.09% NFMR and 92.11% IR on 4DMatch, and 82.79% NFMR and 79.07% IR on 4DLoMatch.

---


### 232. [Learning the Graph and the Embedding Together: Classifier-Independent Rewiring for Heterophilic Node Classification](https://arxiv.org/abs/2609.32613)

**<font color=#1a73e8>作者：</font>** Harshit Kumar, Sujan Chakraborty, Priyanka Saha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural networks lose much of their advantage on heterophilic graphs, where connected nodes often carry different labels. Graph rewiring is a popular remedy, but rewiring methods are usually evaluated with a single classifier, which makes it hard to tell whether the gains come from the new topology or from that particular pairing. We propose an affinity-guided rewiring method that estimates the graph and the node representation together. It alternates, in the spirit of expectation maximisation, between training a lightweight graph neural network on the current graph and re-weighting candidate edges under a modularity objective with a pseudo-label homophily term. Candidate edges come from a compact pool scored by a contrastively learned node similarity and a neighbourhood-distribution affinity. The method returns two classifier-independent outputs: a rewired graph and a node embedding learned on it. Across six heterophilic benchmarks and five downstream classifiers, it improves accuracy over the original graph with normalised features in 23 of 30 classifier-dataset combinations, with a mean gain of 5.8 points, and reduces the accuracy spread between classifiers about fourfold. A controlled ablation shows that the two outputs are each useful and play complementary roles: the embedding contributes most of the accuracy gain, while the rewired graph makes different classifiers agree. A fully unsupervised variant, which uses no labels during rewiring, retains most of the improvement. The rewired graphs are also more homophilic and improve label propagation and community detection.

---


### 233. [Stabilizing the Dynamic Low-Rank Training](https://arxiv.org/abs/2609.32615)

**<font color=#1a73e8>作者：</font>** Zhonghan Xu, Ling Wang, Junhao Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training neural networks directly in a low-rank parameterization is an appealing route to reducing memory, compute, and storage simultaneously during both training and inference. Dynamic low-rank training (DLRT), which confines weights to a rank-$r$ manifold via the Galerkin projection of the gradient flow, is particularly attractive because it identifies efficient subnetworks on the fly without specialized initialization or post-factorization. However, DLRT fails to find trainable networks under high compression. In this paper, we derive the gradient flow of the best rank-$r$ approximation and point out that the offset of DLRT comes from a curvature-coupling term which is large and thus non-negligible under aggressive compression. Guided by this analysis, we propose a stable dynamic low-rank training method, named SDLRT, which maintains a lightweight compensation buffer that reinjects the top neglected singular directions. Additionally, we introduce a negative feedback on the truncation tolerance to stabilize each layer's rank. Experimentally, SDLRT reliably finds trainable subnetworks where DLRT collapses and as a PEFT adapter on DeBERTa-v3, it achieves the best average score on SuperGLUE at only $2.8\%$ parameter overhead over LoRA.

---


### 234. [Intuition vectors](https://arxiv.org/abs/2609.32619)

**<font color=#1a73e8>作者：</font>** Shahar Haim, Daniel C. McNamee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large self-supervised vision models learn representations that support scene segmentation and the semantic decomposition of physical objects. We ask whether their representational geometry supports transfer to visual reasoning problems without any task-specific fine-tuning. We hypothesized that relational representations may bridge perception and abstract reasoning by encoding similarities and transformations among visual inputs such that an intuitive, implicit form of reasoning may be performed via latent vector arithmetic. Specifically, we examine DINOv3, MAE, and random pixel projections on abstract and naturalistic Bongard problems, ARC-AGI-1 and ARC-AGI-2, and novel ARC-GEN instances. On both Bongard benchmarks, the accuracy of a simple nearest-centroid readout of frozen visual embeddings is within four percentage points of the task-specific baselines reported with the original benchmarks. In ARC, latent difference vectors summarizing demonstration input-output transformations, which we refer to as intuition vectors, show greater alignment with test vectors from the same task, whereas those from unrelated tasks are near orthogonal. This latent geometry is operational: transporting a query along its intuition vector consistently improves exact-output retrieval, reaching 70.7 on ARC-AGI-2 evaluation. Across 397,000 ARC-GEN instances from 794 tasks, single-pair intuition vectors identify the generating task with approximately 87\% leave-one-out accuracy. These findings suggest that latent vector arithmetic over frozen visual representations supports implicit rule inference across varied problem domains without a generative model component, indicating that inferring an abstract transformation and generating its instance-specific consequence may be separable capacities.

---


### 235. [DraftAttention2: Fast Video Diffusion with Low-Resolution-Guided Mixed-Precision Attention](https://arxiv.org/abs/2609.32628)

**<font color=#1a73e8>作者：</font>** Rui Ding, Haopeng Li, Weize Ma 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation has broad applications in content creation and entertainment. Diffusion transformers have advanced the quality of generated videos, but attention over spatiotemporal tokens becomes increasingly expensive as video resolution and duration increase. We present DraftAttention2, a training-free framework that uses the low-resolution draft attention map to jointly select attention blocks and assign their numerical precision. Specifically, spatial 2D average- and max-pooled queries and keys capture complementary regional statistics to estimate block importance, and a shared ranking assigns higher precision to important blocks, lower precision to less important retained blocks, and skips the rest under configurable budgets. Our analysis separates sparsification error from attention-weighted quantization error, establishing when recovering skipped interactions with low-bit computation tightens the output-error bound. This analysis motivates retaining more interactions at low precision while reserving higher precision for blocks with larger attention mass. To translate these fine-grained assignments into practical speedups, we further develop fused operand preparation and a single attention kernel with precision-specific phases, sharing data movement, softmax statistics, and output accumulation across precisions. Experiments demonstrate that our method achieves a superior quality-efficiency trade-off over existing efficient video generation methods. Notably, its advantage is particularly pronounced for few-step video diffusion, where jointly combining sparsity with 4- and 8-bit mixed-precision computation substantially improves generation quality while retaining significant acceleration. Code is available at this https URL

---


### 236. [SWE-MILE: Asynchronous Potential-Induced Milestone Credit Assignment for Long-Horizon Software Engineering Agents](https://arxiv.org/abs/2609.32631)

**<font color=#1a73e8>作者：</font>** Chaoqun Cui, Hao Zhou, Meiqi Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon software engineering (SWE) agents trained with reinforcement learning with verifiable rewards (RLVR) typically receive only terminal outcome supervision, making it difficult to distinguish productive actions from redundant exploration or functional regressions. We propose SWE-MILE, an asynchronous potential-induced milestone credit assignment framework that derives fine-grained process supervision from workflow runtime, without auxiliary reward models or external evaluators. SWE-MILE quantifies task-relevant file exposure and test-state alignment as navigation and verification potentials, respectively. Differences in these potentials attribute milestone progress and regressions to individual actions, while discounted backward credit propagates supervision to preceding steps. To efficiently acquire intermediate verification states, SWE-MILE further introduces asynchronous shadow probing, which replays repository-changing actions in an isolated sandbox and runs verification in parallel with the agent's primary interaction, largely hiding verification latency. The resulting process credit augments terminal outcome advantages and provides informative learning signals. Experiments on two representative long-horizon SWE tasks demonstrate substantial improvements in agent performance, highlighting workflow runtime signals as a practical source of process supervision for long-horizon SWE agents.

---


### 237. [Extremely Fast and Compact Binary Graph Representations via Randomized Operator Sketching](https://arxiv.org/abs/2609.32641)

**<font color=#1a73e8>作者：</font>** Srajan Agarwal, Megha P, Bikas C Das 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural networks typically rely on dense, floating-point node representations, which can impose substantial memory and computational costs. Binary graph hashing offers an alternative by encoding node information as compact bit strings. However, existing approaches either sacrifice global topological information for computational efficiency or incur substantial generation costs. We introduce an ultra-fast, entirely algebraic hashing method that constructs binary node representations directly from graph structure, without requiring node features or gradient-based training. Our method approximates a high-order structural transition matrix using randomized column sampling inspired by the Nyström method and combines it with an efficient label-safe semantic propagation mechanism. The resulting continuous representations are discretized through column-wise thresholding to obtain compact binary codes. Experiments on ten node classification datasets show that the proposed method consistently improves classification accuracy over existing feature-free binary baselines while requiring sub-second code generation on many datasets. The resulting binary representations are also naturally suited to event-driven computation, making them compatible with neuromorphic spiking neural networks and gradient-free learning rules. These results demonstrate that simple algebraic approximations can provide an efficient alternative to learned pipelines for discrete graph representation learning.

---


### 238. [Prediction Limits and Koopman Closure of Geometry-Induced Soft State Abstractions](https://arxiv.org/abs/2609.32652)

**<font color=#1a73e8>作者：</font>** Mohit Kumar, Somayeh Kargaran  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study when geometry-induced soft state abstractions admit accurate finite-dimensional linear dynamics. Each state is represented by simplex-valued coordinates obtained from class-specific Kernel Affine Hull Machine (KAHM) reconstruction scores, and a matrix is used to predict the next-state coordinates. Our main result is a computable lower confidence bound on the minimum root-mean-square prediction error over all matrices satisfying a prescribed spectral-norm limit. The bound combines within-class variation of successor coordinates with the deviation of soft coordinates from their one-hot reference labels, and can be evaluated from independent state-successor pairs without fitting a prediction matrix. For fixed coordinates and evaluation distribution, the certificate converges almost surely to a population lower bound as the sample size grows; any tolerance below this limit is eventually certified unattainable. Reconstruction-score margins further control the soft-to-hard assignment error. Under deterministic dynamics and exact coordinate closure, eigenvectors of the closure matrix and its reduced transpose induce Koopman and adjoint Koopman eigenfunctions, respectively. A four-state KAHM construction shows that identical soft coordinates can permit exact closure under one dynamics map yet force positive prediction error under another. Experiments on Duffing, Van der Pol, CartPole, MountainCar, and Acrobot compare direct soft-coordinate prediction with state-space DMD/EDMD baselines and report prediction, representation-variation, and spectral diagnostics. The benchmarks assess fitted models but do not numerically evaluate the exclusion certificate.

---


### 239. [MixBench-TS: A Multivariate Time Series Forecasting Benchmark Where Channel Mixing Pays Off](https://arxiv.org/abs/2609.32656)

**<font color=#1a73e8>作者：</font>** Ibram Abdelmalak, Mischa Putzke, Jungmin Choi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multivariate Time Series Forecasting (MTSF) models that mix information across channels assume that the past of one channel carries information about the future of another. Yet they are evaluated on a small fixed set of standard datasets whose cross-channel structure is rarely examined. We ask two questions: "How can we reliably measure lagged, non-linear, and joint coupling in MTSF datasets?" and "Do the standard datasets actually have such coupling?" To answer the first, we test four candidate measures on synthetic datasets with planted ground-truth coupling: Granger Causality (GC), Transfer Entropy (TE), lagged Mutual Information (MI), and the CD gain, a model-based measure we introduce that compares a channel-dependent (CD) model to its channel-independent (CI) variant. Only lagged MI and the CD gain recover every planted coupling. For the second question, the answer is a definite no, as the standard datasets have a median of only 23% lagged-coupled channel pairs and a median CD gain of -4.9%, compared to 78% and +4.6% on chaotic ODE systems. We therefore propose MixBench-TS, a benchmark of 10 real-world datasets with a median of 55.5% lagged-coupled pairs and a median CD gain of +1.7%. Across six state-of-the-art models tuned under one protocol, CI models win on 10/10 (MSE) and 8/10 (MAE) standard datasets, but on only 3/10 and 2/10 MixBench-TS datasets. We recommend using our benchmark for evaluating new CD models. Moreover, we propose profiling new datasets with lagged MI and the CD gain before using them to evaluate multivariate models. Code and data are available at this https URL.

---


### 240. [World Models with Predictable Long-Horizon Marginals](https://arxiv.org/abs/2609.32657)

**<font color=#1a73e8>作者：</font>** Yuhao Du, Shunian Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate one-step predictions do not ensure that a world model's rollouts retain the data distribution. We make the model's decoded stationary law explicit by learning a decoder of a fixed Gaussian reference and constraining the behaviour-averaged transition to preserve that reference. For controlled systems, a joint transition uses a conditional action chart to preserve behaviour occupancy without requiring invariance at each fixed action. Joint state--action rotations and parallel Gaussian noise give an exactly preserving transition with a tractable conditional density. We derive an absolute convergence bound from finite initialization banks and control departure from the reference through conditional action-space divergence. Across $216$ fitted pixel checkpoints on twelve control tasks, the occupancy model with a reference mixture retains every evaluated chain at $10^5$ steps in all $36$ task--seed cells, with a rollout-minus-reference energy-statistic difference of $-0.0002\pm0.0003$ (training-seed standard error). Each of the four nonpreserving comparison arms loses chains, although the Gaussian arm is more accurate at ten steps. An offline DreamerV3 reference also achieves better short-horizon accuracy. These results distinguish three properties of a world model: the distribution it approaches, the rate of approach, and the conditional dynamics it learns.

---


### 241. [Equivariant Neural Primal-Dual Assignment for Maximum Common Edge Subgraphs](https://arxiv.org/abs/2609.32661)

**<font color=#1a73e8>作者：</font>** Jiaqing Xie, Yanchao Li, Zhuo Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Maximum common edge subgraph (MCES) matching finds a partial vertex correspondence between two labeled graphs that preserves as many labeled edges as possible. Molecular similarity search requires matching many graph pairs, making the cost of repeated queries important. The strongest baseline attains accurate MCES solutions but trains a separate network for each pair. We introduce Equivariant Neural Primal-Dual Assignment (ENPDA), which learns a shared matching policy and applies it to new pairs without further training, answering queries roughly three orders of magnitude faster and recovering its training cost after a few dozen queries. The policy recomputes exact objective marginals for candidate matches and learns corrections and step sizes that update their scores. Target prices respond to competition when several source vertices favor the same target. Four update rounds and a Hungarian projection produce a partial one-to-one matching. We prove per-pair guarantees that hold for any network parameters. In exact arithmetic, reordering either graph permutes the assignment and price states, the projected matching is one-to-one, and repaired prices give a valid MCES upper bound. Subtracting the preserved-edge count bounds the optimality gap; combined with structural caps, these certificates prove global optimality for 60 of 291 native test pairs. On three molecular benchmarks with disjoint train/validation/test splits, ENPDA improves over an analytic counterpart with the same update and projection budget by 7.4-8.6 accuracy points; after one second of refinement search, 2.5-3 points of the gain remain. Transferred without fine-tuning to edge-deletion tasks from social and protein graphs, the policy gains 9.1-17.6 points over the analytic counterpart. When output matchings must keep aromatic rings intact, ENPDA recovers more reference bonds than the baselines on all three datasets.

---


### 242. [Timestep Weighting: A Hidden Key to Effective ELBO-Based Flow-Matching RL](https://arxiv.org/abs/2609.32665)

**<font color=#1a73e8>作者：</font>** Qinwei Ma, Jingzhe Shi, Simin Fan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> ELBO-based reinforcement learning offers a sampler-agnostic approach to fine-tuning flow matching models with reward feedback. Timestep weighting in ELBO-based RL has large impact on performance, and it also provides a unified view (as we show in this work) to understand prediction losses heuristically chosen in prior work, yet it remains under-researched and is often chosen to inherit pretrain configs. We investigate impacts and dynamics of timestep weighting in ELBO-based RL. We show that effective weighting depends on both the reward landscape and stage of learning. (1) Through experiments on controlled CIFAR image generation, complemented by robotics, we investigate how weighting impacts reward-driven updates across noise levels. (2) Through gradient analysis, we reveal distinct patterns of cross-noise coordination across tasks and their evolution during training. These findings motivate the hypothesis that useful weighting depends on the gap between the policy's current behavior and the behavior favored by the reward. (3) Guided by this analysis, we study simple static weighting, budgeted profile selection, and dynamic schedules that improve performance beyond conventional target choices. Our results establish timestep weighting as an important design choice for flow-matching RL and motivate further research into methods that choose and adapt it throughout learning.

---


### 243. [Learning from a Thoughtful Teacher: Adaptive On-Policy Self-Distillation for Mathematical Reasoning](https://arxiv.org/abs/2609.32667)

**<font color=#1a73e8>作者：</font>** Jiacheng Du, Weiwei Xie, Tianyi Du 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) trains a question-only student with token-level feedback from a teacher given training-only privileged information (PI). OPSD therefore provides dense, on-policy supervision, and is free of a larger external teacher, but its effectiveness rests on how PI is designed and utilized. Our preliminary diagnostics suggest a significant gap between teacher utility and student learnability, where a small fraction of high-disagreement tokens dominate the distillation signal, and short teacher continuations at these positions further expose more explicit PI leakage than transferable correction cues, indicating a strong intent on injecting PI-conditioned shortcuts. We propose Adaptive On-Policy Self-Distillation (AOPSD), which adapts what information the teacher receives and how strongly its feedback influences learning. AOPSD encodes each solution as a reasoning DAG, orders problems by the student's evolving capability, and reveals only the affordable subgraph and its next frontier as PI. For high-disagreement tokens, AOPSD utilizes short teacher continuations as probes to encourage useful guidance while mitigating PI-conditioned shortcuts among teacher supervisions. On HMMT25, AIME24, AIME25, and BRUMo25, AOPSD achieves 72.5% Pass@8, which is 6.7 percentage points above OPSD and 4.2 above the strongest competing baseline while reducing 15 percentage points of training time at lower cost.

---


### 244. [When Better Gets Worse: Improvement Fidelity for Self-Improving Agents in Adaptive Worlds](https://arxiv.org/abs/2609.32677)

**<font color=#1a73e8>作者：</font>** Ke Wang, Zijie Zhao, Zhiyi Yuan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-improving agents increasingly rely on proxy verifiers to choose policy updates, yet deployment can change the world in which those updates are evaluated. An update that looks better to the verifier can therefore become worse after deployment even when the verifier ranks policies well overall. We formalize this gap as Improvement Fidelity, which asks whether proxy improvements preserve the sign and ordering of deployment improvements over the updates an improvement process actually proposes. We show that global policy accuracy need not guarantee update fidelity: operator shift and deployment response can create update-level errors, while candidate margins determine whether those errors change the replacement decision. We introduce PIVOT-KG, a paired, decision-aware validator that allocates scarce high-fidelity evaluation according to the expected reduction in selection regret per unit cost. Across 90 held-out roots in Leduc, Kuhn, and Melting Pot, proxy and deployment optimal sets are disjoint in 51 cases. In an eight-candidate HighwayEnv stress test, PIVOT-KG reduces mean improvement-selection regret from 0.0435 under the exact Uniform validation rule to 0.0055 at the primary budget. Together, these results show why reliable self-improvement should evaluate proposed improvements in the worlds they induce, while providing a practical rule for allocating scarce deployment evidence when it can affect the replacement decision.

---


### 245. [The GUI Is Not the State: Diagnosing State Aliasing in GUI World Models](https://arxiv.org/abs/2609.32679)

**<font color=#1a73e8>作者：</font>** Dongsheng Liu, Chao Jin, Wenkui Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> GUI World Models (GUI-WMs) are increasingly used to predict future states for agent planning and simulation, yet most existing formulations condition only on the current GUI observation and action. We identify state aliasing, where the vis- ible interface omits transition-relevant environment state, so identical observable conditions can correspond to different valid futures. To diagnose this failure mode, we introduce StateAliasBench, a diagnostic benchmark that explicitly isolates such ambiguities via strict pairing. We further propose lightweight predictive- state recovery that infers structured state from history and augments otherwise frozen GUI-WMs through a deterministic state interface. Family-specific special- ists provide state recovery across heterogeneous state types, and multi-teacher dis- tillation consolidates them into a single unified estimator. Experiments show that existing GUI-WMs exhibit systematic failures under observation-only condition- ing, while predictive-state augmentation substantially restores state-sensitive pre- diction across evaluated WMs, preserves generative fidelity, and improves down- stream performance of GUI agents on AndroidWorld. These results suggest that reliable GUI world modeling should account not only for what is visible, but also for the hidden transition state that determines what happens next.

---


### 246. [Dude, Where's My State? Execution Information Requirements for Stateful Agents](https://arxiv.org/abs/2609.32687)

**<font color=#1a73e8>作者：</font>** Nikita Mehrotra, Ashish Tiwari, Priyanshu Gupta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-running agents must preserve information that later steps depend on. We introduce the Execution Information Requirement (EIR), a lower bound on the information that must remain accessible for correct completion under specified task and access conditions. We develop LACUNA, a framework that generates tasks with known dependencies and varies information demand, retention, and recovery separately from the difficulty of individual operations. Across four models, restoring a missing result raises accuracy on affected recall steps to 100%, compared with 0% for equal-length irrelevant information. Sufficient storage alone does not ensure success: retention policies can discard required results, errors can propagate through later computations, and agents can stop before recovery is complete. We also introduce VESTIGE, which uses agent execution traces to construct semantic graphs and measure information demand for real tasks. Across 72,562 software-agent trajectories, VESTIGE reveals a steeper distance-related decline in solution-relevant rereading for failed runs (RR 0.951 per distance doubling), while adjusted peak demand alone is not associated with failure. Together, these contributions support evaluating whether agents preserve and recover the information their tasks require.

---


### 247. [Flat-Consensus Diffusion for Robust Data Reshaping under Noisy Evaluator](https://arxiv.org/abs/2609.32696)

**<font color=#1a73e8>作者：</font>** Hongyu Cao, Kunpeng Liu, Fei Xie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Data shape determines how features are structured, how patterns are separated, and how distributions cover the underlying domain. Poor data shape can make models learn noise rather than generalizable structure. This paper studies robust feature-centric data reshaping: generating feature transformations that remain useful, stable, and reproducible under noisy evaluation and imperfect data conditions. We view reshaping operation sequence search as reward-guided diffusion generation, and robust reshaping as searching for regions in the latent reward landscape rather than isolated high-reward transformations. The key challenge is dual instability: noisy evaluators distort local reward guidance, while stochastic generative trajectories can converge to inconsistent solutions. We propose FCDiff, a flat-consensus diffusion framework that addresses both failures through a micro-macro decomposition. The micro layer replaces point-estimate reward guidance with Gaussian-smoothed, Monte Carlo averaged gradients, steering generation toward locally flat reward regions. The macro layer aggregates independently guided trajectories with a weighted Frechet-mean barycenter, selecting consensus-supported basins and filtering stochastic outliers. Across an 8-dataset headline cohort under heavy-tailed evaluator noise, FCDiff attains the best aggregate rank on lower-tail reliability and robustness against both search-based AutoFE and robustness-oriented generative baselines, with statistically significant accuracy gains over every generative baseline. Our results show that robust data reshaping requires searching for flat, consensus-supported regions rather than sharp single-trajectory optima.

---


### 248. [CoWindow Attention: Full Causal Coverage Is a Collective Property](https://arxiv.org/abs/2609.32704)

**<font color=#1a73e8>作者：</font>** Jingze Shi, Zhangyang Peng, Xianduo Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> FullAttn repeatedly exposes the complete causal history to every attention head, creating substantial redundant computation and memory traffic even with IO-efficient dense kernels. We introduce CoWA, a structured attention architecture that distributes access to the causal history across KV heads. All heads share near-diagonal and prefix-sink windows, while complementary long-range windows partition the remaining history. Their union provides full causal coverage although each head attends sparsely to distant tokens. This position-defined attention pattern requires no learned router or indexer, is used consistently during training and inference, and aligns with KV-head tensor parallelism. A window-matched ablation at 8K isolates the effect of complementary long-range allocation: CoWA with 100% collective coverage reaches 89.73% accuracy, compared with 89.97% for FullAttn, while duplicated long-range windows perform substantially worse. Across a broader controlled associative-recall comparison with matched token budgets, CoWA closely tracks FullAttn as the context grows, whereas other sparse patterns lose a substantial fraction of the associations. In an attention-operator benchmark at 128K tokens with tensor parallelism, CoWA reduces forward and backward latency during training by 7.4x and 8.6x and decoding latency during inference by 3.0x over FullAttn. Its per-rank peak operator memory matches FullAttn during training and is 7.6x lower during decoding. Across scaling-law training from 0.6B to 14B parameters, CoWA closely tracks FullAttn in perplexity while reducing total training FLOPs. The resulting 14B models and 32B models from separate continued training achieve comparable knowledge, reasoning, and long-context retrieval scores to FullAttn. These results show that full causal coverage can be a collective property of the head ensemble rather than a duplicated property of every head.

---


### 249. [DPAMixerSR: An Efficient Degradation-Pattern-Aware Model for Image Super-Resolution](https://arxiv.org/abs/2609.32705)

**<font color=#1a73e8>作者：</font>** Song-Li Wu, Haonan Jiang, Jixuan Fan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While content-adaptive schemes have delivered notable advances in image super-resolution (SR), existing approaches typically focus on texture complexity and ignore intrinsic degradation factors (e.g., blur kernels or noise patterns), leading to suboptimal computation allocation and reconstruction performance. To remedy this, we propose DPAMixerSR, a degradation-pattern-aware framework that enables efficient SR through adaptive sparse computation. We design a lightweight Perceptual Degradation Ranking (PDR) module partitions the image into severely and mildly degraded patches, which are routed to the Adaptive Sparse Processing (ASP) and a lightweight convolutional branch, respectively. ASP performs structure-aligned, multi-scale sparse propagation and bidirectional refinement, while the convolutional branch enhances efficiency in mildly degraded regions. By coupling degradation-driven routing with structure-aligned sparse processing, DPAMixerSR establishes a self-regulating framework that dynamically balances computational efficiency and reconstruction fidelity. Extensive experiments on various SR tasks demonstrate that our DPAMixerSR achieves superior structural restoration and perceptual fidelity with markedly reduced computational overhead, providing a novel and scalable framework for degradation-aware, resource-efficient SR.

---


### 250. [ProDyGS: Dynamic Gaussian Splatting from a Single Static Monocular Camera](https://arxiv.org/abs/2609.32711)

**<font color=#1a73e8>作者：</font>** Ugo Leone Cavalcanti, Fabio Tosi, Matteo Poggi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present ProDyGS, a novel dynamic 3D Gaussian Splatting framework for high-quality novel view synthesis from videos captured by a single static camera. While existing methods rely on multi-view setups or significant camera motion for geometric constraints, our approach addresses the challenging scenario where multi-view supervision is completely absent. We overcome this limitation by generating synthetic multi-view supervision through depth-guided proxy image synthesis. Specifically, we estimate temporally consistent depth maps using foundational monocular depth networks, then construct 3D Gaussian representations that generate proxy images from arbitrary viewpoints. A deformation network learns temporal dynamics by warping canonical Gaussians using this augmented supervision. Experiments on the DyNeRF dataset demonstrate that our method achieves state-of-the-art performance while requiring only monocular depth estimation as external supervision, outperforming approaches that rely on stronger priors such as scene flow.

---


> [!TIP]
> 当前位于：**201-250**（第 5/19 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-908](./part-19.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
