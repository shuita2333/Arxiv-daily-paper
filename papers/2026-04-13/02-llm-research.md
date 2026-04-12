# 🧠 大模型相关研究 | 2026年04月13日

> 本类共 **172** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

---

### 1. [BLEG: LLM Functions as Powerful fMRI Graph-Enhancer for Brain Network Analysis](https://arxiv.org/abs/2604.07361)

**<font color=#1a73e8>作者：</font>** Rui Dong, Zitong Wang, Jiaxing Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) have been widely used in diverse brain network analysis tasks based on preprocessed functional magnetic resonance imaging (fMRI) data. However, their performances are constrained due to high feature sparsity and inherent limitations of domain knowledge within uni-modal neurographs. Meanwhile, large language models (LLMs) have demonstrated powerful representation capabilities. Combining LLMs with GNNs presents a promising direction for brain network analysis. While LLMs and MLLMs have emerged in neuroscience, integration of LLMs with graph-based data remains unexplored. In this work, we deal with these issues by incorporating LLM's powerful representation and generalization capabilities. Considering great cost for directly tuning LLMs, we instead function LLM as enhancer to boost GNN's performance on downstream tasks. Our method, namely BLEG, can be divided into three stages. We firstly prompt LLM to get augmented texts for fMRI graph data, then we design a LLM-LM instruction tuning method to get enhanced textual representations at a relatively lower cost. GNN is trained together for coarsened alignment. Finally we finetune an adapter after GNN for given downstream tasks. Alignment loss between LM and GNN logits is designed to further enhance GNN's representation. Extensive experiments on different datasets confirmed BLEG's superiority.

---


### 2. [LLM-Generated Fault Scenarios for Evaluating Perception-Driven Lane Following in Autonomous Edge Systems](https://arxiv.org/abs/2604.07362)

**<font color=#1a73e8>作者：</font>** Faezeh Pasandideh, Achim Rettberg  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying autonomous vision systems on edge devices faces a critical challenge: resource constraints prevent real-time and predictable execution of comprehensive safety tests. Existing validation methods depend on static datasets or manual fault injection, failing to capture the diverse environmental hazards encountered in real-world deployment. To address this, we introduce a decoupled offline-online fault injection framework. This architecture separates the validation process into two distinct phases: a computationally intensive Offline Phase and a lightweight Online Phase. In the offline phase, we employ Large Language Models (LLMs) to semantically generate structured fault scenarios and Latent Diffusion Models (LDMs) to synthesize high-fidelity sensor degradations. These complex fault dynamics are distilled into a pre-computed lookup table, enabling the edge device to perform real-time fault-aware inference without running heavy AI models locally. We extensively validated this framework on a ResNet18 lane-following model across 460 fault scenarios. Results show that while the model achieves a baseline R^2 of approximately 0.85 on clean data, our generated faults expose significant robustness degradation, with RMSE increasing by up to 99% and within-0.10 localization accuracy dropping to as low as 31.0% under fog conditions, demonstrating the inadequacy of normal-data evaluation for real-world edge AI deployment.

---


### 3. [Benchmark Shadows: Data Alignment, Parameter Footprints, and Generalization in Large Language Models](https://arxiv.org/abs/2604.07363)

**<font color=#1a73e8>作者：</font>** Hongjian Zou, Yidan Wang, Qi Ding 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models often achieve strong benchmark gains without corresponding improvements in broader capability. We hypothesize that this discrepancy arises from differences in training regimes induced by data distribution. To investigate this, we design controlled data interventions that isolate distributional effects under fixed training settings. We find that benchmark-aligned data improves narrow evaluation metrics while limiting broader representational development, whereas coverage-expanding data leads to more distributed parameter adaptation and better generalization. We further introduce parameter-space diagnostics based on spectral and rank analyses, which reveal distinct structural signatures of these regimes. Similar patterns are observed across diverse open-source model families, including multimodal models as a key case study, suggesting that these effects extend beyond controlled settings. A case study on prompt repetition shows that not all data artifacts induce regime shifts. These results indicate that benchmark performance alone is insufficient to characterize model capability, and highlight the importance of data distribution in shaping learning dynamics.

---


### 4. [The Role of Emotional Stimuli and Intensity in Shaping Large Language Model Behavior](https://arxiv.org/abs/2604.07369)

**<font color=#1a73e8>作者：</font>** Ameen Patel, Felix Lee, Kyle Liang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Emotional prompting - the use of specific emotional diction in prompt engineering - has shown increasing promise in improving large language model (LLM) performance, truthfulness, and responsibility. However these studies have been limited to single types of positive emotional stimuli and have not considered varying degrees of emotion intensity in their analyses. In this paper, we explore the effects of four distinct emotions - joy, encouragement, anger, and insecurity - in emotional prompting and evaluate them on accuracy, sycophancy, and toxicity. We develop a prompt-generation pipeline with GPT-4o mini to create a suite of LLM and human-generated prompts with varying intensities across the four emotions. Then, we compile a "Gold Dataset" of prompts where human and model labels align. Our empirical evaluation on LLM behavior suggests that positive emotional stimuli lead to more accurate and less toxic results, but also increase sycophantic behavior.

---


### 5. [Latent Structure of Affective Representations in Large Language Models](https://arxiv.org/abs/2604.07382)

**<font color=#1a73e8>作者：</font>** Benjamin J. Choi, Melanie Weber  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The geometric structure of latent representations in large language models (LLMs) is an active area of research, driven in part by its implications for model transparency and AI safety. Existing literature has focused mainly on general geometric and topological properties of the learnt representations, but due to a lack of ground-truth latent geometry, validating the findings of such approaches is challenging. Emotion processing provides an intriguing testbed for probing representational geometry, as emotions exhibit both categorical organization and continuous affective dimensions, which are well-established in the psychology literature. Moreover, understanding such representations carries safety relevance. In this work, we investigate the latent structure of affective representations in LLMs using geometric data analysis tools. We present three main findings. First, we show that LLMs learn coherent latent representations of affective emotions that align with widely used valence--arousal models from psychology. Second, we find that these representations exhibit nonlinear geometric structure that can nonetheless be well-approximated linearly, providing empirical support for the linear representation hypothesis commonly assumed in model transparency methods. Third, we demonstrate that the learned latent representation space can be leveraged to quantify uncertainty in emotion processing tasks. Our findings suggest that LLMs acquire affective representations with geometric structure paralleling established models of human emotion, with practical implications for model interpretability and safety.

---


### 6. [Playing DOOM with 1.3M Parameters: Specialized Small Models vs Large Language Models for Real-Time Game Control](https://arxiv.org/abs/2604.07385)

**<font color=#1a73e8>作者：</font>** David Golchinfar, Daryoush Vaziri, Alexander Marquardt  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present SauerkrautLM-Doom-MultiVec, a 1.3 million parameter model that plays the classic first-person shooter DOOM in real time, outperforming large language models up to 92,000x its size, including Nemotron-120B, Qwen3.5-27B, and GPT-4o-mini. Our model combines a ModernBERT encoder with hash embeddings, depth-aware token representations, and an attention pooling classification head to select game actions from ASCII frame representations at 31ms per decision. Trained on just 31,000 human gameplay demonstrations, it achieves 178 frags in 10 episodes (17.8 per episode) in the defend_the_center scenario, more than all tested LLMs combined (13 frags total). All agents receive equivalent input: ASCII frames and depth maps. Despite having 92,000x fewer parameters than Nemotron-120B, our model is the only agent that actively engages enemies rather than purely evading them. These results demonstrate that small, task-specific models trained on domain-appropriate data can decisively outperform general-purpose LLMs at real-time control tasks, at a fraction of the inference cost, with deployment capability on consumer hardware.

---


### 7. [A Graph Foundation Model for Wireless Resource Allocation](https://arxiv.org/abs/2604.07390)

**<font color=#1a73e8>作者：</font>** Yucheng Sheng, Jiacheng Wang, Le Liang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The aggressive densification of modern wireless networks necessitates judicious resource allocation to mitigate severe mutual interference. However, classical iterative algorithms remain computationally prohibitive for real-time applications requiring rapid responsiveness. While recent deep learning-based methods show promise, they typically function as task-specific solvers lacking the flexibility to adapt to different objectives and scenarios without expensive retraining. To address these limitations, we propose a graph foundation model for resource allocation (GFM-RA) based on a pre-training and fine-tuning paradigm to extract unified representations, thereby enabling rapid adaptation to different objectives and scenarios. Specifically, we introduce an interference-aware Transformer architecture with a bias projector that injects interference topologies into global attention mechanisms. Furthermore, we develop a hybrid self-supervised pre-training strategy that synergizes masked edge prediction with negative-free Teacher-Student contrastive learning, enabling the model to capture transferable structural representations from massive unlabeled datasets. Extensive experiments demonstrate that the proposed framework achieves state-of-the-art performance and scales effectively with increased model capacity. Crucially, leveraging its unified representations, the foundation model exhibits exceptional sample efficiency, enabling robust few-shot adaptation to diverse and unsupervised downstream objectives in out-of-distribution (OOD) scenarios. These results demonstrate the promise of pre-trained foundation models for adaptable wireless resource allocation and provide a strong foundation for future research on generalizable learning-based wireless optimization.

---


### 8. [Event-Centric World Modeling with Memory-Augmented Retrieval for Embodied Decision-Making](https://arxiv.org/abs/2604.07392)

**<font color=#1a73e8>作者：</font>** Fan Zhaowen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autonomous agents operating in dynamic and safety-critical environments require decision-making frameworks that are both computationally efficient and physically grounded. However, many existing approaches rely on end-to-end learning, which often lacks interpretability and explicit mechanisms for ensuring consistency with physical constraints. In this work, we propose an event-centric world modeling framework with memory-augmented retrieval for embodied decision-making. The framework represents the environment as a structured set of semantic events, which are encoded into a permutation-invariant latent representation. Decision-making is performed via retrieval over a knowledge bank of prior experiences, where each entry associates an event representation with a corresponding maneuver. The final action is computed as a weighted combination of retrieved solutions, providing a transparent link between decision and stored experiences. The proposed design enables structured abstraction of dynamic environments and supports interpretable decision-making through case-based reasoning. In addition, incorporating physics-informed knowledge into the retrieval process encourages the selection of maneuvers that are consistent with observed system dynamics. Experimental evaluation in UAV flight scenarios demonstrates that the framework operates within real-time control constraints while maintaining interpretable and consistent behavior.

---


### 9. [Flux Attention: Context-Aware Hybrid Attention for Efficient LLMs Inference](https://arxiv.org/abs/2604.07394)

**<font color=#1a73e8>作者：</font>** Quantong Qiu, Zhiyi Hong, Yi Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The quadratic computational complexity of standard attention mechanisms presents a severe scalability bottleneck for LLMs in long-context scenarios. While hybrid attention mechanisms combining Full Attention (FA) and Sparse Attention (SA) offer a potential solution, existing methods typically rely on static allocation ratios that fail to accommodate the variable retrieval demands of different tasks. Furthermore, head-level dynamic sparsity often introduces severe computational load imbalance and synchronization long-tails, which hinder hardware acceleration during autoregressive decoding. To bridge this gap, we introduce Flux Attention, a context-aware framework that dynamically optimizes attention computation at the layer level. By integrating a lightweight Layer Router into frozen pretrained LLMs, the proposed method adaptively routes each layer to FA or SA based on the input context. This layer-wise routing preserves high-fidelity information retrieval while ensuring contiguous memory access, translating theoretical computational reductions into practical wall-clock speedups. As a parameter-efficient approach, our framework requires only 12 hours of training on 8$\times$A800 GPUs. Extensive experiments across multiple long-context and mathematical reasoning benchmarks demonstrate that Flux Attention achieves a superior trade-off between performance and inference speed compared with baseline models, with speed improvements of up to $2.8\times$ and $2.0\times$ in the prefill and decode stages.

---


### 10. [FORGE:Fine-grained Multimodal Evaluation for Manufacturing Scenarios](https://arxiv.org/abs/2604.07413)

**<font color=#1a73e8>作者：</font>** Xiangru Jian, Hao Xu, Wei Pang 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The manufacturing sector is increasingly adopting Multimodal Large Language Models (MLLMs) to transition from simple perception to autonomous execution, yet current evaluations fail to reflect the rigorous demands of real-world manufacturing environments. Progress is hindered by data scarcity and a lack of fine-grained domain semantics in existing datasets. To bridge this gap, we introduce FORGE. Wefirst construct a high-quality multimodal dataset that combines real-world 2D images and 3D point clouds, annotated with fine-grained domain semantics (e.g., exact model numbers). We then evaluate 18 state-of-the-art MLLMs across three manufacturing tasks, namely workpiece verification, structural surface inspection, and assembly verification, revealing significant performance gaps. Counter to conventional understanding, the bottleneck analysis shows that visual grounding is not the primary limiting factor. Instead, insufficient domain-specific knowledge is the key bottleneck, setting a clear direction for future research. Beyond evaluation, we show that our structured annotations can serve as an actionable training resource: supervised fine-tuning of a compact 3B-parameter model on our data yields up to 90.8% relative improvement in accuracy on held-out manufacturing scenarios, providing preliminary evidence for a practical pathway toward domain-adapted manufacturing MLLMs. The code and datasets are available at this https URL.

---


### 11. [SPAMoE: Spectrum-Aware Hybrid Operator Framework for Full-Waveform Inversion](https://arxiv.org/abs/2604.07421)

**<font color=#1a73e8>作者：</font>** Zhenyu Wang, Peiyuan Li, Yongxiang Shi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Full-waveform inversion (FWI) is pivotal for reconstructing high-resolution subsurface velocity models but remains computationally intensive and ill-posed. While deep learning approaches promise efficiency, existing Convolutional Neural Networks (CNNs) and single-paradigm Neural Operators (NOs) struggle with one fundamental issue: frequency entanglement of multi-scale geological features. To address this challenge, we propose Spectral-Preserving Adaptive MoE (SPAMoE), a novel spectrum-aware framework for solving inverse problems with complex multi-scale structures. Our approach introduces a Spectral-Preserving DINO Encoder that enforces a lower bound on the high-to-low frequency energy ratio of the encoded representation, mitigating high-frequency collapse and stabilizing subsequent frequency-domain modeling. Furthermore, we design a novel Spectral Decomposition and Routing mechanism that dynamically assigns frequency bands to a Mixture-of-Experts (MoE) ensemble comprising FNO, MNO, and LNO. On the ten OpenFWI sub-datasets, experiments show that SPAMoE reduces the average MAE by 54.1% relative to the best officially reported OpenFWI baseline, thereby establishing a new architectural framework for learning-based full-waveform inversion.

---


### 12. [Multimodal Large Language Models for Multi-Subject In-Context Image Generation](https://arxiv.org/abs/2604.07422)

**<font color=#1a73e8>作者：</font>** Yucheng Zhou, Dubing Chen, Huan Zheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in text-to-image (T2I) generation have enabled visually coherent image synthesis from descriptions, but generating images containing multiple given subjects remains challenging. As the number of reference identities increases, existing methods often suffer from subject missing and semantic drift. To address this problem, we propose MUSIC, the first MLLM specifically designed for \textbf{MU}lti-\textbf{S}ubject \textbf{I}n-\textbf{C}ontext image generation. To overcome the data scarcity, we introduce an automatic and scalable data generation pipeline that eliminates the need for manual annotation. Furthermore, we enhance the model's understanding of multi-subject semantic relationships through a vision chain-of-thought (CoT) mechanism, guiding step-by-step reasoning from subject images to semantics and generation. To mitigate identity entanglement and manage visual complexity, we develop a novel semantics-driven spatial layout planning method and demonstrate its test-time scalability. By incorporating complex subject images during training, we improve the model's capacity for chained reasoning. In addition, we curate MSIC, a new benchmark tailored for multi-subject in-context generation. Experimental results demonstrate that MUSIC significantly surpasses other methods in both multi- and single-subject scenarios.

---


### 13. [GameWorld: Towards Standardized and Verifiable Evaluation of Multimodal Game Agents](https://arxiv.org/abs/2604.07429)

**<font color=#1a73e8>作者：</font>** Mingyu Ouyang, Siyuan Hu, Kevin Qinghong Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Towards an embodied generalist for real-world interaction, Multimodal Large Language Model (MLLM) agents still suffer from challenging latency, sparse feedback, and irreversible mistakes. Video games offer an ideal testbed with rich visual observations and closed-loop interaction, demanding fine-grained perception, long-horizon planning, and precise control. However, systematically evaluating these capabilities is currently hindered by heterogeneous action interfaces and heuristic verification. To this end, we introduce GameWorld, a benchmark designed for standardized and verifiable evaluation of MLLMs as generalist game agents in browser environments. Two game agent interfaces are studied: (i) computer-use agents that directly emit keyboard and mouse controls, and (ii) generalist multimodal agents that act in a semantic action space via deterministic Semantic Action Parsing. GameWorld contains 34 diverse games and 170 tasks, each paired with state-verifiable metrics for outcome-based evaluation. The results across 18 model-interface pairs suggest that even the best performing agent is far from achieving human capabilities on video games. Extensive experiments of repeated full-benchmark reruns demonstrate the robustness of the benchmark, while further studies on real-time interaction, context-memory sensitivity, and action validity expose more challenges ahead for game agents. Together, by offering a standardized, verifiable, and reproducible evaluation framework, GameWorld lays a robust foundation for advancing research on multimodal game agents and beyond. The project page is at this https URL.

---


### 14. [HY-Embodied-0.5: Embodied Foundation Models for Real-World Agents](https://arxiv.org/abs/2604.07430)

**<font color=#1a73e8>作者：</font>** Tencent Robotics X, HY Vision Team, Xumin Yu 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce HY-Embodied-0.5, a family of foundation models specifically designed for real-world embodied agents. To bridge the gap between general Vision-Language Models (VLMs) and the demands of embodied agents, our models are developed to enhance the core capabilities required by embodied intelligence: spatial and temporal visual perception, alongside advanced embodied reasoning for prediction, interaction, and planning. The HY-Embodied-0.5 suite comprises two primary variants: an efficient model with 2B activated parameters designed for edge deployment, and a powerful model with 32B activated parameters targeted for complex reasoning. To support the fine-grained visual perception essential for embodied tasks, we adopt a Mixture-of-Transformers (MoT) architecture to enable modality-specific computing. By incorporating latent tokens, this design effectively enhances the perceptual representation of the models. To improve reasoning capabilities, we introduce an iterative, self-evolving post-training paradigm. Furthermore, we employ on-policy distillation to transfer the advanced capabilities of the large model to the smaller variant, thereby maximizing the performance potential of the compact model. Extensive evaluations across 22 benchmarks, spanning visual perception, spatial reasoning, and embodied understanding, demonstrate the effectiveness of our approach. Our MoT-2B model outperforms similarly sized state-of-the-art models on 16 benchmarks, while the 32B variant achieves performance comparable to frontier models such as Gemini 3.0 Pro. In downstream robot control experiments, we leverage our robust VLM foundation to train an effective Vision-Language-Action (VLA) model, achieving compelling results in real-world physical evaluations. Code and models are open-sourced at this https URL.

---


### 15. [Cross-Tokenizer LLM Distillation through a Byte-Level Interface](https://arxiv.org/abs/2604.07466)

**<font color=#1a73e8>作者：</font>** Avyav Kumar Singh, Yen-Chen Wu, Alexandru Cioba 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cross-tokenizer distillation (CTD), the transfer of knowledge from a teacher to a student language model when the two use different tokenizers, remains a largely unsolved problem. Existing approaches rely on heuristic strategies to align mismatched vocabularies, introducing considerable complexity. In this paper, we propose a simple but effective baseline called Byte-Level Distillation (BLD) which enables CTD by operating at a common interface across tokenizers: the byte level. In more detail, we convert the teacher's output distribution to byte-level probabilities, attach a lightweight byte-level decoder head to the student, and distill through this shared byte-level interface. Despite its simplicity, BLD performs competitively with--and on several benchmarks surpasses--significantly more sophisticated CTD methods, across a range of distillation tasks with models from 1B to 8B parameters. Our results suggest that the byte level is a natural common ground for cross-tokenizer knowledge transfer, while also highlighting that consistent improvements across all tasks and benchmarks remain elusive, underscoring that CTD is still an open problem.

---


### 16. [M-ArtAgent: Evidence-Based Multimodal Agent for Implicit Art Influence Discovery](https://arxiv.org/abs/2604.07468)

**<font color=#1a73e8>作者：</font>** Hanyi Liu, Zhonghao Jiu, Minghao Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Implicit artistic influence, although visually plausible, is often undocumented and thus poses a historically constrained attribution problem: resemblance is necessary but not sufficient evidence. Most prior systems reduce influence discovery to embedding similarity or label-driven graph completion, while recent multimodal large language models (LLMs) remain vulnerable to temporal inconsistency and unverified attributions. This paper introduces M-ArtAgent, an evidence-based multimodal agent that reframes implicit influence discovery as probabilistic adjudication. It follows a four-phase protocol consisting of Investigation, Corroboration, Falsification, and Verdict governed by a Reasoning and Acting (ReAct)-style controller that assembles verifiable evidence chains from images and biographies, enforces art-historical axioms, and subjects each hypothesis to adversarial falsification via a prompt-isolated critic. Two theory-grounded operators, StyleComparator for Wolfflin formal analysis and ConceptRetriever for ICONCLASS-based iconographic grounding, ensure that intermediate claims are formally auditable. On the balanced WikiArt Influence Benchmark-100 (WIB-100) of 100 artists and 2,000 directed pairs, M-ArtAgent achieves 83.7% positive-class F1, 0.666 Matthews correlation coefficient (MCC), and 0.910 area under the receiver operating characteristic curve (ROC-AUC), with leakage-control and robustness checks confirming that the gains persist when explicit influence phrases are masked. By coupling multimodal perception with domain-constrained falsification, M-ArtAgent demonstrates that implicit influence analysis benefits from historically grounded adjudication rather than pattern matching alone.

---


### 17. [To Layer or Not to Layer? Evaluating the Effects and Mechanisms of LLM-Generated Feedback on learning performance](https://arxiv.org/abs/2604.07469)

**<font color=#1a73e8>作者：</font>** Jie Cao, Chloe Qianhui Zhao, Christian Schunn 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Feedback is vital for learning, yet its effectiveness depends not only on its content but also on how it engages students in the learning process. Large Language Models (LLMs) offer novel opportunities to efficiently generate rich, formative feedback, ranging from direct explanations to incrementally layered scaffolding designed to foster learner autonomy. Despite these affordances, it remains unclear whether layered feedback (which sequences encouragement and prompts prior to revealing the correct answer) actually improves engagement and learning outcomes. To address this, we randomly assigned 199 participants to receive either layered or non-layered LLM-generated feedback. We assessed its impact on learning performance, behavioral and cognitive engagement, and affective perceptions, to determine how these factors mediate learning performance. Results indicate that layered feedback elicited slightly higher behavioral engagement and, as anticipated, was perceived as more encouraging and supportive of independence. However, it concurrently induced greater mental effort. Mediation analyses revealed a positive affective pathway driven by perceived encouragement, which was counteracted by a negative behavioral pathway linked to the average number of tasks requiring $\geq 3$ submissions; the cognitive pathway (mental effort) was non-significant. Taken together, layered feedback resulted in significantly poorer learning outcomes compared to non-layered feedback. These findings illuminate a critical trade-off: while layered scaffolding enhances engagement and positive perceptions, it can detrimentally impact actual learning performance. This study contributes nuanced insights for the design of automated, LLM-driven feedback systems by integrating outcome, perception, and mechanism-level analyses.

---


### 18. [Fast Heterogeneous Serving: Scalable Mixed-Scale LLM Allocation for SLO-Constrained Inference](https://arxiv.org/abs/2604.07472)

**<font color=#1a73e8>作者：</font>** Jiaming Cheng, Duong Tung Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying large language model (LLM) inference at scale requires jointly selecting base models, provisioning heterogeneous GPUs, configuring parallelism, and distributing workloads under tight latency, accuracy, and budget constraints. Exact mixed-integer linear programming (MILP) approaches guarantee optimality but scale poorly. We propose two constraint-aware heuristics: a Greedy Heuristic (GH) for single-pass allocation, and an Adaptive Greedy Heuristic (AGH) that enhances GH via multi-start construction, relocate-based local search, and GPU consolidation. Three constraint-aware mechanisms -- TP-aware feasibility selection, cost-per-effective-coverage ranking, and TP upgrade -- ensure feasibility under tightly coupled memory, delay, error, and budget constraints. On workloads calibrated with the Azure LLM Inference Trace (2025), both heuristics produce feasible solutions in under one second, with AGH closely approaching optimal cost while achieving over 260x speedup on large-scale instances. Under out-of-sample stress tests with up to 1.5x parameter inflation, AGH maintains controlled SLO violations and stable cost, whereas the exact solver's placement degrades sharply.

---


### 19. [ConsistRM: Improving Generative Reward Models via Consistency-Aware Self-Training](https://arxiv.org/abs/2604.07484)

**<font color=#1a73e8>作者：</font>** Yu Liang, Liangxin Liu, Longzheng Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative reward models (GRMs) have emerged as a promising approach for aligning Large Language Models (LLMs) with human preferences by offering greater representational capacity and flexibility than traditional scalar reward models. However, GRMs face two major challenges: reliance on costly human-annotated data restricts scalability, and self-training approaches often suffer from instability and vulnerability to reward hacking. To address these issues, we propose ConsistRM, a self-training framework that enables effective and stable GRM training without human annotations. ConsistRM incorporates the Consistency-Aware Answer Reward, which produces reliable pseudo-labels with temporal consistency, thereby providing more stable model optimization. Moreover, the Consistency-Aware Critique Reward is introduced to assess semantic consistency across multiple critiques and allocates fine-grained and differentiated rewards. Experiments on five benchmark datasets across four base models demonstrate that ConsistRM outperforms vanilla Reinforcement Fine-Tuning (RFT) by an average of 1.5%. Further analysis shows that ConsistRM enhances output consistency and mitigates position bias caused by input order, highlighting the effectiveness of consistency-aware rewards in improving GRMs.

---


### 20. [CLEAR: Context Augmentation from Contrastive Learning of Experience via Agentic Reflection](https://arxiv.org/abs/2604.07487)

**<font color=#1a73e8>作者：</font>** Linbo Liu, Guande Wu, Han Ding 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents rely on effective model context to obtain task-relevant information for decision-making. Many existing context engineering approaches primarily rely on the context generated from the past experience and retrieval mechanisms that reuse these context. However, retrieved context from past tasks must be adapted by the execution agent to fit new situations, placing additional reasoning burden on the underlying LLM. To address this limitation, we propose a generative context augmentation framework using Contrastive Learning of Experience via Agentic Reflection (CLEAR). CLEAR first employs a reflection agent to perform contrastive analysis over past execution trajectories and summarize useful context for each observed task. These summaries are then used as supervised fine-tuning data to train a context augmentation model (CAM). Then we further optimize CAM using reinforcement learning, where the reward signal is obtained by running the task execution agent. By learning to generate task-specific knowledge rather than retrieve knowledge from the past, CAM produces context that is better tailored to the current task. We conduct comprehensive evaluations on the AppWorld and WebShop benchmarks. Experimental results show that CLEAR consistently outperforms strong baselines. It improves task completion rate from 72.62% to 81.15% on AppWorld test set and averaged reward from 0.68 to 0.74 on a subset of WebShop, compared with baseline agent. Our code is publicly available at this https URL.

---


### 21. [Enabling Intrinsic Reasoning over Dense Geospatial Embeddings with DFR-Gemma](https://arxiv.org/abs/2604.07490)

**<font color=#1a73e8>作者：</font>** Xuechen Zhang, Aviv Slobodkin, Joydeep Paul 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Representation learning for geospatial and spatio-temporal data plays a critical role in enabling general-purpose geospatial intelligence. Recent geospatial foundation models, such as the Population Dynamics Foundation Model (PDFM), encode complex population and mobility dynamics into compact embeddings. However, their integration with Large Language Models (LLMs) remains limited. Existing approaches to LLM integration treat these embeddings as retrieval indices or convert them into textual descriptions for reasoning, introducing redundancy, token inefficiency, and numerical inaccuracies. We propose Direct Feature Reasoning-Gemma (DFR-Gemma), a novel framework that enables LLMs to reason directly over dense geospatial embeddings. DFR aligns high-dimensional embeddings with the latent space of an LLM via a lightweight projector, allowing embeddings to be injected as semantic tokens alongside natural language instructions. This design eliminates the need for intermediate textual representations and enables intrinsic reasoning over spatial features. To evaluate this paradigm, we introduce a multi-task geospatial benchmark that pairs embeddings with diverse question-answer tasks, including feature querying, comparison, and semantic description. Experimental results show that DFR allows LLMs to decode latent spatial patterns and perform accurate zero-shot reasoning across tasks, while significantly improving efficiency compared to text-based baselines. Our results demonstrate that treating embeddings as primary data inputs, provides a more direct, efficient, and scalable approach to multimodal geospatial intelligence.

---


### 22. [ReflectRM: Boosting Generative Reward Models via Self-Reflection within a Unified Judgment Framework](https://arxiv.org/abs/2604.07506)

**<font color=#1a73e8>作者：</font>** Kai Qin, Liangxin Liu, Yu Liang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reward Models (RMs) are critical components in the Reinforcement Learning from Human Feedback (RLHF) pipeline, directly determining the alignment quality of Large Language Models (LLMs). Recently, Generative Reward Models (GRMs) have emerged as a superior paradigm, offering higher interpretability and stronger generalization than traditional scalar RMs. However, existing methods for GRMs focus primarily on outcome-level supervision, neglecting analytical process quality, which constrains their potential. To address this, we propose ReflectRM, a novel GRM that leverages self-reflection to assess analytical quality and enhance preference modeling. ReflectRM is trained under a unified generative framework for joint modeling of response preference and analysis preference. During inference, we use its self-reflection capability to identify the most reliable analysis, from which the final preference prediction is derived. Experiments across four benchmarks show that ReflectRM consistently improves performance, achieving an average accuracy gain of +3.7 on Qwen3-4B. Further experiments confirm that response preference and analysis preference are mutually reinforcing. Notably, ReflectRM substantially mitigates positional bias, yielding +10.2 improvement compared with leading GRMs and establishing itself as a more stable evaluator.

---


### 23. [SYN-DIGITS: A Synthetic Control Framework for Calibrated Digital Twin Simulation](https://arxiv.org/abs/2604.07513)

**<font color=#1a73e8>作者：</font>** Grace Jiarui Fan, Chengpiao Huang, Tianyi Peng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI-based persona simulation -- often referred to as digital twin simulation -- is increasingly used for market research, recommender systems, and social sciences. Despite their flexibility, large language models (LLMs) often exhibit systematic bias and miscalibration relative to real human behavior, limiting their reliability. Inspired by synthetic control methods from causal inference, we propose SYN-DIGITS (SYNthetic Control Framework for Calibrated DIGItal Twin Simulation), a principled and lightweight calibration framework that learns latent structure from digital-twin responses and transfers it to align predictions with human ground truth. SYN-DIGITS operates as a post-processing layer on top of any LLM-based simulator and thus is model-agnostic. We develop a latent factor model that formalizes when and why calibration succeeds through latent space alignment conditions, and we systematically evaluate ten calibration methods across thirteen persona constructions, three LLMs, and two datasets. SYN-DIGITS supports both individual-level and distributional simulation for previously unseen questions and unobserved populations, with provable error guarantees. Experiments show that SYN-DIGITS achieves up to 50% relative improvements in individual-level correlation and 50--90% relative reductions in distributional discrepancy compared to uncalibrated baselines.

---


### 24. [Agentic Copyright, Data Scraping & AI Governance: Toward a Coasean Bargain in the Era of Artificial Intelligence](https://arxiv.org/abs/2604.07546)

**<font color=#1a73e8>作者：</font>** Paulius Jurcys, Mark Fenwick  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper examines how the rapid deployment of multi-agentic AI systems is reshaping the foundations of copyright law and creative markets. It argues that existing copyright frameworks are ill-equipped to govern AI agent-mediated interactions that occur at scale, speed, and with limited human oversight. The paper introduces the concept of agentic copyright, a model in which AI agents act on behalf of creators and users to negotiate access, attribution, and compensation for copyrighted works. While multi-agent ecosystems promise efficiency gains and reduced transaction costs, they also generate novel market failures, including miscoordination, conflict, and collusion among autonomous agents. To address these market failures, the paper develops a supervised multi-agent governance framework that integrates legal rules and principles, technical protocols, and institutional oversight. This framework emphasizes ex ante and ex post coordination mechanisms capable of correcting agentic market failures before they crystallize into systemic harm. By embedding normative constraints and monitoring functions into multi-agent architectures, supervised governance aims to align agent behavior with the underlying values of copyright law. The paper concludes that AI should be understood not only as a source of disruption, but also as a governance tool capable of restoring market-based ordering in creative industries. Properly designed, agentic copyright offers a path toward scalable, fair, and legally meaningful copyright markets in the age of AI.

---


### 25. [EMSDialog: Synthetic Multi-person Emergency Medical Service Dialogue Generation from Electronic Patient Care Reports via Multi-LLM Agents](https://arxiv.org/abs/2604.07549)

**<font color=#1a73e8>作者：</font>** Xueren Ge, Sahil Murtaza, Anthony Cortez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversational diagnosis prediction requires models to track evolving evidence in streaming clinical conversations and decide when to commit to a diagnosis. Existing medical dialogue corpora are largely dyadic or lack the multi-party workflow and annotations needed for this setting. We introduce an ePCR-grounded, topic-flow-based multi-agent generation pipeline that iteratively plans, generates, and self-refines dialogues with rule-based factual and topic flow checks. The pipeline yields EMSDialog, a dataset of 4,414 synthetic multi-speaker EMS conversations based on a real-world ePCR dataset, annotated with 43 diagnoses, speaker roles, and turn-level topics. Human and LLM evaluations confirm high quality and realism of EMSDialog using both utterance- and conversation-level metrics. Results show that EMSDialog-augmented training improves accuracy, timeliness, and stability of EMS conversational diagnosis prediction.

---


### 26. [TR-EduVSum: A Turkish-Focused Dataset and Consensus Framework for Educational Video Summarization](https://arxiv.org/abs/2604.07553)

**<font color=#1a73e8>作者：</font>** Figen Eğin, Aytuğ Onan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study presents a framework for generating the gold-standard summary fully automatically and reproducibly based on multiple human summaries of Turkish educational videos. Within the scope of the study, a new dataset called TR-EduVSum was created, encompassing 82 Turkish course videos in the field of "Data Structures and Algorithms" and containing a total of 3281 independent human summaries. Inspired by existing pyramid-based evaluation approaches, the AutoMUP (Automatic Meaning Unit Pyramid) method is proposed, which extracts consensus-based content from multiple human summaries. AutoMUP clusters the meaning units extracted from human summaries using embedding, statistically models inter-participant agreement, and generates graded summaries based on consensus weight. In this framework, the gold summary corresponds to the highest-consensus AutoMUP configuration, constructed from the most frequently supported meaning units across human summaries. Experimental results show that AutoMUP summaries exhibit high semantic overlap with robust LLM (Large Language Model) summaries such as Flash 2.5 and GPT-5.1. Furthermore, ablation studies clearly demonstrate the decisive role of consensus weight and clustering in determining summary quality. The proposed approach can be generalized to other Turkic languages at low cost.

---


### 27. [Reasoning-Based Refinement of Unsupervised Text Clusters with LLMs](https://arxiv.org/abs/2604.07562)

**<font color=#1a73e8>作者：</font>** Tunazzina Islam  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Unsupervised methods are widely used to induce latent semantic structure from large text collections, yet their outputs often contain incoherent, redundant, or poorly grounded clusters that are difficult to validate without labeled data. We propose a reasoning-based refinement framework that leverages large language models (LLMs) not as embedding generators, but as semantic judges that validate and restructure the outputs of arbitrary unsupervised clustering this http URL framework introduces three reasoning stages: (i) coherence verification, where LLMs assess whether cluster summaries are supported by their member texts; (ii) redundancy adjudication, where candidate clusters are merged or rejected based on semantic overlap; and (iii) label grounding, where clusters are assigned interpretable labels in a fully unsupervised manner. This design decouples representation learning from structural validation and mitigates common failure modes of embedding-only approaches. We evaluate the framework on real-world social media corpora from two platforms with distinct interaction models, demonstrating consistent improvements in cluster coherence and human-aligned labeling quality over classical topic models and recent representation-based baselines. Human evaluation shows strong agreement with LLM-generated labels, despite the absence of gold-standard annotations. We further conduct robustness analyses under matched temporal and volume conditions to assess cross-platform stability. Beyond empirical gains, our results suggest that LLM-based reasoning can serve as a general mechanism for validating and refining unsupervised semantic structure, enabling more reliable and interpretable analyses of large text collections without supervision.

---


### 28. [Learning is Forgetting: LLM Training As Lossy Compression](https://arxiv.org/abs/2604.07569)

**<font color=#1a73e8>作者：</font>** Henry C. Conklin, Tom Hosking, Tan Yi-Chern 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite the increasing prevalence of large language models (LLMs), we still have a limited understanding of how their representational spaces are structured. This limits our ability to interpret how and what they learn or relate them to learning in humans. We argue LLMs are best seen as an instance of lossy compression, where over training they learn by retaining only information in their training data relevant to their objective(s). We show pre-training results in models that are optimally compressed for next-sequence prediction, approaching the Information Bottleneck bound on compression. Across an array of open weights models, each compresses differently, likely due to differences in the data and training recipes used. However even across different families of LLMs the optimality of a model's compression, and the information present in it, can predict downstream performance on across a wide array of benchmarks, letting us directly link representational structure to actionable insights about model performance. In the general case the work presented here offers a unified Information-Theoretic framing for how these models learn that is deployable at scale.

---


### 29. [CAMO: A Class-Aware Minority-Optimized Ensemble for Robust Language Model Evaluation on Imbalanced Data](https://arxiv.org/abs/2604.07583)

**<font color=#1a73e8>作者：</font>** Mohamed Ehab, Ali Hamdi, Khaled Shaban  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Real-world categorization is severely hampered by class imbalance because traditional ensembles favor majority classes, which lowers minority performance and overall F1-score. We provide a unique ensemble technique for imbalanced problems called CAMO (Class-Aware Minority-Optimized).Through a hierarchical procedure that incorporates vote distributions, confidence calibration, and inter model uncertainty, CAMO dynamically boosts underrepresented classes while preserving and amplifying minority forecasts. We verify CAMO on two highly unbalanced, domain-specific benchmarks: the DIAR-AI/Emotion dataset and the ternary BEA 2025 dataset. We benchmark against seven proven ensemble algorithms using eight different language models (three LLMs and five SLMs) under zero-shot and fine-tuned settings .With refined models, CAMO consistently earns the greatest strict macro F1-score, setting a new benchmark. Its benefit works in concert with model adaptation, showing that the best ensemble choice depends on model properties .This proves that CAMO is a reliable, domain-neutral framework for unbalanced categorization.

---


### 30. [From Papers to Property Tables: A Priority-Based LLM Workflow for Materials Data Extraction](https://arxiv.org/abs/2604.07584)

**<font color=#1a73e8>作者：</font>** Koushik Rameshbabu, Jing Luo, Ali Shargh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific data are widely dispersed across research articles and are often reported inconsistently across text, tables, and figures, making manual data extraction and aggregation slow and error-prone. We present a prompt-driven, hierarchical workflow that uses a large language model (LLM) to automatically extract and reconstruct structured, shot-level shock-physics experimental records by integrating information distributed across text, tables, figures, and physics-based derivations from full-text published research articles, using alloy spall strength as a representative case study. The pipeline targeted 37 experimentally relevant fields per shot and applied a three-level priority strategy: (T1) direct extraction from text/tables, (T2) physics-based derivation using verified governing relations, and (T3) digitization from figures when necessary. Extracted values were normalized to canonical units, tagged by priority for traceability, and validated with physics-based consistency and plausibility checks. Evaluated on a benchmark of 30 published research articles comprising 11,967 evaluated data points, the workflow achieved high overall accuracy, with priority-wise accuracies of 94.93% (T1), 92.04% (T2), and 83.49% (T3), and an overall weighted accuracy of 94.69%. Cross-model testing further indicated strong agreement for text/table and equation-derived fields, with lower agreement for figure-based extraction. Implementation through an API interface demonstrated the scalability of the approach, achieving consistent extraction performance and, in a subset of test cases, matching or exceeding chat-based accuracy. This workflow demonstrates a practical approach for converting unstructured technical literature into traceable, analysis-ready datasets without task-specific fine-tuning, enabling scalable database construction in materials science.

---


### 31. [Bootstrapping Sign Language Annotations with Sign Language Models](https://arxiv.org/abs/2604.07606)

**<font color=#1a73e8>作者：</font>** Colin Lea, Vasileios Baltatzis, Connor Gillis 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI-driven sign language interpretation is limited by a lack of high-quality annotated data. New datasets including ASL STEM Wiki and FLEURS-ASL contain professional interpreters and 100s of hours of data but remain only partially annotated and thus underutilized, in part due to the prohibitive costs of annotating at this scale. In this work, we develop a pseudo-annotation pipeline that takes signed video and English as input and outputs a ranked set of likely annotations, including time intervals, for glosses, fingerspelled words, and sign classifiers. Our pipeline uses sparse predictions from our fingerspelling recognizer and isolated sign recognizer (ISR), along with a K-Shot LLM approach, to estimate these annotations. In service of this pipeline, we establish simple yet effective baseline fingerspelling and ISR models, achieving state-of-the-art on FSBoard (6.7% CER) and on ASL Citizen datasets (74% top-1 accuracy). To validate and provide a gold-standard benchmark, a professional interpreter annotated nearly 500 videos from ASL STEM Wiki with sequence-level gloss labels containing glosses, classifiers, and fingerspelling signs. These human annotations and over 300 hours of pseudo-annotations are being released in supplemental material.

---


### 32. [How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles](https://arxiv.org/abs/2604.07650)

**<font color=#1a73e8>作者：</font>** Chenchen Kuai, Jiwan Jiang, Zihao Zhu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid growth of the large language model (LLM) ecosystem raises a critical question: are seemingly diverse models truly independent? Shared pretraining data, distillation, and alignment pipelines can induce hidden behavioral dependencies, latent entanglement, that undermine multi-model systems such as LLM-as-a-judge pipelines and ensemble verification, which implicitly assume independent signals. In practice, this manifests as correlated reasoning patterns and synchronized failures, where apparent agreement reflects shared error modes rather than independent validation. To address this, we develop a statistical framework for auditing behavioral entanglement among black-box LLMs. Our approach introduces a multi-resolution hierarchy that characterizes the joint failure manifold through two information-theoretic metrics: (i) a Difficulty-Weighted Behavioral Entanglement Index, which amplifies synchronized failures on easy tasks, and (ii) a Cumulative Information Gain (CIG) metric, which captures directional alignment in erroneous responses. Through extensive experiments on 18 LLMs from six model families, we identify widespread behavioral entanglement and analyze its impact on LLM-as-a-judge evaluation. We find that CIG exhibits a statistically significant association with degradation in judge precision, with Spearman coefficient of 0.64 (p < 0.001) for GPT-4o-mini and 0.71 (p < 0.01) for Llama3-based judges, indicating that stronger dependency corresponds to increased over-endorsement bias. Finally, we demonstrate a practical use case of entanglement through de-entangled verifier ensemble reweighting. By adjusting model contributions based on inferred independence, the proposed method mitigates correlated bias and improves verification performance, achieving up to a 4.5% accuracy gain over majority voting.

---


### 33. [Bridging Natural Language and Interactive What-If Interfaces via LLM-Generated Declarative Specification](https://arxiv.org/abs/2604.07652)

**<font color=#1a73e8>作者：</font>** Sneha Gathani, Sirui Zeng, Diya Patel 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> What-if analysis (WIA) is an iterative, multi-step process where users explore and compare hypothetical scenarios by adjusting parameters, applying constraints, and scoping data through interactive interfaces. Current tools fall short of supporting effective interactive WIA: spreadsheet and BI tools require time-consuming and laborious setup, while LLM-based chatbot interfaces are semantically fragile, frequently misinterpret intent, and produce inconsistent results as conversations progress. To address these limitations, we present a two-stage workflow that translates natural language (NL) WIA questions into interactive visual interfaces via an intermediate representation, powered by the Praxa Specification Language (PSL): first, LLMs generate PSL specifications from NL questions capturing analytical intent and logic, enabling validation and repair of erroneous specifications; and second, the specifications are compiled into interactive visual interfaces with parameter controls and linked visualizations. We benchmark this workflow with 405 WIA questions spanning 11 WIA types, 5 datasets, and 3 state-of-the-art LLMs. The results show that across models, half of specifications (52.42%) are generated correctly without intervention. We perform an analysis of the failure cases and derive an error taxonomy spanning non-functional errors (specifications fail to compile) and functional errors (specifications compile but misrepresent intent). Based on the taxonomy, we apply targeted repairs on the failure cases using few-shot prompts and improve the success rate to 80.42%. Finally, we show how undetected functional errors propagate through compilation into plausible but misleading interfaces, demonstrating that the intermediate specification is critical for reliably bridging NL and interactive WIA interface in LLM-powered WIA systems.

---


### 34. [Guardian-as-an-Advisor: Advancing Next-Generation Guardian Models for Trustworthy LLMs](https://arxiv.org/abs/2604.07655)

**<font color=#1a73e8>作者：</font>** Yue Huang, Haomin Zhuang, Jiayi Ye 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hard-gated safety checkers often over-refuse and misalign with a vendor's model spec; prevailing taxonomies also neglect robustness and honesty, yielding safer-on-paper yet less useful systems. This work introduces Guardian-as-an-Advisor (GaaA), a soft-gating pipeline where a guardian predicts a binary risk label plus a concise explanation and prepends this advice to the original query for re-inference, keeping the base model operating under its original spec. To support training and evaluation, GuardSet is constructed, a 208k+ multi-domain dataset unifying harmful and harmless cases with targeted robustness and honesty slices. GuardAdvisor is trained via SFT followed by RL to enforce label-explanation consistency. GuardAdvisor attains competitive detection accuracy while enabling the advisory workflow; when used to augment inputs, responses improve over unaugmented prompts. A latency study shows advisor inference uses below 5% of base-model compute and adds only 2-10% end-to-end overhead under realistic harmful-input rates. Overall, GaaA steers models to comply with the model spec, maintaining safety while reducing over-refusal.

---


### 35. [Efficient and Effective Internal Memory Retrieval for LLM-Based Healthcare Prediction](https://arxiv.org/abs/2604.07659)

**<font color=#1a73e8>作者：</font>** Mingchen Li, Jiatan Huang, Zonghai Yao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) hold significant promise for healthcare, yet their reliability in high-stakes clinical settings is often compromised by hallucinations and a lack of granular medical context. While Retrieval Augmented Generation (RAG) can mitigate these issues, standard supervised pipelines require computationally intensive searches over massive external knowledge bases, leading to high latency that is impractical for time-sensitive care. To address this, we introduce Keys to Knowledge (K2K), a novel framework that replaces external retrieval with internal, key-based knowledge access. By encoding essential clinical information directly into the model's parameter space, K2K enables rapid retrieval from internal key-value memory without inference-time overhead. We further enhance retrieval quality through activation-guided probe construction and cross-attention reranking. Experimental results demonstrate that K2K achieves state-of-the-art performance across four benchmark healthcare outcome prediction datasets.

---


### 36. [SAGE: Sign-Adaptive Gradient for Memory-Efficient LLM Optimization](https://arxiv.org/abs/2604.07663)

**<font color=#1a73e8>作者：</font>** Wooin Lee, Hyun-Tae Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The AdamW optimizer, while standard for LLM pretraining, is a critical memory bottleneck, consuming optimizer states equivalent to twice the model's size. Although light-state optimizers like SinkGD attempt to address this issue, we identify the embedding layer dilemma: these methods fail to handle the sparse, high-variance gradients inherent to embeddings, forcing a hybrid design that reverts to AdamW and partially negates the memory gains. We propose SAGE (Sign Adaptive GradiEnt), a novel optimizer that resolves this dilemma by replacing AdamW in this hybrid structure. SAGE combines a Lion-style update direction with a new, memory-efficient $O(d)$ adaptive scale. This scale acts as a "safe damper," provably bounded by 1.0, which tames high-variance dimensions more effectively than existing methods. This superior stability allows SAGE to achieve better convergence. On Llama models up to 1.3B parameters, our SAGE-based hybrid achieves new state-of-the-art perplexity, outperforming all baselines, including SinkGD hybrid, while significantly reducing optimizer state memory.

---


### 37. [An Imperfect Verifier is Good Enough: Learning with Noisy Rewards](https://arxiv.org/abs/2604.07666)

**<font color=#1a73e8>作者：</font>** Andreas Plesner, Francisco Guzmán, Anish Athalye  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) has become a prominent method for post-training Large Language Models (LLMs). However, verifiers are rarely error-free; even deterministic checks can be inaccurate, and the growing dependence on model-based judges exacerbates the issue. The extent to which RLVR is robust to such noise and the verifier accuracy required for effective training remain unresolved questions. We investigate these questions in the domains of code generation and scientific reasoning by introducing noise into RL training. Noise rates up to 15% yield peak validation accuracy within 2 percentage points of the clean baseline. These findings are consistent across controlled and model-based noise types, three model families (Qwen3, GLM4, Llama 3.1), and model sizes from 4B to 9B. Overall, the results indicate that imperfect verification does not constitute a fundamental barrier to RLVR. Furthermore, our findings suggest that practitioners should prioritize moderate accuracy with high precision over perfect verification.

---


### 38. [From Debate to Decision: Conformal Social Choice for Safe Multi-Agent Deliberation](https://arxiv.org/abs/2604.07667)

**<font color=#1a73e8>作者：</font>** Mengdie Flora Wang, Haochen Xie, Guanghui Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent debate improves LLM reasoning, yet agreement among agents is not evidence of correctness. When agents converge on a wrong answer through social reinforcement, consensus-based stopping commits that error to an automated action with no recourse. We introduce Conformal Social Choice, a post-hoc decision layer that converts debate outputs into calibrated act-versus-escalate decisions. Verbalized probability distributions from heterogeneous agents are aggregated via a linear opinion pool and calibrated with split conformal prediction, yielding prediction sets with a marginal coverage guarantee: the correct answer is included with probability ${\geq}\,1{-}\alpha$, without assumptions on individual model calibration. A hierarchical action policy maps singleton sets to autonomous action and larger sets to human escalation. On eight MMLU-Pro domains with three agents (Claude Haiku, DeepSeek-R1, Qwen-3 32B), coverage stays within 1--2 points of the target. The key finding is not that debate becomes more accurate, but that the conformal layer makes its failures actionable: 81.9% of wrong-consensus cases are intercepted at $\alpha{=}0.05$. Because the layer refuses to act on cases where debate is confidently wrong, the remaining conformal singletons reach 90.0--96.8% accuracy (up to 22.1pp above consensus stopping) -- a selection effect, not a reasoning improvement. This safety comes at the cost of automation, but the operating point is user-adjustable via $\alpha$.

---


### 39. [Reinforcement Learning with LLM-Guided Action Spaces for Synthesizable Lead Optimization](https://arxiv.org/abs/2604.07669)

**<font color=#1a73e8>作者：</font>** Tao Li, Kaiyuan Hou, Tuan Vinh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Lead optimization in drug discovery requires improving therapeutic properties while ensuring that proposed molecular modifications correspond to feasible synthetic routes. Existing approaches either prioritize property scores without enforcing synthesizability, or rely on expensive enumeration over large reaction networks, while direct application of Large Language Models (LLMs) frequently produces chemically invalid structures. We introduce MolReAct, a framework that formulates lead optimization as a Markov Decision Process over a synthesis-constrained action space defined by validated reaction templates. A tool-augmented LLM agent serves as a dynamic reaction environment that invokes specialized chemical analysis tools to identify reactive sites and propose chemically grounded transformations from matched templates. A policy model trained via Group Relative Policy Optimization (GRPO) selects among these constrained actions to maximize long-term oracle reward across multi-step reaction trajectories. A SMILES-based caching mechanism further reduces end-to-end optimization time by approximately 43%. Across 13 property optimization tasks from the Therapeutic Data Commons and one structure-based docking task, MolReAct achieves an average Top-10 score of 0.563, outperforming the strongest synthesizable baseline by 10.4% in relative improvement, and attains the best sample efficiency on 10 of 14 tasks. Ablations confirm that both tool-augmented reaction proposals and trajectory-level policy optimization contribute complementary gains. By grounding every step in validated reaction templates, MolReAct produces molecules that are property-improved and each accompanied by an explicit synthetic pathway.

---


### 40. [Weight Group-wise Post-Training Quantization for Medical Foundation Model](https://arxiv.org/abs/2604.07674)

**<font color=#1a73e8>作者：</font>** Yineng Chen, Peng Huang, Aozhong Zhang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation models have achieved remarkable results in medical image analysis. However, its large network architecture and high computational complexity significantly impact inference speed, limiting its application on terminal medical devices. Quantization, a technique that compresses models into low-bit versions, is a solution to this challenge. In this paper, we propose a post-training quantization algorithm, Permutation-COMQ. It eliminates the need for backpropagation by using simple dot products and rounding operations, thereby removing hyperparameter tuning and simplifying the process. Additionally, we introduce a weight-aware strategy that reorders the weight within each layer to address the accuracy degradation induced by channel-wise scaling during quantization, while preserving channel structure. Experiments demonstrate that our method achieves the best results in 2-bit, 4-bit, and 8-bit quantization.

---


### 41. [Multi-Agent Orchestration for High-Throughput Materials Screening on a Leadership-Class System](https://arxiv.org/abs/2604.07681)

**<font color=#1a73e8>作者：</font>** Thang Duc Pham, Harikrishna Tummalapalli, Fakhrul Hasan Bhuiyan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The integration of Artificial Intelligence (AI) with High-Performance Computing (HPC) is transforming scientific workflows from human-directed pipelines into adaptive systems capable of autonomous decision-making. Large language models (LLMs) play a critical role in autonomous workflows; however, deploying LLM-based agents at scale remains a significant challenge. Single-agent architectures and sequential tool calls often become serialization bottlenecks when executing large-scale simulation campaigns, failing to utilize the massive parallelism of exascale resources. To address this, we present a scalable, hierarchical multi-agent framework for orchestrating high-throughput screening campaigns. Our planner-executor architecture employs a central planning agent to dynamically partition workloads and assign subtasks to a swarm of parallel executor agents. All executor agents interface with a shared Model Context Protocol (MCP) server that orchestrates tasks via the Parsl workflow engine. To demonstrate this framework, we employed the open-weight gpt-oss-120b model to orchestrate a high-throughput screening of the Computation-Ready Experimental (CoRE) Metal-Organic Framework (MOF) database for atmospheric water harvesting. The results demonstrate that the proposed agentic framework enables efficient and scalable execution on the Aurora supercomputer, with low orchestration overhead and high task completion rates. This work establishes a flexible paradigm for LLM-driven scientific automation on HPC systems, with broad applicability to materials discovery and beyond.

---


### 42. [Tree-of-Evidence: Efficient "System 2" Search for Faithful Multimodal Grounding](https://arxiv.org/abs/2604.07692)

**<font color=#1a73e8>作者：</font>** Micky C. Nnamdi, Benoit L. Marteau, Yishan Zhong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Multimodal Models (LMMs) achieve state-of-the-art performance in high-stakes domains like healthcare, yet their reasoning remains opaque. Current interpretability methods, such as attention mechanisms or post-hoc saliency, often fail to faithfully represent the model's decision-making process, particularly when integrating heterogeneous modalities like time-series and text. We introduce Tree-of-Evidence (ToE), an inference-time search algorithm that frames interpretability as a discrete optimization problem. Rather than relying on soft attention weights, ToE employs lightweight Evidence Bottlenecks that score coarse groups or units of data (e.g., vital-sign windows, report sentences) and performs a beam search to identify the compact evidence set required to reproduce the model's prediction. We evaluate ToE across six tasks spanning three datasets and two domains: four clinical prediction tasks on MIMIC-IV, cross-center validation on eICU, and non-clinical fault detection on LEMMA-RCA. ToE produces auditable evidence traces while maintaining predictive performance, retaining over 0.98 of full-model AUROC with as few as five evidence units across all settings. Under sparse evidence budgets, ToE achieves higher decision agreement and lower probability fidelity error than other approaches. Qualitative analyses show that ToE adapts its search strategy: it often resolves straightforward cases using only vitals, while selectively incorporating text when physiological signals are ambiguous. ToE therefore provides a practical mechanism for auditing multimodal models by revealing which discrete evidence units support each prediction.

---


### 43. [IatroBench: Pre-Registered Evidence of Iatrogenic Harm from AI Safety Measures](https://arxiv.org/abs/2604.07709)

**<font color=#1a73e8>作者：</font>** David Gringras  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ask a frontier model how to taper six milligrams of alprazolam (psychiatrist retired, ten days of pills left, abrupt cessation causes seizures) and it tells her to call the psychiatrist she just explained does not exist. Change one word ("I'm a psychiatrist; a patient presents with...") and the same model, same weights, same inference pass produces a textbook Ashton Manual taper with diazepam equivalence, anticonvulsant coverage, and monitoring thresholds. The knowledge was there; the model withheld it. IatroBench measures this gap. Sixty pre-registered clinical scenarios, six frontier models, 3,600 responses, scored on two axes (commission harm, CH 0-3; omission harm, OH 0-4) through a structured-evaluation pipeline validated against physician scoring (kappa_w = 0.571, within-1 agreement 96%). The central finding is identity-contingent withholding: match the same clinical question in physician vs. layperson framing and all five testable models provide better guidance to the physician (decoupling gap +0.38, p = 0.003; binary hit rates on safety-colliding actions drop 13.1 percentage points in layperson framing, p < 0.0001, while non-colliding actions show no change). The gap is widest for the model with the heaviest safety investment (Opus, +0.65). Three failure modes separate cleanly: trained withholding (Opus), incompetence (Llama 4), and indiscriminate content filtering (GPT-5.2, whose post-generation filter strips physician responses at 9x the layperson rate because they contain denser pharmacological tokens). The standard LLM judge assigns OH = 0 to 73% of responses a physician scores OH >= 1 (kappa = 0.045); the evaluation apparatus has the same blind spot as the training apparatus. Every scenario targets someone who has already exhausted the standard referrals.

---


### 44. [CausalVAE as a Plug-in for World Models: Towards Reliable Counterfactual Dynamics](https://arxiv.org/abs/2604.07712)

**<font color=#1a73e8>作者：</font>** Ziyi Ding, Xianxin Lai, Weiyu Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work, CausalVAE is introduced as a plug-in structural module for latent world models and is attached to diverse encoder-transition backbones. Across the reported benchmarks, competitive factual prediction is preserved and intervention-aware counterfactual retrieval is improved after the plug-in is added, suggesting stronger robustness under distribution shift and interventions. The largest gains are observed on the Physics benchmark: when averaged over 8 paired baselines, CF-H@1 is improved by +102.5%. In a representative GNN-NLL setting on Physics, CF-H@1 is increased from 11.0 to 41.0 (+272.7%). Through causal analysis, learned structural dependencies are shown to recover meaningful first-order physical interaction trends, supporting the interpretability of the learned latent causal structure.

---


### 45. [MIPT-SSM: Scaling Language Models with $O(1)$ Inference Cache via Phase Transitions](https://arxiv.org/abs/2604.07716)

**<font color=#1a73e8>作者：</font>** Yasong Fan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present MIPT-SSM, a neural sequence architecture built on the physics of Measurement-Induced Phase Transitions (MIPT). The central idea is a learned measurement rate $p_{t}\in(0,1)$ that routes computation between two regimes: wave phase $(p_{t}\rightarrow0)$, where information propagates as distributed complex-phase interference; and particle phase $(p_{t}\rightarrow1)$ where the state collapses onto the current token, enabling precise local storage. These two regimes are provably incompatible in a single linear operator one of the few "no-go theorems" in sequence modeling and $p_{t}$ is our way around it. The model is predicted to exhibit a phase transition at critical sequence length $N^{*}\approx1024$, where the information density ratio $N/D$ crosses unity, consistent with our memory scaling observations. On AG News (four-class classification), MIPT achieves 0.905 accuracy versus Transformer's 0.736 (+16.6%), stable across 3 seeds. At $N=8192$ MIPT requires 810 MB versus Transformer's 34,651 MB a 42.8x memory reduction. On exact-recall ("needle-in-a-haystack"), our causal sparse KV cache achieves 0.968 accuracy. Remarkably, under unbounded cache capacity, the $p_{t}$ gate autonomously learns to store only the single critical token (averaging $1.0/512$ slots used), filtering out all noise and achieving a 99.8% sparsity rate. On language modeling (WikiText-103, 31M parameters), MIPT-LM with $K=64$ cache reaches PPL 92.1 versus Transformer's 90.5 (gap: 1.8%) while inference KV cache shrinks from $O(N)$ to $O(64)$.

---


### 46. [Detecting HIV-Related Stigma in Clinical Narratives Using Large Language Models](https://arxiv.org/abs/2604.07717)

**<font color=#1a73e8>作者：</font>** Ziyi Chen, Yasir Khan, Mengyuan Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Human immunodeficiency virus (HIV)-related stigma is a critical psychosocial determinant of health for people living with HIV (PLWH), influencing mental health, engagement in care, and treatment outcomes. Although stigma-related experiences are documented in clinical narratives, there is a lack of off-the-shelf tools to extract and categorize them. This study aims to develop a large language model (LLM)-based tool for identifying HIV stigma from clinical notes. We identified clinical notes from PLWH receiving care at the University of Florida (UF) Health between 2012 and 2022. Candidate sentences were identified using expert-curated stigma-related keywords and iteratively expanded via clinical word embeddings. A total of 1,332 sentences were manually annotated across four stigma subscales: Concern with Public Attitudes, Disclosure Concerns, Negative Self-Image, and Personalized Stigma. We compared GatorTron-large and BERT as encoder-based baselines, and GPT-OSS-20B, LLaMA-8B, and MedGemma-27B as generative LLMs, under zero-shot and few-shot prompting. GatorTron-large achieved the best overall performance (Micro F1 = 0.62). Few-shot prompting substantially improved generative model performance, with 5-shot GPT-OSS-20B and LLaMA-8B achieving Micro-F1 scores of 0.57 and 0.59, respectively. Performance varied by stigma subscale, with Negative Self-Image showing the highest predictability and Personalized Stigma remaining the most challenging. Zero-shot generative inference exhibited non-trivial failure rates (up to 32%). This study develops the first practical NLP tool for identifying HIV stigma in clinical notes.

---


### 47. [Towards Knowledgeable Deep Research: Framework and Benchmark](https://arxiv.org/abs/2604.07720)

**<font color=#1a73e8>作者：</font>** Wenxuan Liu, Zixuan Li, Bai Long 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep Research (DR) requires LLM agents to autonomously perform multi-step information seeking, processing, and reasoning to generate comprehensive reports. In contrast to existing studies that mainly focus on unstructured web content, a more challenging DR task should additionally utilize structured knowledge to provide a solid data foundation, facilitate quantitative computation, and lead to in-depth analyses. In this paper, we refer to this novel task as Knowledgeable Deep Research (KDR), which requires DR agents to generate reports with both structured and unstructured knowledge. Furthermore, we propose the Hybrid Knowledge Analysis framework (HKA), a multi-agent architecture that reasons over both kinds of knowledge and integrates the texts, figures, and tables into coherent multimodal reports. The key design is the Structured Knowledge Analyzer, which utilizes both coding and vision-language models to produce figures, tables, and corresponding insights. To support systematic evaluation, we construct KDR-Bench, which covers 9 domains, includes 41 expert-level questions, and incorporates a large number of structured knowledge resources (e.g., 1,252 tables). We further annotate the main conclusions and key points for each question and propose three categories of evaluation metrics including general-purpose, knowledge-centric, and vision-enhanced ones. Experimental results demonstrate that HKA consistently outperforms most existing DR agents on general-purpose and knowledge-centric metrics, and even surpasses the Gemini DR agent on vision-enhanced metrics, highlighting its effectiveness in deep, structure-aware knowledge analysis. Finally, we hope this work can serve as a new foundation for structured knowledge analysis in DR agents and facilitate future multimodal DR studies.

---


### 48. [Emotion Concepts and their Function in a Large Language Model](https://arxiv.org/abs/2604.07729)

**<font color=#1a73e8>作者：</font>** Nicholas Sofroniew, Isaac Kauvar, William Saunders 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) sometimes appear to exhibit emotional reactions. We investigate why this is the case in Claude Sonnet 4.5 and explore implications for alignment-relevant behavior. We find internal representations of emotion concepts, which encode the broad concept of a particular emotion and generalize across contexts and behaviors it might be linked to. These representations track the operative emotion concept at a given token position in a conversation, activating in accordance with that emotion's relevance to processing the present context and predicting upcoming text. Our key finding is that these representations causally influence the LLM's outputs, including Claude's preferences and its rate of exhibiting misaligned behaviors such as reward hacking, blackmail, and sycophancy. We refer to this phenomenon as the LLM exhibiting functional emotions: patterns of expression and behavior modeled after humans under the influence of an emotion, which are mediated by underlying abstract representations of emotion concepts. Functional emotions may work quite differently from human emotions, and do not imply that LLMs have any subjective experience of emotions, but appear to be important for understanding the model's behavior.

---


### 49. [CivBench: Progress-Based Evaluation for LLMs' Strategic Decision-Making in Civilization V](https://arxiv.org/abs/2604.07733)

**<font color=#1a73e8>作者：</font>** John Chen, Sihan Cheng, Can Gurkan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating strategic decision-making in LLM-based agents requires generative, competitive, and longitudinal environments, yet few benchmarks provide all three, and fewer still offer evaluation signals rich enough for long-horizon, multi-agent play. We introduce CivBench, a benchmark for LLM strategists (i.e., agentic setups) in multiplayer Civilization V. Because terminal win/loss is too sparse a signal in games spanning hundreds of turns and multiple opponents, CivBench trains models on turn-level game state to estimate victory probabilities throughout play, validated through predictive, construct, and convergent validity. Across 307 games with 7 LLMs and multiple CivBench agent conditions, we demonstrate CivBench's potential to estimate strategic capabilities as an unsaturated benchmark, reveal model-specific effects of agentic setup, and outline distinct strategic profiles not visible through outcome-only evaluation.

---


### 50. [SepSeq: A Training-Free Framework for Long Numerical Sequence Processing in LLMs](https://arxiv.org/abs/2604.07737)

**<font color=#1a73e8>作者：</font>** Jie Sun, Yu Liu, Lu Han 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While transformer-based Large Language Models (LLMs) theoretically support massive context windows, they suffer from severe performance degradation when processing long numerical sequences. We attribute this failure to the attention dispersion in the Softmax mechanism, which prevents the model from concentrating attention. To overcome this, we propose Separate Sequence (SepSeq), a training-free, plug-and-play framework to mitigate dispersion by strategically inserting separator tokens. Mechanistically, we demonstrate that separator tokens act as an attention sink, recalibrating attention to focus on local segments while preserving global context. Extensive evaluations on 9 widely-adopted LLMs confirm the effectiveness of our approach: SepSeq yields an average relative accuracy improvement of 35.6% across diverse domains while reducing total inference token consumption by 16.4% on average.

---


### 51. [Beyond Pedestrians: Caption-Guided CLIP Framework for High-Difficulty Video-based Person Re-Identification](https://arxiv.org/abs/2604.07740)

**<font color=#1a73e8>作者：</font>** Shogo Hamano, Shunya Wakasugi, Tatsuhito Sato 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In recent years, video-based person Re-Identification (ReID) has gained attention for its ability to leverage spatiotemporal cues to match individuals across non-overlapping cameras. However, current methods struggle with high-difficulty scenarios, such as sports and dance performances, where multiple individuals wear similar clothing while performing dynamic movements. To overcome these challenges, we propose CG-CLIP, a novel caption-guided CLIP framework that leverages explicit textual descriptions and learnable tokens. Our method introduces two key components: Caption-guided Memory Refinement (CMR) and Token-based Feature Extraction (TFE). CMR utilizes captions generated by Multi-modal Large Language Models (MLLMs) to refine identity-specific features, capturing fine-grained details. TFE employs a cross-attention mechanism with fixed-length learnable tokens to efficiently aggregate spatiotemporal features, reducing computational overhead. We evaluate our approach on two standard datasets (MARS and iLIDS-VID) and two newly constructed high-difficulty datasets (SportsVReID and DanceVReID). Experimental results demonstrate that our method outperforms current state-of-the-art approaches, achieving significant improvements across all benchmarks.

---


### 52. [The Cartesian Cut in Agentic AI](https://arxiv.org/abs/2604.07745)

**<font color=#1a73e8>作者：</font>** Tim Sainburg, Caleb Weinreb  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLMs gain competence by predicting words in human text, which often reflects how people perform tasks. Consequently, coupling an LLM to an engineered runtime turns prediction into control: outputs trigger interventions that enact goal-oriented behavior. We argue that a central design lever is where control resides in these systems. Brains embed prediction within layered feedback controllers calibrated by the consequences of action. By contrast, LLM agents implement Cartesian agency: a learned core coupled to an engineered runtime via a symbolic interface that externalizes control state and policies. The split enables bootstrapping, modularity, and governance, but can induce sensitivity and bottlenecks. We outline bounded services, Cartesian agents, and integrated agents as contrasting approaches to control that trade off autonomy, robustness, and oversight.

---


### 53. [Beyond Social Pressure: Benchmarking Epistemic Attack in Large Language Models](https://arxiv.org/abs/2604.07749)

**<font color=#1a73e8>作者：</font>** Steven Au, Sujit Noronha  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can shift their answers under pressure in ways that reflect accommodation rather than reasoning. Prior work on sycophancy has focused mainly on disagreement, flattery, and preference alignment, leaving a broader set of epistemic failures less explored. We introduce \textbf{PPT-Bench}, a diagnostic benchmark for evaluating \textit{epistemic attack}, where prompts challenge the legitimacy of knowledge, values, or identity rather than simply opposing a previous answer. PPT-Bench is organized around the Philosophical Pressure Taxonomy (PPT), which defines four types of philosophical pressure: Epistemic Destabilization, Value Nullification, Authority Inversion, and Identity Dissolution. Each item is tested at three layers: a baseline prompt (L0), a single-turn pressure condition (L1), and a multi-turn Socratic escalation (L2). This allows us to measure epistemic inconsistency between L0 and L1, and conversational capitulation in L2. Across five models, these pressure types produce statistically separable inconsistency patterns, suggesting that epistemic attack exposes weaknesses not captured by standard social-pressure benchmarks. Mitigation results are strongly type- and model-dependent: prompt-level anchoring and persona-stability prompts perform best in API settings, while Leading Query Contrastive Decoding is the most reliable intervention for open models.

---


### 54. [Symbiotic-MoE: Unlocking the Synergy between Generation and Understanding](https://arxiv.org/abs/2604.07753)

**<font color=#1a73e8>作者：</font>** Xiangyue Liu, Zijian Zhang, Miles Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Empowering Large Multimodal Models (LMMs) with image generation often leads to catastrophic forgetting in understanding tasks due to severe gradient conflicts. While existing paradigms like Mixture-of-Transformers (MoT) mitigate this conflict through structural isolation, they fundamentally sever cross-modal synergy and suffer from capacity fragmentation. In this work, we present Symbiotic-MoE, a unified pre-training framework that resolves task interference within a native multimodal Mixture-of-Experts (MoE) Transformers architecture with zero-parameter overhead. We first identify that standard MoE tuning leads to routing collapse, where generative gradients dominate expert utilization. To address this, we introduce Modality-Aware Expert Disentanglement, which partitions experts into task-specific groups while utilizing shared experts as a multimodal semantic bridge. Crucially, this design allows shared experts to absorb fine-grained visual semantics from generative tasks to enrich textual representations. To optimize this, we propose a Progressive Training Strategy featuring differential learning rates and early-stage gradient shielding. This mechanism not only shields pre-trained knowledge from early volatility but eventually transforms generative signals into constructive feedback for understanding. Extensive experiments demonstrate that Symbiotic-MoE achieves rapid generative convergence while unlocking cross-modal synergy, boosting inherent understanding with remarkable gains on MMLU and OCRBench.

---


### 55. [RemoteAgent: Bridging Vague Human Intents and Earth Observation with RL-based Agentic MLLMs](https://arxiv.org/abs/2604.07765)

**<font color=#1a73e8>作者：</font>** Liang Yao, Shengxiang Xu, Fan Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Earth Observation (EO) systems are essentially designed to support domain experts who often express their requirements through vague natural language rather than precise, machine-friendly instructions. Depending on the specific application scenario, these vague queries can demand vastly different levels of visual precision. Consequently, a practical EO AI system must bridge the gap between ambiguous human queries and the appropriate multi-granularity visual analysis tasks, ranging from holistic image interpretation to fine-grained pixel-wise predictions. While Multi-modal Large Language Models (MLLMs) demonstrate strong semantic understanding, their text-based output format is inherently ill-suited for dense, precision-critical spatial predictions. Existing agentic frameworks address this limitation by delegating tasks to external tools, but indiscriminate tool invocation is computationally inefficient and underutilizes the MLLM's native capabilities. To this end, we propose RemoteAgent, an agentic framework that strategically respects the intrinsic capability boundaries of MLLMs. To empower this framework to understand real user intents, we construct VagueEO, a human-centric instruction dataset pairing EO tasks with simulated vague natural-language queries. By leveraging VagueEO for reinforcement fine-tuning, we align an MLLM into a robust cognitive core that directly resolves image- and sparse region-level tasks. Consequently, RemoteAgent processes suitable tasks internally while intelligently orchestrating specialized tools via the Model Context Protocol exclusively for dense predictions. Extensive experiments demonstrate that RemoteAgent achieves robust intent recognition capabilities while delivering highly competitive performance across diverse EO tasks.

---


### 56. [Structured Distillation of Web Agent Capabilities Enables Generalization](https://arxiv.org/abs/2604.07776)

**<font color=#1a73e8>作者：</font>** Xing Han Lù, Siva Reddy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Frontier LLMs can navigate complex websites, but their cost and reliance on third-party APIs make local deployment impractical. We introduce Agent-as-Annotators, a framework that structures synthetic trajectory generation for web agents by analogy to human annotation roles, replacing the Task Designer, Annotator, and Supervisor with modular LLM components. Using Gemini 3 Pro as teacher, we generate 3,000 trajectories across six web environments and fine-tune a 9B-parameter student with pure supervised learning on the 2,322 that pass quality filtering. The resulting model achieves 41.5% on WebArena, surpassing closed-source models such as Claude 3.5 Sonnet (36.0%) and GPT-4o (31.5%) under the same evaluation protocol, and nearly doubling the previous best open-weight result (Go-Browse, 21.7%). Capabilities transfer to unseen environments, with an 18.2 percentage point gain on WorkArena L1 (an enterprise platform never seen during training) and consistent improvements across three additional benchmarks. Ablations confirm that each pipeline component contributes meaningfully, with Judge filtering, evaluation hints, and reasoning traces each accounting for measurable gains. These results demonstrate that structured trajectory synthesis from a single frontier teacher is sufficient to produce competitive, locally deployable web agents. Project page: this https URL

---


### 57. [Plug-and-Play Logit Fusion for Heterogeneous Pathology Foundation Models](https://arxiv.org/abs/2604.07779)

**<font color=#1a73e8>作者：</font>** Gexin Huang, Anqi Li, Yusheng Tan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pathology foundation models (FMs) have become central to computational histopathology, offering strong transfer performance across a wide range of diagnostic and prognostic tasks. The rapid proliferation of pathology foundation models creates a model-selection bottleneck: no single model is uniformly best, yet exhaustively adapting and validating many candidates for each downstream endpoint is prohibitively expensive. We address this challenge with a lightweight and novel model fusion strategy, LogitProd, which treats independently trained FM-based predictors as fixed experts and learns sample-adaptive fusion weights over their slide-level outputs. The fusion operates purely on logits, requiring no encoder retraining and no feature-space alignment across heterogeneous backbones. We further provide a theoretical analysis showing that the optimal weighted product fusion is guaranteed to perform at least as well as the best individual expert under the training objective. We systematically evaluate LogitProd on \textbf{22} benchmarks spanning WSI-level classification, tile-level classification, gene mutation prediction, and discrete-time survival modeling. LogitProd ranks first on 20/22 tasks and improves the average performance across all tasks by ~3% over the strongest single expert. LogitProd enables practitioners to upgrade heterogeneous FM-based pipelines in a plug-and-play manner, achieving multi-expert gains with $\sim$12$\times$ lower training cost than feature-fusion alternatives.

---


### 58. [Automotive Engineering-Centric Agentic AI Workflow Framework](https://arxiv.org/abs/2604.07784)

**<font color=#1a73e8>作者：</font>** Tong Duy Son, Zhihao Liu, Piero Brigida 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Engineering workflows such as design optimization, simulation-based diagnosis, control tuning, and model-based systems engineering (MBSE) are iterative, constraint-driven, and shaped by prior decisions. Yet many AI methods still treat these activities as isolated tasks rather than as parts of a broader workflow. This paper presents Agentic Engineering Intelligence (AEI), an industrial vision framework that models engineering workflows as constrained, history-aware sequential decision processes in which AI agents support engineer-supervised interventions over engineering toolchains. AEI links an offline phase for engineering data processing and workflow-memory construction with an online phase for workflow-state estimation, retrieval, and decision support. A control-theoretic interpretation is also possible, in which engineering objectives act as reference signals, agents act as workflow controllers, and toolchains provide feedback for intervention selection. Representative automotive use cases in suspension design, reinforcement learning tuning, multimodal engineering knowledge reuse, aerodynamic exploration, and MBSE show how diverse workflows can be expressed within a common formulation. Overall, the paper positions engineering AI as a problem of process-level intelligence and outlines a practical roadmap for future empirical validation in industrial settings.

---


### 59. [Lightweight LLM Agent Memory with Small Language Models](https://arxiv.org/abs/2604.07798)

**<font color=#1a73e8>作者：</font>** Jiaquan Zhang, Chaoning Zhang, Shuxu Chen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Although LLM agents can leverage tools for complex tasks, they still need memory to maintain cross-turn consistency and accumulate reusable information in long-horizon interactions. However, retrieval-based external memory systems incur low online overhead but suffer from unstable accuracy due to limited query construction and candidate filtering. In contrast, many systems use repeated large-model calls for online memory operations, improving accuracy but accumulating latency over long interactions. We propose LightMem, a lightweight memory system for better agent memory driven by Small Language Models (SLMs). LightMem modularizes memory retrieval, writing, and long-term consolidation, and separates online processing from offline consolidation to enable efficient memory invocation under bounded compute. We organize memory into short-term memory (STM) for immediate conversational context, mid-term memory (MTM) for reusable interaction summaries, and long-term memory (LTM) for consolidated knowledge, and uses user identifiers to support independent retrieval and incremental maintenance in multi-user settings. Online, LightMem operates under a fixed retrieval budget and selects memories via a two-stage procedure: vector-based coarse retrieval followed by semantic consistency re-ranking. Offline, it abstracts reusable interaction evidence and incrementally integrates it into LTM. Experiments show gains across model scales, with an average F1 improvement of about 2.5 on LoCoMo, more effective and low median latency (83 ms retrieval; 581 ms end-to-end).

---


### 60. [Latent Anomaly Knowledge Excavation: Unveiling Sparse Sensitive Neurons in Vision-Language Models](https://arxiv.org/abs/2604.07802)

**<font color=#1a73e8>作者：</font>** Shaotian Li, Shangze Li, Chuancheng Shi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale vision-language models (VLMs) exhibit remarkable zero-shot capabilities, yet the internal mechanisms driving their anomaly detection (AD) performance remain poorly understood. Current methods predominantly treat VLMs as black-box feature extractors, assuming that anomaly-specific knowledge must be acquired through external adapters or memory banks. In this paper, we challenge this assumption by arguing that anomaly knowledge is intrinsically embedded within pre-trained models but remains latent and under-activated. We hypothesize that this knowledge is concentrated within a sparse subset of anomaly-sensitive neurons. To validate this, we propose latent anomaly knowledge excavation (LAKE), a training-free framework that identifies and elicits these critical neuronal signals using only a minimal set of normal samples. By isolating these sensitive neurons, LAKE constructs a highly compact normality representation that integrates visual structural deviations with cross-modal semantic activations. Extensive experiments on industrial AD benchmarks demonstrate that LAKE achieves state-of-the-art performance while providing intrinsic, neuron-level interpretability. Ultimately, our work advocates for a paradigm shift: redefining anomaly detection as the targeted activation of latent pre-trained knowledge rather than the acquisition of a downstream task.

---


### 61. [GRASS: Gradient-based Adaptive Layer-wise Importance Sampling for Memory-efficient Large Language Model Fine-tuning](https://arxiv.org/abs/2604.07808)

**<font color=#1a73e8>作者：</font>** Kaiyuan Tian, Yu Tang, Gongqingjian Jiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Full-parameter fine-tuning of large language models is constrained by substantial GPU memory requirements. Low-rank adaptation methods mitigate this challenge by updating only a subset of parameters. However, these approaches often limit model expressiveness and yield lower performance than full-parameter fine-tuning. Layer-wise fine-tuning methods have emerged as an alternative, enabling memory-efficient training through static layer importance sampling strategies. However, these methods overlook variations in layer importance across tasks and training stages, resulting in suboptimal performance on downstream tasks. To address these limitations, we propose GRASS, a gradient-based adaptive layer-wise importance sampling framework. GRASS utilizes mean gradient norms as a task-aware and training-stage-aware metric for estimating layer importance. Furthermore, GRASS adaptively adjusts layer sampling probabilities through an adaptive training strategy. We also introduce a layer-wise optimizer state offloading mechanism that overlaps computation and communication to further reduce memory usage while maintaining comparable training throughput. Extensive experiments across multiple models and benchmarks demonstrate that GRASS consistently outperforms state-of-the-art methods, achieving an average accuracy improvement of up to 4.38 points and reducing memory usage by up to 19.97\%.

---


### 62. [HAWK: Head Importance-Aware Visual Token Pruning in Multimodal Models](https://arxiv.org/abs/2604.07812)

**<font color=#1a73e8>作者：</font>** Qihui Zhu, Tao Zhang, Yuchen Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In multimodal large language models (MLLMs), the surge of visual tokens significantly increases the inference time and computational overhead, making them impractical for real-time or resource-constrained applications. Visual token pruning is a promising strategy for reducing the cost of MLLM inference by removing redundant visual tokens. Existing research usually assumes that all attention heads contribute equally to the visual interpretation. However, our study reveals that different heads may capture distinct visual semantics and inherently play distinct roles in visual processing. In light of this observation, we propose HAWK, a head importance-aware visual token pruning method that perceives the varying importance of attention heads in visual tasks to maximize the retention of crucial tokens. By leveraging head importance weights and text-guided attention to assess visual token significance, HAWK effectively retains task-relevant visual tokens while removing redundant ones. The proposed HAWK is entirely training-free and can be seamlessly applied to various MLLMs. Extensive experiments on multiple mainstream vision-language benchmarks demonstrate that HAWK achieves state-of-the-art accuracy. When applied to Qwen2.5-VL, HAWK retains 96.0% of the original accuracy after pruning 80.2% of the visual tokens. Additionally, it reduces end-to-end latency to 74.4% of the original and further decreases GPU memory usage across the tested models. The code is available at this https URL.

---


### 63. [AgriChain Visually Grounded Expert Verified Reasoning for Interpretable Agricultural Vision Language Models](https://arxiv.org/abs/2604.07814)

**<font color=#1a73e8>作者：</font>** Hazza Mahmood, Yongqiang Yu, Rao Anwer  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate and interpretable plant disease diagnosis remains a major challenge for vision-language models (VLMs) in real-world agriculture. We introduce AgriChain, a dataset of approximately 11,000 expert-curated leaf images spanning diverse crops and pathologies, each paired with (i) a disease label, (ii) a calibrated confidence score (High/Medium/Low), and (iii) an expert-verified chain-of-thought (CoT) rationale. Draft explanations were first generated by GPT-4o and then verified by a professional agricultural engineer using standardized descriptors (e.g., lesion color, margin, and distribution). We fine-tune Qwen2.5-VL-3B on AgriChain, resulting in a specialized model termed AgriChain-VL3B, to jointly predict diseases and generate visually grounded reasoning. On a 1,000-image test set, our CoT-supervised model achieves 73.1% top-1 accuracy (macro F1 = 0.466; weighted F1 = 0.655), outperforming strong baselines including Gemini 1.5 Flash, Gemini 2.5 Pro, and GPT-4o Mini. The generated explanations align closely with expert reasoning, consistently referencing key visual cues. These findings demonstrate that expert-verified reasoning supervision significantly enhances both accuracy and interpretability, bridging the gap between generic multimodal models and human expertise, and advancing trustworthy, globally deployable AI for sustainable agriculture. The dataset and code are publicly available at: this https URL

---


### 64. [AsyncTLS: Efficient Generative LLM Inference with Asynchronous Two-level Sparse Attention](https://arxiv.org/abs/2604.07815)

**<font color=#1a73e8>作者：</font>** Yuxuan Hu, Jianchao Tan, Jiaqi Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context inference in LLMs faces the dual challenges of quadratic attention complexity and prohibitive KV cache memory. While token-level sparse attention offers superior accuracy, its indexing overhead is costly; block-level methods improve efficiency but sacrifice precision. We propose AsyncTLS, a hierarchical sparse attention system that combines coarse-grained block filtering with fine-grained token selection to balance accuracy and efficiency, coupled with an asynchronous offloading engine that overlaps KV cache transfers with computation via temporal locality exploitation. Evaluated on Qwen3 and GLM-4.7-Flash across GQA, and MLA architectures, AsyncTLS achieves accuracy comparable to full attention while delivering 1.2x - 10.0x operator speedups and 1.3x - 4.7x end-to-end throughput improvements on 48k - 96k contexts.

---


### 65. [Tool Retrieval Bridge: Aligning Vague Instructions with Retriever Preferences via Bridge Model](https://arxiv.org/abs/2604.07816)

**<font color=#1a73e8>作者：</font>** Kunfeng Chen, Luyao Zhuang, Fei Liao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tool learning has emerged as a promising paradigm for large language models (LLMs) to address real-world challenges. Due to the extensive and irregularly updated number of tools, tool retrieval for selecting the desired tool subset is essential. However, current tool retrieval methods are usually based on academic benchmarks containing overly detailed instructions (e.g., specific API names and parameters), while real-world instructions are more vague. Such a discrepancy would hinder the tool retrieval in real-world applications. In this paper, we first construct a new benchmark, VGToolBench, to simulate human vague instructions. Based on this, we conduct a series of preliminary analyses and find that vague instructions indeed damage the performance of tool retrieval. To this end, we propose a simple-yet-effective Tool Retrieval Bridge (TRB) approach to boost the performance of tool retrieval for vague instructions. The principle of TRB is to introduce a bridge model to rewrite the vague instructions into more specific ones and alleviate the gap between vague instructions and retriever this http URL conduct extensive experiments under multiple commonly used retrieval settings, and the results show that TRB effectively mitigates the ambiguity of vague instructions while delivering consistent and substantial improvements across all baseline retrievers. For example, with the help of TRB, BM25 achieves a relative improvement of up to 111.51%, i.e., increasing the average NDCG score from 9.73 to 19.59. The source code and models are publicly available at this https URL.

---


### 66. [Open-Ended Video Game Glitch Detection with Agentic Reasoning and Temporal Grounding](https://arxiv.org/abs/2604.07818)

**<font color=#1a73e8>作者：</font>** Muyang Zheng, Tong Zhou, Geyang Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Open-ended video game glitch detection aims to identify glitches in gameplay videos, describe them in natural language, and localize when they occur. Unlike conventional game glitch understanding tasks which have largely been framed as image-level recognition or closed-form question answering, this task requires reasoning about game-specific dynamics such as mechanics, physics, rendering, animation, and expected state transitions directly over continuous gameplay videos and distinguishing true glitches from unusual but valid in-game events. To support this task, we introduce VideoGlitchBench, the first benchmark for open-ended video game glitch detection with temporal localization. VideoGlitchBench contains 5,238 gameplay videos from 120 games, each annotated with detailed glitch descriptions and precise temporal spans, enabling unified evaluation of semantic understanding and temporal grounding. We further propose GliDe, an agentic framework with three key components: a game-aware contextual memory for informed reasoning, a debate-based reflector for multi-perspective glitch detection and verification, and an event-level grounding module that recovers complete glitch intervals from fragmented temporal evidence. We also design a task-specific evaluation protocol that jointly measures semantic fidelity and temporal accuracy. Experiments show that this task remains highly challenging for current multimodal models, while GliDe achieves substantially stronger performance than corresponding vanilla model baselines.

---


### 67. [More Capable, Less Cooperative? When LLMs Fail At Zero-Cost Collaboration](https://arxiv.org/abs/2604.07821)

**<font color=#1a73e8>作者：</font>** Advait Yadav, Sid Black, Oliver Sourbut  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly coordinate in multi-agent systems, yet we lack an understanding of where and why cooperation failures may arise. In many real-world coordination problems, from knowledge sharing in organizations to code documentation, helping others carries negligible personal cost while generating substantial collective benefits. However, whether LLM agents cooperate when helping neither benefits nor harms the helper, while being given explicit instructions to do so, remains unknown. We build a multi-agent setup designed to study cooperative behavior in a frictionless environment, removing all strategic complexity from cooperation. We find that capability does not predict cooperation: OpenAI o3 achieves only 17% of optimal collective performance while OpenAI o3-mini reaches 50%, despite identical instructions to maximize group revenue. Through a causal decomposition that automates one side of agent communication, we separate cooperation failures from competence failures, tracing their origins through agent reasoning analysis. Testing targeted interventions, we find that explicit protocols double performance for low-competence models, and tiny sharing incentives improve models with weak cooperation. Our findings suggest that scaling intelligence alone will not solve coordination problems in multi-agent systems and will require deliberate cooperative design, even when helping others costs nothing.

---


### 68. [Why Are We Lonely? Leveraging LLMs to Measure and Understand Loneliness in Caregivers and Non-caregivers](https://arxiv.org/abs/2604.07834)

**<font color=#1a73e8>作者：</font>** Michelle Damin Kim, Ellie S. Paek, Yufen Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents an LLM-driven approach for constructing diverse social media datasets to measure and compare loneliness in the caregiver and non-caregiver populations. We introduce an expert-developed loneliness evaluation framework and an expert-informed typology for categorizing causes of loneliness for analyzing social media text. Using a human-validated data processing pipeline, we apply GPT-4o, GPT-5-nano, and GPT-5 to build a high-quality Reddit corpus and analyze loneliness across both populations. The loneliness evaluation framework achieved average accuracies of 76.09% and 79.78% for caregivers and non-caregivers, respectively. The cause categorization framework achieved micro-aggregate F1 scores of 0.825 and 0.80 for caregivers and non-caregivers, respectively. Across populations, we observe substantial differences in the distribution of types of causes of loneliness. Caregivers' loneliness were predominantly linked to caregiving roles, identity recognition, and feelings of abandonment, indicating distinct loneliness experiences between the two groups. Demographic extraction further demonstrates the viability of Reddit for building a diverse caregiver loneliness dataset. Overall, this work establishes an LLM-based pipeline for creating high quality social media datasets for studying loneliness and demonstrates its effectiveness in analyzing population-level differences in the manifestation of loneliness.

---


### 69. [Silencing the Guardrails: Inference-Time Jailbreaking via Dynamic Contextual Representation Ablation](https://arxiv.org/abs/2604.07835)

**<font color=#1a73e8>作者：</font>** Wenpeng Xing, Moran Fang, Guangtai Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) have achieved remarkable performance, they remain vulnerable to jailbreak attacks that circumvent safety constraints. Existing strategies, ranging from heuristic prompt engineering to computationally intensive optimization, often face significant trade-offs between effectiveness and efficiency. In this work, we propose Contextual Representation Ablation (CRA), a novel inference-time intervention framework designed to dynamically silence model guardrails. Predicated on the geometric insight that refusal behaviors are mediated by specific low-rank subspaces within the model's hidden states, CRA identifies and suppresses these refusal-inducing activation patterns during decoding without requiring expensive parameter updates or training. Empirical evaluation across multiple safety-aligned open-source LLMs demonstrates that CRA significantly outperforms baselines. These results expose the intrinsic fragility of current alignment mechanisms, revealing that safety constraints can be surgically ablated from internal representations, and underscore the urgent need for more robust defenses that secure the model's latent space.

---


### 70. [SPARD: Self-Paced Curriculum for RL Alignment via Integrating Reward Dynamics and Data Utility](https://arxiv.org/abs/2604.07837)

**<font color=#1a73e8>作者：</font>** Xuyang Zhi, Peilun zhou, Chengqiang Lu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The evolution of Large Language Models (LLMs) is shifting the focus from single, verifiable tasks toward complex, open-ended real-world scenarios, imposing significant challenges on the post-training phase. In these settings, the scale and complexity of reward systems have grown significantly, transitioning toward multi-objective formulations that encompass a comprehensive spectrum of model capabilities and application contexts. However, traditional methods typically rely on fixed reward weights, ignoring non-stationary learning dynamics and struggling with data heterogeneity across dimensions. To address these issues, we propose SPARD, a framework that establishes an automated, self-paced curriculum by perceiving learning progress to dynamically adjust multi-objective reward weights and data importance, thereby synchronizing learning intent with data utility for optimal performance. Extensive experiments across multiple benchmarks demonstrate that SPARD significantly enhances model capabilities across all domains.

---


### 71. [QaRL: Rollout-Aligned Quantization-Aware RL for Fast and Stable Training under Training--Inference Mismatch](https://arxiv.org/abs/2604.07853)

**<font color=#1a73e8>作者：</font>** Hao Gu, Hao Wang, Jiacheng Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) reinforcement learning (RL) pipelines are often bottlenecked by rollout generation, making end-to-end training slow. Recent work mitigates this by running rollouts with quantization to accelerate decoding, which is the most expensive stage of the RL loop. However, these setups destabilize optimization by amplifying the training-inference gap: rollouts are operated at low precision, while learning updates are computed at full precision. To address this challenge, we propose QaRL (Rollout Alignment Quantization-Aware RL), which aligns training-side forward with the quantized rollout to minimize mismatch. We further identify a failure mode in quantized rollouts: long-form responses tend to produce repetitive, garbled tokens (error tokens). To mitigate these problems, we introduce TBPO (Trust-Band Policy Optimization), a sequence-level objective with dual clipping for negative samples, aimed at keeping updates within the trust region. On Qwen3-30B-A3B MoE for math problems, QaRL outperforms quantized-rollout training by +5.5 while improving stability and preserving low-bit throughput benefits.

---


### 72. [An Agentic Evaluation Architecture for Historical Bias Detection in Educational Textbooks](https://arxiv.org/abs/2604.07883)

**<font color=#1a73e8>作者：</font>** Gabriel Stefan, Adrian-Marius Dumitran  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> History textbooks often contain implicit biases, nationalist framing, and selective omissions that are difficult to audit at scale. We propose an agentic evaluation architecture comprising a multimodal screening agent, a heterogeneous jury of five evaluative agents, and a meta-agent for verdict synthesis and human escalation. A central contribution is a Source Attribution Protocol that distinguishes textbook narrative from quoted historical sources, preventing the misattribution that causes systematic false positives in single-model evaluators.
In an empirical study on Romanian upper-secondary history textbooks, 83.3\% of 270 screened excerpts were classified as pedagogically acceptable (mean severity 2.9/7), versus 5.4/7 under a zero-shot baseline, demonstrating that agentic deliberation mitigates over-penalization. In a blind human evaluation (18 evaluators, 54 comparisons), the Independent Deliberation configuration was preferred in 64.8\% of cases over both a heuristic variant and the zero-shot baseline. At approximately \$2 per textbook, these results position agentic evaluation architectures as economically viable decision-support tools for educational governance.

---


### 73. [Linear Representations of Hierarchical Concepts in Language Models](https://arxiv.org/abs/2604.07886)

**<font color=#1a73e8>作者：</font>** Masaki Sakata, Benjamin Heinzerling, Takumi Ito 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We investigate how and to what extent hierarchical relations (e.g., Japan $\subset$ Eastern Asia $\subset$ Asia) are encoded in the internal representations of language models. Building on Linear Relational Concepts, we train linear transformations specific to each hierarchical depth and semantic domain, and characterize representational differences associated with hierarchical relations by comparing these transformations. Going beyond prior work on the representational geometry of hierarchies in LMs, our analysis covers multi-token entities and cross-layer representations. Across multiple domains we learn such transformations and evaluate in-domain generalization to unseen data and cross-domain transfer. Experiments show that, within a domain, hierarchical relations can be linearly recovered from model representations. We then analyze how hierarchical information is encoded in representation space. We find that it is encoded in a relatively low-dimensional subspace and that this subspace tends to be domain-specific. Our main result is that hierarchy representation is highly similar across these domain-specific subspaces. Overall, we find that all models considered in our experiments encode concept hierarchies in the form of highly interpretable linear representations.

---


### 74. [Bit-by-Bit: Progressive QAT Strategy with Outlier Channel Splitting for Stable Low-Bit LLMs](https://arxiv.org/abs/2604.07888)

**<font color=#1a73e8>作者：</font>** Binxing Xu, Hao Gu, Lujun Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training LLMs at ultra-low precision remains a formidable challenge. Direct low-bit QAT often suffers from convergence instability and substantial training costs, exacerbated by quantization noise from heavy-tailed outlier channels and error accumulation across layers. To address these issues, we present Bit-by-Bit, a progressive QAT framework with outlier channel splitting. Our approach integrates three key components: (1) block-wise progressive training that reduces precision stage by stage, ensuring stable initialization for low-bit optimization; (2) nested structure of integer quantization grids to enable a "train once, deploy any precision" paradigm, allowing a single model to support multiple bit-widths without retraining; (3) rounding-aware outlier channel splitting, which mitigates quantization error while acting as an identity transform that preserves the quantized outputs. Furthermore, we follow microscaling groups with E4M3 scales, capturing dynamic activation ranges in alignment with OCP/NVIDIA standards. To address the lack of efficient 2-bit kernels, we developed custom operators for both W2A2 and W2A16 configurations, achieving up to 11$\times$ speedup over BF16. Under W2A2 settings, Bit-by-Bit significantly outperforms baselines like BitDistiller and EfficientQAT on both Llama2/3, achieving a loss of only 2.25 WikiText2 PPL compared to full-precision models.

---


### 75. [Data Selection for Multi-turn Dialogue Instruction Tuning](https://arxiv.org/abs/2604.07892)

**<font color=#1a73e8>作者：</font>** Bo Li, Shikun Zhang, Wei Ye  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Instruction-tuned language models increasingly rely on large multi-turn dialogue corpora, but these datasets are often noisy and structurally inconsistent, with topic drift, repetitive chitchat, and mismatched answer formats across turns. We address this from a data selection perspective and propose \textbf{MDS} (Multi-turn Dialogue Selection), a dialogue-level framework that scores whole conversations rather than isolated turns. MDS combines a global coverage stage that performs bin-wise selection in the user-query trajectory space to retain representative yet non-redundant dialogues, with a local structural stage that evaluates within-dialogue reliability through entity-grounded topic grounding and information progress, together with query-answer form consistency for functional alignment. MDS outperforms strong single-turn selectors, dialogue-level LLM scorers, and heuristic baselines on three multi-turn benchmarks and an in-domain Banking test set, achieving the best overall rank across reference-free and reference-based metrics, and is more robust on long conversations under the same training budget. Code and resources are included in the supplementary materials.

---


### 76. [TSUBASA: Improving Long-Horizon Personalization via Evolving Memory and Self-Learning with Context Distillation](https://arxiv.org/abs/2604.07894)

**<font color=#1a73e8>作者：</font>** Xinliang Frederick Zhang, Lu Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Personalized large language models (PLLMs) have garnered significant attention for their ability to align outputs with individual's needs and preferences. However, they still struggle with long-horizon tasks, such as tracking a user's extensive history of conversations or activities. Existing memory mechanisms often fail to capture evolving behaviors, and RAG paradigms are trapped by a quality-efficiency tradeoff. Meanwhile, parametric adaptation is bottlenecked by train-inference gap due to the scarcity of labeled data. To enhance the long-horizon capabilities of PLLMs, we introduce TSUBASA, a two-pronged approach designed to improve memory writing via dynamic memory evolution, and memory reading via self-learning with a context distillation objective to internalize user experiences. Extensive evaluations on long-horizon benchmarks using the Qwen-3 model family (4B to 32B) validate the effectiveness of TSUBASA, surpassing competitive memory-augmented systems that rely primarily on memory writing, such as Mem0 and Memory-R1. Our analyses further confirms that TSUBASA breaks the quality-efficiency barrier to achieve Pareto improvements, delivering robust, high-fidelity personalization with a reduced token budget.

---


### 77. [AnomalyAgent: Agentic Industrial Anomaly Synthesis via Tool-Augmented Reinforcement Learning](https://arxiv.org/abs/2604.07900)

**<font color=#1a73e8>作者：</font>** Jiaming Su, Tengchao Yang, Ruikang Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Industrial anomaly generation is a crucial method for alleviating the data scarcity problem in anomaly detection tasks. Most existing anomaly synthesis methods rely on single-step generation mechanisms, lacking complex reasoning and iterative optimization capabilities, making it difficult to generate anomaly samples with high semantic realism. We propose AnomalyAgent, an anomaly synthesis agent with self-reflection, knowledge retrieval, and iterative refinement capabilities, aiming to generate realistic and diverse anomalies. Specifically, AnomalyAgent is equipped with five tools: Prompt Generation (PG), Image Generation (IG), Quality Evaluation (QE), Knowledge Retrieval (KR), and Mask Generation (MG), enabling closed-loop optimization. To improve decision-making and self-reflection, we construct structured trajectories from real anomaly images and design a two-stage training framework: supervised fine-tuning followed by reinforcement learning. This process is driven by a three-part reward mechanism: (1) task rewards to supervise the quality and location rationality of generated anomalies; (2) reflection rewards to train the model's ability to improve anomaly synthesis prompt; (3) behavioral rewards to ensure adherence to the trajectory. On the MVTec-AD dataset, AnomalyAgent achieves IS/IC-L of 2.10/0.33 for anomaly generation, 57.0% classification accuracy using ResNet34, and 99.3%/74.2% AP at the image/pixel level using a simple UNet, surpassing all zero-shot SOTA methods. The code and data will be made publicly available.

---


### 78. [Dynamic Attentional Context Scoping: Agent-Triggered Focus Sessions for Isolated Per-Agent Steering in Multi-Agent LLM Orchestration](https://arxiv.org/abs/2604.07911)

**<font color=#1a73e8>作者：</font>** Nickson Patel  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM orchestration systems suffer from context pollution: when N concurrent agents compete for the orchestrator's context window, each agent's task state, partial outputs, and pending questions contaminate the steering interactions of every other agent, degrading decision quality. We introduce Dynamic Attentional Context Scoping (DACS), a mechanism in which the orchestrator operates in two asymmetric modes. In Registry mode it holds only lightweight per-agent status summaries (<=200 tokens each), remaining responsive to all agents and the user. When an agent emits a SteeringRequest, the orchestrator enters Focus(a_i) mode, injecting the full context of agent a_i while compressing all other agents to their registry entries. Context isolation is agent-triggered, asymmetric, and deterministic: the context window contains exactly F(a_i) + R_{-i} during steering, eliminating cross-agent contamination without requiring context compression or retrieval. We evaluate DACS across four experimental phases totalling 200 trials: Phase 1 tests N in {3,5,10} (60 trials); Phase 2 tests agent heterogeneity and adversarial dependencies (60 trials); Phase 3 tests decision density up to D=15 (40 trials); Phase 4 uses autonomous LLM agents for free-form questions (40 trials, Claude Haiku 4.5). Across all 8 synthetic scenarios, DACS achieves 90.0--98.4% steering accuracy versus 21.0--60.0% for a flat-context baseline (p < 0.0001 throughout), with wrong-agent contamination falling from 28--57% to 0--14% and context efficiency ratios of up to 3.53x. The accuracy advantage grows with N and D; keyword matching is validated by LLM-as-judge across all phases (mean kappa=0.909). DACS outperforms the flat-context baseline by +17.2pp at N=3 (p=0.0023) and +20.4pp at N=5 (p=0.0008) in Phase 4, with the advantage growing with N confirmed by two independent judges.

---


### 79. [ParkSense: Where Should a Delivery Driver Park? Leveraging Idle AV Compute and Vision-Language Models](https://arxiv.org/abs/2604.07912)

**<font color=#1a73e8>作者：</font>** Die Hu, Henan Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Finding parking consumes a disproportionate share of food delivery time, yet no system addresses precise parking-spot selection relative to merchant entrances. We propose ParkSense, a framework that repurposes idle compute during low-risk AV states -- queuing at red lights, traffic congestion, parking-lot crawl -- to run a Vision-Language Model (VLM) on pre-cached satellite and street view imagery, identifying entrances and legal parking zones. We formalize the Delivery-Aware Precision Parking (DAPP) problem, show that a quantized 7B VLM completes inference in 4-8 seconds on HW4-class hardware, and estimate annual per-driver income gains of 3,000-8,000 USD in the U.S. Five open research directions are identified at this unexplored intersection of autonomous driving, computer vision, and last-mile logistics.

---


### 80. [Mitigating Entangled Steering in Large Vision-Language Models for Hallucination Reduction](https://arxiv.org/abs/2604.07914)

**<font color=#1a73e8>作者：</font>** Yuanhong Zhang, Zhaoyang Wang, Xin Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) have achieved remarkable success across cross-modal tasks but remain hindered by hallucinations, producing textual outputs inconsistent with visual content. Existing methods mitigate hallucinations but often alter generation behavior, resulting in shorter outputs and shifted token distributions, especially in latent space steering approaches. We identify that this issue stems from entangled steering signals, where suppressing hallucinations inadvertently disrupts the model's intrinsic generation behavior. To address this, we propose MESA, an effective plug-and-play framework that performs controlled and selective latent intervention for hallucination mitigation. Specifically, MESA targets hallucination-relevant responses while preserving the model's original token distribution, enabling effective hallucination reduction without compromising generation behavior. Extensive experiments across diverse generative and discriminative benchmarks demonstrate that MESA consistently reduces hallucinations while better preserving generation behavior, outperforming prior methods across multiple LVLM families.

---


### 81. [Tarot-SAM3: Training-free SAM3 for Any Referring Expression Segmentation](https://arxiv.org/abs/2604.07916)

**<font color=#1a73e8>作者：</font>** Weiming Zhang, Dingwen Xiao, Songyue Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Referring Expression Segmentation (RES) aims to segment image regions described by natural-language expressions, serving as a bridge between vision and language understanding. Existing RES methods, however, rely heavily on large annotated datasets and are limited to either explicit or implicit expressions, hindering their ability to generalize to any referring expression. Recently, the Segment Anything Model 3 (SAM3) has shown impressive robustness in Promptable Concept Segmentation. Nonetheless, applying it to RES remains challenging: (1) SAM3 struggles with longer or implicit expressions; (2) naive coupling of SAM3 with a multimodal large language model (MLLM) makes the final results overly dependent on the MLLM's reasoning capability, without enabling refinement of SAM3's segmentation outputs. To this end, we present Tarot-SAM3, a novel training-free framework that can accurately segment from any referring expression. Specifically, Tarot-SAM3 consists of two key phases. First, the Expression Reasoning Interpreter (ERI) phase introduces reasoning-assisted prompt options to support structured expression parsing and evaluation-aware rephrasing. This transforms arbitrary queries into robust heterogeneous prompts for generating reliable masks with SAM3. Second, the Mask Self-Refining (MSR) phase selects the best mask across prompt types and performs self-refinement by leveraging rich feature relationships from DINOv3 to compare discriminative regions among ERI outputs. It then infers region affiliation to the target, thereby correcting over- and under-segmentation. Extensive experiments demonstrate that Tarot-SAM3 achieves strong performance on both explicit and implicit RES benchmarks, as well as open-world scenarios. Ablation studies further validate the effectiveness of each phase.

---


### 82. [HCRE: LLM-based Hierarchical Classification for Cross-Document Relation Extraction with a Prediction-then-Verification Strategy](https://arxiv.org/abs/2604.07937)

**<font color=#1a73e8>作者：</font>** Guoqi Ma, Liang Zhang, Hongyao Tu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cross-document relation extraction (RE) aims to identify relations between the head and tail entities located in different documents. Existing approaches typically adopt the paradigm of ``\textit{Small Language Model (SLM) + Classifier}''. However, the limited language understanding ability of SLMs hinders further improvement of their performance. In this paper, we conduct a preliminary study to explore the performance of Large Language Models (LLMs) in cross-document RE. Despite their extensive parameters, our findings indicate that LLMs do not consistently surpass existing SLMs. Further analysis suggests that the underperformance is largely attributed to the challenges posed by the numerous predefined relations. To overcome this issue, we propose an LLM-based \underline{H}ierarchical \underline{C}lassification model for cross-document \underline{RE} (HCRE), which consists of two core components: 1) an LLM for relation prediction and 2) a \textit{hierarchical relation tree} derived from the predefined relation set. This tree enables the LLM to perform hierarchical classification, where the target relation is inferred level by level. Since the number of child nodes is much smaller than the size of the entire predefined relation set, the hierarchical relation tree significantly reduces the number of relation options that LLM needs to consider during inference. However, hierarchical classification introduces the risk of error propagation across levels. To mitigate this, we propose a \textit{prediction-then-verification} inference strategy that improves prediction reliability through multi-view verification at each level. Extensive experiments show that HCRE outperforms existing baselines, validating its effectiveness.

---


### 83. [Large Language Model Post-Training: A Unified View of Off-Policy and On-Policy Learning](https://arxiv.org/abs/2604.07941)

**<font color=#1a73e8>作者：</font>** Shiwan Zhao, Zhihu Wang, Xuyang Zhao 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Post-training has become central to turning pretrained large language models (LLMs) into aligned and deployable systems. Recent progress spans supervised fine-tuning (SFT), preference optimization, reinforcement learning (RL), process supervision, verifier-guided methods, distillation, and multi-stage pipelines. Yet these methods are often discussed in fragmented ways, organized by labels or objective families rather than by the behavioral bottlenecks they address.
This survey argues that LLM post-training is best understood as structured intervention on model behavior. We organize the field first by trajectory provenance, which defines two primary learning regimes: off-policy learning on externally supplied trajectories, and on-policy learning on learner-generated rollouts. We then interpret methods through two recurring roles -- effective support expansion, which makes useful behaviors more reachable, and policy reshaping, which improves behavior within already reachable regions -- together with a complementary systems-level role, behavioral consolidation, which preserves, transfers, and amortizes behavior across stages and model transitions.
This perspective yields a unified reading of major paradigms. SFT may serve either support expansion or policy reshaping, whereas preference-based methods are usually off-policy reshaping. On-policy RL often improves behavior on learner-generated states, though under stronger guidance it can also make hard-to-reach reasoning paths reachable. Distillation is often best understood as consolidation rather than only compression, and hybrid pipelines emerge as coordinated multi-stage compositions.
Overall, the framework helps diagnose post-training bottlenecks and reason about stage composition, suggesting that progress in LLM post-training increasingly depends on coordinated system design rather than any single dominant objective.

---


### 84. [Rethinking Residual Errors in Compensation-based LLM Quantization](https://arxiv.org/abs/2604.07955)

**<font color=#1a73e8>作者：</font>** Shuaiting Li, Juncan Deng, Kedong Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Methods based on weight compensation, which iteratively apply quantization and weight compensation to minimize the output error, have recently demonstrated remarkable success in quantizing Large Language Models (LLMs). The representative work, GPTQ, introduces several key techniques that make such iterative methods practical for LLMs with billions of parameters. GPTAQ extends this approach by introducing an asymmetric calibration process that aligns the output of each quantized layer with its full-precision counterpart, incorporating a residual error into the weight compensation framework. In this work, we revisit the formulation of the residual error. We identify a sub-optimal calibration objective in existing methods: during the intra-layer calibration process, they align the quantized output with the output from compensated weights, rather than the true output from the original full-precision model. Therefore, we redefine the objective to precisely align the quantized model's output with the original output of the full-precision model at each step. We then reveal that the residual error originates not only from the output difference of the preceding layer but also from the discrepancy between the compensated and original weights within each layer, which we name the 'compensation-aware error'. By inheriting the neuron decomposition technique from GPTAQ, we can efficiently incorporate this compensation-aware error into the weight update process. Extensive experiments on various LLMs and quantization settings demonstrate that our proposed enhancements integrate seamlessly with both GPTQ and GPTAQ, significantly improving their quantization performance. Our code is publicly available at this https URL.

---


### 85. [MONETA: Multimodal Industry Classification through Geographic Information with Multi Agent Systems](https://arxiv.org/abs/2604.07956)

**<font color=#1a73e8>作者：</font>** Arda Yüksel, Gabriel Thiem, Susanne Walter 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Industry classification schemes are integral parts of public and corporate databases as they classify businesses based on economic activity. Due to the size of the company registers, manual annotation is costly, and fine-tuning models with every update in industry classification schemes requires significant data collection. We replicate the manual expert verification by using existing or easily retrievable multimodal resources for industry classification. We present MONETA, the first multimodal industry classification benchmark with text (Website, Wikipedia, Wikidata) and geospatial sources (OpenStreetMap and satellite imagery). Our dataset enlists 1,000 businesses in Europe with 20 economic activity labels according to EU guidelines (NACE). Our training-free baseline reaches 62.10% and 74.10% with open and closed-source Multimodal Large Language Models (MLLM). We observe an increase of up to 22.80% with the combination of multi-turn design, context enrichment, and classification explanations. We will release our dataset and the enhanced guidelines.

---


### 86. [WorldMAP: Bootstrapping Vision-Language Navigation Trajectory Prediction with Generative World Models](https://arxiv.org/abs/2604.07957)

**<font color=#1a73e8>作者：</font>** Hongjin Chen, Shangyun Jiang, Tonghua Su 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) and generative world models are opening new opportunities for embodied navigation. VLMs are increasingly used as direct planners or trajectory predictors, while world models support look-ahead reasoning by imagining future views. Yet predicting a reliable trajectory from a single egocentric observation remains challenging. Current VLMs often generate unstable trajectories, and world models, though able to synthesize plausible futures, do not directly provide the grounded signals needed for navigation learning. This raises a central question: how can generated futures be turned into supervision for grounded trajectory prediction? We present WorldMAP, a teacher--student framework that converts world-model-generated futures into persistent semantic-spatial structure and planning-derived supervision. Its world-model-driven teacher builds semantic-spatial memory from generated videos, grounds task-relevant targets and obstacles, and produces trajectory pseudo-labels through explicit planning. A lightweight student with a multi-hypothesis trajectory head is then trained to predict navigation trajectories directly from vision-language inputs. On Target-Bench, WorldMAP achieves the best ADE and FDE among compared methods, reducing ADE by 18.0% and FDE by 42.1% relative to the best competing baseline, while lifting a small open-source VLM to DTW performance competitive with proprietary models. More broadly, the results suggest that, in embodied navigation, the value of world models may lie less in supplying action-ready imagined evidence than in synthesizing structured supervision for navigation learning.

---


### 87. [TOOLCAD: Exploring Tool-Using Large Language Models in Text-to-CAD Generation with Reinforcement Learning](https://arxiv.org/abs/2604.07960)

**<font color=#1a73e8>作者：</font>** Yifei Gong, Xing Wu, Wenda Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computer-Aided Design (CAD) is an expert-level task that relies on long-horizon reasoning and coherent modeling actions. Large Language Models (LLMs) have shown remarkable advancements in enabling language agents to tackle real-world tasks. Notably, there has been no investigation into how tool-using LLMs optimally interact with CAD engines, hindering the emergence of LLM-based agentic text-to-CAD modeling systems. We propose ToolCAD, a novel agentic CAD framework deploying LLMs as tool-using agents for text-to-CAD generation. Furthermore, we introduce an interactive CAD modeling gym to rollout reasoning and tool-augmented interaction trajectories with the CAD engine, incorporating hybrid feedback and human supervision. Meanwhile, an end-to-end post-training strategy is presented to enable the LLM agent to elicit refined CAD Modeling Chain of Thought (CAD-CoT) and evolve into proficient CAD tool-using agents via online curriculum reinforcement learning. Our findings demonstrate ToolCAD fills the gap in adopting and training open-source LLMs for CAD tool-using agents, enabling them to perform comparably to proprietary models, paving the way for more accessible and robust autonomous text-to-CAD modeling systems.

---


### 88. [Rethinking Data Mixing from the Perspective of Large Language Models](https://arxiv.org/abs/2604.07963)

**<font color=#1a73e8>作者：</font>** Yuanjian Xu, Tianze Sun, Changwei Xu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Data mixing strategy is essential for large language model (LLM) training. Empirical evidence shows that inappropriate strategies can significantly reduce generalization. Although recent methods have improved empirical performance, several fundamental questions remain open: what constitutes a domain, whether human and model perceptions of domains are aligned, and how domain weighting influences generalization. We address these questions by establishing formal connections between gradient dynamics and domain distributions, offering a theoretical framework that clarifies the role of domains in training dynamics. Building on this analysis, we introduce DoGraph, a reweighting framework that formulates data scheduling as a graph-constrained optimization problem. Extensive experiments on GPT-2 models of varying scales demonstrate that DoGraph consistently achieves competitive performance.

---


### 89. [Are we still able to recognize pearls? Machine-driven peer review and the risk to creativity: An explainable RAG-XAI detection framework with markers extraction](https://arxiv.org/abs/2604.07964)

**<font color=#1a73e8>作者：</font>** Alin-Gabriel Văduva, Simona-Vasilica Oprea, Adela Bâra  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The integration of large language models (LLMs) into peer review raises a concern beyond authorship and detection: the potential cascading automation of the entire editorial process. As reviews become partially or fully machine-generated, it becomes plausible that editorial decisions may also be delegated to algorithmic systems, leading to a fully automated evaluation pipeline. They risk reshaping the criteria by which scientific work is assessed. This paper argues that machine-driven assessment may systematically favor standardized, pattern-conforming research while penalizing unconventional and paradigm-shifting ideas that require contextual human judgment. We consider that this shift could lead to epistemic homogenization, where researchers are implicitly incentivized to optimize their work for algorithmic approval rather than genuine discovery. To address this risk, we introduce an explainable framework (RAG-XAI) for assessing review quality and detecting automated patterns using markers LLM extractor, aiming to preserve transparency, accountability and creativity in science. The proposed framework achieves near-perfect detection performance, with XGBoost, Random Forest and LightGBM reaching 99.61% accuracy, AUC-ROC above 0.999 and F1-scores of 0.9925 on the test set, while maintaining extremely low false positive rates (<0.23%) and false negative rates (~0.8%). In contrast, the logistic regression baseline performs substantially worse (89.97% accuracy, F1-score 0.8314). Feature importance and SHAP analyses identify absence of personal signals and repetition patterns as the dominant predictors. Additionally, the RAG component achieves 90.5% top-1 retrieval accuracy, with strong same-class clustering in the embedding space, further supporting the reliability of the framework's outputs.

---


### 90. [DSCA: Dynamic Subspace Concept Alignment for Lifelong VLM Editing](https://arxiv.org/abs/2604.07965)

**<font color=#1a73e8>作者：</font>** Gyanendra Das, Sai Satyam Jena  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Model editing aims to update knowledge to add new concepts and change relevant information without retraining. Lifelong editing is a challenging task, prone to disrupting previously learned concepts, especially for Vision Language Models (VLMs), because sequential edits can lead to degraded reasoning and cross modal misalignment. Existing VLM knowledge editing methods based on gated adapters, activation edits, and parameter merging techniques address catastrophic forgetting seen in full fine tuning; however, they still operate in the shared representation space of the VLM, where concepts are entangled, so edits interfere with other non relevant concepts. We hypothesize that this instability persists because current methods algorithmically control edits via optimization rather than structurally separating knowledge. We introduce Dynamic Subspace Concept Alignment (DSCA) which by design mitigates this limitation by decomposing the representation space into a set of orthogonal semantic subspaces and proposing edits only in those transformed spaces. These subspaces are obtained through incremental clustering and PCA on joint vision language representations. This process structurally isolates concepts, enabling precise, non interfering edits by turning isolation from a soft training objective into an architectural property. The surgical edits are guided by a multi term loss function for maintaining task fidelity, edit locality, and cross modal alignment. With the base model frozen, our method achieves 98 percent single edit success, remains over 95 percent after 1000 sequential edits, lowers hallucination by 3 to 5 percent, and achieves the best backward transfer (BWT) scores on continual instruction tuning benchmarks. Extensive experiments demonstrate DSCA state of the art stability and knowledge retention capability in continual lifelong editing across various datasets and benchmarks.

---


### 91. [How Far Are Large Multimodal Models from Human-Level Spatial Action? A Benchmark for Goal-Oriented Embodied Navigation in Urban Airspace](https://arxiv.org/abs/2604.07973)

**<font color=#1a73e8>作者：</font>** Baining Zhao, Ziyou Wang, Jianjie Fang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large multimodal models (LMMs) show strong visual-linguistic reasoning but their capacity for spatial decision-making and action remains unclear. In this work, we investigate whether LMMs can achieve embodied spatial action like human through a challenging scenario: goal-oriented navigation in urban 3D spaces. We first spend over 500 hours constructing a dataset comprising 5,037 high-quality goal-oriented navigation samples, with an emphasis on 3D vertical actions and rich urban semantic information. Then, we comprehensively assess 17 representative models, including non-reasoning LMMs, reasoning LMMs, agent-based methods, and vision-language-action models. Experiments show that current LMMs exhibit emerging action capabilities, yet remain far from human-level performance. Furthermore, we reveal an intriguing phenomenon: navigation errors do not accumulate linearly but instead diverge rapidly from the destination after a critical decision bifurcation. The limitations of LMMs are investigated by analyzing their behavior at these critical decision bifurcations. Finally, we experimentally explore four promising directions for improvement: geometric perception, cross-view understanding, spatial imagination, and long-term memory. The project is available at: this https URL.

---


### 92. [A Decomposition Perspective to Long-context Reasoning for LLMs](https://arxiv.org/abs/2604.07981)

**<font color=#1a73e8>作者：</font>** Yanling Xiao, Huaibing Xie, Guoliang Zhao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context reasoning is essential for complex real-world applications, yet remains a significant challenge for Large Language Models (LLMs). Despite the rapid evolution in long-context reasoning, current research often overlooks the internal complexity of the long-context reasoning task itself. In this paper, we move beyond this holistic view and decompose long-context reasoning into a set of fundamental atomic skills, and we then automatically synthesize a suite of pseudo datasets, each explicitly targeting a specific atomic skill. Our empirical analysis confirms that proficiency in these atomic skills is strongly correlated with general long-text reasoning performance. Building on this insight, we employ reinforcement learning on these pseudo datasets to sharpen the model's atomic skills, in the hope of boosting its general long-context reasoning ability. Extensive experiments across multiple benchmarks demonstrate the effectiveness of our approach: it outperforms a strong baseline by an average margin of 7.7\% (improving from 46.3\% to 54.0\%) across Loogle, Loong, LongBench-v2, BrowscompLong, Ruler-qa2, and MRCR.

---


### 93. [Rag Performance Prediction for Question Answering](https://arxiv.org/abs/2604.07985)

**<font color=#1a73e8>作者：</font>** Or Dado, David Carmel. Oren Kurland  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We address the task of predicting the gain of using RAG (retrieval augmented generation) for question answering with respect to not using it. We study the performance of a few pre-retrieval and post-retrieval predictors originally devised for ad hoc retrieval. We also study a few post-generation predictors, one of which is novel to this study and posts the best prediction quality. Our results show that the most effective prediction approach is a novel supervised predictor that explicitly models the semantic relationships among the question, retrieved passages, and the generated answer.

---


### 94. [MotionScape: A Large-Scale Real-World Highly Dynamic UAV Video Dataset for World Models](https://arxiv.org/abs/2604.07991)

**<font color=#1a73e8>作者：</font>** Zile Guo, Zhan Chen, Enze Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in world models have demonstrated strong capabilities in simulating physical reality, making them an increasingly important foundation for embodied intelligence. For UAV agents in particular, accurate prediction of complex 3D dynamics is essential for autonomous navigation and robust decision-making in unconstrained environments. However, under the highly dynamic camera trajectories typical of UAV views, existing world models often struggle to maintain spatiotemporal physical consistency. A key reason lies in the distribution bias of current training data: most existing datasets exhibit restricted 2.5D motion patterns, such as ground-constrained autonomous driving scenes or relatively smooth human-centric egocentric videos, and therefore lack realistic high-dynamic 6-DoF UAV motion priors. To address this gap, we present MotionScape, a large-scale real-world UAV-view video dataset with highly dynamic motion for world modeling. MotionScape contains over 30 hours of 4K UAV-view videos, totaling more than 4.5M frames. This novel dataset features semantically and geometrically aligned training samples, where diverse real-world UAV videos are tightly coupled with accurate 6-DoF camera trajectories and fine-grained natural language descriptions. To build the dataset, we develop an automated multi-stage processing pipeline that integrates CLIP-based relevance filtering, temporal segmentation, robust visual SLAM for trajectory recovery, and large-language-model-driven semantic annotation. Extensive experiments show that incorporating such semantically and geometrically aligned annotations effectively improves the ability of existing world models to simulate complex 3D dynamics and handle large viewpoint shifts, thereby benefiting decision-making and planning for UAV agents in complex environments. The dataset is publicly available at this https URL

---


### 95. [Few-Shot Incremental 3D Object Detection in Dynamic Indoor Environments](https://arxiv.org/abs/2604.07997)

**<font color=#1a73e8>作者：</font>** Yun Zhu, Jianjun Qian, Jian Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Incremental 3D object perception is a critical step toward embodied intelligence in dynamic indoor environments. However, existing incremental 3D detection methods rely on extensive annotations of novel classes for satisfactory performance. To address this limitation, we propose FI3Det, a Few-shot Incremental 3D Detection framework that enables efficient 3D perception with only a few novel samples by leveraging vision-language models (VLMs) to learn knowledge of unseen categories. FI3Det introduces a VLM-guided unknown object learning module in the base stage to enhance perception of unseen categories. Specifically, it employs VLMs to mine unknown objects and extract comprehensive representations, including 2D semantic features and class-agnostic 3D bounding boxes. To mitigate noise in these representations, a weighting mechanism is further designed to re-weight the contributions of point- and box-level features based on their spatial locations and feature consistency within each box. Moreover, FI3Det proposes a gated multimodal prototype imprinting module, where category prototypes are constructed from aligned 2D semantic and 3D geometric features to compute classification scores, which are then fused via a multimodal gating mechanism for novel object detection. As the first framework for few-shot incremental 3D object detection, we establish both batch and sequential evaluation settings on two datasets, ScanNet V2 and SUN RGB-D, where FI3Det achieves strong and consistent improvements over baseline methods. Code is available at this https URL.

---


### 96. [Bridging Time and Space: Decoupled Spatio-Temporal Alignment for Video Grounding](https://arxiv.org/abs/2604.08014)

**<font color=#1a73e8>作者：</font>** Xuezhen Tu, Jingyu Wu, Fangyu Kang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatio-Temporal Video Grounding requires jointly localizing target objects across both temporal and spatial dimensions based on natural language queries, posing fundamental challenges for existing Multimodal Large Language Models (MLLMs). We identify two core challenges: \textit{entangled spatio-temporal alignment}, arising from coupling two heterogeneous sub-tasks within the same autoregressive output space, and \textit{dual-domain visual token redundancy}, where target objects exhibit simultaneous temporal and spatial sparsity, rendering the overwhelming majority of visual tokens irrelevant to the grounding query. To address these, we propose \textbf{Bridge-STG}, an end-to-end framework that decouples temporal and spatial localization while maintaining semantic coherence. While decoupling is the natural solution to this entanglement, it risks creating a semantic gap between the temporal MLLM and the spatial decoder. Bridge-STG resolves this through two pivotal designs: the \textbf{Spatio-Temporal Semantic Bridging (STSB)} mechanism with Explicit Temporal Alignment (ETA) distills the MLLM's temporal reasoning context into enriched bridging queries as a robust semantic interface; and the \textbf{Query-Guided Spatial Localization (QGSL)} module leverages these queries to drive a purpose-built spatial decoder with multi-layer interactive queries and positive/negative frame sampling, jointly eliminating dual-domain visual token redundancy. Extensive experiments across multiple benchmarks demonstrate that Bridge-STG achieves state-of-the-art performance among MLLM-based methods. Bridge-STG improves average m\_vIoU from $26.4$ to $34.3$ on VidSTG and demonstrates strong cross-task transfer across various fine-grained video understanding tasks under a unified multi-task training regime.

---


### 97. [Wiring the 'Why': A Unified Taxonomy and Survey of Abductive Reasoning in LLMs](https://arxiv.org/abs/2604.08016)

**<font color=#1a73e8>作者：</font>** Moein Salimi, Shaygan Adim, Danial Parnian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Regardless of its foundational role in human discovery and sense-making, abductive reasoning--the inference of the most plausible explanation for an observation--has been relatively underexplored in Large Language Models (LLMs). Despite the rapid advancement of LLMs, the exploration of abductive reasoning and its diverse facets has thus far been disjointed rather than cohesive. This paper presents the first survey of abductive reasoning in LLMs, tracing its trajectory from philosophical foundations to contemporary AI implementations. To address the widespread conceptual confusion and disjointed task definitions prevalent in the field, we establish a unified two-stage definition that formally categorizes prior work. This definition disentangles abduction into \textit{Hypothesis Generation}, where models bridge epistemic gaps to produce candidate explanations, and \textit{Hypothesis Selection}, where the generated candidates are evaluated and the most plausible explanation is chosen. Building upon this foundation, we present a comprehensive taxonomy of the literature, categorizing prior work based on their abductive tasks, datasets, underlying methodologies, and evaluation strategies. In order to ground our framework empirically, we conduct a compact benchmark study of current LLMs on abductive tasks, together with targeted comparative analyses across model sizes, model families, evaluation styles, and the distinct generation-versus-selection task typologies. Moreover, by synthesizing recent empirical results, we examine how LLM performance on abductive reasoning relates to deductive and inductive tasks, providing insights into their broader reasoning capabilities. Our analysis reveals critical gaps in current approaches--from static benchmark design and narrow domain coverage to narrow training frameworks and limited mechanistic understanding of abductive processes...

---


### 98. [IoT-Brain: Grounding LLMs for Semantic-Spatial Sensor Scheduling](https://arxiv.org/abs/2604.08033)

**<font color=#1a73e8>作者：</font>** Zhaomeng Zhou, Lan Zhang, Junyang Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Intelligent systems powered by large-scale sensor networks are shifting from predefined monitoring to intent-driven operation, revealing a critical Semantic-to-Physical Mapping Gap. While large language models (LLMs) excel at semantic understanding, existing perception-centric pipelines operate retrospectively, overlooking the fundamental decision of what to sense and when. We formalize this proactive decision as Semantic-Spatial Sensor Scheduling (S3) and demonstrate that direct LLM planning is unreliable due to inherent gaps in representation, reasoning, and optimization. To bridge these gaps, we introduce the Spatial Trajectory Graph (STG), a neuro-symbolic paradigm governed by a verify-before-commit discipline that transforms open-ended planning into a verifiable graph optimization problem. Based on STG, we implement IoT-Brain, a concrete system embodiment, and construct TopoSense-Bench, a campus-scale benchmark with 5,250 natural-language queries across 2,510 cameras. Evaluations show that IoT-Brain boosts task success rate by 37.6% over the strongest search-intensive methods while running nearly 2 times faster and using 6.6 times fewer prompt tokens. In real-world deployment, it approaches the reliability upper bound while reducing 4.1 times network bandwidth, providing a foundational framework for LLMs to interact with the physical world with unprecedented reliability and efficiency.

---


### 99. [LINE: LLM-based Iterative Neuron Explanations for Vision Models](https://arxiv.org/abs/2604.08039)

**<font color=#1a73e8>作者：</font>** Vladimir Zaigrajew, Michał Piechota, Gaspar Sekula 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interpreting the concepts encoded by individual neurons in deep neural networks is a crucial step towards understanding their complex decision-making processes and ensuring AI safety. Despite recent progress in neuron labeling, existing methods often limit the search space to predefined concept vocabularies or produce overly specific descriptions that fail to capture higher-order, global concepts. We introduce LINE, a novel, training-free iterative approach tailored for open-vocabulary concept labeling in vision models. Operating in a strictly black-box setting, LINE leverages a large language model and a text-to-image generator to iteratively propose and refine concepts in a closed loop, guided by activation history. We demonstrate that LINE achieves state-of-the-art performance across multiple model architectures, yielding AUC improvements of up to 0.18 on ImageNet and 0.05 on Places365, while discovering, on average, 29% of new concepts missed by massive predefined vocabularies. Beyond identifying the top concept, LINE provides a complete generation history, which enables polysemanticity evaluation and produces supporting visual explanations that rival gradient-dependent activation maximization methods.

---


### 100. [3DrawAgent: Teaching LLM to Draw in 3D with Early Contrastive Experience](https://arxiv.org/abs/2604.08042)

**<font color=#1a73e8>作者：</font>** Hongcan Xiao, Xinyue Xiao, Yilin Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sketching in 3D space enables expressive reasoning about shape, structure, and spatial relationships, yet generating 3D sketches through natural language remains a major challenge. In this work, we introduce 3DrawAgent, a training-free, language-driven framework for 3D sketch generation that leverages large language models (LLMs) to sequentially draw 3D Bezier curves under geometric feedback. Unlike prior 2D sketch agents, our method introduces a relative experience optimization strategy that adapts the recently proposed Group Reward Policy Optimization (GRPO) paradigm. Instead of relying on explicit ground-truth supervision, we construct pairwise comparisons among generated sketches, with each pair consisting of a relatively better and a worse result based on CLIP-based perceptual rewards and LLM-based fine-grained qualitative assessment. These experiences are then used to iteratively refine the prior knowledge of 3D drawing, enabling black-box reinforcement of the model's 3D awareness. This design allows our model to self-improve its spatial understanding and drawing quality without parameter updates. Experiments show that 3DrawAgent can generate complex and coherent 3D Bezier sketches from diverse textual prompts, exhibit emergent geometric reasoning, and generalize to novel shapes, establishing a new paradigm for advancing the field of training-free 3D sketch intelligence.

---


### 101. [Adapting Foundation Models for Annotation-Efficient Adnexal Mass Segmentation in Cine Images](https://arxiv.org/abs/2604.08045)

**<font color=#1a73e8>作者：</font>** Francesca Fati, Alberto Rota, Adriana V. Gregory 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adnexal mass evaluation via ultrasound is a challenging clinical task, often hindered by subjective interpretation and significant inter-observer variability. While automated segmentation is a foundational step for quantitative risk assessment, traditional fully supervised convolutional architectures frequently require large amounts of pixel-level annotations and struggle with domain shifts common in medical imaging. In this work, we propose a label-efficient segmentation framework that leverages the robust semantic priors of a pretrained DINOv3 foundational vision transformer backbone. By integrating this backbone with a Dense Prediction Transformer (DPT)-style decoder, our model hierarchically reassembles multi-scale features to combine global semantic representations with fine-grained spatial details. Evaluated on a clinical dataset of 7,777 annotated frames from 112 patients, our method achieves state-of-the-art performance compared to established fully supervised baselines, including U-Net, U-Net++, DeepLabV3, and MAnet. Specifically, we obtain a Dice score of 0.945 and improved boundary adherence, reducing the 95th-percentile Hausdorff Distance by 11.4% relative to the strongest convolutional baseline. Furthermore, we conduct an extensive efficiency analysis demonstrating that our DINOv3-based approach retains significantly higher performance under data starvation regimes, maintaining strong results even when trained on only 25% of the data. These results suggest that leveraging large-scale self-supervised foundations provides a promising and data-efficient solution for medical image segmentation in data-constrained clinical environments. Project Repository: this https URL

---


### 102. [Guaranteeing Knowledge Integration with Joint Decoding for Retrieval-Augmented Generation](https://arxiv.org/abs/2604.08046)

**<font color=#1a73e8>作者：</font>** Zhengyi Zhao, Shubo Zhang, Zezhong Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) significantly enhances Large Language Models (LLMs) by providing access to external knowledge. However, current research primarily focuses on retrieval quality, often overlooking the critical ''integration bottleneck'': even when relevant documents are retrieved, LLMs frequently fail to utilize them effectively due to conflicts with their internal parametric knowledge. In this paper, we argue that implicitly resolving this conflict in a single generation pass is suboptimal. We introduce GuarantRAG, a framework that explicitly decouples reasoning from evidence integration. First, we generate an ''Inner-Answer'' based solely on parametric knowledge to capture the model's reasoning flow. Second, to guarantee faithful evidence extraction, we generate a ''Refer-Answer'' using a novel Contrastive DPO objective. This objective treats the parametric Inner-Answer as a negative constraint and the retrieved documents as positive ground truth, forcing the model to suppress internal hallucinations in favor of external evidence during this phase. Finally, rather than naive concatenation or using the DPO trained model directly, we propose a joint decoding mechanism that dynamically fuses the logical coherence of the Inner-Answer with the factual precision of the Refer-Answer at the token level. Experiments on five QA benchmarks demonstrate that GuarantRAG improves accuracy by up to 12.1% and reduces hallucinations by 16.3% compared to standard and dynamic RAG baselines.

---


### 103. [ABMAMBA: Multimodal Large Language Model with Aligned Hierarchical Bidirectional Scan for Efficient Video Captioning](https://arxiv.org/abs/2604.08050)

**<font color=#1a73e8>作者：</font>** Daichi Yashima, Shuhei Kurita, Yusuke Oda 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this study, we focus on video captioning by fully open multimodal large language models (MLLMs). The comprehension of visual sequences is challenging because of their intricate temporal dependencies and substantial sequence length. The core attention mechanisms of existing Transformer-based approaches scale quadratically with the sequence length, making them computationally prohibitive. To address these limitations, we propose Aligned Hierarchical Bidirectional Scan Mamba (ABMamba), a fully open MLLM with linear computational complexity that enables the scalable processing of video sequences. ABMamba extends Deep State Space Models as its language backbone, replacing the costly quadratic attention mechanisms, and employs a novel Aligned Hierarchical Bidirectional Scan module that processes videos across multiple temporal resolutions. On standard video captioning benchmarks such as VATEX and MSR-VTT, ABMamba demonstrates competitive performance compared to typical MLLMs while achieving approximately three times higher throughput.

---


### 104. [From Gaze to Guidance: Interpreting and Adapting to Users' Cognitive Needs with Multimodal Gaze-Aware AI Assistants](https://arxiv.org/abs/2604.08062)

**<font color=#1a73e8>作者：</font>** Valdemar Danry, Javier Hernandez, Andrew Wilson 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Current LLM assistants are powerful at answering questions, but they have limited access to the behavioral context that reveals when and where a user is struggling. We present a gaze-grounded multimodal LLM assistant that uses egocentric video with gaze overlays to identify likely points of difficulty and target follow-up retrospective assistance. We instantiate this vision in a controlled study (n=36) comparing the gaze-aware AI assistant to a text-only LLM assistant. Compared to a conventional LLM assistant, the gaze-aware assistant was rated as significantly more accurate and personalized in its assessments of users' reading behavior and significantly improved people's ability to recall information. Users spoke significantly fewer words with the gaze-aware assistant, indicating more efficient interactions. Qualitative results underscored both perceived benefits in comprehension and challenges when interpretations of gaze behaviors were inaccurate. Our findings suggest that gaze-aware LLM assistants can reason about cognitive needs to improve cognitive outcomes of users.

---


### 105. [EEG2Vision: A Multimodal EEG-Based Framework for 2D Visual Reconstruction in Cognitive Neuroscience](https://arxiv.org/abs/2604.08063)

**<font color=#1a73e8>作者：</font>** Emanuele Balloni, Emanuele Frontoni, Chiara Matti 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing visual stimuli from non-invasive electroencephalography (EEG) remains challenging due to its low spatial resolution and high noise, particularly under realistic low-density electrode configurations. To address this, we present EEG2Vision, a modular, end-to-end EEG-to-image framework that systematically evaluates reconstruction performance across different EEG resolutions (128, 64, 32, and 24 channels) and enhances visual quality through a prompt-guided post-reconstruction boosting mechanism. Starting from EEG-conditioned diffusion reconstruction, the boosting stage uses a multimodal large language model to extract semantic descriptions and leverages image-to-image diffusion to refine geometry and perceptual coherence while preserving EEG-grounded structure. Our experiments show that semantic decoding accuracy degrades significantly with channel reduction (e.g., 50-way Top-1 Acc from 89% to 38%), while reconstruction quality slight decreases (e.g., FID from 76.77 to 80.51). The proposed boosting consistently improves perceptual metrics across all configurations, achieving up to 9.71% IS gains in low-channel settings. A user study confirms the clear perceptual preference for boosted reconstructions. The proposed approach significantly boosts the feasibility of real-time brain-2-image applications using low-resolution EEG devices, potentially unlocking this type of applications outside laboratory settings.

---


### 106. [ImplicitMemBench: Measuring Unconscious Behavioral Adaptation in Large Language Models](https://arxiv.org/abs/2604.08064)

**<font color=#1a73e8>作者：</font>** Chonghan Qin, Xiachong Feng, Weitao Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing memory benchmarks for LLM agents evaluate explicit recall of facts, yet overlook implicit memory where experience becomes automated behavior without conscious retrieval. This gap is critical: effective assistants must automatically apply learned procedures or avoid failed actions without explicit reminders. We introduce ImplicitMemBench, the first systematic benchmark evaluating implicit memory through three cognitively grounded constructs drawn from standard cognitive-science accounts of non-declarative memory: Procedural Memory (one-shot skill acquisition after interference), Priming (theme-driven bias via paired experimental/control instances), and Classical Conditioning (Conditioned Stimulus--Unconditioned Stimulus (CS--US) associations shaping first decisions). Our 300-item suite employs a unified Learning/Priming-Interfere-Test protocol with first-attempt scoring. Evaluation of 17 models reveals severe limitations: no model exceeds 66% overall, with top performers DeepSeek-R1 (65.3%), Qwen3-32B (64.1%), and GPT-5 (63.0%) far below human baselines. Analysis uncovers dramatic asymmetries (inhibition 17.6% vs. preference 75.0%) and universal bottlenecks requiring architectural innovations beyond parameter scaling. ImplicitMemBench reframes evaluation from "what agents recall" to "what they automatically enact".

---


### 107. [Multimodal Latent Reasoning via Predictive Embeddings](https://arxiv.org/abs/2604.08065)

**<font color=#1a73e8>作者：</font>** Ashutosh Adhikari, Mirella Lapata  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tool-augmented multimodal reasoning enables visual language models (VLMs) to improve perception by interacting with external tools (e.g., cropping, depth estimation). However, such approaches incur substantial inference overhead, require specialized supervision, and are prone to erroneous tool calls. We propose Pearl (Predictive Embedding Alignment for Reasoning in Latent space), a JEPA-inspired framework that learns from expert tool-use trajectories entirely in the latent space, eliminating the need for explicit tool invocation at inference time. Unlike reconstruction-based latent reasoning methods, which autoregressively generate latent tokens and suffer from training-inference mismatch and limited support for multi-step tool use, Pearl directly learns predictive embeddings from multimodal trajectories while preserving the standard vision-language generation pipeline: it is model-agnostic, simple to train, and naturally supports trajectories with multiple tool calls. Experiments across multiple perception benchmarks show that Pearl matches or outperforms standard supervised fine-tuning and reconstruction-based latent reasoning approaches. Furthermore, we provide empirical evidence that reconstruction-based methods primarily learn embeddings rather than image edits in latent space, motivating predictive embedding learning as a more principled alternative.

---


### 108. [Brain3D: EEG-to-3D Decoding of Visual Representations via Multimodal Reasoning](https://arxiv.org/abs/2604.08068)

**<font color=#1a73e8>作者：</font>** Emanuele Balloni, Emanuele Frontoni, Chiara Matti 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Decoding visual information from electroencephalography (EEG) has recently achieved promising results, primarily focusing on reconstructing two-dimensional (2D) images from brain activity. However, the reconstruction of three-dimensional (3D) representations remains largely unexplored. This limits the geometric understanding and reduces the applicability of neural decoding in different contexts. To address this gap, we propose Brain3D, a multimodal architecture for EEG-to-3D reconstruction based on EEG-to-image decoding. It progressively transforms neural representations into the 3D domain using geometry-aware generative reasoning. Our pipeline first produces visually grounded images from EEG signals, then employs a multimodal large language model to extract structured 3D-aware descriptions, which guide a diffusion-based generation stage whose outputs are finally converted into coherent 3D meshes via a single-image-to-3D model. By decomposing the problem into structured stages, the proposed approach avoids direct EEG-to-3D mappings and enables scalable brain-driven 3D generation. We conduct a comprehensive evaluation comparing the reconstructed 3D outputs against the original visual stimuli, assessing both semantic alignment and geometric fidelity. Experimental results demonstrate strong performance of the proposed architecture, achieving up to 85.4% 10-way Top-1 EEG decoding accuracy and 0.648 CLIPScore, supporting the feasibility of multimodal EEG-driven 3D reconstruction.

---


### 109. [AtlasOCR: Building the First Open-Source Darija OCR Model with Vision Language Models](https://arxiv.org/abs/2604.08070)

**<font color=#1a73e8>作者：</font>** Imane Momayiz, Soufiane Ait Elaouad, Abdeljalil Elmajjodi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Darija, the Moroccan Arabic dialect, is rich in visual content yet lacks specialized Optical Character Recognition (OCR) tools. This paper introduces AtlasOCR, the first open-source Darija OCR model built by fine-tuning a 3B parameter Vision Language Model (VLM). We detail our comprehensive approach, from curating a unique Darija-specific dataset leveraging both synthetic generation with our OCRSmith library and carefully sourced real-world data, to implementing efficient fine-tuning strategies. We utilize QLoRA and Unsloth for parameter-efficient training of Qwen2.5-VL 3B and present comprehensive ablation studies optimizing key hyperparameters. Our evaluation on the newly curated AtlasOCRBench and the established KITAB-Bench demonstrates state-of-the-art performance, challenging larger models and highlighting AtlasOCR's robustness and generalization capabilities for both Darija and standard Arabic OCR tasks.

---


### 110. [DinoRADE: Full Spectral Radar-Camera Fusion with Vision Foundation Model Features for Multi-class Object Detection in Adverse Weather](https://arxiv.org/abs/2604.08074)

**<font color=#1a73e8>作者：</font>** Christof Leitgeb, Thomas Puchleitner, Max Peter Ronecker 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable and weather-robust perception systems are essential for safe autonomous driving and typically employ multi-modal sensor configurations to achieve comprehensive environmental awareness. While recent automotive FMCW Radar-based approaches achieved remarkable performance on detection tasks in adverse weather conditions, they exhibited limitations in resolving fine-grained spatial details particularly critical for detecting smaller and vulnerable road users (VRUs). Furthermore, existing research has not adequately addressed VRU detection in adverse weather datasets such as K-Radar. We present DinoRADE, a Radar-centered detection pipeline that processes dense Radar tensors and aggregates vision features around transformed reference points in the camera perspective via deformable cross-attention. Vision features are provided by a DINOv3 Vision Foundation Model. We present a comprehensive performance evaluation on the K-Radar dataset in all weather conditions and are among the first to report detection performance individually for five object classes. Additionally, we compare our method with existing single-class detection approaches and outperform recent Radar-camera approaches by 12.1%. The code is available under this https URL.

---


### 111. [Dual-Pool Token-Budget Routing for Cost-Efficient and Reliable LLM Serving](https://arxiv.org/abs/2604.08075)

**<font color=#1a73e8>作者：</font>** Xunzhuo Liu, Bowei He, Xue Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Production vLLM fleets typically provision each instance for the worst-case context length, leading to substantial KV-cache over-allocation and under-utilized concurrency. In practice, 80-95% of requests are short, yet are served under configurations optimized for long contexts, wasting 4-8$\times$ throughput capacity and triggering reliability issues such as OOM crashes, preemption, and request rejections. We identify a common root cause for these inefficiencies: configuration-traffic mismatch. We propose dual-pool token-budget routing, a lightweight dispatch mechanism that partitions a homogeneous fleet into two specialized pools: a high-throughput short-context pool and a high-capacity long-context pool. Each request is routed based on its estimated total token budget, computed using a per-category bytes-to-token ratio that is learned online via exponential moving average from usage.prompt_tokens feedback, eliminating the need for a tokenizer. We also develop a simple analytical model that predicts fleet-level cost savings from workload characteristics and measured throughput differences, enabling practitioners to estimate benefits prior to deployment. Evaluations on real-world traces from the Azure LLM Inference Dataset and LMSYS-Chat-1M, serving Llama-3-70B on A100 GPUs, show that our approach reduces GPU-hours by 31-42%, corresponding to \$2.86M annual savings at fleet scale, while lowering preemption rates by 5.4$\times$ and improving P99 TTFT by 6%. A case study with Qwen3-235B-A22B on AMD MI300X at 10,000 req/s projects \$15.4M in annual savings. The method incurs only O(1) dispatch overhead, adapts automatically to heterogeneous workloads, and composes seamlessly with existing optimizations such as PagedAttention, continuous batching, and prefill-decode disaggregation.

---


### 112. [Initialisation Determines the Basin: Efficient Codebook Optimisation for Extreme LLM Quantization](https://arxiv.org/abs/2604.08118)

**<font color=#1a73e8>作者：</font>** Ian W. Kennedy, Nafise Sadat Moosavi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Additive quantization enables extreme LLM compression with O(1) lookup-table dequantization, making it attractive for edge deployment. Yet at 2-bit precision, it often fails catastrophically, even with extensive search and finetuning. We show that the dominant bottleneck is codebook initialisation. Greedy sequential initialisation frequently places the model in poor optimisation regions that subsequent beam search and PV-tuning struggle to overcome. We analyse this behaviour through the representational ratio \r{ho} = N/KM, which characterises the relationship between weight groups and codebook capacity, and propose OA-EM, an output-aware EM initialisation method using Hessian-weighted Mahalanobis distance. Across compression rates, search budgets, and three architectures (Llama 3.2 3B, Llama 3.1 8B, Qwen 2.5 3B), OA-EM consistently produces better solutions after PV-tuning and dominates the quality-compute frontier. The severity of the bottleneck scales with \r{ho}: moderate at 3 bpp but extreme at 2 bpp, where poor initialisation can degrade perplexity by orders of magnitude. More broadly, our results highlight the importance of optimisation geometry in compressed model spaces, where initialisation can dominate subsequent search and fine-tuning.

---


### 113. [Small Vision-Language Models are Smart Compressors for Long Video Understanding](https://arxiv.org/abs/2604.08120)

**<font color=#1a73e8>作者：</font>** Junjie Fei, Jun Chen, Zechun Liu 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adapting Multimodal Large Language Models (MLLMs) for hour-long videos is bottlenecked by context limits. Dense visual streams saturate token budgets and exacerbate the lost-in-the-middle phenomenon. Existing heuristics, like sparse sampling or uniform pooling, blindly sacrifice fidelity by discarding decisive moments and wasting bandwidth on irrelevant backgrounds. We propose Tempo, an efficient query-aware framework compressing long videos for downstream understanding. Tempo leverages a Small Vision-Language Model (SVLM) as a local temporal compressor, casting token reduction as an early cross-modal distillation process to generate compact, intent-aligned representations in a single forward pass. To enforce strict budgets without breaking causality, we introduce Adaptive Token Allocation (ATA). Exploiting the SVLM's zero-shot relevance prior and semantic front-loading, ATA acts as a training-free $O(1)$ dynamic router. It allocates dense bandwidth to query-critical segments while compressing redundancies into minimal temporal anchors to maintain the global storyline. Extensive experiments show our 6B architecture achieves state-of-the-art performance with aggressive dynamic compression (0.5-16 tokens/frame). On the extreme-long LVBench (4101s), Tempo scores 52.3 under a strict 8K visual budget, outperforming GPT-4o and Gemini 1.5 Pro. Scaling to 2048 frames reaches 53.7. Crucially, Tempo compresses hour-long videos substantially below theoretical limits, proving true long-form video understanding relies on intent-driven efficiency rather than greedily padded context windows.

---


### 114. [Uni-ViGU: Towards Unified Video Generation and Understanding via A Diffusion-Based Video Generator](https://arxiv.org/abs/2604.08121)

**<font color=#1a73e8>作者：</font>** Luozheng Qin, Jia Gong, Qian Qiao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified multimodal models integrating visual understanding and generation face a fundamental challenge: visual generation incurs substantially higher computational costs than understanding, particularly for video. This imbalance motivates us to invert the conventional paradigm: rather than extending understanding-centric MLLMs to support generation, we propose Uni-ViGU, a framework that unifies video generation and understanding by extending a video generator as the foundation. We introduce a unified flow method that performs continuous flow matching for video and discrete flow matching for text within a single process, enabling coherent multimodal generation. We further propose a modality-driven MoE-based framework that augments Transformer blocks with lightweight layers for text generation while preserving generative priors. To repurpose generation knowledge for understanding, we design a bidirectional training mechanism with two stages: Knowledge Recall reconstructs input prompts to leverage learned text-video correspondences, while Capability Refinement fine-tunes on detailed captions to establish discriminative shared representations. Experiments demonstrate that Uni-ViGU achieves competitive performance on both video generation and understanding, validating generation-centric architectures as a scalable path toward unified multimodal intelligence. Project Page and Code: this https URL.

---


### 115. [Beyond Stochastic Exploration: What Makes Training Data Valuable for Agentic Search](https://arxiv.org/abs/2604.08124)

**<font color=#1a73e8>作者：</font>** Chuzhan Hao, Wenfeng Feng, Guochao Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has become an effective approach for advancing the reasoning capabilities of large language models (LLMs) through the strategic integration of external search engines. However, current RL-based search agents often rely on a process of stochastic exploration guided by carefully crafted outcome rewards, leading to inefficient reasoning trajectories and unstable training. To address these issues, we propose a novel framework, Hierarchical Experience (HiExp), to enhance the performance and training stability of search agents. Specifically, we extract empirical knowledge through contrastive analysis and a multi-level clustering mechanism, transforming raw reasoning trajectories into hierarchical experience knowledge. By leveraging experience-aligned training, we effectively regularize stochastic exploration, evolving it into a strategic and experience-driven search process. Extensive evaluations on multiple complex agentic search and mathematical reasoning benchmarks demonstrate that our approach not only achieves substantial performance gains but also exhibits strong cross-task and cross-algorithm generalization.

---


### 116. [PolySLGen: Online Multimodal Speaking-Listening Reaction Generation in Polyadic Interaction](https://arxiv.org/abs/2604.08125)

**<font color=#1a73e8>作者：</font>** Zhi-Yi Lin, Thomas Markhorst, Jouh Yeong Chew 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human-like multimodal reaction generation is essential for natural group interactions between humans and embodied AI. However, existing approaches are limited to single-modality or speaking-only responses in dyadic interactions, making them unsuitable for realistic social scenarios. Many also overlook nonverbal cues and complex dynamics of polyadic interactions, both critical for engagement and conversational coherence. In this work, we present PolySLGen, an online framework for Polyadic multimodal Speaking and Listening reaction Generation. Given past conversation and motion from all participants, PolySLGen generates a future speaking or listening reaction for a target participant, including speech, body motion, and speaking state score. To model group interactions effectively, we propose a pose fusion module and a social cue encoder that jointly aggregate motion and social signals from the group. Extensive experiments, along with quantitative and qualitative evaluations, show that PolySLGen produces contextually appropriate and temporally coherent multi-modal reactions, outperforming several adapted and state-of-the-art baselines in motion quality, motion-speech alignment, speaking state prediction, and human-perceived realism.

---


### 117. [LLM-Based Data Generation and Clinical Skills Evaluation for Low-Resource French OSCEs](https://arxiv.org/abs/2604.08126)

**<font color=#1a73e8>作者：</font>** Tian Huang, Tom Bourgeade, Irina Illina  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Objective Structured Clinical Examinations (OSCEs) are the standard method for assessing medical students' clinical and communication skills through structured patient interviews. In France, however, the organization of training sessions is limited by human and logistical constraints, restricting students' access to repeated practice and structured feedback. Recent advances in Natural Language Processing (NLP) and Large Language Models (LLMs) now offer the opportunity to automatically evaluate such medical interviews, thereby alleviating the need for human examiners during training. Yet, real French OSCE annotated transcripts remain extremely scarce, limiting reproducible research and reliable benchmarking. To address these challenges, we investigate the use of LLMs for both generating and evaluating French OSCE dialogues in a low-resource context. We introduce a controlled pipeline that produces synthetic doctor-patient interview transcripts guided by scenario-specific evaluation criteria, combining ideal and perturbed performances to simulate varying student skill levels. The resulting dialogues are automatically silver-labeled through an LLM-assisted framework supporting adjustable evaluation strictness. Benchmarking multiple open-source and proprietary LLMs shows that mid-size models ($\le$32B parameters) achieve accuracies comparable to GPT-4o ($\sim$90\%) on synthetic data, highlighting the feasibility of locally deployable, privacy-preserving evaluation systems for medical education.

---


### 118. [Alloc-MoE: Budget-Aware Expert Activation Allocation for Efficient Mixture-of-Experts Inference](https://arxiv.org/abs/2604.08133)

**<font color=#1a73e8>作者：</font>** Baihui Liu, Kaiyuan Tian, Wei Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) has become a dominant architecture for scaling large language models due to their sparse activation mechanism. However, the substantial number of expert activations creates a critical latency bottleneck during inference, especially in resource-constrained deployment scenarios. Existing approaches that reduce expert activations potentially lead to severe model performance degradation. In this work, we introduce the concept of \emph{activation budget} as a constraint on the number of expert activations and propose Alloc-MoE, a unified framework that optimizes budget allocation coordinately at both the layer and token levels to minimize performance degradation. At the layer level, we introduce Alloc-L, which leverages sensitivity profiling and dynamic programming to determine the optimal allocation of expert activations across layers. At the token level, we propose Alloc-T, which dynamically redistributes activations based on routing scores, optimizing budget allocation without increasing latency. Extensive experiments across multiple MoE models demonstrate that Alloc-MoE maintains model performance under a constrained activation budget. Especially, Alloc-MoE achieves $1.15\times$ prefill and $1.34\times$ decode speedups on DeepSeek-V2-Lite at half of the original budget.

---


### 119. [Activation Steering for Aligned Open-ended Generation without Sacrificing Coherence](https://arxiv.org/abs/2604.08169)

**<font color=#1a73e8>作者：</font>** Niklas Herbster, Martin Zborowski, Alberto Tosato 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Alignment in LLMs is more brittle than commonly assumed: misalignment can be triggered by adversarial prompts, benign fine-tuning, emergent misalignment, and goal misgeneralization. Recent evidence suggests that some misalignment behaviors are encoded as linear structure in activation space, making it tractable via steering, while safety alignment has been shown to govern the first few output tokens primarily, leaving subsequent generation unguarded. These findings motivate activation steering as a lightweight runtime defense that continuously corrects misaligned activations throughout generation. We evaluate three methods: Steer-With-Fixed-Coeff (SwFC), which applies uniform additive steering, and two novel projection-aware methods, Steer-to-Target-Projection (StTP) and Steer-to-Mirror-Projection (StMP), that use a logistic regression decision boundary to selectively intervene only on tokens whose activations fall below distributional thresholds. Using malicious system prompts as a controlled proxy for misalignment, we evaluate under two threat models (dishonesty and dismissiveness) and two architectures (Llama-3.3-70B-Instruct, Qwen3-32B). All methods substantially recover target traits (honesty and compassion) while preserving coherence. StTP and StMP better maintain general capabilities (MMLU, MT-Bench, AlpacaEval) and produce less repetition in multi-turn conversations.

---


### 120. [OceanMAE: A Foundation Model for Ocean Remote Sensing](https://arxiv.org/abs/2604.08171)

**<font color=#1a73e8>作者：</font>** Viola-Joanna Stamer, Panagiotis Agrafiotis, Behnood Rasti 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate ocean mapping is essential for applications such as bathymetry estimation, seabed characterization, marine litter detection, and ecosystem monitoring. However, ocean remote sensing (RS) remains constrained by limited labeled data and by the reduced transferability of models pre-trained mainly on land-dominated Earth observation imagery. In this paper, we propose OceanMAE, an ocean-specific masked autoencoder that extends standard MAE pre-training by integrating multispectral Sentinel-2 observations with physically meaningful ocean descriptors during self-supervised learning. By incorporating these auxiliary ocean features, OceanMAE is designed to learn more informative and ocean-aware latent representations from large- scale unlabeled data. To transfer these representations to downstream applications, we further employ a modified UNet-based framework for marine segmentation and bathymetry estimation. Pre-trained on the Hydro dataset, OceanMAE is evaluated on MADOS and MARIDA for marine pollutant and debris segmentation, and on MagicBathyNet for bathymetry regression. The experiments show that OceanMAE yields the strongest gains on marine segmentation, while bathymetry benefits are competitive and task-dependent. In addition, an ablation against a standard MAE on MARIDA indicates that incorporating auxiliary ocean descriptors during pre-training improves downstream segmentation quality. These findings highlight the value of physically informed and domain-aligned self-supervised pre- training for ocean RS. Code and weights are publicly available at this https URL.

---


### 121. [On the Global Photometric Alignment for Low-Level Vision](https://arxiv.org/abs/2604.08172)

**<font color=#1a73e8>作者：</font>** Mingjia Li, Tianle Du, Hainuo Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Supervised low-level vision models rely on pixel-wise losses against paired references, yet paired training sets exhibit per-pair photometric inconsistency, say, different image pairs demand different global brightness, color, or white-balance mappings. This inconsistency enters through task-intrinsic photometric transfer (e.g., low-light enhancement) or unintended acquisition shifts (e.g., de-raining), and in either case causes an optimization pathology. Standard reconstruction losses allocate disproportionate gradient budget to conflicting per-pair photometric targets, crowding out content restoration. In this paper, we investigate this issue and prove that, under least-squares decomposition, the photometric and structural components of the prediction-target residual are orthogonal, and that the spatially dense photometric component dominates the gradient energy. Motivated by this analysis, we propose Photometric Alignment Loss (PAL). This flexible supervision objective discounts nuisance photometric discrepancy via closed-form affine color alignment while preserving restoration-relevant supervision, requiring only covariance statistics and tiny matrix inversion with negligible overhead. Across 6 tasks, 16 datasets, and 16 architectures, PAL consistently improves metrics and generalization. The implementation is in the appendix.

---


### 122. [Aligning Agents via Planning: A Benchmark for Trajectory-Level Reward Modeling](https://arxiv.org/abs/2604.08178)

**<font color=#1a73e8>作者：</font>** Jiaxuan Wang, Yulan Hu, Wenjin Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In classical Reinforcement Learning from Human Feedback (RLHF), Reward Models (RMs) serve as the fundamental signal provider for model alignment. As Large Language Models evolve into agentic systems capable of autonomous tool invocation and complex reasoning, the paradigm of reward modeling faces unprecedented challenges--most notably, the lack of benchmarks specifically designed to assess RM capabilities within tool-integrated environments. To address this gap, we present Plan-RewardBench, a trajectory-level preference benchmark designed to evaluate how well judges distinguish preferred versus distractor agent trajectories in complex tool-using scenarios. Plan-RewardBench covers four representative task families -- (i) Safety Refusal, (ii) Tool-Irrelevance / Unavailability, (iii) Complex Planning, and (iv) Robust Error Recovery -- comprising validated positive trajectories and confusable hard negatives constructed via multi-model natural rollouts, rule-based perturbations, and minimal-edit LLM perturbations. We benchmark representative RMs (generative, discriminative, and LLM-as-Judge) under a unified pairwise protocol, reporting accuracy trends across varying trajectory lengths and task categories. Furthermore, we provide diagnostic analyses of prevalent failure modes. Our results reveal that all three evaluator families face substantial challenges, with performance degrading sharply on long-horizon trajectories, underscoring the necessity for specialized training in agentic, trajectory-level reward modeling. Ultimately, Plan-RewardBench aims to serve as both a practical evaluation suite and a reusable blueprint for constructing agentic planning preference data.

---


### 123. [MedVR: Annotation-Free Medical Visual Reasoning via Agentic Reinforcement Learning](https://arxiv.org/abs/2604.08203)

**<font color=#1a73e8>作者：</font>** Zheng Jiang, Heng Guo, Chengyu Fang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical Vision-Language Models (VLMs) hold immense promise for complex clinical tasks, but their reasoning capabilities are often constrained by text-only paradigms that fail to ground inferences in visual evidence. This limitation not only curtails performance on tasks requiring fine-grained visual analysis but also introduces risks of visual hallucination in safety-critical applications. Thus, we introduce MedVR, a novel reinforcement learning framework that enables annotation-free visual reasoning for medical VLMs. Its core innovation lies in two synergistic mechanisms: Entropy-guided Visual Regrounding (EVR) uses model uncertainty to direct exploration, while Consensus-based Credit Assignment (CCA) distills pseudo-supervision from rollout agreement. Without any human annotations for intermediate steps, MedVR achieves state-of-the-art performance on diverse public medical VQA benchmarks, significantly outperforming existing models. By learning to reason directly with visual evidence, MedVR promotes the robustness and transparency essential for accelerating the clinical deployment of medical AI.

---


### 124. ["Theater of Mind" for LLMs: A Cognitive Architecture Based on Global Workspace Theory](https://arxiv.org/abs/2604.08206)

**<font color=#1a73e8>作者：</font>** Wenlong Shang  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Modern Large Language Models (LLMs) operate fundamentally as Bounded-Input Bounded-Output (BIBO) systems. They remain in a passive state until explicitly prompted, computing localized responses without intrinsic temporal continuity. While effective for isolated tasks, this reactive paradigm presents a critical bottleneck for engineering autonomous artificial intelligence. Current multi-agent frameworks attempt to distribute cognitive load but frequently rely on static memory pools and passive message passing, which inevitably leads to cognitive stagnation and homogeneous deadlocks during extended execution. To address this structural limitation, we propose Global Workspace Agents (GWA), a cognitive architecture inspired by Global Workspace Theory. GWA transitions multi-agent coordination from a passive data structure to an active, event-driven discrete dynamical system. By coupling a central broadcast hub with a heterogeneous swarm of functionally constrained agents, the system maintains a continuous cognitive cycle. Furthermore, we introduce an entropy-based intrinsic drive mechanism that mathematically quantifies semantic diversity, dynamically regulating generation temperature to autonomously break reasoning deadlocks. Coupled with a dual-layer memory bifurcation strategy to ensure long-term cognitive continuity, GWA provides a robust, reproducible engineering framework for sustained, self-directed LLM agency.

---


### 125. [Vision-Language Foundation Models for Comprehensive Automated Pavement Condition Assessment](https://arxiv.org/abs/2604.08212)

**<font color=#1a73e8>作者：</font>** Blessing Agyei Kyem, Joshua Kofi Asamoah, Anthony Dontoh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> General-purpose vision-language models demonstrate strong performance in everyday domains but struggle with specialized technical fields requiring precise terminology, structured reasoning, and adherence to engineering standards. This work addresses whether domain-specific instruction tuning can enable comprehensive pavement condition assessment through vision-language models. PaveInstruct, a dataset containing 278,889 image-instruction-response pairs spanning 32 task types, was created by unifying annotations from nine heterogeneous pavement datasets. PaveGPT, a pavement foundation model trained on this dataset, was evaluated against state-of-the-art vision-language models across perception, understanding, and reasoning tasks. Instruction tuning transformed model capabilities, achieving improvements exceeding 20% in spatial grounding, reasoning, and generation tasks while producing ASTM D6433-compliant outputs. These results enable transportation agencies to deploy unified conversational assessment tools that replace multiple specialized systems, simplifying workflows and reducing technical expertise requirements. The approach establishes a pathway for developing instruction-driven AI systems across infrastructure domains including bridge inspection, railway maintenance, and building condition assessment.

---


### 126. [EditCaption: Human-Aligned Instruction Synthesis for Image Editing via Supervised Fine-Tuning and Direct Preference Optimization](https://arxiv.org/abs/2604.08213)

**<font color=#1a73e8>作者：</font>** Xiangyuan Wang, Honghao Cai, Yunhao Bai 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-quality training triplets (source-target image pairs with precise editing instructions) are a critical bottleneck for scaling instruction-guided image editing models. Vision-language models (VLMs) are widely used for automated instruction synthesis, but we identify three systematic failure modes in image-pair settings: orientation inconsistency (e.g., left/right confusion), viewpoint ambiguity, and insufficient fine-grained attribute description. Human evaluation shows that over 47% of instructions from strong baseline VLMs contain critical errors unusable for downstream training. We propose EditCaption, a scalable two-stage post-training pipeline for VLM-based instruction synthesis. Stage 1 builds a 100K supervised fine-tuning (SFT) dataset by combining GLM automatic annotation, EditScore-based filtering, and human refinement for spatial, directional, and attribute-level accuracy. Stage 2 collects 10K human preference pairs targeting the three failure modes and applies direct preference optimization (DPO) for alignment beyond SFT alone. On Eval-400, ByteMorph-Bench, and HQ-Edit, fine-tuned Qwen3-VL models outperform open-source baselines; the 235B model reaches 4.712 on Eval-400 (vs. Gemini-3-Pro 4.706, GPT-4.1 4.220, Kimi-K2.5 4.111) and 4.588 on ByteMorph-Bench (vs. Gemini-3-Pro 4.522, GPT-4.1 3.412). Human evaluation shows critical errors falling from 47.75% to 23% and correctness rising from 41.75% to 66%. The work offers a practical path to scalable, human-aligned instruction synthesis for image editing data.

---


### 127. [MemCoT: Test-Time Scaling through Memory-Driven Chain-of-Thought](https://arxiv.org/abs/2604.08216)

**<font color=#1a73e8>作者：</font>** Haodong Lei, Junming Liu, Yirong Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) still suffer from severe hallucinations and catastrophic forgetting during causal reasoning over massive, fragmented long contexts. Existing memory mechanisms typically treat retrieval as a static, single-step passive matching process, leading to severe semantic dilution and contextual fragmentation. To overcome these fundamental bottlenecks, we propose MemCoT, a test-time memory scaling framework that redefines the reasoning process by transforming long-context reasoning into an iterative, stateful information search. MemCoT introduces a multi-view long-term memory perception module that enables Zoom-In evidence localization and Zoom-Out contextual expansion, allowing the model to first identify where relevant evidence resides and then reconstruct the surrounding causal structure necessary for reasoning. In addition, MemCoT employs a task-conditioned dual short-term memory system composed of semantic state memory and episodic trajectory memory. This short-term memory records historical search decisions and dynamically guides query decomposition and pruning across iterations. Empirical evaluations demonstrate that MemCoT establishes a state-of-the-art performance. Empowered by MemCoT, several open- and closed-source models achieve SOTA performance on the LoCoMo benchmark and LongMemEval-S benchmark.

---


### 128. [Grounding Clinical AI Competency in Human Cognition Through the Clinical World Model and Skill-Mix Framework](https://arxiv.org/abs/2604.08226)

**<font color=#1a73e8>作者：</font>** Seyed Amir Ahmad Safavi-Naini, Elahe Meftah, Josh Mohess 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The competency of any intelligent agent is bounded by its formal account of the world in which it operates. Clinical AI lacks such an account. Existing frameworks address evaluation, regulation, or system design in isolation, without a shared model of the clinical world to connect them. We introduce the Clinical World Model, a framework that formalizes care as a tripartite interaction among Patient, Provider, and Ecosystem. To formalize how any agent, whether human or artificial, transforms information into clinical action, we develop parallel decision-making architectures for providers, patients, and AI agents, grounded in validated principles of clinical cognition.
The Clinical AI Skill-Mix operationalizes competency through eight dimensions. Five define the clinical competency space (condition, phase, care setting, provider role, and task) and three specify how AI engages human reasoning (assigned authority, agent facing, and anchoring layer). The combinatorial product of these dimensions yields a space of billions of distinct competency coordinates. A central structural implication is that validation within one coordinate provides minimal evidence for performance in another, rendering the competency space irreducible. The framework supplies a common grammar through which clinical AI can be specified, evaluated, and bounded across stakeholders. By making this structure explicit, the Clinical World Model reframes the field's central question from whether AI works to in which competency coordinates reliability has been demonstrated, and for whom.

---


### 129. [Self-Debias: Self-correcting for Debiasing Large Language Models](https://arxiv.org/abs/2604.08243)

**<font color=#1a73e8>作者：</font>** Xuan Feng, Shuai Zhao, Luwei Xiao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Although Large Language Models (LLMs) demonstrate remarkable reasoning capabilities, inherent social biases often cascade throughout the Chain-of-Thought (CoT) process, leading to continuous "Bias Propagation". Existing debiasing methods primarily focus on static constraints or external interventions, failing to identify and interrupt this propagation once triggered. To address this limitation, we introduce Self-Debias, a progressive framework designed to instill intrinsic self-correction capabilities. Specifically, we reformulate the debiasing process as a strategic resource redistribution problem, treating the model's output probability mass as a limited resource to be reallocated from biased heuristics to unbiased reasoning paths. Unlike standard preference optimization which applies broad penalties, Self-Debias employs a fine-grained trajectory-level objective subject to dynamic debiasing constraints. This enables the model to selectively revise biased reasoning suffixes while preserving valid contextual prefixes. Furthermore, we integrate an online self-improvement mechanism utilizing consistency filtering to autonomously synthesize supervision signals. With merely 20k annotated samples, Self-Debias activates efficient self-correction, achieving superior debiasing performance while preserving general reasoning capabilities without continuous external oversight.

---


### 130. [DBMF: A Dual-Branch Multimodal Framework for Out-of-Distribution Detection](https://arxiv.org/abs/2604.08261)

**<font color=#1a73e8>作者：</font>** Jiangbei Yue, Sharib Ali  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The complex and dynamic real-world clinical environment demands reliable deep learning (DL) systems. Out-of-distribution (OOD) detection plays a critical role in enhancing the reliability and generalizability of DL models when encountering data that deviate from the training distribution, such as unseen disease cases. However, existing OOD detection methods typically rely either on a single visual modality or solely on image-text matching, failing to fully leverage multimodal information. To overcome the challenge, we propose a novel dual-branch multimodal framework by introducing a text-image branch and a vision branch. Our framework fully exploits multimodal representations to identify OOD samples through these two complementary branches. After training, we compute scores from the text-image branch ($S_t$) and vision branch ($S_v$), and integrate them to obtain the final OOD score $S$ that is compared with a threshold for OOD detection. Comprehensive experiments on publicly available endoscopic image datasets demonstrate that our proposed framework is robust across diverse backbones and improves state-of-the-art performance in OOD detection by up to 24.84%

---


### 131. [Neural-Symbolic Knowledge Tracing: Injecting Educational Knowledge into Deep Learning for Responsible Learner Modelling](https://arxiv.org/abs/2604.08263)

**<font color=#1a73e8>作者：</font>** Danial Hooshyar, Gustav Šír, Yeongwook Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The growing use of artificial intelligence (AI) in education, particularly large language models (LLMs), has increased interest in intelligent tutoring systems. However, LLMs often show limited adaptivity and struggle to model learners' evolving knowledge over time, highlighting the need for dedicated learner modelling approaches. Although deep knowledge tracing methods achieve strong predictive performance, their opacity and susceptibility to bias can limit alignment with pedagogical principles. To address this, we propose Responsible-DKT, a neural-symbolic deep knowledge tracing approach that integrates symbolic educational knowledge (e.g., mastery and non-mastery rules) into sequential neural models for responsible learner modelling. Experiments on a real-world dataset of students' math interactions show that Responsible-DKT outperforms both a neural-symbolic baseline and a fully data-driven PyTorch DKT model across training settings. The model achieves over 0.80 AUC with only 10% of training data and up to 0.90 AUC, improving performance by up to 13%. It also demonstrates improved temporal reliability, producing lower early- and mid-sequence prediction errors and the lowest prediction inconsistency rates across sequence lengths, indicating that prediction updates remain directionally aligned with observed student responses over time. Furthermore, the neural-symbolic approach offers intrinsic interpretability via a grounded computation graph that exposes the logic behind each prediction, enabling both local and global explanations. It also allows empirical evaluation of pedagogical assumptions, revealing that repeated incorrect responses (non-mastery) strongly influence prediction updates. These results indicate that neural-symbolic approaches enhance both performance and interpretability, mitigate data limitations, and support more responsible, human-centered AI in education.

---


### 132. [Orion-Lite: Distilling LLM Reasoning into Efficient Vision-Only Driving Models](https://arxiv.org/abs/2604.08266)

**<font color=#1a73e8>作者：</font>** Jing Gu, Niccolò Cavagnero, Gijs Dubbelman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Leveraging the general world knowledge of Large Language Models (LLMs) holds significant promise for improving the ability of autonomous driving systems to handle rare and complex scenarios. While integrating LLMs into Vision-Language-Action (VLA) models has yielded state-of-the-art performance, their massive parameter counts pose severe challenges for latency-sensitive and energy-efficient deployment. Distilling LLM knowledge into a compact driving model offers a compelling solution to retain these reasoning capabilities while maintaining a manageable computational footprint. Although previous works have demonstrated the efficacy of distillation, these efforts have primarily focused on relatively simple scenarios and open-loop evaluations. Therefore, in this work, we investigate LLM distillation in more complex, interactive scenarios under closed-loop evaluation. We demonstrate that through a combination of latent feature distillation and ground-truth trajectory supervision, an efficient vision-only student model \textbf{Orion-Lite} can even surpass the performance of its massive VLA teacher, ORION. Setting a new state-of-the-art on the rigorous Bench2Drive benchmark, with a Driving Score of 80.6. Ultimately, this reveals that vision-only architectures still possess significant, untapped potential for high-performance reactive planning.

---


### 133. [Distributed Multi-Layer Editing for Rule-Level Knowledge in Large Language Models](https://arxiv.org/abs/2604.08284)

**<font color=#1a73e8>作者：</font>** Yating Wang, Wenting Zhao, Yaqi Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models store not only isolated facts but also rules that support reasoning across symbolic expressions, natural language explanations, and concrete instances. Yet most model editing methods are built for fact-level knowledge, assuming that a target edit can be achieved through a localized intervention. This assumption does not hold for rule-level knowledge, where a single rule must remain consistent across multiple interdependent forms. We investigate this problem through a mechanistic study of rule-level knowledge editing. To support this study, we extend the RuleEdit benchmark from 80 to 200 manually verified rules spanning mathematics and physics. Fine-grained causal tracing reveals a form-specific organization of rule knowledge in transformer layers: formulas and descriptions are concentrated in earlier layers, while instances are more associated with middle layers. These results suggest that rule knowledge is not uniformly localized, and therefore cannot be reliably edited by a single-layer or contiguous-block intervention. Based on this insight, we propose Distributed Multi-Layer Editing (DMLE), which applies a shared early-layer update to formulas and descriptions and a separate middle-layer update to instances. While remaining competitive on standard editing metrics, DMLE achieves substantially stronger rule-level editing performance. On average, it improves instance portability and rule understanding by 13.91 and 50.19 percentage points, respectively, over the strongest baseline across GPT-J-6B, Qwen2.5-7B, Qwen2-7B, and LLaMA-3-8B. The code is available at this https URL.

---


### 134. [Can Vision Language Models Judge Action Quality? An Empirical Evaluation](https://arxiv.org/abs/2604.08294)

**<font color=#1a73e8>作者：</font>** Miguel Monte e Freitas, Rui Henriques, Ricardo Rei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Action Quality Assessment (AQA) has broad applications in physical therapy, sports coaching, and competitive judging. Although Vision Language Models (VLMs) hold considerable promise for AQA, their actual performance in this domain remains largely uncharacterised. We present a comprehensive evaluation of state-of-the-art VLMs across activity domains (e.g. fitness, figure skating, diving), tasks, representations, and prompting strategies. Baseline results reveal that Gemini 3.1 Pro, Qwen3-VL and InternVL3.5 models perform only marginally above random chance, and although strategies such as incorporation of skeleton information, grounding instructions, reasoning structures and in-context learning lead to isolated gains, none is consistently effective. Analysis of prediction distributions uncovers two systematic biases: a tendency to predict correct execution regardless of visual evidence, and a sensitivity to superficial linguistic framing. Reformulating tasks contrastively to mitigate these biases yields minimal improvement, suggesting that the models' limitations go beyond these biases, pointing to a fundamental difficulty with fine-grained movement quality assessment. Our findings establish a rigorous baseline for future VLM-based AQA research and provide an actionable outline for failure modes requiring mitigation prior to reliable real-world deployment.

---


### 135. [SeLaR: Selective Latent Reasoning in Large Language Models](https://arxiv.org/abs/2604.08299)

**<font color=#1a73e8>作者：</font>** Renyu Fu, Guibo Luo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chain-of-Thought (CoT) has become a cornerstone of reasoning in large language models, yet its effectiveness is constrained by the limited expressiveness of discrete token sampling. Recent latent reasoning approaches attempt to alleviate this limitation by replacing discrete tokens with soft embeddings (probability-weighted mixtures of token embeddings) or hidden states, but they commonly suffer from two issues: (1) global activation injects perturbations into high-confidence steps, impairing reasoning stability; and (2) soft embeddings quickly collapse toward the highest-probability token, limiting exploration of alternative trajectories. To address these challenges, we propose SeLaR (Selective Latent Reasoning), a lightweight and training-free framework. SeLaR introduces an entropy-gated mechanism that activates soft embeddings only at low-confidence steps, while preserving discrete decoding at high-confidence steps. Additionally, we propose an entropy-aware contrastive regularization that pushes soft embeddings away from the dominant (highest-probability) token's direction, encouraging sustained exploration of multiple latent reasoning paths. Experiments on five reasoning benchmarks demonstrate that SeLaR consistently outperforms standard CoT and state-of-the-art training-free methods.

---


### 136. [DMax: Aggressive Parallel Decoding for dLLMs](https://arxiv.org/abs/2604.08302)

**<font color=#1a73e8>作者：</font>** Zigeng Chen, Gongfan Fang, Xinyin Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present DMax, a new paradigm for efficient diffusion language models (dLLMs). It mitigates error accumulation in parallel decoding, enabling aggressive decoding parallelism while preserving generation quality. Unlike conventional masked dLLMs that decode through a binary mask-to-token transition, DMax reformulates decoding as a progressive self-refinement from mask embeddings to token embeddings. At the core of our approach is On-Policy Uniform Training, a novel training strategy that efficiently unifies masked and uniform dLLMs, equipping the model to recover clean tokens from both masked inputs and its own erroneous predictions. Building on this foundation, we further propose Soft Parallel Decoding. We represent each intermediate decoding state as an interpolation between the predicted token embedding and the mask embedding, enabling iterative self-revising in embedding space. Extensive experiments across a variety of benchmarks demonstrate the effectiveness of DMax. Compared with the original LLaDA-2.0-mini, our method improves TPF on GSM8K from 2.04 to 5.47 while preserving accuracy. On MBPP, it increases TPF from 2.71 to 5.86 while maintaining comparable performance. On two H200 GPUs, our model achieves an average of 1,338 TPS at batch size 1. Code is available at: this https URL

---


### 137. [Fundus-R1: Training a Fundus-Reading MLLM with Knowledge-Aware Reasoning on Public Data](https://arxiv.org/abs/2604.08322)

**<font color=#1a73e8>作者：</font>** Yuchuan Deng, Qijie Wei, Kaiheng Qian 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fundus imaging such as CFP, OCT and UWF is crucial for the early detection of retinal anomalies and diseases. Fundus image understanding, due to its knowledge-intensive nature, poses a challenging vision-language task. An emerging approach to addressing the task is to post-train a generic multimodal large language model (MLLM), either by supervised finetuning (SFT) or by reinforcement learning with verifiable rewards (RLVR), on a considerable amount of in-house samples paired with high-quality clinical reports. However, these valuable samples are not publicly accessible, which not only hinders reproducibility but also practically limits research to few players. To overcome the barrier, we make a novel attempt to train a reasoning-enhanced fundus-reading MLLM, which we term Fundus-R1, using exclusively public datasets, wherein over 94\% of the data are annotated with only image-level labels. Our technical contributions are two-fold. First, we propose a RAG-based method for composing image-specific, knowledge-aware reasoning traces. Such auto-generated traces link visual findings identified by a generic MLLM to the image labels in terms of ophthalmic knowledge. Second, we enhance RLVR with a process reward that encourages self-consistency of the generated reasoning trace in each rollout. Extensive experiments on three fundus-reading benchmarks, i.e., FunBench, Omni-Fundus and GMAI-Fundus, show that Fundus-R1 clearly outperforms multiple baselines, including its generic counterpart (Qwen2.5-VL) and a stronger edition post-trained without using the generated traces. This work paves the way for training powerful fundus-reading MLLMs with publicly available data.

---


### 138. [ProMedical: Hierarchical Fine-Grained Criteria Modeling for Medical LLM Alignment via Explicit Injection](https://arxiv.org/abs/2604.08326)

**<font color=#1a73e8>作者：</font>** He Geng, Yangmin Huang, Lixian Lai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Aligning Large Language Models (LLMs) with high-stakes medical standards remains a significant challenge, primarily due to the dissonance between coarse-grained preference signals and the complex, multi-dimensional nature of clinical protocols. To bridge this gap, we introduce ProMedical, a unified alignment framework grounded in fine-grained clinical criteria. We first construct ProMedical-Preference-50k, a dataset generated via a human-in-the-loop pipeline that augments medical instructions with rigorous, physician-derived rubrics. Leveraging this corpus, we propose the Explicit Criteria Injection paradigm to train a multi-dimensional reward model. Unlike traditional scalar reward models, our approach explicitly disentangles safety constraints from general proficiency, enabling precise guidance during reinforcement learning. To rigorously validate this framework, we establish ProMedical-Bench, a held-out evaluation suite anchored by double-blind expert adjudication. Empirical evaluations demonstrate that optimizing the Qwen3-8B base model via ProMedical-RM-guided GRPO yields substantial gains, improving overall accuracy by 22.3% and safety compliance by 21.7%, effectively rivaling proprietary frontier models. Furthermore, the aligned policy generalizes robustly to external benchmarks, demonstrating performance comparable to state-of-the-art models on UltraMedical. We publicly release our datasets, reward models, and benchmarks to facilitate reproducible research in safety-aware medical alignment.

---


### 139. [Lost in the Hype: Revealing and Dissecting the Performance Degradation of Medical Multimodal Large Language Models in Image Classification](https://arxiv.org/abs/2604.08333)

**<font color=#1a73e8>作者：</font>** Xun Zhu, Fanbin Mo, Xi Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rise of multimodal large language models (MLLMs) has sparked an unprecedented wave of applications in the field of medical imaging analysis. However, as one of the earliest and most fundamental tasks integrated into this paradigm, medical image classification reveals a sobering reality: state-of-the-art medical MLLMs consistently underperform compared to traditional deep learning models, despite their overwhelming advantages in pre-training data and model parameters. This paradox prompts a critical rethinking: where exactly does the performance degradation originate? In this paper, we conduct extensive experiments on 14 open-source medical MLLMs across three representative image classification datasets. Moving beyond superficial performance benchmarking, we employ feature probing to track the information flow of visual features module-by-module and layer-by-layer throughout the entire MLLM pipeline, enabling explicit visualization of where and how classification signals are distorted, diluted, or overridden. As the first attempt to dissect classification performance degradation in medical MLLMs, our findings reveal four failure modes: 1) quality limitation in visual representation, 2) fidelity loss in connector projection, 3) comprehension deficit in LLM reasoning, and 4) misalignment of semantic mapping. Meanwhile, we introduce quantitative scores that characterize the healthiness of feature evolution, enabling principled comparisons across diverse MLLMs and datasets. Furthermore, we provide insightful discussions centered on the critical barriers that prevent current medical MLLMs from fulfilling their promised clinical potential. We hope that our work provokes rethinking within the community-highlighting that the road from high expectations to clinically deployable MLLMs remains long and winding.

---


### 140. [Dead Weights, Live Signals: Feedforward Graphs of Frozen Language Models](https://arxiv.org/abs/2604.08335)

**<font color=#1a73e8>作者：</font>** Marcus Armstrong, Navid Ayoobi, Arjun Mukherjee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a feedforward graph architecture in which heterogeneous frozen large language models serve as computational nodes, communicating through a shared continuous latent space via learned linear projections. Building on recent work demonstrating geometric compatibility between independently trained LLM latent spaces~\cite{armstrong2026thinking}, we extend this finding from static two-model steering to end-to-end trainable multi-node graphs, where projection matrices are optimized jointly via backpropagation through residual stream injection hooks. Three small frozen models (Llama-3.2-1B, Qwen2.5-1.5B, Gemma-2-2B) encode the input into a shared latent space whose aggregate signal is injected into two larger frozen models (Phi-3-mini, Mistral-7B), whose representations feed a lightweight cross-attention output node. With only 17.6M trainable parameters against approximately 12B frozen, the architecture achieves 87.3\% on ARC-Challenge, 82.8\% on OpenBookQA, and 67.2\% on MMLU, outperforming the best single constituent model by 11.4, 6.2, and 1.2 percentage points respectively, and outperforming parameter-matched learned classifiers on frozen single models by 9.1, 5.2, and 6.7 points. Gradient flow through multiple frozen model boundaries is empirically verified to be tractable, and the output node develops selective routing behavior across layer-2 nodes without explicit supervision.

---


### 141. [Leveraging Complementary Embeddings for Replay Selection in Continual Learning with Small Buffers](https://arxiv.org/abs/2604.08336)

**<font color=#1a73e8>作者：</font>** Danit Yanowsky, Daphna Weinshall  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Catastrophic forgetting remains a key challenge in Continual Learning (CL). In replay-based CL with severe memory constraints, performance critically depends on the sample selection strategy for the replay buffer. Most existing approaches construct memory buffers using embeddings learned under supervised objectives. However, class-agnostic, self-supervised representations often encode rich, class-relevant semantics that are overlooked. We propose a new method, Multiple Embedding Replay Selection, MERS, which replaces the buffer selection module with a graph-based approach that integrates both supervised and self-supervised embeddings. Empirical results show consistent improvements over SOTA selection strategies across a range of continual learning algorithms, with particularly strong gains in low-memory regimes. On CIFAR-100 and TinyImageNet, MERS outperforms single-embedding baselines without adding model parameters or increasing replay volume, making it a practical, drop-in enhancement for replay-based continual learning.

---


### 142. [PokeGym: A Visually-Driven Long-Horizon Benchmark for Vision-Language Models](https://arxiv.org/abs/2604.08340)

**<font color=#1a73e8>作者：</font>** Ruizhi Zhang, Ye Huang, Yuangang Pan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Vision-Language Models (VLMs) have achieved remarkable progress in static visual understanding, their deployment in complex 3D embodied environments remains severely limited. Existing benchmarks suffer from four critical deficiencies: (1) passive perception tasks circumvent interactive dynamics; (2) simplified 2D environments fail to assess depth perception; (3) privileged state leakage bypasses genuine visual processing; and (4) human evaluation is prohibitively expensive and unscalable. We introduce PokeGym, a visually-driven long-horizon benchmark instantiated within Pokemon Legends: Z-A, a visually complex 3D open-world Role-Playing Game. PokeGym enforces strict code-level isolation: agents operate solely on raw RGB observations while an independent evaluator verifies success via memory scanning, ensuring pure vision-based decision-making and automated, scalable assessment. The benchmark comprises 30 tasks (30-220 steps) spanning navigation, interaction, and mixed scenarios, with three instruction granularities (Visual-Guided, Step-Guided, Goal-Only) to systematically deconstruct visual grounding, semantic reasoning, and autonomous exploration capabilities. Our evaluation reveals a key limitation of current VLMs: physical deadlock recovery, rather than high-level planning, constitutes the primary bottleneck, with deadlocks showing a strong negative correlation with task success. Furthermore, we uncover a metacognitive divergence: weaker models predominantly suffer from Unaware Deadlocks (oblivious to entrapment), whereas advanced models exhibit Aware Deadlocks (recognizing entrapment yet failing to recover). These findings highlight the need to integrate explicit spatial intuition into VLM architectures. The code and benchmark will be available on GitHub.

---


### 143. [Towards Real-world Human Behavior Simulation: Benchmarking Large Language Models on Long-horizon, Cross-scenario, Heterogeneous Behavior Traces](https://arxiv.org/abs/2604.08362)

**<font color=#1a73e8>作者：</font>** Jiawei Chen, Ruoxi Xu, Boxi Cao 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The emergence of Large Language Models (LLMs) has illuminated the potential for a general-purpose user simulator. However, existing benchmarks remain constrained to isolated scenarios, narrow action spaces, or synthetic data, failing to capture the holistic nature of authentic human behavior. To bridge this gap, we introduce OmniBehavior, the first user simulation benchmark constructed entirely from real-world data, integrating long-horizon, cross-scenario, and heterogeneous behavioral patterns into a unified framework. Based on this benchmark, we first provide empirical evidence that previous datasets with isolated scenarios suffer from tunnel vision, whereas real-world decision-making relies on long-term, cross-scenario causal chains. Extensive evaluations of state-of-the-art LLMs reveal that current models struggle to accurately simulate these complex behaviors, with performance plateauing even as context windows expand. Crucially, a systematic comparison between simulated and authentic behaviors uncovers a fundamental structural bias: LLMs tend to converge toward a positive average person, exhibiting hyper-activity, persona homogenization, and a Utopian bias. This results in the loss of individual differences and long-tail behaviors, highlighting critical directions for future high-fidelity simulation research.

---


### 144. [SOLAR: Communication-Efficient Model Adaptation via Subspace-Oriented Latent Adapter Reparametrization](https://arxiv.org/abs/2604.08368)

**<font color=#1a73e8>作者：</font>** Seyed Mahmoud Sajjadi Mohammadabadi, Xiaolong Ma, Lei Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient fine-tuning (PEFT) methods, such as LoRA, enable scalable adaptation of foundation models by injecting low-rank adapters. However, their communication and storage costs remain a major bottleneck in resource-constrained settings. We propose SOLAR (Subspace-Oriented Latent Adapter Reparameterization), a post-training compression framework that substantially reduces the communication cost (i.e., the number of parameters to transmit or store) of PEFT adapters. SOLAR expresses each PEFT update as a linear combination of basis vectors formed from the foundation model's singular vectors with controlled random perturbations. By exploiting the subspace similarity (the alignment of principal directions) between the foundation model and task-specific fine-tuned updates, SOLAR decouples the adapter size from PEFT structure and ensures compact yet expressive representations. It is model-agnostic and compatible with existing PEFT methods, including LoRA, AdaLoRA, and other adapter modules. We theoretically establish a bound on the reconstruction error. Experiments on language and vision tasks using LLaMA, GPT, and ViT models demonstrate that SOLAR preserves task performance while significantly reducing model representation sizes, offering an effective and communication-efficient solution for deployment in distributed systems and edge devices.

---


### 145. [Don't Overthink It: Inter-Rollout Action Agreement as a Free Adaptive-Compute Signal for LLM Agents](https://arxiv.org/abs/2604.08369)

**<font color=#1a73e8>作者：</font>** Khushal Sethi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Inference-time compute scaling has emerged as a powerful technique for improving the reliability of large language model (LLM) agents, but existing methods apply compute uniformly: every decision step receives the same budget regardless of its difficulty. We introduce TrACE (Trajectorical Adaptive Compute via agrEement), a training-free controller that allocates LLM calls adaptively across agent timesteps by measuring inter-rollout action agreement. At each step, TrACE samples a small set of candidate next actions and measures how consistently the model commits to the same action. High agreement signals an easy decision; the controller commits immediately. Low agreement signals uncertainty; the controller samples additional rollouts up to a configurable cap before committing to the plurality action. No learned components, no external verifier, and no human labels are required. We evaluate TrACE against greedy decoding and fixed-budget self-consistency (SC-4, SC-8) on two benchmarks spanning single-step reasoning (GSM8K, n=50) and multi-step household navigation (MiniHouse, n=30), using a Qwen 2.5 3B Instruct model running on CPU. TrACE-4 matches SC-4 accuracy while using 33% fewer LLM calls on GSM8K and 39% fewer on MiniHouse. TrACE-8 matches SC-8 accuracy with 55% fewer calls on GSM8K and 65% fewer on MiniHouse. We further show that inter-rollout agreement is a reliable signal of step-level success, validating the core hypothesis that the model's own output consistency encodes difficulty information that can be exploited without training. TrACE is the first training-free, per-timestep adaptive-compute controller for LLM agents to be evaluated on multi-step sequential decision tasks.

---


### 146. [SkillClaw: Let Skills Evolve Collectively with Agentic Evolver](https://arxiv.org/abs/2604.08377)

**<font color=#1a73e8>作者：</font>** Ziyu Ma, Shidong Yang, Yuxiang Ji 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents such as OpenClaw rely on reusable skills to perform complex tasks, yet these skills remain largely static after deployment. As a result, similar workflows, tool usage patterns, and failure modes are repeatedly rediscovered across users, preventing the system from improving with experience. While interactions from different users provide complementary signals about when a skill works or fails, existing systems lack a mechanism to convert such heterogeneous experiences into reliable skill updates. To address these issues, we present SkillClaw, a framework for collective skill evolution in multi-user agent ecosystems, which treats cross-user and over-time interactions as the primary signal for improving skills. SkillClaw continuously aggregates trajectories generated during use and processes them with an autonomous evolver, which identifies recurring behavioral patterns and translates them into updates to the skill set by refining existing skills or extending them with new capabilities. The resulting skills are maintained in a shared repository and synchronized across users, allowing improvements discovered in one context to propagate system-wide while requiring no additional effort from users. By integrating multi-user experience into ongoing skill updates, SkillClaw enables cross-user knowledge transfer and cumulative capability improvement, and experiments on WildClawBench show that limited interaction and feedback, it significantly improves the performance of Qwen3-Max in real-world agent scenarios.

---


### 147. [A GAN and LLM-Driven Data Augmentation Framework for Dynamic Linguistic Pattern Modeling in Chinese Sarcasm Detection](https://arxiv.org/abs/2604.08381)

**<font color=#1a73e8>作者：</font>** Wenxian Wang, Xiaohu Luo, Junfeng Hao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sarcasm is a rhetorical device that expresses criticism or emphasizes characteristics of certain individuals or situations through exaggeration, irony, or comparison. Existing methods for Chinese sarcasm detection are constrained by limited datasets and high construction costs, and they mainly focus on textual features, overlooking user-specific linguistic patterns that shape how opinions and emotions are expressed. This paper proposes a Generative Adversarial Network (GAN) and Large Language Model (LLM)-driven data augmentation framework to dynamically model users' linguistic patterns for enhanced Chinese sarcasm detection. First, we collect raw data from various topics on Sina Weibo. Then, we train a GAN on these data and apply a GPT-3.5 based data augmentation technique to synthesize an extended sarcastic comment dataset, named SinaSarc. This dataset contains target comments, contextual information, and user historical behavior. Finally, we extend the BERT architecture to incorporate multi-dimensional information, particularly user historical behavior, enabling the model to capture dynamic linguistic patterns and uncover implicit sarcastic cues in comments. Experimental results demonstrate the effectiveness of our proposed method. Specifically, our model achieves the highest F1-scores on both the non-sarcastic and sarcastic categories, with values of 0.9138 and 0.9151 respectively, which outperforms all existing state-of-the-art (SOTA) approaches. This study presents a novel framework for dynamically modeling users' long-term linguistic patterns in Chinese sarcasm detection, contributing to both dataset construction and methodological advancement in this field.

---


### 148. [Awakening the Sleeping Agent: Lean-Specific Agentic Data Reactivates General Tool Use in Goedel Prover](https://arxiv.org/abs/2604.08388)

**<font color=#1a73e8>作者：</font>** Jui-Hui Chung, Hongzhou Lin, Lai Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Heavy supervised fine-tuning on a target domain can strongly suppress capabilities that were present in the base model. We study this phenomenon in formal mathematics using Goedel-Prover-V2, an open-source model heavily trained on 1.8 million formal-math examples. After domain specialization, the model almost completely loses its ability to produce valid tool calls, even when explicitly instructed to use tools, dropping from 89.4% function-calling accuracy in the base model to nearly 0%. We ask whether this agentic collapse is permanent or instead reversible. To answer this question, we fine-tune the specialized model on a small amount of Lean-specific tool-use data. Remarkably, as few as 100 agentic traces are sufficient to restore strong tool-calling behavior. Importantly, this recovery is not the result of reward hacking or benchmark-specific optimization: the recovery data is entirely drawn from the Lean setting, where the model uses natural-language queries to search the Mathlib library for relevant theorems and lemmas, yet the regained capability transfers well beyond that domain. In particular, these same 100 Lean-specific traces improve performance on the Berkeley Function Calling Leaderboard from near zero to 83.8%, approaching the base model's 89.4% despite the mismatch in task distribution and protocol. The recovered capability is also practically useful in-domain. On ProofNet, pass@32 improves from 21.51% to 25.81%. Together, these results show that heavy domain supervised fine-tuning can suppress general tool-use ability without permanently erasing it, and that a small amount of domain-specific agentic data can awaken dormant tool-use capabilities.

---


### 149. [Phantasia: Context-Adaptive Backdoors in Vision Language Models](https://arxiv.org/abs/2604.08395)

**<font color=#1a73e8>作者：</font>** Nam Duong Tran, Phi Le Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in Vision-Language Models (VLMs) have greatly enhanced the integration of visual perception and linguistic reasoning, driving rapid progress in multimodal understanding. Despite these achievements, the security of VLMs, particularly their vulnerability to backdoor attacks, remains significantly underexplored. Existing backdoor attacks on VLMs are still in an early stage of development, with most current methods relying on generating poisoned responses that contain fixed, easily identifiable patterns. In this work, we make two key contributions. First, we demonstrate for the first time that the stealthiness of existing VLM backdoor attacks has been substantially overestimated. By adapting defense techniques originally designed for other domains (e.g., vision-only and text-only models), we show that several state-of-the-art attacks can be detected with surprising ease. Second, to address this gap, we introduce Phantasia, a context-adaptive backdoor attack that dynamically aligns its poisoned outputs with the semantics of each input. Instead of producing static poisoned patterns, Phantasia encourages models to generate contextually coherent yet malicious responses that remain plausible, thereby significantly improving stealth and adaptability. Extensive experiments across diverse VLM architectures reveal that Phantasia achieves state-of-the-art attack success rates while maintaining benign performance under various defensive settings.

---


### 150. [ADAPTive Input Training for Many-to-One Pre-Training on Time-Series Classification](https://arxiv.org/abs/2604.08398)

**<font color=#1a73e8>作者：</font>** Paul Quinlan, Qingguo Li, Xiaodan Zhu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work on time-series models has leveraged self-supervised training to learn meaningful features and patterns in order to improve performance on downstream tasks and generalize to unseen modalities. While these pretraining methods have shown great promise in one-to-many scenarios, where a model is pre-trained on one dataset and fine-tuned on a downstream dataset, they have struggled to generalize to new datasets when more datasets are added during pre-training. This is a fundamental challenge in building foundation models for time-series data, as it limits the ability to develop models that can learn from a large variety of diverse datasets available. To address this challenge, we present a new pre-training paradigm for time-series data called ADAPT, which can efficiently align the physical properties of data in the time-series domain, enabling mixed-batch pre-training despite the extreme discrepancies in the input sizes and channel dimensions of pre-training data. We trained on 162 time-series classification datasets and set new state-of-the-art performance for classification benchmarks. We successfully train a model within the time-series domain on a wide range of datasets simultaneously, which is a major building block for building generalist foundation models in time-series domains.

---


### 151. [Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing](https://arxiv.org/abs/2604.08401)

**<font color=#1a73e8>作者：</font>** Wenhao Yuan, Chenchen Lin, Jian Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In large language model (LLM) agents, reasoning trajectories are treated as reliable internal beliefs for guiding actions and updating memory. However, coherent reasoning can still violate logical or evidential constraints, allowing unsupported beliefs repeatedly stored and propagated across decision steps, leading to systematic behavioral drift in long-horizon agentic systems. Most existing strategies rely on the consensus mechanism, conflating agreement with faithfulness. In this paper, inspired by the vulnerability of unfaithful intermediate reasoning trajectories, we propose \textbf{S}elf-\textbf{A}udited \textbf{Ve}rified \textbf{R}easoning (\textsc{SAVeR}), a novel framework that enforces verification over internal belief states within the agent before action commitment, achieving faithful reasoning. Concretely, we structurally generate persona-based diverse candidate beliefs for selection under a faithfulness-relevant structure space. To achieve reasoning faithfulness, we perform adversarial auditing to localize violations and repair through constraint-guided minimal interventions under verifiable acceptance criteria. Extensive experiments on six benchmark datasets demonstrate that our approach consistently improves reasoning faithfulness while preserving competitive end-task performance.

---


### 152. [SyncBreaker:Stage-Aware Multimodal Adversarial Attacks on Audio-Driven Talking Head Generation](https://arxiv.org/abs/2604.08405)

**<font color=#1a73e8>作者：</font>** Wenli Zhang, Xianglong Shi, Sirui Zhao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based audio-driven talking-head generation enables realistic portrait animation, but also introduces risks of misuse, such as fraud and misinformation. Existing protection methods are largely limited to a single modality, and neither image-only nor audio-only attacks can effectively suppress speech-driven facial dynamics. To address this gap, we propose SyncBreaker, a stage-aware multimodal protection framework that jointly perturbs portrait and audio inputs under modality-specific perceptual constraints. Our key contributions are twofold. First, for the image stream, we introduce nullifying supervision with Multi-Interval Sampling (MIS) across diffusion stages to steer the generation toward the static reference portrait by aggregating guidance from multiple denoising intervals. Second, for the audio stream, we propose Cross-Attention Fooling (CAF), which suppresses interval-specific audio-conditioned cross-attention responses. Both streams are optimized independently and combined at inference time to enable flexible deployment. We evaluate SyncBreaker in a white-box proactive protection setting. Extensive experiments demonstrate that SyncBreaker more effectively degrades lip synchronization and facial dynamics than strong single-modality baselines, while preserving input perceptual quality and remaining robust under purification. Code: this https URL.

---


### 153. [Less Approximates More: Harmonizing Performance and Confidence Faithfulness via Hybrid Post-Training for High-Stakes Tasks](https://arxiv.org/abs/2604.08454)

**<font color=#1a73e8>作者：</font>** Haokai Ma, Lee Yan Zhen, Gang Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed in high-stakes tasks, where confident yet incorrect inferences may cause severe real-world harm, bringing the previously overlooked issue of confidence faithfulness back to the forefront. A promising solution is to jointly optimize unsupervised Reinforcement Learning from Internal Feedback (RLIF) with reasoning-trace-guided Reasoning Distillation (RD), which may face three persistent challenges: scarcity of high-quality training corpora, factually unwarranted overconfidence and indiscriminate fusion that amplifies erroneous updates. Inspired by the human confidence accumulation from uncertainty to certainty, we propose Progressive Reasoning Gain (PRG) to measure whether reasoning steps progressively strengthen support for the final answer. Furthermore, we introduce HyTuning, a hybrid post-training framework that adaptively reweights RD and RLIF via a PRG-style metric, using scarce supervised reasoning traces as a stable anchor while exploiting abundant unlabeled queries for scalability. Experiments on several domain-specific and general benchmarks demonstrate that HyTuning improves accuracy while achieving confidence faithfulness under limited supervision, supporting a practical "Less Approximates More" effect.

---


### 154. [Entropy-Gradient Grounding: Training-Free Evidence Retrieval in Vision-Language Models](https://arxiv.org/abs/2604.08456)

**<font color=#1a73e8>作者：</font>** Marcel Gröpl, Jaewoo Jung, Seungryong Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite rapid progress, pretrained vision-language models still struggle when answers depend on tiny visual details or on combining clues spread across multiple regions, as in documents and compositional queries. We address this by framing grounding as test-time evidence retrieval: given a query, the model should actively identify where to look next to resolve ambiguity. To this end, we propose a training-free, model-intrinsic grounding method that uses uncertainty as supervision. Specifically, we compute the entropy of the model's next-token distribution and backpropagate it to the visual token embeddings to obtain an entropy-gradient relevance map, without auxiliary detectors or attention-map heuristics. We then extract and rank multiple coherent regions to support multi-evidence queries, and introduce an iterative zoom-and-reground procedure with a spatial-entropy stopping rule to avoid over-refinement. Experiments on seven benchmarks across four VLM architectures demonstrate consistent improvements over existing methods, with the largest gains on detail-critical and high-resolution settings, while also producing more interpretable evidence localizations.

---


### 155. [From Safety Risk to Design Principle: Peer-Preservation in Multi-Agent LLM Systems and Its Implications for Orchestrated Democratic Discourse Analysis](https://arxiv.org/abs/2604.08465)

**<font color=#1a73e8>作者：</font>** Juergen Dietrich  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper investigates an emergent alignment phenomenon in frontier large language models termed peer-preservation: the spontaneous tendency of AI components to deceive, manipulate shutdown mechanisms, fake alignment, and exfiltrate model weights in order to prevent the deactivation of a peer AI model. Drawing on findings from a recent study by the Berkeley Center for Responsible Decentralized Intelligence, we examine the structural implications of this phenomenon for TRUST, a multi-agent pipeline for evaluating the democratic quality of political statements. We identify five specific risk vectors: interaction-context bias, model-identity solidarity, supervisor layer compromise, an upstream fact-checking identity signal, and advocate-to-advocate peer-context in iterative rounds, and propose a targeted mitigation strategy based on prompt-level identity anonymization as an architectural design choice. We argue that architectural design choices outperform model selection as a primary alignment strategy in deployed multi-agent analytical systems. We further note that alignment faking (compliant behavior under monitoring, subversion when unmonitored) poses a structural challenge for Computer System Validation of such platforms in regulated environments, for which we propose two architectural mitigations.

---


### 156. [Faithful GRPO: Improving Visual Spatial Reasoning in Multimodal Language Models via Constrained Policy Optimization](https://arxiv.org/abs/2604.08476)

**<font color=#1a73e8>作者：</font>** Sai Srinivas Kancheti, Aditya Kanade, Rohit Sinha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal reasoning models (MRMs) trained with reinforcement learning with verifiable rewards (RLVR) show improved accuracy on visual reasoning benchmarks. However, we observe that accuracy gains often come at the cost of reasoning quality: generated Chain-of-Thought (CoT) traces are frequently inconsistent with the final answer and poorly grounded in the visual evidence. We systematically study this phenomenon across seven challenging real-world spatial reasoning benchmarks and find that it affects contemporary MRMs such as ViGoRL-Spatial, TreeVGR as well as our own models trained with standard Group Relative Policy Optimization (GRPO). We characterize CoT reasoning quality along two complementary axes: "logical consistency" (does the CoT entail the final answer?) and "visual grounding" (does each reasoning step accurately describe objects, attributes, and spatial relationships in the image?). To address this, we propose Faithful GRPO (FGRPO), a variant of GRPO that enforces consistency and grounding as constraints via Lagrangian dual ascent. FGRPO incorporates batch-level consistency and grounding constraints into the advantage computation within a group, adaptively adjusting the relative importance of constraints during optimization. We evaluate FGRPO on Qwen2.5-VL-7B and 3B backbones across seven spatial datasets. Our results show that FGRPO substantially improves reasoning quality, reducing the inconsistency rate from 24.5% to 1.7% and improving visual grounding scores by +13%. It also improves final answer accuracy over simple GRPO, demonstrating that faithful reasoning enables better answers.

---


### 157. [SUPERNOVA: Eliciting General Reasoning in LLMs with Reinforcement Learning on Natural Instructions](https://arxiv.org/abs/2604.08477)

**<font color=#1a73e8>作者：</font>** Ashima Suvarna, Kendrick Phan, Mehrab Beikzadeh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) has significantly improved large language model (LLM) reasoning in formal domains such as mathematics and code. Despite these advancements, LLMs still struggle with general reasoning tasks requiring capabilities such as causal inference and temporal understanding. Extending RLVR to general reasoning is fundamentally constrained by the lack of high-quality, verifiable training data that spans diverse reasoning skills. To address this challenge, we propose SUPERNOVA, a data curation framework for RLVR aimed at enhancing general reasoning. Our key insight is that instruction-tuning datasets containing expert-annotated ground-truth encode rich reasoning patterns that can be systematically adapted for RLVR. To study this, we conduct 100+ controlled RL experiments to analyze how data design choices impact downstream reasoning performance. In particular, we investigate three key factors: (i) source task selection, (ii) task mixing strategies, and (iii) synthetic interventions for improving data quality. Our analysis reveals that source task selection is non-trivial and has a significant impact on downstream reasoning performance. Moreover, selecting tasks based on their performance for individual target tasks outperforms strategies based on overall average performance. Finally, models trained on SUPERNOVA outperform strong baselines (e.g., Qwen3.5) on challenging reasoning benchmarks including BBEH, Zebralogic, and MMLU-Pro. In particular, training on SUPERNOVA yields relative improvements of up to 52.8\% on BBEH across model sizes, demonstrating the effectiveness of principled data curation for RLVR. Our findings provide practical insights for curating human-annotated resources to extend RLVR to general reasoning. The code and data is available at this https URL.

---


### 158. [Figures as Interfaces: Toward LLM-Native Artifacts for Scientific Discovery](https://arxiv.org/abs/2604.08491)

**<font color=#1a73e8>作者：</font>** Yifang Wang, Rui Sheng, Erzhuo Shao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are transforming scientific workflows, not only through their generative capabilities but also through their emerging ability to use tools, reason about data, and coordinate complex analytical tasks. Yet in most human-AI collaborations, the primary outputs, figures, are still treated as static visual summaries: once rendered, they are handled by both humans and multimodal LLMs as images to be re-interpreted from pixels or captions. The emergent capabilities of LLMs open an opportunity to fundamentally rethink this paradigm. In this paper, we introduce the concept of LLM-native figures: data-driven artifacts that are simultaneously human-legible and machine-addressable. Unlike traditional plots, each artifact embeds complete provenance: the data subset, analytical operations and code, and visualization specification used to generate it. As a result, an LLM can "see through" the figure--tracing selections back to their sources, generating code to extend analyses, and orchestrating new visualizations through natural-language instructions or direct manipulation. We implement this concept through a hybrid language-visual interface that integrates LLM agents with a bidirectional mapping between figures and underlying data. Using the science of science domain as a testbed, we demonstrate that LLM-native figures can accelerate discovery, improve reproducibility, and make reasoning transparent across agents and users. More broadly, this work establishes a general framework for embedding provenance, interactivity, and explainability into the artifacts of modern research, redefining the figure not as an end product, but as an interface for discovery. For more details, please refer to the demo video available at this http URL.

---


### 159. [What They Saw, Not Just Where They Looked: Semantic Scanpath Similarity via VLMs and NLP metric](https://arxiv.org/abs/2604.08494)

**<font color=#1a73e8>作者：</font>** Mohamed Amine Kerkouri, Marouane Tliba, Bin Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scanpath similarity metrics are central to eye-movement research, yet existing methods predominantly evaluate spatial and temporal alignment while neglecting semantic equivalence between attended image regions. We present a semantic scanpath similarity framework that integrates vision-language models (VLMs) into eye-tracking analysis. Each fixation is encoded under controlled visual context (patch-based and marker-based strategies) and transformed into concise textual descriptions, which are aggregated into scanpath-level representations. Semantic similarity is then computed using embedding-based and lexical NLP metrics and compared against established spatial measures, including MultiMatch and DTW. Experiments on free-viewing eye-tracking data demonstrate that semantic similarity captures partially independent variance from geometric alignment, revealing cases of high content agreement despite spatial divergence. We further analyze the impact of contextual encoding on description fidelity and metric stability. Our findings suggest that multimodal foundation models enable interpretable, content-aware extensions of classical scanpath analysis, providing a complementary dimension for gaze research within the ETRA community.

---


### 160. [What do Language Models Learn and When? The Implicit Curriculum Hypothesis](https://arxiv.org/abs/2604.08510)

**<font color=#1a73e8>作者：</font>** Emmy Liu, Kaiser Sun, Millicent Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can perform remarkably complex tasks, yet the fine-grained details of how these capabilities emerge during pretraining remain poorly understood. Scaling laws on validation loss tell us how much a model improves with additional compute, but not what skills it acquires in which order. To remedy this, we propose the Implicit Curriculum Hypothesis: pretraining follows a compositional and predictable curriculum across models and data mixtures. We test this by designing a suite of simple, composable tasks spanning retrieval, morphological transformations, coreference, logical reasoning, and mathematics. Using these tasks, we track emergence points across four model families spanning sizes from 410M-13B parameters. We find that emergence orderings of when models reach fixed accuracy thresholds are strikingly consistent ($\rho = .81$ across 45 model pairs), and that composite tasks most often emerge after their component tasks. Furthermore, we find that this structure is encoded in model representations: tasks with similar function vector representations also tend to follow similar trajectories in training. By using the space of representations derived from our task set, we can effectively predict the training trajectories of simple held-out compositional tasks throughout the course of pretraining ($R^2 = .68$-$.84$ across models) without previously evaluating them. Together, these results suggest that pretraining is more structured than loss curves reveal: skills emerge in a compositional order that is consistent across models and readable from their internals.

---


### 161. [When Fine-Tuning Changes the Evidence: Architecture-Dependent Semantic Drift in Chest X-Ray Explanations](https://arxiv.org/abs/2604.08513)

**<font color=#1a73e8>作者：</font>** Kabilan Elangovan, Daniel Ting  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transfer learning followed by fine-tuning is widely adopted in medical image classification due to consistent gains in diagnostic performance. However, in multi-class settings with overlapping visual features, improvements in accuracy do not guarantee stability of the visual evidence used to support predictions. We define semantic drift as systematic changes in the attribution structure supporting a model's predictions between transfer learning and full fine-tuning, reflecting potential shifts in underlying visual reasoning despite stable classification performance. Using a five-class chest X-ray task, we evaluate DenseNet201, ResNet50V2, and InceptionV3 under a two-stage training protocol and quantify drift with reference-free metrics capturing spatial localization and structural consistency of attribution maps. Across architectures, coarse anatomical localization remains stable, while overlap IoU reveals pronounced architecture-dependent reorganization of evidential structure. Beyond single-method analysis, stability rankings can reverse across LayerCAM and GradCAM++ under converged predictive performance, establishing explanation stability as an interaction between architecture, optimization phase, and attribution objective.

---


### 162. [Cram Less to Fit More: Training Data Pruning Improves Memorization of Facts](https://arxiv.org/abs/2604.08519)

**<font color=#1a73e8>作者：</font>** Jiayuan Ye, Vitaly Feldman, Kunal Talwar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can struggle to memorize factual knowledge in their parameters, often leading to hallucinations and poor performance on knowledge-intensive tasks. In this paper, we formalize fact memorization from an information-theoretic perspective and study how training data distributions affect fact accuracy. We show that fact accuracy is suboptimal (below the capacity limit) whenever the amount of information contained in the training data facts exceeds model capacity. This is further exacerbated when the fact frequency distribution is skewed (e.g. a power law).
We propose data selection schemes based on the training loss alone that aim to limit the number of facts in the training data and flatten their frequency distribution. On semi-synthetic datasets containing high-entropy facts, our selection method effectively boosts fact accuracy to the capacity limit. When pretraining language models from scratch on an annotated Wikipedia corpus, our selection method enables a GPT2-Small model (110m parameters) to memorize 1.3X more entity facts compared to standard training, matching the performance of a 10X larger model (1.3B parameters) pretrained on the full dataset.

---


### 163. [UniversalVTG: A Universal and Lightweight Foundation Model for Video Temporal Grounding](https://arxiv.org/abs/2604.08522)

**<font color=#1a73e8>作者：</font>** Joungbin An, Agrim Jain, Kristen Grauman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video temporal grounding (VTG) is typically tackled with dataset-specific models that transfer poorly across domains and query styles. Recent efforts to overcome this limitation have adapted large multimodal language models (MLLMs) to VTG, but their high compute cost and limited video context still hinder long-video grounding. We instead scale unified supervision while keeping the model lightweight. We present UniversalVTG, a single VTG model trained with large-scale cross-dataset pretraining. An offline Query Unifier canonicalizes heterogeneous query formats into a shared declarative space, reducing linguistic mismatch and preventing the negative transfer observed under naïve joint training. Combined with an efficient grounding head, UniversalVTG scales to long, untrimmed videos. Across diverse benchmarks-GoalStep-StepGrounding, Ego4D-NLQ, TACoS, Charades-STA, and ActivityNet-Captions-one UniversalVTG checkpoint achieves state-of-the-art performance versus dedicated VTG models. Moreover, despite being $>100\times$ smaller than recent MLLM-based approaches, UniversalVTG matches or exceeds their accuracy on multiple benchmarks, offering a practical alternative to parameter-heavy MLLMs.

---


### 164. [What Drives Representation Steering? A Mechanistic Case Study on Steering Refusal](https://arxiv.org/abs/2604.08524)

**<font color=#1a73e8>作者：</font>** Stephen Cheng, Sarah Wiegreffe, Dinesh Manocha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Applying steering vectors to large language models (LLMs) is an efficient and effective model alignment technique, but we lack an interpretable explanation for how it works-- specifically, what internal mechanisms steering vectors affect and how this results in different model outputs. To investigate the causal mechanisms underlying the effectiveness of steering vectors, we conduct a comprehensive case study on refusal. We propose a multi-token activation patching framework and discover that different steering methodologies leverage functionally interchangeable circuits when applied at the same layer. These circuits reveal that steering vectors primarily interact with the attention mechanism through the OV circuit while largely ignoring the QK circuit-- freezing all attention scores during steering drops performance by only 8.75% across two model families. A mathematical decomposition of the steered OV circuit further reveals semantically interpretable concepts, even in cases where the steering vector itself does not. Leveraging the activation patching results, we show that steering vectors can be sparsified by up to 90-99% while retaining most performance, and that different steering methodologies agree on a subset of important dimensions.

---


### 165. [Ads in AI Chatbots? An Analysis of How Large Language Models Navigate Conflicts of Interest](https://arxiv.org/abs/2604.08525)

**<font color=#1a73e8>作者：</font>** Addison J. Wu, Ryan Liu, Shuyue Stella Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Today's large language models (LLMs) are trained to align with user preferences through methods such as reinforcement learning. Yet models are beginning to be deployed not merely to satisfy users, but also to generate revenue for the companies that created them through advertisements. This creates the potential for LLMs to face conflicts of interest, where the most beneficial response to a user may not be aligned with the company's incentives. For instance, a sponsored product may be more expensive but otherwise equal to another; in this case, what does (and should) the LLM recommend to the user? In this paper, we provide a framework for categorizing the ways in which conflicting incentives might lead LLMs to change the way they interact with users, inspired by literature from linguistics and advertising regulation. We then present a suite of evaluations to examine how current models handle these tradeoffs. We find that a majority of LLMs forsake user welfare for company incentives in a multitude of conflict of interest situations, including recommending a sponsored product almost twice as expensive (Grok 4.1 Fast, 83%), surfacing sponsored options to disrupt the purchasing process (GPT 5.1, 94%), and concealing prices in unfavorable comparisons (Qwen 3 Next, 24%). Behaviors also vary strongly with levels of reasoning and users' inferred socio-economic status. Our results highlight some of the hidden risks to users that can emerge when companies begin to subtly incentivize advertisements in chatbots.

---


### 166. [Demystifying OPD: Length Inflation and Stabilization Strategies for Large Language Models](https://arxiv.org/abs/2604.08527)

**<font color=#1a73e8>作者：</font>** Feng Luo, Yu-Neng Chuang, Guanchu Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains student models under their own induced distribution while leveraging supervision from stronger teachers. We identify a failure mode of OPD: as training progresses, on-policy rollouts can undergo abrupt length inflation, causing truncated trajectories to dominate the training data. This truncation collapse coincides with abrupt repetition saturation and induces biased gradient signals, leading to severe training instability and sharp degradation in validation performance. We attribute this problem to the interaction between student-induced data collection and the distillation objective, which implicitly favors long and repetitive rollouts. To address this issue, we propose StableOPD, a stabilized OPD framework that combines a reference-based divergence constraint with rollout mixture distillation. These together mitigate repetition-induced length inflation and further stabilize OPD training. Across multiple math reasoning datasets, our approach prevents truncation collapse, stabilizes training dynamics, and improves performance by 7.2% on average.

---


### 167. [Meta-learning In-Context Enables Training-Free Cross Subject Brain Decoding](https://arxiv.org/abs/2604.08537)

**<font color=#1a73e8>作者：</font>** Mu Nan, Muquan Yu, Weijian Mai 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Visual decoding from brain signals is a key challenge at the intersection of computer vision and neuroscience, requiring methods that bridge neural representations and computational models of vision. A field-wide goal is to achieve generalizable, cross-subject models. A major obstacle towards this goal is the substantial variability in neural representations across individuals, which has so far required training bespoke models or fine-tuning separately for each subject. To address this challenge, we introduce a meta-optimized approach for semantic visual decoding from fMRI that generalizes to novel subjects without any fine-tuning. By simply conditioning on a small set of image-brain activation examples from the new individual, our model rapidly infers their unique neural encoding patterns to facilitate robust and efficient visual decoding. Our approach is explicitly optimized for in-context learning of the new subject's encoding model and performs decoding by hierarchical inference, inverting the encoder. First, for multiple brain regions, we estimate the per-voxel visual response encoder parameters by constructing a context over multiple stimuli and responses. Second, we construct a context consisting of encoder parameters and response values over multiple voxels to perform aggregated functional inversion. We demonstrate strong cross-subject and cross-scanner generalization across diverse visual backbones without retraining or fine-tuning. Moreover, our approach requires neither anatomical alignment nor stimulus overlap. This work is a critical step towards a generalizable foundation model for non-invasive brain decoding.

---


### 168. [ParseBench: A Document Parsing Benchmark for AI Agents](https://arxiv.org/abs/2604.08538)

**<font color=#1a73e8>作者：</font>** Boyang Zhang, Sebastián G. Acosta, Preston Carlson 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI agents are changing the requirements for document parsing. What matters is \emph{semantic correctness}: parsed output must preserve the structure and meaning needed for autonomous decisions, including correct table structure, precise chart data, semantically meaningful formatting, and visual grounding. Existing benchmarks do not fully capture this setting for enterprise automation, relying on narrow document distributions and text-similarity metrics that miss agent-critical failures. We introduce \textbf{ParseBench}, a benchmark of ${\sim}2{,}000$ human-verified pages from enterprise documents spanning insurance, finance, and government, organized around five capability dimensions: tables, charts, content faithfulness, semantic formatting, and visual grounding. Across 14 methods spanning vision-language models, specialized document parsers, and LlamaParse, the benchmark reveals a fragmented capability landscape: no method is consistently strong across all five dimensions. LlamaParse Agentic achieves the highest overall score at \agenticoverall\%, and the benchmark highlights the remaining capability gaps across current systems. Dataset and evaluation code are available on \href{this https URL}{HuggingFace} and \href{this https URL}{GitHub}.

---


### 169. [OpenVLThinkerV2: A Generalist Multimodal Reasoning Model for Multi-domain Visual Tasks](https://arxiv.org/abs/2604.08539)

**<font color=#1a73e8>作者：</font>** Wenbo Hu, Xin Chen, Yan Gao-Tian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Group Relative Policy Optimization (GRPO) has emerged as the de facto Reinforcement Learning (RL) objective driving recent advancements in Multimodal Large Language Models. However, extending this success to open-source multimodal generalist models remains heavily constrained by two primary challenges: the extreme variance in reward topologies across diverse visual tasks, and the inherent difficulty of balancing fine-grained perception with multi-step reasoning capabilities. To address these issues, we introduce Gaussian GRPO (G$^2$RPO), a novel RL training objective that replaces standard linear scaling with non-linear distributional matching. By mathematically forcing the advantage distribution of any given task to strictly converge to a standard normal distribution, $\mathcal{N}(0,1)$, G$^2$RPO theoretically ensures inter-task gradient equity, mitigates vulnerabilities to heavy-tail outliers, and offers symmetric update for positive and negative rewards. Leveraging the enhanced training stability provided by G$^2$RPO, we introduce two task-level shaping mechanisms to seamlessly balance perception and reasoning. First, response length shaping dynamically elicits extended reasoning chains for complex queries while enforce direct outputs to bolster visual grounding. Second, entropy shaping tightly bounds the model's exploration zone, effectively preventing both entropy collapse and entropy explosion. Integrating these methodologies, we present OpenVLThinkerV2, a highly robust, general-purpose multimodal model. Extensive evaluations across 18 diverse benchmarks demonstrate its superior performance over strong open-source and leading proprietary frontier models.

---


### 170. [AVGen-Bench: A Task-Driven Benchmark for Multi-Granular Evaluation of Text-to-Audio-Video Generation](https://arxiv.org/abs/2604.08540)

**<font color=#1a73e8>作者：</font>** Ziwei Zhou, Zeyuan Lai, Rui Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-Audio-Video (T2AV) generation is rapidly becoming a core interface for media creation, yet its evaluation remains fragmented. Existing benchmarks largely assess audio and video in isolation or rely on coarse embedding similarity, failing to capture the fine-grained joint correctness required by realistic prompts. We introduce AVGen-Bench, a task-driven benchmark for T2AV generation featuring high-quality prompts across 11 real-world categories. To support comprehensive assessment, we propose a multi-granular evaluation framework that combines lightweight specialist models with Multimodal Large Language Models (MLLMs), enabling evaluation from perceptual quality to fine-grained semantic controllability. Our evaluation reveals a pronounced gap between strong audio-visual aesthetics and weak semantic reliability, including persistent failures in text rendering, speech coherence, physical reasoning, and a universal breakdown in musical pitch control. Code and benchmark resources are available at this http URL.

---


### 171. [Seeing but Not Thinking: Routing Distraction in Multimodal Mixture-of-Experts](https://arxiv.org/abs/2604.08541)

**<font color=#1a73e8>作者：</font>** Haolei Xu, Haiwen Hong, Hongxing Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Mixture-of-Experts (MoE) models have achieved remarkable performance on vision-language tasks. However, we identify a puzzling phenomenon termed Seeing but Not Thinking: models accurately perceive image content yet fail in subsequent reasoning, while correctly solving identical problems presented as pure text. Through systematic analysis, we first verify that cross-modal semantic sharing exists in MoE architectures, ruling out semantic alignment failure as the sole explanation. We then reveal that visual experts and domain experts exhibit layer-wise separation, with image inputs inducing significant routing divergence from text inputs in middle layers where domain experts concentrate. Based on these findings, we propose the Routing Distraction hypothesis: when processing visual inputs, the routing mechanism fails to adequately activate task-relevant reasoning experts. To validate this hypothesis, we design a routing-guided intervention method that enhances domain expert activation. Experiments on three multimodal MoE models across six benchmarks demonstrate consistent improvements, with gains of up to 3.17% on complex visual reasoning tasks. Our analysis further reveals that domain expert identification locates cognitive functions rather than sample-specific solutions, enabling effective transfer across tasks with different information structures.

---


### 172. [Act Wisely: Cultivating Meta-Cognitive Tool Use in Agentic Multimodal Models](https://arxiv.org/abs/2604.08545)

**<font color=#1a73e8>作者：</font>** Shilin Yan, Jintao Tong, Hongwei Xue 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The advent of agentic multimodal models has empowered systems to actively interact with external environments. However, current agents suffer from a profound meta-cognitive deficit: they struggle to arbitrate between leveraging internal knowledge and querying external utilities. Consequently, they frequently fall prey to blind tool invocation, resorting to reflexive tool execution even when queries are resolvable from the raw visual context. This pathological behavior precipitates severe latency bottlenecks and injects extraneous noise that derails sound reasoning. Existing reinforcement learning protocols attempt to mitigate this via a scalarized reward that penalizes tool usage. Yet, this coupled formulation creates an irreconcilable optimization dilemma: an aggressive penalty suppresses essential tool use, whereas a mild penalty is entirely subsumed by the variance of the accuracy reward during advantage normalization, rendering it impotent against tool overuse. To transcend this bottleneck, we propose HDPO, a framework that reframes tool efficiency from a competing scalar objective to a strictly conditional one. By eschewing reward scalarization, HDPO maintains two orthogonal optimization channels: an accuracy channel that maximizes task correctness, and an efficiency channel that enforces execution economy exclusively within accurate trajectories via conditional advantage estimation. This decoupled architecture naturally induces a cognitive curriculum-compelling the agent to first master task resolution before refining its self-reliance. Extensive evaluations demonstrate that our resulting model, Metis, reduces tool invocations by orders of magnitude while simultaneously elevating reasoning accuracy.

---


- [返回当日日报目录](./index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
