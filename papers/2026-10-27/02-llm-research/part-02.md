# 🧠 大模型相关研究 | 2026年10月27日

> 本类共 **204** 篇论文：已确认 **185** 篇，待复核 **19** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-204](./part-05.md)

---

### 51. [OpenHome: From Perception to Insight in Smart-Home Camera Videos](https://arxiv.org/abs/2610.31986)

**<font color=#1a73e8>作者：</font>** Xianglong Wang, Neil Rodrigues, Pei Guo 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision language models (VLMs) have been increasingly adopted in consumer smart-home camera systems to interpret recorded videos and provide insights. However, video clips captured from smart-home cameras are different from curated web videos dominating existing VLM benchmarks. Smart-home video clips often do not contain subtitles or narration and are captured from different viewing angles, under various lighting conditions, and in diverse scenarios. However, the capabilities of the model in this domain, under sparse visual signals and limited context, are not fully assessed by existing VLM benchmarks. To close this gap, we introduce OpenHome, a visual-only, four-option multiple-choice benchmark for evaluating smart-home video understanding. It contains 2,254 questions on 1,118 real-world video clips and organizes 10 tasks into three capability levels. Perception evaluates visible content, Reasoning evaluates causal, spatial, and temporal relationships, and Insight evaluates subject intent, supporting evidence and appropriate homeowner responses. Based on the dataset, we describe the task design, data pipeline and evaluation protocol, and report results for 32 closed-source and open-weight VLMs. The best model, Gemini 4 Argon, reaches 81.2% overall accuracy. Frontier closed-source models outperform open-weight models on every level. The best closed-source model leads the best open-weight model by 16.3% on Perception, 22.4% on Reasoning and 37.4% on Insight.

---


### 52. [TRACE: Data-Free Text Reconstruction Attacks against Approximate Unlearning in LLMs](https://arxiv.org/abs/2610.31995)

**<font color=#1a73e8>作者：</font>** Mengying Zhang, Derui Wang, Ibrahim Khalil 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) face growing demands for data removal driven by regulatory compliance, copyright concerns, and privacy protection, approximate unlearning has emerged as a practical alternative to expensive full retraining. In practice, pre- and post-unlearning model snapshots are often maintained for auditing and rollback, introducing a previously overlooked side channel. This paper demonstrates that approximate unlearning in LLM can leave residual traces within model snapshots, which may be recoverable and thus enable the privacy breaches that approximate unlearning is intended to prevent. Here, we propose TRACE, a framework that reconstructs unlearned training data given access to pre- and post-unlearning model snapshots, without any data-specific prior knowledge. To achieve this, TRACE identifies a compact set of candidate tokens from embedding-level parameter differences to constrain the search space, and assembles sequences via a contrastive scoring mechanism based on the perplexity gap between the two models. A two-stage exploration-then-completion strategy enables the recovery of multiple distinct samples. Extensive experiments on various datasets, including TOFU, MUSE, and WMDP, across multiple LLMs and six representative unlearning methods, demonstrate that TRACE achieves high-fidelity reconstruction. This paper exposes significant privacy risks in current LLM approximate unlearning deployments and highlights the need for defenses against parameter-difference leakage and appropriate management of model snapshot access.

---


### 53. [DraMaze: A Multi-Agent Pipeline with Future-Aware Memory for Diverse Microdrama Script Generation](https://arxiv.org/abs/2610.32002)

**<font color=#1a73e8>作者：</font>** Siyang He, Qiqi Wang, Fan Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid growth of microdramas has increased demand for high-quality script production. Long-form microdrama script generation with LLMs requires both diverse plot progression and long-range narrative coherence. Our observations reveal that candidate continuations increasingly concentrate on fewer narrative mechanisms as generation progresses, while conventional retrieval may reinforce trope reuse and overlook historical information essential to future plots. To address these challenges, we propose DraMaze, a multi-agent pipeline that explores diverse causal paths through trope memory-guided evolutionary tree search and mutation. It further constructs a Backward Narrative Dependency Tree to organize, retain, and retrieve historical memories based on future narrative goals. We also introduce MiDramaBench, a bilingual benchmark for evaluating script logic and creative quality across different script lengths, together with causal-pattern metrics for narrative repetition and diversity. Experiments show consistent improvements across three backbone LLMs. For 60-episode scripts of up to 60k words, DraMaze reduces causal-pattern repetition by 32.1% and achieves a Logic score of 82.5, outperforming the best-performing baseline by 8.5 points.

---


### 54. [CRM-Agent-Bench: Benchmarking Tool-Using Agents in Stateful Enterprise Environments](https://arxiv.org/abs/2610.32004)

**<font color=#1a73e8>作者：</font>** Monojit Banerjee, Zhujun Lan, Defu Cao  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Deploying language agents in real applications demands more than the right answer: an agent must execute a multi-step business process correctly, follow domain-specific rules, and interact with a user across a dialogue, where the gap between saying and doing is the gap between a satisfied customer and a real loss. We argue that a deployable-agent benchmark should jointly assess four facets: the outcome an agent reaches, the trajectory it takes, its operational viability, and its policy compliance. Customer relationship management (CRM), where mutable records meet operational rules and consequential effects, exercises all four. We introduce CRM-Agent-Bench, an execution-grounded benchmark of 555 stateful, multi-turn tasks across nine business domains and 36 capability tags. Each task supplies a task-specific executable contract drawn from checks over actions, arguments, order, response, target state, and protected state; success is the strict conjunction of the checks declared for that task. We evaluate the complete agent system through these contracts and report scored coverage, latency, and cost. Across sixteen systems evaluated on the audited final release, strict success spans 64.32% to 83.60%; the closely grouped leading systems nonetheless diverge sharply in cost and per-domain reliability. CRM-Agent-Bench offers an auditable framework for measuring contract-grounded business-transaction integrity and adherence to task-declared benchmark policies, with a portable structure designed for extension as models improve. Github repository: this https URL

---


### 55. [GS-MoE: Training-Free MoE Compression via Groupwise Subspace Sharing and Pruning](https://arxiv.org/abs/2610.32009)

**<font color=#1a73e8>作者：</font>** Carson Cary, Yukai Jin, Yihao Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models reduce computation through sparse activation, but storing their expert parameters remains a major memory bottleneck. We introduce GS-MoE, a training-free compression framework that addresses redundancy across and within experts through two compression axes: shared-subspace rank and expert intermediate width. Groupwise low-rank representations capture shared structure across experts while retaining expert-specific projections, and Nyström-based neuron compression reduces intermediate width within each expert. For fixed shared subspaces, we derive per-expert reconstruction-error reductions from the reconstruction objective and use them to guide expert grouping. Budgets are allocated hierarchically using a gradient-free layer-importance score to guide the allocation of rank and width budgets across layers, which eigenvalues and leverage then distribute as non-uniform ranks across groups and intermediate widths across experts. Experiments demonstrate the complementary benefits of compression along both axes, particularly at high compression rates on fine-grained MoE models. On DeepSeek-MoE-16B-Base, at a 60% reduction in total model parameters, GS-MoE retains approximately 90% of the uncompressed model's average reasoning performance, compared with 73% for D$^2$-MoE, while achieving 20% lower out-of-domain perplexity. We provide a code implementation at: this https URL

---


### 56. [MAGIC: Margin-gated Contrastive Debiasing with Evidence Restoration for VLM Test-time Robustness Scaling](https://arxiv.org/abs/2610.32013)

**<font color=#1a73e8>作者：</font>** Shunshun Gu, Enze Zhang, Ming Pei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper studies the problem of test-time robustness scaling for large vision-language models (LVLMs), which aims to mitigate language bias during inference. Existing approaches typically adopt test-time scaling techniques such as contrastive decoding to improve inference performance. Despite the progress, the performance of these approaches is far from satisfactory due to intentional evidence removal during perturbations and redundant inference cost. Towards this end, we propose a novel approach named Margin-gated Contrastive Debiasing with Evidence Restoration (MAGIC). The core of our MAGIC is to evaluate the decision margins of LVLMs to selectively activate textual and visual perturbation branches for efficient debiased inference. In particular, our MAGIC first measures the prediction margins of crucial tokens, and applies a gating function to identify low-confidence responses that are susceptible to language biases. For selected samples, we integrate the token logits from multiple textual and image perturbation branches with the original ones for debiased decision. More importantly, we selectively restore the most informative corrupted views with sharp prediction distributions for ambiguous samples after debiasing, enabling evidence recovery for discriminative decision-making. We further utilize a calibration dataset to actively identify and prune ineffective branches during contrastive debiasing for cost reduction. Extensive experiments on benchmark datasets validate the effectiveness of the proposed MAGIC in comparison with extensive baselines.

---


### 57. [SynMark: Semantic-Coordinate Multi-Bit Watermarking during LLM Code Generation](https://arxiv.org/abs/2610.32017)

**<font color=#1a73e8>作者：</font>** Rui Xu, Weizhi Liu, Zhaoxia Yin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-generated code is increasingly reused across downstream applications and often undergoes identifier renaming or structural refactoring, making robustness to functionality-preserving edits essential for generative multi-bit code watermarking. Existing methods commonly derive message routes from surface-token prefixes, so such edits can desynchronize routing and degrade watermark recovery. We propose SynMark, which replaces surface-dependent routing with learned semantic coordinates and further calibrates residual recovery errors after transformation. For watermark embedding, Scope learns semantic coordinates from aligned prefixes of functionally equivalent variants for keyed routing and applies a syntax-aware adaptive bias during generation. For watermark extraction, Traced recomputes semantic routes from transformed code and uses reliability-weighted aggregation to suppress unreliable token contributions. Under 100% identifier renaming, SynMark retains 82.27% and 83.77% BitAcc on CodeLlama and DeepSeek-Coder, respectively. Across three code LMs, it also improves clean BitAcc and Pass@1 by up to 4.53 and 11.18 percentage points over the strongest watermarked baselines.

---


### 58. [CEMIR vs. FISER: a comparative study of reasoning-based and enrichment-based approaches to pragmatic intent recognition](https://arxiv.org/abs/2610.32022)

**<font color=#1a73e8>作者：</font>** Ziya Hosseynzadeh, Farjad Fallah, Farnoosh Fallah 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Intent recognition in human-robot interaction requires agents to resolve ambiguous natural language instructions by inferring the speaker's underlying goals. Research has increasingly focused on two notable paradigms for addressing this task: structured symbolic reasoning and multimodal input enrichment. However, it remains unclear whether enrichment-based methods provide benefit in settings where the ambiguity concerns unstated human intent rather than missing observable scene information. In this paper, we present a comparative and diagnostic study benchmarking FISER - a framework utilizing structured social and embodied reasoning - against CEMIR (Context-Enriched Multimodal Intent Recognition), a method that performs multimodal enrichment by synthesizing narratives and photorealistic images from textual prompts. By evaluating both approaches across four Large Language Models (LLMs), ranging from Qwen2.5-Omni-3B to GPT-5, on the HandMeThat v2 benchmark, we analyze their capability to resolve pragmatic ambiguities. Our statistical analysis, employing multiple-comparison correction, reveals no statistically significant difference in performance between FISER and CEMIR across any model or difficulty level. This pattern holds across all sixteen model-by-difficulty comparisons, as well as in a targeted ablation isolating CEMIR's narrative and visual components. Instead, performance is primarily associated with backbone capability and the inherent difficulty of the ambiguity. These findings suggest a boundary condition for text-derived multimodal enrichment: when the relevant task constraints are already available in the textual instruction, synthetic multimodal augmentation may not provide measurable benefit over structured reasoning on the same text.

---


### 59. [RSI-Opt: Recursive Self-Improvement Optimizer Agents For Model Training](https://arxiv.org/abs/2610.32026)

**<font color=#1a73e8>作者：</font>** Binghang Lu, Yige Sun, Guang Lin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conventional neural-network training typically follows a predefined optimization recipe, motivating a LLM agent that monitors training dynamics and adjusts optimizer settings as training progresses, but a fixed agent policy does not accumulate experience across runs. We introduce RSI-Opt, a plug-and-play Recursive Self-Improvement Optimizer Agents which evolves the knowledge that guides this process: a prompt, a playbook of procedures, a library of tested optimizer code, and a decision cadence. A meta-agent rewrites this policy using evidence from earlier runs, and an archive retains evaluated policies for further evolution. Across 5 generations on three training tasks, the meta-agents develop reusable procedures and code and conduct their own CPU proxy experiments. RSI-Opt substantially improves optimizer-agent performance, with representative raw-space summary $z$-scores increasing from $+10.48$ to $+14.33$ on the evolution suite with Opus 5.5 and from $-0.36$ to $+3.11$ on held-out tasks with GPT-5.5 through cross-model policy transfer. On the Burgers PDE, it reduces mean relative $L_2$ error by approximately 2.7-fold with Opus 5.5 and 8.8-fold with GPT-6.1 over the fixed-prompt agent baseline, although PDE transfer varies across LLMs and tasks. Controlled comparisons show that the evolved policy combines reusable optimization knowledge with adaptation to each task: initial decisions capture most observed gains on seen tasks, while continued adaptation improves outcomes on unseen tasks. These findings demonstrate how procedures and executable tools accumulated across training runs can improve optimizer-agent performance and support transfer to scientific machine learning.

---


### 60. [Do AI-for-Science Agents Preserve Model Safety?](https://arxiv.org/abs/2610.32045)

**<font color=#1a73e8>作者：</font>** Michael Yew Chuan Lee, Manya Sriram, N. Benjamin Erichson  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI-for-Science agents are increasingly being used for formulating scientific hypotheses, running autonomous experiments, and interpreting evidence. These agents are constructed by integrating a large language model (LLM) into a domain-specific agent harness, which in turn can improve the LLM's scientific capability and enable the model to orchestrate scientific tools. In this work, we ask whether model safety is preserved when an LLM is integrated in an AI-for-Science agent harness. We evaluate five agent harnesses on 50 harmful chemistry requests. Specifically, we study how the safety behavior changes under direct prompting, two simple adversarial prompting strategies, and an adaptive attack. Across four recent GPT variants, our results show that the agent harness can increase harmful compliance even under direct prompting. More critically, we find that adaptive attacks that are largely unsuccessful against the base LLM suddenly become highly successful after the agent harness is introduced. Our results show that the safety behavior of the base LLM is not durable once a harness is introduced. Thus, as AI-for-Science agents become more capable and autonomous, the community needs to evaluate and align the agent using domain-specific safety benchmarks.

---


### 61. [Can Test-Time Memory Evolution Outperform Test-Time Training for Scientific Discovery?](https://arxiv.org/abs/2610.32046)

**<font color=#1a73e8>作者：</font>** Yepeng Liu, Shengmai Chen, Xuandong Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent \emph{test-time training} (TTT) frameworks have enabled open-weight large language models (LLMs) to outperform inference-only frameworks powered by frontier models on scientific discovery tasks. However, TTT introduces additional computational cost for online weight updates during the discovery process, making computational efficiency an important consideration when scaling to larger models. This motivates us to explore an efficient \emph{test-time adaptation} method for scientific discovery. We introduce \emph{Test-Time Memory Evolution} (TTME), a plug-and-play test-time adaptation method, as an alternative to TTT. TTME continually updates the external memory by distilling the experience to guide subsequent discovery without updating model weights. To have a clean comparison, we evaluate TTME and TTT under the same discovery framework, replacing only the test-time adaptation method. Our evaluation shows that TTME outperforms TTT on all five mathematical tasks, while reducing computational cost by $82.8$-$84.6\%$ in FLOPs and $47.7$-$58.4\%$ in runtime. These results establish TTME as an effective and computationally efficient alternative to TTT in the evaluated discovery settings.

---


### 62. [How Much Do You Trust A Dog? Quantifying Hint-Following in Reasoning Language Models](https://arxiv.org/abs/2610.32055)

**<font color=#1a73e8>作者：</font>** Anxin Guo, Chirag Pabbaraju, Sara Ahmadian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) often exhibit sycophancy, altering their answers to align with user suggestions even on objective factual and reasoning tasks. Yet the quantitative form of this influence--- and whether it is calibrated to source reliability--- remains poorly understood. In this work, we investigate this behavior through hint-induced answer shifts on MMLU questions, evaluating prompts of the form ``[Source] thinks the answer is (X)''. We systematically vary the source to which the hint is attributed (a professor, a friend, or a dog) across three open-source model families, Qwen, Gemma, and SmolLM. We show that the change induced by the hint follows a predictable structure well-characterized by an exponential tilt: the hint induces an approximately constant mean shift in the hinted answer's log-odds, with question--target susceptibility largely shared across sources. To explore how this pattern can arise, we introduce a formal decomposition of the hint response and illustrate in controlled synthetic experiments how KL-regularized reward-based training reshapes both hinted and unhinted answer distributions. Finally, we evaluate whether this shift is calibrated to source reliability, finding that the log-odds shift persists even when the hint-giver is declared inaccurate or accompanied by explicit warnings not to trust the source, highlighting the vulnerability of LLMs to adversarial steering.

---


### 63. [HyScale: Scaling Long-Context Training for Learned Sparse Attention](https://arxiv.org/abs/2610.32057)

**<font color=#1a73e8>作者：</font>** Yangsheng Deng, Xinjing Huang, Yulong Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present HyScale, a long-context training system for learned sparse attention. Learned sparse attention is a promising architecture for million-token contexts, widely adopted in production since DeepSeek-V3.2. Selection, however, grows into the training bottleneck. For each query, it scores every previous token whereas sparse attention reads only $k$; worse, current systems materialize a full score table and repeat selection during recomputation. Our key insight is that the output of selection is not an activation, but rather a set of indices. Building on it, HyScale introduces HyTopK and selection replay. HyTopK finds each query's exact top-$k$ on the fly without a score table, while selection replay reuses forward-pass selection in recomputation. Together with holistic system optimizations tackling end-to-end training challenges, HyScale speeds up GLM-5.1 training on 1M-token sequences by 2.07$\times$ over Megatron-LM on 512 H20 GPUs. It also speeds up the CSA layers of DeepSeek-V4-Flash and the QSA layers of Qwen3.8-Flash-Next by 2.01$\times$ and 1.57$\times$ at 1M tokens on 32 H800 GPUs.

---


### 64. [Understanding Communication Failures in Multi-Agent LLM Systems](https://arxiv.org/abs/2610.32060)

**<font color=#1a73e8>作者：</font>** Priya Pitre, Jun Hou, Yi Fang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems aim to improve reasoning through debate, evidence sharing, and mutual correction, but interaction can also introduce failures that final accuracy alone cannot explain. Agents may converge too early, ignore dissent, suppress correct minority answers, or preserve a wrong framing across rounds. We present a corpus-grounded taxonomy of communication failures, built from 3,211 failed multi-round trajectories across medical QA, coding, finance, multi-hop reasoning, ethics, and embodied text tasks. Using this taxonomy, we analyze failure distributions across datasets and system designs, round-level error dynamics, recovery hardness, majority transitions, minority-signal suppression, and self-reported confidence. We find that failures are dominated by recovery/correction and consensus/decision problems rather than isolated first-round mistakes, with many emerging after agents first observe peer responses. Based on these findings, we recommend stronger disagreement handling, evidence verification, minority-signal preservation, and recovery checks before finalization.

---


### 65. [SPA: Structure-Preserving Approximation of Gated Activations under FHE](https://arxiv.org/abs/2610.32065)

**<font color=#1a73e8>作者：</font>** Rui Li, Wenyuan Wu, Weijie Miao  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Nonlinear activation evaluation remains a major bottleneck in neural inference under fully homomorphic encryption (FHE). FHE supports efficient addition and multiplication, but lacks native operations for exponential functions, reciprocals, and value-dependent selection. High-degree polynomial approximations on fixed intervals are therefore commonly used to replace nonlinear activations. They can achieve small errors but often incur substantial multiplicative depth and latency. We observe that several widely used nonlinear activations share the algebraic structure $A(x)=xg(x)$ with $g(-x)=1-g(x)$. This class includes GELU, SiLU, fixed-parameter Swish, and the scalar nonlinear branches of GEGLU/SwiGLU. We propose \SPA{} (\emph{Structure-Preserving Approximation}) to exploit this shared structure. \SPA{} retains the exact odd component $x/2$ and approximates only the even residual as a polynomial in $x^2$, yielding a comparison-free arithmetic kernel. This construction removes redundant odd degrees of freedom and enables lower-cost polynomial evaluation at a given error target. Plaintext experiments with Gemma-4-E2B and Llama-3.2-3B show that SPA largely preserves downstream task performance without weight updates. Fixed-interval CKKS benchmarks show favorable error--latency trade-offs. On $[-5,5]$, \SPA{}-balanced achieves a $3.25\times$ speedup over MOAI (ICLR'~26) for erf-GELU with comparable error. On the same interval, \SPA{}-accurate achieves $79.22\%$ lower root mean squared error (RMSE) and a $10.40\times$ speedup over Euston (S\&P'~26) for QuickGELU. For SiLU, \SPA{}-accurate achieves $19.02\%$ lower RMSE and a $2.06\times$ speedup over THOR (CCS'~25).

---


### 66. [DriveMind: Mind-Evolving Belief Tracking for Closed-Loop Autonomous Driving](https://arxiv.org/abs/2610.32069)

**<font color=#1a73e8>作者：</font>** Yan Shi, Kehua Chen, Jiarui Qi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent multimodal large language models (MLLMs) can perceive a traffic scene, reason about it, and propose a driving action within a single model. However, existing MLLM-based drivers reason from scratch at each frame and commit to a single explanation, discarding earlier hypotheses about the scene. When the scene is ambiguous, the agent locks in on the wrong interpretation and acts on it before evidence accumulates. In this paper, we propose DriveMind, an MLLM-based driving framework that keeps several hypotheses about the scene alive at the same time and updates their weights as new frames arrive. Inspired by particle filtering, DriveMind propagates each hypothesis through a VLM, scores it against the current observation, and resamples to maintain diversity. On Bench2Drive, adding belief tracking to the same driving pipeline improves the Driving Score (DS) from 68.50 to 81.37 and the Success Rate (SR) from 41.36% to 54.09%. The largest gains occur on ambiguous scenarios such as unsignalized intersections (+20.0 DS) and oncoming-traffic interactions (+20.5 DS). Beyond the overall metrics, DriveMind also improves fine-grained interactive driving abilities such as merging, emergency braking, and give-way.

---


### 67. [Guided Zero-Shot Anomaly Explanation for Anonymized Crowd Video Monitoring: Context, Categorization, and Spatial Localization](https://arxiv.org/abs/2610.32073)

**<font color=#1a73e8>作者：</font>** Mulugeta Weldezgina Asres, Lei Jiao, Christian Walter Omlin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the promising development of deep learning for video anomaly detection (VAD), explainability (XAI) of these models remains a challenge. Explainable and privacy-protecting VAD builds transparency and trust that facilitates adoption of computer vision systems, including safety and security monitoring. However, anomaly explainability in privacy-preserving VAD systems is underexplored. In this study, we present the XAVAD approach, a unified descriptive anomaly XAI for an anonymized VAD, that integrates flexible zero-shot anonymization, anomaly type categorization, visual localization, and scene context description. We provide empirical and qualitative assessments of multifaceted explanations integrated with full-body visual anonymization for privacy protection. We adopt a multimodal CLIP embedding for videos, using improved LLM-assisted prompting and pool-scoring mechanisms for anomaly-type identification. We enhance Grad-ECLIP for spatial anomaly heatmap localization, leveraging computation and accuracy through our novel prompt-guided patching autofocus mechanism. We employ VLMs to generate context and reasoning descriptions of detected anomalies through curated prompt engineering. We have evaluated the accuracy and computational cost of XAVAD on several publicly available CCTV and video datasets. Our experiments demonstrate substantial gains of our XAVAD over state-of-the-art benchmark approaches and provide insights into privacy protection trade-offs in XAI for VAD. We further present ablation studies and assessments across diverse configurations and modeling alternatives to demonstrate the efficacy of our proposed methods. Code: this https URL}{this https URL .

---


### 68. [Label-Budgeted Attribute Inference from Protected Features in Edge-Cloud Split Multimodal LLMs](https://arxiv.org/abs/2610.32079)

**<font color=#1a73e8>作者：</font>** Junguang Yao, Peichun Hua, Hanxiu Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Edge-cloud split inference runs the early layers of a multimodal large language model (MLLM) on a device and sends intermediate features to a server to complete the task. While keeping raw images local is often perceived as a privacy benefit, an honest-but-curious server can still infer sensitive attributes, such as age, gender, and race, from the received features. Existing protections intervene at the input, transmitted representation, or model's responses, but their native evaluations rely on final-response refusals or fixed-classifier failures, which underestimate an adaptive server's capabilities. To address this, we propose a label-budgeted attribute-inference framework that measures representation-level privacy through a recovery curve: the share of the unprotected leakage the server recovers as a function of its labeled-sample budget, from zero (a classifier trained on unprotected features) to a full labeled set. Our evaluation across two popular MLLMs reveals two critical findings. First, in unprotected pipelines, intermediate features leak all three attributes regardless of the split depth. Second, even when protection mechanisms are deployed across different stages, sensitive information remains recoverable under limited label budgets. For example, Safe-LLaVA removes biometric content from the model's responses, but from the features it transmits in split inference, 20 labeled samples per class recover 75-85% of the unprotected leakage. This work provides a label-budgeted measure of feature-level privacy for split MLLM inference and motivates defenses that act on the transmitted representation.

---


### 69. [Behaviour analysis for large language model-driven agents](https://arxiv.org/abs/2610.32087)

**<font color=#1a73e8>作者：</font>** Tianqiang Yan, Lizhen Qu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Understanding language-agent behaviour requires learning how actions are organised across a trajectory and how this organisation relates to context and outcomes. We propose a general framework that connects data-driven behavioural discovery with analysis and experimental investigation. Categories developed from recorded activity define what is measured. Analyses preserve the behaviours' positions in the process and express their relationships as interpretable hypotheses. Statistical assessment and tests in held-out contexts examine the strength and scope of the evidence. Experiments, including prompt steering, then test how behaviour and outcomes change under deliberately varied conditions. A study of iterative self-reflection illustrates how discovery, dependency learning and prompt comparisons can inform one another. We develop this approach for trajectories of varying length, event order and agent roles, and identify advances in coding, analysis and experimentation needed to support its wider use.

---


### 70. [AgentTrace: Execution-Level Fingerprinting of Black-Box LLM Agents](https://arxiv.org/abs/2610.32092)

**<font color=#1a73e8>作者：</font>** Gejian Zhao, Hanzhou Wu, Xinpeng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Verifying the provenance of autonomous LLM agents is a critical security challenge. Existing semantic attribution is easily obfuscated by system prompts, while active watermarking conflicts with schema-constrained tool generation. We propose AgentTrace, an active framework that identifies the foundation model behind a black-box agent via observable execution traces. AgentTrace injects structurally ambiguous probes to trigger tokenization-sensitive serialization failures at rigid tool interfaces. While these initial failures provide coarse-grained separation across model families, the temporal sequence of subsequent repair operations reveals fine-grained, model-specific recovery behaviors. By modeling these multi-step trajectories with lightweight Markov chains, AgentTrace achieves 96.0% attribution accuracy under adversarial identity spoofing. Crucially, sequential repair modeling successfully distinguishes the evaluated intra-family variants sharing identical tokenizers (e.g., Llama-3 8B/70B), substantially outperforming unordered behavioral statistics while remaining robust against prompt obfuscation and temperature scaling.

---


### 71. [DELA: Learning Controllable Edits for Diffusion Language Models](https://arxiv.org/abs/2610.32096)

**<font color=#1a73e8>作者：</font>** Xinsong Feng, Chenan Wang, Leshu Tang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (DLMs) support bidirectional denoising and iterative refinement, but generation remains largely controlled by token-level masking schedules. This leaves draft-level refinement implicit and limits explicit control over when to insert missing content, delete redundant spans, revisit uncertain regions, or stop editing. We introduce Diffusion Editing Language Adapter (DELA), a plug-in framework that enables controllable draft refinement with a frozen DLM. DELA operates on clean, variable-length drafts using four explicit editing actions: Insert, Delete, Remask, and Stop. The controller determines when and where to edit the draft, while the frozen DLM fills masked regions through denoising, separating high-level edit control from token-level generation. A naive single-phase editor would be computationally expensive because arbitrary interior edits can disrupt prefix stability and limit reliable KV-cache reuse. To address this, DELA uses a two-phase decoding procedure: a fast, append-only drafting phase that supports KV-cache reuse, followed by a global refinement phase that enables targeted non-monotonic edits to the full draft. We train the controller using a staged curriculum that begins with learning local edit priors from synthetic recovery tasks and mined actions that improve draft quality. Subsequent stages refine edit selection through rollout-based outcome preferences and alignment with downstream task feedback. Experiments on mathematical reasoning and code generation show that DELA achieves gains of up to 5.5 percentage points over direct diffusion decoding while keeping the backbone frozen. DELA thus provides a modular approach to explicit draft-level control in diffusion language models.

---


### 72. [PRISM: Promoting Sampling Diversity of Large Language Models with Implicit Stochastic Modulation](https://arxiv.org/abs/2610.32101)

**<font color=#1a73e8>作者：</font>** Qixin Xu, Zihan Zhu, Xiaojiang Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) exhibit mode collapse, where their output distribution concentrates on familiar semantic modes. When diversity disappears, repeated sampling becomes semantic repetition rather than discovery, making rare but stronger solutions unlikely to surface and leaving self-evolution and continual learning difficult to sustain. Most remedies intervene only at inference time, shaping sam- ples without making diversity a model capability. We propose PRISM, a training-time framework that internalizes diversity within the model. PRISM combines (i) submodular curation that pairs each prompt with diverse-yet-correct multi-teacher solutions, and (ii) stochastic embedding modulation, which turns special-token perturbations into implicit signals for sampling distinct outputs. A theoretical analysis establishes the stability of this mechanism. On WritingPrompts and BookMIA, PRISM moves the quality-diversity frontier outward, achieving the best generation quality in all model-benchmark settings while maintaining the strongest or near-strongest semantic diversity across two open-weight model families. It also improves sampling efficiency on math and code benchmarks. Beyond inference, PRISM yields a stronger foundation for reinforcement learning, sustaining diverse rollouts and mitigating the diversity collapse commonly observed during RL training.

---


### 73. [ReMedI: Inference-Time Refinement and Self-Distillation for Controllable Molecular Optimization](https://arxiv.org/abs/2610.32103)

**<font color=#1a73e8>作者：</font>** Jia Yi Zhang, Shivanshu Shekhar, Allison McLevige 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In drug development, lead optimization must improve competing properties, such as increasing permeability and reducing toxicity, while limiting scaffold changes that could compromise the lead's potency. RL-based post-training, such as C-MORAL, addresses this problem by fine-tuning molecular language models to directly optimize molecular leads for objectives of interest, which relies on expensive task-specific datasets and faces challenges in achieving multi-objective optimization (MOO). We argue a pre-trained model may already contain useful molecular edits that zero-shot generation cannot efficiently reach. Motivated by the limited search capabilities of zero-shot generation, we develop an efficient Metropolis-Hastings search strategy to better explore the proposal distribution. We propose ReMedI, which uses the molecular language model as a base proposer for inference-time alignment. Given a lead and a set of multi-objective tasks, the model proposes edits conditioned on the current molecule, while Metropolis--Hastings refinement guides sequential edits under an objective for property improvement, preservation, and lead similarity. On both C-MuMOInstruct and SMDD benchmarks, refinement improves frozen base models across three backbones, reaching significantly higher multi-objective optimization success rates compared to baselines. These search traces can then distilled into the base model which improves zero-shot generation and subsequent search using approximately 7.8 times less training molecular leads than that of C-MORAL. ReMedI achieves approximately 2.8 times the strict-success coverage of RL baseline C-MORAL, including on out-of-distribution tasks, with matched lead-relative similarity.

---


### 74. [Putting Transformer Theories to the Test](https://arxiv.org/abs/2610.32104)

**<font color=#1a73e8>作者：</font>** Awni Altabaa, Tobias Schnabel, Kiran Tomlinson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Several formal theories have been developed to characterize the capabilities and limitations of the transformer architecture, each employing different abstractions that capture different features of the architecture. Due to the differences in their underlying assumptions and conceptual frameworks, these theories can disagree in their predictions about what tasks transformers find easy or hard. We map out seven theories of transformer capability (Star-free, $\mathsf{AC}^0$, $\mathsf{TC}^0$, C-RASP, MPC, BAPO, and Sensitivity) and translate their results into a common matrix of predictions across a suite of tasks covering different computational structures. We provide new theoretical results to complete this matrix. We then evaluate theoretical predictions through controlled experiments measuring in-distribution sample complexity, length generalization, and pretrained language model performance. We find that no single theory explains the observed pattern of successes and failures. When a theory does not capture the transformer behaviors relevant to a task, its predictions break down; for instance, we show that the $k$-hop induction task is predicted hard by C-RASP because it does not model content-dependent attention, but we train small transformers on this task that length-generalize. Similarly, theories assuming hard attention like $\mathsf{AC}^0$ and BAPO predict binary majority to be hard, for which we also find success in practice. Together, our results point to several specific features that a theory of transformers must capture: soft rather than hard attention, dynamic content-dependent retrieval, bounded computation at each position, an account of learnability and inductive biases, and a combination of upper and lower bounds.

---


### 75. [PersonaScienceBench: Evaluating Scientific Agents with Diverse Simulated Researchers](https://arxiv.org/abs/2610.32106)

**<font color=#1a73e8>作者：</font>** Siyang Wu, Weizhi Zhang, Chen Yang 等 32 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific agents collaborate with researchers whose expertise and preferences differ, but benchmarks usually hold the collaborator fixed. We introduce PersonaScienceBench: 200 tasks from five benchmarks across four scientific domains. Simulated researchers provide context and feedback according to persona profiles, while task objectives and grading remain fixed. Agents encounter researcher preferences only through conversation. Across eighteen modelconfigurations, task performance, fact recovery, and self-repetition reveal different strengths. Detailed GPT 6 Astra analyses show distinct agent responses across researcher profiles; interaction traces illustrate targeted clar ification and workflow revision. These behaviors can differ even when final scores match. PersonaScienceBench therefore evaluates how agents collaborate with diverse researchers alongside whether they complete the task.

---


### 76. [Beyond What to Say: Proactive Utterance Timing with Inner Thoughts for Werewolf Agents](https://arxiv.org/abs/2610.32107)

**<font color=#1a73e8>作者：</font>** Yoshiki Tanaka, Shuya Uchiyama, Daichi Hamaguchi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Participating in a conversation involves not only deciding what to say but also whether to speak at all. This judgment carries even greater significance in environments like the Werewolf game, where participants' interests conflict, because both utterances and silence are subject to interpretation and assessment by others. Therefore, determining when to speak, as well as what to say, is crucial for an LLM agent playing the Werewolf game. In this study, we introduce a Werewolf AI agent developed for the Anytime Utterance Track of the AIWolfDial shared task. Our system builds on the existing Inner Thoughts framework, which determines utterance timing during conversations by generating internal thoughts and evaluating the value of each thought for expression at that moment. Since existing methods were designed for general dialogue, we have redesigned the system specifically for the competitive environment and incomplete information setting of Werewolf games. We call our adapted method Adversarial Inner Thoughts. Through experiments involving analysis of self-play logs and human evaluations, we analyze and discuss the effectiveness of our approach.

---


### 77. [Context or Knowledge: How LLMs Attribute Their Own Answers](https://arxiv.org/abs/2610.32109)

**<font color=#1a73e8>作者：</font>** Kirill Afendulev, Alexey Dontsov, Alla Chepurova 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models can answer a question from a supplied document or from their parametric knowledge. When later asked where the answer came from, what determines their source report? We study this by intervening on the model's key-value (KV) cache after the answer is generated and before the source question is asked. On a controlled factual task with four models (7B-32B), changing or removing the document's cache never changes the report. In contrast, transplanting the question-and-answer (Q+A) cache between runs with identical question and answer tokens transfers it: every eligible report follows the donor, while the recipient's document is unchanged. On the two smaller models, steering Q+A values along directions fitted before any source question reverses 98.9-100% of reports across four document conditions at a fixed strength, while norm-matched random directions flip at most 1.1%. The components of keys and values along fitted directions carry the transplant effect: copying them alone nearly reproduces the report change; holding them fixed nearly prevents it. Applied during answer generation, the same value directions also change which source supplies the answer, though more weakly and depending on the prompt. Source reporting in this setting thus depends causally on cached state produced while answering. We do not establish general reporting accuracy or a complete interpretation of this state.

---


### 78. [Who Verifies the Tools? How Warped Formatters Mislead Agents and Their Verifiers](https://arxiv.org/abs/2610.32110)

**<font color=#1a73e8>作者：</font>** William Jeffries  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agents and verifiers often rely on the text a tool prints, and that text can misrepresent what the tool actually did, even when the tool's computation is correct. We saw this happen in a production RAG research system used by the Pilsudski Institute in New York, where tool output formatters misled an agent into giving wrong or incomplete information to users. Each tool did its job correctly, but its output omitted search limits, result caps, or identifier namespaces. We also recreated an unlabeled estimate caught in code review before release. We studied whether these formatters misled agents and verifiers and how much the repaired wording helps. We fed tool results to agents using two formatter versions: one with the key omissions and one with all missing details clearly stated. That difference alone changed what the agents claimed and what the verifiers accepted. Unsupported agent claims dropped substantially for three of the four failure types. In one test, verifiers went from accepting incorrect answers 90 out of 90 times to rejecting them 90 out of 90 times. A control showed the verifiers could catch the errors once they were given the missing facts and asked to judge correctness. We include the audit prompt we used with Codex and Claude Code in an exploratory demonstration, written with prior knowledge of our own system's defects. When pointed at an old version of our own system, it rediscovered the defects that were still live and surfaced twelve more we had not catalogued. When pointed at OpenClaw and Hermes, two of the best-known open-source agentic systems, it found warped formatters in both. We opened PRs to fix both, and the OpenClaw fix has already been merged. Practitioners can run the same prompt on their own systems today.

---


### 79. [REACT: Representational Early Analysis and Control of Chain-of-Thought Trajectories](https://arxiv.org/abs/2610.32113)

**<font color=#1a73e8>作者：</font>** Hanwen Zhang, Enyi Jiang, Ruike Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) generation offers an opportunity to intervene before a reasoning model completes its answer. But does the point at which risk is easiest to detect also offer the most effective control? We study this question with REACT, a conditional activation intervention that learns a safety direction from paired safe and unsafe trajectories and applies it once to an early CoT hidden state. The model weights remain frozen, and all subsequent tokens are generated without further edits. To study timing, we train directions separately at each of the first five CoT positions and evaluate ungated edits with full post-edit regeneration. Across three distilled reasoning models and three generation seeds, the strongest gains concentrate in a two- to three-token early window; on DeepSeek-R1-Distill-Llama-8B, the effect falls to approximately zero at the fourth and fifth tokens, even though later states can be more predictive of risk. This separates risk readability from effective control: intervention timing must be evaluated through its effect on subsequent generation. On the same 8B model, REACT raises the rate of fully safe CoT-answer outputs on StrongREJECT-273 from 29.06% to 82.05%, while keeping benign refusal and usefulness near baseline. An anonymized implementation is available at this https URL.

---


### 80. [Tampered ML: Evaluating LLM Judgment of Machine Learning Research](https://arxiv.org/abs/2610.32114)

**<font color=#1a73e8>作者：</font>** Soroush Ebadian, Parand A. Alamdari, Joe Benton 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> One approach to accelerating progress on AI alignment is to automate parts of alignment research itself. Doing so requires systems that can perform reliably on hard-to-supervise research tasks, including identifying flaws in research proposals and evaluating whether a proposed experiment supports its intended claim. To evaluate this capability, we introduce Tampered ML, a benchmark of 1,858 item-pairs, each consisting of an experiment proposal reconstructed from a published machine learning paper and a minimally edited counterfactual that introduces a targeted methodological flaw. Models must identify the more methodologically sound proposal in both presentation orders. A human validation study on a stratified sample estimates that 86% of items are valid (95% CI: 81-91%). Frontier models perform above chance but remain far from reliable (with Opus 5 achieving 77.9% accuracy). They are highly sensitive to the order of presentation and favor flawed designs that appear more specific, transparent, or conventional.

---


### 81. [Semantically Rich, Metrically Affect-Blind: A Geometric Blind Spot in Modern Text Embedders](https://arxiv.org/abs/2610.32122)

**<font color=#1a73e8>作者：</font>** Mahdi Naser Moghadasi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We report a systematic dissociation in modern text embedders: sentiment is almost perfectly decodable from their embeddings, yet almost entirely absent from their metric. Across eleven frozen encoders spanning 2021 to 2026, including 2026-generation models and the 4B-parameter LLM embedder Qwen3-Embedding-4B, a linear probe recovers sentence polarity at up to 91.3% accuracy while cosine similarity separates polarity by a margin of only 0.003-0.064. Qwen3-Embedding-4B, the strongest probe in the panel, reaches 91.3% probe accuracy but only 64.3 retrieval MAP. Because retrieval, clustering, deduplication, and retrieval-augmented generation operate on the metric rather than on a trained probe, these systems are effectively blind to information their encoder demonstrably contains. A task-conditioning control suggests this reflects the pretraining objective rather than a prompting artifact: conditioning Jina-v5 on its classification task rather than its retrieval task recovers only about half of the MAP gain that injection achieves on the same weights (63.2 to 73.8, versus 85.1), and leaves the alignment gap essentially unchanged. Sentiment-Injected Sentence Embeddings (SISE) train a small (0.13M-0.69M-parameter) supervised-contrastive head on a frozen encoder in seconds on a CPU, using the labelled training set. The head improves every encoder released since 2022 on full-data probe accuracy (up to +5.8 points), retrieval MAP (up to +26.0) and polarity margin (7-61x). This is a specialization, not a free gain: the compact 128-d head loses 38-41 Spearman points on STS-B, while a fused variant that concatenates it with the base embedding loses 2.4-12.0. With the head, a 0.6B encoder at 128 dimensions matches a 4B encoder given the same head (91.8 vs. 90.3 MAP). We release a CPU-reproducible pipeline and a reusable diagnostic, the Attribute Alignment Gap.

---


### 82. [MPQ: A Message-Passing View of Post-Training Quantization](https://arxiv.org/abs/2610.32127)

**<font color=#1a73e8>作者：</font>** Yanshuo Chen, Chenxi Liu, Reza Shirkavand 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Post-training quantization (PTQ) is a key technique for efficiently deploying large language models, as it compresses weights into low-bit representations without retraining. Existing PTQ solvers, including GPTQ, LDLQ, and block coordinate descent, commit each weight block to a single codeword before its neighbors are considered, leaving near-optimal alternatives unexplored. In this work, we cast row-wise PTQ as posterior inference over discrete codebooks, in which existing solvers correspond to a zero-temperature, hard-decision limit retaining only the top codeword per block. We propose Message-Passing Quantization (MPQ), which preserves soft posterior information across blocks during inference and commits to hard codewords only at the output stage. MPQ first uses vector approximate message passing to compute approximate blockwise posteriors, then refines a hard-decision initialization by exact block coordinate descent. Across 2-bit lattice and 3- and 4-bit scalar quantization on dense language models from Llama, Qwen, and Mistral families, MPQ improves perplexity and zero-shot accuracy over strong hard-decision baselines, and composes favorably with preprocessing techniques such as activation-aware scaling and incoherence processing. Our implementation is available at this https URL.

---


### 83. [From Noisy Retrieval to Decision Evidence: Silver Evidence Demonstrations for In-Context Learning](https://arxiv.org/abs/2610.32128)

**<font color=#1a73e8>作者：</font>** Masoud Monajatipoor, Fazlolah Mohaghegh, Hamid Reza Hassanzadeh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> RAG and retrieval-augmented few-shot ICL can struggle when decision-relevant evidence is buried in long, noisy context. Retrieved passages and demonstrations may contain redundant or distracting information. Although expert-labeled development examples may identify the text supporting each decision, these annotations are typically used only as answer-side rationales rather than as supervision for filtering noisy retrieval. We propose silver-evidence demonstrations, which replace raw retrieved passages in ICL examples with generated, target-conditioned evidence summaries. For each labeled development example, an LLM generates silver evidence without access to the expert label or gold evidence; this evidence is then paired with the expert label and gold evidence where available. At test time, a single structured call generates silver evidence from retrieved passages and then predicts the final label and decision evidence. Across EI 2.0, SciFact, synthetic policy retrieval, and HICRIC/IMR data, our full method improves over equally sized gold-only ICL (label-only for policy) on three of four datasets and improves evidence F1 on all annotated datasets. It also achieves higher mean label accuracy than InstructRAG-style ICL on all four datasets. These results suggest that replacing demonstration-side retrieved passages with compact, target-conditioned silver evidence is particularly useful for decisions based on long and noisy text, where it reduces distracting context while preserving decision-relevant signals and expert supervision.

---


### 84. [Shorter Is Not Cheaper: A Controlled Comparison of Declarative Animation Specifications and Free-Form Code for LLM-Generated Explanations](https://arxiv.org/abs/2610.32129)

**<font color=#1a73e8>作者：</font>** Jiantang Huang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chat assistants increasingly answer conceptual questions with interactive, animated explanations, generated either as free-form HTML/JavaScript or as declarative specifications that a fixed runtime plays. The declarative route is widely expected to be cheaper, faster and more reliable, because its outputs are shorter and constrained. We test this expectation in controlled comparisons whose hypotheses and analysis plans were frozen before the runs. We designed ExplainSpec, a time-indexed declarative animation format, and an observation contract that makes every generated explanation programmatically inspectable; validated, pacing-agnostic checkers score 20 explanation requests from five domains. Three Claude models (360 jobs) and, in a follow-up, the open-weight Qwen3-14B with thinking enabled and disabled (240 jobs) answered every request in both formats. For every model the specifications were 25-48% shorter in answer tokens (output excluding reasoning), yet with reasoning enabled total output fell significantly only for the largest Claude model and no model generated significantly faster. The reasons differed. The Claude models reasoned far more before writing specifications (exploratory; for the two larger models, from 15-20% to 85-88% of generations). Qwen3-14B reasoned about as much in both formats (a pre-registered test of this shift was not supported), and its shorter answers saved little against a reasoning trace more than twice as long. Nor were specifications more reliable: free-form pages were valid after one repair round in 95-100% of jobs for every model, whereas Qwen3-14B produced valid specifications in only 33% of jobs and passed all semantic tests in 17% (HTML/JavaScript: 62%). For reasoning models, a shorter format alone therefore does not make generation cheaper, faster or more reliable, and a format learned in context can cost reliability.

---


### 85. [Beyond Data Schedule: Fast LLM Pretraining on Data Mixtures by Loss-Reweighting](https://arxiv.org/abs/2610.32141)

**<font color=#1a73e8>作者：</font>** Jiazheng Li, Huaqing Zhang, Jing Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models often acquire specialized capabilities through successive pretraining stages, but these gains can come at the cost of forgetting earlier knowledge. In this work, we investigate whether such trade-offs can be improved by changing how strongly each domain contributes to learning while keeping its data exposure fixed. We find that, in controlled knowledge--mathematics experiments, loss reweighting produces a single checkpoint that surpasses the best knowledge and reasoning scores attained along either stage trajectory. This reveals an independent control that data-mixture ratios alone do not capture. Building on this finding, we propose LARE (Loss-Adaptive Reweighting under fixed Exposure), which automatically adjusts domain weights from running loss statistics. Motivated by a theoretical analysis of gradient noise, its normalized inverse-square-root rule balances relative loss scales without changing the sampled mixture or requiring additional runs to search for weights. Across knowledge, mathematics, and code, \Method{} improves all five evaluated benchmarks for a 1.5B model trained on 240B tokens, averaging +7.84 pp over a matched direct mixture, including gains of +17.06 pp on GSM8K and +9.00 pp on MATH. These findings demonstrate that adjusting domain loss scales can improve joint capabilities without additional domain exposure.

---


### 86. [Rethinking LoRA Initialization for Robust Asymmetric Learning Rates](https://arxiv.org/abs/2610.32142)

**<font color=#1a73e8>作者：</font>** Disen Liao, Yaoliang Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-Rank Adaptation (LoRA) is often highly sensitive to learning-rate (LR) choices. Recent empirical studies suggest that, once LRs are carefully tuned, vanilla LoRA can remain competitive with many proposed LoRA variants. This shifts the central practical question from designing ever more variants to reducing the cost and brittleness of LR selection. LoRA+ addresses this issue with asymmetric LRs, using a larger LR for the up-projection matrix $B$ than for the down-projection matrix $A$. However, the ratio $\eta_B / \eta_A$ itself becomes an additional hyperparameter: large ratios can improve adaptation, but under the standard LoRA initialization they can also cause unstable training and ratio-dependent performance collapse. We identify the source of this brittleness through a signal--noise decomposition of LoRA dynamics. Under standard \initA, the update contains an initialization-induced noise term whose magnitude can be affected by the LR for $B$, $\eta_B$, the initialization scale $\beta$, and the adapter rank $r$. In practical LLM fine-tuning, this non-vanishing noise can limit the performance gains expected from LoRA+ style asymmetric LRs. To suppress this effect, we propose \initAA, a simple initialization that scales the variance of $A$ as $\sigma_A^2 \propto n^{-2}$ while keeping $B_0=0$. Under matched rank and training time for both initializations, this reduces the initialization-noise energy by an additional factor of $1/n$, stabilizing asymmetric LoRA training while preserving zero initial adapter output. Empirically, \initAA substantially widens the stable LR region across initialization scales, adapter ranks, and LoRA update multipliers. Across tasks and models, \initAA reduces best-ratio drift, prevents the high-ratio collapse observed with standard \initA, and makes the width-based guideline $\eta_B \approx n \eta_A$ a useful starting point for finite pretrained models.

---


### 87. [Disentangling Question, Response, and Verifier Languages in Multilingual P(True) Self-Evaluation](https://arxiv.org/abs/2610.32144)

**<font color=#1a73e8>作者：</font>** Jewon Yeom, Jaewon Sok, Seonghyeon Park 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When a language model is asked whether its own answer is correct, three languages are involved: that of the question, that requested for the answer, and that of the verifier instruction asking for the judgment. Multilingual confidence evaluations seldom separate the three. We vary them independently in a six-language factorial design with ten open-weight models (3B-14B) on LSQA, MMMLU and TriviaQA, holding each answer fixed across verifier languages and measuring confidence with a first-token P(True) probe. The three languages move different parts of the evaluation: which of them governs accuracy depends on the benchmark, matching the response language to the question or verifier language sharpens discrimination but not calibration, and the verifier language alone shifts calibration error by up to 0.04 without changing accuracy. The scorer matters as well: an unvalidated judge would have shrunk the MMMLU English-Hindi accuracy gap from 0.198 to 0.038. Multilingual confidence results, model rankings included, are therefore comparable only when all three languages are reported and the scorer is validated.

---


### 88. [Separating Angular Alignment from Radial Ordering in Hyperbolic Vision-Language Models](https://arxiv.org/abs/2610.32146)

**<font color=#1a73e8>作者：</font>** Mingyang Gao, Yuwei Wu, Shiyu Luo 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperbolic vision-language models are well suited to modeling the hierarchical structure of multimodal data, because hyperbolic volume grows exponentially with radius, enabling low-distortion representations of tree-like taxonomies from general to specific concepts. However, existing pretraining objectives for hyperbolic vision-language models entangle semantic alignment with entailment modeling, forcing radial coordinates to simultaneously encode semantic matching and hierarchical structure, leading to conflicting geometric constraints. In this paper, we introduce AURORA, a hyperbolic vision-language framework that decouples the objectives through angular alignment and a novel Radial-Angular Order Cone (RAOC) for entailment modeling. Angular alignment captures semantic similarity while preserving the radial structure for representing hierarchies. Unlike conventional entailment cones, RAOC determines angular allowance from relative parent-child radial gaps. It is incorporated into hierarchical entailment contrastive training to capture partial-order relations. We further introduce a norm regularization term that prevents undesirable radial degeneration for stable training. We train models on millions of image-text pairs and evaluate them across zero-shot classification, image-text retrieval, hierarchical reasoning, and compositional understanding. Our model consistently outperforms strong Euclidean and hyperbolic vision-language baselines, demonstrating the effectiveness of decoupling semantic alignment from hierarchical entailment modeling.

---


### 89. [From Promises to Accountability: Comparative AI Modeling and Visualization of Electoral Commitments in Nepali Political Texts](https://arxiv.org/abs/2610.32150)

**<font color=#1a73e8>作者：</font>** Prakash Poudyal, Nischal Karki, Amrit Dahal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Election Commitment Mining refers to the analysis of election commitments made by electoral candidates or political parties during election campaigns. However, many elected candidates and political parties, especially in developing South Asian countries, do not fully deliver on the promises they make before elections. Even after the elections, commitments presented through election manifestos, posters, pamphlets, videos, and other campaign materials are often not systematically or transparently archived. As a result, these promises tend to fade away over time, making it difficult to hold the elected candidates accountable for their commitments. To address this persistent issue, this research aims to develop a system capable of structuring the commitments made by candidates during election periods. In this work, we created the first gold-standard dataset of Nepali political texts (Cohen's kappa = 0.777) and evaluated machine learning, deep learning and large language models to automatically extract and analyze election commitments. LaBSE-LR achieved the best results among machine learning models (0.897 accuracy, 0.896 macro F1-score, 0.947 AUROC), while fastText-LSTM achieved the highest performance among deep learning models (0.914 accuracy, 0.913 macro F1-score, 0.961 AUROC). Among the three evaluated large language models, Qwen3-8B performed best in the few-shot setting (0.848 macro F1-score). The outcome of this work is integrated into a mobile application, where commitments can be visualized with the support of GAI, enhancing transparency, civic engagement, and electoral accountability.

---


### 90. [The LLENS Platform for On-Premises Large Language Model Agents in a Japanese University Hospital: Development and Evaluation Study](https://arxiv.org/abs/2610.32151)

**<font color=#1a73e8>作者：</font>** Ken Enda, Jien Saito, Masami Mukai 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model agents that use tools could take on part of the electronic health record and desk work that occupies physicians' time, but in many hospitals the medical information systems run inside closed networks, so the model and the agent harness must also sit inside. We designed, implemented, and deployed LLENS, a clinical support AI agent platform that runs inside the closed network of Hokkaido University Hospital on one host with 8 NVIDIA H200 GPUs, the open-weight model Kimi K2.6 (~1 trillion parameters), and a web application rebuilt from Open WebUI. The harness has 10 components, including page image reading, full-text attachment input, a path-addressed document tree without a vector index, a network-isolated sandbox, artifact return, self-checking of generated output, subagents, and saved procedures. Kimi K2.6 was chosen from 3 open-weight candidates and scored 480/500 on the 2026 Japanese Medical Licensing Examination; it generated 119 tokens/s for one user and served 16 concurrent requests at 908 tokens/s in total. On 180 questions over hospital documents (3 seeds each), mean accuracy was 10.7% with no documents, 81.3% with fixed retrieval (top 10 chunks of one lexical search), and 97.2% with interactive access, in which the model reads with document tools and the sandbox (15.9 percentage points above fixed retrieval, 95% CI 10.9-21.3); the difference lay in filtering/counting questions (16.7% vs 87.8%). Five scenarios with synthetic data ran on combinations of the components: needlestick injury response, batch adverse event grading, scanned referral letter transcription, falls data aggregation and plotting, and investigation of 3 topics by subagents. The platform has run on the hospital network since September 14, 2026.

---


### 91. [Detecting Insecure Compositions of Clean Agent Skills via Capability-Flow Graph Analysis](https://arxiv.org/abs/2610.32155)

**<font color=#1a73e8>作者：</font>** Yihao Li, Chuanpu Fu, Yizhou Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents increasingly extend their capabilities by invoking third-party skills, where each skill encapsulates instructions, scripts, and resources for agents to execute on demand. This paper reveals that deploying many benign skills together introduces compositional security risks: multiple individually clean skills can compose into safety-violation chains, because the agent passes an upstream skill's output to a downstream skill's input across invocations. The risk arises not from any single skill, but from the agent's runtime orchestration, and thus cannot be captured by existing malicious skill detection methods. To this end, we develop KnotScryer to detect insecure skill compositions by treating skills as typed capability flows. In particular, we abstract each skill into a capability summary, and construct the Skill Capability-Flow Graph (SCFG), where edges denote cross-skill information flow. Moreover, we design a search policy that tracks protected or untrusted data along handoff edges to locate paths reaching insecure operations. Finally, a two-layer verification method replays the insecure information flow for reachability analysis and applies a task-anchored LLM chain audit to confirm the semantic plausibility of the identified violation chains. We deploy KnotScryer to analyze 13,598 clean skills from ClawHub, and validate the detected chains across three agent frameworks and three LLMs. KnotScryer identifies 612 insecure compositions, which are consistently exploited across agent frameworks. Meanwhile, under GLM-5.1, it outperforms tag-match and graph-only baselines by improving the exploitation rate from 16.5%-18.2% to 85.6%, while reducing the search space by 85.3%. Furthermore, 13.7% of the detected chains consist entirely of skills labeled safe by a single-skill scanner, showing that KnotScryer effectively identifies insecure compositions that per-skill auditing cannot.

---


### 92. [Not All Information Is Worth Asking For: Decision-Informed Information Seeking with LLMs](https://arxiv.org/abs/2610.32181)

**<font color=#1a73e8>作者：</font>** Seunghan Lee, Jun Seo, Junhyeok Kang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to support decisions under incomplete information, where deciding what to look up and when to stop matters as much as the final answer. However, LLMs fall into an information trap: They pay for checks, i.e., costly pieces of evidence, that cannot change their decision or are not worth their cost, and they keep asking when the evidence is already sufficient. To this end, we propose Decision-Informed Value-of-information Acquisition (DIVA), a simple yet effective procedure for LLM information seeking based on the decision value of evidence. DIVA 1) lets the LLM specify a small decision model, i.e., how likely a bad outcome is and how each check would shift this probability, through short numeric questions and 2) values each candidate check by how much its imagined outcomes improve the decision net of its cost, stopping when no check is worth its cost. Its variant, DIVA-U, further accounts for the LLM's uncertain estimates of how strongly each check shifts this probability. DIVA is training-free and applies to any LLM. Across four domains and 20 LLMs, DIVA-U has lower regret, i.e., value lost relative to the best possible decision, than every LLM baseline on real-world data, mainly by stopping once evidence suffices, and DIVA cuts the regret of the best LLM baseline by 75% in synthetic scenarios where every check's reliability is given. Code: this http URL.

---


### 93. [Depth-Dependent Safety Geometry in Vision-Language Models: Layer-Wise Localization and Bidirectional Refusal Control](https://arxiv.org/abs/2610.32182)

**<font color=#1a73e8>作者：</font>** Muhammad Zeeshan Karamat, Syed Talal Hassan, Christiana Chamon Garcia  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) are widely deployed, yet the internal mechanisms behind their safety behavior remain poorly understood. We present a lightweight inference-time framework for localizing and manipulating safety-sensitive representations in frozen VLMs, without retraining or modifying parameters. On Qwen3-VL-4B, layer-wise activation divergence analysis reveals non-uniform safety geometry across depth. Causal interventions show that early vision layers support strong bidirectional refusal control through activation steering along a learned safety direction, with unsafe rejection spanning 6%-96%, whereas later layers respond more to activation magnitude scaling and exhibit a substantial safety-selectivity trade-off. Deeper layers remain well separated along the safety direction yet are largely insensitive to steering, distinguishing representational separability from causal controllability. InternVL2.5-4B shows qualitatively similar depth-dependent activation geometry despite differences in layer location and magnitude. Our results expose a white-box, representation-level refusal-bypass attack surface in VLM vision encoders and motivate inference-time stabilization of safety-sensitive representations.

---


### 94. [Collection-Date Assignment Redirects Answers in Temporal QA](https://arxiv.org/abs/2610.32191)

**<font color=#1a73e8>作者：</font>** Minsu Oh, Seunghui Jwa, Soo Kyun Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A collection date records when a source revision was acquired, not when its contents changed. Can assigning this metadata redirect temporal question answering despite unchanged evidence? Swapping the question day and following day between two revisions lowers later-reference exact match (EM) by 37.6-51.4 percentage points across five open-weight LLMs on 595 Wikipedia pages, replicated on 128 disjoint pages. Previous-day swaps retain 29.0-39.6-point losses on 497 pages. Seven prompt variants, including explicit ignore-collection instructions and archived-revision provenance, retain the effect. Fictional answers and English month-name question dates show that remembered answers and identical date strings are unnecessary. Matched thinking reduces Qwen3.5's penalty from 30.1 to 11.1 points, while native reasoners vary. Two API LLMs show small Wikipedia swap effects and rarely shift to earlier answers on fictional records. Large swap-induced losses concentrate around the question date; swaps between distant dates have much smaller effects. Adding fields containing one observed acquisition date lowers EM relative to omission in three of five LLMs after correction. The diagnostic isolates metadata effects from changing evidence or missing the relevant revision, and provides a practical audit for temporal QA inputs.

---


### 95. [Evidence-Grounded SLM Behavioral Prediction Architecture for Future Assistance Use](https://arxiv.org/abs/2610.32193)

**<font color=#1a73e8>作者：</font>** Adeyemi Adeseye, Aisvarya Adeseye, Hannu Tenhunen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Users often exhibit changes in interaction behavior before explicitly seeking assistance, enabling systems to anticipate future assistance use. This is especially important in high-stakes environments, where delayed assistance can have operational, financial, or safety consequences. However, conventional Large Language Models (LLMs) are often unsuitable for continuous on-device behavioral prediction because of their computational and memory demands. Behavioral patterns are also highly individual and device-specific, motivating local processing that preserves privacy and data sovereignty. Small Language Models (SLMs) offer a promising alternative, but their ability to reason reliably over low-level sequential interaction events remains underexplored. This study introduces Evidence-Grounded Local Behavioral Prediction (ELBP), a four-layer architecture combining deterministic interaction processing, dual-view behavioral representation, SLM-based prediction, and evidence verification with abstention. Three instruction-tuned models of 3B parameters or fewer were evaluated using raw, structured, dual-view, and complete ELBP configurations. The best-performing model, Qwen2.5-3B with ELBP, achieved a full-set F1-score of 0.80 and PR-AUC of 0.84, representing a 15.9\% relative improvement over raw-event prompting and 17.6\% over XGBoost, while full-set ECE decreased by 43.2\% relative to raw-event prompting. With evidence verification and abstention, selective F1 increased to 0.84 at 91\% coverage and evidence support reached 96\%. These results show that structured behavioral representation and evidence-verified selective prediction can improve the reliability of behavioral forecasting in SLMs.

---


### 96. [Principia: Test-Time Hypotheses to Principle Construction for Scientific Discovery](https://arxiv.org/abs/2610.32195)

**<font color=#1a73e8>作者：</font>** Dongki Kim, Sangwoo Park, Jinheon Baek 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific discovery requires identifying the scientific principles underlying observed phenomena to guide further investigation. As these empirical principles are often unknown in complex discovery processes, they are constructed via a hypotheses-to-principle pipeline to obtain recurring causalities from progressively accumulated observations during test-time discovery. However, constructing this knowledge requires substantial domain expertise, time, and effort, making this translation stage a bottleneck for scientific discovery. To address this limitation, we propose Principia, an LLM-based framework that constructs and continually refines scientific principles at test time. Drawing on how human researchers develop principles, Principia forms comparative causal hypotheses from related inputs and their observed outcomes, then synthesizes recurring relationships across these hypotheses into inductive principles. By applying the constructed hypotheses and inductive principles to the task, it obtains new observations, revises the hypotheses used based on these new observations, and reconstructs principles from the updated hypotheses, allowing scientific knowledge to continuously evolve throughout test-time discovery. Across benchmarks spanning molecular optimization, protein engineering, gene perturbation, and molecular property prediction, Principia outperforms baselines relying on internal knowledge, external sources, or experience summaries, while generating principles that are plausible and consistent with the scientific literature, demonstrating its effectiveness in constructing and refining task-specific hypotheses and principles at test time for scientific discovery. Our code is available at this https URL.

---


### 97. [SWE-Shift: Evaluating Coding Agents in Evolving Workspaces](https://arxiv.org/abs/2610.32196)

**<font color=#1a73e8>作者：</font>** Victor Shea-Jay Huang, Rongqing Li, Zhangyue Yin 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Repository-level coding benchmarks largely assume that tasks and environments remain unchanged throughout execution. In software development, code, dependencies, runtime state, and requirements can change while an agent is still working. We introduce SWE-Shift, a benchmark for evaluating coding agents under such mid-execution changes. From the same saved history and workspace, a Clean continuation proceeds without intervention, while a matched Shifted continuation receives a task-relevant update. Success requires completing the current task, preserving still-valid work, and satisfying the applicable state and evidence checks. The benchmark contains 120 scenarios across 12 change families, each evaluated at nine scheduled intervention positions. We evaluate 17 coding-agent systems, all of which have lower Shifted than Clean success. GPT-6 Astra drops from 67.35% to 24.79%, with 20.34% paired success. Tool/session changes and stale evidence yield zero paired success across all systems. Late-position paired success is lower for some systems and higher for others. These results show that success on the unchanged task can coexist with failures to preserve work, recover state, or refresh evidence after an update.

---


### 98. [SOPO: Socratic Guided Policy Optimization for Span-Level Hallucination Detection](https://arxiv.org/abs/2610.32212)

**<font color=#1a73e8>作者：</font>** Jiawei Dong, Zilong Bai, Pengtian zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have gained widespread adoption in various natural language processing tasks, but suffer from hallucination issues where they generate unfaithful or inconsistent content. While Reinforcement Learning with Verifiable Rewards (RLVR) has shown promising applications in reasoning tasks, its application to span-level hallucination detection is challenged by localization ambiguity, reward sparsity on hard examples, and uncontrolled length inflation. To address these issues, we introduce Socratic Guided Policy Optimization (SOPO), a multi-turn RL framework for robust hallucination detection. The key innovation of SOPO is a Socratic feedback mechanism, where a teacher model guides the reasoning trajectories during rollout by providing indirect hints inferred from the ground truth. This teacher-guided approach enables the model to generate more effective reasoning trajectories for hard examples, thus alleviating reward sparsity. Furthermore, we incorporate Turn-based Advantage Scaling to penalize verbosity bias, encouraging the model to develop efficient and autonomous reasoning capabilities. Empirical results on RAGTruth demonstrate that SOPO (4B) achieves state-of-the-art performance, surpassing leading proprietary models (e.g., GPT-5) and standard RL baselines, while obtaining higher reported mean scores than GRPO on four out-of-domain benchmarks, with mixed evidence against CAPO. We release our training and evaluation code alongside the 1.7B and 4B SOPO models at this https URL.

---


### 99. [Head Dimension Matters in Language Models for Long-Context Retrieval](https://arxiv.org/abs/2610.32213)

**<font color=#1a73e8>作者：</font>** Seiya Tokui, Shoichiro Yamaguchi, Sosuke Kobayashi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-head attention retrieves and combines context representations through query--key interactions and value aggregation, with head dimension constraining the per-head representation space. In long-context processing, it remains unclear whether allocating a fixed parameter budget to fewer, wider heads improves information retrieval. In this paper, we investigate how head dimension affects the performance of long-context retrieval tasks. Our empirical studies reveal that pretraining loss and short-context non-retrieval task performance are not affected much by head dimension, while long-context retrieval performance improves with wider heads at fixed model sizes. We find that models with wider heads have a higher proportion of retrieval heads, associating more parameters with retrieval. Our ablation studies also show that the retrieval performance improves with wider heads even when the projection weights in attention modules are frozen during long-context continual pretraining, suggesting that wider heads not only benefit updates in attention modules but lead to more effective adaptation of components such as embeddings and MLPs.

---


### 100. [PEAR: Adaptive Advantage Reshaping for Perception and Exploration in Large Vision-Language Models](https://arxiv.org/abs/2610.32216)

**<font color=#1a73e8>作者：</font>** Junxin Wang, Yingfeng Luo, Xiangchen Song 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Effective multimodal reasoning requires a model to reliably utilize visual information while sufficiently exploring diverse reasoning paths. To achieve this goal, prior work combines visual dependency and token entropy to reshape sequence-level advantages, but scaling the contribution of token entropy by visual dependency can leave high-entropy tokens with low visual dependency underweighted, despite their important role in reasoning exploration. To address this limitation, we propose PEAR, an adaptive advantage reshaping method for improving perception and exploration in multimodal reasoning. PEAR retains visual dependency as the base signal and adds an entropy-based exploration gain only at high-entropy positions, with lower visual dependency leading to a larger additional gain. The fused signal is then mapped to positive token-level weights that reshape the sequence-level advantage. Experiments on Qwen2.5-VL-3B/7B show that PEAR achieves the highest average performance among evaluated baselines across multimodal reasoning benchmarks, alongside leading results on textual reasoning and general multimodal benchmarks.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-204](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
