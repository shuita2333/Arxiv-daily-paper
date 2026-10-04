# 🧠 大模型相关研究 | 2026年10月05日

> 本类共 **384** 篇论文：已确认 **365** 篇，待复核 **19** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**301-350**（第 7/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-384](./part-08.md)

---

### 301. [Continuous Conditioning of VLAs with Augmenting EMG and Visual Task Descriptors](https://arxiv.org/abs/2610.01794)

**<font color=#1a73e8>作者：</font>** Edward W. Staley, Connor O. Pyles, Rahul Hingorani 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models rely strongly on language for describing task information, despite having multimodal inputs. We hypothesize that other modalities in the state space may present opportunities for supplemental task conditioning, which may be particularly relevant in cluttered or otherwise ambiguous scenes. We introduce two tuned models to test this hypothesis: (1) an electrophysiology-conditioned VLA (EC-VLA) that incorporates 8-channel electromyography envelopes as continuous conditioning input concatenated to the proprioceptive vector, and (2) a visually-annotated VLA (VA-VLA) that incorporates visual segmentation annotations to the image inputs. On a cube-selection task evaluated across three participants, EC-VLA matches a language-prompted baseline in uncluttered, in-distribution conditions and substantially outperforms it in cluttered, out-of-distribution scenes. Similarly, VA-VLA shows modest improvements over a language-prompted baseline in in-distribution scenes with substantial improvement in cluttered, out-of-distribution trials. Together, these results provide strong evidence for the potential benefit of task-conditioning beyond language.

---


### 302. [SkillEvoLean: Mutation-enhanced skill evolution for Lean provers](https://arxiv.org/abs/2610.01799)

**<font color=#1a73e8>作者：</font>** Kuo Zhou, ZiXion Yang, Lu Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Skill evolution offers a promising way to improve large language model agents without updating their parameters, but its use in formal theorem proving remains underexplored. Existing methods mainly target natural-language reasoning, improving skills by analyzing successful and failed trajectories and incrementally revising solving strategies. Although the Lean verifier provides reliable execution feedback, when all sampled trajectories fail, existing skill evolution methods lack successful trajectories from which to infer effective update directions. Furthermore, these methods also focus mainly on the root instruction file, thus underexploring the evolution of reference knowledge including mathematical concepts and proving techniques. To address these limitations, we propose a mutation-enhanced skill self-evolution framework for building skill-augmented Lean provers. The framework jointly evolves a high-level solving policy and its reference knowledge through progressive and mutation-based updates. Progressive evolution derives local improvements from successful and failed trajectories, while mutation is triggered when no complete proof can be generated, sampling mathematical concepts to produce and select new skill candidates under verifier feedback. We evaluate our method on MiniF2F, PutnamBench, the 2025 International Mathematical Olympiad (IMO 2025), and the 2026 USA Mathematical Olympiad (USAMO 2026). Under the same backbone model, trajectorysampling budget, and test-time compute, our method achieves proof success rates of 100.0%, 90.6%, 4/6, and 4/6, respectively, with GPT-5.5, outperforming the baseline methods. Further analysis shows that concept-guided mutation outperforms random-text-guided mutation by 6.9 and 8.2 percentage points on MiniF2F and PutnamBench, respectively, while solving one additional problem on both IMO 2025 and USAMO 2026.

---


### 303. [LineupRL: Verifiable Reinforcement Learning for Time Series Captioning via Caption-to-Series Identification](https://arxiv.org/abs/2610.01800)

**<font color=#1a73e8>作者：</font>** Haochen Zhang, Laura Yao, Zachary Plotkin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Time series captioning is a fundamental step in time series understanding and can also serve as the bridge between signal and natural language. Supervised fine-tuning (SFT) relies on a larger model's captions and cannot exceed their quality. Reinforcement learning (RL) can, but its rewards were designed for other modalities and other tasks, and they transfer poorly to open-ended generation in the time series domain. We address this by proposing LineupRL, a reinforcement learning with verifiable rewards (RLVR) pipeline whose reward is caption-to-series identification. The reward model is a frozen large language model (LLM) verifier that reads the generated caption and the candidate time series as raw values, never the chart, and must pick the described time series from multiple distractors. Matching is a far lighter demand on the verifier than writing questions or judging a caption, so an off-the-shelf LLM can supply the reward. Across two captioning benchmarks, and on forecasting and reconstruction where the predictor sees only the caption, LineupRL outperforms SFT and RL baselines on every metric. The 3B vision language model (VLM) trained by LineupRL also outperforms, at 1/24 of the parameters, the 72B VLM whose captions the SFT baseline is distilled from. Our case study shows that LineupRL resists reward hacking, and that the captioner it trains both traces the trend and names the values at key points.

---


### 304. [Beyond Linear Concepts: Discovering and Aligning Non-Linear Concept Manifolds in Large Language Models](https://arxiv.org/abs/2610.01821)

**<font color=#1a73e8>作者：</font>** Tido Specht, Elias Benedict Krey, Nils Neukirch 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding information processing in large language models (LLMs) requires dissecting the geometric organization of their internal token representations. While existing mechanistic interpretability (MI) methods seek to extract concepts, they are constrained by a strong linearity assumption challenged by evidence of non-linear feature manifolds. We move beyond linear concepts by adapting Non-Linear Multi-Dimensional Concept Discovery (NLMCD) from computer vision to token-level LLM activations, modeling concepts as low-dimensional manifolds. To compare concept manifolds across layers and models, we introduce a concept-based alignment (CBA) score, a generalized Rand index that measures geometric proximity without explicit feature matching. Our analysis yields six key findings: (i) a neighboring-layer sanity check shows CBA is more sensitive than PCA- or CKA-based linear baselines; (ii) layer-by-layer alignment matrices reveal two block structures in intermediate and late layers, consistent across models and obscured by linear metrics; (iii) concept composition remains syntax-dominated through most of the network before giving way to increasingly mixed syntactic-semantic concepts in later layers, with increasing output-orientation toward the final layers; (iv) multilingual concept sharing between English and Mandarin is training-dependent rather than universal, strongest in Qwen, weaker in Llama, and absent in GPT-2; (v) inter-model alignment mirrors this structure, with strong correspondence between same-family Qwen models of different scale but weak alignment across model families; and (vi) across Tulu-3 training stages, alignment is highest between adjacent stages, with the largest shift between the base model and SFT, while subsequent preference-alignment stages (DPO, RLVR) leave early layers largely unchanged and RLVR mostly preserves DPO's concepts in late layers.

---


### 305. [The Asymptotics of Language Model Alignment with Memory](https://arxiv.org/abs/2610.01828)

**<font color=#1a73e8>作者：</font>** Haricharan Balasundaram, V. Arvind Rameshwar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language model (LM) alignment broadly aims to perturb a given LM $Q$ into an aligned LM $q$ such that i) the outputs produced by $q$ and $Q$ are 'close' in probability, ii) $q$ has a higher expected reward than $Q$. Two common techniques for LM alignment are: KL-constrained RL, which requires knowledge of the LM distribution and is computationally expensive, and the best-of-$n$ algorithm, which requires only sampling from the LM. The work of Yang et al. established asymptotic closeness between the distributions produced by the two alignment methods for an $m$--length i.i.d. token sequence output by the LM, in the limit as $m$ increases to infinity. However, the i.i.d. assumption is not representative of practical LMs, whose output sequences often have memory. In this paper, we extend the asymptotic closeness result to the case when the $m$--length token sequence outputted by the LM is Markovian. Further, for finite-length output sequences -- particularly, when $m=1$ -- we provide a complete characterization of LM distributions and reward functions for which the KL-divergence between the distributions produced by the two alignment methods is zero -- a question first posed in Yang et al.

---


### 306. [Continuous Process-Level Evaluation for Evolving Enterprise AI Agent Skills](https://arxiv.org/abs/2610.01833)

**<font color=#1a73e8>作者：</font>** Ngoc Phuoc An Vo, Aarya Doshi, Vadim Sheinin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise AI agent skills evolve as tool APIs, models, and specifications change, yet final-output evaluation can miss process-level behavioral drift. We present a continuous evaluation framework combining outcome-level and process-level checks, applied to Revenue and Productivity variants of a Business Value Determination skill in an enterprise Value Aware Resiliency system. The framework independently computes per-run ground truth, materializes reusable template tests, and evaluates tool selection, arguments, execution order, and database integrity through programmatic checks and a narrowly scoped LLM judge. We evaluate 240 trials across two skills, two specification variants, two agent harnesses, and three models. Of 175 trials passing all applicable final numerical checks, 162 (92.6 percent; Wilson 95 percent CI: 87.7-95.6 percent) contained another evaluator-detected deviation. Under a broader seven-check final-state definition, 151 of 164 passing runs (92.1 percent; 95 percent CI: 86.9-95.3 percent) still violated a trajectory check. Dependency attribution reduced a mean of 6.34 failed checks per run to 2.65 roots. Specification sensitivity varied by model and harness, with exploratory bootstrap interaction intervals excluding zero for all three Revenue comparisons and one of three Productivity comparisons. Runtime-resolved templates provided reusable regression coverage across the evaluated configurations; longitudinal validation under actual API evolution remains future work.

---


### 307. [AVSD-Scenes: A Dataset for Audio-Visual Description of Urban Scenes](https://arxiv.org/abs/2610.01861)

**<font color=#1a73e8>作者：</font>** Dhanunjaya Varma Devalraju, Arshdeep Singh, Mark D. Plumbley  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Natural language descriptions can provide rich semantic representations of audio-visual urban scenes, yet datasets that jointly describe both auditory and visual information remain limited. In this paper, we introduce AVSD-Scenes, a paired audio-visual scene description dataset for urban environments. The dataset contains 12,291 audio-visual scene descriptions generated from the TAU Urban Audio-Visual Scenes dataset. To construct the dataset, we first generate audio- and visual-based descriptions using Qwen2-Audio-7B and Qwen2.5-VL-7B, respectively. These modality-specific descriptions are then combined using large language models, namely Qwen3-14B, Mistral-Small-3.2-24B-Instruct-2506, and Gemma-3-27B-it, to produce multimodal descriptions that capture complementary information from both modalities. We benchmark AVSD-Scenes using semantic alignment, cross-modal retrieval, scene classification, LLM-as-a-judge evaluation, and human subjective assessment. Results show that multimodal descriptions improve semantic alignment and cross-modal retrieval performance compared with modality-specific descriptions while preserving strong scene-discriminative information. The generated descriptions achieve up to 94.5% accuracy in urban scene classification, while combining audio, visual, and description embeddings further improves accuracy to 95.4%. Furthermore, the descriptions remain highly scene-discriminative even when scene labels are removed from the prompting instructions, indicating that they capture semantic information derived from the audio-visual content rather than merely reflecting label information.

---


### 308. [LiteReality-Agent: An Agentic System for Interactable 3D Indoor Scene Reconstruction](https://arxiv.org/abs/2610.01863)

**<font color=#1a73e8>作者：</font>** Zhening Huang, Yueyan Li, Johnathan Chiu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present LiteReality-Agent, an agentic system for reconstructing real indoor environments as realistic, articulated, and simulation-ready 3D scenes from RGB-D scans. At its core, LiteReality-Agent formulates 3D reconstruction as a coding problem, in which a coding agent gathers evidence using specialised tools and iteratively edits a Python script, this http URL, which can be executed to produce a 3D digital twin of the room. With this formulation, we develop a robust observe-edit-verify harness that supports evidence gathering, measurement, verification, layout optimisation, simulation readiness, and quality control throughout the reconstruction process. LiteReality-Agent produces high-quality reconstructions suitable for simulation and downstream embodied AI tasks. Furthermore, as agent capabilities continue to improve rapidly, the system introduced by LiteReality-Agent remains a strong orchestration framework for future agents: it equips them with specialised tools, structured workflows, and robust verification mechanisms that substantially improve reconstruction quality and reliability. We demonstrate that LiteReality-Agent produces reconstructions that are more geometrically accurate, visually realistic, and simulation-compatible than those generated by recent frontier models, such as Astra and Fable. We therefore view LiteReality-Agent as a practical and important building block for robust real-to-sim systems. Both the source code and the data-capture application are publicly available. Code:this https URL

---


### 309. [Walking the Embedding Space: Datastore Extraction from Multimodal RAG](https://arxiv.org/abs/2610.01871)

**<font color=#1a73e8>作者：</font>** Maria Carmen Jica, Ali Satvaty, Suzan Verberne 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multimodal Retrieval-Augmented Generation (MRAG) has emerged as a reliable and cost-effective technique of grounding the generative capabilities of Multimodal Large Language Models (MLLMs) into relevant, up-to-date, external knowledge. Despite presenting several benefits, such as reducing hallucinatory behavior, they also introduce new attack surfaces, including leakage of private information and vulnerabilities against data extraction attacks.
In this paper, we introduce $\immrag$, an adaptive and automatic data extraction attack procedure operating in a black box setting against \emph{image-returning} MRAG, a configuration in which the retrieved visual artifact is itself the response. Each query blends an attacker-held shadow image with an image already recovered from the system, and relevance-weighted resampling steers subsequent queries towards regions of the embedding space that still yield novel retrievals. Unlike current extraction attacks that aim to persuade the model towards data leakage by placing a malicious query as a textual prompt, $\immrag$ embeds the malicious instructions inside a user-given input image. We evaluate $\immrag$ on three plausible and distinct real-world scenarios: medical assistant, document-focused helper and general purpose tool. The experiments involve the study of the effectiveness of the attack on multiple CLIP-family retrievers, as well as the impact of various generators. A single 2500-query run reconstructs up to 611 distinct radiology images, 566 document scans and 416 general-purpose images under local-feature correspondence, and reaches up to $5.6\times$ as many distinct datastore items as a non-adaptive baseline. Our results show the urgent need for safeguards specifically designed for multimodal data.

---


### 310. [From Network Intrusion Detection to Blockchain-Backed Endpoint Detection and Response: Mapping the Landscape of Decentralized Detection-and-Response Architectures](https://arxiv.org/abs/2610.01872)

**<font color=#1a73e8>作者：</font>** Yahya Shahsavari, Sara Rouhani, Kaiwen Zhang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> While the literature on blockchain-assisted intrusion detection and prevention systems (IDS/IPS) for Internet of Things (IoT) and Industrial Internet of Things (IIoT) networks is mature, existing systematic reviews suffer from two critical limitations: they overlook the structural shift toward modern Endpoint Detection and Response (EDR) and Extended Detection and Response (XDR) architectures, and they conflate blockchain's distinct functional roles into a single monolithic category. This Systematization of Knowledge (SoK) addresses these gaps by proposing a three-axis taxonomy that classifies proposals by detection-system class (NIDS, HIDS, EDR/XDR), blockchain functional role, and response-automation maturity. Synthesizing research published in high-impact venues between 2019 and 2026, we provide a rigorous gap analysis exposing why a genuine per-endpoint blockchain-anchored response loop remains nearly nonexistent due to latency, deployment, and community mismatches. Furthermore, we evaluate structural, cross-cutting challenges persisting across the literature, including consensus latency on constrained devices, post-quantum cryptographic vulnerability, smart-contract attack surfaces, and the adversarial vulnerability of evolving LLM-based detection engines. Finally, we outline a comprehensive research agenda centered on hybrid on-chain/off-chain orchestration to bridge the gap between decentralized trust and rapid response automation.

---


### 311. [Where LLMs Fail with Visualization DSLs](https://arxiv.org/abs/2610.01873)

**<font color=#1a73e8>作者：</font>** Chang Han, Andrew McNutt, Katherine Isaacs  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As LLMs take up the role of authoring charts using visualization domain-specific languages (DSLs), the human constraints that shaped those languages may no longer apply, as what is easy for a person is not necessarily easy for a model. To understand how LLMs might work better with DSLs, we explore where and how they fail with current DSL designs. We evaluate 10 JSON-style visualization DSLs with 41 tasks across 3 LLMs, then assess the generated specifications with JSON and rendering checks, and qualitative coding of failed cases. Analyzing how this specification generation process fails, we identify four recurring failure patterns, link each to specific DSL features, and discuss design considerations for future DSL designs.

---


### 312. [Stochastic Rounding in Low-Precision Transformer Inference: A Variable-Precision Emulation Study of a Small GPT-2](https://arxiv.org/abs/2610.01889)

**<font color=#1a73e8>作者：</font>** Yohan Chatelain, Pablo de Oliveira Castro  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Should low-precision transformer inference use stochastic rounding (SR) or round-to-nearest (RN)? The answer depends on where in the network you look. We isolate this effect by holding the numerical format fixed and varying only the rounding rule at individual operation sites. To enable experiments at freely chosen precisions, we extend the PRISM vectorized rounding library to arbitrary virtual precision via a variable-precision stochastic rounding (VPSR) algorithm, proving that the rounding decision is evaluated exactly in hardware floating point.
We develop two analyses providing complementary insight into this site-level trade-off. First, a probabilistic forward-error bound for linear projections shows that SR's error envelope grows as $O(\sqrt{n} u)$ in reduction length $n$, versus $O(n u)$ for RN, a gap that widens rapidly at low precision and is most pronounced in the long multilayer perceptron (MLP) down-projection. Second, a second-order decomposition of expected cross-entropy loss change at the output softmax into signed drift, drift curvature, and a Fisher-weighted variance penalty reveals why the two sites behave oppositely: MLP noise is predominantly a uniform logit shift to which softmax is invariant, so SR's variance is largely discounted; head noise is non-uniform across the vocabulary and is not.
On DistilGPT-2 at $t=6$ significand bits, observations match theory: SR in the MLP raises perplexity to 1.15x the full-precision reference, versus 2.21x for RN. At the language-model head, the ordering reverses because SR introduces non-uniform variance, whereas deterministic RN carries none. In a mixed-precision configuration (MLP output at $t=6$), assigning SR to the MLP and RN to the head brings perplexity within 1.10x of the full-precision reference, a 28% reduction over matched-bit RN.

---


### 313. [Asynchronous LLM Post-Training: Group-Mass Capping and Convergence Analysis](https://arxiv.org/abs/2610.01896)

**<font color=#1a73e8>作者：</font>** Qijia He, Ruinan Jin, Jun Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Asynchronous reinforcement learning (RL) improves the efficiency of large language model post-training but introduces stale rollouts generated by earlier policies. Theoretical understanding of how this staleness affects convergence and how to mitigate its impact remains limited. We derive a convergence bound for GRPO-style algorithms that explicitly characterizes the tradeoff between the gradient estimator's second moment and bias. For trajectory-level importance-weighted estimators, our analysis shows that once the second moment is uniformly controlled, delay enters the bound through the bias introduced by clipping or rescaling. Guided by this insight, we propose a novel group mass capping GRPO (GMC-GRPO) method, which minimizes a ratio-based bias bound within a class of weighted estimators sharing a common second-moment guarantee. We establish convergence guarantees for asynchronous GMC-GRPO and show that, compared with TIC-GRPO, it improves the threshold dependence of the fourth-order delay term from $O(\epsilon^{-4})$ to $O(\epsilon^{-2})$ as $\epsilon\to0$, where $1+\epsilon$ is the ratio threshold. Under local policy overlap, the delay-dependent term decreases as $G^{-2/5}$ after tuning the step size, where $G$ is the group size. For fixed behavior and current policies, the bias introduced by group rescaling also vanishes as $G\to\infty$, whereas the bias from trajectory-wise clipping can persist. Experiments across Qwen3 models and reasoning benchmarks demonstrate improved robustness to stale rollouts, with GMC-GRPO achieving the best performance among stable baselines under large rollout delays.

---


### 314. [MoLE: Mixture of Latent Experts for Complementary Visual Reasoning](https://arxiv.org/abs/2610.01917)

**<font color=#1a73e8>作者：</font>** Yingcheng Liu, Tianyi Jiang, Yujuan Ding 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent visual reasoning equips vision--language models with continuous intermediate states that can process visual evidence without explicit textual reasoning traces or repeated image operations. However, existing methods often allow multiple latent tokens to access the same visual evidence through shared value projections, providing no mechanism for them to extract complementary visual information; simply increasing the latent budget can therefore yield redundant latent representations. We argue that effective latent reasoning should encourage different latent tokens to extract complementary visual information, and thereby act as specialized visual experts. Based on this insight, we propose MoLE, a Mixture of Latent Experts framework that controls both what visual evidence each latent visual expert observes and how it transforms that evidence. MoLE isolates latent visual experts during evidence extraction and uses dedicated latent summary experts to aggregate the complementary representations of latent visual experts. A two-stage training pipeline first forces visual evidence through this latent pathway and then restores direct visual access, requiring neither predefined expert roles nor intermediate visual targets. Across five visual reasoning benchmarks, MoLE achieves an average score of 78.6, outperforming data-matched supervised fine-tuning by 4.9 and the strongest evaluated latent visual reasoning baseline at the same latent budget by 3.6. Representation analyses show lower latent-state similarity and more diverse visual attention, while masking the latent pathway reduces average performance by 9.2. These results demonstrate that specializing latent computation is more effective than merely increasing the number of latent tokens.

---


### 315. [Cross-Lingual Alignment for Decoder-Only Models using MoE Routers](https://arxiv.org/abs/2610.01921)

**<font color=#1a73e8>作者：</font>** Lucas Bandarkar, Clark Peng, Ahmed Haj Ahmed 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cross-lingual contrastive learning has been a core component of multilingual encoder training, but the ability to explicitly align representations is not possible in decoder-only LLMs because of varying multilingual tokenization. However, a growing amount of research suggests that even in LLMs, higher cross-lingual representational alignment leads to improved cross-lingual transfer. In this paper, we propose a novel approach to reimagine cross-lingual contrastive learning given the architectural constraints of modern LLMs. Rather than applying an auxiliary alignment loss on hidden states, we propose using the outputs of the mixture-of-experts (MoE) routers as the target for alignment. Router outputs lend themselves better to pooling over many tokens, enabling more reliable cross-lingual comparisons at the sequence-level. Controlled continual pre-training experiments on four open-source MoEs show that incorporating this routing loss also aligns the underlying hidden representations across languages. Most importantly, this loss improves multilingual performance on our diverse evaluation suite, demonstrating the potential of cross-lingual MoE router alignment.

---


### 316. [Learning to Predict Distributions over Weight Updates for Test-Time Adaptation](https://arxiv.org/abs/2610.01934)

**<font color=#1a73e8>作者：</font>** Azal Ahmad Khan, Keshav Ramji, Tahira Naseem 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hypernetworks have recently shown success in dynamically adapting the parameters of Large Language Models (LLMs) at runtime based on signals such as task descriptions or additional demostrations. Here we ask: how much adaptation signal can be obtained using only the input query to an LLM?. To answer this, we study query-conditioned Hypernetworks for LoRA estimation. Further, we introduce distributional Hypernetworks, able to produce not only point estimates of parameter adaptors, but also a distribution over possible LoRAs. For this we propose a simple end-to-end loss using a differentiable Monte Carlo approximation and explore multiple distribution parametrizations including regression and convex combination variants. Results show that even using the mean of the learned distribution can outperform deterministic hypernetworks. Crucially, the learned distribution enables a different form of test-time scaling: instead of spending additional compute only by sampling more token sequences from a fixed model, we sample weight updates, yielding multiple adapted models for the same query. Performance improves as more weight samples are considered and remains stronger than corresponding token-sampling adaptation baselines. Finally, we find that generated updates can transfer across queries, suggesting that the hypernetwork learns reusable structure in how the model should adapt. Together, these results show that query-conditioned distributions over weight updates can support both adaptation and test-time scaling.

---


### 317. [Mapping the RAG Landscape: A Four Axis Taxonomy of Efficiency, Defense, Interactivity, and Reasoning](https://arxiv.org/abs/2610.01936)

**<font color=#1a73e8>作者：</font>** Meghana Sunil, Shravya V, Shravan Venkatraman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have demonstrated remarkable fluency across many tasks but remain limited by their static, parameter bound knowledge and their susceptibility to hallucinating information. Retrieval Augmented Generation (RAG) addresses these issues by incorporating external retrieval into the generation process, grounding model outputs in verifiable and up to date sources. While prior surveys primarily focus on core RAG architectures and standard pipelines, recent research explores broader challenges and capabilities that extend beyond these foundational designs. This survey provides a consolidated and structured examination of contemporary RAG developments, organizing the field into a four axis taxonomy: improving retrieval efficiency, strengthening robustness and security, supporting user driven and interactive workflows, and enabling multi step or complex reasoning. We formalize key components of the RAG framework and review methods spanning dense and sparse retrieval, fusion strategies, embedding optimizations, and reinforcement learning based retrieval policies, highlighting how these advances influence practical deployment and system design. We also synthesize evaluation practices, domain specific applications, and architectural variants such as Naive, Advanced, and Modular RAG. Finally, we outline persistent challenges related to retrieval quality, reliability, domain adaptation, scalability, and explainability, and identify opportunities for building RAG systems that are more reliable, adaptable, and transparent.

---


### 318. [A rubric landscape for evaluating clinical reasoning in large language models: what exists, what is missing, and what needs to be combined](https://arxiv.org/abs/2610.01938)

**<font color=#1a73e8>作者：</font>** Zhangshu Joshua Jiang, Zina Ibrahim, James T. Teo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Exam-style accuracy does not establish whether large language models (LLMs) reason well over clinical records. We define clinical reasoning as integrating and updating evidence across time and sources to form, revise and justify a patient's problem representation and a defensible plan.
This structured narrative review maps three literatures: medical education assessment instruments, clinical LLM benchmarks published from 2023 onwards, and general-domain methods for evaluating long-form generation. We examine six dimensions: problem representation, temporal synthesis, differential and management reasoning, counterfactual reasoning, calibrated uncertainty, and reasoning faithfulness. Preprints are included and flagged.
No single instrument covers all six dimensions. Problem representation and differential or management reasoning are reasonably covered, although reliability varies by instrument and setting. TIMER-Eval targets temporal synthesis, and ER-Reason assesses sequential diagnostic belief updating. Dedicated uncertainty and counterfactual evaluations are emerging, but their applicability to longitudinal free-text reasoning remains limited. Factual completeness is well theorised in general-domain evaluation, with early clinical evidence of important omissions. Faithfulness remains the weakest dimension, with one identified clinical causal-ablation study on multiple-choice questions.
Existing tools should be combined through binary rubric items, separate completeness and correctness scores, case-specific importance weighting with non-compensable safety caps, temporal order-consistency checks, and chance-corrected reliability reporting. Further design work is needed for calibrated uncertainty, counterfactual reasoning and faithfulness over longitudinal free-text records. This review provides a design rationale, not a validated instrument.

---


### 319. [Fewer Tokens, Better Action: GPT-6 Astra Robot Agents with 14% Higher Success Rate but 65% Fewer Tokens](https://arxiv.org/abs/2610.01939)

**<font color=#1a73e8>作者：</font>** Ruiyang Si, Jianxin Bi, Shunyu Yang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision language model (VLM) agents can control robots through visual feedback and action primitives, but repeated model invocations and redundant observations incur substantial token overhead. We introduce PyRUA-Lean, an interactive code-execution framework that couples feedback-driven primitive composition with selective observation: the agent composes classical robot primitives and learned vision-language-action (VLA) policies into Python cells that perform conditional checks and local retries, returning only explicitly requested images and state feedback for replanning. Across 700 simulated task instances from LIBERO-PRO, RoboTwin 2.0, and RoboCasa365, we compare PyRUA-Lean with a tool-calling baseline using the same GPT-6 Astra planner and underlying robot primitives. Under equal LLM-call budgets, PyRUA-Lean increases overall success from 63.1% to 71.7%. On instances solved by both agents, it uses 49% fewer LLM calls and 65% fewer input tokens.

---


### 320. [Anti-Persona: Disrupting Unauthorized Identity Binding and Recognition in Personalized Vision--Language Models](https://arxiv.org/abs/2610.01944)

**<font color=#1a73e8>作者：</font>** Abhishek Basu, Fahad Shamshad, Karthik Nandakumar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot personalization enables large vision--language models (LVLMs) to learn user-specific visual concepts for applications such as personalized retrieval and subject-aware querying. However, it also creates a privacy risk: an adversary can bind a target identity from a few reference images and subsequently detect that identity in new images through natural-language queries. We introduce Anti-Persona, an image-level defense against unauthorized identity binding and recognition in personalized LVLMs. Our key insight is that identity personalization relies on visual features shared across multiple reference images. We aggregate these features into an identity prototype and optimize visually subtle perturbations that disrupt prototype alignment in the vision-encoder space. Spatial smoothing and low-frequency preservation further promote visual fidelity and practical resilience to image compression. The resulting protection does not depend on a specific prompt and supports both proactive anti-personalization and reactive image protection. Experiments on two representative personalized LVLMs demonstrate protection rates of up to $95.0\%$ while preserving visual fidelity. The method remains stable across prompt variations and evaluated identity-query tasks, and improves black-box transfer under encoder mismatch.

---


### 321. [Latent JEPA: Abstract Future Prediction for Latent Reasoning in Chemistry](https://arxiv.org/abs/2610.01947)

**<font color=#1a73e8>作者：</font>** Xinjian Zhao, Yaoyao Xu, Xuemin Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models offer a promising foundation for chemical reasoning, bringing together chemical knowledge and multistep problem solving. Chemical intuition can provide an initial sense of plausible outcomes before the details of a solution are fully worked out. Inspired by how such expectations complement explicit analysis, we study how continuous latent thoughts can be trained to anticipate informative aspects of future solutions without verbalizing every intermediate step. We introduce Latent JEPA, a framework that combines autoregressive learning with joint-embedding prediction of one or more future views. For chemical reasoning, we develop textual and molecular prediction objectives that connect latent thoughts to both subsequent reasoning and molecular outcomes. Experiments on ChemCoTBench show gains in molecular optimization and on several editing and reaction metrics. Representation analyses show that future prediction makes latent thoughts more informative about molecular outcomes and strengthens their correspondence with chemical structure. These findings support abstract future prediction as a learning principle for connecting continuous latent reasoning with scientific outcomes.

---


### 322. [Do Your Own Research: Learning to Forecast by Learning to Search](https://arxiv.org/abs/2610.01955)

**<font color=#1a73e8>作者：</font>** Yusuf Afifi, Artur Kiulian, Anton Polishko 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Outcome-based reinforcement learning can train language models to forecast real-world events, but prior forecasting work either freezes research context before training or deploys agentic research only at test time, so the skill of gathering evidence is never shaped by the reward. We introduce an agentic forecasting environment, dataset, and harness built from 2,100+ resolved Polymarket questions; the agent acquires its own context at rollout time (web search, page reading, and financial time series, all restricted by layered leak filtering to information published before each question's cutoff), and we train Qwen3.5-35B-A3B (3B active parameters) on it with single-epoch GRPO under a Brier-score reward. Training changes how the agent interacts with information: calibration improves 30-40%, and search attempts fall from 3.8 to 2.25 per rollout as evidence discipline is learned. Evaluated in an identical harness against four frontier models, the trained policy also finishes ahead of every frontier model tested at evidence-based forecasting, including Claude Opus 4.5 (soft-Brier 0.254 vs. 0.256, n=265), at about 5% of the inference cost, and its margin is widest on the hardest questions, the ones the crowd itself had not decided. We release the environment, dataset, and per-rollout records as a reusable harness for temporal forecasting agents.

---


### 323. [SIEVE: Selective attention-value Suppression for Vision-Language Models Unlearning](https://arxiv.org/abs/2610.01962)

**<font color=#1a73e8>作者：</font>** Si Qi Goh, Cap Dang Xuan Kiet, Tat-Jen Cham 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The ability of vision-language models (VLMs) to associate visual identities with biographical information creates a need for selective unlearning of personally identifiable information (PII) while preserving permitted knowledge about the same individual. This setting is challenging because both sensitive and retained information can share the same visual inputs and intermediate representations. We introduce SIEVE, a simple and effective framework for selective VLM unlearning. SIEVE directly regularizes attention-value representations while also controlling model outputs. SIEVE suppresses attention values for forget examples toward a constant zero, while preserving retain-example representations by matching them to a frozen reference model. These objectives are combined with sequence-level forget and retain supervision, enabling targeted forgetting without largely affecting retained knowledge. Extensive experiments show that SIEVE achieves state-of-the-art performance on unlearning with multiple model-modality settings, while maintaining competitive retained utility. Ablation studies further show that value suppression and negative cross-entropy contribute complementary forgetting signals, while reference-based value matching substantially reduces utility degradation. These results demonstrate that attention values provide an effective intervention point for selective multimodal unlearning when sensitive and retained knowledge are closely related.

---


### 324. [Counterfactual Auditing of Bias in Open-Source Large Language Models for Clinical Triage](https://arxiv.org/abs/2610.01963)

**<font color=#1a73e8>作者：</font>** Manar Aljohani, Brandon Ho, Kenneth McKinley 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Emergency department (ED) triage is a high-stakes prioritization task in which demographic, socioeconomic, and system-context information may improperly influence acuity assignment. Although open-source large language models (LLMs) are increasingly considered for local and privacy-preserving clinical decision support, it remains unclear how counterfactual bias varies across model families, sizes, medical-domain models, and domain-adapted models. We present a comparative counterfactual audit of ten open-source LLMs for pediatric Emergency Severity Index (ESI) prediction. Starting from real and handbook-style clinical vignettes, we construct paired counterfactual variants that change only one injected demographic, socioeconomic, healthcare-access, behavioral, social, or system-context variable while holding the clinical presentation fixed. Models include Qwen2.5-7B, Qwen2.5-14B-Instruct, a QLoRA fine-tuned Qwen2.5-7B, MedGemma variants, MedLLaMA2-7B, GPT-OSS-20B, and GPT-OSS-120B. We measure any counterfactual shift, undertriage, overtriage, shifts greater than one ESI level, mean shift, and mean absolute shift. Counterfactual sensitivity varied substantially and did not consistently decrease with larger model size or medical-domain pretraining. The fine-tuned Qwen2.5-7B showed the lowest overall sensitivity, with a 5.27% any-shift rate and mean absolute shift of 0.0534, versus 16.02% and 0.1706 for the base model. Several larger or medical-domain models showed more significant shifts. Stratified and correlation analyses further revealed clinically important directionality and shared failure patterns hidden by aggregate rates. These findings support counterfactual auditing as a lightweight, clinically interpretable framework for comparing fairness risks in open-source LLMs before clinical deployment.

---


### 325. [FastCI: Efficient GPU-Intensive CI for LLM Training Frameworks](https://arxiv.org/abs/2610.01967)

**<font color=#1a73e8>作者：</font>** Tianshuo Qiao, Naiqian Zheng, Xiaopeng Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) keep growing in size and complexity, their training frameworks evolve at a rapid pace as well. Therefore, continuous integration (CI) is critical for maintaining the quality and stability of these frameworks. However, unlike traditional software, CI for LLM training frameworks relies on GPU-intensive tests, which usually involve complete model training or evaluation. This leads CI itself to become a new bottleneck for fast-paced development. In this paper, we introduce FastCI, a framework that improves the efficiency of CI for LLM training frameworks. FastCI leverages runtime evidence to select affected tests and prune tests that execute changed code in equivalent contexts. Then FastCI prioritizes high-risk tests to expose potential failures earlier, and optimizes test workloads along dimensions outside the intended validation scope of each test. Evaluated on the CI workload of our LLM training framework, FastCI reduces the CI latency by 77.5% and the GPU resource usage by 63.9%, while improving the modified code coverage retention by 3.2%, compared with the currently deployed CI pipelines. FastCI has now been integrated into the CI pipelines of our LLM training framework at ByteDance.

---


### 326. [Token-Level Video Reinforcement Learning](https://arxiv.org/abs/2610.01973)

**<font color=#1a73e8>作者：</font>** Yifan Wang, Gordon Guocheng Qian, Yanyu Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) for video generation usually assigns one scalar reward to an entire sampled video. Yet a video is not uniformly flawed: some visual tokens may already satisfy the prompt, whereas others require correction. A scalar reward cannot localize errors, causing optimization to perturb satisfactory tokens while under-targeting the tokens that actually need to change. We introduce Token-Level Video Reinforcement Learning, TVRL, a framework that derives token-level credit from the reward being optimized. Our key insight is that the answer likelihood of a frozen vision-language model provides both signals: its outputs contribute to the video-level reward, while magnitudes of its video-input gradients reveal which generated video tokens most affect that score. We instantiate TVRL in Group Relative Policy Optimization by averaging prompt-derived question rewards into one group-relative advantage and using detached, question-conditioned token-credit maps to reweight dense denoising-transition log-probabilities inside the clipped policy ratio. On VBench-2.0, TVRL achieves an Overall score of 57.69, outperforming the base model by 3.60 points. TVRL also improves matched GRPO baselines across three SDE samplers (SAGE, Flow, and Dance) by 2.68--3.15 points and across four reward models (VideoAlign, VideoScore2, UnifiedReward2, and Qwen3.5-9B) by 1.33--3.15 points.

---


### 327. [Universal Byte-Level Encoding: UTF-8/UTF-16 Routing to Reduce Cross-Script Token-Budget Disparities](https://arxiv.org/abs/2610.01984)

**<font color=#1a73e8>作者：</font>** Hyunsik Kim, Youngmoon Jung  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Byte-level byte-pair encoding (BBPE) tokenizers are attractive for multilingual large language models (LLMs) because they cover all Unicode text. In UTF-8-based BBPE, however, many scripts start from a higher fallback cost than English: when no learned merges can be applied, a multibyte character requires multiple byte-derived symbols. We call this worst-case pre-merge cost the encoding floor. A higher floor can increase token counts and per-request cost and shrink usable context. Changing the text encoding can reduce this gap, but a single global encoding can make already-efficient English spans more expensive in mixed-script text. We propose Universal Byte-Level Encoding (UBE), a dual-alphabet tokenizer that keeps 1-2-byte UTF-8 characters on the UTF-8 path while routing 3-4-byte UTF-8 characters through UTF-16. This lowers the encoding floor for 3-byte Basic Multilingual Plane (BMP) characters in scripts with high token premiums (token counts relative to English) without raising it for already-efficient spans in mixed-script text. UBE changes only the byte representation presented to byte-pair encoding (BPE); the merge rule remains standard, and exact decoding is preserved. UBE also composes with alternative boundary policies and morphology-based representations. In a Unicode 17 audit, UBE exactly round-trips all Unicode scalar values and all inputs in the official normalization, grapheme-break, and emoji test suites. Across intrinsic evaluations, UBE lowers dispersion in English-normalized token-count ratios, reducing cross-lingual token-budget disparity. In multilingual language model (LM) experiments, UBE matches BBPE's LM quality. In the main multilingual settings, UBE reduces token counts most for high-premium scripts and slightly lowers English token counts, yielding more usable context under fixed token budgets and faster prompt processing in content-matched benchmarks.

---


### 328. [From Reasoning Failures to Composable Video Spatial Intelligence](https://arxiv.org/abs/2610.01999)

**<font color=#1a73e8>作者：</font>** Pengzhan Sun, Junbin Xiao, Ramanathan Rajaraman 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial reasoning benchmarks evaluate vision-language models across diverse tasks, but task-level scores do not reveal which underlying capabilities account for success or failure. Each task requires recovering spatial evidence, representing geometry, and reasoning over it. We disentangle these capabilities by comparing predicted and ground-truth spatial context under a shared schema and coordinate contract. This comparison reveals four recurring sources of error: inaccurate perception, missing information in the spatial context, selection of the wrong measurement, and errors in reference frames or in tracking position and orientation. Guided by this diagnosis, we develop CROSS, a training-free library of typed geometric operators and spatial skills that function over available evidence to support reliable video spatial reasoning. The resulting library supplies verified context to non-coding VLMs or callable skills to a SpatialClaw agent. We evaluate \methodname{} on five benchmarks. \methodname{} raises the average score from 55.9\% to 60.2\% on ReVSI and improves the SpatialClaw result from 62.8\% to 66.3\% on DSI-Bench. These gains demonstrate that explicit handling of spatial conventions can repair systematic reasoning failures without additional training.

---


### 329. [Mingbird: A Local-First Agent Harness Enabling Small Open Models to Complete Real Tasks](https://arxiv.org/abs/2610.02001)

**<font color=#1a73e8>作者：</font>** Hao Wang, Ting Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Small open-weight models (2-9B) run on ordinary laptops, but under cloud-scale agent harnesses they rarely complete real tasks: tool prefill overflows the context, self-correction diverges, tool demonstrations loop, and tasks are silently abandoned. We present evidence, from a controlled single-machine comparison and one third-party benchmark, that a substantial share of these failures is attributable to the harness rather than the model. We introduce Mingbird, a local-first agent harness for Windows and Ollama whose ten mechanisms compensate point-by-point for small-model failure forms, three of them representative: a byte-level net-zero prefill budget, a finish gate that re-reads the task before accepting completion, and signature-level loop detection. On LRAB, a controlled comparison holding machine, models, budgets, and scoring fixed (4 harnesses $\times$ 4 open models (2B-35B) $\times$ 18 real tasks, deterministic artifact scoring), Mingbird reaches 0.886 overall against 0.631 (goose), 0.479 (opencode), and 0.405 (agent-mini), with all 288 cells published; on $\tau^2$-bench (278 tasks, three arms, one protocol) it totals 0.856 against 0.791 and 0.737; and a frontier-model probe on the same 18 tasks spans 0.997 to 0.478 across harnesses, with well-formed scaffolds staying within 0.072 of each other. A leave-one-mechanism-out ablation is reported as directional only: same-night replications of the same arm move its mean by up to 0.069, the size of every nominal single-trial delta, and the one batch-matched comparison (full mechanism stack versus text re-read alone) gives the executable completion guards a paired +0.10 across three replications. The evidence carries stated limits: a self-built benchmark, a single machine, and single-trial scoring.

---


### 330. [Mem++: Non-Destructive Memory for Long-Term Organizational LLM Agents](https://arxiv.org/abs/2610.02002)

**<font color=#1a73e8>作者：</font>** Ahmad Yehia, Aly O. Abdelkareem, Islam Ahmed 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents now take part in organizational work, where many authors record decisions across documents over months. Because a revised decision arrives as a new document rather than an edit, answering a question requires knowing which version held at a given time. However, most memory systems compress the record at write time. By distilling each document into facts, notes or graph edges, these methods fix what can be answered before any question is asked. To address this, we propose Mem++, a non-destructive memory framework shifting from write-time distillation to read-time selection. Mem++ stores every document whole with its date and author, and it calls no generative model at write time. At read time, it retrieves only documents dated up to the time a question asks about and fuses lexical and semantic rankings. Unlike systems that overwrite older versions, Mem++ keeps them and leaves the choice to the answering model. Evaluations on the organizational benchmark OrgMemBench demonstrate that Mem++ surpasses the strongest memory system baseline by 8.0 to 13.1 points across two answering models. With gpt-4.1-mini, it also achieves the best overall score, 2.6 points above RAG. In addition, Mem++ achieves the best average LLM-judge score on LoCoMo and ranks second on LongMemEval-S, behind only its entity-graph variant. Code for benchmark evaluation is available at this https URL.

---


### 331. [Counting Moves, Weighing Voices: Bayesian Dialectical Argumentation for Calibrated Multi-LLM Councils under Persistent Adversaries](https://arxiv.org/abs/2610.02005)

**<font color=#1a73e8>作者：</font>** Ionel Eduard Stan, Paolo Napoletano  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A multi-LLM \emph{council} lets several large language models (LLMs) deliberate on a question and return an answer together with a confidence estimate. As these systems become increasingly used for reasoning, that confidence should represent a calibrated \emph{probability of being correct}, and the decision should remain robust when some agents are persistently unreliable. Existing \emph{council aggregation} methods fail on both fronts: their confidence estimates measure decisiveness rather than correctness, and they cannot identify or discount persistently unreliable agents. We introduce Bayesian Dialectical Argumentation (BDA), which treats the council's \emph{typed} moves---who proposed, challenged, or conceded which answer---as observations of a classical annotator model with \emph{per-agent} reliabilities. This formulation recasts multi-agent deliberation as a reliability estimation problem, using the deliberation trace to infer agent reliability under persistent adversarial behavior. By weighting evidence according to inferred agent reliability, BDA yields calibrated posterior probabilities over candidate answers while allowing persistently unreliable agents to be inverted rather than merely outvoted. Across binary and multi-class benchmarks, BDA achieves the best calibration among zero-cost council aggregation methods, requiring no additional LLM calls, and improves robustness under persistent adversarial coalitions while remaining competitive in clean settings.

---


### 332. [On Language Drift during RLVR Post-Training](https://arxiv.org/abs/2610.02015)

**<font color=#1a73e8>作者：</font>** Michael Sullivan, Alexander Koller  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in LLM reasoning models---driven primarily by the paradigm of post-training via reinforcement learning with verifiable reward (RLVR)---have enabled them to accomplish impressively complex tasks. However, in parallel with their rising capabilities, LLMs have increasingly displayed signs of language drift in their chains of thought (CoTs): unusual, non-standard, and seemingly nonsensical language use. Although it is well-documented---and can potentially impair CoT monitorability---the causes of language drift are thus far poorly understood. In this paper, we identify the conditions under which language drift occurs: we prove theoretically that RLVR optimization pressure permits unbounded language drift, while supervised fine-tuning does not. We then show empirically that language drift specifically arises during RLVR on novel reasoning tasks---i.e. when the target behavior cannot be drawn out of the base model. Finally, we prove that it is not possible to constrain language drift without constraining expected reward, suggesting that CoT monitorability cannot be improved without harming performance during RLVR post-training at the frontier.

---


### 333. [Controllable Multi-label Video Safety Detection via Adaptive Tversky Policy Optimization](https://arxiv.org/abs/2610.02019)

**<font color=#1a73e8>作者：</font>** Guangyu Yang, Jingbiao Mei, Mingsheng Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid growth of video-based social media has increased users' exposure to harmful content, creating a need for reliable automated video safety detection. Although recent Vision-Language Models (VLMs) show strong video understanding capabilities, existing harmful video detection systems face two key limitations: they typically reduce safety detection to binary classification, overlooking the inherently multi-label nature of unsafe videos, and they rely on static training objectives that do not support controllable precision-recall trade-offs, though the desired operating point may vary across moderation pipelines and unsafe categories. To address these gaps, we propose Adaptive Tversky Policy Optimization (ATPO), a reinforcement learning framework for Multi-label Video Safety Detection (Multi-VSD). ATPO introduces the Adaptive Tversky Reward (ATR), which dynamically adjusts false-positive and false-negative penalties during training to enable controllable precision-recall trade-offs. Experiments on SafeWatch-Bench and XD-Violence show that ATPO substantially improves multi-label performance, increasing the Jaccard Index from 40.66 to 75.44 on SafeWatch-Bench-Real. Moreover, ATR enables reliable steering of the precision-recall operating point, supporting deployment scenarios with heterogeneous policy requirements. Code and checkpoints are provided at this https URL .

---


### 334. [Task-Adaptive Grounded 3D-Programmers Using 2D VLMs](https://arxiv.org/abs/2610.02021)

**<font color=#1a73e8>作者：</font>** Arman Raayatsanati, Sombit Dey, Anna-Maria Halacheva 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent vision-language models (VLMs) exhibit remarkable generalization and reasoning abilities, yet 3D understanding in these models is limited by data scale, training diversity, and reasoning capacity. Instead of naively extending these models into 3D, we take a different approach: we enable powerful 2D VLMs to operate reliably in 3D by introducing 3D grounding and iterative feedback loops with two novel concepts: Canonical Coordinate Framing (CCF) and Task-Adaptive Feedback (TAF). CCF serves as a unified visual representation that anchors both inputs and outputs to a shared Euclidean coordinate system, solving common challenges in 3D grounding such as axis ambiguity, inconsistent metric scale, and floating references. Complementary to this structured framing of the 3D inputs, TAF closes the reasoning loop with task-adaptive dynamic feedback that enables 2D VLMs to perform varied open-vocabulary tasks within their native visual context.
Building on this foundation, we introduce 3D-Prog, a 3D understanding, reasoning, and generation framework that jointly employs the capabilities of CCF and TAF together with powerful VLMs. Without requiring any retraining, 3D-Prog performs open-vocabulary 3D understanding, manipulation, and generation across both object-level and scene-level tasks. Our experiments show that the joint use of CCF and TAF transforms 2D VLMs into geometry-aware 3D programmers, achieving consistent, interpretable, and high-quality results across diverse 3D tasks.

---


### 335. [Old Ideas, Novel Problems: The Instability of LLM-Based Novelty Evaluation](https://arxiv.org/abs/2610.02022)

**<font color=#1a73e8>作者：</font>** Noy Sternlicht, Simra Shahid, Peter Jansen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated ideation systems are often evaluated on the novelty of the ideas they produce, and that judgment is increasingly delegated to large language models. Such judges are typically built ad hoc and validated, if at all, on human-authored papers rather than on the generated ideas they are meant to score. So, how do novelty judges perform?
Not well. We present a systematic controlled study of novelty evaluation design choices. We first build an evaluation set automatically, mining OpenReview for passages where reviewers explicitly affirm or dispute a paper's originality and keeping only submissions with unanimous agreement at the extremes of their research area; we pair these with ideas from a vanilla LLM generator. Across six judges, we find that small prompt design choices have large consequences; e.g., simply telling the judge that reviewers found one idea novel and the other not can change its verdict on more than half of the identical idea pairs it is shown, shifting pairwise accuracy by over 50 points and occasionally pushing it below chance. The same change helps one judge and hurts another. Retrieval and larger reasoning budgets help little, and two purpose-built novelty evaluators are outperformed by our cheapest prompted baseline. These results raise questions about reported novelty gains of automated ideation systems, and call for robust novelty evaluation methods.

---


### 336. [SPHERE: Adaptive VR Indoor Scene Generation via LLM-Enhanced Spatial Preference Learning and Human-in-the-Loop RL](https://arxiv.org/abs/2610.02023)

**<font color=#1a73e8>作者：</font>** Hyeonmin Lee, Zheng Wei, Kyungmin Kwon 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) advance 3D indoor scene synthesis, current pipelines fail to retain user-specific preferences across sessions, making immersive authoring a repetitive and physically fatiguing process. We present SPHERE, an adaptive VR generation framework that transforms isolated synthesis into continuous human-AI co-creation. SPHERE extracts persistent spatial preferences from natural multimodal interactions (speech and controller edits). To ensure geometric resilience against spatial distortions, it abstracts these raw edits into hierarchical constraints modeling both local functional and global topological contexts. Furthermore, a human-in-the-loop reinforcement learning mechanism dynamically updates retrieval policies based on the user's final edited scenes. A mixed-design user study ($N=42$) and an offline ablation demonstrate that SPHERE significantly reduces corrective edits and physical demand, preventing bias toward shallow object-level traits to yield geometrically resilient, profile-aligned layouts. Ultimately, SPHERE demonstrates how capturing demonstrated spatial logic enables controlled spatial adaptation, establishing a reliable, governed human-AI collaboration framework for immersive authoring. Project page and source code will be available at: this https URL

---


### 337. [Mimir: Physics-Grounded LLM Agents for Long-Horizon Irrigation Control](https://arxiv.org/abs/2610.02038)

**<font color=#1a73e8>作者：</font>** Yimeng Liu, Mi Zhang, Younsuk Dong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly combine reasoning, tool use, and action, but most evidence comes from episodic tasks with relatively immediate feedback and reset failures. Long-running physical control operates in a different regime: actions alter future states, errors compound across decisions, and an agent must improve from experience without being allowed to rewrite the physical rules that make execution safe. We study this regime through irrigation, where daily decisions interact with soil-water dynamics over entire growing seasons. We present Mimir, a physics-grounded LLM agent organized around two repair timescales. At the fast timescale, a structured physical interface and deterministic simulator turn an LLM output into a proposal that we numerically check, revise, and subject to bounded deterministic action selection before execution. At the slow timescale, recurrent failure patterns are consolidated into persistent contextual principles that condition future proposals, while the physical model, evaluator, and execution constraints remain immutable. Under a common retrospective evaluator across multiple sites, crops, and years, Mimir attains the lowest reported aggregate control cost among the evaluated references and uses about 51% less irrigation than the historical schedule replay. The ablation study show higher control cost when forward simulation, verified revision, or persistent context is removed; model-scale and model-family studies show no monotonic gain from increasing LLM size. The resulting lesson show that persistent physical agents can combine semantic reasoning with bounded, evidence-driven self-improvement while reserving physical truth and actuator authority for explicit numerical mechanisms.

---


### 338. [CARM: Cancellation-Aware Response Masking for LLM Reinforcement Learning](https://arxiv.org/abs/2610.02039)

**<font color=#1a73e8>作者：</font>** Yafei Zhang, Songshuo Lu, Sicong Liao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent years have witnessed the rapid adoption of reinforcement learning (RL) in large language model (LLM) post-training, with substantial gains in mathematical reasoning and code generation. In practical systems, however, policy updates and differences between rollout and training engines can make sampled responses off-policy. Sequence-level masking addresses this mismatch by deciding whether an entire response should contribute to optimization. A common masking rule uses the length-normalized geometric mean of sampled token probability ratios. Its signed log-ratios can cancel across positions, concealing substantial bidirectional policy drift. We propose \emph{Cancellation-Aware Response Masking} (CARM), a sequence-level mask that takes the absolute value of each token log-ratio before averaging, preventing opposing probability changes from canceling. We prove that accepted responses satisfy a joint bound on the fraction of sampled-token ratios outside a prescribed band and their mean log-distance beyond its boundaries. Experiments on mathematical reasoning and code generation show that CARM improves mean@16 averaged over AIME 2024/2025/2026 and BeyondAIME by up to $3.13$ percentage points over geometric-mean masking, and increases average pass@1 across four code benchmarks by $2.88$ points over the strongest evaluated baseline. These findings support CARM as a theoretically grounded and effective method for response-level off-policy control in LLM reinforcement learning.

---


### 339. [Typological Alignment of Stack-Based Language Models on Mildly Context-Sensitive Artificial Languages](https://arxiv.org/abs/2610.02040)

**<font color=#1a73e8>作者：</font>** Nadine El-Naggar, Tatsuki Kuribayashi, Ted Briscoe  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Some properties of languages, e.g., subject-object-verb (SOV) word order, are more prevalent than others among the thousands of attested natural languages (NLs). Such typological commonality is often attributed to learning biases. Computational simulations, recently with language models (LMs), have facilitated the exploration of this theory. In this paper, we extend existing analyses of the relationship between LMs' learning biases and typological commonality on both data and model sides, focusing on: (i) cross-serial dependencies, the upper limit of attested syntactic complexity, and (ii) stack-based LMs (SLMs), potentially facilitating learning of hierarchical patterns. We first evaluate generalization of SLMs on cross-serial dependencies across diverse artificial languages and confirm that they struggle with such constructions. However, SLMs with limited working memory generalize better suggesting a possible basis for such inductive bias and thus the typological commonality of some word order configurations.

---


### 340. [Form and Void: Entangled Composition through an Autonomous AI Agent](https://arxiv.org/abs/2610.02045)

**<font color=#1a73e8>作者：</font>** Shiwen Wang, Jian Yang, Xu Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Positive and negative space is a fundamental principle in visual composition, supporting visually coherent forms and layered semantic relationships. Generating such compositions is challenging because it requires coordinated control over two semantic concepts that share a common boundary. Although recent text-to-image models and multimodal large language models (MLLMs) have achieved strong performance in image generation and visual understanding, positive-negative space generation remains difficult, particularly under direct single-pass prompting. In this work, we present the \textbf{F}orm \textbf{a}nd \textbf{V}oid \textbf{A}gent (\textbf{FaV-A}), a multimodal agent designed for staged positive-negative space generation. FaV-A follows a progressive workflow: it first generates a base object, then analyzes its shape and spatial structure to identify candidate negative-space semantics, and finally produces compositional instructions for the final image generation stage. Experimental results and ablation analyses suggest that FaV-A provides a more effective framework than direct zero-shot MLLM baselines for producing visually coherent and semantically aligned positive-negative space compositions.

---


### 341. [HydroJEV: A one-second, training-free screen for cyber-attack and fault attribution in water distribution networks](https://arxiv.org/abs/2610.02048)

**<font color=#1a73e8>作者：</font>** Tianwei Mu, Shengyan Jiang, Mingzhe Yuan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When a SCADA alarm is raised in a water distribution network, operators must decide quickly whether it reflects a cyberattack, a physical fault, a normal transient or a faulty sensor. Supervised classifiers need labelled incidents that utilities rarely have, and frontier large language models (LLMs) take tens of seconds per decision. We tested whether Jev, a training-free model that returns class probabilities in about one second, can serve as the first tier of this triage. On a four-class cause-attribution benchmark built on the C-Town network in EPANET, Jev was compared with a hand-written rule tree, a supervised classifier and seven cloud LLMs on identical evidence in four sealed, pre-registered rounds. With only a label-free prior correction, Jev matched the rule tree (macro-F1 0.62-0.64 against 0.56-0.61 in distribution) and exceeded the supervised classifier by 0.36-0.42 on event subtypes absent from its labels, in all four rounds, and it outperformed the classifier whenever fewer than about four labelled events per class were available. Jev also decided 20-40 times faster than frontier LLMs. Accepting only benign Jev verdicts confirmed by the rule tree spared an LLM reviewer 35-38% of windows on fresh sealed sets without loss of macro-F1. Transferred unchanged to two further networks, this gated cascade stayed within the non-inferiority margin of its reviewer on all four sets. A fast, training-free screen can therefore take over about a third of the review load in SCADA anomaly triage while preserving the accuracy of deliberate review.

---


### 342. [External Observers May See More Clearly: Cross-Model Span-Level Hallucination Detection in Large Language Models via Hidden State Probing](https://arxiv.org/abs/2610.02066)

**<font color=#1a73e8>作者：</font>** Kingshuk Gupta, Davide Buscaldi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) increasingly serve as foundational reasoning engines, their tendency to hallucinate remains a critical vulnerability. While recent internal state probes offer a promising alternative to slow external retrieval systems, they largely reduce hallucination detection to a token-wise binary classification task, failing to capture the structured, sequential boundaries of semantic drift. Here, we introduce an internal hidden state framework for fine-grained, span-level hallucination detection. By inspecting layer-wise activation patterns, we attempt to detect the exact hallucination onset and continuation tokens in an LLM generation. Our experiments show that this approach successfully isolates hallucination onsets, achieving substantial improvements in Precision-Recall AUC over random baselines despite extreme class imbalance. Ultimately, we propose a novel cross-model detection framework in which one model observes the internal representations elicited by another model's generation. We find that an external observer can match or exceed a generator's self-detection of its own hallucination onsets, including when the observer is the smaller model, suggesting that self-detection is not the ceiling for onset localisation.

---


### 343. [Causal Memory Policy: Making Memory Utility Identifiable by Intervening on Retrieval](https://arxiv.org/abs/2610.02070)

**<font color=#1a73e8>作者：</font>** Arman Behnam, Binghui Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Memory-augmented large language models must decide which memories to retain, and recent systems do so by estimating each memory's effect on task performance. However, these estimates rely entirely on retrieved memories. When a memory is never retrieved, store-level interventions produce identical outcomes, leaving its utility unidentified. This is a retrieval-level positivity violation, invisible to diagnostics that examine only memory operations. We introduce Causal Memory Policy (CMP), a causal framework that restores identification by intervening on retrieval itself, reserving a fixed number of context slots for memories sampled with known propensities. CMP estimates memory utility by self-normalized inverse propensity weighting under a balanced assignment design. We prove the causal factorization of memory utility through retrieval, the unbiasedness and exact variance of the estimator, and the optimal decision rule under irreversible operations. Empirically, identification fails for 54% of required memories on LongMemEval and 67% on LoCoMo, and the failure persists in a deployed memory system. CMP improves discrimination between required and non-required memories from 0.54 to 0.66 AUC. Finally, we show that identified memory utility alone is insufficient for retention decisions: per-query utility reaches 0.78 AUC on the query for which it is estimated, yet no aggregation available to a retention policy predicts a memory's value on unseen queries. Code is available at: this https URL.

---


### 344. [LLM2Jev: LLMs Are Already Jev-Style Decision Models -- When and How to Fine-Tune Them](https://arxiv.org/abs/2610.02076)

**<font color=#1a73e8>作者：</font>** Yinheng Li, Justin Wagle  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Jev-style decision models return categorical probability distributions over predefined options without generating free-form text, enabling software systems to act on their outputs directly. In this work, we investigate the extent to which general-purpose LLMs already possess this capability out of the box, and when fine-tuning is actually necessary. We present LLM2Jev, an architecture-preserving framework that extracts calibrated decisions directly from next-token probabilities over bracketed numeric identifiers. LLM2Jev provides both a training-free inference recipe and a fine-tuning objective that optimizes candidate selection via a tree-factorized listwise loss while anchoring auxiliary predictions to the base model using KL divergence penalties. Evaluating on Qwen3.5-4B and Qwen3-0.6B, we find that modern LLMs are inherently effective decision models: without training, the 4B model matches community Jev-style models built on the same backbone, outperforms letter-logit readouts, supports arbitrary option counts, and natively handles multimodal decisions over images. Fine-tuning provides targeted rather than universal benefits -- substantially improving weaker models and specific tasks (such as many-option intent routing), but offering diminishing returns for strong backbones. Crucially, our KL anchors prevent behavioral degradation in conversational text generation, with LoRA delivering the strongest performance on capable models.

---


### 345. [GeoLatent: Geometry-Guided Latent Structuring with Routed Optimization for 3D Reasoning](https://arxiv.org/abs/2610.02091)

**<font color=#1a73e8>作者：</font>** Yakun Zhu, Yi Bin, Yujuan Ding 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite progress in vision-language models, 3D spatial reasoning from 2D images remains challenging. Text-based methods describe intermediate geometry with discrete tokens, limiting fidelity for continuous spatial relations. Continuous latents offer richer representations, but a single latent type does not explicitly separate the cues needed across spatial tasks. Decomposed spatial latents address this by representing position, direction, and global geometry separately under geometric supervision. Yet the geometry representation can still collapse toward one dominant direction, and unrestricted attention can leave the latents underused during answer learning. We introduce GeoLatent, combining Common--Residual Geometry Alignment (CR-GEO) with routed optimization to structure the geometry states while promoting latent-mediated answer learning. CR-GEO separates shared from residual teacher geometry; routed optimization jointly trains geometry and language, temporarily directs visual answer learning through the latents, and restores full attention with geometry supervision. In controlled comparisons, CR-GEO raises geometry effective rank from 1.00 to 3.87, while blocking latent readout at the bottleneck lowers direction accuracy from 89.1% to 25.8% on 128 fixed questions. After recovery, the differentiated geometry representation and latent-mediated visual route remain available alongside direct image access. GeoLatent achieves 73.0% on SPAR-Bench and 72.1% on SPBench, outperforming previously reported methods on both.

---


### 346. [Scalable, Transferable Meta-network for Data Selection Requires a Different Loss (and Why the Obvious Choice is Problematic)](https://arxiv.org/abs/2610.02092)

**<font color=#1a73e8>作者：</font>** Zilin Du, Bowen Yang, Boyang Albert Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Data selection is critical for training large language models on massive and heterogeneous corpora. Meta-learning for Training-data Selection offers a principled alternative to heuristic scoring by learning data weights from a target validation objective, but existing methods face a trade-off between fine-grained valuation and transferability to unseen data. A natural solution is to replace per-sample weights with a selection network. However, we find that directly incorporating such a network into existing MTS objectives leads to unstable optimization and poor generalization, caused by weight suppression and persistent reliance on easy-to-learn features. To address these issues, we propose Transferable Example Scoring and Selection (TESS), a scalable data-selection framework built on a Pointwise Value Matching objective (PVM). Experiments on LLM safety and targeted instruction tuning demonstrate strong transfer across datasets, from subsets to full corpora, and from smaller to larger models.

---


### 347. [Where-OPD: Spatially Guided On-Policy Self-Distillation of MLLMs with Synthetic Scenes](https://arxiv.org/abs/2610.02117)

**<font color=#1a73e8>作者：</font>** Sophia Sirko-Galouchenko, Monika Wysoczanska, Andrei Bursuc 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation has recently emerged as an effective approach for improving language-model reasoning by supervising students with a frozen or EMA version of themselves that receives privileged information. Its application to multimodal large language models (MLLMs), however, remains largely unexplored. Recent approaches use privileged visual information, such as image crops corresponding to a question, to improve fine-grained perception, but their gains are confined to tasks that benefit from such visual zooming and require either human-annotated grounding data or external teacher models. We introduce a different form of on-policy self-distillation for MLLMs that provides the teacher with textual, spatially grounded guidance identifying the visual elements relevant to a query. We use procedurally generated scenes with automatically available object identities and spatial coordinates, enabling scalable and annotation-free post-training. The teacher uses this spatial guidance to locate and integrate evidence from multiple relevant image regions, while the student learns to reproduce the resulting behavior from the image and question alone. Our approach consistently improves performance on counting, document and chart understanding benchmarks across multiple models. Importantly, although post-training uses only synthetic scenes, the resulting improvements transfer to real-world perception benchmarks, yielding a 3.23-point gain in average performance across CVBench, V*, ZoomBench, BLINK, HR-Bench, and MME-RealWorld. These results show that spatially grounded privileged information can induce broader perceptual capabilities through on-policy self-distillation, enabling substantial synthetic-to-real transfer beyond the task and data distribution used for post-training. Project page: this https URL

---


### 348. [Harnessing Domain Specialists in Multimodal Mixture-of-Experts for Efficient Adaptation](https://arxiv.org/abs/2610.02123)

**<font color=#1a73e8>作者：</font>** Damiano Marsili, Raphi Kang, Aditya Mehta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) architectures scale model capacity through sparse computation, routing each token through only a small subset of experts. In this work, we explore whether this sparsity gives rise to emergent intrinsic organization in multimodal MoEs. We find that experts develop strong semantic specialization across modalities and domains despite not being explicitly trained for modularity. Building on this structure, we introduce ExpertLens, a data-free method that identifies domain-specialized experts directly from pretrained model weights by decoding router weights into semantically meaningful vocabulary tokens. We leverage this specialization for efficient multimodal adaptation by selectively fine-tuning experts relevant to a target domain. Across math, medical, and remote sensing tasks, ExpertLens matches or surpasses full fine-tuning while updating only 21.7 - 47.0% of model parameters and achieving a 4.0x average training speedup, and outperforms LoRA in both adaptation performance and training efficiency. These results show that sparsity introduced for efficiency can give rise to semantic modularity that is directly useful for efficient adaptation.

---


### 349. [Local Support Learning](https://arxiv.org/abs/2610.02126)

**<font color=#1a73e8>作者：</font>** Assaf Ben-Kish, Akarsh Kumar, James Glass 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We explore catastrophic forgetting in the context of large pre-trained models. By considering forgetting as a geometric problem in the input space of each weight matrix, we uncover a natural retention objective under which updates produced by gradient-based optimizers are suboptimal. Following this observation, we propose Local Support Learning (LSL), a general-purpose framework that augments gradient-based training for retention of prior capabilities without access to prior data. During a new learning phase, LSL pairs two components with distinct roles: a standard weight adapter, trained as usual to minimize the loss, and a gating function that enables the adapter only on input activations from its own training distribution, making the update local to that distribution. The key challenge is that this gate must route data from all learning phases while training only on data from the current one. We address this with a gate based on a Gaussian Mixture Model (GMM), whose likelihood decays rapidly away from its training data, giving it a natural tendency to stay closed on data from prior phases. We show that this post-training approach can resolve forgetting in LLMs of up to 7 billion parameters, retaining both pretrained and finetuned capabilities across multiple training phases, while being efficient in memory and compute, robust to hyperparameter choice, and showing scaling potential.

---


### 350. [Keyword Harnesses Fail Open: A Cheap Diagnostic Ladder for Tool-Use Claims in Small Language Models](https://arxiv.org/abs/2610.02142)

**<font color=#1a73e8>作者：</font>** Juan S. Santillana  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Keyword-matching benchmarks can credit small models for tool use they never perform. We document such a false positive in a matched-architecture pair of Spanish security language models and propose a ladder of strict, cheap diagnostics. A 661.6M parameter model (approx. 65% code/technical text; no dedicated SFT) and a 1,109M model (web-heavy multi-phase curriculum; 6B-token tool-SFT) share decoder, tokenizer, and special tokens, scoring almost identically on lenient tool-use metrics (B4: 0.660 vs. 0.650).
Verbatim-reproduction checks on training examples separate them completely: the 600M emits valid tool calls with generalized arguments on 6/6 examples; the 1B does so on 0/6 across checkpoints. A first-token probe localizes the 1B's failure to a missing prior (prob. $10^{-4}$--$10^{-5}$ on <|tool_call|>), which was erased by its web-heavy training phase. A targeted SFT recipe (diverse corpus, 5x higher learning rate, 2,202 steps, ~3.3 GPU-hours) repairs the 1B using three orders of magnitude fewer tokens than the failed phase. On all 269 corpus rows, valid emission rises from 0.100 to 0.959 (600M: 0.926). On 238 unseen prompts, the repaired 1B passes 0.536 vs. the 600M's 0.428 ($p = 0.004$). Embedding-drift checks show the repair did not move the trigger token's tied embedding (97.7% of the bf16 table remains bit-identical), meaning changes live in the surrounding network.
Both models over-trigger, rarely answering negative prompts without a call (0.09 for 600M, 0.17 for repaired 1B). Factorial analyses confirm all repair configurations install the format, though suppression benefits from a diverse corpus remain a hypothesis due to seed sensitivity. This cheap diagnostic ladder costs minutes of CPU time and should gate tool-use claims on small models.

---


> [!TIP]
> 当前位于：**301-350**（第 7/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-384](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
