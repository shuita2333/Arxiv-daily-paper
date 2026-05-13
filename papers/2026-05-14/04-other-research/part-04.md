# 📦 其他研究 | 2026年05月14日

> 本类共 **396** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-396](./part-08.md)

---

### 151. [The DAWN of World-Action Interactive Models](https://arxiv.org/abs/2605.11550)

**<font color=#1a73e8>作者：</font>** Hongbo Lu, Liang Yao, Chenghao He 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A plausible scene evolution depends on the maneuver being considered, while a good maneuver depends on how the scene may evolve. Existing World Action Models (WAMs) largely miss this reciprocity, treating world prediction and action generation as either isolated parallel branches or rigid predict-then-plan pipelines. We formalize this perspective as World-Action Interactive Models (WAIMs), and instantiate it in autonomous driving with \textbf{DAWN} (\textbf{D}enoising \textbf{A}ctions and \textbf{W}orld i\textbf{N}teractive model), a simple yet strong latent generative baseline. DAWN operates in a compact semantic latent space and couples a \emph{World Predictor} with a \emph{World-Conditioned Action Denoiser}: the predicted world hypothesis conditions action denoising, while the denoised action hypothesis is fed back to update the world prediction, so that both are recursively refined during inference. Rather than eliminating test-time world evolution altogether or rolling out the full future in pixel space, DAWN performs a short explicit latent rollout that is sufficient to support long-horizon trajectory generation in complex interactive scenes. Experiments show that DAWN achieves strong planning performance and favorable safety-related results across multiple autonomous driving benchmarks. More broadly, our results suggest that interactive world-action generation is a principled path toward truly actionable world models.

---


### 152. [VNDUQE: Information-Theoretic Novelty Detection using Deep Variational Information Bottleneck](https://arxiv.org/abs/2605.11551)

**<font color=#1a73e8>作者：</font>** Aryan Gondkar, Hayder Radha, Yiming Deng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Detecting out-of-distribution (OOD) samples is critical for safe deployment of neural networks in safety-critical applications. While maximum softmax probability (MSP) provides a simple baseline, it lacks theoretical grounding and suffers from miscalibration. We propose VNDUQE (VIB-based Novelty Detection and Uncertainty Quantification for Nondestructive Evaluation), which investigates novelty detection through the Deep Variational Information Bottleneck (VIB), which explicitly constrains information flow through learned representations. We train VIB models on MNIST with held-out digit classes and evaluate OOD detection using information-theoretic metrics: KL divergence and prediction entropy. Our results reveal complementary detection signals: KL divergence achieves perfect detection (100\% AUROC on noise) on far-OOD samples (noise, domain shift), while prediction entropy excels at near-OOD detection (94.7\% AUROC on novel digit classes). A parallel detection strategy combining both metrics achieves 95.3\% average AUROC and 92\% true positive rate at 5\% false positive rate, which is a 32 percentage point improvement over baseline MSP (85.0\% AUROC, 60.1\% TPR). Compression via the information bottleneck principle ($\beta=10^{-3}$) reduces Expected Calibration Error by 38\%, demonstrating that information-theoretic constraints produce fundamentally more reliable uncertainty estimates. These findings directly support active learning with expensive computational oracles, where well-calibrated novelty detection enables principled threshold selection for oracle queries.

---


### 153. [A Controlled Counterexample to Strong Proxy-Based Explanations of OOD Performance: in a Fixed Pretraining-and-Probing Setup](https://arxiv.org/abs/2605.11554)

**<font color=#1a73e8>作者：</font>** Hongmin Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Task-agnostic structure proxies are often used to interpret why one pretraining corpus transfers better than another, but such explanations require the proxy to track the structure that matters for the downstream task. We test this requirement in a fixed pretraining-and-probing setup motivated by computationally bounded notions of learned structure, including epiplexity. The core question is whether a proxy ranking of two pretraining datasets must agree with their ranking by OOD probe accuracy. We show that it need not. First, we give a controlled construction in which a formal structure quantity, its operational proxy, and the task-relevant structure for a target family separate. We then instantiate the same mechanism in a synthetic sequence-model experiment: under the primary all-sample evaluation, the OOD accuracy ranking reverses the proxy ranking in two of three seeds, with auxiliary diagnostics and ablations supporting the same interpretation. The counterexample does not reject structure-based explanations in general; it identifies a boundary on strong proxy-based explanations. A proxy for total learned structure can fail to track the task-relevant structure that drives OOD performance, even in a controlled setting.

---


### 154. [ScribbleDose: Scribble-Guided Dose Prediction in Radiotherapy](https://arxiv.org/abs/2605.11555)

**<font color=#1a73e8>作者：</font>** Zhenxi Zhang, Yitao Zhuang, Yao Pu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Anatomical structure masks are widely adopted in radiotherapy dose prediction, as they provide explicit geometric constraints that facilitate structure-dose coupling. However, conventional manual delineation of these masks requires precise annotation of structure boundaries relevant to radiotherapy, which is time-consuming and labor-intensive. To address these limitations, we propose a scribble-guided dose prediction framework that relies solely on anatomical structures annotated with sparse scribbles. Specifically, we design a Scribble Completion Module (SCM) to generate dense anatomical masks by propagating sparse scribble labels to semantically similar voxels. During the propagation process, a supervoxel-based regularization is introduced to preserve geometric boundary consistency to ensure anatomical plausibility. Furthermore, we propose a Structure-Guided Dose Generation Module (SGDGM) to strengthen the correspondence between sparse structural cues and dose distribution. The completed dense masks derived from scribbles serve as structural guidance to condition dose prediction, forming a scribble-mask-dose learning pipeline under sparse annotation. Experiments on the GDP-HMM dataset demonstrate that ScribbleDose achieves competitive dose prediction performance using only sparse structural annotations. The source code and reannotated scribble annotations are publicly available at this https URL.

---


### 155. [Hindsight Hint Distillation: Scaffolded Reasoning for SWE Agents from CoT-free Answers](https://arxiv.org/abs/2605.11556)

**<font color=#1a73e8>作者：</font>** Shengjie Wang, Guanghe Li, Zonghan Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Solving complex long-horizon tasks requires strong planning and reasoning capabilities. Although datasets with explicit chain-of-thought (CoT) rationales can substantially benefit learning, they are costly to obtain. To address this challenge, we propose Hindsight Hint Distillation (HHD), which only requires easy-to-obtain question-answer pairs without CoT annotations. Inspired by how human teachers use student mistakes to provide targeted guidance, HHD synthesizes hindsight hints from the model's own failed self-rollouts and uses them to scaffold on-policy rollouts that successfully complete the tasks. The model then self-distills these scaffolded trajectories and generalizes to new problems without hint guidance. Experiments show that HHD significantly outperforms iterative RFT and trajectory-synthesis baselines, achieving an absolute improvement of 8\% on SWE-bench Verified, while all baselines improve by only around 2\%. Notably, the reasoning strategies induced by HHD generalize effectively to out-of-distribution tasks, yielding the largest gains on SWE-bench Multilingual despite no training on multilingual data. These results demonstrate that HHD can effectively synthesize expert-like reasoning from CoT-free data and substantially improve long-horizon performance.

---


### 156. [A Composite Activation Function for Learning Stable Binary Representations](https://arxiv.org/abs/2605.11558)

**<font color=#1a73e8>作者：</font>** Seokhun Park, Choeun Kim, Kwanho Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation functions play a central role in neural networks by shaping internal representations. Recently, learning binary activation representations has attracted significant attention due to their advantages in computational and memory efficiency, as well as interpretability. However, training neural networks with Heaviside activations remains challenging, as their non-differentiability obstructs standard gradient-based optimization. In this paper, we propose Heavy Tailed Activation Function (HTAF), a smooth approximation to the Heaviside function that enables stable training with gradient-based optimization. We construct HTAF as a sigmoid hyperbolic tangent composite function and theoretically show that it maintains a large gradient mass around zero inputs while exhibiting slower gradient decay in the tail regions. We show that Spiking Neural Networks, Binary Neural Networks and Deep Heaviside neural Networks can be trained stably using HTAF with gradient-based optimization. Finally, we introduce Implicit Concept Bottleneck Models (ICBMs), an interpretable image model that leverages HTAF to induce discrete feature representations. Extensive experiments across various architectures and image datasets demonstrate that ICBM enables stable discretization while achieving prediction performance comparable to or better than standard models.

---


### 157. [A Generative AI Driven Interactive Narrative Serious Fame for Stress Relief and Its Randomized Controlled Pilot Study](https://arxiv.org/abs/2605.11562)

**<font color=#1a73e8>作者：</font>** Ting-Chen Hsu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Background: Stress has become a widespread phenomenon, and serious games are increasingly recognized as engaging tools for stress relief. However, despite the rapid advancement of Generative Artificial Intelligence (Gen-AI), its integration into stress-relief serious games remains insufficiently explored. Objective: This study aimed to address this gap by developing "Reverie", an Gen-AI driven serious game powered by the Unity engine and ChatGPT, and to preliminarily evaluate its effectiveness in stress reduction, user experience, and cognitive emotion regulation. Methods: A 14-day pilot study was conducted with 20 students experiencing moderate to high levels of stress. Participants used "Reverie" as a stress-relief intervention. Stress levels, user experience, and cognitive emotion regulation strategies were assessed to examine the game's feasibility and preliminary efficacy. Results: The results showed that "Reverie" significantly reduced participants' stress levels over the intervention period (p=.016*), indicating a cumulative positive effect. In addition, the game demonstrated excellent user experience and was associated with improvements in cognitive emotion regulation strategies. Conclusions: This study proposes a Gen-AI driven design framework for serious games for stress relief. Besides, this pilot study provides initial support for the feasibility and promise of combining LLM-driven gameplay in a personalized digital intervention context.

---


### 158. [TCP-SSM: Efficient Vision State Space Models with Token-Conditioned Poles](https://arxiv.org/abs/2605.11563)

**<font color=#1a73e8>作者：</font>** Sara Shoouri, Morteza Tavakoli Taba, Hun-Seok Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> State Space Models (SSMs) have emerged as a compelling alternative to attention models for long-range vision tasks, offering input-dependent recurrence with linear complexity. However, most efficient SSM variants reduce computation cost by modifying scan routes, resolutions, or traversal patterns, while largely leaving the recurrent dynamics implicit. Consequently, the model's state-dependent memory behavior is difficult to control, particularly in compact backbones where long scan paths can exceed the effective memory horizon. We propose Token-Conditioned Poles SSM (TCP-SSM), a structured selective SSM framework that improves efficiency while making recurrence dynamics explicit and interpretable through stable poles. TCP-SSM builds each scan operator with 1) real poles that model monotone or sign-alternating decay, and 2) complex-conjugate poles that capture damped oscillatory responses. Using bounded radius and angle modulation, TCP-SSM converts shared base poles into token-dependent poles, allowing each scan step to adapt its memory behavior to the current visual token while preserving pole stability. For practical scalability, we integrate grouped pole sharing with a lightweight low-rank input pathway, yielding an efficient scan operator that preserves linear-time scan complexity. Across image classification, semantic segmentation, and object detection, TCP-SSM reduces SSM computation complexity up to 44% in Vision Mamba-style models while maintaining or surpassing baseline accuracy.

---


### 159. [Dynamic Execution Commitment of Vision-Language-Action Models](https://arxiv.org/abs/2605.11567)

**<font color=#1a73e8>作者：</font>** Feng Chen, Xianghui Wang, Yuxuan Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models predominantly adopt action chunking, i.e., predicting and committing to a short horizon of consecutive low-level actions in a single forward pass, to amortize the inference cost of large-scale backbones and reduce per-step latency. However, committing these multi-step predictions to real-world execution requires balancing success rate against inference efficiency, a decision typically governed by fixed execution horizons tuned per task. Such heuristics ignore the state-dependent nature of predictive reliability, leading to brittle performance in dynamic or out-of-distribution settings. In this paper, we introduce A3, an Adaptive Action Acceptance mechanism that reframes dynamic execution commitment as a self-speculative prefix verification problem. A3 first computes a trajectory-wise consensus score of actions via group sampling, then selects a representative draft and prioritizes downstream verification. Specifically, it enforces: (1) consensus-ordered conditional invariance, which validates low-consensus actions by judging whether they remain consistent when re-decoded conditioned on high-consensus actions; and (2) prefix-closed sequential consistency, which guarantees physical rollout integrity by accepting only the longest continuous sequence of verified actions starting from the beginning. Consequently, the execution horizon emerges as the longest verifiable prefix satisfying both internal model logic and sequential execution constraints. Experiments across diverse VLA models and benchmarks demonstrate that A3 eliminates the need for manual horizon tuning while achieving a superior trade-off between execution robustness and inference throughput.

---


### 160. [Dual-Temporal LSTM with Hybrid Attention for Airline Passenger Load Factor Forecasting: Integrating Intra-Flight and Inter-Flight Booking Dynamics](https://arxiv.org/abs/2605.11569)

**<font color=#1a73e8>作者：</font>** ASM Nazrul Islam, Md. Hasanul Kabir, Md. Liakot Ali 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate short-term demand forecasting is crucial to airline revenue management, yet most existing systems fail to meet this need because current models treat booking data as a single temporal dimension, either the accumulation of bookings for a specific flight or the historical booking profile of the same route. This unidimensional view discards information carried by the other temporal stream and forecasting absolute passenger counts introduces a further operational fragility when change in planned aircraft type alters total seat capacity. This study addresses both limitations. A dual-stream Long Short-Term Memory (LSTM) integrated with attention framework is proposed that simultaneously processes two complementary input sequences: a horizontal sequence capturing intra-flight booking accumulation over the days preceding departure, and a vertical sequence capturing inter-flight booking patterns at fixed days-before-departure offsets across historical flights. Multiple dual-stream architectural variants, combining self-attention, cross-attention, and hybrid attention with concatenation, residual, and gated fusion strategies, are developed and evaluated. Experiments on real-world reservation data from the national airline of Bangladesh, Biman Bangladesh Airlines (BBA), demonstrate that the proposed hybrid model achieves a Mean Absolute Error of 2.8167 and a coefficient of determination ($R^{2}$) of 0.9495, outperforming single-stream baselines, tree-based models, and three prior dual-LSTM architectures applied to the same data. Validation across four flight category pairs; domestic versus international, direct versus transit, high versus low frequency, and short versus mid versus long haul confirms that the model generalizes across operationally diverse route types. Biman Bangladesh Airlines (BBA) has officially integrated this methodology into its operations.

---


### 161. [OUI as a Structural Observable: Towards an Activation-Centric View of Neural Network Training](https://arxiv.org/abs/2605.11570)

**<font color=#1a73e8>作者：</font>** Alberto Fernández-Hernández, Jose I. Mestre, Cristian Pérez-Corral 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation functions are what make deep networks expressive: without them, the model collapses to a linear map. Yet we still evaluate training mostly from the outside, through loss, accuracy, return, or final calibration, while the internal structural evolution of the network remains largely unobserved. In this paper, we argue that the Overfitting--Underfitting Indicator (OUI) should be understood as a first practical observable of that internal structure. Across our recent results, OUI consistently appears as an early, label-free, activation-based signal that reveals whether a network is entering a poor or promising training regime before convergence. In supervised learning, it anticipates weight decay regimes; in reinforcement learning, it discriminates learning-rate regimes early in PPO actor--critic; and in online control, it can drive layer-wise weight decay adaptation. Read together with recent evidence that activation patterns tend to stabilize earlier than parameters, these results suggest a broader research direction: an activation-centric theory of training dynamics. OUI is becoming an empirical foothold toward this theory.

---


### 162. [FedOUI: OUI-Guided Client Weighting for Federated Aggregation](https://arxiv.org/abs/2605.11571)

**<font color=#1a73e8>作者：</font>** Alberto Fernández-Hernández, Jose I. Mestre, Cristian Pérez-Corral 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning usually aggregates client updates using dataset size or gradient-level criteria, while overlooking internal signals about how each client model is organizing its input space during training. We introduce FedOUI, a simple aggregation rule based on the Overfitting-Underfitting Indicator (OUI), an activation-based and label-free metric. Each participating client sends its local update together with a OUI value computed on a fixed probe batch, and the server estimates the round-wise OUI distribution to assign lower weights to structurally atypical clients through a smooth reweighting rule. We evaluate FedOUI on CIFAR-10 under strong non-IID partitioning and noisy-client conditions, comparing it with FedAvg, FedProx, and a gradient-alignment baseline. The clearest gains appear under strong heterogeneity, where OUI-based weighting improves aggregation quality while remaining lightweight and interpretable. These results show that internal activation structure can provide useful information for federated aggregation beyond client size and gradient geometry.

---


### 163. [TB-AVA: Text as a Semantic Bridge for Audio-Visual Parameter Efficient Finetuning](https://arxiv.org/abs/2605.11572)

**<font color=#1a73e8>作者：</font>** Seongah Kim, Dinh Phu Tran, Hyeontaek Hwang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio-visual understanding requires effective alignment between heterogeneous modalities, yet cross-modal correspondence remains challenging when temporally aligned audio and visual signals lack clear semantic this http URL propose to use text as a semantic anchor for audio-visual representation this http URL this end, we introduce a parameter-efficient adaptation frameworkbuilt on frozen audio and visual encoders, centered on Text-Bridged Audio-Visual Adapter (TB-AVA), which enables text-mediated interaction between audio and visual streams. At the core of TB-AVA, Gated Semantic Modulation (GSM) selectively modulates feature channels based on text-inferred semantic relevance. We evaluate the proposed approach on multiple benchmarks, including AVE, AVS, and AVVP, where the proposed framework achieves state-of-the-art performance, demonstrating text as an effective semantic anchor for parameter-efficient fine-tuning (PEFT) in audio-visual learning.

---


### 164. [BitLM: Unlocking Multi-Token Language Generation with Bitwise Continuous Diffusion](https://arxiv.org/abs/2605.11577)

**<font color=#1a73e8>作者：</font>** Shaobin Zhuang, Yuang Ai, Jiaming Han 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autoregressive language models generate text one token at a time, yet natural language is inherently structured in multi-token units, including phrases, n-grams, and collocations that carry meaning jointly. This one-token bottleneck limits both the expressiveness of the model during pre-training and its throughput at inference time. Existing remedies such as speculative decoding or diffusion-based language models either leave the underlying bottleneck intact or sacrifice the causal structure essential to language modeling. We propose BitLM, a language model that represents each token as a fixed-length binary code and employs a lightweight diffusion head to denoise multiple tokens in parallel within each block. Crucially, BitLM preserves left-to-right causal attention across blocks while making joint lexical decisions within each block, combining the reliability of autoregressive modeling with the parallelism of iterative refinement. By replacing the large-vocabulary softmax with bitwise denoising, BitLM reframes token generation as iterative commitment in a compact binary space, enabling more efficient pre-training and substantially faster inference without altering the causal foundation that makes language models effective. Our results demonstrate that the one-token-at-a-time paradigm is not a fundamental requirement but an interface choice, and that changing it can yield a stronger and faster language model. We hope BitLM points toward a promising direction for next-generation language model architectures.

---


### 165. [The Midas Touch for Metric Depth](https://arxiv.org/abs/2605.11578)

**<font color=#1a73e8>作者：</font>** Yu Ma, Zizhan Guo, Zuyi Xiong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances have markedly improved the cross-scene generalization of relative depth estimation, yet its practical applicability remains limited by the absence of metric scale, local inconsistencies, and low computational efficiency. To address these issues, we present \emph{\textbf{M}idas \textbf{T}ouch for \textbf{D}epth} (MTD), a mathematically interpretable approach that converts relative depth into metric depth using only extremely sparse 3D data. To eliminate local scale inconsistencies, it applies a segment-wise recovery strategy via sparse graph optimization, followed by a pixel-wise refinement strategy using a discontinuity-aware geodesic cost. MTD exhibits strong generalization and achieves substantial accuracy improvements over previous depth completion and depth estimation methods. Moreover, its lightweight, plug-and-play design facilitates deployment and integration on diverse downstream 3D tasks. Project page is available at this https URL.

---


### 166. [A Mixture Autoregressive Image Generative Model on Quadtree Regions for Gaussian Noise Removal via Variational Bayes and Gradient Methods](https://arxiv.org/abs/2605.11585)

**<font color=#1a73e8>作者：</font>** Shota Saito, Yuta Nakahara, Kohei Horinouchi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper addresses the problem of image denoising for grayscale images. We propose a probabilistic image generative model that combines a quadtree region-partitioning model with a mixture autoregressive model, and propose a framework that reduces MAP (maximum a posteriori)-estimation-based denoising to the maximization of a variational lower bound. To maximize this lower bound, we develop an algorithm that alternately applies variational Bayes and gradient methods. We particularly demonstrate that the gradient-based update rule can be computed analytically without numerical computation or approximation. We carried out some experiments to verify that the proposed algorithm actually removes image noise and to identify directions for future improvement.

---


### 167. [SoK: Unlearnability and Unlearning for Model Dememorization](https://arxiv.org/abs/2605.11592)

**<font color=#1a73e8>作者：</font>** Mengying Zhang, Derui Wang, Ruoxi Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Advanced model dememorization methods, including availability poisoning (unlearnability) and machine unlearning, are emerging as key safeguards against data misuse in machine learning (ML). At the training stage, unlearnability embeds imperceptible perturbations into data before release to reduce learnability. At the post-training stage, unlearning removes previously acquired information from models to prevent unauthorized disclosure or use. While both defenses aim to preserve the right to withhold knowledge, their vulnerabilities and shared foundations remain unclear. Specifically, both unlearnability and unlearning suffer from issues such as shallow dememorization, leading to falsely claimed data learnability reduction or forgetting in the presence of weight perturbations. Moreover, input perturbations may affect the effectiveness of downstream unlearning, while unlearning may inadvertently recover domain knowledge hidden by unlearnability. This interplay calls for deeper investigation. Finally, there is a lack of formal guarantees to provide theoretical insights into current defenses against shallow dememorization. In this Systematization of Knowledge, we present the first integrated analysis of model dememorization approaches leveraging unlearnability and unlearning. Our contributions are threefold: (i) a unified taxonomy of unlearnability and scalable unlearning methods; (ii) an empirical evaluation revealing the robustness, interplay, and shallow dememorization of leading methods; and (iii) the first theoretical guarantee on dememorization depth for models processed through certified unlearning. These results lay the foundation for unifying dememorization mechanisms across the ML lifecycle to achieve a deeper immemor state for sensitive knowledge.

---


### 168. [PointForward: Feedforward Driving Reconstruction through Point-Aligned Representations](https://arxiv.org/abs/2605.11594)

**<font color=#1a73e8>作者：</font>** Cheng Chi, Xianqi Wang, Hongcheng Luo 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-fidelity reconstruction of driving scenes is crucial for autonomous driving. While recent feedforward 3D Gaussian Splatting (3DGS) methods enable fast reconstruction, their per-pixel Gaussian prediction paradigm often suffers from multi-view inconsistency and layering artifacts. Moreover, existing methods often model dynamic instances via dense flow prediction, which lacks explicit cross-view correspondence and instance-level consistency. In this paper, we propose PointForward, a feedforward driving reconstruction framework through point-aligned representations. Unlike pixel-aligned methods, we initialize sparse 3D queries in world space and aggregate multi-view image information via spatial-temporal fusion onto these queries, enforcing explicit cross-view consistency in a single feedforward pass. To handle scene dynamics, we introduce scene graphs that explicitly organize moving instances during reconstruction. By leveraging 3D bounding boxes, our method enables instance-level motion propagation and temporally consistent dynamic representations. Extensive experiments demonstrate that PointForward achieves state-of-the-art performance on large-scale driving benchmarks. The code will be available upon the publication of the paper.

---


### 169. [Native Explainability for Bayesian Confidence Propagation Neural Networks: A Framework for Trusted Brain-Like AI](https://arxiv.org/abs/2605.11595)

**<font color=#1a73e8>作者：</font>** Georgios Makridis, Georgios Fatouros, John Soldatos 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The EU Artificial Intelligence Act (Regulation 2024/1689), fully applicable to high-risk systems from August 2026, creates urgent demand for AI architectures that are simultaneously trustworthy, transparent, and feasible to deploy on resource-constrained edge devices. Brain-like neural networks built on the Bayesian Confidence Propagation Neural Network (BCPNN) formalism have re-emerged as a credible alternative to backpropagation-driven deep learning. They deliver state-of-the-art unsupervised representation learning, neuromorphic-friendly sparsity, and existing FPGA implementations that target edge deployment. Despite this momentum, no systematic framework exists for explaining BCPNN decisions -- a gap the present paper fills. We argue that BCPNN is, in the sense of Rudin's interpretable-by-design agenda, an inherently transparent model whose architectural primitives map directly onto established explainable-AI (XAI) families. We make four contributions. First, we propose the first XAI taxonomy for BCPNN. It maps weights, biases, hypercolumn posteriors, structural-plasticity usage scores, attractor dynamics, and input-reconstruction populations onto attribution, prototype, concept, counterfactual, and mechanistic explanation modalities. Second, we introduce sixteen architecture-level explanation primitives (P1--P16), several without analogue in standard ANNs. We provide closed-form algorithms for computing each from quantities the model already maintains. Third, we introduce five design-time Configuration-as-Explanation primitives (Config-P1 to Config-P5) that treat BCPNN hyperparameter choices as an auditable pre-deployment explanation artifact. Fourth, we sketch a roadmap for integration into industrial IoT deployments and discuss EU AI Act alignment, edge feasibility, and Industry 5.0 implications.

---


### 170. [EpiCastBench: Datasets and Benchmarks for Multivariate Epidemic Forecasting](https://arxiv.org/abs/2605.11598)

**<font color=#1a73e8>作者：</font>** Madhurima Panja, Danny D'Agostino, Huitao Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The increasing adoption of data-driven decision-making in public health has established epidemic forecasting as a critical area of research. Recent advances in multivariate forecasting models better capture complex temporal dependencies than conventional univariate approaches, which model individual series independently. Despite this potential, the development of robust epidemic forecasting methods is constrained by the lack of high-quality benchmarks comprising diverse multivariate datasets across infectious diseases and geographical regions. To address this gap, we present EpiCastBench, a large-scale benchmarking framework featuring 40 curated (correlated) multivariate epidemic datasets. These publicly available datasets span a wide range of infectious diseases and exhibit diverse characteristics in terms of temporal granularity, series length, and sparsity. We analyze these datasets to identify their global features and structural patterns. To ensure reproducibility and fair comparison, we establish standardized evaluation settings, including a unified forecasting horizon, consistent preprocessing pipelines, diverse performance metrics, and statistical significance testing. By leveraging this framework, we conduct a comprehensive evaluation of 15 multivariate forecasting models spanning statistical baselines to state-of-the-art deep learning and foundation models. All datasets and code are publicly available on Kaggle (this https URL) and GitHub (this https URL).

---


### 171. [DiffScore: Text Evaluation Beyond Autoregressive Likelihood](https://arxiv.org/abs/2605.11601)

**<font color=#1a73e8>作者：</font>** Wen Lai, Yingli Shen, Dingnan Jin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autoregressive language models are widely used for text evaluation, however, their left-to-right factorization introduces positional bias, i.e., early tokens are scored with only leftward context, conflating architectural asymmetry with true text quality. We propose masked reconstruction as an alternative paradigm, where every token is scored using full bidirectional context. We introduce DiffScore, an evaluation framework built on Masked Large Diffusion Language Models. By measuring text recoverability across continuous masking rates, DiffScore eliminates positional bias and naturally establishes an evaluation hierarchy from local fluency to global coherence. We further provide diagnostic tools unavailable to autoregressive frameworks: multi-timestep quality profiles that decompose scores across masking rates, and bidirectional PMI decomposition that disentangles fluency from faithfulness. Experiments across ten benchmarks show that DiffScore consistently outperforms autoregressive baselines in both zero-shot and fine-tuned settings. The code is released at: this https URL.

---


### 172. [Convolutional-Neural-Networks for Deanonymisation of I2P Traffic](https://arxiv.org/abs/2605.11606)

**<font color=#1a73e8>作者：</font>** Luca Rohrer, Konrad Baechler, Dieter Arnold  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This study investigates the potential for deanonymizing services within the Invisible Internet Project (I2P) network through passive traffic analysis and machine learning techniques. The primary objective is to identify distinctive patterns in I2P traffic despite the encryption of its payload. To achieve this, a controlled laboratory environment was established to generate synthetic I2P traffic, providing a training dataset for machine learning models. Furthermore, Fano's inequality is employed to perform a theoretical analysis of anonymous data transmission in mix networks such as I2P, thereby supporting a data-driven approach to uncover causal relationships. In computer experiments, advanced deep learning methods - particularly Convolutional Neural Networks - are applied within the laboratory I2P network, and their effectiveness is further evaluated using real-world traffic data. The results indicate that the proposed methodologies do not compromise the anonymity guarantees of the I2P network.

---


### 173. [PRISM: A Geometric Risk Bound that Decomposes Drift into Scale, Shape, and Head](https://arxiv.org/abs/2605.11608)

**<font color=#1a73e8>作者：</font>** Chieh-Yen Lin, Shao-Hua Sun  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Comparing post-training LLM variants, such as quantized, LoRA-adapted, and distilled models, requires a diagnostic that identifies how a variant has drifted, not only whether it has degraded. Existing similarity scores such as CKA and SVCCA can flag degradation, but they do not directly link representation drift to risk or mechanism. We propose PRISM, Proxy Risk Inference via Structural Mapping, which exploits the linear output head of LLMs and the empirically near-isometric structure of their backbones to derive a closed-form upper bound on the cross-entropy risk gap between a target model and a post-training variant. The bound is calibrated for variant ranking and decomposes drift into three independently measurable axes: scale mismatch, shape mismatch, and head divergence. Each axis corresponds to a distinct failure mode, including shape distortion under low-bit quantization, scale separability under LoRA forgetting, and head divergence under GGUF k-quantization. As a result, the dominant axis suggests a remediation direction rather than merely raising a degradation flag. Because the shape term is differentiable, the same geometry can also serve as a training-time regularizer against catastrophic forgetting. Across two model families and five benchmarks, PRISM ranks variants with mean Spearman correlations of 0.820 for post-training quantization and 0.831 for LoRA forgetting, and its axis-guided shape regularizer outperforms experience replay in aggregate at mitigating downstream forgetting.

---


### 174. [Anti-Self-Distillation for Reasoning RL via Pointwise Mutual Information](https://arxiv.org/abs/2605.11609)

**<font color=#1a73e8>作者：</font>** Guobin Shen, Xiang Cheng, Chenxiao Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation, where a student is pulled toward a copy of itself conditioned on privileged context (e.g., a verified solution or feedback), offers a promising direction for advancing reasoning capability without a stronger external teacher. Yet in math reasoning the gains are inconsistent, even when the same approach succeeds elsewhere. A pointwise mutual information analysis traces the failure to the privileged context itself: it inflates the teacher's confidence on tokens already implied by the solution (structural connectives, verifiable claims) and deflates it on deliberation tokens ("Wait", "Let", "Maybe") that drive multi-step search. We propose Anti-Self-Distillation (AntiSD), which ascends a divergence between student and teacher rather than descending it: this reverses the per-token sign and yields a naturally bounded advantage in one step. An entropy-triggered gate disables the term once the teacher entropy collapses, completing a drop-in replacement for default self-distillation. Across five models from 4B to 30B parameters on math reasoning benchmarks, AntiSD reaches the GRPO baseline's accuracy in 2 to 10x fewer training steps and improves final accuracy by up to 11.5 points. AntiSD opens a path to scalable self-improvement, where a language model bootstraps its own reasoning through its training signal.

---


### 175. [From Generic Correlation to Input-Specific Credit in On-Policy Self Distillation](https://arxiv.org/abs/2605.11613)

**<font color=#1a73e8>作者：</font>** Guobin Shen, Lei Huang, Xiang Cheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation has emerged as a promising paradigm for post-training language models, in which the model conditions on environment feedback to serve as its own teacher, providing dense token-level rewards without external teacher models or step-level annotations. Despite its empirical success, what this reward actually measures and what kind of credit it assigns remain unclear. Under a posterior-compatibility interpretation of feedback conditioning, standard in the implicit-reward literature, we show that the self-distillation token reward is a Bayesian filtering increment whose trajectory sum is exactly the pointwise mutual information between the response and the feedback given the input. This pMI can be raised by input-specific reasoning or by input-generic shortcuts, so we further decompose the teacher log-probability along the input axis. Based on this analysis, we propose CREDIT (Contrastive REward from DIsTillation), which isolates the input-specific component with a batch-contrastive baseline. At the sequence level, CREDIT is a teacher-side surrogate for a contrastive pMI objective that also penalizes responses remaining likely under unrelated inputs. Across coding, scientific reasoning, and tool-use benchmarks on two model families, CREDIT delivers the strongest aggregate performance at negligible additional compute.

---


### 176. [Grounding by Remembering: Cross-Scene and In-Scene Memory for 3D Functional Affordances](https://arxiv.org/abs/2605.11616)

**<font color=#1a73e8>作者：</font>** Qirui Wang, Jingyi He, Yining Pan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Functional affordance grounding requires more than recognizing an object: an agent must localize the specific region that supports an interaction, such as the handle to pull or the button to press. This is difficult for training-free vision-language pipelines because actionable regions are often small, visually ambiguous, and repeated across multiple same-category instances in a scene. We propose AFFORDMEM, a framework that grounds 3D functional affordances by remembering geometry at two levels. The first is cross-scene affordance memory: the agent maintains a category-level memory bank of RGB images with affordance regions rendered as overlays, and recalls the most informative examples at query time to guide a frozen VLM toward small operable subregions that text-only prompting consistently misses. The second is in-scene spatial memory: as the agent processes the scene, it organizes candidate instances and their 3D spatial relations into a structured scene graph, enabling the language model to resolve references over distant or currently unobserved candidates such as "the second handle from the top." AFFORDMEM requires no model fine-tuning and no target-scene annotation, using a reusable memory bank built from source scenes. On SceneFun3D, our method improves AP50 over the prior training-free state of the art by 3.23 on Split 0 and 3.7 on Split 1. Ablation studies support complementary benefits: cross-scene affordance memory improves fine-grained localization, while in-scene spatial memory provides the larger gain on spatially qualified queries. The project homepage is available at the project page.

---


### 177. [MIST: Reliable Streaming Decision Trees for Online Class-Incremental Learning via McDiarmid Bound](https://arxiv.org/abs/2605.11617)

**<font color=#1a73e8>作者：</font>** Phu-Hoa Pham, Chi-Nguyen Tran, Nguyen Lam Phu Quy 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Streaming decision trees are natural candidates for open-world continual learning, as they perform local updates, enjoy bounded memory, and static decision boundaries. Despite these, they still fail in online class-incremental learning due to two coupled miscalibrations: (i) their split criterion grows unreliable as the class count K expands, and (ii) the absence of knowledge transfer at split time. Both failures share a common root: the range of Information Gain intrinsically scales with log2 K. Consequently, any Hoeffding-style confidence radius derived from it must inevitably grow with the class count, making a K-independent split criterion structurally impossible, taking away the potential benefits of applying streaming decision trees to continual learning. To fix this issue, we present MIST (McDiarmid Incremental Streaming Tree), which resolves both failures through three integrated components: (i) a tight, K-independent McDiarmid confidence radius for Gini splitting that acts as a structural regulariser; (ii) a Bayesian inheritance protocol that projects parent statistics to child nodes via truncated-Gaussian moments, with variance reduction guarantees strongest precisely when splitting is most conservative; and (iii) per-leaf KLL quantile sketches that support both continuous threshold evaluation and geometry-adaptive leaf prediction from a single data structure. On standard and stress-test tabular streams, MIST is competitive with global parametric methods on near-Gaussian benchmarks and uniquely robust on non-Gaussian geometry where SOTA benchmarks collapse.

---


### 178. [PhishSigma++: Malicious Email Detection with Typed Entity Relations](https://arxiv.org/abs/2605.11619)

**<font color=#1a73e8>作者：</font>** Shang Shang, Ruiqi Wang, Ruijie Qi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Here is a further shortened version (pure text, no extra formatting, academic style preserved, no content change):
Abstract. With the rise of AI-generated content (AIGC), phishing actors now possess richer linguistic capabilities and evasion techniques. Most existing detectors over-rely on mutable textual features, achieving high accuracy on clean data but degrading severely under text-focused adversarial manipulation. This mirrors the lab-to-real performance gap. We investigate invariant signals in phishing emails: even when attackers modify surface text, functional intent constrains relations among typed entities. Threat-actor tradecraft is described via high-level TTPs, but rule-based systems like Sigma express invariants only through manually curated, field-specific patterns, limiting flexibility. We introduce PhishSigma++, an entity-relation-based malicious email detector for RFC822 messages that generalizes Sigma's design. It extracts 40 typed entity classes, computes 5 cross-type relations to build a typed email graph, and uses particle swarm optimization (PSO) to select a sparse discriminative mask, supporting classification and type-level evidence summary. On 29,142 messages, PhishSigma++ achieves 0.9675 F1 on clean data and outperforms text-centric baselines under non-adaptive Good Word padding at \r{ho}=0.8. It maintains 0.9579 F1, while a token-based Bayesian filter collapses to 0.0243 and a DistilBERT phishing checkpoint falls to 0.7284. Compared with traditional Sigma rules, PhishSigma++ offers higher detection, broader relational invariance coverage, and data-driven feature selection. We also show that thresholded typed relation scores encode a useful fragment of Sigma-style field conditions, unifying hand-crafted rule logic and learned relation masks in a single-email framework.

---


### 179. [RNA-FM: Flow-Matching Generative Model for Genome-wide RNA-Seq Prediction](https://arxiv.org/abs/2605.11622)

**<font color=#1a73e8>作者：</font>** Yaxuan Song, Jianan Fan, Tianyi Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Histopathology whole-slide images (WSIs) are routinely acquired in clinical practice and contain rich tissue morphology but lack direct molecular architecture and functional programs defining pathological states, whereas RNA sequencing (RNA-seq) provides genome-wide transcriptional profiles at substantial cost, thereby motivating WSI-based genome-wide transcriptomic prediction. Existing approaches for predicting gene expression from WSIs predominantly rely on deterministic regression with one-to-one mapping, limiting their ability to capture biological heterogeneity and predictive uncertainty. We propose RNA-FM, a flow-matching generative framework for genome-wide bulk RNA-seq prediction from WSIs. RNA-FM formulates transcriptomic prediction as a continuous-time conditional transport problem, learning a velocity field that maps a simple prior to the target gene expression distribution conditioned on morphologies. By integrating pathway-level structure, RNA-FM enables scalable and biologically interpretable genome-wide gene expression imputation. Extensive experiments demonstrate that RNA-FM consistently outperforms state-of-the-art approaches while maintaining biological meaningfulness. Code is available at this https URL.

---


### 180. [Nice Fold or Hero Call: Learning Budget-Efficient Thinking for Adaptive Reasoning](https://arxiv.org/abs/2605.11625)

**<font color=#1a73e8>作者：</font>** Zhaomeng Zhou, Lan Zhang, Junyang Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large reasoning models (LRMs) improve problem solving through extended reasoning, but often misallocate test-time compute. Existing efficiency methods reduce cost by compressing reasoning traces or conditioning budget on perceived difficulty, yet largely overlook solvability. As a result, they may spend large budgets on queries beyond the model's capability while compressing hard-but-solvable queries that require deeper reasoning. In this work, we formulate adaptive reasoning as a computational investment under uncertainty, where budget should follow the expected return of reasoning rather than perceived difficulty alone. To instantiate this principle, we propose Budget-Efficient Thinking (BET), a two-stage framework that combines behavioral cold-start with GRPO under an investment-cost-aware reward. By aligning solve-or-fold decisions with rollout-derived solvability, BET learns three behaviors: (1) short solve, answering easy queries concisely; (2) nice fold, abstaining early when continued reasoning has near-zero expected return; and (3) hero call, preserving sufficient compute for hard-but-solvable queries. Across seven benchmarks and three base models, BET reduces reasoning tokens by ~55% on average while achieving overall performance improvements, and transfers zero-shot from mathematical reasoning to scientific QA and logical reasoning with comparable efficiency gains.

---


### 181. [Single-Shot HDR Recovery via a Video Diffusion Prior](https://arxiv.org/abs/2605.11628)

**<font color=#1a73e8>作者：</font>** Chinmay Talegaonkar, Jinshi He, Christopher McKenna 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent generative methods for single-shot high dynamic range (HDR) image reconstruction show promising results, but often struggle with preserving fidelity to the input image. They require separate models to handle highlights and shadows, or sacrifice interpretability by directly predicting the final HDR image. We address these limitations by re-casting single-shot HDR reconstruction as conditional video generation and fusing the generated frames into an HDR image. We finetune a video diffusion model to generate an exposure bracket, conditioned on a low dynamic range (LDR) input. We fuse this image bracket using per-pixel weights predicted by a light-weight UNet. This formulation is simple, interpretable, and effective. Rather than directly hallucinating an HDR image, it explicitly reconstructs the intermediate exposure stack and fuses it into the final output. Our method eliminates the need for separate models across exposure regimes and produces HDR reconstructions with high input fidelity. On quantitative benchmarks, we outperform state-of-the-art generative baselines with comparable model capacity on several reconstruction metrics. Human evaluators further prefer our results in 72% of pairwise comparisons against existing methods. Finally, we show that this input-conditioned sequence generation and fusion framework extends beyond HDR to other image reconstruction tasks, such as all-in-focus image recovery from a single defocus-blurred input.

---


### 182. [GeomHerd: A Forward-looking Herding Quantification via Ricci Flow Geometry on Agent Interactive Simulations](https://arxiv.org/abs/2605.11645)

**<font color=#1a73e8>作者：</font>** Lake Yang, Junwei Su, Jingfeng Zeng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Herding -- where agents align their behaviors and act collectively -- is a central driver of market fragility and systemic risk. Existing approaches to quantify herding rely on price-correlation statistics, which inherently lag because they only detect coordination after it has already moved realised returns. We propose GeomHerd, a forward-looking geometric framework that bypasses this observability lag by quantifying coordination directly on upstream agent-interaction graphs. To generate these graphs, we treat a heterogeneous LLM-driven multi-agent simulator -- each financial trader instantiated by a persona-conditioned LLM call -- as a forecastable world, and evaluate the geometric pipeline on the Cividino--Sornette continuous-spin agent-based substrate as our headline financial testbed. By tracking the discrete Ollivier--Ricci curvature of these action graphs, GeomHerd captures the structural topology of emerging coordination. Theoretically, we establish a mean-field bridge mapping our graph-theoretic metric to CSAD, the classical macroscopic herding statistic, linking GeomHerd to downstream price-dispersion measurement. Empirically, GeomHerd anticipates herding long before aggregate market baselines: on the continuous-spin substrate, our primary detector fires a median of 272 steps before order-parameter onset; a contagion detector ($\beta_{-}$) recalls 65% of critical trajectories 318 steps early; and on co-firing trajectories the agent-graph signal precedes price-correlation-graph baselines by 40 steps. As a complementary indicator, the effective vocabulary of agent actions contracts during cascades. The geometric signature transfers out-of-domain to the Vicsek self-driven-particle model, and a curvature-conditioned forecasting head reduces cascade-window log-return MAE over detector-conditioned and price-only baselines.

---


### 183. [Weather-Robust Cross-View Geo-Localization via Prototype-Based Semantic Part Discovery](https://arxiv.org/abs/2605.11654)

**<font color=#1a73e8>作者：</font>** Chi-Nguyen Tran, Dao Sy Duy Minh, Huynh Trung Kiet 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-view geo-localization (CVGL), which matches an oblique drone view to a geo-referenced satellite tile, has emerged as a key alternative for autonomous drone navigation when GNSS signals are jammed, spoofed, or unavailable. Despite strong recent progress, three limitations persist: (1) global-descriptor designs compress the patch grid into a single vector without separating layout from texture across the view gap; (2) altitude-related scale variation is retained in the learned embedding rather than marginalized; and (3) multi-objective training relies on hand-tuned scalars over losses on incompatible gradient scales. We propose SkyPart, a lightweight swappable head for patch-based vision transformers (ViTs) that institutes explicit part grouping over the patch grid. SkyPart has four theory-grounded components: (i) learnable prototypes competing for patch tokens via single-pass cosine assignment; (ii) altitude-conditioned linear modulation applied only during training, making the retrieval embedding altitude-free at inference; (iii) a graph-attention readout over active prototypes; and (iv) a Kendall uncertainty-weighted multi-objective loss whose stationary points are Pareto-stationary. At 26.95M parameters and 22.14 GFLOPs, SkyPart is the smallest among top-performing methods and sets a new state of the art on SUES-200, University-1652, and DenseUAV under a single-pass, no-re-ranking, no-TTA protocol. Its advantage over the strongest baseline widens under the ten-condition WeatherPrompt corruption benchmark.

---


### 184. [A Cross-Cultural Analysis of Animated Representations of Emotions for Wearable Interfaces](https://arxiv.org/abs/2605.11668)

**<font color=#1a73e8>作者：</font>** Michal R. Wrobel, Duygun Erol Barkana, Agnieszka Landowska  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Although pervasive sensing technologies are increasingly capable of continuously detecting human emotional states, there is still a critical challenge: how to unobtrusively communicate this sensed data back to the user. Realistic avatars are effective but often unsuitable for the limited screen space and peripheral nature of wearable. Abstract geometric animation offers a promising, rapidly interpretable alternative, but its cross-cultural validity remains under-explored. This study investigates the universality of animated emotion representations. We conducted a comparative study with 105 participants from Poland and Turkey and analyzed how they map emotions to visual parameters, such as color, shape, size, speed, and animation type. The results indicate that color and object size are universally understood as carriers of emotional meaning, making them suitable for global visualization models. However, some cultural variation in dynamic range preferences was revealed by animation speed. These results lay the groundwork for developing generative visualization algorithms that translate continuous sensor data into intuitive, culturally relevant feedback for pervasive environments.

---


### 185. [Cochise: A Reference Harness for Autonomous Penetration Testing](https://arxiv.org/abs/2605.11671)

**<font color=#1a73e8>作者：</font>** Andreas Happe, Jürgen Cito  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recent work on LLM-driven autonomous penetration testing reports promising results, but existing systems often combine many architectural, prompting, and tool-integration choices, making it difficult to tell what is gained over a simple agent scaffold. We present cochise, a 597 LOC Python reference harness for autonomous penetration-testing experiments. Cochise connects an LLM-driven agent to a Linux execution host over SSH and supports controlled target environments reachable from that jump host.
The prototype implements a separated Planner--Executor architecture in which long-term state is maintained outside the LLM context, while a ReAct-style executor issues commands over SSH and self-corrects based on command outputs. The scenario prompt can be adapted to different target environments. To demonstrate the efficacy of our minimal harness, we evaluate it against a live third-party testbed called Game of Active Directory (GOAD).
Alongside the harness, we release replay and analysis tools: (i) cochise-replay for offline visualization of captured runs, (ii) cochise-analyze-alogs and cochise-analyze-graphs for cost, token, duration, and compromise analysis, and (iii) a corpus of JSON trajectory logs from GOAD runs, allowing researchers to study agent behavior without provisioning the 48--64 GB RAM / 190 GB storage testbed themselves. Cochise is intended not as a state-of-the-art pen-testing agent, but as reusable experimental infrastructure for comparing models, agent architectures, and penetration-testing traces.

---


### 186. [OOM-Free Alpamayo via CPU-GPU Memory Swapping for Vision-Language-Action Models](https://arxiv.org/abs/2605.11678)

**<font color=#1a73e8>作者：</font>** Seungwoo Roh, Huiyeong Kim, Jong-Chan Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> End-to-end Vision-Language-Action (VLA) models for autonomous driving unify perception, reasoning, and control in a single neural network, achieving strong driving performance but requiring 20-60GB of GPU memory-far exceeding the 12-16GB available on commodity GPUs. We present a framework, which enables memory-efficient VLA inference on VRAM-constrained GPUs through system-level optimization alone, without model modification. Our work proceeds in three stages: (1) Sequential Demand Layering reduces VRAM usage from model-level to layer-level granularity; (2) Pipelined Demand Layering hides parameter transfer time within layer execution time via transfer--compute overlap; and (3) a GPU-Resident Layer Decision Policy, informed by per-module residency benefit analysis, eliminates the residual transfer overhead that pipelining cannot hide. We further propose a performance prediction model that determines the optimal configuration-both the number and placement of resident layers-from a single profiling run with less than 1.3% prediction error across all configurations. Applied to NVIDIA's Alpamayo-R1-10B (21.52GB) on an RTX 5070Ti (16GB), our work achieves up to 3.55x speedup over Accelerate offloading while maintaining full BF16 precision.

---


### 187. [ShapeCodeBench: A Renewable Benchmark for Perception-to-Program Reconstruction of Synthetic Shape Scenes](https://arxiv.org/abs/2605.11680)

**<font color=#1a73e8>作者：</font>** Shivam Kumar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce ShapeCodeBench, a synthetic benchmark for perception-to-program reconstruction: given a rendered raster image, a model must emit an executable drawing program that a deterministic evaluator re-renders and compares with the target. The v1 DSL has four primitives on a 512 x 512 black-on-white canvas, but every instance is generated from a seeded RNG, so fresh held-out sets can be created to reduce exact-instance contamination. We release a frozen eval_v1 split with 150 samples across easy, medium, and hard tiers, scored by exact match, pixel accuracy, foreground IoU, parse success, and execution success. We evaluate an empty-program floor, a classical computer-vision heuristic, Claude Opus 4.7 at high and max effort, and GPT-5.5 at medium and extra_high reasoning effort. The heuristic is competitive on easy scenes but collapses when overlaps fuse components; the strongest multimodal configuration preserves much of the foreground structure but still misses exact match because of small parameter errors. Best overall exact match remains low, so ShapeCodeBench is far from saturated. The benchmark code, frozen dataset, run artifacts, and paper sources are released to support independent replication and extension.

---


### 188. [HySecTwin: A Knowledge-Driven Digital Twin Framework Augmented with Hybrid Reasoning for Cyber-Physical Systems](https://arxiv.org/abs/2605.11682)

**<font color=#1a73e8>作者：</font>** David Holmes, Ahmad Moshin, Surya Nepal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Existing Digital Twin (DT) approaches often lack semantic reasoning capabilities for effective cybersecurity modelling in Cyber-Physical Systems (CPS). This paper presents HySecTwin, a knowledge-driven digital twin architecture that places automated reasoning at the core of real-time threat detection. HySecTwin incorporates semantic modelling to transform heterogeneous CPS telemetry, device attributes, and operational relationships into machine-interpretable representations, combined with an embedded reasoning engine operating over contextualized system states. Unlike opaque detection methods, the framework integrates deterministic rule-based inference with hybrid fuzzy reasoning to generate explicit, interpretable, and auditable security assessments from live device telemetry. This enables context-aware monitoring of complex CPS environments while preserving transparency and trust. Experimental evaluation using a representative CPS testbed and MITRE ATT\&CK campaign-inspired attack scenarios demonstrates sub-millisecond twin synchronization latency and up to 21.5\% faster threat detection compared with deterministic reasoning alone. The results show that semantic modelling, semantic enrichment, and hybrid reasoning improve explainability and resilience without extra system overhead. HySecTwin provides a lightweight, containerized, and extensible framework for secure-by-design digital twin deployments in mission-critical infrastructures

---


### 189. [DORA: Dynamic Online Reinforcement Agent for Token Merging in Vision Transformers](https://arxiv.org/abs/2605.11683)

**<font color=#1a73e8>作者：</font>** Kaixuan He, Song Chen, Yi Kang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers (ViTs) incur significant computational overhead due to the quadratic complexity of self-attention relative to the token sequence length. While existing token reduction methods mitigate this issue, they predominantly rely on fixed heuristic metrics, predefined ratios, or static offline masks, which lack the adaptability to capture input-dependent redundancy during inference. In this paper, we propose DORA (Dynamic Online Reinforcement Agent), the first reinforcement learning (RL)-driven online inference framework for dynamic token merging in ViTs. We formulate the merging process as a sequential Markov Decision Process (MDP), where a lightweight RL agent determines the merging strategy for each Transformer block based on the current feature state and layer-specific context. To balance computational efficiency and feature fidelity, the agent is optimized via a dense reward function incorporating a non-linear distillation-based penalty. We implement an asymmetric Actor-Critic architecture that utilizes a high-capacity Critic for stable offline training while retaining a minimal Actor head for low-computation online inference. Evaluations across multiple ViT scales (Tiny to Large) demonstrate that DORA improves the accuracy-efficiency Pareto front compared to current baselines. Under strict negligible accuracy-drop constraints (<= 0.05%), DORA achieves up to a 12.66% token merging rate, and delivers up to a 569.7% relative improvement over the most efficient baseline. On ImageNet-1K, under aligned accuracy constraints, DORA achieves up to a 76% relative improvement in computational savings compared to state-of-the-art methods. Furthermore, on out-of-distribution (OOD) benchmarks such as ImageNet-A and ImageNet-C, DORA attains a relative efficiency advantage of over 430%.

---


### 190. [Partial Model Sharing Improves Byzantine Resilience in Federated Conformal Prediction](https://arxiv.org/abs/2605.11684)

**<font color=#1a73e8>作者：</font>** Ehsan Lari, Reza Arablouei, Stefan Werner  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a Byzantine-resilient federated conformal prediction (FCP) method that leverages partial model sharing, where only a subset of model parameters is exchanged each round. Unlike existing robust FCP approaches that primarily harden the calibration stage, our method protects both the federated training and conformal calibration phases. During training, partial sharing inherently restricts the attack surface and attenuates poisoned updates while reducing communication. During calibration, clients compress their non-conformity scores into histogram-based characterization vectors, enabling the server to detect Byzantine clients via distance-based maliciousness scores and to estimate the conformal quantile using only benign contributors. Experiments across diverse Byzantine attack scenarios show that the proposed method achieves closer-to-nominal coverage with substantially tighter prediction intervals than standard FCP, establishing a robust and communication-efficient approach to federated uncertainty quantification.

---


### 191. [Persistent and Conversational Multi-Method Explainability for Trustworthy Financial AI](https://arxiv.org/abs/2605.11687)

**<font color=#1a73e8>作者：</font>** Georgios Makridis, Georgios Fatouros, John Soldatos 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Financial institutions increasingly require AI explanations that are persistent, cross-validated across methods, and conversationally accessible to human decision-makers. We present an architecture for human-centered explainable AI in financial sentiment analysis that combines three contributions. First, we treat XAI artifacts -- LIME feature attributions, occlusion-based word importance scores, and saliency heatmaps -- as persistent, searchable objects in distributed S3-compatible storage with structured metadata and natural-language summaries, enabling semantic retrieval over explanation history and automatic index reconstruction after system failures. Second, we enable multi-method explanation triangulation, where a retrieval-augmented generation (RAG) assistant compares and synthesizes results from multiple XAI methods applied to the same prediction, allowing users to assess explanation robustness through natural-language dialogue. Third, we evaluate the faithfulness of generated explanations using automated checks over grounding completeness, hallucinated claims, and method-attribution behavior. We demonstrate the architecture on an EXTRA-BRAIN financial sentiment analysis pipeline using FinBERT predictions and present evaluation results showing that constrained prompting reduces hallucination rate by 36\% and increases method-attribution citations by 73\% compared to naive prompting. We discuss implications for trustworthy, human-centered AI services in regulated financial environments.

---


### 192. [Shaping Zero-Shot Coordination via State Blocking](https://arxiv.org/abs/2605.11688)

**<font color=#1a73e8>作者：</font>** Mingu Kang, Sunwoo Lee, Yonghyeon Jo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Zero-shot coordination (ZSC) aims to enable agents to cooperate with independently trained partners without prior interaction, a key requirement for real-world multi-agent systems and human-AI collaboration. Existing approaches have largely emphasized increasing partner diversity during training, yet such strategies often fall short of achieving reliable generalization to unseen partners. We introduce State-Blocked Coordination (SBC), a simple yet effective framework that improves ZSC by inducing diverse interaction scenarios without direct environment modification. Specifically, SBC generates a family of virtual environments through state blocking, allowing agents to experience a wide range of suboptimal partner policies. Across multiple benchmarks, SBC demonstrates superior performance in zero-shot coordination, including strong generalization to human partners.

---


### 193. [Slicing and Dicing: Configuring Optimal Mixtures of Experts](https://arxiv.org/abs/2605.11689)

**<font color=#1a73e8>作者：</font>** Margaret Li, Sneha Kudugunta, Danielle Rothermel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) architectures have become standard in large language models, yet many of their core design choices - expert count, granularity, shared experts, load balancing, token dropping - have only been studied one or two at a time over narrow configuration ranges. It remains an open question whether these choices can be optimized independently, without considering interactions. We present the first systematic study of over 2,000 pretraining runs spanning models up to 6.6B total parameters, in which we exhaustively vary total experts, expert dimension, heterogeneous expert sizing within a single layer, shared expert size and load-balancing mechanisms. We find that at every active-parameter scale that we study, performance consistently improves with total MoE parameters even at extreme active expert parameter ratios like this http URL, the optimal expert size is nearly invariant to total parameter count and depends only on active parameter count. Third, we see that other choices like shared experts, heterogeneous experts and load-balancing settings have small effects relative to expert count and granularity, although dropless routing yields a consistent gain. Overall, our results suggest a simpler recipe: focus on expert count and granularity, other choices have minimal effect on final quality.

---


### 194. [Compositional Neural Operators for Multi-Dimensional Fluid Dynamics](https://arxiv.org/abs/2605.11691)

**<font color=#1a73e8>作者：</font>** Hamda Hmida, Hsiu-Wen Chang, Youssef Mesri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Partial differential equations (PDEs) govern diverse physical phenomena, yet high-fidelity numerical solutions are computationally expensive and Machine Learning approaches lack generalization. While Scientific Foundation Models (SFMs) aim to provide universal surrogates, typical encoding-decoding approaches suffer from high pretraining costs and limited interpretability. In this paper, we propose Compositional Neural Operators (CompNO) for 2D systems, a framework that decomposes complex PDEs into a library of Foundation Blocks. Each block is a specialized Neural Operator pretrained on elementary physics. This modular library contains convection, diffusion, and nonlinear convection blocks as well as a Poisson Solver, enabling the framework to address the pressure-velocity coupling. These experts are assembled via an Adaptation Block featuring an Aggregator. This aggregator learns nonlinear interactions by minimizing data loss and physics-based residuals driven from governing equations. The proposed approach has been evaluated on the Convection-Diffusion equation, the Burgers' equation, and the Incompressible Navier-Stokes equation. Our results demonstrate that learning from elementary operators significantly improves adaptability, enhances model interpretability and facilitates the reuse of pretrained blocks when adapting to new physical systems.

---


### 195. [Augmented Lagrangian Method for Last-Iterate Convergence for Constrained MDPs](https://arxiv.org/abs/2605.11694)

**<font color=#1a73e8>作者：</font>** Michael Lu, Max Qiushi Lin, Mo Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study policy optimization for infinite-horizon, discounted constrained Markov decision processes (CMDPs). While existing theoretical guarantees typically hold for the mixture policy, deploying such a policy is computationally and memory intensive. This leads to a practical mismatch where a single (last-iterate) policy must be deployed. Recent theoretical works have thus focused on proving last-iterate convergence, but are largely limited to the tabular setting or to algorithmic variants that are rarely used in practice. To address this, we use the classic inexact augmented Lagrangian ($\texttt{AL}$) method from constrained optimization, and propose a general framework with provable last-iterate convergence for CMDPs. We first focus on the tabular setting and propose to solve the $\texttt{AL}$ sub-problem with projected Q-ascent ($\texttt{PQA}$). Combining the theoretical guarantees of $\texttt{PQA}$ and the standard $\texttt{AL}$ analysis enables us to establish global last-iterate convergence. We generalize these results to handle log-linear policies, and demonstrate that an efficient, projected variant of $\texttt{PQA}$ can achieve last-iterate convergence with comparable guarantees as prior work. Finally, we demonstrate that our framework scales to complex non-linear policies, and evaluate it on continuous control tasks.

---


### 196. [Emergent Communication between Heterogeneous Visual Agents through Decentralized Learning](https://arxiv.org/abs/2605.11695)

**<font color=#1a73e8>作者：</font>** Mikako Ochiai, Masatoshi Nagano, Tadahiro Taniguchi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Symbols are shared, but perception is private. We study emergent communication between heterogeneous visual agents through decentralized learning, asking what visual information can become shareable when agents have different visual representations. Instead of optimizing messages through a shared external communicative objective, our agents exchange only discrete token sequences and update their own models using local perceptual evidence. This setting focuses on an underexplored aspect of emergent communication, examining whether common symbols can arise without shared perceptual access, and how the similarity between private visual spaces constrains the content and symmetry of the resulting language. We instantiate this setting in the Metropolis-Hastings Captioning Game (MHCG), where two agents collaboratively form shared captions by exchanging proposed token sequences that a listener accepts or rejects using an MH-style criterion evaluated against its own visual features. We compare three pairings of frozen visual encoders, with agents starting from randomly initialized text modules. Experiments on MS-COCO show that MHCG produces visually informative shared token sequences that outperform a no-communication baseline in cross-agent alignment, visual-feature prediction, and image-text retrieval; all cross-agent metrics decline as encoder mismatch increases. Moderate encoder heterogeneity reduces the number of shared sequences while preserving per-sequence visual specificity, whereas stronger encoder heterogeneity yields fewer, coarser, and more asymmetric sequences. Ablations show that listener-side MH acceptance is critical for avoiding degenerate token formation. These results suggest that shared symbols can arise from local perceptual evaluation alone, with visual representational similarity across encoders shaping both the content and symmetry of the resulting language.

---


### 197. [WildRelight: A Real-World Benchmark and Physics-Guided Adaptation for Single-Image Relighting](https://arxiv.org/abs/2605.11696)

**<font color=#1a73e8>作者：</font>** Lezhong Wang, Mehmet Onurcan Kaya, Siavash Bigdeli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent single-image relighting methods, powered by advanced generative models, have achieved impressive photorealism on synthetic benchmarks. However, their effectiveness in the complex visual landscape of the real world remains largely unverified. A critical gap exists, as current datasets are typically designed for multi-view reconstruction and fail to address the unique challenges of single-image relighting. To bridge this synthetic-to-real gap, we introduce WildRelight, the first in-the-wild dataset specifically created for evaluating single-image relighting models. WildRelight features a diverse collection of high-resolution outdoor scenes, captured under strictly aligned, temporally varying natural illuminations, each paired with a high-dynamic-range environment map. Using this data, we establish a rigorous benchmark revealing that state-of-the-art models trained on synthetic data suffer from severe domain shifts. The strictly aligned temporal structure of WildRelight enables a new paradigm for domain adaptation. We demonstrate this by introducing a physics-guided inference framework that leverages the captured natural light evolution as a self-supervised constraint. By integrating Diffusion Posterior Sampling (DPS) with temporal Sampling-Aware Test-Time Adaptation (TTA), we show that the dataset allows synthetic models to align with real-world statistics on-the-fly, transforming the intractable sim-to-real challenge into a tractable self-supervised task. The dataset and code will be made publicly available to foster robust, physically-grounded relighting research.

---


### 198. [ScaleMoGen: Autoregressive Next-Scale Prediction for Human Motion Generation](https://arxiv.org/abs/2605.11704)

**<font color=#1a73e8>作者：</font>** Inwoo Hwang, Hojun Jang, Bing Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present ScaleMoGen, a scale-wise autoregressive framework for text-driven human motion generation. Unlike conventional autoregressive approaches that rely on standard next-token prediction, ScaleMoGen frames motion generation as a coarse-to-fine process. We quantize 3D motions into compositional discrete tokens across multiple skeletal-emporal scales of increasing granularity, learning to generate motion by autoregressively predicting next-scale token maps. To maintain structural integrity, our motion tokenizers and quantizers are explicitly designed so that discrete tokens at every scale strictly preserve the skeletal hierarchy. Additionally, we employ bitwise quantization and prediction, which efficiently scale up the tokenizer vocabulary to preserve motion details and stabilize optimization. Extensive experiments demonstrate that ScaleMoGen achieves state-of-the-art performance, establishing an FID of 0.030 (vs. 0.045 for MoMask) on HumanML3D and a CLIP Score of 0.693 (vs. 0.685 for MoMask++) on the SnapMoGen dataset. Furthermore, we demonstrate that our skeletal-temporal multi-scale representation naturally facilitates training-free, text-guided motion editing.

---


### 199. [Unlocking Compositional Generalization in Continual Few-Shot Learning](https://arxiv.org/abs/2605.11710)

**<font color=#1a73e8>作者：</font>** Phu-Quy Nguyen-Lam, Phu-Hoa Pham, Dao Sy Duy Minh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Object-centric representations promise a key property for few-shot learning: Rather than treating a scene as a single unit, a model can decompose it into individual object-level parts that can be matched and compared across different concepts. In practice, this potential is rarely realized. Continual learners either collapse scenes into global embeddings, or train with part-level matching objectives that tie representations too closely to seen patterns, leaving them unable to generalize to truly novel concepts. In this paper, we identify this fundamental structural conflict and pioneer a new paradigm that strictly decouples representation learning from compositional inference. Leveraging the inherent patch-level semantic geometry of self-supervised Vision Transformers (ViTs), our framework employs a dual-phase strategy. During training, slot representations are optimized entirely toward holistic class identity, preserving highly generalizable, object-level geometries. At inference, preserved slots are dynamically composed to match novel scenes. We demonstrate that this paradigm offers dual structural benefits: The frozen backbone naturally prevents representation drift, while our lightweight, holistic optimization preserves the features' capacity for novel-concept transfer. Extensive experiments validate this approach, achieving state-of-the-art unseen-concept generalization and minimal forgetting across standard continual learning benchmarks.

---


### 200. [Debiased Model-based Representations for Sample-efficient Continuous Control](https://arxiv.org/abs/2605.11711)

**<font color=#1a73e8>作者：</font>** Jiafei Lyu, Zichuan Lin, Scott Fujimoto 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model-based representations recently stand out as a promising framework that embeds latent dynamics information into the representations for downstream off-policy actor-critic learning. It implicitly combines the advantages of both model-free and model-based approaches while avoiding the training costs associated with model-based methods. Nevertheless, existing model-based representation methods can fail to capture sufficient information about relevant variables and can overfit to early experiences in the replay buffer. These incur biases in representation and actor-critic learning, leading to inferior performance. To address this, we propose Debiased model-based Representations for Q-learning, tagged DR.Q algorithm. DR.Q explicitly maximizes the mutual information between the representations of the current state-action pair and the next state besides minimizing their deviations, and samples transitions with faded prioritized experience replay. We evaluate DR.Q on numerous continuous control benchmarks with a single set of hyperparameters, and the results demonstrate that DR.Q can match or surpass recent strong baselines, sometimes outperforming them by a large margin. Our code is available at this https URL.

---


> [!TIP]
> 当前位于：**151-200**（第 4/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-396](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
