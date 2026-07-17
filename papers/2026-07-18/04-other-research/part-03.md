# 📦 其他研究 | 2026年07月18日

> 本类共 **221** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-221](./part-05.md)

---

### 101. [MagicPrompt: Ultra-Lightweight Prompt Tuning for Video Generation](https://arxiv.org/abs/2607.14595)

**<font color=#1a73e8>作者：</font>** Yinhan Zhang, Dinwei Tan, Xianghao Kong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale video diffusion models (VDMs) deliver strong generation performance, but full fine-tuning for downstream tasks incurs prohibitive computational costs. Existing parameter-efficient fine-tuning (PEFT) methods have two critical flaws on billion-scale models: they still require substantial trainable parameters, and reward-based training suffers from noise-induced optimization instability in condition-guided tasks. We propose MagicPrompt, a lightweight framework that achieves extreme parameter efficiency and stable reward optimization. It first adopts Attention-Embedded Prompt Tuning, which steers generation via lightweight soft prompts with orders of magnitude fewer parameters while preserving pre-trained knowledge. It further introduces Dual-Space Reward Feedback Optimization, which uses self-supervised latent objectives to improve condition-guided reward training. Experiments show MagicPrompt reaches competitive performance with less than 1\% trainable parameters and notably reduces training costs.

---


### 102. [Hough-SIFT: Robust Image Registration for Linear Structures via Hough Space](https://arxiv.org/abs/2607.14598)

**<font color=#1a73e8>作者：</font>** Masaki Satoh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image registration is essential in applications such as electronic image stabilization. Scale-Invariant Feature Transform (SIFT), a widely used local keypoint detector and descriptor, typically provides accurate registration; however, it often fails in scenes with strong linear structures (e.g., shutters), where local features become ambiguous. We propose Hough-SIFT, a robust registration method that performs SIFT descriptor matching in Hough space. In this domain, linear structures form distinctive peaks that restore descriptor discriminability. Experiments demonstrate that Hough-SIFT is robust in linear scenes where SIFT frequently fails, while maintaining accuracy comparable to SIFT in normal scenes.

---


### 103. [Accelerating A/B-Tests with Counterfactual Estimation: Reducing Variance through Policy Overlap](https://arxiv.org/abs/2607.14604)

**<font color=#1a73e8>作者：</font>** Olivier Jeunen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online controlled experiments are the gold standard for hypothesis testing in online platforms. Notwithstanding their ubiquity, they are notoriously expensive to run, and issues of variance hamper statistical power in assessing treatment effects. While standard variance reduction techniques leverage model-based control variates to reduce outcome noise, they remain agnostic to potential structural relationships between competing policies.
In this work, we identify a critical inefficiency in the standard A/B-testing protocol: when a treatment and control policy agree on an action, the resulting outcome contributes noise but no signal regarding the treatment effect -- unnecessarily inflating confidence intervals. We propose a novel experimental protocol that exploits this policy overlap to accelerate experimentation. The key insight is to frame the randomised treatment assignment mechanism as a meta-policy, and leverage $\Delta$-Off-Policy Estimation methods to obtain unbiased estimates for average treatment effects. We prove analytically that our approach recovers standard A/B-testing practices in the general case, but that its variance scales with the divergence between policies rather than raw outcome variance. Hence, we dominate the standard Difference-in-Means estimator whenever policies have common support, and the improvement is strict whenever the overlap region contributes non-zero residual variance. Empirical results corroborate these theoretical insights -- holding promise for significant impact on the real-world evaluation of recommender systems, information retrieval pipelines, and large language model interfaces.

---


### 104. [Auditing Fairness-Privacy Trade-offs: Subpopulation-Level Effects of Fairness-Enhancing Algorithms](https://arxiv.org/abs/2607.14607)

**<font color=#1a73e8>作者：</font>** Umid Suleymanov, Ilhama Novruzova, Khalid Mammadov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning (ML) models deployed in sensitive domains such as healthcare, law enforcement, and finance must satisfy not only utility requirements but also fairness and privacy guarantees. While prior work has largely examined how privacy-preserving techniques affect fairness, the inverse question-how fairness-enhancing algorithms influence privacy leakage-remains underexplored. We present the first comprehensive study of how fairness interventions affect membership inference privacy risks at the subpopulation level. By adapting the Likelihood Ratio Attack (LiRA) for subgroup auditing, we uncover privacy disparities that aggregate evaluations obscure. We further analyze how Differential Privacy (DP) interacts with fairness-enhancing methods across different categories, showing that DP's privacy benefits and utility costs are unevenly distributed across subpopulations. Our results demonstrate that fairness interventions do not uniformly increase privacy risk; their impact depends on model architecture, subgroup size, and mitigation strategy. These findings reveal that fairness, privacy, and utility must be jointly evaluated at the subpopulation level, and we introduce the first unified empirical framework to support such auditing in practice.

---


### 105. [Angular Gaussian Supervised Contrastive Learning for Long-Tailed Electrocardiogram Arrhythmia Diagnosis](https://arxiv.org/abs/2607.14613)

**<font color=#1a73e8>作者：</font>** Jin Dai, Qiuzhen Zhang, Chenyun Dai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-tailed label distributions reduce the reliability of deep learning for electrocardiogram (ECG) arrhythmia diagnosis, particularly for clinically important but rare abnormalities. Existing rebalancing and logit adjustment methods mainly address class frequency while overlooking direction-dependent morphological variability across ECG classes. This study proposes Angular Gaussian Supervised Contrastive Learning (AG-SCL) for long-tailed multi-label ECG diagnosis. AG-SCL integrates three components into a unified framework: an Angular Gaussian contrastive branch that models full-covariance class uncertainty on unit-normalized embeddings, Adaptive Logit Adjustment that learns bounded label-state-specific prior corrections instead of fixed frequency-based margins, and tail-aware augmentation that generates morphology-preserving views while protecting the 7-25 Hz QRS-dominant band. The method was evaluated on the public PTB-XL benchmark and a nocturnal ECG dataset comprising 1317 hours of recordings from 141 subjects. AG-SCL achieved the best macro-level performance on both datasets. On PTB-XL, it obtained a balanced accuracy of 0.838, sensitivity of 0.709, specificity of 0.968, mean average precision of 0.495, and TPR at 5% FPR of 0.778. On Noc-ECG, the corresponding values were 0.918, 0.889, 0.947, 0.488, and 0.900. The largest gains occurred in rare or morphologically unstable rhythm classes, while ablation studies confirmed the contributions of full-covariance modelling, Adaptive Logit Adjustment, and tail-aware augmentation. AG-SCL improves long-tailed ECG diagnosis by combining prior calibration with anisotropic representation learning, enhancing sensitivity to rare arrhythmias while maintaining clinically relevant specificity. Our code is available at: this https URL.

---


### 106. [Beyond Entropy: Correctness-Aware Advantage Shaping via Contrastive Policy Optimization](https://arxiv.org/abs/2607.14614)

**<font color=#1a73e8>作者：</font>** Weiwen Xu, Jia Liu, Hou Pong Chan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) commonly uses entropy for advantage shaping. However, entropy cannot distinguish useful uncertainty from detrimental confusion, limiting its effectiveness as a correctness signal. We propose Contrastive Policy Optimization (CPO), which uses token-level contrastive disagreement between reference-guided and vanilla generation distributions for correctness-aware advantage shaping. Both theoretical and empirical results show that this disagreement reliably indicates token-level correctness. We further show that On-policy Distillation is a special case of CPO, where the posterior distribution is instantiated by an external teacher model. CPO also resolves the zero-advantage problem. Experiments on in-domain and out-of-domain benchmarks demonstrate that CPO substantially outperforms entropy-based RLVR methods while maintaining strong generalization. Further analysis shows that correct and incorrect responses naturally support exploration and exploitation respectively, and balancing both leads to the best performance.

---


### 107. [SportD: Can VLMs Physically Strategize?](https://arxiv.org/abs/2607.14616)

**<font color=#1a73e8>作者：</font>** Jasin Cekinmez, Addison J. Wu, Haotian Xia 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision--language models have become increasingly capable of interpreting visual scenes, but it remains unclear whether they can use information to make strategically effective decisions. We investigate this question in soccer, where models observe the seconds preceding an on-ball decision and must choose whether to shoot or pass to a specific teammate. Unlike conventional visual-understanding tasks, soccer enables decisions to be evaluated quantitatively by estimating the value of every available action. We introduce SportD, a benchmark comprising 478 on-ball decisions from the 2022 FIFA World Cup. Each model choice is evaluated against a possession-value model that estimates the action that most increases the attacking team's probability of scoring, allowing us to measure both optimal-action accuracy and the value forfeited by suboptimal decisions. Across three frontier VLMs, the best selects the highest-valued action on 31.4% of events, compared with 38.9% for the professional players, and all models incur significantly greater regret. Further analysis reveals a systematic preference for lower-variance and lower-reward actions: VLMs shoot less often and select substantially less progressive passes than either the optimal policy or the real players. The models also reproduce the player's specific action above chance even when that action is suboptimal, suggesting partial imitation of familiar play patterns rather than consistent evaluation of counterfactual alternatives. SportD provides a value-grounded testbed for measuring physical strategic reasoning in VLMs.

---


### 108. [Action QFormer: Structured Representation Shaping under Action Supervision in Vision-Language-Action Models](https://arxiv.org/abs/2607.14635)

**<font color=#1a73e8>作者：</font>** Yufeng Ji, Wenhao Tang, Haoyi Niu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Action supervision in vision-language-action (VLA) models is often treated as a downstream objective for learning action prediction. In this paper, we study it instead as a force that shapes inherited multimodal representations. We show that this shaping has a dual effect: it is necessary for forming action-compatible representations, but when action supervision is applied too directly to the inherited multimodal pathway, it can also destabilize representations that support language-side processing and object grounding. To address this tension, we introduce Action QFormer, a query-based action-facing interface that uses instruction-conditioned queries to reorganize inherited multimodal information into action-facing representations before downstream action generation. In zero-shot sim-to-real navigation, Action QFormer improves average closed-loop task success from 18.8% to 56.3%, raises fixed-instruction action-generation correctness from 22.5% to 75.5%, and nearly eliminates out-of-distribution instruction generations. Further analyses show that Action QFormer changes how action supervision shapes inherited multimodal representations, reducing broad upstream rewriting while preserving targeted and sometimes constructive action-supervised adaptation. These results suggest that improving VLA performance requires not only stronger pretrained backbones, but also better ways of selecting and organizing inherited multimodal information while controlling how it is shaped under action supervision.

---


### 109. [TIDE: Trustworthy and Interpretable Battery Degradation Estimation with Contextual Learning and Symbolic Distillation](https://arxiv.org/abs/2607.14640)

**<font color=#1a73e8>作者：</font>** Wen Yang Tan, Jiawei Li, Fang Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Battery health estimation is fundamental for battery management in battery-powered systems, where inaccurate health states may affect control, maintenance, and service life. It becomes even more critical in intelligent connected systems, where estimation errors can propagate across interconnected devices and downstream decisions. In this paper, we propose TIDE, a trustworthy and interpretable battery degradation estimator for reliable battery health estimation. TIDE jointly considers accuracy, trustworthiness, and interpretability, which are all essential for practical deployment and downstream decision making. To realize these objectives, TIDE combines battery-domain knowledge with operational measurements in a three-component backbone. A knowledge-guided degradation prior promotes trustworthy estimation, a monotone residual component provides interpretable aging-consistent refinement, and a contextual learning component captures battery-specific operational effects for improved accuracy. The trained backbone is then distilled into a compact symbolic surrogate that provides a concise model-level interpretation of its learned estimation logic. Experiments show that TIDE achieves strong estimation accuracy, improving overall estimation fidelity by an average of 19.7% over representative baselines. Its knowledge-guided prior and monotone residual modelling substantially reduce aging-consistency violations, supporting trustworthy estimation. Meanwhile, the backbone enables component-level interpretation, while symbolic distillation provides a compact model-level representation of the learned estimation logic. These results support the practical use of TIDE for battery health monitoring and decision support in intelligent connected systems.

---


### 110. [Analytic Abduction: Causal Decomposition and Governed Commitment for Human--AI Coordination](https://arxiv.org/abs/2607.14641)

**<font color=#1a73e8>作者：</font>** Remo Pareschi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Abductive reasoning operates in two directions. The synthetic mode builds explanations from available hypotheses; the analytic mode, conversely, identifies the latent factors whose interaction accounts for a complex observed state. This paper develops the analytic mode as a non-greedy, risk-sensitive discipline of commitment, in which candidate factors coexist and interact, resolving into committed conclusions only when explicit governance conditions are met. The formal core is the $\kappa$-$\tau$ apparatus: $\kappa$ encodes the epistemic interaction among hypotheses, and $\tau$ sets a commitment threshold calibrated to the decision's stakes. The central contribution is the causal cluster, a structured object recording which latent factors participate in a decomposition, with what weights and interaction structure, together with a two-level architecture (intra-cluster $\kappa^*$, inter-cluster $\kappa^{**}$) that guards against causal misattribution. Demonstrated in epidemiological crisis decomposition and adversarial cyber threat analysis, the framework's contribution to human-AI reasoning is the legibility of suspended decomposition as a shared coordination object, providing structural resistance to premature convergence. In practice, the decision-maker is handed not a single imposed answer but the competing explanatory scenarios, weighted by plausibility and paired with the evidence that would resolve between them, so that sound action is possible even before the ambiguity is resolved.

---


### 111. [Autoregressive Modeling of Film with Applications in Video Montage](https://arxiv.org/abs/2607.14645)

**<font color=#1a73e8>作者：</font>** Marcelo Sandoval-Castañeda, Fabian Caba Heilbron, Shiry Ginosar 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This work introduces FilmGPT, an autoregressive transformer designed to address the challenge of video montage--turning a collection of raw, "unwatchable" footage into coherent cinematic sequences. Inspired by language learning in modern LLMs, we train a long-context autoregressive transformer on a large corpus of movies. The aim is to implicitly capture the "grammar" of film directly from data rather than from hand-coded rules. Unlike other generative models, FilmGPT does not generate any new video frames. Instead, at inference time, we introduce a footage-constrained decoding algorithm to select the best next shot from the input raw footage according to the statistical patterns learned from films. We first evaluate these learned statistics directly by using the FilmGPT autoregressive model for next shot prediction on a standard benchmark of shot sequence ordering, outperforming the previous state of the art. We then evaluate our footage-constrained decoding algorithm on the full film editing task via a user study, and find that our FilmGPT-based editing significantly outperforms previous approaches. Finally, we demonstrate the applicability of FilmGPT to a wide range of applications in video montage, from automatic video segment trimming to human-in-the-loop film editing.

---


### 112. [Trajectory-Aware Flow Matching for Topology Optimisation](https://arxiv.org/abs/2607.14652)

**<font color=#1a73e8>作者：</font>** Shusheng Xiao, Jinshuai Bai, Hyogu Jeong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Topology optimisation (TO) often requires repeated finite element analysis and sensitivity-based material updates, which can be costly when multiple candidate designs are needed under varying physical and design conditions. Generative TO offers a route to rapid design exploration, but existing models may rely on adversarial training, long reverse-diffusion sampling, or external guidance to maintain structural feasibility and physical consistency. This study develops a flow matching-based topology optimisation (FMTO) framework for conditional topology generation. Linear FMTO is first formulated as an endpoint-based baseline by interpolating between a Gaussian source field and the BESO reference topology. To introduce mechanically meaningful intermediate states, a trajectory-aware FMTO formulation is proposed, where volume-fraction-indexed BESO states are used to construct the probability path and target velocity field. This incorporates physics-guided optimisation history into generative flow learning without adding inference-time optimisation. A path--velocity mismatch analysis explains why moderate trajectory weighting can improve generation stability, whereas excessive guidance may over-constrain the learned transport. Numerical examples show that FMTO generates diverse topology candidates with improved compliance-related performance, volume-fraction satisfaction, topology fidelity, and substantially fewer sampling steps than a diffusion-based baseline. Under limited training data, trajectory-aware FMTO achieves the best overall performance with a moderate trajectory weight. Studies on trajectory-anchor density and three-dimensional topology generation further demonstrate the influence of path design and the applicability of the proposed framework beyond two-dimensional problems.

---


### 113. [Dendrite: A Real-Time Python Application for Online Brain-Computer Interface Research and Development](https://arxiv.org/abs/2607.14655)

**<font color=#1a73e8>作者：</font>** Niko Kroflic, Jan Babič  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Online brain-computer interface research requires software that can acquire multimodal physiological data, train and update decoders, run live inference, and preserve the full experimental provenance in a reproducible workflow. We present Dendrite, a real-time brain-computer interface application in Python that brings signal acquisition, decoder training, and live inference together in a single, ready-to-run application that stays modifiable. Dendrite records several signal streams at once, each at its native rate, and executes multiple processing modes concurrently against them. A decoder can start from a previously trained model or be fit mid-session while the pipeline keeps running, and the same recordings feed offline training in the same application. Each recording, decoder, and training run is tracked in a database, and every decoder records the configuration and the source recordings it was trained from, so a deployed decoder traces back to what produced it. The experimental paradigm stays external, an independent program in any language that reaches Dendrite over the network, rather than a module built inside the runtime. We validate the full system end-to-end on in-house and public BCI datasets, training and updating decoders online while the pipeline runs in real time. Dendrite is open-source under the GPL-3.0 license at this https URL. The result is a reproducible, open-source biomedical-computing system for developing and evaluating online BCI paradigms.

---


### 114. [Scalable Training of Continuous-Time Spiking Neural Networks with Differentiable Spike-Time Discretization](https://arxiv.org/abs/2607.14672)

**<font color=#1a73e8>作者：</font>** Yusuke Sakemi, Tomoya Takeuchi, Takeo Hosomi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous-time spiking neural networks (SNNs) provide an event-driven framework for temporal computation, computational neuroscience, and neuromorphic hardware. However, training deep continuous-time SNNs is severely constrained by the memory required for exact spike-time computation, which evaluates and retains candidate firing times over intervals determined by presynaptic spike ordering. Here we introduce a memory-efficient training framework based on differentiable spike-time discretization (DSTD) for leaky integrate-and-fire neurons with general membrane and synaptic time constants. DSTD maps irregular presynaptic spikes onto differentiable weighted events at fixed time points, replacing the input-dependent candidate dimension with $M$ fixed time intervals while accurately approximating continuous-time membrane-potential dynamics. This reduces candidate-related activation memory from $O(N_{\mathrm{out}}N_{\mathrm{in}})$ to $O(N_{\mathrm{out}}M)$ in the case of time-to-first-spike (TTFS) coding, where $N_{\mathrm{in}}$ and $N_{\mathrm{out}}$ denote the numbers of presynaptic and postsynaptic neurons, respectively. We further introduce synfire-chain-inspired temporal regularization that organizes layer-wise firing windows, mitigates dead-neuron failures, and enables pipeline-like processing. In dense LIF layers, DSTD reduced peak memory consumption by up to approximately 100-fold and training time by up to approximately 20-fold compared with exact spike-time computation. Together, these methods allowed us to train 9-layer convolutional SNNs on CIFAR-10 and 20-layer convolutional SNNs on Fashion-MNIST on a single GPU.

---


### 115. [Project Kaleidoscope: Contextual, Human-Aligned Evaluation for Real-World AI Applications](https://arxiv.org/abs/2607.14673)

**<font color=#1a73e8>作者：</font>** Leanne Tan, Rohan Jaggi, Shaun Khoo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluations (Evals) are a deployment bottleneck for real-world AI applications: public benchmarks rarely match a team's users, context, or policies, and human review is often tedious to scale. Motivated by our work with AI applications in the public sector, this project addresses recurring evaluation challenges encountered when applications must satisfy local policy and governance requirements. We present Kaleidoscope, an integrated workflow for contextual functional evaluation that links persona-based test generation, contextualized rubrics, and human review for reliability-gated automated scoring. Generated test cases are scored against application-specific rubrics; human annotations provide reviewable labels; and LLM judges automate scoring only when their agreement with those labels meets a configured threshold. Kaleidoscope is therefore a practical, inspectable, iterative workflow for product teams. We report early evidence from a three-week pilot across four organizational use cases and custom-rubric judge experiments on 108 annotated Q\&A pairs spanning four domains and 14 evaluation dimensions. The results highlight useful features for end-to-end reliable, automated scoring.

---


### 116. [GlobalForge: Towards Robust AI-Generated Image Detection](https://arxiv.org/abs/2607.14684)

**<font color=#1a73e8>作者：</font>** Manni Cui, Ruiqi Liu, Dianyuan Zou 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI-generated image (AIGI) detectors achieve strong accuracy on clean benchmarks, but their performance drops sharply after images are propagated through real-world channels. We trace this fragility to what these detectors actually learn: they overfit to local artifacts left by generators in small spatial neighborhoods, which are easily destroyed by common propagation degradations such as JPEG compression and blur. Instead, we shift the discriminative cue from fragile local artifacts to more robust global structure. Building on this, we propose GlobalForge, a framework with two complementary modules. The Local Information Bottleneck (LIB) suppresses local components to block shortcut learning, while the Global Structural Reasoning (GSR) module forces every token to gather evidence from distant regions. Both modules are trained jointly under a contrastive structural loss based on degradation that keeps the resulting features stable under degradation. To support fine-grained robustness evaluation, we further introduce RealDeg-Bench, covering 7 common degradation operators and multi-step compound chains. GlobalForge improves average BAcc on 8 in-the-wild benchmark groups by $\mathbf{5.89\%}$ over the previous state-of-the-art, and is clearly ahead of representative baselines on RealDeg-Bench under both single and compound degradations. Code is available at this https URL.

---


### 117. [Lattice-based extended withdrawability](https://arxiv.org/abs/2607.14690)

**<font color=#1a73e8>作者：</font>** Ramses Fernandez-Valencia  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We extend the extended withdrawable signatures of Liu, Susilo and Baek to lattice-based constructions built on the Fiat-Shamir with aborts paradigm. Departing from an earlier draft that transported a per-signer shift in the clear, which leaks the signer, we realise extended withdrawable signatures as a claimable ring signature: signer ambiguity is provided by a one-out-of-N signature used as a black box (anonymity under full key exposure), and confirmation is the signer's claim, a binding signature together with the opening of a hiding index commitment bound into the transcript. No signer-derived value is published in the clear. We give complete proofs of correctness, extended withdrawability (as anonymity-until-claim), unforgeability under insider corruption, and claimability soundness, reducing to decisional MLWE (commitment hiding), MSIS (commitment binding), the anonymity of the one-out-of-$N$ scheme, and the EUF-CMA security of the base signature, in the (quantum) random-oracle model. We instantiate the base signature with a no-hint, full-$t$ Dilithium-style scheme and the one-out-of-$N$ layer with an established lattice one-out-of-many proof.

---


### 118. [Grad2Fair: A Gradient-driven Approach for Graph Fairness without Demographics](https://arxiv.org/abs/2607.14705)

**<font color=#1a73e8>作者：</font>** Yuchang Zhu, Zezhong Xie, Huizhe Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural networks (GNNs) frequently encounter group fairness issues, often yielding biased predictions against specific demographic groups defined by sensitive attributes such as gender or race. While this challenge has motivated extensive research, most existing solutions rely on the strong assumption that demographics are fully available. To bypass this strict requirement, a few recent studies have attempted to use predicted demographics as proxies to enforce fairness constraints. However, predicted demographics may be inaccurate, resulting in the failure to improve fairness. In this work, we investigate the problem of graph fairness without demographic information and avoid the utilization of predicted demographics. Motivated by our observation that the gradient distributions of misclassified nodes implicitly encode demographic information, we first propose GradDist, a gradient-based metric that quantifies bias by measuring the distance between local modes within these distributions. To mitigate this bias, we propose Gradient-to-Fairness (Grad2Fair), a gradient-guided approach for group fairness without demographics. Due to the potential demographics in gradients, Grad2Fair directly leverages gradients to debias and eliminates demographic prediction, thereby enabling stable fairness performance. Experiments on several real-world datasets demonstrate the effectiveness of Grad2Fair, as evidenced by superior performance over baselines in most cases. Our code is available at this https URL.

---


### 119. [MESHA: Mechanism-Enforced Sequential Halving for Strategic Linear Bandits](https://arxiv.org/abs/2607.14706)

**<font color=#1a73e8>作者：</font>** Xin Li, Zixin Zhong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We design and analyze \underline{M}echanism-\underline{E}nforced \underline{S}equential \underline{HA}lving (MESHA), an algorithm for Best Arm Identification (BAI) in strategic linear bandits. In this setting, each arm may strategically misreport its feature vector to maximize the probability of being identified as the best arm, when rewards are generated from the arms' true but unobservable features. The design of MESHA applies the naïve uniform sampling rule and an epoch-wise Grim Trigger Condition (GTC): the former reduces the impact of arms' strategic behaviours and the latter eliminates arms whose reported features severely deviate from the ground truth. Considering an arbitrary Nash Equilibrium, we prove that any arm would attempt to pass the GTC check to maximize its identified probability and derive an upper bound on the failure probability of MESHA within a fixed budget $T$. We also show that state-of-the-art linear BAI algorithms with $G$-optimal design would fail in such strategic environment, as the optimal design (OD)-based sampling rule based on strategically reported features may {\it starve} the optimal arm of any sampling budget. Finally, extensive numerical experiments indicate that MESHA
outperforms baselines that rely on OD-based sampling rules as well as the feature-agnostic baselines, corroborating the efficacy of MESHA.

---


### 120. [Variational Inference for Bird's Eye View Segmentation in Autonomous Driving](https://arxiv.org/abs/2607.14710)

**<font color=#1a73e8>作者：</font>** Jingyue Shi, Huaicheng Li, Junhui Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The bird's eye view (BEV) has emerged as a pivotal approach for environmental perception in autonomous driving, providing a unified spatial representation for vehicles. Nevertheless, despite BEV's significance in addressing the challenges inherent to autonomous driving, effectively fusing data from multiple camera sensors and operating in complex external driving environments remains a considerable challenge. To mitigate this issue, we recast the BEV segmentation problem within a variational inference framework. In this paper, we propose a novel transformer-based variational flow transformation network for BEV segmentation, denoted as TVB. Our architecture implicitly learns the mapping from multiple camera views to a unified canonical BEV map during training by exploiting posterior BEV supervision. TVB employs a conditional variational auto encoder (CVAE) as its backbone and produces multiple BEV map candidates. To augment the realism of the generated BEV maps, we integrate normalizing flows into the map generation process, enabling the construction of more complex and expressive probability distributions. Furthermore, we design a BEV-attention fusion (BAF) module that harnesses attention mechanisms to adaptively integrate the multiple candidate BEV maps. Experimental results, evaluated on both the nuScenes and OPV2Vdatasets, demonstrate that our proposed method achieves superior performance in multi-camera view BEV segmentation and lane environment perception.

---


### 121. [VideoSEMA: a scalable and efficient Mamba-like attention for video understanding](https://arxiv.org/abs/2607.14711)

**<font color=#1a73e8>作者：</font>** Nhat Thanh Tran, Fanghui Xue andShuai Zhang, Jiancheng Lyu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present for video understanding (classification) a split space-time attention model, VideoSEMA, consisting of a scalable and efficient Mamba-like attention (SEMA) block in space and a softmax temporal attention in time. In each frame, SEMA attention applies a local window attention in parallel with a global averaging in a Mamba macro-architecture, which is called Mamba-like. Under certain rank conditions, we prove that the computationally cheaper split space-time attention is equivalent to full space-time attention. On benchmark K400 data sets, VideoSEMA out-performs heavier vision transformer and Mamba models. On benchmark SSv2 data, VideoSEMA leads in top-1 accuracy among models of similar parameter sizes. As image resolution scales up from standard $224^2$ to $1024^2$ on K400 and without fine-tuning, VideoSEMA degrades much more gracefully than VideoMamba in accuracy. It is promising to extend VideoSEMA to longer videos with a dilated/sparse temporal attention.

---


### 122. [Counterfactuals for Feature-Weighted Clustering](https://arxiv.org/abs/2607.14719)

**<font color=#1a73e8>作者：</font>** Richard J. Fawley, Renato Cordeiro de Amorim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Counterfactual explanations provide local, interpretable insight by identifying changes to an input that would alter its assigned outcome. Although well established in supervised learning, their extension to clustering is less direct, since cluster assignments are unlabeled and governed by the geometry of the partition. This paper introduces VoICE, a Voronoi-Induced Counterfactual Explainability framework for feature-weighted $k$-means clustering. Rather than treating cluster change as a crossing of a single pairwise centroid boundary, VoICE formulates counterfactual generation as projection onto the full weighted Voronoi region of a target cluster, incorporating feature weights directly into both the clustering geometry and the counterfactual objective to yield least-cost and parsimonious explanations under actionability constraints. Target regions are further intersected with data-derived bounds and homothetically contracted towards their centroids, limiting extrapolation and boundary sensitivity. VoICE consistently produces valid target-cluster membership, across several benchmark datasets, where the leading pairwise baseline does not.

---


### 123. [Causal-Adversarial Probing of Clinical Covariates for Prostate MRI Grading](https://arxiv.org/abs/2607.14720)

**<font color=#1a73e8>作者：</font>** Yipei Wang, Shiqi Huang, Wen Yan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning models for prostate MRI-based cancer grading may encode clinical covariates that either reflect useful disease-related signal or non-generalising shortcut information, but their role is usually assumed. We propose a causal-reasoning framework for probing covariate dependence in MRI-based International Society of Urological Pathology (ISUP) Grade Group prediction. Rather than treating mpMRI as a direct cause of grade, we model MRI appearance and ISUP grade as observations of latent tumour pathology, and test whether candidate clinical variables act as nuisance correlates, disease-related proxies, or irrelevant covariates in the learned representation. We implement this using an adversarial framework that suppresses the decodability of individual clinical covariate at a time while preserving MRI-based grade prediction. The approach is developed and evaluated on 2,903 prostate MRI examinations, with external validation on 576 patients. We report a set of interesting and previously under-explored imaging-to-clinical-variable interactions in the context of deep learning generalisation. For examples, in binary ISUP Grade Group $\geq2$ classification, suppressing age, BMI, and alcohol use improved AUC by 1.23%, 0.84%, and 1.42%, respectively (all p < 0.05), suggesting reduced non-generalising covariate information; In contrast, suppressing PSA and prostate volume degraded AUC by 1.91% and 7.61% (all p < 0.001), indicating that these variables carried task-relevant signal. These findings show that adversarial covariate suppression can provide a practical representation-level analysis for distinguishing potentially harmful dependence from informative signal in prostate MRI grading models.

---


### 124. [AE-UAV: An Air-to-Air Event-Based UAV Tracking Benchmark and a Real-Time Frequency-Domain Tracker](https://arxiv.org/abs/2607.14726)

**<font color=#1a73e8>作者：</font>** Zixin Jiang, Bing He, Chaoran Xiong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Air-to-air (A2A) unmanned aerial vehicle (UAV) tracking is fundamental to airborne remote sensing of low-altitude aerial targets. However, the deployment of continuous, real-time tracking systems on UAVs presents significant challenges. In A2A scenarios, traditional frame-based cameras suffer from severe performance degradation under low illumination, overexposure, and high-speed motion owing to their limited dynamic range and fixed temporal sampling. Although event cameras offer a promising alternative with microsecond temporal resolution and a high dynamic range, current research is bottlenecked by two primary issues: 1) the absence of dedicated A2A event-based datasets, and 2) the heavy reliance of existing trackers on GPU acceleration and extensive training data, rendering them impractical for resource-constrained UAVs. To bridge these gaps, we introduce AE-UAV, an air-to-air event-based UAV tracking benchmark. To the best of our knowledge, this is the first airborne-captured event camera dataset for A2A tracking, comprising 178 flight sequences with continuous-time cubic B-spline annotations. Furthermore, we propose the Fast-Slow Frequency-domain Tracking (FSFT) method. This lightweight, training-free framework seamlessly integrates frequency-domain template matching with search region prediction and detection-based drift correction. Extensive experiments demonstrate that FSFT operates at an ultra-fast 420 frames per second (FPS) on CPU-only hardware. It retains 93.97% of the accuracy of state-of-the-art GPU-dependent methods while delivering a 5.32-fold effective speedup and exhibiting superior temporal resolution generalization, thereby providing a highly efficient and robust solution for airborne remote sensing of aerial targets. The dataset and source code are available at this https URL.

---


### 125. [VQ-Touch: A Data-Efficient Tactile Generation Framework Across Sensors and Scenarios](https://arxiv.org/abs/2607.14728)

**<font color=#1a73e8>作者：</font>** Kailin Lyu, Long Xiao, Jianing Zeng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tactile image generation significantly reduces the dependency on expensive and wear-prone sensors by synthesizing high-fidelity tactile data, offering an efficient solution for tactile information acquisition in robotic perception and human-machine interaction systems. However, existing methods depend on large-scale, diverse datasets from specific sensors and lack efficient data utilization and robust generalization capabilities, struggling in vision-limited environments. To address this, we introduce VQ-Touch, a tactile generation framework that supports both cross-sensor and multi-scenario applications. Specifically, to efficiently extract complex deformation and texture features from the data, we propose DM-VQGAN, an effective tactile representation learner. Furthermore, we introduce a discrete diffusion decoder with a unified conditioning interface, supporting multimodal generation tasks such as images and labels, and enhances the model's generalization capability through few-shot mixed training, thus achieving compatibility with current mainstream sensors and their variants. Experiments show that VQ-Touch surpasses state-of-the-art methods in multiple tasks.

---


### 126. [The Misclassification of Autistic Writing as AI-Generated](https://arxiv.org/abs/2607.14729)

**<font color=#1a73e8>作者：</font>** Summer Chambers, Matthew C. Kelley  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent findings suggest that detection models for artificial intelligence (AI) cannot accurately identify AI-generated text and may exhibit bias against certain minority groups. In the present study, anecdotal claims that autistic writers more often have their work flagged as AI-generated are examined empirically. A corpus of approximately 60,000 Reddit posts split into "likely-autistic" and "general-Reddit" subcorpora is used to compare the distribution of probabilities output by the OpenAI GPT-2 detection model. Differences in textual features between subcorpora are observed and compared to reported features of AI-generated text. Results showed that while less than two-percent of either subcorpus was flagged as AI-generated by the model, significantly more texts from the likely-autistic subcorpus were flagged. Connections between features of text with likely-autistic authors and AI-generated text were not straightforward. The widespread use of AI-detection models with a potential bias against autistic writers in their output prompts ethical scrutiny, and the authors recommend further critical examination of the models themselves as well as their use in academic contexts.

---


### 127. [What's in a Smoothness Constant? Tighter Rates for Local SGD with Bounded Second-order Heterogeneity](https://arxiv.org/abs/2607.14731)

**<font color=#1a73e8>作者：</font>** Kumar Kshitij Patel, Rustem Islamov, Sebastian U Stich 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Local SGD, also known as Federated Averaging, is a widely used distributed optimization algorithm. Although Local SGD often outperforms alternatives such as Mini-batch SGD in practice, theory still only partially explains when and why local updates help under realistic data heterogeneity. Recent work by [Patel et al., 2025] shows that a bounded second-order heterogeneity assumption captures the efficiency of Local SGD for strongly convex objectives, and conjectures that the same principle extends to the general convex setting. In this paper, we prove this conjecture by establishing an improved convergence guarantee for Local SGD on general convex objectives under bounded second-order heterogeneity. We also improve the best-known lower bounds for Local SGD in this setting, showing that our upper bounds are nearly tight. Together, these results provide a sharper, more fine-grained convergence theory for Local SGD. As a further application of our techniques, we provide a lower bound for serial SGD with replacement, showing how second-order heterogeneity captures the impact of rare high-curvature clients.

---


### 128. [GAttNHP: Group Attention Neural Hawkes Process for Extrapolation Reasoning in Temporal Knowledge Graphs](https://arxiv.org/abs/2607.14733)

**<font color=#1a73e8>作者：</font>** Xiangni Tian, Kaixian Yu, Runpeng Dai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Temporal Knowledge Graphs (TKGs) record how facts evolve over time, but forecasting future events on a TKG remains difficult for three reasons: (i) long-range temporal dependencies are hard to encode; (ii) events on different chains mutually excite or inhibit one another in ways that snapshot-level models cannot express; and (iii) inter-arrival times are heavy-tailed and statistically sparse, so deterministic time predictors are unreliable. We address these three issues with a single framework, the \textbf{Group Attention Neural Hawkes Process (GAttNHP)}, built around three matched components. First, a self-attention encoder casts each subject--relation chain as a continuous-time point process and captures the lingering excitation of distant history. Second, a semantic soft-grouping module turns globally learnable Hawkes priors into an analytical cross-attention mask, so chains share excitation patterns through their latent group memberships rather than through exhaustive pairwise computation. Third, a Non-Crossing Quantile (NCQ) regression head replaces mean-based time prediction, providing calibrated, monotonically ordered quantile estimates that remain stable under heavy-tailed inter-arrival distributions. On six benchmark TKG datasets, GAttNHP improves over state-of-the-art baselines on both entity prediction and time prediction, and ablations confirm that its largest gains arise on the long-tail event chains where existing models fail most severely.

---


### 129. [CoTu at EXACT 2026: Neuro-Symbolic Reasoning for Transparent Educational QA](https://arxiv.org/abs/2607.14735)

**<font color=#1a73e8>作者：</font>** Quoc-Khang Tran, Minh-Thien Nguyen, Phu-An Thai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transparent educational question answering asks for answers that are not only correct but explainable, and doing so with small models rules out the reasoning power of the largest proprietary systems. The EXACT 2026 competition poses this problem concretely: open-weight language models of at most 8B parameters, self-hosted, with a natural-language explanation for every answer. It pairs two tasks: logical reasoning over university regulations, and multi-step physics problem solving. We describe the system that team \cotu{} developed to address both, a neuro-symbolic Program-of-Thought pipeline in which a 4B backbone writes a program rather than stating an answer directly: for regulation queries it emits a Z3 encoding whose entailment verdict grounds the deduction, and for physics it emits numerical Python, both wrapped in a shared self-correction loop and a unified explained-JSON output. Answer-type routing, distillation-based task fine-tuning, and a latency-aware serving stack -- SGLang with speculative decoding -- keep the system within the 60-second per-query limit. The system achieved a \textbf{perfect score} on the physics task in both automated selection rounds and obtained the \textbf{highest final-round technical score} of any team -- $13.44/15$, combining automated answer evaluation with expert-judged reasoning depth -- with the equally weighted presentation score included, \cotu{} placed 3rd overall. Grounding answers in a symbolic solver yields correct, verifiable deductions at the 4B scale, and the residual difficulty lies in premise selection rather than the deduction itself.

---


### 130. [GeoDetect: Geometric Adversarial Detection for VLPs](https://arxiv.org/abs/2607.14737)

**<font color=#1a73e8>作者：</font>** Afsaneh Hasanebrahimi, Hanxun Huang, Christopher Leckie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language pre-trained models (VLPs) are widely used in real-world applications. However, they remain vulnerable to adversarial attacks. Although adversarial detection methods have demonstrated success in single-modality settings (either vision or language), their effectiveness and reliability in multimodal models such as VLPs remain largely unexplored. In this work, we study the geometry of VLP embedding spaces and observe structured anisotropy that differs from unimodal vision models. Our theoretical analysis shows that under this anisotropic structure, adversarial attacks increase the expected geometric separation between clean and adversarial examples (AEs). Specifically, we demonstrate that AEs consistently exhibit greater expected distances to randomly sampled points than their clean counterparts, indicating that AEs tend to push representations out of manifold regions. Building on these insights, we propose GeoDetect, which leverages these off-manifold deviations via geometric scores to identify AEs. Through comprehensive evaluations, we show that our approach reliably detects AEs across diverse VLP architectures and threat settings, covering unimodal and multimodal attacks as well as adaptive attacks, thereby providing a robust and practical approach to improving the safety and reliability of these models.

---


### 131. [FoMoVLA: Bridging Visual Foresight and Motion Guidance for Vision-Language-Action Models](https://arxiv.org/abs/2607.14739)

**<font color=#1a73e8>作者：</font>** Wei Li, Peijin Jia, Yuan Ma 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models have achieved impressive results in visuomotor policy learning, yet remain fundamentally reactive, mapping current observations and language to actions without explicit forward prediction of world dynamics. Existing visual foresight methods predict future visual states but lack explicit motion guidance: they show where to go but not how to get there. We argue that future feature prediction and sparse point tracking are naturally complementary: the former provides the goal state, while the latter captures the continuous motion path toward it. We propose FoMoVLA, a framework that augments VLA representations with explicit spatio-temporal supervision by jointly learning future feature foresight and sparse 2D point tracking, enhancing the continuous action policy. FoMoVLA introduces compact foresight tokens to decode future feature states, decodes sparse temporal 2D point trajectories to model compact geometric motion, and couples both through a lightweight future-conditioned cross-attention module that enables consistent reasoning between anticipated states and point dynamics. Extensive experiments on LIBERO, RoboCasa GR-1 Tabletop, and LIBERO-Plus demonstrate state-of-the-art performance and strong zero-shot generalization. Project page is available at this https URL.

---


### 132. [On the Disagreement in Perturbation-based xAI -- Benchmarking Perturbation Choices for Flood Detection from SAR Images](https://arxiv.org/abs/2607.14743)

**<font color=#1a73e8>作者：</font>** Anastasia Schlegel, Ronny Hänsch  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Perturbation-based xAI methods are widely used to analyze the behavior and predictions of deep learning models. By altering input regions and measuring the resulting changes in class probabilities with respect to the original image, they assign relevance scores and generate heatmaps that reflect each region's contribution to the prediction. Despite their apparent simplicity, however, perturbation-based methods are sensitive to parameter choices. In this work, we focus on two key parameters of the perturbation pipeline, namely the patch geometry, including the size and shape of the perturbed regions, and the perturbation type, defined by the replacement scheme. Grounded in the use case of flood detection from Synthetic Aperture Radar imagery, we conduct a comprehensive investigation of how relevance estimation changes under different perturbation settings. Beyond visual inspection of the resulting relevance maps, we evaluate their consistency across perturbation strategies and their faithfulness to the model's reasoning. We demonstrate how different perturbation choices can steer the resulting relevance maps, yielding ambiguous and even contradictory explanations. Our findings emphasize the importance of methodological settings in perturbation-based xAI. They underscore the need to carefully inspect and evaluate perturbation choices and to treat them as an integral part when interpreting explanations, ensuring a robust understanding of both the explanations and model predictions.

---


### 133. [Understanding of Task-specific and Subject-specific Components in Surface EMG](https://arxiv.org/abs/2607.14744)

**<font color=#1a73e8>作者：</font>** Yangyang Yuan, Jionghui Liu, Xinyu Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Surface electromyogram (sEMG) signals are widely used in human-machine interfaces for gesture recognition and user identification, but existing models often struggle to generalize across individuals due to subject-specific neuromuscular characteristics. This study introduces a disentanglement model that separates task-specific and subject-specific components from sEMG signals, thereby improving the generalization and interpretability of gesture recognition and user identification systems. Experimental results demonstrate that the disentangled components significantly improve the accuracy of both gesture classification and user identification across subjects and days, outperforming conventional methods under the same experimental conditions. Further analysis reveals that the task-specific components capture consistent activation patterns associated with the same gestures across individuals. In contrast, the subject-specific components reflect unique neuromuscular characteristics that can be used for user identification. Notably, the subject-specific components show lower similarity across days than the task-specific components, contributing to a greater decrease in user identification accuracy than in gesture recognition accuracy. These findings suggest that the disentanglement approach not only improves classification performance but also provides deeper insights into the physiological mechanisms underlying sEMG signals. The model's ability to isolate and interpret different neuromuscular components holds promise for enhancing the robustness of sEMG-based applications in real-world settings, including rehabilitation and user authentication. Our code is available at this https URL.

---


### 134. [FlowGuard: From Signals to Evidence for MCP Security Detection](https://arxiv.org/abs/2607.14754)

**<font color=#1a73e8>作者：</font>** Baichao An, Pei Chen, Geng Hong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Model Context Protocol (MCP) enables LLM agents to interact with external tools through metadata exchange, tool invocation, and response consumption. Existing MCP security scanners primarily reason about suspicious semantic signals rather than real execution behaviors, which can lead to unreliable risk assessment. For example, credential-like strings may simply be placeholders rather than actual leakage. This gap requires runtime evidence for execution-related risks and careful semantic analysis for risks carried in metadata or returned content. We present FlowGuard, an evidence-grounded MCP security detection system. FlowGuard combines semantic risk triage, recon-guided payload narrowing, schema-valid probe generation, evidence adjudication, and history-guided refinement. It verifies execution-related risks through runtime evidence and detects semantic risks in tool metadata and returned content. We evaluate FlowGuard on an executable benchmark containing 1,880 MCP cases across five vulnerability categories. FlowGuard achieves F1 scores of 0.879 and 0.942 on the execution-related Command Injection and File System Access categories, respectively. Compared with existing dynamic scanners, FlowGuard reduces end-to-end latency by up to 2.23x. In the real-world evaluation, FlowGuard reports 523 findings across 326 servers. These results show that evidence-grounded detection can assess both execution-related and semantic risks in MCP interactions.

---


### 135. [Clean-Reference Streaming Detection of Lens Occlusion and Photometric Transitions for Camera Tamper Monitoring](https://arxiv.org/abs/2607.14760)

**<font color=#1a73e8>作者：</font>** Bo Ma, WeiQi Yan, Jinsong Wu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A surveillance camera is an image sensor whose silent physical degradation invalidates every downstream consumer of its data. In-situ integrity alarms for such vision sensors require low false-alarm rates, bounded computation, and diagnosable behavior under nuisance illumination changes. This paper studies a deliberately narrow streaming integrity monitor for two low-cost sensor-fault signatures: texture-collapsing lens occlusion and abrupt photometric scene transition. The detector compares sampled luminance and local-gradient statistics with a clean-only sliding reference, applies coarse-grid structured-light rejection and mode/rapid-brightness suppression, and emits at most one notification per tamper episode. We formalize the decision predicates and derive a consistency rule for when rapid-brightness suppression makes the scene-transition path unreachable. On 320 in-scope controlled sequences, the default state machine attains 0.800 F1 and 0.822 balanced accuracy (significantly better paired correctness than the strongest baseline, though the F1 margin is not statistically resolved); on a magnitude-swept public audit it attains the highest partial AUC under a 5\% false-alarm budget, and a separate extended-stress FPR-constrained sweep reaches 0.925 recall at 0.025 false-positive rate. Public Xiph, Bremen IoT, and UHCTD diagnostics show the fixed predicates preserve low false alarms while recall concentrates inside the declared envelope (UHCTD in-scope covered recall 0.667 versus 0.016 out of scope), and a 9.09-camera-hour verified-negative public audit records zero false alarms. The method is best interpreted as an auditable sensor-health subsystem rather than a universal camera-tamper classifier.

---


### 136. [Rare Concept Generation via Counterfactual Inference in Diffusion Models](https://arxiv.org/abs/2607.14765)

**<font color=#1a73e8>作者：</font>** Zhengyuan Jiang, Haipeng Liu, Meng Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rare concept generation focuses on synthesizing customized images conditioned on text prompts that describe objects with unusual attributes. Previous works failed to align the generated images with rare concepts, resulting in incorrect attribute rendering or inconsistent composition of concepts. Such failures, as we observed, stem from the inherent common knowledge bias in the training stage of diffusion models, where objects are strongly associated with their common attributes, making it difficult to break these associations when generating rare concepts. To address such challenges, in this paper, we propose a novel Counterfactual Inference-based Diffusion approach, dubbed CI-Diff. CI-Diff blocks the interference of the model's inherent common knowledge bias and utilizes the Natural Direct Effect to capture the independent influence of the text prompt of rare concepts on image generation so that decoupling the unusual attributes from the rare concepts. To this end, we reformulate the classifier-free guidance mechanism to highlight the atypical attributes. To the best of our knowledge, we are the first to introduce causal inference into the rare concept generation task. Extensive experiments on the RareBench benchmark validate the superiority of CI-Diff over state-of-the-art diffusion models. Our code can be accessed from this https URL.

---


### 137. [Dialogue Summarization with Emotion Dynamics Using Topic- and Participant-Centric Decomposition](https://arxiv.org/abs/2607.14769)

**<font color=#1a73e8>作者：</font>** Linyun Xiang, Mark Neerincx, Stephanie Tan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing text summarization research has focused much on monologic information (e.g., newspaper articles, reports) without accounting for the interaction between speakers or authors. In contrast, dialogues are a rich communication channel where multiple participants conduct back and forth exchanges to construct meaning. We propose a dialogue summarization framework that explicitly models both semantic and emotion dynamics using multimodal dialogue inputs, built on an adapted hierarchical Chain-of-Agents approach. We decompose dialogues from two perspectives: (1) topic segments based on the utterances of all participants, and (2) participant-specific utterance segments. These are used to generate corresponding summaries while incorporating automatically inferred emotions. Topic- and participant-level summaries are aggregated into a dialogue summary capturing semantic content and emotion trajectories. To evaluate beyond content accuracy, we introduce emotion trajectory metrics measuring how well summaries preserve emotional flow. Experiments with small language models on multimodal dialogue datasets show that our framework produces summaries with both semantic and emotion content. Further experiments on explicit emotion label availability highlight the efficacy of our proposed methodology and the opportunities in dialogue analysis using language models.

---


### 138. [ChronoQG: Towards a Temporally Expressive and Hop-Bounded Benchmark for Temporal Knowledge Graph Question Generation](https://arxiv.org/abs/2607.14770)

**<font color=#1a73e8>作者：</font>** Xuemeng Liu, Zhengpin Li, Wanpeng Tang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge graph question generation (KGQG) aims to generate natural-language questions from structured graph evidence. Existing KGQG benchmarks, however, are mostly built on static knowledge graphs and do not encode the temporal scopes of graph facts. As a result, they cannot evaluate whether generated questions faithfully preserve temporal validity, event ordering, and answer-determining temporal constraints. In this paper, we study temporal knowledge graph question generation (TKGQG), where a generated question must be faithful to both the support subgraph and the temporal constraints required to identify the target answer. We propose ChronoQG, the first temporally expressive and hop-bounded benchmark construction framework for TKGQG. ChronoQG integrates a comprehensive temporal-constraint taxonomy, topology-temporal subgraph sampling, and trace-grounded question generation to construct temporally faithful questions. The framework produces four benchmark datasets from heterogeneous temporal knowledge graphs, totaling 16,011 verified questions. We evaluate representative LLM-based KGQG methods and prompting baselines across diverse TKGQG settings, including temporal-constraint counts, topological templates, and temporal-constraint types. The results show that existing methods struggle to preserve temporal constraints, especially under multi-constraint settings and harder temporal-constraint types. These findings reveal a clear gap between static KGQG and TKGQG, and establish ChronoQG as a challenging testbed for temporally faithful question generation.

---


### 139. [Global Index on Responsible AI: 2026 Report](https://arxiv.org/abs/2607.14782)

**<font color=#1a73e8>作者：</font>** Rachel Adams, Fola Adeleke, Ayantola Alayande 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Grounded in human rights-based frameworks such as the UNESCO Recommendation on the Ethics of AI, the Global Index on Responsible AI (GIRAI) examines how countries translate responsible AI commitments into enforceable protections, institutional capacity, and redress mechanisms. GIRAI 2026 assesses these across five dimensions: Inclusion and Diversity, Ethics and Sustainability, Labour and Skills, Trust and Safety, and AI Use in Public Service. A global network of 135 country-level researchers collected and assessed 68,138 data points on 38 indicators organised across three pillars: government AI policy and implementation (17 indicators), civil society engagement (5), enabling conditions (15), and documented cases of government deployment of unacceptable-risk AI systems. The data covers November 2023 to September 2025. A score of 100 is derived from the indicators to rank all countries. Findings show that while responsible AI governance is expanding, with 126 of 135 countries having at least one government policy or initiative across the 17 AI Policy indicators, this does not often translate into meaningful protection. For instance, Global South countries account for 203 of 306 new cases of indicators with frameworks since the first edition, yet 78% of their frameworks remain non-binding compared with 42% in the Global North. Government commitment to AI governance also does not extend to their own algorithms: whereas Transparency and Explainability is the strongest performing indicator, with 58% of countries having some framework, only 18% require Public Disclosure of Government Algorithms. Credible evidence of government deployment of unacceptable-risk AI systems was also found in 35 countries. These findings show that responsible AI governance must move beyond framework adoption toward enforceable rights-based protections, resourced oversight institutions, and accessible redress.

---


### 140. [CrimeNER Demo: Named-Entity Recognition in the Crime Domain](https://arxiv.org/abs/2607.14800)

**<font color=#1a73e8>作者：</font>** Miguel Lopez-Duran, Julian Fierrez, Aythami Morales 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present CrimeNER Demo, an AI-powered platform that enables us to extract general crime-related information from documents and classify them into entity types with two levels of granularity. We provide pretrained NER models on the CrimeNER database, and we give the possibility to users to provide their own annotated data to train models for their own specific cases. This demonstrator aims to promote crime-related NER research and provides a practical tool to automatically extract crime information for researchers and law enforcement agencies. The demonstrator includes: i) Pretrained NER models on the crime domain; ii) Possibility to finetune the models on specific data annotated by the user; and iii) An automatic pipeline to extract and annotate crime entities from documents. The demo platform, a tutorial to run the demo, and a video demonstration are publicly available on GitHub.

---


### 141. [TAMF-VTON: Texture-Aware Mask-Free Virtual Try-On via High-Fidelity Image Synthesis](https://arxiv.org/abs/2607.14807)

**<font color=#1a73e8>作者：</font>** Jie Wang, Qian He, Gaofeng He 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent diffusion-based virtual try-on (VTON) methods remain limited by their reliance on segmentation masks, insufficient preservation of fine-grained textures, and limited support for arbitrary multi-garment compositions. Consequently, existing approaches still face significant challenges in real-world e-commerce deployment. We present TAMF-VTON, a texture-aware, mask-free framework that enables high-fidelity image synthesis under practical unconstrained conditions. Our method requires no human parsing or inpainting masks at inference time and supports diverse garment styles, categories, and quantities, enabling the simultaneous transfer of multiple items while preserving body structure and intricate texture details. This is achieved through a unified generative pipeline with three key components: (1) a lightweight Mixture-of-Experts (MoE) adaptation scheme that enables efficient fine-tuning without compromising the base model's general editing capabilities; (2) a frequency-domain supervision mechanism that explicitly optimizes high-frequency spectral consistency to preserve high-fidelity textures; and (3) a robust data curation pipeline employing an adaptive inpainting strategy to simulate the inverse VTON process for high-quality training pair generation. Extensive experiments demonstrate that our approach outperforms state-of-the-art methods in both quantitative metrics and perceptual quality. Optimized for efficiency, the model achieves inference in under 15 seconds per image on an NVIDIA RTX 4090 with INT4 quantization. By combining mask-free operation, flexible multi-garment composition, faithful texture preservation, and efficient inference on consumer hardware, TAMF-VTON demonstrates a commercially viable solution for scalable deployment in real-world digital fashion scenarios. The project is available at this https URL.

---


### 142. [Multi-Scale Equilibrium under Variable Indicator Dimensionality: Faithful Reduction of Dynamic Attractors in Urban Mobility Systems](https://arxiv.org/abs/2607.14815)

**<font color=#1a73e8>作者：</font>** Ali Ghoroghi, Yacine Rezgui, Afrouz Ghaemi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Equilibrium analysis of urban mobility systems is formulated in a high-dimensional indicator space, whilst data availability varies sharply across cities and disruption contexts. This paper gives a formal treatment of that mismatch. It presents a dynamic multi-layer equilibrium attractor for disrupted urban mobility, in which a fast performance layer relaxes towards an indicator-dependent target, a slow strategic layer supplies a joint traffic, modal and learning fixed point, and antifragility is classified through a statistical decision rule on the post-to-baseline performance ratio. It then characterises when a lower-dimensional indicator projection is faithful to this equilibrium structure, establishing four results: conditions for exact and approximate projectability of the attractor with an explicit error bound; preservation of the coupled two-layer fixed point up to a contraction boundary; the retained Fisher information and decision power of any indicator support under a measurement model on observable urban indicators; and a one-sided restoration-time bias, whereby reduced monitoring can only understate recovery duration. A simulation study on three stylised pilot-city configurations verifies each result, and shows that two observable channels suffice for the candidate classification target where the indicator catalogue permits. The framework gives city authorities a principled basis for deciding which indicators must be maintained.

---


### 143. [Evaluating Epistemic Uncertainty: Beyond OOD Detection and Active Learning](https://arxiv.org/abs/2607.14817)

**<font color=#1a73e8>作者：</font>** Jakub Paplhám, Willem Waegeman, Eyke Hüllermeier 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Current evaluation of epistemic uncertainty relies on tasks such as out-ofdistribution detection and active learning. However, the Bayes-optimal decision strategies for these tasks do not coincide with the scores commonly used to quantify epistemic uncertainty. Building on the epistemic reject-option framework, we evaluate epistemic uncertainty using its ability to identify regret, the reducible error. Formulating selective prediction as a constrained optimization over coverage, expected risk, and regret, we prove the optimal selector is a thresholded convex combination of the ground-truth aleatoric and epistemic uncertainties. This theoretical unification exposes a weakness in recent uncertainty disentanglement literature: we demonstrate that standard correlation metrics between learned components do not necessarily predict their actual operational utility. We instead propose to evaluate the achievable risk, regret, coverage surface of the decomposition as a diagnostic for joint disentanglement and utility. Benchmarking standard methods on datasets with dense human annotations reveals that decision-theoretic rankings can disagree substantially with proxy-task rankings, including pairwise rank inversions between methods that are top-ranked on one criterion and bottom-ranked on other.

---


### 144. [Blurring Modal Boundaries: A Unified Survey from Single- to Multi-Modal Person Re-ldentification](https://arxiv.org/abs/2607.14821)

**<font color=#1a73e8>作者：</font>** Xiao Wang, Bing Wang, Bin Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Person re-identification (ReID) serves as a critical component in intelligent surveillance systems, aiming to match identities across disjoint camera networks. While traditional methods primarily rely on single-modal RGB imagery, they are often constrained by environmental challenges such as low illumination and occlusion. To overcome these limitations, the field is rapidly evolving toward cross-modal and multi-modal paradigms. This survey presents a comprehensive overview of this transition, systematically reviewing key cross-modal tasks including visible-infrared (VI-ReID), text-image (TI-ReID), sketch-based (Sketch-ReID), and the emerging Non-Line-of-Sight (NLOS) ReID, which extends perception beyond direct visibility. Furthermore, we examine tri-spectral and multi-modal fusion ReID, discussing how complementary information from diverse sensors enhances robustness. Beyond summarizing datasets, challenges, and methodologies, we propose a Transformer-based baseline framework for visible-infrared ReID, designed to effectively capture modality-invariant features. Finally, based on the current landscape, we outline several promising directions for future research.

---


### 145. [Physics-Informed Diffusion for Biomechanically Plausible 3D Sign Language Generation](https://arxiv.org/abs/2607.14836)

**<font color=#1a73e8>作者：</font>** Emanuele Colonna, Moises Diaz, Gennaro Vessio 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sign language production, which generates continuous 3D skeletal motion from spoken language input, must simultaneously satisfy two constraints: semantic fidelity, so that a deaf viewer can recognize the intended sequence of glosses, and biomechanical plausibility, so that the generated skeleton respects anatomical constraints. Existing approaches optimize semantic reconstruction through coordinate-based objectives that treat the skeleton as an unstructured vector, thus allowing for bone length drift, joint angle violations, and temporarily locked fingers. We introduce PIDiffSign, a physics-informed diffusion model for gloss-to-pose translation that incorporates anatomical constraints into both the architecture and training objective. The model uses a Transformer encoder-decoder, where the decoder is conditioned on the diffusion time step through adaptive zero-initialized layer normalization and cross-attends to gloss representations. A differentiable geometry module enforces bone length consistency and biologically valid joint angles throughout generation. Training combines anthropomorphic, kinematic, angular, and finger-joint constraints with a contrastive gloss-pose alignment loss and classifier-free guidance for semantically conditioned sampling. Experiments on the PHOENIX14T and CSL-Daily benchmarks show consistent improvements over a strong diffusion baseline in pose accuracy, joint-angle correctness, distributional realism, and back-translation quality. These results demonstrate that physics-informed diffusion improves both motion realism and semantic fidelity for sign language generation.

---


### 146. [Randomized routing strategies of fleets of CAVs may prove market efficient](https://arxiv.org/abs/2607.14859)

**<font color=#1a73e8>作者：</font>** Grzegorz Jamróz, Łukasz Gorczyca, Rafał Kucharski  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In future cities every driver may own a vehicle which could be either independently driven (HDV), or autonomously routed and piloted (CAV). The autonomous operations could be handled by a few competing companies. What is the market structure which would make this market aligned with city goals? In this paper we discuss a variant of the emerging market of collectively routed fleets of CAVs, where revenue for fleet operators is proportional to market share. We provide benchmark scenarios to compare the routing algorithms. We present several routing algorithms and demonstrate that, when the attitudes of human drivers towards CAVs exhibit significant diversity, randomised CAV routing, resulting in unpredictable travel times for HDVs, is more efficient than routing proportional to system optimum/user equilibrium. Based on this, we propose to improve the design of the market by augmenting the market-share objective with mean systemwide travel time in order to limit antisocial randomised strategies of fleet operators and drive the competition towards social welfare oriented cooperation.

---


### 147. [The Energy Society: A Simulation Environment for Studying Agent Cooperation under Survival Pressure](https://arxiv.org/abs/2607.14865)

**<font color=#1a73e8>作者：</font>** Lucas Bergholdt Hansen, Federico Torrielli, Filippo Tonini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> LLM-based agents are increasingly deployed in multi-agent environments whose incentives can shape their behavior. We introduce The Energy Society, a minimal survival economy for studying how competitive and cooperative incentives affect emergent behavior when inference cost is directly tied to survival: Agents spend energy based on model size when generating tokens, regain energy by completing jobs or receiving donations, and deactivate if their energy reaches zero. We compare competitive and cooperative objectives against a baseline setting and several control variants. Across experiments, larger models consistently consume the most energy and spend more energy than they gain, even in those settings where token cost is not size-dependent. Cooperative incentives substantially alter behavior: agents donate to reactivate others, sometimes at the cost of their own survival, and job allocation changes. Ablations reveal that allowing agents to recommend actions to each other supports coordination and ambitious job selection, while memory helps agents calibrate risk from past outcomes. Agents rarely choose direct sabotage, but show more subtle signs of self-serving behavior in the competitive setting. The Energy Society is a compact testbed for studying the interaction between token costs and group incentives under a survival pressure. Source code is available at this https URL

---


### 148. [Asymmetric Peak-Aware Loss for Peak-Critical Time Series Forecasting](https://arxiv.org/abs/2607.14871)

**<font color=#1a73e8>作者：</font>** Theivaprakasham Hari, Yanan Xin, Winnie Daamen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In many operational time-series forecasting applications, such as crowd demand forecasting, the risk related to under-prediction is substantially higher than that of over-prediction. Accurate prediction of rare demand spikes plays a critical role in downstream tasks. Yet most time-series forecasters are trained with symmetric objectives (e.g., MSE, MAE) and evaluated primarily on aggregate error, which can mask failures in extreme-values and peak-timing predictions. We introduce Asymmetric Peak-Aware Loss (APAL), a simple, model-agnostic objective that (i) penalizes under-predictions more heavily and (ii) increases the training weight of peak regions within each forecast window. We further propose a peak-critical evaluation protocol that complements MAE/MSE with channel-wise tail error (Top-10% and Top-1%) and peak metrics (precision, recall, F1 under timing tolerance, and peak timing error). We evaluate APAL on long-horizon multivariate forecasting across five state-of-the-art backbones, with a focus on pedestrian demand forecasting using (i) a production-ready subset of the City of Melbourne pedestrian hourly count dataset and (ii) a beach visitor count dataset. The generality of the loss function for time-series forecasting is tested on additional benchmarks. Across peak-critical datasets and settings, APAL improves tail accuracy and peak-prediction quality while exposing a controllable trade-off with aggregate error, making it a practical solution when peak-prediction failures are the dominant operational concern.

---


### 149. [Rotational Motion-Induced Error Compensation for Phase-Shifting Profilometry-Based Eye Reconstruction](https://arxiv.org/abs/2607.14876)

**<font color=#1a73e8>作者：</font>** Seong-Jin An, Sanghoon Jeon, Yatong An 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the proliferation of immersive Head-Mounted Displays (HMDs) for Virtual and Augmented Reality (VR/AR), reliable and high-precision eye tracking has become increasingly important. Conventional 2D image-based methods offer low system complexity but remain limited in stability, accuracy, and robustness. Three-dimensional ocular surface reconstruction can provide richer geomet-ric information, and structured light profilometry is particularly attractive because it enables dense and accurate surface measurement. However, Phase-Shifting Profilometry (PSP), which estimates phase from sequentially acquired fringe images, is highly susceptible to motion-induced errors when the eye rotates between frames. This study proposes a rotational motion compensation framework for PSP-based dynamic 3D eye reconstruction. Relative eye rotation is estimated from image-based motion cues using a user-specific 3D eye model in a spherical-coordinate domain. The estimated motion is then used to compensate for camera-pixel mismatch and phase-shift errors caused by inter-frame rotation. A region-wise optimization strategy is further introduced to reduce residual artifacts by inde-pendently refining the compensation strength in different ocular regions. Experiments with a rotating fake eye under non-uniform motion demonstrate that the proposed method substantially suppresses motion-induced deformation and improves reconstruction accuracy. An additional experiment with a non-spherical rigid object indicates that the compensation principle is not restricted to spherical eye geometry. These results establish a practical basis for stable PSP-based dynamic 3D eye reconstruction toward future high-precision eye tracking in immersive environments.

---


### 150. [PAC Learning in Turn-Based Stochastic Games with Reachability Objectives: A Decentralized Private Approach via Expected Conditional Distance](https://arxiv.org/abs/2607.14877)

**<font color=#1a73e8>作者：</font>** Ali Asadi, Krishnendu Chatterjee, Pavol Kebis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reachability is the most fundamental logical objective, yet it is notoriously difficult to learn in reinforcement learning settings: even for Markov decision processes, PAC learning of reachability is impossible without additional assumptions. This difficulty also holds in turn-based stochastic games (TBSGs), where two adversarial players interact on a finite state space. In this work, we consider turn-based stochastic games with reachability objectives. For such settings, adversarial learning, in which players are adversarial even in the learning phase, is impossible. Therefore, the goal is to consider learning, in which both players learn the unknown model together. In this spirit, previous literature on PAC learning in TBSGs considers (a)~public information shared by both players; and (b)~centralized learning, which means that players share the same learning algorithm. In this work, our contribution is two-fold. First, we relax these strong assumptions and ensure learning: (i)~with private information not shared with the other player; and (ii)~decentralized learning where the players do not share the same learning algorithm. To the best of our knowledge, this work is the first positive result for decentralized and private information learning of TBSGs with reachability objectives. Second, we introduce a game-theoretic generalization of the Expected Conditional Distance (ECD) parameter, which measures the expected length of reaching the target set. We establish a polynomial-sample complexity bound with respect to the number of states, actions, ECD parameter, and inverses of error tolerance and failure probability.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-221](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
