# 📦 其他研究 | 2026年06月03日

> 本类共 **651** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**551-600**（第 12/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | **551-600** | [601-650](./part-13.md) | [651-651](./part-14.md)

---

### 551. [Disentanglement-Based Equivariant Learning for Compositional VQA](https://arxiv.org/abs/2606.02168)

**<font color=#1a73e8>作者：</font>** Zhou Du, Zhaoquan Yuan, Xiao Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Compositional visual question answering (VQA) represents a challenging yet fundamental task that requires models to comprehend novel combinations of previously learned concepts. The current methods often overlook the disentanglement of underlying concepts and are restricted in terms of their ability to effectively capture the compositional variation mechanism. Moreover, the state-of-the-art techniques depend on additional clues for training, which is not feasible in real-world VQA scenarios. To address these issues, in this paper, we introduce a novel Disentanglement-based EquivAriant Learning (DEAL) framework for compositional VQA, which is guided exclusively by ground-truth answers. In DEAL, we employ causality-inspired interventions to disentangle concepts derived from visual and textual inputs within a re-encoding framework. Based on the principle of equivariance, we subsequently perform a compositional transformation on the inference input and impose the equivariant constraint on the output to augment the compositional reasoning capacity of the model. Comprehensive experiments conducted on the benchmark CLEVR-CoGenT and GQA-SGL datasets validate the superiority of our proposed DEAL approach over the existing state-of-the-art methods for compositional VQA tasks in both visual and linguistic generalization settings.

---


### 552. [CRAFTQA: A Code-Driven Adaptive Framework for Complex Structured Data Reasoning](https://arxiv.org/abs/2606.02170)

**<font color=#1a73e8>作者：</font>** Chengtao Gan, Zhiqiang Liu, Long Jin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Real-world scenarios involve massive heterogeneous structured data (e.g., tables, knowledge graphs), making effective reasoning over such diverse data increasingly important. Unified structured data question answering has emerged as a prominent research trend, aiming to answer natural language questions across different structured data types within a single framework. However, existing unified methods share a common limitation: they rely on a set of predefined functions, which restricts their ability to perform complex reasoning beyond these predefined operations. To overcome this fundamental limitation, we propose CRAFTQA, a novel adaptive code-driven framework comprising two core modules, CodeSTEP and CRAFT. The CodeSTEP module is a paradigm that generates a complete executable Python code sequence, which contains step-by-step code-based reasoning operations based on the question. The CRAFT module dynamically generates custom code functions for operations beyond the predefined function set, and seamlessly integrates with CodeSTEP to significantly enhance flexibility in handling complex reasoning. Comprehensive experiments on multiple structured datasets demonstrate that CRAFTQA achieves remarkable improvements in complex reasoning scenarios compared to existing unified methods.

---


### 553. [InsightVQA: High-Dimensional Emotion-Cognitive Visual Question Answering Benchmark](https://arxiv.org/abs/2606.02171)

**<font color=#1a73e8>作者：</font>** Shiyu Wang, Ziyu Liu, Chaoyi Yu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual emotion understanding requires models not only to recognize emotional states, but also to why they arise and perform higher-level cognitive reasoning. However, existing benchmarks mainly focus on emotion recognition, offering limited support for grounded understanding and response-oriented analysis. To address this gap, we introduce \textbf{InsightVQA}, a large-scale dataset for hierarchical visual question answering on emotion understanding and cognitive reasoning. Building from 351K images collected from six public sources, we apply a rigorous multi-stage filtering pipeline to curate 138K high-confidence images. Each image is annotated at three hierarchical levels: perception QA for emotion and valence recognition, grounded understanding QA constructed from visual trigger extraction through constraint-guided generation, and cognition QA centered on response intent prediction and sequential insight reasoning. In total, InsightVQA contains 725K QA pairs. We further present \textbf{InsightVQA-Bench}, a high-quality evaluation benchmark comprising 30K samples for fine-grained evaluation. To support evaluation, we introduce \textbf{InsightNet}, an emotion-tuned baseline for MLLMs. Results demonstrate that InsightVQA poses significant challenges for grounded emotion understanding and reasoning.

---


### 554. [Closing the Alignment-Maturity Gap in Federated Prototype Learning](https://arxiv.org/abs/2606.02172)

**<font color=#1a73e8>作者：</font>** Mario Casado-Diez, Alejandro Dopico-Castro, Verónica Bolón-Canedo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning discriminative visual representations from distributed, heterogeneous data is a fundamental challenge in Federated Learning (FL). Prototype-based methods address statistical heterogeneity by sharing class-level representations across clients but create a distance-dependent gradient pressure that is particularly severe during early training rounds: alignment pressure applied to immature global prototypes, aggregated from noisy local representations, generates large gradients that suppress the emergence of local discriminative structure. The result is a poorly organized embedding space and degraded recognition performance, particularly under severe non-IID conditions. We propose FedSAP, a framework that stabilises federated representation learning through two complementary mechanisms: a deterministic alignment curriculum that delays global alignment until local representations become stable and a geometry-driven proxy separation loss that enforces inter-class structure on the unit hypersphere using the existing prototype bank without introducing additional parameters or communication overhead. Together, these mechanisms produce compact, well-separated class clusters without altering the underlying communication protocol between federation's participants. Experiments across three benchmarks and varying degrees of heterogeneity show gains of up to 4 percentage points over the prototype-based baselines evaluated, with improvements most pronounced under high heterogeneity. The representational nature of our framework further enables a straightforward extension to semi-supervised settings, where unlabelled data is incorporated with minimal modification, underscoring the generality of scheduled alignment as a design principle.

---


### 555. [Low-Pass Flow Matching](https://arxiv.org/abs/2606.02177)

**<font color=#1a73e8>作者：</font>** Francesco M. Ruscio, T. Konstantin Rusch  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow Matching typically relies on white noise sources, a choice often misaligned with the power spectra of natural data, which tend to decay with frequency. To address this, we introduce Low-Pass Flow Matching, a variant of Flow Matching based on an operator-modulated interpolant. This formulation induces a time-varying spectral bias that transitions from the source spectrum to a frequency-decaying bias as the path approaches the data. We validate our method on unconditional image generation tasks, including the scientific Galaxy10 dataset. Empirically, we show that our method is particularly effective when paired with adaptive ODE solvers, where it improves or preserves sample quality while substantially reducing sampling cost compared to standard baselines.

---


### 556. [Order within Chaos: Capturing Intrinsic Energy Anomalies for AI-Manipulated Image Forgery Localization](https://arxiv.org/abs/2606.02178)

**<font color=#1a73e8>作者：</font>** Yiming Wang, Baiqi Wu, Qingming Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advancements in generative AI have led to image editing models capable of producing realistic forgeries that evade traditional image forgery localization methods, as these approaches depend on physical noise absent in synthetic data. To address this challenge, we theoretically demonstrate that the diffusion process inherently suppresses local high-frequency variance, creating a statistical energy gap that is distinguishable from the natural entropy of optical imaging. Guided by this insight, we propose FLAME, a unified framework that utilizes a LAD map to capture these intrinsic anomalies, coupled with a parameter-efficient adapter for SAM to achieve precise, pixel-level forgery localization. Furthermore, to bridge the lag between forensic benchmarks and evolving generative models, we introduce EditStream, an automated pipeline for continuous, instruction-based training data synthesis. Extensive experiments demonstrate that FLAME establishes a new state-of-the-art, significantly outperforming previous methods on AI-generated forgery datasets while effectively generalizing to unseen generative architectures. Our code is available at this https URL.

---


### 557. [On the Generalization in Topology Optimization via Sensitivity-Conditioned Bernoulli Flow Matching](https://arxiv.org/abs/2606.02179)

**<font color=#1a73e8>作者：</font>** Mohammad Rashed, Duarte F. Valoroso Madeira, Babak Gholami 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Surrogate models for topology optimization (TO) exhibit highly variable out-of-distribution (OOD) generalization under distribution shifts such as changing loads or boundary conditions, yet the source of this variability remains unclear. We hypothesize that OOD performance is governed by how much information the conditioning signal preserves about the adjoint sensitivity (reduced gradient) that drives classical TO. Modeling the TO pipeline as a causal Markov chain, the Data Processing Inequality establishes that, under this abstraction, the sensitivity field is an information-theoretically optimal conditioning signal for topology prediction. However, computing exact adjoint sensitivities can be expensive or unavailable in practice; we observe that certain physical fields can approximate sensitivities through monotone transformations. To formalize this, we introduce \textbf{pseudo-sensitivities} to characterize which fields enable generalization versus those that are information-poor. We then show that a sensitivity-conditioned Bernoulli flow-matching generator empirically confirms these predictions: conditioning on sensitivities yields state-of-the-art OOD performance, while increasingly distant physical fields degrade toward raw parameter conditioning. Results hold across structural TO benchmarks under load shifts and our new CFD-TO dataset under boundary-condition shifts such as multi-outlet configurations. Code and datasets are available at this https URL .

---


### 558. [The Unicity Execution Layer](https://arxiv.org/abs/2606.02181)

**<font color=#1a73e8>作者：</font>** Ahto Buldas, Dirk Draheim, Mike Gault 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper introduces the Unicity Execution Layer, a modular component of the Unicity framework enabling secure off-chain transactions while maintaining trustless double-spending prevention. We present a formal security model where token ownership is represented by public keys and transfers require digital signatures. We prove three fundamental security properties: (1) no double-spending--each token state can be spent at most once, (2) no blocking--only the legitimate owner can prevent a token from being spent, and (3) service-side privacy--the Unicity Service cannot link transactions with the same token. The user-side privacy is addressed by introducing generalized multi-public-key signature schemes that allow one secret to generate multiple unlinkable public keys, and interactive and non-interactive concrete instantiations, enabling private transactions with stable public identity with minimal key management overhead.

---


### 559. [Unicity: Predicates and Atomic Swaps](https://arxiv.org/abs/2606.02192)

**<font color=#1a73e8>作者：</font>** Ahto Buldas, Dirk Draheim, Mike Gault 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We generalize Unicity token ownership to programmable spending conditions called predicates, enabling smart-contract like functionality executed off-chain directly by relying parties rather than by consensus participants. We prove that the security properties of the Unicity execution layer are preserved under reduction to predicate family unforgeability. To demonstrate the utility of the model, we show how to implement trustless atomic swaps by using predicates.

---


### 560. [Coherent Off-Policy Improvement of Large Behavior Models with Learned Rewards](https://arxiv.org/abs/2606.02194)

**<font color=#1a73e8>作者：</font>** Christian Scherer, Joe Watson, Theo Gruner 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distilling expert demonstration data into large generative models using behavioral cloning is a scalable approach to learning capable policies for robotic control, particularly for dexterous manipulation. Reinforcement learning (RL) can be used as a means to finetune these policies further using additional experience. An open question is whether RL is more sample-efficient than collecting more human demonstrations. Prior work has finetuned large pretrained policies in a scalable fashion by applying RL to a smaller residual policy that corrects the pretrained model. However, for the typical sparse reward tasks, RL algorithms can struggle to optimize the behavior in a sample-efficient manner. We explore inverse reinforcement learning, where a dense reward function is learned from expert demonstrations, potentially reducing the challenge of RL finetuning. We specifically consider coherent imitation learning, an IRL method that facilitates improvement of the BC policy through using a specific reward formulation with theoretical guarantees. We show that our IRL method maintains or improves the performance of pi-0.5 on all six sparse manipulation tasks and achieves a $\geq 90\%$ success rate on five out of six complex manipulation tasks, outperforming RL-based baselines using sparse rewards. By ensuring our initial pretrained finetuning policy is optimal for our initial reward and critic, our method circumvents the initial drop commonly seen in RL finetuning and enables faster improvement.

---


### 561. [PyFEX: Uncovering Evasive Python-based Threats via Resilient and Exhaustive Path Exploration](https://arxiv.org/abs/2606.02196)

**<font color=#1a73e8>作者：</font>** Meng Wang, Yue Ma, Majid Garoosi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid expansion of the Python ecosystem has fueled two distinct but converging threats: adversaries increasingly target the software supply chain via the Python Package Index (PyPI), while also building evasive, cross-platform malicious binaries compiled from source code written in Python. Current program analysis techniques struggle to address this dual threat. Static analysis based tools are often blinded by runtime obfuscation and compiled bytecode, while dynamic analysis based ones are fragile, prone to evasion by environmental guardrails, and often terminates prematurely due to unsatisfied dependencies.
To overcome these limitations, we present PyFEX, a resilient forced-execution engine. PyFEX explores a program's behavioral space systematically by forcing execution across all conditional branches to bypass evasion checks. To address the fragility of dynamic execution, it introduces a novel resilient crash recovery mechanism that synthesizes dummy objects to satisfy failed operations at the runtime, allowing analysis to proceed past fatal errors, and employs path merging to mitigate path explosion. PyFEX further incorporates an automated entry identification mechanism that proactively discovers and invokes dormant functions, exposing malicious logic hidden within uncalled APIs. To demonstrate the efficacy of this engine, we built PyFEXScan, a proof-of-concept malware detector built on top of PyFEX. Evaluated against both known malicious PyPI packages and real-world compiled binaries, PyFEX exposes critical behaviors missed by the existing state-of-the-art tools. In a live deployment on PyPI, PyFEXScan discovered 212 previously unknown malicious packages accounting for over 91,648 downloads, underscoring the necessity of resilient, exhaustive analysis for securing the Python ecosystem.

---


### 562. [Model Multiplicity and Predictive Arbitrariness in Recidivism Risk Assessment](https://arxiv.org/abs/2606.02198)

**<font color=#1a73e8>作者：</font>** Ashwin Singh, Carlos Castillo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prediction tasks over individual futures, which are inherently noisy, often admit multiple similarly accurate models. When these models produce different predictions for the same individual, they raise concerns of arbitrariness in decision-making. How severe can this arbitrariness be, in theory and in practice? How can it be resolved to support high-stakes risk assessment?
We address these questions through a study of a machine learning-based decision support system for recidivism risk assessment that has been in use for over 15 years. By translating complex legal rules into an algorithm for labeling post release outcomes (recidivist or non-recidivist), we first construct a dataset of thousands of inmate releases. Using this dataset, we learn interpretable models that improve predictive performance, reduce error-rate disparities between groups, and ensure that rehabilitative progress lowers risk scores. Next, we study predictive multiplicity, by first deriving a tight lower bound on the expected predictive agreement of any finite set of models over a dataset, and then by evaluating the extent to which structural diversity (e.g., different model coefficients) within this set translates to predictive multiplicity (i.e., different predictions for the same individual). Our experiments indicate that the existence of many similarly accurate models with comparable error-rate disparities does not necessarily translate into severe predictive multiplicity. Empirically, similarly performant models can exhibit substantially higher predictive agreement than worst-case theoretical guarantees suggest. We find that a simple policy that assigns each inmate the lowest risk among these models is effective for addressing predictive arbitrariness.

---


### 563. [Cross-Environment Neural Reranking for Sample-Efficient Action Selection in Text-Based Agents](https://arxiv.org/abs/2606.02204)

**<font color=#1a73e8>作者：</font>** Kan Shao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model agents achieve strong performance on text-based benchmarks but incur prohibitive inference costs, motivating the use of compact neural rerankers for action selection. We investigate whether a single lightweight model can perform action selection across multiple diverse environments, a capability that would eliminate per-environment model maintenance. Training DeBERTa-v3 (184M-434M parameters) jointly on ALFWorld, WebShop, and ScienceWorld with minority-class upsampling, we find that rebalanced two-environment joint training substantially improves over single-environment ALFWorld performance (net gain +0.412) while maintaining competitive WebShop performance (+0.214 vs. +0.249 single-environment). Three-environment training yields a mean combined net gain of +0.551 +/- 0.024 across 4 seeds, with per-environment results approaching specialized single-environment models while providing positive cross-domain transfer. Cross-environment adaptation is highly sample-efficient: fine-tuning on only 9.2% of target-domain data recovers 93% of full-data performance, and scaling model capacity yields limited benefits, indicating data diversity is the primary driver. Environment-aware LoRA adapter routing with PCGrad achieves a best-seed result of +0.611 (seed 42), with seeds 456 and 789 at +0.554 and +0.559, but exhibits high variance due to seed 123 collapsing to +0.263 (4-seed mean +0.497 +/- 0.158), representing a promising but currently unstable direction. Joint training with clean splits and data rebalancing is a key ingredient. We will release our three-environment benchmark of 51,580 training instances (41,740 raw unique states with minority-class upsampling) and all model checkpoints upon acceptance.

---


### 564. [Consistency Training while Mitigating Obfuscation via Rate Matching](https://arxiv.org/abs/2606.02211)

**<font color=#1a73e8>作者：</font>** Sohaib Imran, Prakhar Gupta, Jannes Elstner 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are often influenced by extraneous input features, such as cues revealing a user's preferred answer. Consistency training reduces this influence by training models to behave similarly across inputs with and without the extraneous feature. However, existing methods train for consistency over entire responses or internal activations, which also constrains whether the model verbalises said extraneous features. We show this leads to obfuscation, where the model learns not to mention a cue while remaining influenced by it, which may undermine monitorability. To address this, we introduce Rate Matching Consistency Training (RMCT), which trains for consistency over selected behavioural properties without constraining how this behaviour is expressed. RMCT matches the rate at which the model exhibits a target behaviour (e.g., following a bias cue) across input perturbations, rather than requiring paired inputs with and without the extraneous feature, extending consistency training to settings where the extraneous features cannot be removed. We evaluate RMCT on sycophancy reduction in two open-weight language models, achieving reductions in bias-following comparable to a standard consistency-training baseline on held-out bias types, while largely preserving the model's tendency to verbalise the bias cue. Further, we find that RMCT is more data-efficient at the expense of being less compute-efficient in our experiments. Overall, RMCT shows that consistency training can improve behavioural robustness without directly trading off against monitorability.

---


### 565. [Symmetry-Aware 9D Pose Estimation with Sim(3)-Consistent Feature and Spherical Inception Convolution](https://arxiv.org/abs/2606.02219)

**<font color=#1a73e8>作者：</font>** Panfei Cheng, Hongshan Yu, Wenrui Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object pose estimation is a fundamental problem for an agent system to perceive or manipulate objects in images or videos. However, current instance-level methods struggle with generalization to unseen objects. Category-level methods seek to address this, but remain constrained by the complexities of learning in the non-linear Sim(3) space and intra-class variations. To address these challenges, We propose an effective method for category-level object pose estimation with two key innovations: (1) A translation/size estimator, featuring a semantic-guided symmetry-aware module that leverages robust generalization capabilities of a large vision model (LVM) to infer symmetry points, resulting in accurate translation and size without shape priors. This result serves as a precomputed cue for rotation estimation, thereby reducing the difficulty of learning in the non-linear Sim(3) space and laying a robust foundation for tackling the inherently more challenging rotation estimation. (2) A feature fusion module, based on our proposed spherical large-kernel inception convolution, fuses semantic features from the LVM with systematically computed geometric features to extract essential pose features from intra-class variations by modeling long-range dependencies without excessive computational cost. Built on these innovations, we achieve SOTA on benchmarks and real-world scenes, while developing a robust robotic picking system capable of handling diverse objects. Our code will be available at the project page: {\hypersetup{urlcolor=blue}this https URL}.

---


### 566. [CORE-MTL: Rethinking Gradient Balancing via Causal Orthogonal Representations](https://arxiv.org/abs/2606.02221)

**<font color=#1a73e8>作者：</font>** Chengfeng Wu, Tao Zou, Yanru Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-task learning (MTL) aims to construct a joint model for multiple tasks by sharing a common representation across domains. To achieve this goal, existing optimization-centric methods either balance task gradients or modify the shared architecture. However, as these approaches remain agnostic to the content of the shared representation, they fail to disentangle task-relevant structure from spurious context, leading to negative transfer and poor generalization. To overcome this limitation, we propose Causal Orthogonal Representations for Multi-Task Learning (CORE-MTL), a causally motivated representation-centric framework that encourages a structured semantic-residual factorization of the shared representation, concentrating task-relevant structure in the semantic stream while relegating nuisance variation to the residual stream. We instantiate this framework in the visual domain by leveraging physical priors for structured scenes and statistical constraints for attributes. Theoretically, our method enjoys a tighter out-of-distribution generalization bound than optimization-centric methods and reduces task gradient interference without explicit gradient projection or reweighting. Empirically, CORE-MTL consistently outperforms existing methods on visual multi-task benchmarks in both in-distribution and out-of-distribution settings. Code is publicly available at this https URL.

---


### 567. [Network Learning with Semi-relaxed Gromov-Wasserstein](https://arxiv.org/abs/2606.02223)

**<font color=#1a73e8>作者：</font>** Charles Dufour, Ulysse Naepels, Leonardo V. Santoro  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating the generative mechanism of large-scale networks is a fundamental challenge in statistical machine learning. It requires the identification of the latent connectivity structure, which is in general an NP-hard combinatorial problem due to the absence of canonical node labels. We address this challenge by allowing for probabilistic couplings, thereby relaxing the assignment problem. Our estimation framework can be formulated as a semi-relaxed Gromov-Wasserstein objective and provides a low-dimensional representation of the generative structure. We solve this via a block-coordinate conditional gradient algorithm. Despite the relaxation, the resulting solution is typically deterministic: in fact, we show that the optimality gap between the relaxed solution and the deterministic assignment vanishes at rate $O(1/n)$, where $n$ is the number of nodes. This allows for tractable recovery of the underlying model and enables rigorous statistical analysis: we establish consistency and minimax-optimal convergence rates for both stochastic block models and Holder-smooth graphons. Our implementation scales efficiently with $n$, as demonstrated on both synthetic and real-world datasets.

---


### 568. [A Doeblin-Anchored Contrastive Chart for Learning Markov Transition Kernels](https://arxiv.org/abs/2606.02232)

**<font color=#1a73e8>作者：</font>** Ao Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning a Markov transition model is not merely conditional density estimation: the learned object must be a valid transition kernel before it is iterated in downstream dynamics. This paper introduces a Doeblin-anchored contrastive chart, a statistical-to-dynamical coordinate framework for learning transition kernels from contrastive objectives. Given a restart law and an anchor strength, the chart mixes the target transition with the restart law. The resulting anchored kernel is simultaneously a Doeblin-minorized Markov kernel, the positive conditional law in a binary contrastive experiment, and an explicitly invertible coordinate for the original transition law. We prove that the anchored contrastive risk identifies the anchored transition density and calibrates excess risk to density error. Since inversion of a learned score may produce a signed or unnormalized object, we introduce a measurable Markovization operator that restores kernel validity while preserving integrated $L^1$ accuracy up to a constant factor. Oracle inequalities and Hölder--ReLU approximation bounds yield nonparametric rates for independent transition pairs. For stationary geometrically $\beta$-mixing trajectories, a conservative thinning-and-coupling extension yields the same reconstruction interface with an effective sample size. Occupancy-weighted perturbation bounds transfer one-step kernel error to finite-horizon marginal, path-law, and occupation-measure errors under explicit coverage.

---


### 569. [Why Are DMD Students Lazy? Understanding the Copying Behavior in Few-Step Distillation](https://arxiv.org/abs/2606.02237)

**<font color=#1a73e8>作者：</font>** Shucheng Li, Iolo Jones, Alexander Tong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distribution Matching Distillation (DMD) compresses pretrained diffusion models into efficient few-step generators by aligning their noised distributions across all scales. In principle, such distribution-level supervision remains agnostic to specific noise-data pairings of the teacher; this provides the student the freedom to remap latent noise, a behavior consistently observed in low-dimensional settings. Surprisingly, we find that in high-dimensional settings, distilled students spontaneously reproduce the original noise-data pairings of the teacher, a phenomenon we term copying. We demonstrate that copying is neither a byproduct of adversarial objectives nor a result of teacher memorization. Instead, our evidence suggests that copying is an emergent property arising from the limited geometric freedom of the student model during high-dimensional distillation.

---


### 570. [BlockGen: Flexible Blockwise Sequence Modeling with Hybrid Samplers](https://arxiv.org/abs/2606.02241)

**<font color=#1a73e8>作者：</font>** Justin Deschenaux, Caglar Gulcehre  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Is the uniform-state diffusion framework a more powerful paradigm for discrete diffusion? Recent studies indicate that this may be the case. In combination with predictor-corrector samplers, uniform-state diffusion models (USDMs) produce samples of higher-quality than masked diffusion models (MDMs), and USDMs equal or outperform MDMs in downstream tasks, even though they exhibit greater perplexity. Two issues remain unresolved. First, existing work compares uniform and masked diffusion with un-informed correctors that re-inject noise at random positions, rather than targeting tokens most likely to be wrong. Second, prior work compares full-sequence diffusion models, so we do not know whether the same conclusion holds when tokens are generated block by block. To address these issues, we introduce BlockGen, a blockwise sequence model that we instantiate with both masked and uniform diffusion. BlockGen trains on a mixture of block sizes and its likelihood interpolates between AR and pure diffusion more finely than models with a fixed block size. BlockGen enables AR-informed predictor-corrector sampling (ARPC), which combines AR and diffusion predictions to re-generate unlikely tokens without an auxiliary verifier. Under ancestral sampling, uniform outperforms masked in the block-by-block setting, especially in the few-step regime. Under ARPC, the gap closes and reverses at high NFE. With block size $16$ on GSM8K, MDMs reach slightly higher accuracy than USDMs, and we observe a similar trend in Generative Perplexity on OpenWebText. Find our code at this https URL.

---


### 571. [Towards Resolving Optimization Conflicts Between Image- and Text-Based Person Re-Identification](https://arxiv.org/abs/2606.02242)

**<font color=#1a73e8>作者：</font>** Karina Kvanchiani, Timur Mamedov  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The joint optimization of image-based (I2I) and text-based (T2I) person re-identification (ReID) is hindered by modality discrepancies and conflicting training objectives, leading to suboptimal shared representations. While I2I ReID focuses on identity-level invariance across images of the same person, T2I ReID is driven by instance-specific textual descriptions tied to unique visual traits. This paper explores the fundamental difference between two ReID tasks and their optimization processes for effective training. Since I2I and T2I ReID are often studied separately, the loss functions optimized for one retrieval setting may negatively affect the representation quality required by the other. Motivated by these findings, we propose a decoupled two-stage training pipeline for learning a shared representation across image and text modalities. The pipeline is based on a single vision encoder that supports both I2I and T2I retrieval while avoiding cross-task interference during training. We provide extensive experiments across multiple configurations, varying domain mixing procedures, learning strategies, and task objectives. We observed that I2I ReID pre-training positively impacts the generalization ability to T2I data. Besides, we find that incorporating textual supervision during the vision encoder training stage enhances both I2I and T2I performance. We believe our insights provide a meaningful step toward unified ReID systems and cross-modal retrieval overall.

---


### 572. [CEON: Circular Economy Ontology Network](https://arxiv.org/abs/2606.02253)

**<font color=#1a73e8>作者：</font>** Huanyu Li, Els de Vleeschauwer, Robin Keskisärkkä 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Increasing the circularity of resource use in our society has been recognized as a path to sustainability, i.e., transitioning into a more circular economy. There are many different circular strategies to do so, such as reusing products and components, refurbishing and remanufacturing used products, or recycling left-over or used materials. To enable these strategies, it is necessary to share information at the infrastructure level and to communicate between industry sectors along the product life cycle. Enabling semantic interoperability in this information sharing and communication is therefore a key to increasing circularity. However, knowledge representation for the circular economy (CE) domain, which involves many relevant industry sectors related to product life cycles, remains challenging. To bridge this gap, we developed the Circular Economy Ontology Network (CEON) within the Onto-DESIDE project. This ontology network aims to fill gaps in CE by defining cross-sectorial concepts and to enable semantics-aware data documentation. We demonstrate CEON through cross-industry data documentation scenarios spanning construction, electronics, and textile sectors.

---


### 573. [Who Annotates in NLP? A Large-scale Assessment of Human Annotation Reporting between 2018 and 2025](https://arxiv.org/abs/2606.02255)

**<font color=#1a73e8>作者：</font>** Maria Kunilovskaya, Gagan Bhatia, Lisa Sophie Albertelli 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Human annotation is the empirical foundation of much NLP research, from dataset construction to model evaluation, but papers often leave unclear who produced the annotations and how the annotation process was controlled. We provide the first large-scale, task-level audit of human annotation reporting across major NLP venues, asking which annotation details are documented, which are missing, and how reporting varies across time, topic, venue, and intended use of human judgment. We introduce a unified taxonomy of annotation-reporting practices and validate an LLM-assisted extraction pipeline against Annotated-gold, a human-adjudicated gold standard of 41 papers and 72 annotation tasks, where the best model reaches human-comparable agreement with adjudicated labels, with Krippendorff's alpha of 0.606 versus 0.585 for human-human agreement. Using this pipeline, we construct Annotated-llm, a dataset covering ACL-venue papers from 2018-2025, with 2,667 extracted annotation tasks from 1,603 papers, and find that papers frequently report operational details such as recruitment strategies, annotator expertise, and annotation volume, but often omit details needed to assess annotation validity, including training, language proficiency, compensation, socio-demographics, adjudication, and agreement values, especially in model-evaluation studies. Our results show that annotation reporting in NLP has improved over time but remains uneven, and they establish a scalable framework and bare-minimum reporting recommendations for making human annotation more reliable, reproducible, and interpretable.

---


### 574. [ArrythML: An Autoencoder-Based TinyML Approach for On-Device Arrhythmia Detection on Resource-Constrained Embedded Systems](https://arxiv.org/abs/2606.02256)

**<font color=#1a73e8>作者：</font>** Nagarajan S, Kurian Polachan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Our work presents a method for ECG segmentation and arrhythmia detection using Tiny Machine Learning (TinyML) models for real-time, on-device inference on resource-constrained embedded systems. We develop INT8 quantized autoencoder-based TinyML models with minimal layers and parameters for embedded deployment. These models are evaluated using a custom dataset derived from the MIT-BIH Arrhythmia Database and validated in both PC-based simulations and on-device environments.
For the evaluations, over 95,000 ECG segments are processed on an ESP32-S3 microcontroller running the TensorFlow Lite Micro runtime. Post-evaluation, detailed analysis, including annotation-wise and record-wise failure analysis, is conducted to characterize model behavior across diverse ECG morphologies and rhythm patterns and to explain missed detections. In several cases, apparent misclassifications may correspond to early or subtle anomaly patterns labeled as normal in the reference annotations, highlighting the model's sensitivity. A refined evaluation by filtering out ambiguous cases in the dataset shows that the best-performing DNN-based autoencoder achieves a recall of 84%, an F1-score of 79%, a model size of approximately 180 KB, and an inference latency of 9 ms on-device. These results demonstrate the feasibility of low-power, privacy-preserving embedded wearable systems capable of performing accurate arrhythmia detection entirely on-device.

---


### 575. [Guided Sensemaking: Agents in Collaborative Deliberation](https://arxiv.org/abs/2606.02260)

**<font color=#1a73e8>作者：</font>** Aaditya Bhatia, Navdeep Kaur Bhatia, Marc-Antoine Parent 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI systems are aggressively reshaping how students engage with information and perform cognitive work; convenience-oriented use has the potential to displace effortful reasoning, reflection, and learning, especially for those who lack domain expertise and effective human-AI interaction strategies. Current AI tools are heavily focused on chat-style interfaces geared towards answer generation and efficiency in a linear and fragmented stream of text, offering limited support for structured reflection, argument construction, and sensemaking in collaborative contexts. We introduce Guided Sensemaking, an AI-augmented multiagent discourse platform that facilitates composition of well-thought-out ideas around a central question, provides scaffolding for critical thinking, and enables visualization of argumentative structure to support critical thinking and collaborative deliberation. The system uses several interactive agents to provide context-sensitive questioning prompts and a scaffolding for thought that exposes thematic clusters, agreements, and points of contention without collapsing diverse perspectives. This paper proposes a conceptual design and interaction paradigm that positions generative AI not as a shortcut to answers but as a research partner that externalizes reasoning, preserves user agency, and fosters structured, traceable sensemaking in educational and civic contexts.

---


### 576. [A combination of noise and bilateral filters achieve supralinear and scalable adversarial robustness in CNNs](https://arxiv.org/abs/2606.02267)

**<font color=#1a73e8>作者：</font>** Nicolas Stalder, Benjamin F. Grewe, Matteo Saponati 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The vulnerability of deep neural networks to adversarial examples poses a significant challenge for real-world deployment. Existing techniques to enhance deep network robustness rely on adversarial training, an approach that is powerful but computationally intensive and typically tailored to specific attack types. To address these limitations, existing works have explored techniques such as adding gaussian noise or filtering images, both of which can boost the network robustness to various adversarial attacks, albeit modestly. Here, we theoretically demonstrate that these two approaches enhance robustness against adversarial attacks through complementary mechanisms, resulting in supralinear robustness when combined. Building on this insight, we experimentally show that a simple preprocessor combining Gaussian noise and bilateral filtering yields supralinear improvements in adversarial robustness with minimal computational cost. Next, we combine our preprocessor with adversarial training and test on RobustBench to assess its supralinear improvement over state-of-the-art defenses. First, this combination ranks second on AutoAttack and third overall, while using only $\sim$35% of the training FLOPs, using a model with $\sim$50% less parametets, trained with $\sim$33% of the epochs and $\sim$15% the data compared to state-of-the-art defenses. Second, our method scales efficiently, matching the accuracy of competing models with roughly 2-8x less total compute across 3 orders of magnitude. Overall, our approach provides a principled and easily integrable framework for enhancing adversarial robustness, offering negligible computational overhead and a simple yet theoretically grounded design.

---


### 577. [From Extrinsic to Intrinsic: Geodesic-Guided Representation Learning for 3D Geometric Data](https://arxiv.org/abs/2606.02268)

**<font color=#1a73e8>作者：</font>** Yuming Zhao, Junhui Hou, Qijian Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geometric analysis fundamentally distinguishes between \textit{extrinsic} and \textit{intrinsic} perspectives. The dominant paradigm in current 3D representation learning relies on either extrinsic spatial structures or high-level semantics, struggling to capture the essence of shape identity and underlying manifold topology. To bridge this gap, we introduce a novel 3D representation learning paradigm, namely \textbf{PRISM}, for \textbf{P}re-training, which learns isometric embeddings by \textbf{R}ecovering the \textbf{I}ntrinsic \textbf{S}urface geodesic \textbf{M}etric. PRISM incorporates a topology-enforcing objective that explicitly constrains the structure of latent space, alongside a specialized two-stage training recipe mitigating sample imbalance inherent in the distribution of geodesic distances. Experiments demonstrate that our approach shows satisfactory accuracy, robustness, and high efficiency in geodesic distance prediction and achieves superior performance across diverse downstream tasks, including shape recognition, surface parameterization, and non-rigid correspondence. The code will be publicly available at this https URL.

---


### 578. [CityTrajBench: A Unified Benchmark for City-Scale Vehicle Trajectory Generation](https://arxiv.org/abs/2606.02287)

**<font color=#1a73e8>作者：</font>** Shibo Zhu, Xiaodan Shi, Dayin Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Urban trajectory generation is a fundamental task for transportation simulation, urban planning, and mobility analytics. However, systematic comparison across trajectory generation methods remains difficult because existing studies often rely on different datasets, preprocessing pipelines, trajectory representations, and evaluation metrics. This fragmentation makes it unclear whether reported performance differences arise from the generation mechanism itself or from inconsistent experimental protocols. To address this issue, we present CityTrajBench, a unified benchmark framework and protocol for city-scale vehicle trajectory generation. CityTrajBench standardizes data ingestion, trajectory normalization, feature construction, model adaptation, map-aware post-processing, model selection, and multi-level evaluation under a common setting. It supports heterogeneous generators, including statistical baselines, VAE-based, GAN-based, diffusion-based, and flow-matching-based models, and evaluates them on three real-world urban trajectory datasets. The benchmark measures global spatial realism, trip-level distribution fidelity, trajectory-level geometric similarity, conditional mobility consistency, and efficiency. Experiments reveal clear trade-offs across model families: DiffTraj is strongest on trajectory-level geometric fidelity, DiffRNTraj is competitive on structure-sensitive global realism, and TrajFlow provides a strong balance across realism, quality, conditional consistency, and efficiency. Meanwhile, a simple Markov baseline remains competitive on coarse-grained trip and local-movement statistics. These findings show that urban trajectory generation quality is inherently multi-objective, that no single model dominates all criteria equally, and that CityTrajBench provides a reproducible benchmark protocol and testbed for future research on urban mobility generation.

---


### 579. [Neural Acquisition & Representation of Subsurface Scattering](https://arxiv.org/abs/2606.02292)

**<font color=#1a73e8>作者：</font>** Arjun Majumdar, Raphael Braun, Hendrik Lensch  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a method to acquire and estimate the sub-surface scattering properties of light transport at a highly detailed level by learning the pixel footprint response at each point on the object surface. The reconstruction leverages 3D scanning techniques as input to a U-Net CNN. A stereo projector-camera setup using phase-shifted profilometry (PSP) patterns efficiently captures the data for a variety of scattering objects. Reconstructing dense pixel footprints allows for relighting with arbitrary high-resolution projector patterns. The final output is a relit color image. Qualitative and quantitative comparison against illuminated real-world captured images demonstrate that the predicted footprints are almost identical to the actual responses. The same model is trained for multiple views across multiple objects such that the learned representations can be used to generalize to unseen sub-surface scattering materials as well.

---


### 580. [AI as a Tool for Simulation-Based Experiments in Literary Studies](https://arxiv.org/abs/2606.02293)

**<font color=#1a73e8>作者：</font>** Matthew Wilkens  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generative artificial intelligence (AI) systems open new possibilities for experimentation in literary studies via controlled, grounded, large-scale, low-cost simulations of cultural production. Current systems have not yet been shown to produce high-quality, book-length narrative texts that reliably reflect arbitrarily specified cultural constraints or stylistic features. But there exists substantial relevant research on each of the components required for literary-historical simulation. These include the use and validation of AI systems as proxies for differentiable human populations; the narrative and stylistic properties of AI-generated texts; the stability and coherence of multiagent, multiturn AI simulations of human actors; and technical methods through which to alter in predictable ways the knowledge and behavior of generative systems. Together, these areas could provide a starting point for more ambitious AI-based modeling of cultural systems of literary production.
We describe the possibilities and challenges of simulation-based experiments in literary studies, summarize the current state of the art in relevant fields, and explain key technical aspects of the work. To provide an example directly relevant to literary scholars, we present the results of experiments on literary text generation, including comparisons to high-status, human-authored novels. Our results include the first demonstration of (limited) in-distribution outputs by AI models in this domain. We conclude with a description of future work on full counterfactual literary-historical simulations using AI.

---


### 581. [Regularized Large Neighborhood Search](https://arxiv.org/abs/2606.02294)

**<font color=#1a73e8>作者：</font>** Germain Vivier-Ardisson, Laurent Demonet, Axel Parmentier 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Operations research practitioners typically tackle NP-hard combinatorial problems using large neighborhood search (LNS), a scalable heuristic that iteratively refines a current solution by locally re-optimizing subsets of its variables. In contrast, most existing approaches for integrating combinatorial optimization layers into neural networks still assume access to an exact global solution, which is computationally intractable. We bridge this gap by introducing regularized LNS (RLNS). By regularizing or perturbing local subproblems, we turn the LNS heuristic into an efficient MCMC sampler over the combinatorial set of feasible solutions, with associated Fenchel-Young losses. Under entropic regularization, we prove that RLNS performs exact block Gibbs sampling. Furthermore, adjusting the number of RLNS iterations allows us to interpolate between pseudolikelihood and exact maximum likelihood estimation, for end-to-end learning without global solvers. We demonstrate our approach on $k$-subset selection, generalized assignment, and stochastic vehicle scheduling problems.

---


### 582. [Quantitative Movement Testing: Measuring Patient Movements from a Single Smartphone Video](https://arxiv.org/abs/2606.02301)

**<font color=#1a73e8>作者：</font>** Pranav Mahajan, Amanda Wall, Eleonora Maria Camerone 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Chronic pain diminishes quality of life by decreasing functional ability, yet objectively measuring this functional impact remains challenging in real-world settings. While optical motion capture provides high precision for assessing altered movement quality, it is costly and restricted to laboratory environments. We aimed to develop and validate Quantitative Movement Testing (QMT), a computer vision pipeline extracting 3D kinematic biomarkers from standard monocular smartphone video, balancing clinical accessibility with biomechanical accuracy. We validated the QMT pipeline, utilising deep learning-based 3D pose-estimation, against gold-standard optical motion capture in healthy controls (N=13). Following leave-one-subject-out calibration to correct systematic bias, we deployed QMT in two prospective clinical cohorts to assess real-world utility: a pre- and post-intervention trial for fibromyalgia patients, and a 30-day longitudinal at-home monitoring study of chronic sciatica patients and healthy controls. In laboratory validation, QMT extracted clinical kinematic metrics with high agreement to optical motion capture, yielding strong correlations (r > 0.85) and low mean absolute errors. QMT demonstrated high test-retest reliability (r > 0.86) in fibromyalgia patients and successfully tracked day-to-day movement fluctuations in chronic sciatica. While real-world home settings introduced higher measurement variance than lab settings, QMT found group-level differences between healthy controls and sciatica patients based entirely on remote recordings. Monocular 3D pose estimation offers a scalable alternative to traditional assessments. QMT provides an objective, accessible biomarker for tracking disease progression and treatment response in clinical trials, though further research is needed to optimise reliability in home environments.

---


### 583. [SeClaw: Spec-Driven Security Task Synthesis for Evaluating Autonomous Agents](https://arxiv.org/abs/2606.02302)

**<font color=#1a73e8>作者：</font>** Hao Cheng, Changtao Miao, Tianle Song 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous LLM agents increasingly operate in stateful environments where they access tools, files, memory, and external services. While such capabilities enable complex real-world workflows, they also introduce security risks that are difficult to capture with existing evaluations. Current agent security benchmarks often rely on manually curated tasks, provide limited coverage of emerging threats, and focus primarily on final outcomes rather than the execution processes that lead to unsafe behavior. We introduce SeClaw, a framework that combines specification-driven security task synthesis with execution-based security evaluation for Autonomous agents. Spec-driven security task synthesis enables scalable and controllable construction of security tasks from structured risk specifications, while SeClaw docker provides a standardized testbed for evaluating agent behavior under diverse safety-risk scenarios. The benchmark covers risks arising from resources, user tasks, environments, and intrinsic agent behaviors, and supports trajectory-aware assessment of unsafe actions beyond final responses. By bridging systematic task synthesis and reproducible security evaluation, SeClaw provides a practical foundation for measuring, diagnosing, and comparing security failures in autonomous LLM agents. The code is available at this https URL.

---


### 584. [Cross-Domain Dead Tree Detection via Knowledge Distillation in Aerial Imagery](https://arxiv.org/abs/2606.02303)

**<font color=#1a73e8>作者：</font>** Anis Ur Rahman, Mete Ahishali, Einari Heinaro 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detecting dead trees in aerial imagery is vital for assessing forest health, especially as tree mortality increases globally due to climate change, but domain variability and scarce labeled data often limit model generalization. This study advances the TreeMort-1T-UNet (Tree Mortality 1-Task U-Net) model, initially trained on Finnish aerial imagery (source domain), by applying knowledge distillation (KD) to adapt it to various target domains, including Polish, German, and Estonian datasets representing diverse forest types. We assess four KD variants: Basic, Self, Feature-level, and Ensemble, against a fine-tuning baseline, using Mean Tree IoU, Instance F1-score, Instance Precision, and Mean Centroid Error as key metrics, alongside representational analyses (e.g., cosine similarity, CKA, SSIM, t-SNE, and linear probing) for domain invariance. Feature-level KD outperforms others, yielding a Mean Tree IoU of 0.106, Instance F1-score of 0.63, Instance Precision of 0.55, and Mean Centroid Error of 3.039 on the Polish dataset, with robust precision across other target domains (e.g., 0.15 on Finnish, 0.67 on Polish, 0.60 on German, 0.59 on Estonian). It excels in low-data scenarios with fewer false positives and shows superior representational invariance (e.g., higher deep-layer CKA/SSIM, better domain mixing in t-SNE, and linear probing AUC of 0.95), making it ideal for precision-critical forestry applications. Additional ablation studies confirm that key components like feature alignment enhance its performance balance across metrics. Our findings demonstrate KD's potential to enhance transfer learning in remote sensing, offering a scalable, domain-robust tool for ecological monitoring and sustainable forest management.

---


### 585. [Measurement Geometry and Design for Trustworthy Generative Inverse Problems](https://arxiv.org/abs/2606.02309)

**<font color=#1a73e8>作者：</font>** Pengfei Jin, Na Li, Quanzheng Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative models are increasingly used as priors for inverse problems, but their ability to produce realistic images creates a basic trust problem: a plausible reconstruction may be supported by the measurements, or it may be filled in by the prior along unobserved directions. This distinction is especially important in medical imaging, where acquisition operators are designed under scan-time, dose, and calibration constraints. We study generative inverse problems from a measurement-geometry perspective. The central question is whether a fixed measurement operator can distinguish nearby images that are plausible under the generative prior, and whether this relationship can guide better measurements. We introduce a local measurement-manifold compatibility measure that quantifies how well the operator observes prior-relevant tangent directions. Under local regularity assumptions, we prove that this quantity controls the stable part of the reconstruction error, while the generative prior controls off-manifold drift. This worst-direction certificate motivates practical fixed and sequential acquisition rules based on overall local volume preservation, including a posterior-cloud design that adapts measurements at test time without training a sampling policy. Across row-sampling, tomographic, and MR acquisition settings, the proposed scores predict failure modes, explain measurement-induced hallucinations, and guide better sampling. In fastMRI Cartesian sampling, posterior-cloud measurement design improves over strong non-learned ACS-preserving baselines, including variable-density and Poisson-like masks.

---


### 586. [Deep Learning for Remote Sensing to Improve Flood Inundation Mapping](https://arxiv.org/abs/2606.02310)

**<font color=#1a73e8>作者：</font>** Yogesh Bhattarai, Vijay Chaudhary, Wai Lim Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Flooding is the most pervasive natural disaster worldwide. Timely and accurate flood inundation mapping are essential for informing disaster risk management. Optical satellite missions provide high-resolution, multispectral observations critical for flood detection and inundation mapping. However, their operational utility is severely constrained by cloud cover during extreme precipitation events. Conventional cloud-removal techniques based on temporal compositing or interpolation often fail to capture inundation dynamics. In this study, we introduce a cloud-removal framework for flood imagery based on Denoising Diffusion Probabilistic Models, leveraging the Masked Diffusion Transformer architecture. The proposed approach exploits self-attention mechanisms to capture wider spatial context and employs masked token modeling to explicitly learn the reconstruction of cloud-obscured regions. Trained on multispectral Sentinel-2B flood scenes with realistic cloud patterns, the model generates cloud-free image realizations that preserve both visual fidelity and hydrological consistency. Reconstruction performance is evaluated using standard image quality metrics alongside flood-specific hydrological measures, demonstrating improved continuity of water bodies and preservation of spectral signatures critical for water detection indices. The results indicate that diffusion-based generative modeling offers a robust and physically consistent alternative for cloud removal in optical flood monitoring, enabling more reliable, continuous observations to support disaster risk management and flood-related decision making.

---


### 587. [TVIR: Building Deep Research Agents Towards Text--Visual Interleaved Report Generation](https://arxiv.org/abs/2606.02320)

**<font color=#1a73e8>作者：</font>** Xinkai Ma, Zhiqi Bai, Dingling Zhang 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deep Research Agents have shown strong capability in multi-step information retrieval, reasoning, and long-form report generation, but existing benchmarks and systems remain predominantly text-centric, with limited evaluation of whether visual elements are factually reliable and well aligned with the surrounding analysis. To address this gap, we introduce TVIR (Text--Visual Interleaved Report Generation), which includes TVIR-Bench, a benchmark of 100 expert-curated multimodal deep research tasks that require visual elements to serve specific analytical sub-goals, and TVIR-Agent, a hierarchical multi-agent framework that serves as a strong baseline for constructing outlines, retrieving images, generating charts with traceable sources, and composing reports through context-aware sequential writing. We further develop a dual-path evaluation framework that combines Textual Assessment and Visual Assessment. Experiments across nine deep research systems show that TVIR-Agent achieves strong overall performance, underscoring the importance of explicit multimodal design and evaluation for evidence-driven report generation.

---


### 588. [Repair Before Veto: Repair-Augmented Constraint Learning for Contextual Decisions](https://arxiv.org/abs/2606.02326)

**<font color=#1a73e8>作者：</font>** Yifan Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hard constraints are usually treated as terminal vetoes: once a candidate violates a requirement, the learned rule rejects it and any repair is handled outside the decision semantics. This misses a common deployed regime in which the system already knows a finite menu of modifications, such as adding a ticket option, changing a configuration, or requesting an available service upgrade. Existing constraint-learning, soft-relaxation, and recourse methods address nearby problems, but they do not learn whether an option should be repaired before being vetoed. We introduce Repair-Augmented Constraint Learning (RACL), a contextual decision framework that lifts known repair operators into the classifier semantics. A candidate is accepted when an affordable repair makes it feasible and preferred enough; otherwise the system returns a structured rejection credit and, when applicable, a repair plan. This repair-before-veto view strictly generalizes no-repair HASSLE-style semantics, reveals an irreducible false-veto gap for terminal-veto rules, separates binary-label non-identifiability from decision-rule learnability, and gives capacity and calibration bounds for the observed-feasibility shared-weight setting. Across controlled and DB1B-derived benchmarks, RACL recovers the intended credit and repair structure. On the hardest raw-data-derived tier, validation-selected RACL reduces false vetoes to 10/4039 (FVR 0.0025), versus about 1064/4039 for the strongest repair-search black-box baseline, while making the FVR/EDR trade-off explicit.

---


### 589. [Riemannian Gradient Descent for Low-Rank Architectures](https://arxiv.org/abs/2606.02328)

**<font color=#1a73e8>作者：</font>** Nicholas Knight  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We explore Riemannian optimization techniques for rank-factored matrix parameters, targeting contemporary deep learning applications. We examine ten points in the algorithm design space: two geometries for rank-$r$ matrices, three geometries for rank-$r$ partial isometries, and block-matrix variants of these five, where factors are shared across block-rows and block-columns. We apply our methods to the multihead attention parameters in small language models. After tuning learning rates, our methods do not conclusively outperform an AdamW baseline. Our implementations are available online.

---


### 590. [Hallucination-Aware Diffusion Sampling for Inverse Problems via Robust Prior Updates](https://arxiv.org/abs/2606.02331)

**<font color=#1a73e8>作者：</font>** Pengfei Jin, Yiqi Tian, Kailong Fan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based inverse problem solvers can produce realistic reconstructions, but realism alone does not ensure that the recovered details are supported by the measurement. We study this failure as measurement-conditioned hallucination: visually meaningful content that is either implausible or inconsistent with the measured instance. Our analysis separates Bayes-rule-based diffusion inverse solvers into a prior update and a measurement-conditioning step, showing that hallucinated content can enter through the prior-side proposal before the measurement correction is applied. Motivated by this view, we propose Robust Prior Update (RPU), a solver-level module that probes the local stability of the diffusion prior update, re-anchors the resulting displacement at the current iterate, and leaves the measurement update unchanged. We instantiate RPU in DPS and evaluate it on FFHQ and ImageNet inverse problems using automatic metrics and human faithfulness studies. On FFHQ, RPU improves PSNR and LPIPS over DPS across box inpainting, Gaussian deblurring, and motion deblurring. In human judgments, RPU receives 91.9% of blind non-tie majority preferences and 91.1% of ground-truth-assisted non-tie preferences on FFHQ box inpainting, while the ImageNet Gaussian reader study is tie-heavy but favors RPU among non-tie cases. These results support a targeted claim: robustifying the prior update can improve instance faithfulness in diffusion inverse solvers, especially when the prior shapes weakly constrained content.

---


### 591. [Forget Attention: Importance-Aware Attention Is All You Need](https://arxiv.org/abs/2606.02332)

**<font color=#1a73e8>作者：</font>** Soohyeong Shin, Yeongwook Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Combining attention's global retrieval with the sequential importance signal of state space models (SSMs) is the open challenge of hybrid language modeling. Transformers see everywhere but cannot prioritize; SSMs know what matters but cannot revisit. Existing hybrids -- Jamba (block level) and Hymba (head level) -- place the two in separate compartments, so neither informs the other during the attention computation itself. We propose SISA (SSM-Informed Softmax Attention), which adds an SSM-derived importance term directly inside the attention score and realizes the full operation as a single SDPA call on augmented query/key vectors -- no recurrent state, no custom kernel. At 152M / 5B tokens, SISA reaches LAMBADA-greedy 17.3% (vs. Transformer 13.9 and Mamba-3 15.5) and attains NIAH 100% from step 1K, 7x faster than Transformer's retrieval convergence; at 369M, Mamba-3 leads LAMBADA while SISA preserves perfect NIAH and stock-SDPA execution. SISA thus defines a third design axis for SSM-attention hybrids -- score-level fusion -- beyond the block-level and head-level paradigms that have dominated the field.

---


### 592. [Coordination Graphs for Constrained Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2606.02337)

**<font color=#1a73e8>作者：</font>** Santiago Amaya-Corredor, Miguel Calvo-Fullana, Anders Jonsson  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Constrained Multi-agent reinforcement learning (CMARL) faces two intertwined challenges: the joint action space grows exponentially with the number of agents, and additional requirements couple agents in ways that reward structure alone does not capture. We introduce Coordination Graphs for Constrained Multi-Agent Reinforcement Learning (CG-CMARL), a framework that addresses both challenges by combining coordination graphs with Lagrangian duality. The system decomposes the joint problem into pairwise regions, each served by a set of shared Q-functions, one for the primary objective and one for each of the constraints, so that the number of learned models is independent of the number of agents. At execution time, Max-Sum message passing coordinates actions across the factor graph, while a Lagrangian multiplier controls the objective--constraint tradeoff, allowing a single trained model to trace a Pareto front without retraining. We provide convergence guarantees under mild conditions, together with a compositional error bound that decomposes into separate interpretable sources, each traceable to a specific design choice and independently controllable. Experiments on cooperative navigation tasks (where teams of up to 10 agents must coordinate to reach target positions while satisfying pairwise constraints) show that our method produces Pareto fronts dominating established baselines trained at fixed reward-shaping ratios, while scaling to team sizes where centralized approaches become intractable.

---


### 593. [Entropy Minimization without Model Collapse: Mitigating Prediction Bias in Medical Imaging](https://arxiv.org/abs/2606.02339)

**<font color=#1a73e8>作者：</font>** Tim Nielen, Sameer Ambekar, Johannes Kiechle 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Entropy minimization (EM) is the dominant objective for test-time adaptation, yet its failure mode, model collapse, remains poorly understood. In this work, we show that distribution shifts can cause feature clusters corresponding to distinct classes in the model's representation space to merge, while the decision boundary remains fixed. This induces a systematic skew in the predicted class distribution, referred to as prediction bias. Prediction bias refers to a shift in the predicted class distribution, with some classes overrepresented and others suppressed. We show that entropy minimization amplifies this prediction bias by tightening the existing clusters, reinforcing the incorrect groupings until all predictions collapse to a trivial solution. Next, to demonstrate the significance of prediction bias and mitigate it, we further propose Distribution Shift Bias Reduction (DSBR), a bias-correcting objective that specifically targets this failure mode by equalizing the contribution of each predicted class to the unsupervised entropy minimization loss. To study this failure mode, we design suitable adaptation settings using four medical-imaging datasets and additionally evaluate on ImageNet-C. We find that DSBR consistently stabilizes test-time adaptation, prevents model collapse, and matches or outperforms state-of-the-art methods. Moreover, DSBR operates solely at test-time.

---


### 594. [Detecting Pen-In-Air States from Video: A Proof-of-Concept Toward Complementary Handwriting Analysis](https://arxiv.org/abs/2606.02342)

**<font color=#1a73e8>作者：</font>** Lauren Sismeiro, Remy Plastre, Binbin Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic aspects of handwriting are critical for assessing developmental disorders such as dysgraphia and are typically captured using digitizing tablets. However, tablet-based sensing restricts analysis of Pen-Up behavior to a short proximity range above the writing surface, potentially missing high-lift in-air movements. As a proof of concept, we investigate whether top-view video can provide a complementary source of information for inferring pen-contact states without relying on tablet proximity sensing. We propose an interpretable hybrid pipeline combining pen-tip tracking using a YOLO-based detector with kinematic feature extraction and machine learning classification. A pilot dataset of diverse handwriting videos was manually annotated at the frame level and evaluation used a Leave-One-Video-Out (LOVO) protocol. The method achieved reliable event-level detection of Pen-Up segments, with an F_2 score up to 0.805, consistent with the emphasis on recall in a screening-oriented setting. These results support the feasibility of video-based Pen-Up detection as a low-cost and non-intrusive complement to digitizing tablets, and provide a foundation for future large-scale studies.

---


### 595. [I-(OT)^2: A Client-optimal Oblivious Transfer Protocol for IoT Devices](https://arxiv.org/abs/2606.02344)

**<font color=#1a73e8>作者：</font>** Elia Onofri, Andrea Ciccotelli, Roberto Di Pietro  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Oblivious Transfer (OT) is a fundamental cryptographic primitive enabling privacy-preserving computation and constitutes a core building block for secure multi-party computation while supporting a wide range of security-sensitive applications: private information retrieval, zero-knowledge proofs, and password-authenticated key exchange, to cite a few. While recent advances in OT extension have significantly reduced amortised costs, their reliance on batches of random base OTs and substantial pre-computation phases limits their practicality in scenarios where the number of transfers is modest or where communication latency and client-side computation are critical constraints. In such settings, efficient base OT protocols remain both relevant and necessary. In this work, we introduce $I$-$(OT)^2$, a novel base 1-out-of-2 OT protocol grounded in the quadratic residuosity problem, specifically designed to minimise receiver-side computation and interaction. Our construction is particularly appealing on client--server architectures in which the receiver operates on low-power hardware, such as Internet of Things (IoT) devices. Through a lightweight offline pre-computation phase, $I$-$(OT)^2$ shifts the on-transfer computational burden almost entirely to the Sender, while reducing online communication to only six messages and four digests exchanged. We provide a detailed description of the protocol, accompanied by a formal proof of its security. Moreover, to demonstrate the viability of $I$-$(OT)^2$, we also present an open-source proof-of-concept implementation (in C language) evaluated on real IoT hardware. Results are staggering: for 128-bit security using a 3072-bit RSA modulus, the receiver incurs an average online cost per OT as low as 2.80 {\mu}s on desktop platforms and 39.90 {\mu}s on IoT devices, more than 10$\times$ faster than the well known SimplestOT.

---


### 596. [VEDAL: Variational Error-Driven Asynchronous Learning for 3D Gaussian Splatting Pruning](https://arxiv.org/abs/2606.02346)

**<font color=#1a73e8>作者：</font>** Aoduo Li, Jiancheng Li, Huan Ye 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) achieves remarkable novel view synthesis quality with real-time rendering, yet suffers from excessive memory consumption due to millions of Gaussian primitives. Existing pruning methods rely on heuristic importance scores or synchronous batch updates, leading to suboptimal compression and training instability. We propose VEDAL, a principled framework that formulates Gaussian pruning as variational free energy minimization. Our approach introduces (1) a prediction-error gating mechanism that asynchronously activates pruning based on per-Gaussian reconstruction uncertainty, and (2) a variational uncertainty head that models pruning decisions as latent variables with learnable priors. The free energy objective naturally balances reconstruction fidelity against model complexity through an information-theoretic lens. Extensive experiments on Mip-NeRF 360, Tanks&Temples, and Deep Blending demonstrate that VEDAL achieves 5.2x compression with only 0.31 dB PSNR drop, outperforming PUP 3D-GS by +0.05 dB at a higher compression ratio and LightGaussian by +0.35 dB at comparable quality, while maintaining real-time rendering at 185 FPS.

---


### 597. [TROPHIES: Temporal Reconstruction of Places, Humans, and Cameras from Multi-view Videos](https://arxiv.org/abs/2606.02350)

**<font color=#1a73e8>作者：</font>** Jinpeng Liu, Yukang Xu, Yutong Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing humans and their surrounding environments in a globally consistent 4D space is essential for comprehensive perception. However, prior works typically assume single-view inputs or decouple humans, scenes, and cameras, making them unable to recover coherent geometry, stable motion, and physically aligned trajectories. These limitations motivate us to introduce a new task: unified human-scene-camera reconstruction from multi-view videos, which aims to jointly estimate dynamic humans, static scenes, and camera poses in one global coordinate frame. We propose TROPHIES--Temporal Reconstruction of Places, Humans, and Cameras from Multi-view Videos-a unified framework tailored for this task. TROPHIES features a Human Branch that models humans through temporal and spatial reasoning, and a Scene Branch that reconstructs static geometry with human-aware attention. A global alignment and optimization module couples both branches by enforcing scale consistency, contact priors, and cross-view temporal coherence. Experiments on EgoHuman and EgoExo4D demonstrate that TROPHIES achieves globally aligned, physically plausible 4D reconstructions and consistently outperforms existing paradigms in both global fidelity and human-scene consistency.

---


### 598. [Local Preferential Bayesian Optimization](https://arxiv.org/abs/2606.02351)

**<font color=#1a73e8>作者：</font>** Johanna Menn, Miriam Kober, Paul Brunzema 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian optimization (BO) is a popular and effective approach for tuning expensive, noisy experiments, but requires the formulation of an explicit objective function. Preferential BO (PBO) removes this requirement by learning from pairwise human feedback, yet existing methods struggle to efficiently optimize beyond low- and medium-dimensional problems due to their global search approaches. We address this limitation by developing a family of local PBO methods that transfer key ideas from high-dimensional BO to the preferential setting. In particular, we introduce local PBO methods which adapt trust-region and derivative-informed local search to pairwise preference feedback, where the latter exploits first- and second-order derivatives of the Laplace-approximated GP posterior. Our benchmark on GP sample paths, standard optimization benchmark functions, and policy-search tasks shows that local PBO methods are especially effective in high-dimensional and complex landscapes with steep optima. Compared with global preference-based baselines, they can substantially reduce cumulative regret, making them particularly useful for real-world preference-based optimization tasks such as policy search.

---


### 599. [Minimax-Optimal Policy Regret in Partially Observable Markov Games](https://arxiv.org/abs/2606.02363)

**<font color=#1a73e8>作者：</font>** Raman Arora  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study sequential decision-making in partially observable environments against strategic, adaptive opponents, modeled as partially observable Markov games (POMGs). The central challenge is to learn latent dynamics from partial observations while facing an adversary whose behavior depends on the learner's strategy, making standard regret notions inadequate. We prove that an epoch-based optimistic maximum-likelihood algorithm achieves $\tilde{O}(\sqrt{T})$ policy regret for fixed problem parameters, with explicit dependence on the horizon, adversary memory, confidence radius, and the aggregate Eluder dimension of the observable-operator class. The algorithm selects one policy per geometrically growing epoch using confidence sets built cumulatively from past data, which keeps the cost of comparing adversary responses across policies logarithmic in $T$. We also prove a lower bound matching the $\sqrt{T}$ and aggregate-Eluder-dimension dependence, up to problem-dependent and logarithmic factors. Finally, we extend the framework to horizon-adaptive guarantees and adversaries with geometric fading memory.

---


### 600. [FOAM: Frequency and Operator Error-Based Adaptive Damping Method for Reducing Staleness-Oriented Error for Shampoo](https://arxiv.org/abs/2606.02365)

**<font color=#1a73e8>作者：</font>** Kyunghun Nam, Sumyeong Ahn  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Shampoo is attracting considerable attention for its superior performance on large-scale optimization benchmarks; yet it faces a significant practical bottleneck: the prohibitive computational overhead of matrix inversion. To mitigate this, practitioners typically rely on stale preconditioner updates, creating a fundamental trade-off between computational efficiency and optimization fidelity. In this work, we provide a theoretical study of staleness through the complementary lenses of convergence and stability. While staleness improves computational efficiency, it inherently degrades performance and introduces numerical instability. Crucially, we identify that damping, acting as a numerical stabilizer, can effectively suppress these negative effects. Guided by this analysis, we propose FOAM, an adaptive algorithm that stabilizes training by dynamically controlling both the damping factor and the eigendecomposition frequency based on an approximation of the staleness-oriented error. Experimental results demonstrate that FOAM reduces wall-clock time compared to standard Shampoo while maintaining robust convergence.

---


> [!TIP]
> 当前位于：**551-600**（第 12/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | **551-600** | [601-650](./part-13.md) | [651-651](./part-14.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
