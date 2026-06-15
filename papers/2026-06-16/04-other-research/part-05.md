# 📦 其他研究 | 2026年06月16日

> 本类共 **211** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-211**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-211**

---

### 201. [Optimal Hidden-Target Learning for Online Inventory Optimization on General Convex Sets](https://arxiv.org/abs/2606.14679)

**<font color=#1a73e8>作者：</font>** Anthony Pineci, Yunzong Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online inventory optimization (OIO) is online convex optimization with physical memory: inventory carryover makes the feasible action set depend on the past. A natural principle, used in stochastic inventory learning and recently in OIO under a single linear capacity constraint, is to maintain a hidden target chosen by an online learner and implement its projection onto the currently feasible order-up-to set. We prove that this simple principle is optimal for OIO on arbitrary bounded convex capacity sets. With online gradient descent as the base learner, the method improves the best known regret guarantee for OIO on general convex sets from inverse to inverse-square-root dependence on the common-demand probability, and we prove a matching lower bound. The same principle gives the first polylogarithmic regret guarantee for strongly convex losses and the first dynamic regret guarantee adapting to Euclidean path variation on general convex capacity sets.
The analysis introduces a norm alignment principle: the right state variable is the distance from the hidden target to the feasible set, measured in the same norm as the projection. Under norm alignment, this distance evolves pathwise as a scalar queue, with target movement as arrival and common demand as service. This reduction to one-dimensional queue control resolves the state dependence and extends the guarantees to general convex capacity sets, beyond the reach of prior productwise approaches. Experiments on synthetic and real-world inventory data corroborate the theory.

---


### 202. [HumP-KD: A Hybrid Uncertainty-Aware Multi-Stage Progressive Knowledge Distillation Framework for Efficient Fire Classification](https://arxiv.org/abs/2606.14684)

**<font color=#1a73e8>作者：</font>** Mohammed Arif Mainuddin, Najifa Tabassum, Omar Ibne Shahid 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time fire classification systems require models that are simultaneously accurate, computationally efficient, and deployable on resource-constrained hardware. This work proposes \textbf{HumP-KD}, a Hybrid Uncertainty-aware Multi-stage Progressive Knowledge Distillation framework for efficient fire classification. Two datasets, FlameVision and Dataset-II, containing 8,600 and 31,309 images, are used. Various CNN and transformer baselines are applied under standard preprocessing, online augmentation, Gaussian noise and motion blur robustness conditions. The proposed HumP-KD model distills knowledge from two frozen heterogeneous transformer teachers, Swin-Tiny and ViT-Base, along with their Meta-MLP ensemble, into a lightweight MobileViT-S student via three tightly integrated components. Hierarchical Progressive Knowledge Distillation employs a Hierarchical Feature Builder. It generates a fused spatial attention mask to guide distillation toward discriminative regions selectively. Multi-Stage Knowledge Distillation progressively activates three distillation stages across training. On Dataset-II, HumP-KD achieves a mean F1 score of $0.9876 \pm 0.0063$ across 10 independent trials, significantly outperforming the MobileViT-S baseline trained without distillation ($0.9537 \pm 0.0351$), with statistical significance confirmed by both independent t-test ($p = 0.0195$) and Wilcoxon signed-rank test ($W = 1$, $p = 0.0039$). The proposed method also demonstrates strong generalization across datasets and robustness under degraded visual conditions. The student model retains only 4.94M parameters and 19.01Mb model size, representing a $5.7\times$ parameter reduction over Swin-Tiny and a $17.5\times$ reduction over ViT-Base, while achieving 37.72 CPU FPS, making it suitable for real-time deployment.

---


### 203. [CottonLeafVision: An Explainable and Robust Deep Learning Framework for Cotton Leaf Disease Classification](https://arxiv.org/abs/2606.14686)

**<font color=#1a73e8>作者：</font>** Rafi Ahamed, Md. Abir Rahman, Tasnia Tarannum Roza 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Globally, cotton is a highly economically beneficial crop, as the textile industry heavily depends on it. So, the precise identification and detection of cotton leaf disease is crucial for economic stability. The development goal of "CottonLeafVision" is to accurately classify and detect cotton leaf disease. With this goal, we have evaluated multiple pretrained Deep Convolutional Neural Networks, including DenseNet201, InceptionV3, and VGG19 on a publicly available cotton leaf disease image dataset. This image dataset includes seven classes, six disease classes, and one healthy class, collected under various field conditions reflecting real-world challenges. Among these pretrained models, with DenseNet201, we have achieved the highest classification accuracy of 98%. To enhance the model reliability and interpretability, we have implemented different techniques and methods such as Gradient-weighted Class Activation Mapping (Grad-CAM), occlusion sensitivity analysis and adversarial training to increase the noise resistance of the model. Finally, we have developed a prototype in order to utilize the model's capabilities on real life agriculture. This paper shows the deep learning model's capabilities to classify the disease in real-life cotton disease management situations.

---


### 204. [Flood and Harvest: The Provable Necessity of Trivia for Generating Valuable Mathematics via the Lens of Language Generation in the Limit](https://arxiv.org/abs/2606.14688)

**<font color=#1a73e8>作者：</font>** Xiaoyu Li, Andi Han, Dai Shi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI systems coupled to proof assistants now generate formal mathematics at scale, and the gap between what a checker can verify and what a mathematician would value has become the binding constraint. We model the generation of valuable mathematics as nested language generation in the limit: a verifiable formal language $F$, accessed through a membership oracle (the proof checker), contains an unknown valuable language $H \in \mathcal{H}$ revealed only through an adversarial enumeration of a core $C \subseteq H$ of exact density $\alpha$ (the literature). Every output is valuable ($\in H$), trivial ($\in F \setminus H$), or a hallucination ($\notin F$). We settle four questions. First, the verifier is not taste: the collections admitting generation with breadth are exactly those of the oracle-free model, characterized fiber-wise by Angluin's condition. Second, the verifier does buy sound coverage, covering all unseen valuable statements while asserting only valid ones: possible with it, impossible without it; it relocates unavoidable errors from false to trivial. Third, and centrally, a sharp dichotomy on the tight family: generators emitting finitely many trivia achieve optimal coverage $\alpha/2$, while any infinite trivia allowance, even at vanishing rate, jumps the optimum to $1-\alpha/2$ (both tight, for cores presented as the candidate intersection), and one generator attains both ends. The transition is in trivia count, not rate; the gap $1-\alpha$ is the unrecorded mass. Fourth, both regimes instantiate in a compression model of mathematics. A perfect verifier cannot substitute for taste: the unbounded stream of correct-but-worthless statements is not an engineering accident but a provable necessity, since covering unrecorded valuable mathematics requires an infinite, but asymptotically negligible, stream of certified trivia.

---


### 205. [A Complexity Measure for Active Learning in Multi-group Mean Estimation](https://arxiv.org/abs/2606.14690)

**<font color=#1a73e8>作者：</font>** Abdellah Aznag, Rachel Cummings, Adam N. Elmachtoub  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study a \emph{max-risk} objective for active learning in a multi-group mean estimation $d$-armed bandits: a learner adaptively allocates a budget of $T$ samples across $d$ groups to minimize the worst-case uncertainty index $\max_{k\in[d]}\sigma_k^2/n_k$, where $\sigma_k$ is the standard deviation of the distribution of arm $d$, and $n_k$ is the number of times arm $d$ is sampled. We develop a local minimax framework and prove the first general lower bound for this objective, valid for any finite-variance hypothesis class. The bound separates difficulty into three orthogonal factors: a \emph{budget} term, a \emph{heteroscedasticity} index measuring how unevenly the uncertainty is spread across arms, and a model-dependent complexity measure, the \emph{Variance Local Curvature} ($\mathrm{VLC}$), which captures how much information a local change of variance creates inside the hypothesis class. For smooth classes, the $\mathrm{VLC}$ is a reparametrization of a variance--Fisher information, with closed-form values for common families. Benchmarking against the strongest available upper bound shows near-optimality up to logarithmic factors in broad regimes, and pinpoints a systematic gap in highly heterogeneous instances. Our proof introduces two key ingredients: a loss-induced $\ell_1$ geometry on the decision space, and a representation-based instance generator that reduces hard-instance construction to an explicit random matrix calculation.

---


### 206. [Learning Coordinated Preference for Multi-Objective Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2606.14693)

**<font color=#1a73e8>作者：</font>** Pengxin Wang, Lihao Guo, Yi Xie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Cooperative multi-objective multi-agent reinforcement learning (MOMARL) models team decision making under multiple, potentially conflicting objectives. In this setting, conflicts arise not only across objectives but also across agents with different observations, roles, and contributions. We propose Preference Coordinated Multi-agent Policy Optimization (PCMA), which learns coordinated agent-specific preferences to enable complementary trade-offs among agents. Theoretically, we formulate cooperative MOMARL as a team-optimal game and show that, under suitable conditions, preference diversity can induce team improvement through a first-order improvement decomposition. Experiments on multiple cooperative MOMA environments and a practical traffic-control scenario show that PCMA improves both performance and trade-off coordination.

---


### 207. [AdaSR: Adaptive Streaming Reasoning with Hierarchical Relative Policy Optimization](https://arxiv.org/abs/2606.14694)

**<font color=#1a73e8>作者：</font>** Junlong Tong, Wenqi Xu, Yingqi Fan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large reasoning models typically follow a read-then-think paradigm: they observe the complete input, reason over a static context, and then produce the answer. Yet many real-world scenarios are inherently dynamic, such as audio and video stream, where information arrives as a continuous stream and models must reason, update, and respond under partial observations. Recent streaming reasoning methods allow models to think while reading, but they largely rely on supervised imitation of pre-constructed trajectories, which limits their flexibility. In this paper, we propose AdaSR, an adaptive streaming reasoning framework that enables models to reason during input streaming and perform final deliberation once the stream is complete, learning when to think, and how much computation to allocate across different stages. To optimize this hierarchical reasoning process, we introduce Hierarchical Relative Policy Optimization (HRPO), which decomposes policy optimization into streaming reasoning and deep reasoning phases, providing more fine-grained advantage assignment instead of uniformly distributing a single sequence-level advantage over all tokens. HRPO integrates format, accuracy, and adaptive thinking rewards to enforce valid reasoning protocols, preserve final task performance, and encourage latency-aware computation allocation. Experiments show that AdaSR achieves a better balance among reasoning accuracy, computational efficiency, and streaming latency compared with supervised fine-tuning baseline. We release our code at this https URL.

---


### 208. [Persona-Pruner: Sculpting Lightweight Models for Role-Playing](https://arxiv.org/abs/2606.14695)

**<font color=#1a73e8>作者：</font>** Jinsu Kim, Jihoon Tack, Noah Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language Models (LMs) have shown remarkable potential as role-playing chatbots, delivering consistent, stylized interactions when given a specification of a character or user persona. However, applying these capabilities to real-world applications (e.g., ecosystems with numerous NPCs interacting simultaneously) exposes a critical inefficiency due to the excessive computational cost. In this paper, we question the necessity of dedicating a full, generalist model to a single persona, hypothesizing that a specific character identity relies on only a fraction of the model's total capacity. We observe that naively pruning LMs often severely degrades the role-playing performance for a specific persona; it does not distinguish between redundant knowledge and essential character traits. We propose Persona-Pruner, a framework that sculpts a lightweight role-playing model by isolating persona-specific sub-networks from a single description. Our experiments consistently show that Persona-Pruner preserves role-playing performance substantially more effectively than existing state-of-the-art LLM pruning techniques, reducing the performance drop from the dense model by up to 93.8% over the strongest baseline on RoleBench in LLM-as-a-judge score, while still maintaining general LLM capabilities. Code is available at this https URL.

---


### 209. [Instruct-Particulate: Scaling Feed-Forward 3D Object Articulation with Kinematic Control](https://arxiv.org/abs/2606.14699)

**<font color=#1a73e8>作者：</font>** Ruining Li, Yuxin Yao, Matt Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing articulated 3D objects is important for animation, gaming, and robotic simulations. Recent neural networks can estimate the articulated structure of 3D objects, but their generalization remains limited by the scarcity of annotated data for this task. To address this gap, we introduce Instruct-Particulate, a model that takes a 3D mesh together with a target kinematic specification, including part descriptions, connectivity, joint types, and optional point prompts, and predicts the corresponding kinematic part segmentation and joint motion parameters. The kinematic specification disambiguates the task and allows the model to target annotations of different granularity, thereby making it possible to use more abundant heterogeneous training data. At test time, the kinematic specification can be obtained automatically from large-scale vision-language models, so the model can be applied to any input mesh. To train our model at scale, we construct a heterogeneous dataset of more than 150,000 articulated 3D objects, extending existing publicly available collections with data obtained by partially labelling other 3D models (monolithic or already decomposed into parts) with kinematic labels by means of vision-language models. Experiments show that our model generalizes better across categories and to AI-generated meshes, enabling articulated asset reconstruction from real-world images via image-to-3D models.

---


### 210. [RATS! Patches Talk Through Registers: Emergent Parts in Register Attention Transformers](https://arxiv.org/abs/2606.14701)

**<font color=#1a73e8>作者：</font>** Timing Yang, Predrag Neskovic, Jansen Seheult 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When humans see a bird, they recognize far more than just "bird" -- they see a head, wings, and talons, a structured assembly of reusable parts that can be identified across every bird they have ever seen. We ask whether a self-supervised visual model can discover the same compositional structure on its own. To this end, we propose RATS (Register Attention Transformers), which decomposes the classification token into N learnable register tokens that route patch information through an L->N->N->L bottleneck via a three-step compress-communicate-broadcast attention. The N registers are partitioned across the H attention heads, so that registers assigned to different heads do not interact with each other. Without auxiliary losses or part annotations, each register spontaneously specializes into a proto-semantic region whose emerging structure resembles object parts. RATS surpasses all baselines by +12 mIoU on average across five segmentation benchmarks, with consistent gains on ADE20K (+1.11 mIoU) and COCO (+0.2 AP^m). Its register dictionary further exhibits part-level consistency and semantic proximity across related categories. Our results suggest that RATS may provide a useful architectural prior for structured and interpretable visual representation learning.

---


### 211. [Gaze Heads: How VLMs Look at What They Describe](https://arxiv.org/abs/2606.14703)

**<font color=#1a73e8>作者：</font>** Rohit Gandikota, David Bau  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> How a vision-language model internally solves the task of describing an image is far from obvious. We find that the model develops a specific mechanism for this: a small set of attention heads in its language-model backbone, which we call gaze heads, whose attention tracks the image region the model is currently describing. We find them with a simple correlation score from a few forward passes, using comic strips as a controlled testbed where narrative order is laid out spatially. These gaze heads do not just track the image tokens being described: redirecting their attention to a chosen region forces the VLM to describe that region instead. A single attention-mask intervention on the top-100 gaze heads, fewer than 9% of all heads, steers the model's answer to any chosen comic panel at 83.1% accuracy, while the same intervention on random heads fails to redirect the answer, and intervening on all heads destroys generation. The same lever also extends to continuous control: switching the gaze target mid-generation makes the model wrap up its current panel description and move to the new one within a few tokens. Beyond comics, the same intervention redirects answers to chosen regions in natural COCO images. The mechanism further recurs across model sizes from 2B to 32B parameters and across other VLM architectures, although some frozen-encoder families show no comparable head set. More broadly, this shows that targeted edits identified through mechanistic analysis can serve as practical inference-time levers for steering multimodal model behavior, without any retraining. Our code, interactive demo, and datasets are available at this https URL

---


> [!TIP]
> 当前位于：**201-211**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-211**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
