# 📦 其他研究 | 2026年10月09日

> 本类共 **324** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-324](./part-07.md)

---

### 201. [Global Average Precision for Representation Learning](https://arxiv.org/abs/2610.09863)

**<font color=#1a73e8>作者：</font>** Bill Psomas, Mohammad Mahdi, Michalis Thomas 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Standard information retrieval metrics, such as mean Average Precision (mAP), assess performance one query at a time, based on how the similarities between a query and its positives compare against those with its negatives. The same holds for common representation learning losses, such as InfoNCE and per-query AP surrogates. None of them considers whether similarities are comparable across queries, which any system with a single decision threshold relies on. Global Average Precision (gAP) does, by ranking all query-candidate pairs in one list and computing a single AP. We introduce gSAP, a differentiable surrogate of gAP. It needs only a similarity matrix and a binary matrix marking the positive pairs, the same input as existing losses, so it is a drop-in replacement for them and agnostic to the encoder, the modality, and the source of supervision. Since it considers all possible pairwise comparisons in the batch jointly, it also remains trainable at low temperatures, a regime where per-query surrogates run out of gradient. Swapping it into established recipes improves supervised metric learning, cross-modal alignment, and self-supervised pretraining, where, to our knowledge, it is the first ranking loss to replace the community standard InfoNCE in the latter two. Its similarities are more consistent across queries, which drives the gains under a universal threshold. gSAP retrieves up to four times as many positive pairs as the strongest AP surrogate at the same precision, and it degrades the least when queries with no positives in the database are added. Beyond thresholding, models trained with gSAP also learn better representations, with higher transfer, $k$NN and zero-shot classification accuracy.

---


### 202. [MUNITE: Unified Multimodal Latent Inference for Any-to-Any Multimodal Generation](https://arxiv.org/abs/2610.09866)

**<font color=#1a73e8>作者：</font>** Kyeongmin Yeo, Minhyuk Sung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce MUNITE, a latent-variable framework for flexible any-to-any multimodal generation that treats encoding and latent generation as the same inference problem under different amounts of observed evidence. Given any subset of modalities, MUNITE models the conditional distribution over the latent representation associated with the complete observation. Full observation recovers deterministic encoding, no observation recovers the latent marginal, and intermediate subsets define conditional latent inference, all within a single conditional flow model. A shared latent sample captures variation that must remain consistent across generated targets, while modality-specific generative decoders model the remaining uncertainty independently. To learn these conditional distributions from incomplete training examples, we extend conditional flow matching through self-distillation: predictions conditioned on richer available observations supervise the same model conditioned on smaller subsets at the same intermediate latent state. When the richer-evidence trajectory follows the exact conditional flow, this provides the same expected learning signal as full-target denoising. Across PolyMNIST-D-Q, FFHQ64, and image-text-audio, MUNITE achieves competitive or better generation quality and source-target alignment, with higher joint-generation coherence. In particular, it attains the highest coherence in all one-to-many and unconditional image-text-audio comparisons, showing the effectiveness of unified latent inference across diverse multimodal settings.

---


### 203. [Bringing BNNs to Fast Event Processing](https://arxiv.org/abs/2610.09873)

**<font color=#1a73e8>作者：</font>** Paul Longour, Julien Moreau, Franck Davoine  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Binary Neural Networks (BNNs) enable efficient deep learning deployment on resource constrained devices with weights and activations compressed to one bit, substantially reducing model size and inference cost. Event cameras offer complementary advantages, including low latency, high dynamic range, and low power consumption, by capturing asynchronous streams of events rather than dense image frames. Despite their shared emphasis on efficiency, the combination of these technologies remains largely unexplored. This work aims at adapting and evaluating modern deep BNN architectures on event data. We also show that cross-modal pretraining from RGB data can improve the classification accuracy of BNNs on neuromorphic datasets. We introduce the Polar-wise Binary Event Volume (PBEV), a binary representation that enables event-camera data to be processed directly by BNNs and represents a step toward fully binarized event-based vision systems. Best evaluated BNN on N-Caltech101 classification benchmarks shows 90.58% accuracy with 7.5x less operations than their full-precision counterparts.

---


### 204. [SANet: Selective Attention Network for Infrared Small Target Detection](https://arxiv.org/abs/2610.09875)

**<font color=#1a73e8>作者：</font>** Yingmei Zhang, Wangtao Bao, Qin Xiao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrared small target detection aims to accurately identify and locate dim targets in complex backgrounds and supports applications such as maritime surveillance and military search and rescue. However, the small size and weak contrast of infrared targets make it difficult to balance detection accuracy and false alarms. This paper proposes a selective attention network (SANet) for infrared small target detection. A dual-path semantic-aware module combines standard and pinwheel-shaped convolutions to preserve local spatial consistency and capture broader contextual information. Spatial and channel attention further refine the features and improve target-background discrimination. To address the limitations of static skip connections in U-Net, a selective attention fusion module adaptively integrates features across scales using spatially varying weights. It selectively enhances salient regions and improves discrimination between true targets and false alarms. Experiments on three public benchmarks, NUAA-SIRST, IRSTD-1K, and NUDT-SIRST, show that SANet achieves competitive performance in intersection over union (IoU), normalized IoU, detection probability, and false alarm rate. Its IoU exceeds that of the second-best method by 1.93, 4.32, and 2.21 percentage points, respectively. These results support the effectiveness of SANet in dim-target perception, discriminative feature representation, and background suppression.

---


### 205. [Think Before You Paint: Recursive Latent Reasoning for Diffusion Models](https://arxiv.org/abs/2610.09876)

**<font color=#1a73e8>作者：</font>** Paweł Skierś, Małgorzata Grzanka, Wojciech Masarczyk 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion models generate realistic images but often fail on visual reasoning tasks, such as filling in a Sudoku or drawing the path through a maze. When a discrete symbolic representation is available, recursive methods such as the Tiny Recursive Model (TRM) solve even hard instances of these puzzles. We ask how such reasoning can be carried over to pixels, where no symbolic representation is available. We propose Painter-Thinker (PaTh): a small recursive network (the Thinker) reasons over a grid of learned tokens that encode the noisy image and the conditioning, refines a latent state within every denoising step, and steers a frozen diffusion model (the Painter) through ControlNet adapters. The Thinker is trained with the standard reconstruction loss alone, without symbolic targets, a solver, or a verifier. PaTh solves 92.5% of hard MNIST Sudoku puzzles (prior best 75%) and 71.2% of extreme ones (prior best 4.1%), with 10M parameters against 82M for a standard diffusion model. It also improves on mazes, Queens, and CLEVR scenes with specified spatial relations, and its advantage grows with problem size. Diagnostic experiments show that PaTh recovers from injected mistakes that the diffusion model cannot repair, especially when many cells are wrong. Together, these results show that reasoning mechanisms developed for symbolic data can be integrated into pixel-space diffusion without symbolic supervision, opening a path toward generating data under increasingly complex constraints.

---


### 206. [Layerwise Error Attribution for Fast and Robust Mixed-Precision Post-Training Quantization](https://arxiv.org/abs/2610.09877)

**<font color=#1a73e8>作者：</font>** Samy Houache, Yann Traonmilin, Jean-François Aujol  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixed-precision post-training quantization is a network compression method that assigns bits layer by layer, under a global memory budget using a small calibration set. The main difficulties are to overcome the combinatorial nature of the allocation problem and to manage the sensitivity to small, potentially corrupted databases. Hence, an efficient allocation method should be fast to compute and preserve model quality when calibration data are corrupted. To design such a method, we derive a layerwise probabilistic analysis of the quantization error that separates propagated error from the local perturbation introduced at a given layer. We use this local term to build a separable score for a simple allocation algorithm, that requires no external solver. The probabilistic nature of our approach brings robustness to corrupted data. On denoising tasks with DRUNet, with an average budget of 4 bits per weight, our method matches or improves state-of-the-art mixed-precision baselines under clean calibration, and is more robust to corrupted calibration, with PSNR gains of up to 7.5 dB under the tested corruptions. Experiments show bit-allocation speed-ups from 28x to 2,570x over the studied baselines. For quantized diffusion models, our experiments show that a direct application of our framework also improves the state-of-the-art.

---


### 207. [Identifiability of a dissipative knowledge-dynamics model: exact recovery under designed excitation, degeneration on observational data](https://arxiv.org/abs/2610.09889)

**<font color=#1a73e8>作者：</font>** Arman Kostanian, Armen Beklaryan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Human learning is a dissipative dynamical process: mastery accumulates through practice, decays through forgetting, and propagates across interdependent concepts. We model it as a nonlinear dissipative system of ordinary differential equations whose parameters are mechanistically meaningful (a concept-transfer matrix encoding prerequisite coupling, per-concept forgetting rates, and a saturating practice-response gain), and we study when those parameters can actually be recovered from data. We prove a structural identifiability theorem for the associated inverse problem under explicit excitation conditions, with constructive closed-form recovery for the two-concept case, together with monotonicity, robustness and L-stability results. We derive a semi-implicit L-stable scheme for the dissipative subsystem and a batched solver numerically equivalent to the per-trajectory formulation (bit-exact predictions, gradients to $10^{-10}$) yet two orders of magnitude faster, making estimation feasible on cohorts of $10^5$ learners. The empirical study is two-sided. Under the theorem's excitation conditions, synthetic recovery is exact: parameters to machine precision, prerequisite structure at $F_1 = 1.0$. On large observational benchmarks it is not. An apparently strong recovery, with forgetting rates correlating with topic difficulty at Spearman $\rho = 0.83$, is refuted by four independent controls: it survives destroying the temporal order of the data, is matched by a classical Bayesian baseline, and is unaffected by removing real timestamps. We trace this to the stationary structure of the model and show that it is the degeneration the theorem predicts in the absence of designed excitation. The result delineates a sharp boundary between identifiable and unidentifiable regimes and yields a validation protocol for interpretability claims.

---


### 208. [Outperformance Inverse Optimization: Learning Objective Functions that Outperform Agent Decisions](https://arxiv.org/abs/2610.09890)

**<font color=#1a73e8>作者：</font>** Akira Kitaoka  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Inverse optimization estimates the weights of an objective function that explain observed decisions as optimal solutions, and is used in a variety of fields. For mixed-integer linear programs (MILPs), existing methods aim to reproduce the observations as optimal solutions, and thus learn compromise weights when the observations are suboptimal. We propose outperformance inverse optimization, which instead seeks weights that induce, at each state, an optimal solution outperforming the observed action in every component. We give a loss function that can be evaluated with forward-problem oracles alone and is thus applicable to MILPs, together with gradient-based and DC optimization algorithms for minimizing it. For weights inducing a unique outperforming optimal solution at all observations, we prove that the probability of failing to induce such a solution at a new state (the generalization error) is bounded by a quantity inversely proportional to the number of observations, and that this bound is tight in the number of observations up to logarithmic factors. In experiments on synthetic and real data, the proposed methods improve the prediction of solutions outperforming the actions over existing methods.

---


### 209. [Love for Believable AI: Artificial Partiality and Relationship Persistence as an Engineerable Stance](https://arxiv.org/abs/2610.09895)

**<font color=#1a73e8>作者：</font>** Sebastian Cochinescu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We study a behavioral mechanism for artificial partiality in conversational agents. The paper reports no human-subjects data and makes no claim about attachment, trust, perceived mind, or machine interiority. Partiality has two components: caring, defined as allocation of a finite interaction surplus above a guaranteed per-user service floor, and particularity, defined as a per-user state estimate accumulated from relationship history on fixed inference machinery. We implement both as a persistence layer over one open-weight base model and evaluate them on constructed multi-session relationships with known hidden-state schedules. A four-channel divergence compares known-user and stranger conditions on identical probes with paired generation seeds; the stranger prompt is not length-matched, and one channel (initiative) is an allocator output rather than generated behavior. The full mechanism reproduces the ordinal shape, but not the magnitude, of an analytically specified curve and is the only arm satisfying the protocol-defined joint signature on the calibrated battery. The initial mechanism fails probe-quality equivalence because relationship content reduces topical relevance. A guarded revision satisfies equivalence on the calibrated battery but not on a second battery not used in calibration, where it scores higher than the unmodified baseline. On that second battery, the specificity margin is 0.0198, below the 0.02 protocol threshold. The paired mean right-user--wrong-user estimation-accuracy contrast is 0.375 but is not positive in every run. The mechanism is therefore a candidate for a later perception study, not evidence that users perceive love. The versioned protocol record is not independently time-stamped and is not described as a preregistration. Ethical constraints include a stranger-treatment floor, a bounded surplus, disclosure, and de-intensification.

---


### 210. [NL2Hull: A Natural Language-Driven Constrained Ship Design Decision Framework](https://arxiv.org/abs/2610.09896)

**<font color=#1a73e8>作者：</font>** Wenhua Huo, Fenglei Han, Wangyuan Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ship-form design combines smooth geometric representation, local shape editing, and constraints on the resulting hull. We present the Natural-Language-to-Hull Framework (NL2Hull Framework), which formulates ship-form editing as a typed discrete decision problem and connects language decisions to numerical geometry. Its Constrained Free-Form Deformation Engine (CFFD Engine) represents hull waterlines with non-uniform rational B-splines (NURBS), applies free-form deformation (FFD) to their control points, reconstructs the hull, and checks geometric constraints. We construct the Ship Design Decision Dataset (SDD Dataset) with 134,558 cleaned records and evaluate compared models on its subset Ship Design Decision Benchmark (SDDBench), containing 5,000 records and 43,496 typed questions. We propose Chip, a constrained ship-design decision model for processing natural-language requests. Chip reaches 95.90\% question accuracy and 99.32\% FFD exact match, with a negative log-likelihood of 0.0951, an expected calibration error of 0.0032, and a Brier score of 0.0551. The NL2Hull Framework provides a reproducible interface for evaluating language-based ship-form decisions while identifying the geometry and continuous-control components that require further development. Our code and dataset is available at this https URL.

---


### 211. [A Scale For Value Alignment In Human-AI Interaction](https://arxiv.org/abs/2610.09911)

**<font color=#1a73e8>作者：</font>** Lena Hegemann, Steeven Villa, Hyemin Bang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Value alignment is a central objective in AI and HCI research, yet no validated instrument measures how users perceive it. This gap hampers the comparison and accumulation of findings and limits the effectiveness of applications, where understanding users' viewpoints is critical. We construct and evaluate a 13-item psychometric scale that measures perceived value alignment across two components: value understanding and value manifestation. It is based on a large item pool drawn from prior empirical studies, filtered by experts, and finally assessed by users (N=607) across diverse AI scenarios. Confirmatory factor analysis on an independent sample (N=259) confirmed the two-factor structure and high internal consistency for both subscales. Using optimization, we also derived a 6-item short form for quick administration. The scale is a reliable measure, providing HCI researchers with a common evaluation metric across contexts.

---


### 212. [NeuralZip: Reusable Setup for Fast Lossless Compression](https://arxiv.org/abs/2610.09916)

**<font color=#1a73e8>作者：</font>** Martín Bravo, Samuel Horváth, Gonzalo Navarro 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Lossless compression can reduce the storage and movement of model weights without changing their floating-point values, but repeated statistical analysis and code construction add computational overhead. We study whether the statistical structure of exponents can be prepared once and reused. For this, we introduce NeuralZip, which groups chunks with similar exponent distributions, shares Huffman codes, and selectively represents recurring exponent tuples using packed exponents, thereby achieving additional moderate compression ratios. A setup chooses these representations before subsequent encodings, while every encoding still processes the current tensor values. In floating-point model checkpoints, post-setup compression is 1.81-21.33$\times$ faster than the baselines and achieves exact bit-to-bit reconstruction. We show that this setup can be precomputed and transferred from another compatible architecture, preserving similar compression ratios and avoiding the need to amortize setup costs. Therefore, compression adaptation is transferable and reusable. Training checkpoints demonstrate continued reuse as the weights evolve. Finally, GPU experiments reduce active memory usage by up to 27.5$\%$ while reproducing the logits exactly.

---


### 213. [CYBERFORT: A Compliance-Chain Platform Operationalising the Cyber Resilience Act for SMEs](https://arxiv.org/abs/2610.09918)

**<font color=#1a73e8>作者：</font>** Nikolaos Kekatos, Georgios Koutidis, Mihaela Curcă 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The EU Cyber Resilience Act (CRA) turns product cybersecurity into a lifecycle compliance obligation for manufacturers, importers, distributors, and integrators of products with digital elements on the EU market, a load that falls largely on small and medium-sized enterprises (SMEs) that rarely have dedicated governance, risk, and compliance (GRC) capacity. We present CYBERFORT, an open-source CRA-first compliance platform developed under the EU Digital Europe Programme and one of twelve projects in the EU CRA cluster. CYBERFORT operationalises the CRA through a guided scope self-assessment, a question bank tied to Annex I and the vulnerability-handling obligations, and a compliance-checking engine that links every answer to controls, policies, and machine-attested evidence, reusing ISO/IEC 27001, NIS2, and GDPR controls only where they coincide with CRA obligations. Its central contribution is the compliance chain, a traceable structure linking each product risk through its controls and policies to the CRA obligations it satisfies, and onward through evidence to the technical-documentation file and EU declaration of conformity, so that every operational gap is traceable and can be closed before market placement. Deployed at this https URL for a first cohort of 43 organisations, the platform is presented with the engineering behind the chain, measured results from a completed end-to-end case study on a SIEM/XDR product with AI-driven remediation spanning the CRA obligation chapters, and the controlled effort study that remains in progress.

---


### 214. [Eigenvalues of the Hessian in Deep Learning: The Origin of Symmetry and Its Breaking](https://arxiv.org/abs/2610.09919)

**<font color=#1a73e8>作者：</font>** Yossi Arjevani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hessian spectra at trained models in deep learning exhibit a persistent pattern: eigenvalues organize into distinct clusters, including a large bulk near zero and a few isolated outliers. This paper shows that a natural account of these spectral phenomena emerges when the original setting is understood as a departure from a nearby, otherwise hidden, highly symmetric reference.
Modifications, including changes to the architecture, data distribution, or parameter metric, expose a nearby reference configuration whose Hessian exhibits rich invariances-ones not accounted for by weight symmetries. There, symmetry enables a precise description of the spectra, forcing high-dimensional kernels and eigenvalues of large multiplicity. Returning to the original configuration breaks the Hessian symmetry and thereby produces the observed hierarchy of clusters and outliers.
The framework is developed in some generality, with a detailed analysis of three-layer ReLU networks and applications to convolutional, graph, and transformer models, as well as to the NTK. The same mechanism is further shown to yield analogous spectral structures in layerwise Hessians and the Gauss-Newton matrix.

---


### 215. [KGATE : a Knowledge Graph Embedding Training Environment](https://arxiv.org/abs/2610.09927)

**<font color=#1a73e8>作者：</font>** Benjamin Loire, Galadriel Brière, Célia Brahimi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge graph embedding (KGE) models encode the entities and relations of a knowledge graph into a low-dimensional latent space, enabling tasks such as classification or link prediction. Most KGE models follow an autoencoder architecture, in which an encoder projects the knowledge graph into the latent space and a decoder reconstruct it. Combining both encoder and decoder components is increasingly needed, yet existing libraries rarely support complete autoencoders, are often unmaintained, rely on undocumented default hyperparameters, and produce results that cannot be compared across libraries. Here we present KGATE (Knowledge Graph Autoencoder Training Environment), a modular Python library built on PyTorch Geometric and TorchKGE. KGATE lets users assemble initializers, encoders, decoders, losses, negative samplers, and evaluation metrics as building blocks, or plug in their own block. KGATE includes a preprocessing procedure that controls data leakage, a builtin training pipeline, and reproducibility by design. Benchmarks against six existing KGE libraries show that KGATE training time is comparable with the fastest libraries while offering a broader set of features.

---


### 216. [Do Generative Priors Align with Human Naturalness Perception?](https://arxiv.org/abs/2610.09928)

**<font color=#1a73e8>作者：</font>** Taiki Fukiage  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual generative models are trained to capture the probability distributions of natural images, yet whether their native priors reflect the regularities governing human perception of image naturalness remains an open question. Here, we probe these priors through native prediction errors across 25 open image and video generators. Because raw single-image losses are dominated by scene content and visual complexity, we evaluate directional loss differences using content-preserving, paired relational interventions that selectively disrupt facial configurations or physical illumination consistency while limiting changes in low-level image statistics. Across both domains, these loss differences reproduce human-like selective sensitivities and tolerances, capturing the classic Thatcher effect on faces and shape-dependent responses to illumination inconsistencies. Notably, these loss differences reliably track continuous gradations of human naturalness judgments across individual stimulus pairs (peaking at $r = .84$ on faces and $.64$ on physical scenes) and retain unique human-aligned signals even after controlling for feature distances from frozen vision encoders and standard image quality metrics. We also find that while overall sensitivity to these violations broadly covaries with human alignment across models, the two systematically decouple along denoising schedules, with alignment peaking earlier than sensitivity, revealing that human-like naturalness judgments dissociate from generic violation detection. Together, these findings demonstrate that learning visual distributions yields generative loss landscapes that capture distinct aspects of human naturalness perception.

---


### 217. [Expected Sample Complexity in Multi-Armed Bandits](https://arxiv.org/abs/2610.09929)

**<font color=#1a73e8>作者：</font>** Nadav Sukenik, Nadav Merlis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sample complexity is a widely used metric in sequential decision-making problems, defined as the number of suboptimal decisions during the interaction between the agent and an environment. We study the sample complexity of stochastic multi-armed bandit problems and introduce the expected sample complexity performance measure, analyzing it in a novel framework called approximately correct in expectation (ACE). We show that ACE guarantees imply almost sure convergence to the optimal expected reward, in contrast to high-probability guarantees found in other frameworks, and also show how to convert ACE guarantees into explicit expected regret bounds. We further show that, in contrast to existing measures, deterministic algorithms cannot obtain favorable ACE bounds, and analyze stochastic algorithms in two settings: when the allowed suboptimality level $\epsilon$ is known to the algorithm and when it is unknown. In the former, we devise an explore-then-$\epsilon$-greedy algorithm, and in the latter, we analyze the expected sample complexity of Thompson sampling. Finally, we establish nearly matching lower bounds for both settings, showing that the algorithms are tight in $\epsilon$ and proving a performance separation between the two regimes.

---


### 218. [Itgan at NADI 2026 shared task: Parameter-Efficient Whisper Adaptation for Robust, Mixed-Dialect and Code-Switched Arabic ASR](https://arxiv.org/abs/2610.09934)

**<font color=#1a73e8>作者：</font>** Ibrahim Almajai  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We describe the Itgan systems for the three ASR subtasks of NADI 2026, namely robust country-level ASR (1.1), mixed-dialect ASR (1.2), and Tunisian code-switched ASR (1.3). All three share one recipe, Whisper adapted with LoRA on consumer GPUs, and each was carried by a different addition to it. On 1.1, where the dialect label is given at test time, per-dialect specialists continued from a pooled adapter gave the largest gain, and the submitted system reached 57.1% country-average WER. A post-evaluation linear probe on frozen encoder features routes utterances without the label and recovers 44% of what oracle routing gives. On 1.2 the choice of base model mattered more than adapter capacity, and system combination helped only once we added a decorrelated member, reaching 46.7% WER. On 1.3 our system placed second at 14.49% WER with the lowest CER among the leading submissions, 5.38%. Its last 0.60 WER points came without further training, mostly from an exact weight-space average of independently trained runs, with ROVER voting adding the remainder. Every comparison carries a paired-bootstrap test, and we report eight directions that did not work.

---


### 219. [Learning Traffic Flow Dynamics with Stochastic Physics-Informed Neural Cellular Automata](https://arxiv.org/abs/2610.09946)

**<font color=#1a73e8>作者：</font>** Federica Bragone, Matthieu Barreau  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traffic flow modeling is essential for understanding and predicting the collective dynamics of vehicles on road networks. Cellular automata provide a simple, interpretable yet powerful framework for representing these dynamics via local interaction rules, while retaining the ability to reproduce complex macroscopic traffic phenomena. However, learning local transition rules from data while preserving physically meaningful constraints remains challenging, particularly for stochastic models. In this work, we propose a physics-informed neural cellular automaton (PI-NCA) for data-driven traffic flow modeling. Building on the standard neural cellular automaton (NCA), we design a neural architecture that is physically consistent with the road topology and guarantees conservation of the total number of vehicles, thereby constraining the learned transition rules to physically admissible dynamics. We further extend this framework to stochastic dynamics by parameterizing probabilistic transition rules while preserving the same physics-informed constraints. We evaluate the proposed models on multiple traffic scenarios generated by the well-established Nagel-Schreckenberg and Kerner-Klenov-Wolf cellular automata. The results demonstrate that the PI-NCA successfully learns the dynamics of both traffic models and consistently outperforms a standard NCA, while the stochastic extension captures probabilistic transition rules without compromising the imposed physical constraints.

---


### 220. [Force without transmission: a depth-induced rank collapse that no loss on the representation reopens](https://arxiv.org/abs/2610.09958)

**<font color=#1a73e8>作者：</font>** Martin Hofmann, Patrick Mäder  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training can drive a transformer into a rank collapse: all token representations point in one direction, and learning stops. In a related collapse of attention, a loss term with a bounded corrective force repairs the network during the run. We ask whether such a term repairs rank collapse. We collapse small transformers by weakening their skip connection and treat copies of the collapsed network. No added loss term repaired the collapse, although the stronger kind pushed with about a tenth of the task gradient. The reason was the path, not the strength. The task gradient no longer reached the query and key weights, which decide where attention looks, and the added term's gradient faded before the blocks where the collapse forms. Restoring the skip connection, which changes no weight, reopened this path at once. The rank then recovered, but only far above the scale of collapse. After a burst of high learning rate the path stayed open and the rank recovered untreated. Registered predictions from the path ranked recovery times but did not transfer to this cause. In every case the loss stayed above that of a healthy network after the rank recovered. Whether a collapsed network can be repaired depends on whether the gradient still reaches the weights that must change, not on how strongly a loss term pushes.

---


### 221. [TR-PTQ: High-Accuracy Integer-Only Transformer Post Training Quantization via Taylor Region Reformulation](https://arxiv.org/abs/2610.09969)

**<font color=#1a73e8>作者：</font>** Eliyahu Levy, Adam Teman, Yoni Pugachov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training quantization (PTQ) enables efficient deployment, yet transformer architectures remain challenging to quantize due to nonlinear layers. While existing methods attribute accuracy loss to insufficient numerical precision, often necessitating floating-point fallbacks, we demonstrate that degradation is actually driven by specific structural error sources. We find that learned scale parameters in normalization layers and compounded approximations in GELU are the primary error contributors, whereas SoftMax remains inherently robust to aggressive quantization. To address these bottlenecks, we introduce TR-PTQ, a unified integer-only formulation using shared Taylor Region (TR) exponential and logarithm primitives. This approach allows computationally expensive operations, including division and square roots, to be performed entirely in the log-domain via standard integer arithmetic. Combined with a calibration-free, outlier-aware optimization for LayerNorm parameters, our method eliminates the need for floating-point hardware units for nonlinearities, achieving less than 1.5\% absolute accuracy degradation across vision and language benchmarks.

---


### 222. [Efficient Patch-Based Anomaly Detection Fused with Diffusion Driven Generative Modeling for Semiconductor Wafer Bin Map Open Set Anomaly Detection](https://arxiv.org/abs/2610.09993)

**<font color=#1a73e8>作者：</font>** Limon Bin Hossain, Md Sadib Rahman Ananta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatial defect signatures on wafer bin maps (WBMs) trace yield loss to specific process faults, yet supervised classifiers recognize only the defect types seen during training, and one-class detectors built on a single mechanism tend to capture either local structural deviations or global distributional violations, but rarely both. This work proposes a hybrid one-class framework that couples a patch-based student-teacher detector (EfficientAD) with a denoising diffusion probabilistic model (DDPM) used for partial-diffusion reconstruction, and fuses their percentile-calibrated scores through a fixed convex combination. Trained on only 700 normal wafers from the WM-38K mixed-type dataset and evaluated on 18,658 held-out wafers, the fused detector reached an AUROC of 0.9985 and reduced misclassifications from 852 (DDPM) and 1,412 (EfficientAD) to 618, with all pairwise differences significant at p < 0.001. Beyond aggregate accuracy, the analysis shows that the gain arises from weakly overlapping errors between the two modules, yet fixed-weight fusion recovers only 40-70% of the correction available to an oracle selector. Under the benchmark's inverted class balance, average precision and F1 saturate, while the Matthews correlation coefficient and negative predictive value expose unreliable normal predictions. Pixel-level maps further show that strong image-level separability does not imply spatial localization, and the diffusion module succeeds as a local density prior rather than through global geometric reasoning. These findings motivate sample-adaptive fusion and imbalance-aware evaluation of hybrid wafer anomaly detectors.

---


### 223. [Temporal Predictive Multiplicity: Equally Accurate Time Series Models Yield Different Forecast Trajectories](https://arxiv.org/abs/2610.09994)

**<font color=#1a73e8>作者：</font>** Emanuele Albini, Francesca Toni, Saumitra Mishra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Models with near-identical predictive performance can yield substantially different predictions, a phenomenon known as predictive multiplicity. Prior work has mostly studied this at the level of individual scalar outputs. In time-series forecasting, however, predictions across horizons jointly define a trajectory, and horizon-wise comparisons can hide important differences in predictive behavior. To address this problem, we introduce temporal predictive multiplicity, a framework that characterizes disagreement over complete forecast trajectories among models with near-identical predictive performance. We show that constraining predictive performance alone can still admit a broad range of different trajectories. We further show that constraining multiplicity at individual horizons partially reduces, but does not eliminate, trajectory-level multiplicity. Experiments with 19 neural forecasting architectures on 11 datasets confirm that near-optimal models can exhibit substantial variability in the forecast trajectories they produce, and trajectory-level disagreement is largely unrelated to horizon-wise disagreement. Our framework, therefore, exposes a gap in existing multiplicity studies: models with indistinguishable predictive performance imply fundamentally different temporal trajectories, with consequential downstream effects.

---


### 224. [Beyond Reward Suppression: Near-Optimal Offline Attacks on Warm-Start Bandits with Bounded Rewards](https://arxiv.org/abs/2610.10000)

**<font color=#1a73e8>作者：</font>** Qirun Zeng, Manhin Poon, Xiangxiang Dai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adversarial attacks on bandits aim to mislead a learner toward a target arm while keeping the attack cost small. Existing attacks typically achieve this by suppressing non-target arms. In practice, however, manipulation such as fake reviews often directly promotes the target item. We study this gap through bounded offline attacks on warm-start bandits, where an attacker can inject only valid action-reward pairs into the warm-start history before deployment. We show that target promotion is not merely a heuristic: when the target arm lies near the lower reward boundary, any order-optimal-cost attack against UCB that makes it selected in nearly all online rounds must allocate a nonvanishing fraction of its cost to the target arm. We then design an attack that achieves the optimal sublinear cost and characterize its allocation between target promotion and non-target suppression. We further extend the attack to Thompson Sampling, $\epsilon$-greedy, and a broader class of bandit algorithms. Experiments on real-world and synthetic data validate the effectiveness of our attacks.

---


### 225. [Perceptually Aligned Evaluation of Style Transfer](https://arxiv.org/abs/2610.10003)

**<font color=#1a73e8>作者：</font>** Yang Deng, Eleftherios Ioannou, David Mould 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Style transfer lacks a reliable evaluation standard: ground truth is inherently ill-defined, and existing automatic metrics often fail to reflect human preference. This paper introduces ASTRA (Assessment of Style TRansfer Algorithms), an approach for automatic evaluation of style transfer algorithms; it contains two components, ASTRA-Data and ASTRA-Score. ASTRA-Data consists of a benchmark image set of content and style references, a collection of style transfer results generated on the benchmark set, and user study data capturing human judgements through a two-stage pairwise comparison protocol. From these annotations, we derive ranking-based ground truth for content preservation, style fidelity, and overall preference. Based on ASTRA-Data, we construct ASTRA-Score, a learnt evaluator that predicts preference-aligned scores from content-style-stylization image triplets, enabling automatic and scalable evaluation of new models applied to the benchmark set. Experimental results demonstrate that ASTRA-Score achieves substantially higher correlation with human rankings compared to prior metrics. Overall, ASTRA establishes a robust mechanism for standardised evaluation of style transfer methods.

---


### 226. [Defining Purpose-Limited Secrets](https://arxiv.org/abs/2610.10010)

**<font color=#1a73e8>作者：</font>** Bhumika Mittal, Aalok Thakkar  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A cryptographic secret is issued for a purpose but grants a capability, and the capability is usually larger: a decryption key meant for computing aggregates can read every record, and a token meant to pay one invoice can drain the account. Deployed systems state the purpose in policy and enforce only the capability. We make the purpose a property of the secret. A mechanism sees operations, not reasons, so a scheme enforces an admissible set $A(P)$ of operations that stands in for a declared intended use $I$; whether $I$ captures the human purpose is a modeling obligation that marks where policy takes over. Against the same $I$ we define three regimes: under confinement an operation outside the intended use is infeasible, under mediation a trusted component refuses it, and under accountability use beyond a stated bound is possible but attributed to the holder. The confinement games, for unpredictability and indistinguishability, coincide with the key-query forms of functional-signature unforgeability and constrained-PRF pseudorandomness and correspond to simulation-secure functional encryption within its feasibility boundary; stated against $I$, they also register a predicate that permits too much. A payment token uses all three regimes on one secret: it pays one capped charge at one merchant, can be narrowed but not widened, is checked by the merchant, and identifies the withdrawing account if spent twice. Attenuation unforgeability reduces to unforgeable signatures and a collision-resistant hash without random oracles; traceability and non-frameability hold under discrete log and unforgeable signatures in the random-oracle model. We claim no new primitive, hardness assumption, or general composition theorem; the framework is a common specification against which such primitives are stated and compared.

---


### 227. [Playing with Kruskal: algorithms for flat and hierarchical watershed cuts](https://arxiv.org/abs/2610.10012)

**<font color=#1a73e8>作者：</font>** Jean Cousty, Laurent Najman, Benjamin Perret 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In the framework of edge-weighted graphs, watersheds have proven to be linked to well-known optimization problems, as Minimum Spanning Tree, which allowed the design of efficient algorithms for computing (hierarchical) watershed segmentations. In the present article, after reviewing the literature related to watershed segmentation, we present a detailed end-to-end pipeline of algorithms to compute (hierarchical) watershed segmentations, starting from the computation of graph-based image representations, up to the computation of connected components of the final (hierarchical) segmentation. We consider the several variations of watersheds, including their supervised and unsupervised versions, and the various ways of computing seeds, to name a few. For the first time, we bring together all these watershed notions and algorithms in a compact and understandable way. We aim at providing a reference for those interested in employing and reimplementing the watershed segmentation framework for their task at hand.

---


### 228. [Scalable Patch-Level Self-Supervised Learning](https://arxiv.org/abs/2610.10013)

**<font color=#1a73e8>作者：</font>** Maximilian Seitzer, Gabriele Trivigno, Antonín Vobecký 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning (SSL) at scale produces powerful visual representations. However, most scalable SSL methods rely on ad hoc combinations of multiple objectives and stabilization mechanisms. Taking a step back, we ask if we can design a high-performing, yet principled SSL algorithm. Starting from the multi-view assumption, stipulating that task-relevant content is captured by the information common to different views, we construct an information-theoretic objective decomposing into interpretable terms. This derivation yields JEM, a student-teacher method that learns by aligning corresponding patch representations across views, explicitly regularized by information and structure preservation losses. JEM trains stably from 300M to 7B parameters, and, to our knowledge, is the first latent-space patch-level method demonstrated at 7B scale. Across all scales, JEM reaches strong performance on both global and dense probing tasks, on segmentation benchmarks consistently surpassing the DINOv2 algorithm, an influential foundation for today's strongest visual SSL methods. Notably, at 7B parameters, it exceeds the performance of DINOv3 on panoptic segmentation, despite being trained on $12\times$ less data without refinement stages. These results demonstrate that we can indeed design an SSL algorithm that learns strong representations, is principled and stable.

---


### 229. [A Drosophila Whole-Connectome Network Can Learn Human-Designed Cognitive Tasks](https://arxiv.org/abs/2610.10014)

**<font color=#1a73e8>作者：</font>** Joonghui Cho, Minchan Kang, Daeshik Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can a biological wiring diagram serve as a useful computational substrate beyond the behaviors for which it evolved? We use the publicly released MaleCNS v1.0 connectome, reconstructed from a single adult male Drosophila specimen, as the fixed recurrent topology of an artificial network. We train separate models for bounded addition and for a controlled grounded relational language task built from a fixed 100-word lexicon. In both models, one scalar is learned per anatomical edge. The anatomical graph reaches 92.77% mean accuracy on held-out addition, compared with 67.93% for directed degree-preserving rewires. On the strict paired language endpoint, which matches original and order-reversed scenes to their corresponding descriptions, it reaches 61.59% across four fixed interfaces, compared with 44.17% for matched rewires. At the canonical interface, it ranks first in a fixed 21-graph comparison. On the matched 48-group intervention subset, shuffling task-defined sensory features reduces its score from 60.94% to 19.27%. Together, these results show that higher-order MaleCNS wiring provides a reusable inductive bias for bounded addition and grounded relational language.

---


### 230. [What the Sleeve Feels: Explainable Machine Learning for Textile Pressure-Based Postural Screening](https://arxiv.org/abs/2610.10015)

**<font color=#1a73e8>作者：</font>** Limon Bin Hossain, Md Sadib Rahman Ananta  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Pressure-sensing smart textiles convert body-surface contact into a dense, image-like signal closely tied to posture and movement, making them a promising low-cost route to wearable posture screening. Realizing that promise, however, requires more than classification accuracy: a deployable system must generalize to wearers unseen during training, expose the physical evidence behind its decisions, and tolerate the small donning offsets that occur whenever a garment is removed and re-worn. This paper addresses these three requirements jointly using a knitted piezoresistive sleeve worn on the forearm as a testbed. We regroup fine-grained everyday activities into three coarser screening categories (neutral, potentially undesirable, and functional or transitional), engineer 29 interpretable pressure-distribution features spanning global intensity, spatial center of pressure, quadrant asymmetry, distribution complexity, and short-horizon temporal change, and evaluate under a strict subject-wise split. A tuned XGBoost classifier reaches 0.818 accuracy, 0.788 balanced accuracy, and 0.801 macro F1 on unseen test subjects, with tight frame-level bootstrap 95% intervals of about plus-minus 0.01 and a subject-to-subject standard deviation near 0.06 under leave-one-subject-out cross-validation. A simple 2D-CNN baseline trained on raw frames achieves broadly similar performance, showing that hand-engineered features are not left behind by a learned spatial representation on this task. SHAP-based explanation, a feature-group ablation, per-activity error analysis inside the pooled undesirable class, class-mapping sensitivity, and a simulated donning-rotation stress test together locate what the model relies on, where it degrades, and why, directly targeting the generalization, interpretability, and robustness gaps that determine whether such a system is deployable.

---


### 231. [Oscillatory Neural Dynamics over Sheaves](https://arxiv.org/abs/2610.10018)

**<font color=#1a73e8>作者：</font>** Jan-Willem Van Looy, Alessandro Trenta, Alessio Gravina 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Effective long-range propagation remains a central challenge in graph neural networks, as increasing a model's propagation depth does not guarantee that distant nodes effectively influence each other. Sheaf neural networks enrich graph propagation through matrix-valued transport between stalks; still, this expressivity alone does not automatically imply effective long-range communication. We introduce ONDA, a long-range graph learning framework based on operator-valued information waves. Stalk-valued representations evolve through second-order dynamics governed by learned sheaf transport operators, combining wave-like propagation with expressive local geometry. We characterize long-range influence through a stalk-wise sensitivity analysis and show that the cross-influence never vanishes. Across long-range propagation, severe graph bottlenecks, graph transfer, and heterophilic benchmarks, ONDA consistently improves over scalar wave propagation, diffusive sheaf baselines, and state-of-the-art models, demonstrating the benefit of coupling wave dynamics with matrix-valued transport.

---


### 232. [Matching of signal, noise and hardware timescales for filtering and forecasting of correlated noise signals](https://arxiv.org/abs/2610.10037)

**<font color=#1a73e8>作者：</font>** Joshua Donald, Alex Gabbitas, Arthur G. T. Coveney 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physical reservoir computing exploits the nonlinear dynamics of physical systems to process time-dependent data with greater energy efficiency than conventional machine learning approaches. However, physical reservoirs have fixed intrinsic response timescales, whereas real-world signals combine deterministic and stochastic components across multiple timescales. Here we show, using a nanoporous niobium oxide reservoir, synthetic noisy signals and cryptocurrency-price volatility, that the relationship among noise correlation time, reservoir memory and forecast horizon determines whether correlated noise is filtered or predicted. Noise varying faster than the relevant reservoir memory and forecast horizon is averaged by the reservoir, whereas the temporal structure of slower-varying noise is sufficient for algorithmic forecasting. We introduce the reservoir memory horizon and forecasting regime index to distinguish these operating regimes. These contributions demonstrate that timescale matching can guide the encoding of input time series and development of physical reservoir architectures that filter, analyse and predict stochastic signal components across distinct temporal scales.

---


### 233. [AdSpark: A Large-Scale Dataset and Benchmark for Product-Centric Advertisement Video Generation](https://arxiv.org/abs/2610.10047)

**<font color=#1a73e8>作者：</font>** Zhifei Yang, Zhao Jiang, Keyang Lu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Product-centric advertisement video generation aims to create promotional videos that preserve fine-grained product identity while presenting selling points through coherent multi-shot narratives. However, this emerging task remains underexplored due to the lack of large-scale advertisement-specific datasets and comprehensive evaluation frameworks. To address this gap, we introduce \textbf{AdSpark}, a large-scale dataset and benchmark for product-centric advertisement video generation, based on data from a major e-commerce platform. \textit{AdSpark-300K} contains approximately 300K reference image--prompt--video triplets, comprising a real-world subset and a synthetic subset. Each sample provides structured advertisement annotations, including product identity annotations, selling-point descriptions, creative plans, and aligned audio scripts, enabling models to learn product preservation and advertisement-oriented visual storytelling. We further propose \textit{AdSpark-Bench}, a diagnostic benchmark that evaluates generated advertisements across six dimensions, including visual quality, product fidelity, instruction adherence, temporal coherence, audio alignment, and advertisement effectiveness. Based on AdSpark-Bench, we evaluate representative models, revealing key challenges in product preservation, multi-shot storytelling, and selling-point visualization. Experiments with AdSpark-300K-finetuned models further validate the effectiveness of our dataset. AdSpark provides a unified dataset and benchmark for future research, and we will release the dataset upon acceptance.

---


### 234. [BetweenCut: Private Heavy-Node Classification with Doubly Logarithmic Error in Tree Height](https://arxiv.org/abs/2610.10075)

**<font color=#1a73e8>作者：</font>** Ergute Bao, Graham Cormode, Xiaokui Xiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Finding heavy nodes in a tree---those whose counts exceed a given threshold---is a building block for analysis and learning over structured data. Achieving record-level differential privacy (DP) without sacrificing accuracy is challenging because each record contributes to counts along an entire root-to-leaf path, allowing privacy costs to accumulate across levels. Existing methods account for the multiple threshold comparisons for each record incur additive error margins of $\Omega_{\varepsilon,\delta}(\log h)$ or $\Omega_{\varepsilon,\delta}(\sqrt{\log h})$ for tree height $h$. We introduce \textsc{BetweenCut}, an $(\varepsilon,\delta)$-DP algorithm with an additive error margin of $O_{\varepsilon,\delta}(\log\log h)$, improving the existing bounds for deep trees. This error holds simultaneously for all nodes and is independent of the input database size.

---


### 235. [Multi-Agent Coordination via Support-Preserving Distillation](https://arxiv.org/abs/2610.10087)

**<font color=#1a73e8>作者：</font>** Sangmin Lee, Youngju Na, Chanmi Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline MARL increasingly relies on generative policies to model multimodal joint behavior, typically by distilling a centralized teacher into decentralized one-step actors under the CTDE. We identify a failure mode at the teacher training stage: standard flow-based teachers pair noise with replay targets independently, so nearby noise samples can be routed toward conflicting coordination modes. The teacher then produces samples between valid modes, and because the distillation loss regresses each local actor onto the conditional mean of the teacher's output given local input, this error is not absorbed but propagated to the student. To remove this teacher-side artifact, we propose Mode-Support Semi-Discrete Optimal Transport (MoSDOT), which summarizes multimodal replay into a finite mode support with prescribed capacities and uses conditional semi-discrete optimal transport to assign each noise sample to a single mode before teacher training. We additionally study a shared-randomness variant that uses a shared noise component at execution to expose the residual gap intrinsic to strict-product execution. On controlled diagnostics and offline MARL benchmarks, MoSDOT improves endpoint quality and routing consistency, particularly on datasets exhibiting multimodal joint behavior.

---


### 236. [SkillSandbox: Skill Verification via Dynamic Scenario Synthesis](https://arxiv.org/abs/2610.10088)

**<font color=#1a73e8>作者：</font>** Serin Kim, Kwangwook Seo, Dokyung Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-evolving agents distill task-solving experience into skills for future reuse, but these skills can encode incorrect procedures or non-transferable knowledge. It is therefore critical to verify each skill's reusability: whether its guidance remains useful beyond the experience from which it was distilled. Such verification requires observing how a skill affects execution in new tasks, yet existing tasks may not expose the situations where the target skill can actually be exercised. To construct such situations, we propose SkillSandbox, a framework that dynamically synthesizes a task and its environment for each skill that are skill-relevant yet novel. A Proposer specifies the conditions to preserve and the source-specific details to vary, a Builder constructs an executable scenario, and a Verifier compares executions with and without the skill. The Verifier assesses executability, utility, and efficiency to assign a Keep or Reject verdict, determining whether the skill enters the library. Across ALFWorld and WebShop with three models, SkillSandbox consistently yields the strongest downstream performance and improved execution efficiency. Further analyses examine whether these gains reflect accurate assessment of skill reusability and identify which components of SkillSandbox contribute to them.

---


### 237. [Temporal Residual Bottleneck for Robust Asynchronous Collaborative Perception](https://arxiv.org/abs/2610.10090)

**<font color=#1a73e8>作者：</font>** Melih Yazgan, Ahmed Abouelazm, J. Marius Zöllner  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Collaborative perception extends the sensing range of autonomous vehicles, but its performance degrades when shared features arrive stale or incomplete. Most latency-robust methods compensate delayed collaborator features through flow-guided alignment or direct feature transport. In this work, we formulate asynchronous collaborative perception as temporal residual prediction. Our Temporal Residual Bottleneck keeps a deterministic pose-warped collaborator feature as a conservative anchor and uses a $\Delta t$-conditioned xLSTM to extract residual temporal evidence from the available history. A detector-facing residual bottleneck then applies only gated, regularized corrections before ego-side fusion, reducing the risk of overwriting reliable static structure when temporal correspondence is uncertain. Experiments on DAIR-V2X and OPV2V show that our method is especially effective under severe fixed/irregular delays and packet drops. On DAIR-V2X, the reported checkpoint trades a small amount of synchronized peak accuracy for better robustness under stronger communication degradation. Controlled diagnostics further indicate that direct feature transport has oracle headroom but can become unreliable when deployed without accurate correspondence. These results support temporal residual fusion as a practical alternative for asynchronous and incomplete collaborative perception. Code will be publicly released at this https URL.

---


### 238. [ExperienceIndex: Artifact-Grounded Memory](https://arxiv.org/abs/2610.10091)

**<font color=#1a73e8>作者：</font>** Peter Baile Chen, Geoffrey X. Yu, Xinming Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge-intensive tasks require answering many questions by reasoning about a shared corpus of artifacts (e.g., court cases, or scientific literature). As humans interact with these corpora, they naturally accumulate experiential knowledge about artifacts, enabling them to quickly identify the complete set of relevant artifacts for each new task. However, existing AI agents lack appropriate memory solutions to build or reuse such artifact-grounded experience, leading to lower answer quality and higher online cost. Existing memory solutions extract and reuse information from prior task-solving traces, but they primarily focus on user preferences, factual attributes, or abstract reasoning patterns rather than persistent artifact-specific knowledge. We introduce ExperienceIndex, a novel experience layer for AI agents that captures and reuses knowledge about artifacts based on prior reasoning traces. ExperienceIndex stores two complementary forms of experience: (i) single-artifact experiences that summarize an artifact's contribution to prior tasks and (ii) artifact-pair experiences that encode structural relationships discovered during past reasoning. Integrated as lightweight middleware, ExperienceIndex uses an experience retrieval mechanism to guide agents toward the complete set of relevant artifacts for new tasks, improving both answer quality and efficiency. Across diverse corpora and agentic solutions with different search frameworks, ExperienceIndex delivers consistent gains, raising answer quality by up to 11.0 points and reducing online dollar cost by up to 50.5%. We further demonstrate two benefits: (i) cross-task generalization, where experiences accumulated from text-to-SQL tasks transfer to factoid QA tasks over the same artifact corpus, and (ii) teacher-student learning, where experiences from a stronger model enable a weaker model to reach comparable performance.

---


### 239. [The Cost of Classical Multi-Agent Path Finding](https://arxiv.org/abs/2610.10100)

**<font color=#1a73e8>作者：</font>** Alvin Combrink, Sabino Francesco Roselli, Martin Fabian  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-Agent Path Finding (MAPF) is the problem of planning conflict-free paths for multiple agents in a shared space, each from its start to its goal. Classical MAPF has been the dominant formulation for many years, with its assumptions of discrete time and graph-based conflicts presumably easing the search for solutions. These assumptions limit the physical environments and agents for which a solution is truly collision-free, and also place an upper bound on solution quality that no algorithmic improvements can lift. This work investigates how much solution quality, and in what contexts, the classical MAPF formulation forfeits. Continuous-time MAPF (MAPF$_R$) relaxes these assumptions, making it a natural counter-formulation to compare against across various agent counts and sizes, and graph connectedness, topologies, and resolutions. We find that continuous time and agent shape consideration are worth relatively little on their own; their value comes from enabling an expanded range of move actions, on average improving solution quality by at least $5\%$ on narrow and constrained maps and $17\%$ on maps with open spaces. In some cases, the improvements exceed $20\%$. Doubling the map resolution with classical MAPF recovers less than $3\%$, meaning that little of what is forfeited can be bought back through more compute. This work therefore provides insight on when classical MAPF is a reasonable simplification, and when MAPF$_R$ unlocks significantly higher-quality solutions.

---


### 240. [CAFE+FNO: Fourier Kernel Generation via Multiplicative Feature Composition](https://arxiv.org/abs/2610.10105)

**<font color=#1a73e8>作者：</font>** Hyungjoon Juen, Minwoo Shin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Fourier Neural Operator (FNO) learns solution operators of partial differential equations (PDEs) through Fourier-space kernel parameterization, but frequency truncation can limit the learning of high-frequency variations. AM-FNO and SirenFNO generate kernels for all grid modes from spectral coordinates using shared networks, making coordinate encoding and generator design important. Recent work on implicit neural representations (INRs) has proposed constructing frequency interactions through explicit feature composition rather than relying on subsequent MLPs to form them implicitly. Building on this approach, we propose CAFE+FNO, which incorporates Content-Aware Frequency Encoding+ (CAFE+) into Fourier kernel generation. CAFE+ combines Fourier--Chebyshev features through parallel affine branches and a Hadamard product, forming interactions within and across the two feature families. A kernel MLP maps the resulting representation of each normalized spectral coordinate to a complex channel-mixing matrix. Each layer shares its generator across all stored modes, making the number of trainable parameters independent of the number of modes for a fixed architecture. We compare CAFE+FNO with existing FNO variants on five PDE benchmarks and conduct ablation studies on basis configuration, multiplicative composition, and bandwidth learnability. Code and experimental configurations are available at this https URL.

---


### 241. [A Probabilistic Perspective on Wasserstein-Based Evidential Uncertainty for Out-of-Distribution Segmentation](https://arxiv.org/abs/2610.10116)

**<font color=#1a73e8>作者：</font>** Arnold Brosch, Abdelrahman Eldesokey, Michael Felsberg 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic segmentation networks operate on a fixed set of classes and therefore fail when out-of-distribution (OOD) objects appear during deployment, a critical limitation for safety-critical applications such as autonomous driving. Reliably identifying OOD objects requires well-calibrated epistemic uncertainty, yet common softmax-based confidence scores remain overconfident, while Bayesian alternatives such as Monte Carlo dropout or deep ensembles require costly repeated forward passes. Evidential Deep Learning (EDL) offers an efficient alternative by modeling class probabilities as a Dirichlet distribution learned from a single deterministic forward pass. Existing EDL formulations rely on Euclidean objectives that push predictions towards the simplex vertices, encouraging overconfidence rather than preserving uncertainty for unfamiliar inputs. We instead employ Wasserstein-based objectives, which respect the geometry of the probability simplex, and study the influence of the Wasserstein order on segmentation accuracy and OOD detection within a unified evidential framework. We evaluate this framework on a convolutional (DeepLabV3+) and a transformer-based (SegFormer) architecture on the SegmentMeIfYouCan benchmark, including LostAndFound, RoadObstacle21, RoadAnomaly21, and Fishyscapes. Our results show the optimal Wasserstein order is architecture-dependent: second-order objectives dominate on the convolutional backbone, third-order objectives on the transformer backbone, and our framework surpasses comparable baselines on most metrics, with a single deterministic forward pass.

---


### 242. [YANchor-4B: Effective Long-Horizon Reasoning in O(N) Time with O(1) Memory](https://arxiv.org/abs/2610.10118)

**<font color=#1a73e8>作者：</font>** Huishan Ji, Hua Xu, Weiming Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon reasoning demands access to earlier information at a manageable generation cost. Full-history attention incurs growing storage and computation, while recurrent compression can lose precise details. Therefore, we present YANchor-4B, a general-purpose recurrent model that preserves crucial memory as ANchors for retrieval during subsequent reasoning. Beyond $O(N)$-time generation and $O(1)$ memory, YANchor enables effective long-horizon reasoning through its multidimensional memory mechanism. For example, on challenging math problems, it achieves 82.93% mean pass@1 on AIME 2024--2026 and 63.64% on HMMT, substantially outperforming linear-time, constant-state counterparts, including larger models. It also delivers several-fold higher batched long-generation throughput than Transformer and hybrid baselines on H100. Furthermore, evaluations across dozens of benchmarks demonstrate YANchor's superiority in general-purpose capabilities.

---


### 243. [What Can a Gaussian Process Design Test](https://arxiv.org/abs/2610.10122)

**<font color=#1a73e8>作者：</font>** Ivan De Boi, Marnix Van Soom  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A Gaussian process (GP) model can agree with the data for two reasons: its assumptions are right, or the chosen inputs could never have shown that they are wrong. The distinction can be checked from the design before any responses are observed. Every model implies relations that its noiseless responses must satisfy at the chosen inputs, such as the middle value lies on the line through its two neighbours. For GPs built from finitely many features, these relations are exactly the null space of the kernel matrix. Gale duality gives them a geometric interpretation, in which each observation has a vector and the smallest groups of observations that can expose an error are the circuits. For other kernels the relations become soft: response patterns may be improbable under the prior rather than algebraically impossible. A standard test then combines two kinds of evidence. Structural evidence comes from a violated relation and grows without limit as the noise falls. Prior-based evidence only says that a departure is improbable under the prior. With all inputs at the two ends of an interval, for example, a GP can reject a straight line against a large curvature, but only because the implied intercept is improbable, never because curvature was seen. In simulations the predicted power matched the observed rejection rates. Choosing the next input by predicted power raised the power against a localised discrepancy from 0.48 to 0.72, against 0.51 when choosing by predictive variance, and a grid in two dimensions contained exact tests of additivity that a Latin hypercube lacked. The test itself is classical. The contribution is the prospective reading of that test: before observing the responses, the design already determines what kind of contradiction it can produce.

---


### 244. [m-Set Adversarial Bandits with Winner Feedback](https://arxiv.org/abs/2610.10128)

**<font color=#1a73e8>作者：</font>** Nicolò Cesa-Bianchi, Matteo Papini  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We show upper and lower bounds on the regret of $m$-set adversarial bandits for different utilities (winner reward or sum of rewards) and feedback models (winner index, winner reward, sum of rewards, and their combinations). By comparing to standard bounds for combinatorial and MNL bandits, our results reveal how subtle changes in the setting can have a dramatic impact on the learning rates. Our main technical contributions are the information-theoretic lower bounds on the regret. Experiments on synthetic data confirm our theoretical analyses.

---


### 245. [InterView-C: A Synchronized Multimodal Corpus of VR Avatar-Mediated Survey Interviews](https://arxiv.org/abs/2610.10145)

**<font color=#1a73e8>作者：</font>** Patrick Schrottenbacher, Leon Hammerla, Lydia Kleine 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present InterView-C, a German multimodal corpus of 27 survey interviews conducted entirely in virtual reality, with both interlocutors represented by avatars. The corpus aligns spoken interaction with synchronized behavioral data, including gaze, head and body movement, facial behavior, hand and finger tracking. Its reference transcripts and linguistic annotations provide a reliable interface between this multimodal spoken interaction and predominantly text-based NLP methods. This interface is important because automatically transcribing speech can distort linguistically relevant information, while downstream models trained on existing resources may additionally face transfer challenges when applied to transcribed spoken data. InterView-C therefore provides word-timed and manually post-edited verbatim transcripts for all 54 recordings, interview-item timings, questionnaire responses and negation cue and scope annotations for 1,422 sentences, 1,398 of them doubly annotated ({\alpha}=0.87 for cues; {\alpha}=0.81 for scopes). We demonstrate both challenges empirically: nine open-weight ASR systems disproportionately misrecognize short closed answers and number words, while negation models trained on existing corpora show lower and highly variable performance on our transcribed interviews than a model trained on the InterView-C annotations. InterView-C thus enables linguistic analyses of spoken interaction while retaining their alignment with rich multimodal behavior.

---


### 246. [Pump-and-Dump meets Honeypot Tokens: Detection and Analysis of Telegram Bait-and-Trap Schemes](https://arxiv.org/abs/2610.10149)

**<font color=#1a73e8>作者：</font>** Federico Cernera, Massimo La Morgia, Alessandro Mei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> While Pump-and-Dump schemes have been extensively studied on centralized exchanges (CEXs), how they operate in decentralized exchanges (DEXs) remains largely unexplored. We monitor 83 Telegram channels used to coordinate Pump-and-Dump campaigns and collect 3,677 events across the BNB Smart Chain and Ethereum. Our analysis reveals that, although these operations superficially resemble CEX-based Pump-and-Dump schemes, their underlying mechanism is fundamentally different. Rather than manipulating prices, organizers orchestrate deceptive Pump-and-Dump campaigns around honeypot tokens whose smart contracts allow Telegram subscribers to buy but prevent them from selling. Unaware of this restriction, victims purchase these tokens and are unable to recover their funds. We refer to this new fraud mechanism as Bait-and-Trap. We show that Bait-and-Trap provides a substantially more reliable profit strategy than Pump-and-Dump schemes: organizers gain in 99.3% of cases, extracting over $7 million in profit. To counter this threat, we develop a transaction-simulation tool that detects honeypot tokens before purchase by testing whether a user can successfully sell against the token's live contract state, providing a practical defense against Bait-and-Trap operations.

---


### 247. [HySPE: Positional Encoding via Symplectic Dual Shears](https://arxiv.org/abs/2610.10154)

**<font color=#1a73e8>作者：</font>** Zhongping Ji  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Hyperbolic Symplectic Positional Encoding (HySPE), grounding positional attention in non-compact symplectic transformations. While canonical Rotary Position Embedding (RoPE) parameterizes the compact, elliptic branch of $\Sp(2,\R)$ via rotations, HySPE operationalizes its hyperbolic branch via a damped symmetric composition of dual shears, yielding a conformally symplectic contraction with two spectral decay rates per channel pair. To eliminate the exponential representation drift inherent to naive absolute factorizations, we diagonalize the operator in its invariant eigenbasis and introduce blockwise coordinate rebasing with adaptive centered execution. This guarantees length-independent numerical bounds while matching cached RoPE forward latency (7.21\,ms on an RTX 4090). On TinyShakespeare, HySPE-UltraLong maintains an invariant perplexity of 4.810 up to $16\times$ zero-shot extrapolation ($L=4096$), whereas RoPE degrades to 131.198. Scaled to a 51M-parameter subword Transformer on WikiText-103 ($L_{\text{train}}=512$), HySPE closely matches RoPE in-domain while robustly extrapolating to length 8192, reducing tail perplexity by 83.9\% over RoPE. While these controlled experiments establish HySPE's extrapolation robustness and numerical stability, evaluating its scaling behavior on large-scale foundation models remains an important direction for future investigation.

---


### 248. [BagDINO: Multi-View Baggage Re-Identification with DINOv3](https://arxiv.org/abs/2610.10160)

**<font color=#1a73e8>作者：</font>** Vita Santa Barletta, Danilo Caivano, Rebecca Margiotta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mishandled checked baggage remains a recurrent issue in airport operations, and current recovery workflows still largely rely on tag-based tracking, which does not directly support visual identification when tag evidence is missing or unavailable. This paper investigates baggage re-identification as an instance-level retrieval problem in a multi-camera setting, leveraging DINOv3 foundation-model representations to match a query image against a gallery of registered baggage images. A Torchreid-style BNNeck re-identification head is placed on top of a DINOv3 backbone, and parameter-efficient adaptation is performed via LoRA. Experiments are conducted on the MVB benchmark using a progressive study that compares a fully frozen backbone against LoRA and fine-tuning strategies. Results indicate that parameter-efficient adaptation of foundation-model features provides an effective and stable approach for multi-view baggage re-identification under limited training data.

---


### 249. [A Unified Information-Theoretic Approach to Constrained Multi-Fidelity Multi-Objective Bayesian Optimization](https://arxiv.org/abs/2610.10174)

**<font color=#1a73e8>作者：</font>** Rikuto Matsumoto, Masanori Ishikura, Masayuki Karasuyama  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian optimization often involves multiple objectives, constraints, and fidelity levels. We address the challenge of jointly selecting where and at which fidelity to evaluate to identify the highest-fidelity feasible Pareto frontier in this combined setting. From a unified information-theoretic perspective, we measure query utility by the information gain about this frontier, provided by an observation. Since this mutual information is intractable, we derive a variational lower bound using a mixture of under- and over-truncated approximations to the Pareto-consistent region. Multi-fidelity surrogate models propagate the information to arbitrary fidelities, yielding a cost-aware acquisition function without separate heuristics for fidelity selection or constraint handling. Experiments on synthetic, benchmark, and real-world problems demonstrate effectiveness across diverse objective, constraint, and fidelity settings.

---


### 250. [Collusion-Secure Semi-Quantum Secret Sharing Scheme using a Quantum Third Party](https://arxiv.org/abs/2610.10176)

**<font color=#1a73e8>作者：</font>** Santanu Majhi, Nirupam Basak  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The security of a secret sharing protocol is compromised if one or more dishonest participants can reconstruct the secret by deviating from the prescribed protocol, particularly when such malicious behavior remains undetected. Semi-Quantum Secret Sharing (SQSS) is a variant of secret sharing in which the participants possess only classical capabilities, such as preparing and measuring qubits in the computational ($Z$) basis, while a quantum-capable third party assists the dealer in generating and distributing quantum shares of a classical secret. The limited quantum capabilities of the participants in SQSS protocols may introduce vulnerabilities to collusion attacks, enabling an assisting quantum third party, in collaboration with a dishonest classical participant, to jointly recover the secret even without detection. In this work, we propose a novel SQSS protocol that eliminates this vulnerability and achieves information-theoretic security against collusion attacks. We further prove that the proposed protocol is secure against a broad class of external and internal attacks. Finally, a comparative analysis demonstrates that our construction advances existing SQSS protocols by simultaneously optimizing qubit efficiency, involves a classical dealer, and resilience against DCNA attacks using basic Bell states.

---


> [!TIP]
> 当前位于：**201-250**（第 5/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-324](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
