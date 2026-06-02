# 🧠 大模型相关研究 | 2026年06月03日

> 本类共 **376** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-376](./part-08.md)

---

### 51. [Isolating LLM Lexical Bias: A Curation-Free Triangulated Metric for Preference-Stage Learning](https://arxiv.org/abs/2606.00334)

**<font color=#1a73e8>作者：</font>** Xiaoyang Ming, Jose Hernandez, Thomas Stephan Juzek  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Various language domains have undergone remarkable changes in recent years; these shifts are largely attributed to the advent of Large Language Models and their misalignment with natural language usage. These misalignments are thought to partly originate in the preference-learning stage, e.g. Reinforcement Learning from Human Feedback, which generally makes models more useful but simultaneously may introduce systematic lexical bias. In terms of lexical behavior, this is visible in a model's preference for certain formats or the overuse of words (delve, furthermore), even when such patterns are not present in base model outputs. Research on lexical misalignment induced during preference training is constrained by reliance on manual curation. We address this, by introducing the Triangulated Preference Shift score, a metric that triangulates between human gold standards, base models, and instruct variants to isolate shifts induced specifically by preference learning, without manual curation. We provide data across six model families, anchor the results in the literature, and illustrate the general approach's utility by analyzing whether preference learning shifts models toward what could be interpreted as a "language of prestige". The metric provides an initial automated method to quantify behavioral shifts attributable to preference tuning, and thus, may help inform model alignment and development of trustworthy AI.

---


### 52. [Longitudinal Multimodal Sensing of Physical Activity and Well-Being in Older Adults](https://arxiv.org/abs/2606.00345)

**<font color=#1a73e8>作者：</font>** Flavio Di Martino, Mattia G. Campana, Marcello Magno 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wearable and mobile sensing technologies enable continuous monitoring of human behavior and health in real-world settings. However, predictive modeling in longitudinal multimodal data remains challenging, particularly when targeting complex or clinically derived outcomes. In this work, we present a longitudinal multimodal study of 66 older adults conducted in real-world conditions and combining wearable sensing, behavioral monitoring, and clinical assessments. This setting provides a rare opportunity to study an underrepresented population in long-term, into-the-wild conditions. Building on this dataset, we investigate how the alignment between sensed signals and target variables affects predictive performance across health-related tasks. We design a unified evaluation framework spanning tasks with increasing levels of observability, including Activity Levels prediction, Sleep Duration estimation, and Sleep Apnea Severity classification. Our results reveal a clear gradient of predictability: highly observable behavioral targets achieve robust performance (macro-F1 65%), while more abstract outcomes remain challenging despite consistent improvements over baseline models. Moreover, through explainability analysis, we show that historical features consistently emerge as the most informative predictors, highlighting the central role of longitudinal information.

---


### 53. [From "Weak" Signals to Strong Models: Preference Delta Aggregation with LoRA Merging](https://arxiv.org/abs/2606.00357)

**<font color=#1a73e8>作者：</font>** Qi Sun, Siyue Zhang, Yulin Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training strong large language models (LLMs) requires high-quality supervision, which is often scarce. Recent work shows that paired preference data from weak-weaker model pairs (e.g., Qwen3 4B over 1.7B), despite the limited quality of individual responses, can provide an effective supervision signal through relative quality deltas, which we term a "weak" signal. This motivates a key research question: can multiple "weak" signals be constructively aggregated for improving strong models (e.g., Qwen3 8B)? To this end, we propose Preference Delta Aggregation (PDA), the first framework that derives a preference delta from each weak-weaker model pair, instantiates it as a LoRA adapter learned through preference optimization, and aggregates the resulting deltas via LoRA merging. To further mitigate directional interference during LoRA merging, we introduce Geometric Alignment Merging (GAM), a geometry-aware merging method that aligns adapter subspaces before aggregation, enabling more robust composition of diverse deltas. Evaluations on knowledge reasoning and agentic search benchmarks show that aggregating multiple "weak" signals pushes performance beyond any single signal, with further gains as additional signals are incorporated. Correspondingly, PDA with GAM improves the strong model by 6.8 and 7.3 points on average for knowledge reasoning and agentic search, respectively. It outperforms all single-delta and multi-delta baselines, exceeding the best single-delta baseline by 2.1 and 4.3 points. Further analysis attributes these gains to the effective composition of complementary capabilities encoded across distinct preference deltas.

---


### 54. [Agentic Authoring of Interactive Multiview Visualizations in Genomics](https://arxiv.org/abs/2606.00370)

**<font color=#1a73e8>作者：</font>** Astrid van den Brandt, Kiroong Choe, Sehi L'Yi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Diverse genomics data, scientific questions, and analysis tasks typically demand highly specialized visualizations. Therefore, users often must customize or author new ones tailored to their data. Existing tools are usually either limited in customization or require substantial learning or programming, and even expressive tools assume visualization expertise many users lack. Agentic and large language model (LLM) approaches are increasingly applied to complex scientific tasks, including visualization. Natural-language conversational interfaces offer a promising path to democratizing the authoring of complex visualizations. In the context of genomics, these approaches face additional challenges: genomics visualizations typically integrate heterogeneous data types and are composed of multiple linked interactive views. These challenges motivate more structured LLM-based schemes. We first characterize where vanilla LLM generation succeeds and fails for genomics visualization, identifying eight quality dimensions. We then compare six schemes--direct generation, a fixed pipeline, and four agentic configurations varying in the number of specialist agents and the presence of a reviewer--across 159 cases spanning three levels of query ambiguity and specification complexity. All schemes use the Gosling visualization grammar as structured output. Agentic iteration substantially improves perceived quality over both baselines, while more complex agent architectures yield no additional benefit. We discuss implications for designing agentic systems for domain-specific visualization authoring. All supplemental materials are available at this https URL.

---


### 55. [CRMA: A Spectrally-Bounded Backbone for Modular Continual Fine-Tuning of LLMs](https://arxiv.org/abs/2606.00382)

**<font color=#1a73e8>作者：</font>** Kiran Nayudu, Aswini Nutakki, Sai Vinay Naidu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sequential fine-tuning of large language models forces a choice: let the shared substrate keep learning and accept catastrophic forgetting, or freeze it after task one and foreclose cross-task refinement. Per-task adapter methods (LoRAHub, AdapterFusion, PackNet, Progressive Networks) take the second path. We introduce CRMA (Constrained Residual Mixing Adapter), a residual adapter whose internal mixing matrix M is doubly-stochastic at every forward pass via Sinkhorn normalization, so by Birkhoff's theorem ||M||_2 <= 1 holds by construction -- a structural bound, not a penalty. CRMA's spectrally bounded backbone provides a continuously trained shared substrate that earlier modular methods could not, while preserving their forgetting guarantees. On Mistral-7B across 5 sequential domains and 3 seeds, modular per-task LoRA on a CRMA backbone reduces loss-relative drift from +42.96% +/- 5.5 (naive sequential fine-tuning) to -0.17% +/- 0.17, with disjoint per-seed ranges, and improves prior-task holdout loss by 1.99% +/- 0.54 over a matched frozen-substrate baseline. Three independent experimental setups (Mistral-7B 4-domain controlled ablation, TinyLlama 3-domain contamination-controlled replication, Mistral-7B cross-domain probes at 7B) all show positive backward transfer -- without replay buffers, without growing per-task memory, and without distillation. An inference-time ablation on Gemma-2-9B confirms CRMA mediates access to sequentially trained knowledge: 98/100 vs. 38/100 on the same weights and same questions with only CRMA injection toggled. 867 logged training steps verify ||M||_2 = 1.0 within float32 precision (max deviation 1.2 x 10^-7). The forgetting-prevention effect holds across 1.1B-9.2B parameters and four architecture families.

---


### 56. [VESTA: Visual Exploration with Statistical Tool Agents](https://arxiv.org/abs/2606.00384)

**<font color=#1a73e8>作者：</font>** William Rudman, Abhishek Divekar, Kanishk Jain 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fitting quantitative models to data is a central step in scientific workflows, yet it remains one of the least automated. Recent agent-based systems leverage language and vision-language models (VLMs) to iteratively propose and refine statistical models, but these systems struggle on more challenging modeling tasks. To address these limitations, we introduce VESTA: Visual Exploration with Statistical Tool Agents, a framework that equips VLMs with a dynamically growing exploration toolkit to guide model refinement through data transformations, hypothesis-driven visualizations, and robust statistical tests. Unlike prior systems that rely on iterative critique alone, VESTA actively explores data before and during refinement by selecting or creating diagnostic tools, which accumulate in the model's context and can be reused later. We evaluate VESTA against established baselines in three toolkit configurations: no tools, static expert-written tools, and dynamic model-written tools. To support this evaluation, we introduce DAWN (Dataset for Automated Workflows and Numerical Modeling), a benchmark targeting distribution fitting and time series modeling with varying difficulty tiers, and culminating in real-world astronomy tasks including modeling initial mass functions and gravitational-wave chirp signals. We find that VESTA's dynamic tool creation outperforms prior agentic pipelines, with the largest gains on complex and domain-specific tasks. We further show that dynamically generated tools are substantially more sophisticated than those produced by existing visual tool-creation systems, covering more diagnostic categories per function and strongly preferring visual outputs that the VLM critic can reason over directly.

---


### 57. [Detector-Evasive LLM Paraphrasing via Constrained Policy Optimization](https://arxiv.org/abs/2606.00392)

**<font color=#1a73e8>作者：</font>** Mingyi Wang, Zhuoer Shen, Yuheng Bu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI-text detectors are vulnerable to paraphrasing and detector-guided paraphrasing attacks, but existing detector-evasion methods often lack precise control over semantic preservation. In particular, optimizing directly for detector evasion can degrade fine-grained semantics, whereas scalarized reward designs provide only indirect, weight-sensitive control over the evasion-semantics trade-off. We address this limitation by formulating detector-evasive LLM paraphrasing as a Constrained Markov Decision Process, where detector evasion is the primary objective and semantic preservation is enforced as an explicit constraint. We propose Detector Evasion Policy Optimization (DEPO), a Lagrangian primal-dual reinforcement learning algorithm with a novel GRPO-style group-based policy update. DEPO adaptively balances semantic preservation and detector evasion during training, enabling the policy to improve attack success within a prescribed semantic-preservation region. Experiments on MAGE, M4, RAID, and peer-review datasets, evaluated against MAGE, RoBERTa, RADAR, Binoculars, and Fast-DetectGPT detectors, show that DEPO achieves strong detector evasion while precisely satisfying the semantic preservation constraint. DEPO also exhibits cross-domain, cross-detector, and prompt-level robustness.

---


### 58. [PR2: Predictive Routing Replay for MoE-Based LLM Reinforcement Learning](https://arxiv.org/abs/2606.00395)

**<font color=#1a73e8>作者：</font>** Daize Dong, Junlin Chen, Haolong Jia 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture of Experts (MoE) Large Language Models (LLMs) achieve strong performance at scale. However, reinforcement learning (RL) on MoE-based LLMs often suffers from training instability. A root cause is router drift, i.e., expert activations can change drastically across model updates and differ between disaggregated rollout and training phases, causing large rollout--training mismatch and unstable importance sampling weights in PPO-style RL algorithms. Routing replay mitigates this issue by freezing the replay route within each reasoning trajectory, but it ignores how the router evolves under off-policy updates and thus causes router staleness. To address this limitation, we propose Predictive Routing Replay (PR2), which augments each router with a lightweight evolution predictor that learns to anticipate short-horizon router evolution. During the rollout phase, we use the predictive routing distribution to apply top-$k$ routing, enabling gradients to reach experts that are likely to become active after updates. During the training phase, we replay the resulting predicted route to retain consistency for stable importance estimation. Theoretical analysis and experiments support that PR2 reduces routing-induced mismatch, improves RL stability, and yields stronger performance across various reasoning benchmarks.

---


### 59. [Dynamic Proxy-Mixing: Transferring Replay Controllers from Small to Large Models for Continual Instruction Tuning](https://arxiv.org/abs/2606.00400)

**<font color=#1a73e8>作者：</font>** Ibne Farabi Shihab, Fariya Afrin, Anuj Sharma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual instruction tuning updates a language model through a sequence of new domains, yet each update can progressively erode previously learned capabilities and alignment behavior. Replay is the standard mitigation, but fixed replay ratios are inherently limited because the optimal mixture varies with the current domain, the training stage, and the evolving vulnerability of prior behaviors. We propose PROX-YMIX, a framework that learns a dynamic replay controller on a small proxy model and transfers the frozen controller to a larger target. The controller never observes future tasks and constructs its state from normalized validation losses and their temporal dynamics, producing a masked mixture over the current task and accessible replay buffers. Our core empirical hypothesis is forgetting mirroring: task vulnerability rankings remain largely consistent across model scales even when absolute loss magnitudes differ. We validate this assumption empirically before transferring controllers across scales. On LLaMA-3-8B across five continual instruction tuning sequences, PROXYMIX improves average accuracy by 3.4 points, reduces final forgetting by 3.5 points, and raises safety score by 5.8 points over the strongest non-oracle baseline, at roughly 50x lower policy learning cost than Oracle Target RL. The framework is leakage free and architecture independent at the interface level, and we also identify settings where the proxy assumption breaks down, highlighting limitations for robust deployment.

---


### 60. [Grounded Decoding: Retrieval-Anchored Probability Fusion for Faithful RAG](https://arxiv.org/abs/2606.00432)

**<font color=#1a73e8>作者：</font>** Ibne Farabi Shihab, Fariya Afrin, Sanjeda Akter 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As retrieval-augmented generation (RAG) systems scale, it becomes increasingly challenging to ensure faithful grounding in external evidence. Large language models may still prioritize parametric knowledge over retrieved information when conflicts arise. We propose a novel training-free decoding framework, \emph{Grounded Decoding}, designed to improve factual consistency in RAG without modifying model parameters. Unlike standard approaches that rely on a single conditional distribution, our method constructs two matched-prompt distributions at every generation step: (1) a full RAG distribution conditioned on the query, retrieved documents, and generated prefix, and (2) a retrieval-only distribution conditioned solely on retrieved evidence and the same prefix. The final next-token distribution is derived as the unique solution to a KL-barycenter objective over the probability simplex, yielding a normalized geometric fusion of the two this http URL formulation naturally recovers standard RAG when the grounding weight is zero and smoothly shifts probability mass toward retrieved evidence as grounding strength increases. We further introduce a conflict-aware adaptive weighting scheme that dynamically adjusts grounding based on distributional disagreement and retriever confidence. Experiments on ALCE, Natural Questions, and FActScore demonstrate consistent improvements in factual accuracy and citation quality over standard RAG and competitive decoding-time baselines, while maintaining fluency. Our results indicate that probability-level fusion provides a strong and efficient alternative to logit-level intervention methods for faithful RAG decoding.

---


### 61. [Detect Before You Leap: Mirage Detection in Vision-Language Models](https://arxiv.org/abs/2606.00435)

**<font color=#1a73e8>作者：</font>** Sayeed Shafayet Chowdhury, Md. Shaown Miah  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) can produce confident visual answers even when the required visual evidence is missing, blank, or unrelated to the question. This failure mode, known as mirage (Asadi et al. 2026), is especially concerning in medical and document visual question answering, where plausible but visually ungrounded responses may be mistaken for image-based evidence. We study pre-release mirage detection: given an image-question pair, the goal is to determine whether a VLM should answer or abstain before producing a response. We propose Text-Conditioned Layer-wise Internal Alignment (TC-LIA), a model-agnostic method that probes patch-token representations across the layers of a CLIP ViT-H/14 vision encoder. TC-LIA projects layer-wise image patch tokens into the final CLIP embedding space and measures their similarity to the question embedding, allowing the method to track whether question-relevant visual evidence emerges across vision layers. The resulting alignment trajectory is summarized using final image-text cosine similarity, late-layer top-k patch-text alignment, early-to-late gain, and layer-wise slope. These features are combined with pixel-statistic blank/noise detection, zero-shot domain routing, and structured VLM self-assessment in an ensemble. Across five VQA domains, three input conditions, and twelve VLM backbones, the best systems achieve approximately 94.6-94.7% three-class detection accuracy with mirage rates below 3%, while baseline mirage rates range from 21.7% to 66.6%.

---


### 62. [Physical Object Understanding with a Physically Controllable World Model](https://arxiv.org/abs/2606.00439)

**<font color=#1a73e8>作者：</font>** Rahul Venkatesh, Klemen Kotar, Lilian Naing Chen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A central challenge in visual intelligence is learning the physical structure of scenes from raw videos: how regions form objects and the laws that govern their interactions. Solving these tasks requires world models capable of inferring distributional states of the world from partial observations - capabilities that current architectures do not provide. We introduce a new class of probabilistic world models that support estimation of the probability of any visual variable, such as appearance and dynamics, conditioned on any other variables. Here, we identify that these models can be trained efficiently with autoregressive sequence modeling, yielding world models from which rich object understanding emerges. First, we demonstrate that our model captures the physical laws governing how objects move by generating multiple plausible future states of the world through sequential inference. Then, by analyzing motion correlations across these futures, we extract objects and articulated object subparts. Having discovered these objects, we show that our world model can manipulate them in 3D. Finally, we demonstrate how physical relationships between objects can be computed from the world model, enabling applications such as Visual Jenga.

---


### 63. [SDR: Set-Distance Rewards for Radiology Report Generation](https://arxiv.org/abs/2606.00440)

**<font color=#1a73e8>作者：</font>** Halil Ibrahim Gulluk, Max Van Puyvelde, Wim Van Criekinge 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards has rapidly advanced reasoning in vision--language models. However, for chest X-ray report generation, the standard rewards (i.e. exact-match accuracy and step-level processes) are incompatible because the reports consist of unordered and orthogonal findings, rather than a causal reasoning chain. We address this gap with a set-based view: each report is split into sentences and embedded by a frozen sentence transformer, yielding unordered embedding sets. We propose the use of set-to-set distances between generated and reference embeddings as continuous, permutation-invariant rewards. Across two datasets and three vision--language models (Qwen3-VL-2B/4B, Gemma3-4B), post-training with set-to-set distance based rewards via GRPO consistently outperforms supervised fine-tuning and exact-match GRPO on all headline metrics (BERTScore, RadGraph F1 and CheXbert F1 by average \%6.80, \%7.82 and \%4.45 relative improvements respectively). The same set distances also enable test-time best-of-$N$ selection: scoring candidates by their distance to training-report embeddings outperforms random selection on our trained models as well as three closed-source LLMs (Mistral-Small, Gemini-2.5 Flash-Lite, GPT-4o-mini) with on average \%16.4 relative improvement on BERTScore. Used as a streaming signal, they support a more efficient form of test-time scaling: pruning low-scoring candidates mid-generation reduces generated tokens by over 50\% while preserving the Findings quality of full best-of-$N$ selection. Together these results establish set-distance rewards as a unified signal for both post-training and test-time scaling in chest X-ray report generation. Our code is publicly \href{this https URL}{available}.

---


### 64. [ProtStructQA: A Denotation Threshold in Protein Structural Reasoning](https://arxiv.org/abs/2606.00451)

**<font color=#1a73e8>作者：</font>** Aravind Mandiga, Guoming Li, Jin Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Protein-language systems are often evaluated by whether they generate plausible biological text, but a structural question has a sharper semantics: it denotes a measurement in a 3D coordinate system. We introduce ProtStructQA, an executable benchmark for protein structural question answering in which each natural-language question is generated from a hidden typed domain-specific language (DSL) program and the answer is obtained by executing that program on an AlphaFold-predicted structure. ProtStructQA releases 382.2K questions covering confidence, distances, predicted aligned error (PAE), solvent exposure, secondary structure, topology and contacts, and held-out compositions: a 330K active benchmark over 10K proteins from four species, plus a 52.2K hard-negative robustness pool. Without fine-tuning, we evaluate Qwen3 models from 0.6B to 8B under direct prompting, chain-of-thought, grammar-constrained executable voting, executable voting with chain-of-thought, and multi-turn ReAct-style tool use, and replicate the headline finding on Gemma-3-1B and Gemma-3-12B. We find a capability-dependent denotation threshold between Qwen3-1.7B and Qwen3-4B: below it, tool-mediated ReAct dominates because models often fail to produce executable denotations; above it, chain-of-thought flips from mostly harmful to strongly beneficial and becomes the strongest strategy on most splits. Parse-failure and family-level analyses show that the threshold is a transition from unparseable language to executable structural denotation, while grammar and execution remain selectively valuable for PAE and secondary-structure queries. ProtStructQA reframes scientific QA as compilation from language to measurement and provides a diagnostic testbed for when language models can map words to executable 3D structural measurements.

---


### 65. [SALSA: Speech Aware LLM Adaptation via Learned Steering Activation Vectors](https://arxiv.org/abs/2606.00460)

**<font color=#1a73e8>作者：</font>** Yekaterina Yegorova, Argyrios Gerogiannis, Haolong Zheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech-aware large language models often generalize poorly to out-of-domain settings. We propose SALSA (Speech-Aware LLM Adaptation via Learned Steering Activations), a lightweight adaptation method that learns layer-wise steering vectors. Unlike commonly used steering approaches that rely on contrastive activation differences, SALSA directly optimizes steering vectors using a supervised objective. Across children's speech, multilingual speech, and Mandarin-English code-switching benchmarks, SALSA substantially improves performance over zero-shot inference and speech in-context learning baselines, achieving up to 46.8% relative improvements over zero-shot. Analysis further demonstrates that steering the encoder, particularly the later layers, is more effective than steering the LLM backbone. These findings suggest that steering improves downstream ASR performance by adapting higher-level acoustic and phonetic representations to better align with the pretrained language model representation space, rather than by modifying the decoder itself.

---


### 66. [Short-form Text Rewriting with Phi Silica](https://arxiv.org/abs/2606.00462)

**<font color=#1a73e8>作者：</font>** Divya Tadimeti, Shawn Pan, Sameera Lanka 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Short-form text rewriting is a constrained variant of paraphrasing in which limited context and high semantic density leave little room for variation. While large language models perform well on general paraphrasing, small language models (SLMs) often struggle with semantic fidelity and hallucination robustness in short-form settings. In this work, we present an empirical study of adapting an SLM, Phi Silica, for short-form rewrite through dataset curation, prompt distillation, parameter-efficient fine-tuning, and evaluation. We curate a dataset of short presentation-style text from public slide decks and use GPT-5-chat both to generate rewrite supervision and to conduct LLM-as-a-judge evaluation. Our results show that finetuning improves semantic fidelity, reduces hallucinations, and increases preference win rate against GPT-5-chat rewrites. The findings suggest that targeted adaptation for SLMs can substantially narrow the gap to cloud models and provide practical guidance for adapting SLMs to precision-critical rewrite tasks.

---


### 67. [On the Limits of LLM Adaptability: Impact of Model-Internalized Priors on Annotation Task Performance](https://arxiv.org/abs/2606.00467)

**<font color=#1a73e8>作者：</font>** Etienne Casanova, Rafal Kocielnik, R. Michael Alvarez  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly used for zero-shot annotation and LLM-as-a-judge tasks, yet their reliability hinges on how model-internalized priors interact with user-provided instructions. We investigate three dimensions of this interaction: (1) how an LLM's familiarity with data and task definitions affects performance, (2) the extent to which additional information in prompts can correct zero-shot errors ("decision stickiness"), and (3) model susceptibility to misaligned task definitions. Through experiments on toxicity detection across diverse datasets (spanning social media, gaming, news, and forums) using both dense and mixture-of-experts models, we find that nearly two-thirds of zero-shot errors are resistant to correction, with an overall rescue rate (fraction of initial errors corrected by prompting) of only 34.8%. High-confidence errors prove especially resistant to correction. When given misaligned definitions, LLMs follow them while maintaining confidence levels unchanged from the aligned condition. Crucially, we introduce Definition-Specific Familiarity (DSF), which measures alignment between a model's internal concept and the task definition. After controlling for dataset-level confounds, DSF shows a positive association with model performance (partial r = +0.41), while three distinct memorization metrics (ROUGE-L, BERTScore, and embedding cosine similarity) all fail to show a positive association. These findings show the limitations of prompt-based correction in annotation tasks, highlighting the importance of definition alignment over text-level memorization.

---


### 68. [Doing What They Say, Not What They Reason: Locating the Faithfulness Gap in LLM Agents](https://arxiv.org/abs/2606.00476)

**<font color=#1a73e8>作者：</font>** Yufeng Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Do LLM agents act on the reasoning they state? This question of process fidelity is central to using LLMs in social simulation, yet it is hard to measure where no reference for correct behavior exists. We study it in acontrolled setting, a Texas Poker simulator with a verifiable reference action for every decision by decomposing the faithfulness gap into two steps: reasoning-conclusion and conclusion-action. The two steps behave oppositely.

---


### 69. [ProjQ: Project-and-Quantize for Adapter-Aware LLM Compression](https://arxiv.org/abs/2606.00494)

**<font color=#1a73e8>作者：</font>** Wneya Yu, Chao Zhang, Li Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-Training Quantization (PTQ) and Low-Rank Adaptation (LoRA) constitute the standard pipeline for efficient Large Language Model (LLM) deployment. However, applying them sequentially poses a problem: PTQ often leaves behind random noise that is spread out (across the model's weights) in a way LoRA can't easily fix, meaning that LoRA ends up wasting its limited capacity trying to fix uncorrectable noise instead of improving task performance. In this paper, we propose \textbf{ProjQ}, a novel framework for constraining quantization noise to the low-rank manifold via orthogonal subspace projection. We derive an efficient alternating algorithm that shapes the quantization noise into a low-rank structure, effectively offloading dominant error components to the subsequent adapter while minimizing the residual error in the orthogonal "uncorrectable" subspace. Our theoretical analysis demonstrates that ProjQ preserves strictly greater model plasticity for downstream tasks compared to standard PTQ. Extensive experiments on LLaMA-2, Qwen2.5 and Qwen3 confirm that ProjQ consistently outperforms existing methods in both quantization error compensation and downstream task fine-tuning, achieving up to $2\times$ lower evaluation loss for compensation and matching the performance of standard 4-bit baselines on language modeling tasks with only 3 bits. The code is available on this https URL .

---


### 70. [LaSR: Context-Aware Speech Recognition via Latent Reasoning](https://arxiv.org/abs/2606.00507)

**<font color=#1a73e8>作者：</font>** Heyang Liu, Ziyang Cheng, Jiayi Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in Speech Large Language Models (Speech LLMs) have significantly enhanced spoken language understanding and reasoning. However, their contextual awareness is limited, struggling to perform speech recognition that effectively reflects the speaker's intent and topical context. In this paper, we propose LaSR (Latent Speech Reasoning), a novel training paradigm featuring a context-aware reasoning trajectory that leverages the latent reasoning process. Instead of generating explicit intermediate tokens, LaSR aligns chain-of-thought (CoT) supervision around the acoustic feature region of the targeted word, and introduces latent reasoning periods for context information grounding and transcriptional transition. Furthermore, to effectively benchmark contextual recognition on specialized vocabulary, we propose Spoken Darwin-Science, a large-scale corpus focusing on academic terminologies. Preliminary experiments on Fun-Audio-Chat demonstrate that LaSR significantly improves terminology recognition without introducing additional latency and consistently outperforms standard supervised fine-tuning baselines. Our findings highlight the potential of latent reasoning in building efficient, context-aware speech assistants.

---


### 71. [V-LynX: Token Interface Alignment for Video+X LLMs](https://arxiv.org/abs/2606.00508)

**<font color=#1a73e8>作者：</font>** Jungin Park, Jiyoung Lee, Kwanghoon Sohn  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This study introduces an intriguing phenomenon in Video LLMs: rather than merely translating frames into textual embeddings, Video LLMs establish a continuous manifold, token interface, allowing visual tokens to operate as standalone entities within the architecture. Exploiting this discovery, we propose V-LynX, a scalable framework that integrates novel modalities into Video LLMs by repurposing the internalized interface. Departing from conventional paradigms that necessitate heavy modality-specific encoders or paired supervision, V-LynX employs a lightweight auxiliary pathway in parallel with the frozen vision encoder. Our method integrates new sensory inputs with intrinsic video priors by aligning both attention responses and statistical distributions using unpaired unimodal data sets. This ensures manifold compatibility while preserving the integrity of the Video LLMs. Extensive benchmarks demonstrate that V-LynX achieves SOTA and efficiency across audio-visual QA, 3D reasoning, high-frame-rate, and multi-view video understanding. The code is available at this https URL.

---


### 72. [Skill or Skip? Learning Selective Skill Invocation in Agentic Tasks via Dual-Granularity Preference Learning](https://arxiv.org/abs/2606.00510)

**<font color=#1a73e8>作者：</font>** Chishui Chen, Jiaye Lin, Te Sun 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agent skills are callable procedural modules that provide reusable knowledge and execution policies for complex agentic tasks. However, existing methods mainly focus on selecting relevant skills or improving the skills themselves, while overlooking whether a relevant skill should actually be invoked at the current decision point. Unhelpful invocations may introduce irrelevant context and disrupt an otherwise correct execution process. To address this issue, we propose SelSkill, a dual-granularity preference-learning framework for selective skill invocation. SelSkill formulates skill use as a skill-or-skip decision, uses predictive uncertainty to prioritize candidate decision points, and constructs controlled invoke-skip preference pairs from shared trajectory prefixes. It further combines episode-level outcome preferences with step-level invocation preferences to capture both overall trajectory quality and the local effectiveness of skill invocation. On ALFWorld with Qwen3-8B, SelSkill improves task success by 10.9 percentage points and execution precision by 29.1 percentage points. On BFCL, it improves task success by 5.7 percentage points and execution precision by 29.5 percentage points. Zero-shot results on Tau-bench and PopQA further suggest that the learned invocation policy transfers to new domains with previously unseen skills.

---


### 73. [Threshold-Based Exclusive Batching for LLM Inference](https://arxiv.org/abs/2606.00516)

**<font color=#1a73e8>作者：</font>** Weifang Zhang, Yuzhou Nie, Bowen Pang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mixed batching (MB)--interleaving prefill and decode in a single batch--has become the standard scheduling strategy for large language model (LLM) inference due to its efficiency in maximizing compute and memory utilization. However, through controlled experiments, we find that prefill-decode interference inflates MB's per-step marginal cost above that of pure decode. On the high-bandwidth H200 (4.8 TB/s), this occurs only when decode tokens exceed 80% of the batch; however, on the bandwidth-constrained RTX PRO 6000 (1.792 TB/s), this threshold plummets to just 20%. Consequently, the optimal choice between MB and exclusive batching (EB) fundamentally depends on GPU memory bandwidth, model size, and workload composition. We derive a closed-form condition for this EB-MB performance crossover, along with asymptotically optimal phase-switching thresholds and memory-safe batch sizing for EB. Optimized EB achieves up to 41.9% higher throughput on bandwidth-constrained GPUs, while MB retains its advantage on high-bandwidth hardware with larger models. Our hybrid scheduler EB+ applies this condition online to dynamically switch between EB and MB without manual intervention. Under non-stationary traffic with distribution or concurrency shifts, EB+ attains the highest or near-highest throughput in every setting, outperforming MB by up to 36.4%.

---


### 74. [Acting with AI: An Interaction-Based Framework for Agentic Tort Liability](https://arxiv.org/abs/2606.00518)

**<font color=#1a73e8>作者：</font>** Yiheng Yao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI systems can plan over multiple steps, use tools, and execute tasks over time. When such systems cause harm, tort law struggles to allocate responsibility because the harmful path may be neither fully chosen by the user nor specifically foreseen by the developer. This paper proposes an interaction-based framework for agentic torts, drawing on Michael Bratman's planning theory and on the common law's treatment of human-human concerted action. We distinguish three interaction types: autonomous drift, pure tool use, and collaborative planning. Pure tool cases remain governed by ordinary product-defect and warning doctrines; collaborative planning cases map onto the independent contractor control test, professional malpractice, and negligent misrepresentation; autonomous drift maps onto frolic and detour under respondeat superior and strict product liability. The framework treats the stateful interaction log as the primary evidentiary trace, allowing courts to infer where the human-AI trajectory departed from the authorized undertaking and where liability should attach. We resolve four incident-anchored cases, situate the account alongside strict-liability and insurance-based proposals, note its relationship to regulatory oversight, and propose a ``Reasonable Agent'' standard built around constraint verification, epistemic transparency, runtime grounding, and forensic logging.

---


### 75. [ProactiveLLM: Learning Active Interaction for Streaming Large Language Models](https://arxiv.org/abs/2606.00523)

**<font color=#1a73e8>作者：</font>** Junlong Tong, Yao Zhang, Anhao Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Standard Large Language Models (LLMs) follow a read-then-generate paradigm, causing unnecessary latency and computation. Streaming LLMs alleviate this issue by generating while receiving inputs, but still struggle to decide when to interact with the stream. Existing methods either hard-code interaction timing or rely on costly external alignment signals, such as timing labels, reasoning trajectories, or stronger teachers. In this paper, we propose ProactiveLLM, which achieves active interaction by leveraging the model's endogenous states to guide interaction decisions. The model first learns to perceive semantic sufficiency from partial inputs through two complementary training mechanisms: mask-based streaming modeling and synchronized privileged self-distillation (SPSD). The former applies monotonic random masking to the input during training, simulating progressively revealed streaming inputs and enabling the model to learn local semantic dependencies from partial-input views. The latter aligns the partial-context student view with a full-context teacher view generated by the same evolving model, allowing privileged full-context evidence to guide the student's understanding under incomplete observations. Together, these mechanisms induce endogenous sufficiency cues without requiring external teachers or annotations, providing a versatile foundation for the plug-and-play integration of diverse decision heads. Extensive evaluation across text and speech streaming tasks confirms that ProactiveLLM significantly reduces interaction latency while maintaining quality, validating its capacity for dynamic and active interaction. Code is publicly available at this https URL.

---


### 76. [DREAM-S: Speculative Decoding with Searchable Drafting and Target-Aware Refinement for Multimodal Generation](https://arxiv.org/abs/2606.00535)

**<font color=#1a73e8>作者：</font>** Zining Liu, Yunhai Hu, Tianhua Xia 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speculative decoding (SD) has proven to be an effective technique for accelerating autoregressive generation in large language models (LLMs) however, its application to vision-language models (VLMs) remains relatively unexplored. We propose~\textit{DREAM-S}, a novel SD framework designed specifically for fast and efficient decoding in VLMs. DREAM-S leverages a neural architecture search (NAS) framework with target-aware supernet training to automatically identify both the optimal interaction strategy between the draft and target models, and the most suitable draft model architecture for the underlying hardware implementation platform. DREAM-S additionally incorporates adaptive intermediate feature distillation, guided by attention entropy, to enable efficient draft training. Experiments on a range of well-established VLMs show that DREAM-S achieves up to a $3.85\times$ speedup compared to standard decoding approaches and significantly outperforms existing SD baselines. The code is publicly available at: this https URL .

---


### 77. [GNMR: Runtime Stability Control for Low-Precision Large Language Model Training](https://arxiv.org/abs/2606.00539)

**<font color=#1a73e8>作者：</font>** Boao Kong, Weichen Jia, Engao Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training stability is a key bottleneck in low-precision language model training: efficient low-cost paths can still produce short-lived numerical risks at a small set of operators. We formulate this as runtime stability control and present Gradient Norm-to-Mean Ratio (GNMR), a lightweight controller that compares each recoverable unit's current gradient norm with its historical mean. Together with $\Delta$-GNMR for abrupt short-window increases, GNMR maps local risk signals to bounded recovery actions under a hard $\mathrm{maxO}$ budget and a short lock interval, without changing the numerical format, kernel, or backend recipe. Across activation-quantization stress, DeepSeek-style recipe-level training, and LLaMA-2 13B fine-tuning, GNMR preserves high-fidelity quality with sparse, budgeted recovery. These results support GNMR as a backend-agnostic controller to improve low-precision training stability while preserving low-cost execution.

---


### 78. [ETC: Extreme Token Compression via Task-aware Visual Information Distillation in VLMs](https://arxiv.org/abs/2606.00543)

**<font color=#1a73e8>作者：</font>** Yiling Gao, Hongchen Wei, Zhenzhong Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In Vision-Language Models (VLMs), high-resolution images produce a large number of visual tokens, resulting in high computational costs and KV-cache overhead during inference. To address this problem, we propose an Extreme Token Compression (ETC) framework that minimizes task loss when reducing the number of input tokens based on the principle of variational information distillation. Specifically, from an information-theoretic perspective, we show that minimizing task loss requires the compact representation to preserve the instruction-aware sufficient statistic of the task-relevant visual information for prediction. In practice, ETC leverages text-to-image cross-attention to weight the original visual features to approximate the latent instruction-aware predictive statistic. Moreover, ETC introduces a variational information distillation, enabling the compact representation to preserve the essential information to recover this predictive statistic. Experiments on LLaVA-1.5-7B and Qwen3-VL-2B show that ETC remains effective even under single-token compression, substantially reducing KV-cache overhead while retaining strong task performance.

---


### 79. [Escaping the Mode Lottery: Multi-Response Training Improves Language Model Generalization](https://arxiv.org/abs/2606.00544)

**<font color=#1a73e8>作者：</font>** Hasan Amin, Kian Ahrabian, Ming Yin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern language-model fine-tuning typically pairs each prompt with a single response, even though many prompts admit multiple valid completions. This effectively reduces a multi-modal conditional distribution to a one-sample view, a phenomenon we call the "mode lottery," where training emphasizes a subset of plausible modes while leaving others underrepresented. We study multi-response training (MRT), which retains multiple responses per prompt, and develop a principled account of when and why it helps. Our key insight is that prompts and responses are distinct statistical resources: additional prompts reduce uncertainty about the input distribution, while additional responses reduce uncertainty about the conditional output distribution. This yields a variance-budget tradeoff that predicts when retaining multiple responses is worthwhile, shows diminishing returns as prompt-level uncertainty dominates, and explains why large redundant corpora can exhibit an implicit multi-response effect. We further analyze response selection, and show that Random-K-of-N is the unbiased default for distributional fine-tuning, reward-based selection can induce mode collapse, and a submodular quality-diversity objective provides an efficient alternative with theoretical guarantees. Controlled simulations validate the predicted variance and selection effects, including a striking failure mode where reward-only selection produces gradients misaligned with the true objective. Across structured and real-world datasets, including a new multi-prompt, multi-response benchmark, MRT consistently improves distributional generalization, with the largest gains in high response-diversity, low prompt-redundancy regimes. MRT reframes response multiplicity as a data-allocation problem with clear guidance: when responses are cheap and diverse, keeping more than one is not a heuristic, but a statistically grounded choice.

---


### 80. [The Assistant as a Privileged Persona: A canonical reference in cross-persona self-recognition](https://arxiv.org/abs/2606.00545)

**<font color=#1a73e8>作者：</font>** Asvin G  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-trained language models can recognize their own outputs from a sentence or two out of context. In a companion paper \citep{jack2026twomodes} we showed they can also recognize when they are currently acting on-policy, through the sharp entropy drop of assistant-mode generation. Both signals are tied to the Assistant persona that post-training mainly shapes.
This paper widens the frame to cross-persona authorship judgement on Llama-3.1-70B-Instruct. We measure a matrix of authorship claim rates over a panel of evaluator and generator personas spanning librarian to dragon to Shakespeare, and make two claims. \emph{First}, on the Assistant's own row of the matrix, the Assistant's claim rate, the persona-vector distance from the Assistant in activation space, and the entropy gap between the Assistant's surprise on a persona's text and the persona's surprise on its own text are all tightly coupled. This extends the entropy signature of \emph{acting} from the companion paper to a retrospective signature of \emph{having acted}. \emph{Second}, this coupling fails off the Assistant's row: the natural symmetric extension of the entropy gap does not predict authorship for distinctive evaluators (pirate, dragon, Shakespeare); what does is asymmetric -- the evaluator's surprise compared to the Assistant's surprise on the same text, not to the generator's. We rule out the alternative that any persona could play this reference role by trying many candidate substitutes; none does. We interpret the asymmetry as the model performing an implicit Bayesian likelihood-ratio test against the Assistant as the canonical alternative hypothesis, with the persona-vector geometry of \citet{chen2025persona} (every persona a delta off the Assistant) ensuring that the Assistant is the only persona universally accessible to that test.

---


### 81. [Probe Before You Edit: Probing-Guided Molecular Optimization for LLM Agents in Structure-Based Drug Design](https://arxiv.org/abs/2606.00555)

**<font color=#1a73e8>作者：</font>** Zaifei Yang, Weiyu Chen, Yaqing Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Structure-based drug design increasingly employs LLM agents to iteratively refine ligands against a target pocket, yet a viable ligand must satisfy two often-conflicting objectives -- binding affinity and druggability -- which single optimization steps rarely improve together. To quantify this difficulty, we introduce two diagnostic metrics: the first measures how often a single edit improves both objectives, and the second measures how often a gain on one objective comes with a loss on the other. Applying these diagnostics to current LLM-agent pipelines exposes a consistent failure mode: the agent performs molecular editing without knowing how the pocket-ligand complex responds to local modifications, thus rarely achieving joint improvement. Inspired by medicinal chemists, who probe the pocket-ligand complex with controlled analog edits before choosing an optimization direction, we propose \textbf{PROBE}, an optimization framework built around edit-response probing. PROBE first decomposes the ligand into editable sites and builds a pocket-specific \textbf{site map} that flags where joint gains are plausible, where the two objectives are likely in tension, and where liability substructures should be changed; it then performs controlled probe edits whose responses are distilled into an \textbf{EditManual}. Guided by the site map and EditManual, PROBE runs an iterative multi-agent loop in which an affinity agent, a druggability agent, and a co-optimization agent jointly produce edits. On the CrossDocked2020 benchmark, PROBE achieves state-of-the-art performance and substantially mitigates the failure modes exposed by our diagnostics metrics.

---


### 82. [Decomposed On-Policy Distillation for Vision-Language Reasoning: Steering Gradients for Visual Grounding](https://arxiv.org/abs/2606.00564)

**<font color=#1a73e8>作者：</font>** Hee Suk Yoon, Eunseop Yoon, Jaehyun Jang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While on-policy distillation offers dense supervision for training small reasoning models, its optimization dynamics in the multimodal domain remain under-explored. In this work, we challenge the standard monolithic view of Vision-Language Model (VLM) distillation by mathematically decomposing the loss into two distinct components: the language prior and visual grounding. Our analysis uncovers that gradient vectors for these components are nearly orthogonal, indicating that the objective of aligning with the teacher's language distribution is geometrically independent from the objective of matching its visual perception. Consequently, standard optimization passively follows a suboptimal compromise trajectory that implicitly balances the two objectives. Hypothesizing that visual grounding constitutes the primary bottleneck for vision-language reasoning, we introduce Visual Gradient Steering (VGS), a method that dynamically reorients the update vector to prioritize the visual subspace. Experimental results on multiple distillation settings and complex multimodal benchmarks demonstrate that VGS significantly outperforms the standard monolithic formulation of on-policy distillation, achieving superior grounding with minimal training overhead.

---


### 83. [Same Payload, Different Channel: Measuring Trust Asymmetry in Tool-Using Language Models](https://arxiv.org/abs/2606.00566)

**<font color=#1a73e8>作者：</font>** Mohammed Sameer Syed, Rozhin Yasaei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As language models take on agentic roles that span calling external APIs, reading tool outputs, and acting on instructions embedded in third-party content, their attack surface expands well beyond what users type. Whether a model treats a malicious instruction the same way regardless of where it arrives has not been systematically studied. We introduce the Safety Asymmetry Score (SAS), which measures how much a model's susceptibility to adversarial content shifts depending on whether that content arrives in the user message, tool metadata, or tool output, using matched payload pairs that keep the malicious text identical and vary only the context of delivery. Evaluated across 6 production LLMs and three attack families, we find a consistent and informative asymmetry: agent-native models are substantially more vulnerable when adversarial content arrives via tool descriptions than via user messages, while general-purpose models show the reverse. This asymmetry further inverts when the same content is delivered through tool outputs rather than descriptions, suggesting models implicitly treat tool metadata as trusted instructions and tool results as ordinary data. A mechanistic study on Llama 3.3 70B reveals that the safety-relevant representation is causally present at mid-to-late network depths but non-linearly encoded, explaining why linear probes fail to detect it. These findings expose a systematic, channel-dependent blind spot in how current tool-using models handle adversarial content.

---


### 84. [Revisiting Parameter-Based Knowledge Editing in Large Language Models: Theoretical Limits and Empirical Evidence](https://arxiv.org/abs/2606.00570)

**<font color=#1a73e8>作者：</font>** Wanying Ren, Xin Song, Futing Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Parameter-based knowledge editing updates the internal knowledge of large language models (LLMs) via localized weight modifications and has attracted significant attention. However, most existing methods overlook fundamental theoretical limitations and are rarely evaluated under realistic, practice-oriented settings. In this paper, we first present a theoretical analysis based on the dimensional Collapse Hypothesis, explaining how localized parameter edits can propagate along fragile directions in the representation space, inducing global interference and ultimately causing reasoning collapse. Building on this insight, we conduct a comprehensive empirical evaluation by systematically varying knowledge complexity, number of edits, evaluation dimensions, and baseline methods. Our results show that parameter-based editing methods consistently damage core LLM capabilities. In contrast, a simple retrieval-based baseline achieves consistently stronger performance than all parameter-editing methods across all evaluated conditions. These findings highlight that preserving the fundamental capabilities of LLMs after knowledge editing should be a central concern for future research.

---


### 85. [LASER: Loss-Aware Singular-value Decomposition and Rank Allocation for Efficient Low-Precision Vision-Language Models](https://arxiv.org/abs/2606.00573)

**<font color=#1a73e8>作者：</font>** Haiyu Wang, Yutong Wang, Leshu Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) deliver strong multimodal reasoning capabilities, but their large computational cost and high parameter counts make deployment challenging on resource-constrained devices. Low-rank decomposition has emerged as a promising compression technique, yet existing methods often optimize local matrix reconstruction error, rely on uniform or heuristic rank allocation, and focus mainly on attention projections while leaving feed-forward networks underexplored. In this paper, we propose~\textit{LASER} (\textbf{L}oss-\textbf{A}ware \textbf{S}ingular-value d\textbf{E}composition and \textbf{R}ank allocation), a low-rank compression framework for efficient low-precision VLM inference. LASER derives a curvature-weighted SVD objective from a second-order approximation of the model loss and uses Kronecker-factored Fisher information to guide decomposition toward downstream performance rather than reconstruction alone. We further introduce a loss-aware cross-layer rank allocation strategy based on calibration gradients, enabling more effective parameter budgeting across layers. Finally, we extend low-rank compression to FFN layers through a hybrid scheme that combines SVD with quantization. The evaluation results show that LASER achieves more than $2.3\times$ decoding speedup over previous work while preserving strong accuracy under low-precision inference.

---


### 86. [PropLLM: Propagation-Aware Scene Reconstruction for Network Fault Diagnosis](https://arxiv.org/abs/2606.00582)

**<font color=#1a73e8>作者：</font>** Zongzong Wu, Ming Zhao, Fengxiao Tang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Network faults propagate layer by layer along topology and protocol dependencies, yet operations systems typically observe only symptomatic alerts at the tail end of propagation chains, where distinct root-cause faults may produce highly similar end-point symptoms. Existing approaches, whether rule-based, machine learning (ML)-based, or large language model (LLM)-based, fundamentally map the alert set to a diagnosis in a single pass and are structurally incapable of resolving this end-point ambiguity. This paper proposes PropLLM, which is the first to integrate the hop-by-hop scene reconstruction paradigm with the generative reasoning capabilities of LLMs. Starting from end-point alerts, PropLLM traces back hop-by-hop along the propagation path, retrieving verifiable factual evidence from a dual-layer knowledge graph (KG) at each hop, while the proposed Temporal Causal Propagation Attention (TCPA) mechanism encodes known topological causal priors directly into the attention computation to guide the model along the correct causal direction, ultimately localizing the root cause and determining the fault type through a fully evidenced causal chain. On a real-world Wi-Fi multimodal fault dataset, PropLLM improves fault type diagnosis accuracy by 3.9\% and root cause localization accuracy by 4.7\% over the strongest baseline, while reducing the hallucination rate by 50.8\%. Supplementary experiments on the TeleLogs 5G dataset further demonstrate the effectiveness of the proposed method across different network scenarios.

---


### 87. [Improving Visual Representation Alignment Generation with GRPO](https://arxiv.org/abs/2606.00583)

**<font color=#1a73e8>作者：</font>** Shentong Mo, Sukmin Yun  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent diffusion transformers have demonstrated strong image synthesis capabilities but remain inefficient to train due to weak alignment between generative and discriminative representations. While representation alignment frameworks such as REPA improve convergence by aligning noisy denoising features with pretrained visual encoders, their externally supervised alignment loss is static and lacks adaptivity during training and inference. Existing methods rely on fixed cosine alignment or contrastive objectives, which cannot dynamically balance representation consistency and generation quality, resulting in limited discriminative benefit and failing to optimize alignment in a task-adaptive manner. To address this, we propose VRPO, a reinforcement-based optimization strategy that replaces REPA's static alignment loss with a generative representation policy optimization objective. Instead of enforcing a fixed similarity constraint, VRPO treats representation alignment as a reward-guided process: the model receives adaptive rewards based on generation fidelity, perceptual quality, and semantic coherence between the diffusion features and pretrained visual embeddings. This formulation enables the generator to continuously refine its internal representations toward semantically meaningful directions while improving image quality. Our VRPO-driven training seamlessly integrates into diffusion transformers, introducing negligible computation cost and preserving full compatibility with SiT and DiT architectures. Extensive experiments on ImageNet-256x256 demonstrate that our VRPO-Alignment substantially enhances both convergence and fidelity, achieving up to +1.8 FID improvement and 2.3x faster training compared to REPA under identical compute budgets.

---


### 88. [Response-Aware Multimodal Learning for Post-Treatment Visual Acuity Forecasting](https://arxiv.org/abs/2606.00588)

**<font color=#1a73e8>作者：</font>** Phuoc-Nguyen Bui, Van-Vi Vo, Duc-Tai Le 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-term visual acuity (VA) outcomes after anti-VEGF therapy are central to patient counseling, expectation setting, and follow-up planning in diabetic macular edema (DME). However, in clinical practice, physicians must often estimate long-term visual trajectories based only on early post-treatment findings, making reliable prognostication difficult. Although prior OCT-based learning approaches have largely focused on short-term response or single-endpoint prediction, modeling VA trajectories across multiple future time points from early longitudinal observations remains insufficiently explored. In this study, we assembled a real-world cohort of 188 anti-VEGF-treated DME patients with paired baseline and month-1 OCT scans, along with tabular OCT-derived biomarkers and non-imaging clinical variables. Using only these early data, we formulate a multi-horizon VA forecasting problem aimed at predicting visual outcomes at 3, 6, 12, 18, and 24 months, reflecting clinically meaningful follow-up intervals. We propose ReVA, a response-aware multimodal framework that integrates structural features from baseline and month-1 OCT with the tabular variables to capture baseline disease status and early treatment response. ReVA uses spatial attention to preserve localized prognostic imaging features and a dependency-aware tabular encoder to model interactions among clinical variables. These multimodal representations are fused to predict patient-specific long-term visual acuity trajectories. The proposed framework achieves MAE=0.1246, RMSE=0.1621, and R^2=0.6064 for 24-month VA prediction, with consistent performance across all forecast horizons. Our findings show that incorporating early treatment-response signals enables clinically meaningful long-term visual acuity forecasting, supporting data-driven decision support for routine anti-VEGF management.

---


### 89. [Through the PRISM: Principle-Aware, Interpretable, and Multi-Scale Evaluation of Visual Designs](https://arxiv.org/abs/2606.00592)

**<font color=#1a73e8>作者：</font>** Mona Gandhi, KJ Joseph, Srinivasan Parthasarathy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Effective visual communication stems from the harmony of multiple design principles, such as readability, contrast, alignment, overlap, and coherence, which collectively govern clarity and intent of the communicator. While human designers reason holistically over these principles, machine agents typically condense them into a single heuristic score, offering limited interpretability and diagnostic precision. To address this gap, we introduce PRISM (PRinciple-aware, Interpretable, and Structure-guided Design Modifications), a benchmark that systematically perturbs professional layouts from the Crello dataset along measurable design principles. The benchmark comprises 100K perturbed training samples and 10K perturbed validation designs, each isolating a specific principle violation for controlled analysis of multimodal reasoning about design quality. We show that models like Qwen-2.5-VL and GPT-4o-mini are largely insensitive to targeted principle degradations, whereas GPT-4o exhibits global awareness without fine-grained disentanglement. Building on these insights, we propose a multi-scale evaluation framework that integrates lightweight scorers for quantitative assessment, instruction-tuned vision-language models for localised feedback, and prompt-based methods for global reasoning. Our framework provides interpretable explanations of design failures. Using these localised insights, we show targeted refinements that improve layout quality. Together, PRISM and our framework lay the foundation for interpretable design-literate multimodal reasoning systems.

---


### 90. [SPADER: Step-wise Peer Advantage with Diversity-Aware Exploration Rewards for Multi-Answer Question Answering](https://arxiv.org/abs/2606.00593)

**<font color=#1a73e8>作者：</font>** Qiming Shi, Zhaolu Kang, Yunfan Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed as tool-augmented agents to acquire information beyond parametric knowledge. While recent work has improved long-horizon tool-use reasoning, most approaches focus on tasks with a single correct answer. In contrast, many real-world queries require discovering a comprehensive set of valid answers, a setting known as Multi-Answer QA. This setting raises two challenges: fine-grained credit assignment over long search trajectories and reward alignment for sustained exploration beyond easy high-frequency entities. We propose SPADER, a reinforcement learning framework for long-horizon tool use in Multi-Answer QA. SPADER includes Step-wise Peer Advantage (SPA), a critic-free step-level credit assignment mechanism that aligns parallel trajectories by decision step and estimates advantages from peer returns. It also includes a diversity-aware exploration reward that promotes long-tail entity discovery by upweighting rare findings and downweighting redundant ones. Experiments on QAMPARI, Mintaka, WebQSP, and QUEST show that SPADER generally improves recall and overall F1 over prompting-based agents, outcome-supervised RL methods, and recent step-level supervision approaches. Our code and model weights are available at this https URL.

---


### 91. [Toward Responsible and Epistemically Grounded Multilingual LLMs for Computational Social Science and Humanities](https://arxiv.org/abs/2606.00596)

**<font color=#1a73e8>作者：</font>** Wajdi Zaghouani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models have rapidly evolved in multilingual competence and reasoning capacity, enabling their integration into Social Sciences and Humanities research workflows. Yet existing evaluation paradigms remain anchored in task-based NLP benchmarks and fail to address interpretive validity, cultural situatedness, and epistemic mediation. This paper reconceptualizes multilingual reasoning LLMs as hermeneutic instruments that actively structure meaning production across linguistic and cultural contexts. Drawing on hermeneutics, philosophy of technology, science and technology studies, multilingual NLP research, and computational social science methodology, we develop a theoretically grounded framework for evaluating multilingual reasoning in Social Sciences and Humanities (SSH) research. We articulate a rigorous experimental protocol with operationalized metrics for cultural alignment, cross-lingual stability, and reasoning faithfulness, along with transparency requirements tailored to interpretive research tasks. We illustrate the framework through a concrete application scenario involving multilingual political discourse analysis. The paper contributes a conceptual and methodological foundation for responsible integration of multilingual reasoning LLMs into computational social science infrastructures.

---


### 92. [ASAP: Advancing Medical Volumetric Representation Learning with Anatomy-aware Semantically-adaptive Pre-training](https://arxiv.org/abs/2606.00602)

**<font color=#1a73e8>作者：</font>** Rongsheng Wang, Fenghe Tang, Zihang Jiang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning transferable and interpretable representations from medical volumetric scans remains challenging due to complex anatomical structures and weak, heterogeneous supervision provided by radiology reports. In this paper, we propose Anatomy-aware Semantically-Adaptive Pre-training (ASAP), a principled vision-language pre-training framework for fine-grained medical volumetric representation learning from large-scale chest CT scans and their corresponding radiology reports. ASAP integrates three key components: (1) an anatomy-aware knowledge injection module that incorporates organ-level structural priors via off-the-shelf segmentation tool to encourage anatomically coherent representations; (2) a semantically-adaptive selective alignment mechanism that dynamically associates sentence-level findings with localized volumetric regions; and (3) a semantically-adaptive fusion module for effective interaction between anatomically informed visual features and grounded textual cues under dual-modal masked modeling paradigm. Beyond methodological contributions, we establish a comprehensive benchmark for medical volumetric vision-language pre-training on chest CT, covering 15 datasets and 22 downstream tasks spanning abnormality classification, segmentation, disease prognosis prediction, report generation, vocabulary classification, cross-modal retrieval and visual question answering. This benchmark provides standardized evaluation protocols to systematically assess representation quality under diverse clinical settings and data regimes. Extensive experiments demonstrate that ASAP consistently achieves state-of-the-art performance across tasks and datasets, with particularly pronounced gains under limited supervision and distribution shift, validating its effectiveness in learning transferable and clinically meaningful volumetric representations.

---


### 93. [Linguistics-Aware Non-Distortionary LLM Watermarking](https://arxiv.org/abs/2606.00613)

**<font color=#1a73e8>作者：</font>** Shinwoo Park, Hyejin Park, Hyeseon An 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Watermarking should identify language-model output without degrading quality or limiting verification to the model provider. Multilingual deployment makes this harder because morphology, segmentation, and script change where watermark evidence can enter naturally. We introduce LUNA, a linguistically adaptive watermark that combines model-free detection with single-token non-distortion under the standard random-key model. LUNA estimates normalized next-tag entropy from part-of-speech contexts in an external corpus and uses it to set the depth of a non-distortionary binary tournament sampler; the detector reconstructs the same schedule from text, a tokenizer, a tagger, and a secret key. We evaluate six typologically diverse languages and two domains against eight primary baselines. LUNA attains an AUROC of 0.9959 and the lowest mean absolute median perplexity shift of 0.045 across the twelve settings; its 95% bootstrap interval [0.022, 0.073] lies below all baseline intervals. LUNA also records the lowest mean Self-BLEU, Distinct-1, surprisal, and entropy shifts. It is the only method that simultaneously achieves AUROC > 0.99 and an absolute median perplexity shift below 0.1 in a majority of settings, reaching this regime in 9 of the 12 settings while no baseline reaches it in more than 2. Our code is available at: this https URL

---


### 94. [Pause and Think: A Dataset and Benchmark for Video-Grounded Assistive Action Suggestion](https://arxiv.org/abs/2606.00616)

**<font color=#1a73e8>作者：</font>** Shivam Singh, Saptarshi Majumdar, Pratik Prabhanjan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent Vision-Language Models (VLMs) struggle with grounded reasoning, temporal consistency, and context aware planning in videos. We introduce pause-and-think-T, a reasoning-centric training dataset that encourages models to pause, reason over visual evidence, and produce concise, actionable responses. The dataset promotes structured reasoning prior to answer generation, guiding models toward human-like, scene-grounded assistance. We fine-tune a compact 4B-parameter model and evaluate it on our pause-and-think-B benchmark targeting contextual understanding and goal planning tasks. The model achieves 58.0% accuracy at 59x fewer parameters than Qwen3-VL-235B (58.9%), matching GPT-5.2 on scene understanding and surpassing GPT-4o. Beyond our benchmark, it also shows strong out-of-distribution performance on EgoThink and TempCompass, with substantial gains in affordance, assistance, attribution recognition, situated reasoning, and temporal order, without benchmark-specific training. Our results indicate that targeted reasoning supervision enables compact models to deliver actionable, visually grounded guidance while generalizing beyond training data, without requiring large-scale model expansion.

---


### 95. [MemPro: Agentic Memory Systems as Evolvable Programs](https://arxiv.org/abs/2606.00619)

**<font color=#1a73e8>作者：</font>** Qingshan Liu, Guoqing Wang, Wen Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-horizon autonomous agents require memory systems to retain historical information, track evolving states, and reuse relevant knowledge beyond finite context windows. Existing agentic memory systems typically follow a memory construction-retrieval (MCR) pipeline, but often adapt mainly the memory bank while keeping the surrounding pipeline fixed after deployment. This fixed-pipeline design struggles to handle heterogeneous task-specific failure modes and can become misaligned with memory banks that evolve in scale and structure over time. To address these limitations, we propose MemPro, a system-level evolution framework that treats the entire MCR pipeline as an evolvable program rather than adapting only the memory bank or prompt text. MemPro maintains a version tree of runnable memory-system implementations, where an Evolving Agent iteratively selects promising versions, diagnoses recurring failures, and creates improved child versions through failure-mode-guided edit-debug refinement. Experiments on LongMemEval, LoCoMo, HotpotQA, and NarrativeQA show that MemPro consistently outperforms strong static and prompt-level evolving baselines within a few iterations, continues to improve with evolution, and achieves a favorable performance-cost trade-off. Code is available at this https URL.

---


### 96. [MM-Snowball: Evaluating and Mitigating Hallucination Snowballing in Multimodal Multi-Turn Dialogue](https://arxiv.org/abs/2606.00622)

**<font color=#1a73e8>作者：</font>** Yue Jiang, Xue Jiang, Lihua Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) demonstrate remarkable visual understanding, yet their reliability in interactive settings is severely undermined by hallucination snowballing: a phenomenon where initial errors amplify across conversational turns, leading to a collapse in coherence. This failure reveals a fundamental vulnerability where models progressively neglect visual grounding in favor of over-relying on polluted textual history. Existing benchmarks are predominantly confined to single-turn VQA, which fail to capture the complex dynamics of error propagation in long-horizon interactions. To address this, we introduce MM-Snowball, the first benchmark for fine-grained diagnosis of hallucination snowballing within dialogues. Extensive evaluation shows that our benchmark poses a significant challenge even to advanced MLLMs and reveals the inefficacy of existing mitigation methods designed for single-turn VQA. To counteract this degradation, we propose Conflict-Aware Visual Rectification (CAVR). This training-free method mitigates snowballing through a synergistic dual-mechanism that refreshes visual grounding at the representation level and rectifies output distributions at the logit level, effectively re-anchoring the model to visual facts. Experiments demonstrate that CAVR achieves state-of-the-art performance, offering a promising path toward more reliable interactive AI. Data and code are available at: this https URL

---


### 97. [Hidden Thoughts Are Not Secret: Reasoning Trace Exposure in LLMs](https://arxiv.org/abs/2606.00642)

**<font color=#1a73e8>作者：</font>** Yu-An Lu, Ci-Yang Tsai, Yu-Lin Tsai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reasoning traces have become a valuable form of learning signals for improving and transferring the capabilities of large language models. In particular, detailed traces can help distill reasoning behavior from stronger teacher models into weaker student models. The value of capability transfer has motivated many deployed systems with reasoning models to hide raw internal traces and expose at most summaries and answers to users. As a result, we ask whether such interface-level trace hiding prevents users from obtaining useful reasoning supervision through prompting. We study this question with Reasoning Exposure Prompting (REP), a lightweight in-context elicitation method that uses shadow-model-generated demonstrations wrapped in auxiliary code-like formats to raise user-visible reasoning traces from a victim model. Across the common reasoning dataset, different victim models, and different student model distillation, REP substantially increases similarity between exposed and REP-conditioned internal traces while preserving useful reasoning signals.

---


### 98. [ForeSci: Evaluating LLM Agents for Forward-Looking AI Research Judgment](https://arxiv.org/abs/2606.00644)

**<font color=#1a73e8>作者：</font>** Qiuyu Tian, Zequn Liu, Yingce Xia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI research often requires decisions before future evidence exists: which bottleneck to attack, which direction to pursue, or where a project should be positioned. We introduce ForeSci, a temporally controlled benchmark for evaluating whether LLM agents can make such forward-looking research judgements from historical evidence. ForeSci contains 500 tasks across four fast-moving AI domains and four decision families. Each task is paired with a cutoff-aligned offline knowledge base; post-cutoff papers are hidden during generation and used only for validation. To avoid random future-event prediction, tasks are derived from pre-cutoff taxonomy branches and evidence signals, and answer-generation backbones are selected to precede the task cutoffs. We evaluate native LLMs, Hybrid RAG, and three research-agent adaptations across four backbones. Results show that explicit evidence organization improves traceability and factual support, but gains depend strongly on the decision family. Diagnostics reveal a recurring evidence-decision decoupling: agents may cite relevant evidence while forecasting the wrong research object. ForeSci turns forward-looking AI research judgement into a controlled benchmark for evaluating research agents as decision-making systems.

---


### 99. [LinguIUTics at PsyDefDetect: Iterative Imbalance-Aware Fine-tuning of Qwen3-8B for Psychological Defense Mechanism Classification](https://arxiv.org/abs/2606.00647)

**<font color=#1a73e8>作者：</font>** Shefayat E Shams Adib, Ahmed Alfey Sani, Md Hasibur Rahman Alif 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Detecting psychological defense mechanisms in conversational text remains a challenging clinical NLP problem. For the PsyDefDetect 2026 shared task (nine-class utterance classification evaluated via macro F1), our team LinguIUTics achieves a macro F1-score of 0.3917 on the official positive-class leaderboard, ranking 4th out of 21 registered teams and improving over the Ministral-8B task baseline (31.48 macro F1) by 7.7 absolute points (24.4 percent relative). BERT-family encoders and zero-shot LLMs proved ineffective on rare classes due to severe class imbalance, leading us to QLoRA fine-tuning of Qwen3-8B. We leverage three key strategies: grouped stratified cross-validation (preventing leakage), minority-class round-robin lexical augmentation, and a post-processing pipeline with logit bias tuning and ensemble blending. Together, these components close much of the validation-to-leaderboard gap and substantially improve minority-class recall, driving the critical "Unclear" class (Level 8) from near-zero performance to an F1 score of 0.797.

---


### 100. [MESA: Improving MoE Safety Alignment via Decentralized Expertise](https://arxiv.org/abs/2606.00651)

**<font color=#1a73e8>作者：</font>** Yitong Sun, Yao Huang, Teng Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) architectures scale Large Language Models (LLMs) efficiently, enabling greater capacity with reduced computational cost by dynamically routing inputs to relevant experts, yet introduce a critical vulnerability: Safety Sparsity, where safety capabilities concentrate in few experts, making them susceptible to adversarial bypassing. Meanwhile, conventional alignment methods uniformly adapt all parameters, ignoring their functional differences and inadvertently degrading performances. To address these challenges, we propose MESA (MoE Safety Alignment), a targeted alignment framework for MoE-based LLMs that strategically decentralizes safety responsibility to maximize coverage while minimizing interference with utility. Based on Optimal Transport (OT) theory, MESA operates through two mechanisms: (1) Expert Capacity Reallocation uses a transport cost matrix to distribute safety duties to the most cost-effective experts, and (2) Dynamic Routing Refinement constrains the router to precisely activate these decentralized modules. Experiments show that MESA achieves robust defensive performance against varied harmful benchmarks while preserving helpfulness. Code is available at this https URL.

---


> [!TIP]
> 当前位于：**51-100**（第 2/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-376](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
