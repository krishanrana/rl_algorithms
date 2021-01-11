agent = dict(
    type="ACERAgent",
    hyper_params=dict(
        gamma=0.98,
        c=1,
        n_rollout=10,
        buffer_size=5000,
        sequence_size=10,
        overlap_size=5,
        replay_ratio=16,
        start_from=1000,
        n_step=1,
    ),
    learner_cfg=dict(
        type="ACERLearner",
        backbone=dict(),
        head=dict(
            type="ACERHead",
            configs=dict(hidden_sizes=256, output_activation="identity",),
        ),
        optim_cfg=dict(lr=0.0002, weight_decay=0.0),
    ),
)
