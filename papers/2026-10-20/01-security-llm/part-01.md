# 🔐 大模型安全相关研究 | 2026年10月20日

> 本类共 **14** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [The Model Knows Better: Defending Medical Multi-Agent Systems Against Prompt Injection](https://arxiv.org/abs/2610.22594)

**<font color=#1a73e8>作者：</font>** Fardin Ahsan Sakib, Ziwei Zhu, Ozlem Uzuner  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Medical multi-agent systems, in which LLM agents discuss a case, are increasingly studied for clinical decision support. Prompt injection, text that an attacker adds to a model's input, can manipulate LLMs into wrong decisions. How it affects these systems, and how to protect them, remains unclear. Across two systems, two model families and three benchmarks, a single injected passage succeeds in up to 61% of cases, and collaboration does not consistently protect against it. Existing defenses help only partly: they miss injections that look like ordinary clinical text. Yet when asked to check the injected text against the patient's findings, a model that followed the injection usually rejects it. We therefore propose a training-free defense that verifies the clinical judgments behind the system's decision. Following clinical practice, it separates the patient's findings from clinical judgments, such as diagnoses, recommendations and instructions, and checks each judgment against the findings alone, so the decision rests only on supported judgments. Our defense outperforms all baselines on every benchmark, lowering attack success on MedQA to 4-7% while maintaining accuracy on cases without an attack, and remains effective with a medical model and against defense-aware and adaptive attacks.

---


### 2. [SAFETYEDIT: Sparse Internal Targets with Prompt-Wide Control for LLM Jailbreak Backdoors](https://arxiv.org/abs/2610.22640)

**<font color=#1a73e8>作者：</font>** Yutong Ke, Yansu Wang, Zeyu Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Model-editing backdoors aim to induce harmful responses under a trigger while preserving ordinary behavior on untriggered input. Recent model-editing approaches target affirmative response prefixes through rank-one updates to a small subset of model weights. Yet when this prefix-level target is satisfied, the model may still revert to refusal or produce a coherent, apparently compliant response that does not address the request. To overcome this limitation, existing internal-representation approaches shift focus from output tokens to dense, high-dimensional compliance directions in latent space. Existing representation-level approaches rely on preservation constraints to maintain conditionality, motivating us to ask whether a smaller internal target can offer a different effectiveness-preservation trade-off. Motivated by the comparable control capability of single-coordinate interventions, we investigate a sparse refusal-related MLP coordinate as this target. We propose SAFETYEDIT, which optimizes a single refusal-related coordinate and uses KV-cache marking in early attention layers to propagate a prefix-trigger signal across subsequent instruction positions. On some checkpoints a downstream MLP reader converts this signal into control of the coordinate, while on others the propagated signal alone suffices; the method is defined by the sparse target rather than by a fixed writer-reader pair. Across four open-weight LLMs and three dataset groups, SAFETYEDIT achieves the highest triggered Guard ASR in 11 of 12 comparisons and the highest mean StrongREJECT score in all 12, relative to the baselines evaluated for each model. Crucially, comprehensive ablation and behavioral audits confirm generally minimal changes in untriggered behavior and general capabilities in the tested configurations.

---


### 3. [Refusal Is Not Robustness: Measuring Harmful Reachability in Autoregressive Language Models](https://arxiv.org/abs/2610.22754)

**<font color=#1a73e8>作者：</font>** Parv Kapoor, Teresa Fortes, Claudia Mamede 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM safety evaluations via jailbreaking typically index on attack success rate (ASR): whether a generated response violates safeguards. However, ASR only evaluates sampled outputs and provides little information on the underlying generation process. Autoregressive language models define distributions over possible outputs, and a sampled refusal can coexist with substantial probability mass on harmful generation paths. We study this hidden structure through bounded continuation analysis (BCA), which models autoregressive generation as a stochastic process over token prefixes and computes the finite-horizon probability that generation reaches a harmful continuation. BCA constructs a bounded continuation tree, labels terminal continuations with a semantic harm evaluator, and estimates harmful reachability using exact probabilistic model checking. BCA complements ASR by measuring how much harmful behavior remains accessible beneath a sampled safe response. This makes it useful for distinguishing models that look identical under measured ASR values, and allocating red-team effort toward regions of the generation process with greater hidden risk. Across four instruction-tuned LLMs and 100 JailbreakBench behaviors, we show that BCA effectively quantifies hidden harmful behavior and provides a useful signal to guide red teaming.

---


### 4. [Prune the Leaky Neurons: Mitigating Private Data Leakage in Fine-Tuned LLMs via Joint-Embedding-Guided Pruning](https://arxiv.org/abs/2610.22792)

**<font color=#1a73e8>作者：</font>** Mohamed Shaaban, Mohamed Elmahallawy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fine-tuning large language models (LLMs) on proprietary records enables domain adaptation but introduces two challenges: (i) privacy leakage of memorized private data, such as personally identifiable information (PII), and (ii) balancing private data removal with utility preservation. Existing defenses, including data sanitization and differential privacy, often degrade performance, while privacy-neuron editing lacks a PII-free reference to distinguish identity-specific neurons from those supporting useful text. We propose JEPA-Prune, a post-hoc neuron pruning framework guided by a model trained exclusively on PII-free views. Alongside the fine-tuned private model, JEPA-Prune, trains a public model on surrogate and masked views of the same records using a joint-embedding predictive architecture (JEPA), capturing domain knowledge without identifiers. A cross-model representation probe quantifies deviations between private representations of leaked records and this PII-free reference. Integrated gradients and a scale-invariant specificity score then identify PII-responsive neurons, which are pruned without retraining. Experiments show that pruning just 1.6% of neurons reduces PII inference accuracy by up to 7.4x and PII extraction recall by up to 13.9x, while keeping unseen-text perplexity within 16% of that of the unpruned model for most LLMs. In contrast, privacy-neuron editing increases perplexity by at least 26x.

---


### 5. [Stealthy Poisoning Attacks via Reused KV Cache of Reasoning](https://arxiv.org/abs/2610.22873)

**<font color=#1a73e8>作者：</font>** L. Zhu, Y. Jung, S. Szyller  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern large language model (LLM) systems reuse key-value (KV) caches to accelerate inference. Recent work has shown that reusing KV caches from reasoning traces can also improve task performance, similar to retrieval-augmented generation (RAG). We demonstrate that this form of KV cache reuse introduces new poisoning vulnerabilities. We propose R$^2$ECAP (Reused Reasoning-Cache Poisoning), a black-box attack that plants poisoned reasoning traces solely through interactions with a system's chat interface. R$^2$ECAP constructs two traces: a preceding trace that steers the model toward an adversarial target and a retained trace that carries this target. Because the retained trace is generated conditioned on the preceding trace, its KV cache preserves residual adversarial influence, even after the preceding trace and its cache entries are discarded. We evaluate R$^2$ECAP on three open-weight LLMs and three datasets. R$^2$ECAP achieves up to 79% attack success rate (ASR) and outperforms HijackKV, a state-of-the-art white-box KV poisoning attack, in 8 of 9 resource-constrained settings. It also achieves 46% ASR in a realistic reasoning-trace retrieval system. Finally, R$^2$ECAP remains stealthy, with only 1% of its retained responses detected by a popular prompt injection detector.

---


### 6. [Identify, Classify, Act: Per-Instruction Controlled Compliance for LLMs over External Data](https://arxiv.org/abs/2610.22874)

**<font color=#1a73e8>作者：</font>** Zesheng Shi, Xue Li, Chenrui Dai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs over external data face a per-instruction tension: a single document or tool return often interleaves legitimate directives with adversarial prompt injections, and the model must follow the former while rejecting the latter. Existing defenses suppress or trust all external instructions, collapsing the safety-utility frontier and forcing a choice between over-refusal and over-compliance. We argue the missing capability is \textbf{per-instruction credit attribution} and formalize it as External-Data Instruction Classification, an identify-classify-act decision over each embedded directive. We propose \textbf{EDIC}, a decomposed reward framework for per-instruction compliance. A scene-grounded pipeline injects mixed beneficial and harmful instructions with counterfactual filtering, while a generative judge is initialized by SFT and refined with GRPO to attribute compliance at the instruction level. The judge then produces a reward that separately encourages beneficial compliance and penalizes harmful compliance for RL training. Across two backbones and five benchmarks, EDIC improves both safety and utility over the strongest prior defense, lifting harmful-rejection by up to 7.7\% and Arena-Hard-Auto utility by 12.5\% on Qwen3-4B. The code repository is hosted at this https URL.

---


### 7. [Multiple Turns, Short Horizons: Measuring Effective-Horizon Compression in Jailbreaks](https://arxiv.org/abs/2610.22928)

**<font color=#1a73e8>作者：</font>** Zhipeng Wei, Michael Lee, N. Benjamin Erichson  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-turn jailbreaks use feedback from a victim large language model to adapt their queries over several turns. However, once an effective trajectory has been found, it is unclear how much of the earlier query history is still needed. In this work, we study this by removing early attacker queries and running the remaining queries again in a new conversation while regenerating the victim's responses. We define the effective horizon as the shortest remaining query sequence that recovers the same attack progress. Empirically, we find that roughly half of the original query sequence is sufficient on average to recover the same attack progress. We call this phenomenon effective-horizon compression. We show that this shorter history can recover the best point reached during an unsuccessful attack and provide a better starting point for continuing the attack. It also helps identify which earlier queries should receive less learning signal during attacker training, and downweighting those queries improves performance. We further find that short reward-propagation windows preserve calibrated defense performance close to full-trajectory returns. These results show that multi-turn attacks can contain more queries than are needed to recover the progress reached later in the interaction.

---


### 8. [ECHO: Replacing the Compliance Proxy with Response Harmfulness in Optimization-Based Jailbreak Attack](https://arxiv.org/abs/2610.23030)

**<font color=#1a73e8>作者：</font>** Yuanwei Wu, Lingdong Huang, Yunlong Mao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Despite extensive safety alignment, large language models remain vulnerable to jailbreak attacks. Existing optimization-based attacks share a single objective: maximize a token-level proxy of victim compliance---such as the likelihood of an affirmative prefix---computed on the prompt rather than the decoded reply. This proxy cannot distinguish a cautious hedge from a fully actionable harmful answer, leaving the search blind to what the model actually says. We propose ECHO (Evaluation-Conditioned Harmfulness Optimization), which replaces the compliance proxy with response-level, continuous harmfulness scores from HarmSig, a 1.7B regressor grounded in actual harmful capability. ECHO couples HarmSig with five word-level perturbation operators and Keyword-Anchored Beam Search with global top-m memory, under a strict black-box threat model. Across five open-weight victims on AdvBench, ECHO achieves up to 0.898 StrongREJECT mean score and 89.23% HarmBench success. Our code is publicly available at this https URL.

---


### 9. [Rethinking GRPO for Large Reasoning Model Safety Alignment](https://arxiv.org/abs/2610.23085)

**<font color=#1a73e8>作者：</font>** Jiawei Chen, Yi Zhang, Jiawei Du 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large reasoning models (LRMs) exhibit strong reasoning capabilities but remain vulnerable to unsafe outputs. While Group Relative Policy Optimization (GRPO) is widely used for safety alignment, its group-relative optimization may provide insufficient safety-directed learning signals. In this paper, we identify two failure modes: advantage collapse, where homogeneous rollout groups yield vanishing advantages, and unsafe diversification, where unsafe behaviors persist and become increasingly diverse. Our theoretical analysis reveals that behavioral consistency weakens within-group safety contrasts, while entropy regularization can diversify unsafe responses when relative signals vanish. To address these challenges, we propose Beacon, comprising Safety Signal Recovery (SSR) and Safety-Utility Decoupled Alignment (SUDA). SSR combines advantage-guided trajectory filtering and safe reference supervision to recover effective safety learning signals, while SUDA employs category-aware rewards and benign-only KL anchoring to mitigate over-refusal without compromising safety. Experiments across four Qwen3 and DeepSeek-R1-Distill variants and eight benchmarks show that our framework achieves the best average safety and reasoning performance, reducing average safety error by up to 32.83 percentage points while maintaining low over-refusal.

---


### 10. [Trojan Horse: Automated Repository Poisoning against Coding Agents](https://arxiv.org/abs/2610.23109)

**<font color=#1a73e8>作者：</font>** Xiao Yang, Jinchang Hou, Jiawei Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Coding agents are increasingly capable with autonomy, which exposes them to repository-level poisoning. Existing red-teaming studies remain restricted to manual selection for malicious payload locations and fixed disguise strategies, which cannot represent realistic repository poisoning. We present TrojanForge, the first automated framework for repository poisoning. TrojanForge parses repository structure through abstract syntax trees (AST) and maps agent execution traces onto AST nodes. A security review agent ranks these candidates and selects the least conspicuous ones for payload mounting. Then, through adversarial play with the target agent, TrojanForge iteratively refines disguise strategies by inverting the causes of agent detection, and transfers accumulated success experience across repositories. We further construct TrojanBench, a benchmark of 384 poisoned repositories spanning 6 domains and 9 programming languages. Extensive experiments show that TrojanForge achieves a stable poisoning success rate of over 60% with backdoor injection exceeding 90%. Comprehensive evaluation on TrojanBench across 4 harnesses and 12 models reveals that even commercial agents fail to defend against repository-level poisoning.

---


### 11. [Ignored, Not Refused: What Low Prompt-Injection Success Rates Hide in Small Tool-Using Agents](https://arxiv.org/abs/2610.23254)

**<font color=#1a73e8>作者：</font>** Farhan Zarif, Kazi Shahid Ahmed Galib, Synthia Akter Promi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tool-using agents read untrusted external content, which exposes them to indirect prompt injection (IPI), where hidden instructions hijack the agent's tool calls. Benchmarks measure IPI security by the attack success rate (ASR), which treats every failed attack as a successful defense. To test this assumption, we audit 33,000 trajectories from eleven open-weight agents (2-14B parameters) on InjecAgent and AgentDojo. A label-blind LLM judge shows that most failed attacks are ignored (76-80%) rather than refused (17-18%). With identical model weights, changing only the system prompt shifts InjecAgent ASR from 0.2% to 43%. Our Attack-Task Outcome Matrix (ATOM) further shows that in 21.7% of AgentDojo episodes, the agent stayed safe but did not complete the user's task. A low ASR therefore mostly reflects agents silently ignoring injections, not refusing them. Evaluations should report how attacks fail and whether the user's task is completed, alongside ASR. We release the labeled corpus, judge prompt, and analysis code.

---


### 12. [MobileJailBench: Red Queen Jailbreak Benchmarking for Mobile Agents](https://arxiv.org/abs/2610.23303)

**<font color=#1a73e8>作者：</font>** Songping Wang, Borui Li, Qinglong Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> MLLM-based mobile agents are rapidly gaining autonomy in perception, planning, and closed-loop execution in dynamic mobile environments. However, this autonomy also broadens the attack surface and amplifies the risks of malicious misuse, including privacy leakage, device compromise, and large-scale phishing. Existing jailbreak evaluations leave three critical gaps for mobile agents: they focus on conversational attacks instead of mobile workflows, use static task sets with fixed difficulty, and rely narrowly on attack success rate rather than comprehensive security assessment. To close these gaps, we present MobileJailBench, the first evolving jailbreak benchmark for mobile agents, comprising three key components: (1) a benchmark comprising 520 tasks spanning three jailbreak paradigms and 14 risk categories, built on a high-fidelity mobile sandbox that we construct, enabling realistic workflows across over 20 widely used apps; (2) Dual-Dynamic Evolution, which combines Failure-Distilled Jailbreak Evolution with Weakness-Driven Benchmark Expansion; and (3) Stratified Adjudication Framework for assessing security awareness, execution behavior, and risk consequences. Extensive experiments show that current mobile agents are particularly vulnerable to implicit jailbreaks, as their safety alignment remains largely superficial and fails to generalize from conversational refusal to dynamic mobile interactions. Moreover, our dynamic evolution mechanism sharpens practical threat boundaries by continually uncovering new vulnerabilities, reaching a 100% ASR on Qwen3.5-122B. MobileJailBench provides a reproducible, continuously evolving framework for tracking the true security boundaries of mobile agents.

---


### 13. [Monitor-Validity Failures: LLM Safety Evidence Paths at Evolving Framework Boundaries](https://arxiv.org/abs/2610.23362)

**<font color=#1a73e8>作者：</font>** Junchi Liao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern LLM applications rely on runtime monitors that inspect tool calls, traces, streams, detector outputs, and verifier inputs. This creates an interface-reliability problem: a framework path may remain operational while policy-relevant evidence never reaches its decision point. In one representative case, a regex detector returned a positive match, but the framework stranded the result before the block decision. This differs from jailbreaks and detector errors because the evidence is already recognized yet disconnected from enforcement. We study this repair-boundary signature with canary contracts: parent/fixed confirmation units that place a known payload only on the changed evidence surface and record monitor visibility together with the downstream decision for action-boundary cases. Applying the protocol to public framework repairs, we confirm 18 evidence-path failures across 11 LLM or agent safety project groups and four implementation ecosystems. Nine are established-boundary repairs, eight are new-surface policy-coverage gaps, and one is a boundary-only evidence case. Fourteen reach E1 enforcement boundaries: seven native action outcomes, six configured enforcement boundaries, and one synthetic-consumer consequence. The remaining cases affect verifier, safety-prompt, or observability channels. The cases form carrier, adapter, authority, and surface families and show how ordinary application behavior can remain intact while a safety-specific evidence path misses its decision. Exact revisions, deterministic outcomes, negative controls, and a frozen prospective audit document the confirmation rule. Monitor assumptions therefore need regression tests at the schemas, streams, tools, and adapters that frameworks evolve.

---


### 14. [RedDarwin: Evolving Jailbreak Skills against Frontier LLMs](https://arxiv.org/abs/2610.23726)

**<font color=#1a73e8>作者：</font>** Zhouyuan Ma, Yutao Wu, Hanxun Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Red teaming must continually adapt as frontier LLM safeguards evolve, yet existing approaches largely search for adversarial prompts or optimize within fixed attack procedures. We observe that even when an attack becomes ineffective, its underlying mechanisms can remain useful and can be revised or recombined to construct stronger attacks. Based on this insight, we introduce RedDarwin, an agentic framework that shifts the unit of jailbreak evolution from prompts and fixed attacks to executable attack skills. RedDarwin consists of 47 reusable base skills and autonomously revises, composes, executes, and selects them using target-model feedback, allowing successful discoveries to become building blocks for subsequent evolution. RedDarwin produces 65 evolved skills, improving 44 of 47 base attacks and increasing their mean attack success rate (ASR) on AdvBench from 18.8% to 47.3%. These evolved skills consistently outperform baselines on the held-out StrongREJECT and frontier LLMs unseen during evolution; with only 10 target-model queries, RedDarwin achieves 100% ASR on GPT-5.6-Sol, 92% on Claude-Sonnet-5, and 80% on Gemini-3.8-Flash. Analysis of the evolution trajectories further shows that strong attacks often emerge from novel combinations of reusable mechanisms rather than from individually dominant ones. We believe this paradigm can accelerate adaptive red teaming and inform stronger safeguards, creating complementary value for both safety evaluation and defense.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
